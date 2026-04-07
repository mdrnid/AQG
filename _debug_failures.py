"""Debug validation failures — cek token count setelah cleaning."""
from src.dataset.step2.chunker import chunk_markdown
from src.dataset.step1.formatter import corrupt_spans, extract_qa_pairs, _clean_text_for_processing, _estimate_tokens
from src.dataset.step1.validator import validate_domain
from pathlib import Path

materi_dir = Path("dataset_aqg/materi/02-berinteraksi-dengan-data")
md_files = sorted(materi_dir.rglob("*.md"))

all_chunks = []
for f in md_files:
    chunks = chunk_markdown(str(f), max_tokens=512, min_tokens=128)
    all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}\n")

# Analisis token count sebelum dan sesudah cleaning
print(f"{'Heading':<35} {'orig':>5} {'clean':>6} {'working':>8} {'sc_input':>9}")
print("-" * 70)
for chunk in all_chunks:
    clean = _clean_text_for_processing(chunk.text)
    working = clean if len(clean.split()) >= 10 else chunk.text
    sc = corrupt_spans(chunk)
    sc_tokens = _estimate_tokens(sc.input)
    flag = " ← FAIL" if sc_tokens < 10 else ""
    heading = chunk.section_heading[:33] if chunk.section_heading else "(no heading)"
    print(f"{heading:<35} {chunk.token_count:>5} {_estimate_tokens(clean):>6} {_estimate_tokens(working):>8} {sc_tokens:>9}{flag}")

# Cek QA failures
print("\n=== QA FAILURES ===")
for chunk in all_chunks[:8]:
    qa_pairs = extract_qa_pairs(chunk)
    for qa in qa_pairs:
        r = validate_domain(qa)
        if not r.is_valid:
            print(f"  Q: {qa.input[:60]}")
            print(f"  A: {qa.target[:80]}")
            print(f"  Tokens: {_estimate_tokens(qa.input)} | Reason: {r.failure_reasons}")
            print()
