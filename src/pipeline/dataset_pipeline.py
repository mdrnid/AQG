"""
AQG Dataset Pipeline Runner
Jalankan: python run_pipeline.py --help
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from tqdm import tqdm

from src.dataset.chunker import chunk_all_materials, chunk_markdown
from src.dataset.concept_list import CONCEPTS, get_concepts_for_module
from src.dataset.dataset_writer import write_dataset
from src.dataset.prompt_constructor import TaskParams, build_prompt
from src.dataset.synthetic_generator import _build_llm_client, generate_datapoint
from src.dataset.validator import (
    RawDataPoint,
)


# ── Checkpoint helpers ────────────────────────────────────────────────────────

def _load_checkpoint(checkpoint_path: Path) -> set[str]:
    """Load set of completed section names from checkpoint file."""
    if not checkpoint_path.exists():
        return set()
    completed = set()
    with open(checkpoint_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entry = json.loads(line)
                completed.add(entry["section"])
    return completed


def _save_checkpoint(checkpoint_path: Path, section: str, count: int) -> None:
    """Append completed section to checkpoint file."""
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    with open(checkpoint_path, "a", encoding="utf-8") as f:
        f.write(json.dumps({"section": section, "count": count}) + "\n")


def _save_failures(failures_path: Path, failures: list[dict]) -> None:
    """Append validation failures to JSONL file."""
    failures_path.parent.mkdir(parents=True, exist_ok=True)
    with open(failures_path, "a", encoding="utf-8") as f:
        for entry in failures:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _load_accumulated(output_dir: Path) -> list[dict]:
    """Load all accumulated data points from partial output files."""
    accumulated = []
    partial_file = output_dir / "accumulated.jsonl"
    if partial_file.exists():
        with open(partial_file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    accumulated.append(json.loads(line))
    return accumulated


def _append_accumulated(output_dir: Path, datapoints: list) -> None:
    """Append valid data points to accumulated JSONL."""
    partial_file = output_dir / "accumulated.jsonl"
    partial_file.parent.mkdir(parents=True, exist_ok=True)
    with open(partial_file, "a", encoding="utf-8") as f:
        for dp in datapoints:
            record = {"input": dp.input, "target": dp.target, "metadata": dp.metadata}
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ── Main pipeline ─────────────────────────────────────────────────────────────

def run_pipeline(
    materi_dir: str,
    output_dir: str,
    max_per_chunk: int = 2,
    section_filter: str | None = None,
    difficulties: list[str] | None = None,
    question_types: list[str] | None = None,
    dry_run: bool = False,
) -> None:
    """
    Jalankan pipeline lengkap: chunk → prompt → generate → validate → write.

    Args:
        materi_dir: direktori materi Markdown
        output_dir: direktori output dataset
        max_per_chunk: jumlah soal per chunk (default 2)
        section_filter: nama folder section untuk diproses (None = semua)
        difficulties: list difficulty yang digunakan (default: easy, medium, hard)
        question_types: list question type (default: MCQ)
        dry_run: jika True, skip LLM call (untuk testing pipeline)
    """
    if difficulties is None:
        difficulties = ["easy", "medium", "hard"]
    if question_types is None:
        question_types = ["MCQ"]

    materi_path = Path(materi_dir)
    output_path = Path(output_dir)
    checkpoint_path = output_path / "checkpoint.jsonl"
    failures_path = output_path / "validation_failures.jsonl"

    output_path.mkdir(parents=True, exist_ok=True)

    # Load checkpoint
    completed_sections = _load_checkpoint(checkpoint_path)
    if completed_sections:
        print(f"[INFO] Melanjutkan dari checkpoint. Section selesai: {completed_sections}")

    # Temukan semua section (subfolder)
    if section_filter:
        sections = [materi_path / section_filter]
    else:
        sections = sorted([p for p in materi_path.iterdir() if p.is_dir()])

    if not sections:
        print(f"[ERROR] Tidak ada section ditemukan di {materi_dir}")
        sys.exit(1)

    # Build LLM client sekali
    llm_client = None if dry_run else _build_llm_client()

    total_generated = 0
    total_failed_llm = 0

    for section_path in sections:
        section_name = section_path.name

        if section_name in completed_sections:
            print(f"[SKIP] {section_name} (sudah selesai)")
            continue

        print(f"\n{'='*60}")
        print(f"[SECTION] {section_name}")
        print(f"{'='*60}")

        # Chunk semua file di section ini
        md_files = sorted(section_path.rglob("*.md"))
        if not md_files:
            print(f"[WARNING] Tidak ada file .md di {section_path}")
            continue

        all_chunks = []
        for md_file in md_files:
            try:
                chunks = chunk_markdown(str(md_file))
                all_chunks.extend(chunks)
            except Exception as e:
                print(f"[WARNING] Gagal chunk {md_file.name}: {e}")

        print(f"[INFO] {len(all_chunks)} chunks dari {len(md_files)} file")

        # Ambil konsep untuk section ini
        concepts = get_concepts_for_module(section_name)
        if not concepts:
            # Fallback: gunakan nama section sebagai konsep
            concepts = [section_name.replace("-", " ").title()]
        print(f"[INFO] {len(concepts)} konsep: {concepts[:3]}{'...' if len(concepts) > 3 else ''}")

        # Build prompt inputs
        prompt_inputs = []
        for chunk in all_chunks:
            # Pilih max_per_chunk kombinasi per chunk
            combos = []
            for diff in difficulties:
                for qt in question_types:
                    for concept in concepts[:3]:  # max 3 konsep per chunk
                        combos.append((concept, diff, qt))
                        if len(combos) >= max_per_chunk:
                            break
                    if len(combos) >= max_per_chunk:
                        break
                if len(combos) >= max_per_chunk:
                    break

            for concept, diff, qt in combos[:max_per_chunk]:
                try:
                    params = TaskParams(concept=concept, difficulty=diff, question_type=qt)
                    prompt_inputs.append(build_prompt(chunk, params))
                except ValueError:
                    pass

        print(f"[INFO] {len(prompt_inputs)} prompt inputs akan di-generate")

        # Generate data points — incremental save per data point
        failed_llm = 0
        section_valid_count = 0

        for prompt_input in tqdm(prompt_inputs, desc=f"Generating {section_name}", unit="soal"):
            if dry_run:
                raw_dp = RawDataPoint(
                    input=prompt_input.input,
                    target=(
                        f"Pertanyaan: Contoh soal tentang {prompt_input.params.concept}? "
                        f"Jawaban benar: Jawaban contoh. "
                        f"Distraktor: 1) Pilihan A 2) Pilihan B 3) Pilihan C 4) Pilihan D"
                    ),
                    metadata={
                        "difficulty": prompt_input.params.difficulty,
                        "question_type": prompt_input.params.question_type,
                        "concept": prompt_input.params.concept,
                        "misconception_tags": [],
                        "source_file": prompt_input.chunk.source_file,
                        "section": prompt_input.chunk.section_heading,
                        "source": "dry_run",
                        "validated": False,
                    },
                    source="dry_run",
                )
                result_dp = raw_dp
            else:
                result_dp = generate_datapoint(prompt_input, llm_client, max_retries=2)

            if result_dp is None:
                failed_llm += 1
                continue

            # Validate dan simpan langsung ke disk — tidak tunggu section selesai
            from src.dataset.validator import validate, ValidDataPoint
            val_result = validate(result_dp)
            if val_result.is_valid:
                valid_dp = ValidDataPoint(
                    input=result_dp.input,
                    target=result_dp.target,
                    metadata=result_dp.metadata,
                )
                _append_accumulated(output_path, [valid_dp])
                section_valid_count += 1
            else:
                _save_failures(failures_path, [{
                    "reasons": val_result.failure_reasons,
                    "raw_datapoint": {
                        "input": result_dp.input[:200],
                        "target": result_dp.target[:200],
                        "metadata": result_dp.metadata,
                    },
                }])

        print(f"[RESULT] Valid: {section_valid_count}, Failed LLM: {failed_llm}")

        # Save checkpoint setelah section selesai
        _save_checkpoint(checkpoint_path, section_name, section_valid_count)

        total_generated += section_valid_count
        total_failed_llm += failed_llm

    # Final: load semua accumulated dan write final splits
    print(f"\n{'='*60}")
    print(f"[FINAL] Total valid data points: {total_generated}")
    print(f"[FINAL] Total LLM failures: {total_failed_llm}")

    accumulated_raw = _load_accumulated(output_path)
    if not accumulated_raw:
        print("[WARNING] Tidak ada data yang berhasil di-generate.")
        return

    # Konversi ke ValidDataPoint untuk writer
    from src.dataset.validator import ValidDataPoint
    valid_all = [
        ValidDataPoint(input=r["input"], target=r["target"], metadata=r["metadata"])
        for r in accumulated_raw
    ]

    info = write_dataset(valid_all, output_dir)
    print(f"\n[DONE] Dataset disimpan ke {output_dir}")
    print(f"  Train: {info['splits']['train']}")
    print(f"  Validation: {info['splits']['validation']}")
    print(f"  Test: {info['splits']['test']}")
    print(f"  Total: {info['total']}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="AQG Dataset Pipeline — generate dataset dari materi Markdown"
    )
    parser.add_argument(
        "--materi-dir", default="dataset_aqg/materi",
        help="Direktori materi Markdown (default: dataset_aqg/materi)"
    )
    parser.add_argument(
        "--output-dir", default="dataset_aqg/output",
        help="Direktori output dataset (default: dataset_aqg/output)"
    )
    parser.add_argument(
        "--max-per-chunk", type=int, default=2,
        help="Jumlah soal per chunk (default: 2)"
    )
    parser.add_argument(
        "--section", default=None,
        help="Nama folder section untuk diproses (default: semua)"
    )
    parser.add_argument(
        "--difficulties", nargs="+", default=["easy", "medium", "hard"],
        choices=["easy", "medium", "hard"],
        help="Difficulty levels (default: easy medium hard)"
    )
    parser.add_argument(
        "--question-types", nargs="+", default=["MCQ"],
        choices=["MCQ", "Code Completion"],
        help="Question types (default: MCQ)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Jalankan pipeline tanpa LLM (untuk testing)"
    )

    args = parser.parse_args()

    run_pipeline(
        materi_dir=args.materi_dir,
        output_dir=args.output_dir,
        max_per_chunk=args.max_per_chunk,
        section_filter=args.section,
        difficulties=args.difficulties,
        question_types=args.question_types,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
