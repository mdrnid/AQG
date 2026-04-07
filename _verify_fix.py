from src.dataset.step2.chunker import chunk_markdown
from src.dataset.step1.formatter import corrupt_spans, extract_qa_pairs, _count_sentinels, _clean_text_for_processing

chunks = chunk_markdown('dataset_aqg/materi/02-berinteraksi-dengan-data/03-type-data.md', max_tokens=512, min_tokens=128)

# Test clean text
c0 = chunks[0]
clean = _clean_text_for_processing(c0.text)
print('=== CLEAN TEXT (chunk 1, first 400 chars) ===')
print(clean[:400])
print()

# Test sentinel balance
ok = sum(1 for c in chunks if _count_sentinels(corrupt_spans(c).input) == _count_sentinels(corrupt_spans(c).target) - 1)
print(f'Sentinel balance: {ok}/{len(chunks)} OK')

# Test QA
qa_all = []
for c in chunks:
    qa_all.extend(extract_qa_pairs(c))

print(f'QA pairs total: {len(qa_all)}')
bad_terms = ['Umur', 'Nama', 'Berat Badan', 'Keputusan Memakai']
bad = [qa.input for qa in qa_all if any(t in qa.input for t in bad_terms)]
print(f'Bad terms: {bad if bad else "None - clean!"}')

# Cek span corruption tidak mengandung blockquote/image
sc = corrupt_spans(c0)
has_noise = ('> ' in sc.input) or ('![' in sc.input)
print(f'Span corruption contains blockquote/image: {has_noise}')
print(f'Input preview: {sc.input[:200]}')

# Sample QA
print()
print('=== SAMPLE QA ===')
for qa in qa_all[:5]:
    print(f'  Q: {qa.input}')
    print(f'  A: {qa.target[:100]}')
    print()
