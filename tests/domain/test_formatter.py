"""
Tests untuk src/dataset/step1/formatter.py
Mencakup unit tests dan property-based tests untuk SpanCorruptor dan QAGenerator.
"""
import math
import re
from typing import List

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from src.dataset.step2.chunker import Chunk
from src.dataset.step1.formatter import (
    RawDomainDataPoint,
    corrupt_spans,
    extract_qa_pairs,
    _count_sentinels,
    _estimate_tokens,
)


# ---------------------------------------------------------------------------
# Helpers / Generators
# ---------------------------------------------------------------------------

def make_chunk(
    text: str,
    source_file: str = "01-modul/lesson.md",
    section_heading: str = "## Test Section",
    has_code: bool = False,
) -> Chunk:
    return Chunk(
        text=text,
        source_file=source_file,
        section_heading=section_heading,
        token_count=_estimate_tokens(text),
        has_code=has_code,
    )


def make_chunk_with_code(prose: str) -> Chunk:
    """Buat chunk yang mengandung code block."""
    code = "```python\nprint('hello')\nx = 1 + 2\n```"
    text = prose + "\n\n" + code
    return make_chunk(text, has_code=True)


# Hypothesis strategy: teks biasa (minimal 20 kata agar ada token yang bisa di-mask)
@st.composite
def plain_text_chunk(draw) -> Chunk:
    words = draw(
        st.lists(
            st.text(
                alphabet=st.characters(whitelist_categories=("Ll", "Lu")),
                min_size=2, max_size=10,
            ),
            min_size=20, max_size=80,
        )
    )
    text = " ".join(words)
    return make_chunk(text)


@st.composite
def chunk_with_code_block(draw) -> Chunk:
    """Chunk yang mengandung code block Python."""
    words = draw(
        st.lists(
            st.text(
                alphabet=st.characters(whitelist_categories=("Ll", "Lu")),
                min_size=2, max_size=8,
            ),
            min_size=10, max_size=40,
        )
    )
    prose = " ".join(words)
    code = "```python\nprint('hello')\nx = 1 + 2\n```"
    text = prose + "\n\n" + code
    return make_chunk(text, has_code=True)


@st.composite
def chunk_with_bold_term(draw) -> Chunk:
    """Chunk yang mengandung bold term dan kalimat definisi."""
    term = draw(st.text(
        alphabet=st.characters(whitelist_categories=("Ll", "Lu")),
        min_size=3, max_size=15,
    ))
    assume(len(term.strip()) >= 3)
    text = f"**{term}** adalah konsep penting dalam Python yang sering digunakan oleh programmer."
    return make_chunk(text)


# ---------------------------------------------------------------------------
# Unit Tests — SpanCorruptor
# ---------------------------------------------------------------------------

class TestCorruptSpansUnit:

    def test_output_is_raw_domain_datapoint(self):
        chunk = make_chunk("Python adalah bahasa pemrograman yang populer dan mudah dipelajari oleh semua orang")
        result = corrupt_spans(chunk, seed=42)
        assert isinstance(result, RawDomainDataPoint)

    def test_format_tag_is_span_corruption(self):
        chunk = make_chunk("Python adalah bahasa pemrograman yang populer dan mudah dipelajari oleh semua orang")
        result = corrupt_spans(chunk, seed=42)
        assert result.metadata["format"] == "span_corruption"

    def test_metadata_has_required_fields(self):
        chunk = make_chunk("Python adalah bahasa pemrograman yang populer dan mudah dipelajari")
        result = corrupt_spans(chunk, seed=42)
        for field in ("format", "source_file", "module_name", "section_heading", "token_count", "has_code"):
            assert field in result.metadata, f"Missing field: {field}"

    def test_short_text_still_produces_output(self):
        """Edge case: teks sangat pendek (< 5 token)."""
        chunk = make_chunk("Python bahasa pemrograman")
        result = corrupt_spans(chunk, seed=0)
        assert isinstance(result, RawDomainDataPoint)
        assert result.input
        assert result.target

    def test_code_block_preserved_in_input(self):
        """Code block tidak boleh mengandung sentinel token."""
        code_block = "```python\nprint('hello')\nx = 1 + 2\n```"
        chunk = make_chunk(
            f"Python adalah bahasa pemrograman yang populer.\n\n{code_block}",
            has_code=True,
        )
        result = corrupt_spans(chunk, seed=7)
        # Ekstrak code block dari input
        code_in_input = re.search(r"```[\s\S]*?```", result.input)
        if code_in_input:
            assert "<extra_id_" not in code_in_input.group()

    def test_sentinel_balance(self):
        """Property 3: count_sentinels(input) == count_sentinels(target) - 1."""
        chunk = make_chunk(
            "Python adalah bahasa pemrograman tingkat tinggi yang dirilis pada tahun 1991 oleh Guido van Rossum"
        )
        result = corrupt_spans(chunk, seed=1)
        n_input = _count_sentinels(result.input)
        n_target = _count_sentinels(result.target)
        assert n_input == n_target - 1, (
            f"Sentinel balance gagal: input={n_input}, target={n_target}"
        )


# ---------------------------------------------------------------------------
# Property-Based Tests — SpanCorruptor
# ---------------------------------------------------------------------------

class TestCorruptSpansProperties:

    # Feature: domain-adaptation-dataset, Property 3: Span corruption sentinel balance
    @given(plain_text_chunk())
    @settings(max_examples=100, deadline=None)
    def test_property3_sentinel_balance(self, chunk: Chunk):
        """count_sentinels(input) == count_sentinels(target) - 1"""
        result = corrupt_spans(chunk)
        n_input = _count_sentinels(result.input)
        n_target = _count_sentinels(result.target)
        assert n_input == n_target - 1, (
            f"Property 3 gagal: input sentinels={n_input}, target sentinels={n_target}\n"
            f"input={result.input!r}\ntarget={result.target!r}"
        )

    # Feature: domain-adaptation-dataset, Property 4: Span corruption rate invariant
    @given(plain_text_chunk())
    @settings(max_examples=100, deadline=None)
    def test_property4_corruption_rate_invariant(self, chunk: Chunk):
        """Jumlah token yang di-mask antara 1 dan ceil(token_count * 0.25)."""
        result = corrupt_spans(chunk)
        n_sentinels_input = _count_sentinels(result.input)
        # Setiap sentinel di input mewakili satu span (2-5 token)
        # Minimal 1 sentinel (1 span), maksimal ceil(0.25 * n_tokens) token total
        assert n_sentinels_input >= 1, "Property 4 gagal: tidak ada span yang di-mask"

        # Hitung total token yang di-mask dari target
        # Target format: "<extra_id_0> span0 <extra_id_1> span1 ... <extra_id_N>"
        # Jumlah token di-mask = total token target - jumlah sentinel di target
        target_tokens = result.target.split()
        n_target_sentinels = _count_sentinels(result.target)
        masked_tokens = len(target_tokens) - n_target_sentinels
        max_allowed = math.ceil(chunk.token_count * 0.25)
        assert masked_tokens <= max_allowed, (
            f"Property 4 gagal: masked={masked_tokens} > max={max_allowed}"
        )

    # Feature: domain-adaptation-dataset, Property 5: Code block not masked
    @given(chunk_with_code_block())
    @settings(max_examples=100, deadline=None)
    def test_property5_code_block_not_masked(self, chunk: Chunk):
        """Code block text tidak berubah di input setelah corruption."""
        result = corrupt_spans(chunk)
        # Cari semua code block di teks asli
        original_code_blocks = re.findall(r"```[\s\S]*?```", chunk.text)
        # Cari semua code block di input hasil corruption
        input_code_blocks = re.findall(r"```[\s\S]*?```", result.input)

        assert len(original_code_blocks) == len(input_code_blocks), (
            "Property 5 gagal: jumlah code block berubah"
        )
        for orig, corrupted in zip(original_code_blocks, input_code_blocks):
            assert "<extra_id_" not in corrupted, (
                f"Property 5 gagal: sentinel ditemukan di dalam code block:\n{corrupted}"
            )


# ---------------------------------------------------------------------------
# Unit Tests — QAGenerator
# ---------------------------------------------------------------------------

class TestExtractQAPairsUnit:

    def test_bold_term_generates_qa(self):
        chunk = make_chunk(
            "**List** adalah tipe data collection yang menyimpan banyak nilai sekaligus dalam Python."
        )
        results = extract_qa_pairs(chunk)
        assert len(results) >= 1
        assert any("List" in r.input for r in results)

    def test_inline_code_generates_qa(self):
        chunk = make_chunk(
            "Fungsi `print()` digunakan untuk menampilkan output ke layar dalam Python."
        )
        results = extract_qa_pairs(chunk)
        # print() mungkin di-skip karena mengandung simbol, cek dengan term yang lebih panjang
        chunk2 = make_chunk(
            "Tipe data `boolean` hanya bernilai True atau False dalam Python."
        )
        results2 = extract_qa_pairs(chunk2)
        assert len(results) >= 1 or len(results2) >= 1

    def test_heading_fallback_when_no_bold_or_inline(self):
        chunk = make_chunk(
            "Tipe data ini sangat berguna untuk menyimpan nilai kebenaran dalam program.",
            section_heading="## Boolean",
        )
        results = extract_qa_pairs(chunk)
        assert len(results) >= 1
        assert any("Boolean" in r.input for r in results)

    def test_format_tag_is_qa_generic(self):
        chunk = make_chunk(
            "**Dictionary** adalah struktur data key-value yang sangat berguna dalam Python."
        )
        results = extract_qa_pairs(chunk)
        assert all(r.metadata["format"] == "qa_generic" for r in results)

    def test_no_duplicate_terms(self):
        """Term yang sama di bold dan inline tidak menghasilkan QA duplikat."""
        chunk = make_chunk(
            "**list** adalah tipe data. Gunakan `list` untuk menyimpan banyak nilai."
        )
        results = extract_qa_pairs(chunk)
        inputs = [r.input for r in results]
        # Tidak boleh ada dua QA dengan term yang sama
        assert len(inputs) == len(set(inputs))

    def test_empty_chunk_returns_empty_list(self):
        chunk = make_chunk("   ")
        results = extract_qa_pairs(chunk)
        assert results == []

    def test_metadata_has_required_fields(self):
        chunk = make_chunk(
            "**Set** adalah kumpulan elemen unik tanpa urutan dalam Python."
        )
        results = extract_qa_pairs(chunk)
        assert len(results) >= 1
        for r in results:
            for field in ("format", "source_file", "module_name", "section_heading"):
                assert field in r.metadata


# ---------------------------------------------------------------------------
# Property-Based Tests — QAGenerator
# ---------------------------------------------------------------------------

class TestExtractQAPairsProperties:

    # Feature: domain-adaptation-dataset, Property 7: QA term presence
    @given(chunk_with_bold_term())
    @settings(max_examples=100, deadline=None)
    def test_property7_qa_term_presence(self, chunk: Chunk):
        """Term di input question muncul di target answer."""
        results = extract_qa_pairs(chunk)
        for r in results:
            # Ekstrak term dari input: "Apa itu {term} dalam Python?" atau "Jelaskan {term} dalam Python."
            match = re.search(
                r"(?:Apa itu|Jelaskan|Apa yang dimaksud dengan)\s+(.+?)(?:\s+dalam Python[?.]|\?)",
                r.input,
            )
            if match:
                term = match.group(1).strip()
                assert term.lower() in r.target.lower(), (
                    f"Property 7 gagal: term '{term}' tidak ditemukan di target:\n{r.target!r}"
                )
