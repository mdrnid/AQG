"""
Domain Adaptation Dataset Pipeline
Mengubah materi Markdown menjadi dataset JSONL untuk domain adaptation IndoT5.

Format yang didukung:
- span_corruption : gaya T5 pre-training, zero LLM cost
- qa_generic      : ekstrak QA dari bold/inline code/heading, zero LLM cost
- summarization   : ringkasan via LLM (opsional, butuh API key)
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from tqdm import tqdm

from src.dataset.step2.chunker import Chunk, chunk_all_materials, chunk_markdown
from src.dataset.step1.formatter import (
    RawDomainDataPoint,
    corrupt_spans,
    extract_qa_pairs,
    summarize_chunk,
)
from src.dataset.step1.validator import (
    ValidDomainDataPoint,
    validate_domain_batch,
    domain_validation_report,
)
from src.dataset.step1.dataset_writer import write_domain_dataset


# ---------------------------------------------------------------------------
# Checkpoint helpers
# ---------------------------------------------------------------------------

def _load_checkpoint(checkpoint_path: Path) -> set:
    """Load set nama modul yang sudah selesai."""
    if not checkpoint_path.exists():
        return set()
    completed = set()
    try:
        with open(checkpoint_path, encoding="utf-8") as f:
            data = json.load(f)
            completed = set(data.get("completed_modules", []))
    except Exception:
        pass
    return completed


def _save_checkpoint(checkpoint_path: Path, completed_modules: set) -> None:
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    with open(checkpoint_path, "w", encoding="utf-8") as f:
        json.dump({"completed_modules": sorted(completed_modules)}, f, indent=2)


def _append_accumulated(output_dir: Path, datapoints: List[ValidDomainDataPoint]) -> None:
    acc_file = output_dir / "accumulated.jsonl"
    acc_file.parent.mkdir(parents=True, exist_ok=True)
    with open(acc_file, "a", encoding="utf-8") as f:
        for dp in datapoints:
            f.write(json.dumps(
                {"input": dp.input, "target": dp.target, "metadata": dp.metadata},
                ensure_ascii=False,
            ) + "\n")


def _load_accumulated(output_dir: Path) -> List[dict]:
    acc_file = output_dir / "accumulated.jsonl"
    if not acc_file.exists():
        return []
    records = []
    with open(acc_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def _save_failures(failures_path: Path, failures: List[dict]) -> None:
    failures_path.parent.mkdir(parents=True, exist_ok=True)
    with open(failures_path, "a", encoding="utf-8") as f:
        for entry in failures:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# Format processors
# ---------------------------------------------------------------------------

def _process_chunk(
    chunk: Chunk,
    formats: List[str],
    llm_client=None,
    max_per_chunk: int = 3,
) -> List[RawDomainDataPoint]:
    """Proses satu chunk dengan semua format yang diminta."""
    results: List[RawDomainDataPoint] = []

    if "span_corruption" in formats:
        try:
            dp = corrupt_spans(chunk)
            results.append(dp)
        except Exception as e:
            pass

    if "qa_generic" in formats:
        try:
            qa_pairs = extract_qa_pairs(chunk)
            results.extend(qa_pairs[:max_per_chunk])
        except Exception as e:
            pass

    if "summarization" in formats and llm_client is not None:
        try:
            dp = summarize_chunk(chunk, llm_client)
            if dp is not None:
                results.append(dp)
        except Exception as e:
            pass

    return results


# ---------------------------------------------------------------------------
# Main pipeline function
# ---------------------------------------------------------------------------

def run_domain_pipeline(
    materi_dir: str,
    output_dir: str,
    formats: List[str] = None,
    max_per_chunk: int = 3,
    llm_provider: str = None,
    write_final: bool = True,
    module_filter: Optional[List[str]] = None,
) -> dict:
    """
    Jalankan pipeline domain adaptation.

    Args:
        materi_dir    : direktori materi Markdown (11 modul)
        output_dir    : direktori output
        formats       : list format ["span_corruption", "qa_generic", "summarization"]
        max_per_chunk : max QA pairs per chunk untuk qa_generic
        llm_provider  : provider LLM untuk summarization (None = skip summarization)
        write_final   : jika True, tulis JSONL splits di akhir
        module_filter : list nama modul yang diproses (None = semua modul)
                        contoh: ["01-Berkenalan-dengan-python", "02-berinteraksi-dengan-data"]

    Returns:
        dict: summary statistik pipeline
    """
    if formats is None:
        formats = ["span_corruption", "qa_generic"]

    # Validasi formats
    valid_formats = {"span_corruption", "qa_generic", "summarization"}
    for fmt in formats:
        if fmt not in valid_formats:
            raise ValueError(f"Format tidak valid: '{fmt}'. Pilih dari: {valid_formats}")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    checkpoint_path = output_path / "checkpoint.json"
    failures_path = output_path / "validation_failures.jsonl"

    # Build LLM client jika summarization diminta
    llm_client = None
    if "summarization" in formats and llm_provider:
        try:
            from langchain_openai import ChatOpenAI
            import os
            llm_client = ChatOpenAI(
                model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
                openai_api_key=os.getenv("OPENROUTER_API_KEY"),
                openai_api_base=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
                temperature=0.7,
            )
            print(f"[INFO] LLM client siap: {os.getenv('OPENROUTER_MODEL', 'openai/gpt-4o-mini')}")
        except Exception as e:
            print(f"[WARNING] Gagal build LLM client: {e}. Summarization di-skip.")
            formats = [f for f in formats if f != "summarization"]

    # Load checkpoint
    completed_modules = _load_checkpoint(checkpoint_path)

    # Temukan semua modul
    materi_path = Path(materi_dir)
    all_module_dirs = sorted([p for p in materi_path.iterdir() if p.is_dir()])

    if not all_module_dirs:
        raise ValueError(f"Tidak ada modul ditemukan di {materi_dir}")

    # Filter modul jika module_filter diberikan
    if module_filter:
        module_dirs = [d for d in all_module_dirs if d.name in module_filter]
        if not module_dirs:
            raise ValueError(f"Tidak ada modul yang cocok dengan filter: {module_filter}")
    else:
        module_dirs = all_module_dirs

    print(f"\n{'='*60}")
    print(f"Domain Adaptation Pipeline")
    print(f"Formats  : {formats}")
    print(f"Modul    : {len(module_dirs)}{' (filtered)' if module_filter else ''}")
    print(f"Output   : {output_dir}")
    print(f"{'='*60}\n")

    total_raw = 0
    total_valid = 0
    total_failed = 0
    format_counts: dict = {fmt: 0 for fmt in formats}

    for module_dir in module_dirs:
        module_name = module_dir.name

        if module_name in completed_modules:
            print(f"[SKIP] {module_name} (sudah selesai)")
            continue

        print(f"\n[MODULE] {module_name}")

        # Chunk semua file di modul ini
        md_files = sorted(module_dir.rglob("*.md"))
        if not md_files:
            print(f"  [WARNING] Tidak ada .md di {module_dir}")
            continue

        all_chunks: List[Chunk] = []
        for md_file in md_files:
            try:
                chunks = chunk_markdown(str(md_file), max_tokens=512, min_tokens=128)
                all_chunks.extend(chunks)
            except Exception as e:
                print(f"  [WARNING] Gagal chunk {md_file.name}: {e}")

        print(f"  Chunks  : {len(all_chunks)} dari {len(md_files)} file")

        # Proses setiap chunk
        raw_datapoints: List[RawDomainDataPoint] = []
        for chunk in tqdm(all_chunks, desc=f"  {module_name}", unit="chunk", leave=False):
            dps = _process_chunk(chunk, formats, llm_client, max_per_chunk)
            raw_datapoints.extend(dps)

        total_raw += len(raw_datapoints)
        print(f"  Raw     : {len(raw_datapoints)} data points")

        # Validasi
        valid_list, failure_log = validate_domain_batch(raw_datapoints)
        total_valid += len(valid_list)
        total_failed += len(failure_log)

        # Hitung per format
        for dp in valid_list:
            fmt = dp.metadata.get("format", "unknown")
            if fmt in format_counts:
                format_counts[fmt] += 1

        print(f"  Valid   : {len(valid_list)} | Failed: {len(failure_log)}")

        # Simpan ke accumulated
        if valid_list:
            _append_accumulated(output_path, valid_list)

        # Simpan failures
        if failure_log:
            _save_failures(failures_path, failure_log)

        # Update checkpoint
        completed_modules.add(module_name)
        _save_checkpoint(checkpoint_path, completed_modules)

    # Write final splits
    if write_final:
        print(f"\n[WRITE] Menulis final splits...")
        accumulated = _load_accumulated(output_path)
        if accumulated:
            valid_all = [
                ValidDomainDataPoint(
                    input=r["input"],
                    target=r["target"],
                    metadata=r["metadata"],
                )
                for r in accumulated
            ]
            info = write_domain_dataset(valid_all, output_dir)
            print(f"[DONE] {info['total']} data points → {output_dir}")
            print(f"       Train: {info['splits']['train']} | Val: {info['splits']['validation']} | Test: {info['splits']['test']}")
        else:
            print("[WARNING] Tidak ada data untuk ditulis.")
            info = {}
    else:
        info = {}

    summary = {
        "total_raw": total_raw,
        "total_valid": total_valid,
        "total_failed": total_failed,
        "format_counts": format_counts,
        "output_dir": str(output_path),
    }

    print(f"\n{'='*60}")
    print(f"[SUMMARY]")
    print(f"  Raw generated : {total_raw}")
    print(f"  Valid         : {total_valid}")
    print(f"  Failed        : {total_failed}")
    for fmt, cnt in format_counts.items():
        print(f"  {fmt:20s}: {cnt}")
    print(f"{'='*60}")

    return summary
