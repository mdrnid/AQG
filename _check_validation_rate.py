"""Cek validation rate setelah semua fix."""
from src.dataset.step2.chunker import chunk_markdown
from src.dataset.step1.formatter import corrupt_spans, extract_qa_pairs
from src.dataset.step1.validator import validate_domain_batch
from pathlib import Path

for module in ["01-Berkenalan-dengan-python", "02-berinteraksi-dengan-data"]:
    materi_dir = Path(f"dataset_aqg/materi/{module}")
    md_files = sorted(materi_dir.rglob("*.md"))
    all_chunks = []
    for f in md_files:
        all_chunks.extend(chunk_markdown(str(f), max_tokens=512, min_tokens=128))

    raw = []
    for chunk in all_chunks:
        raw.append(corrupt_spans(chunk))
        raw.extend(extract_qa_pairs(chunk)[:3])

    valid, failures = validate_domain_batch(raw)
    rate = len(valid) / len(raw) * 100 if raw else 0
    print(f"{module}: {len(valid)}/{len(raw)} valid ({rate:.0f}%)")

print("\nDone.")
