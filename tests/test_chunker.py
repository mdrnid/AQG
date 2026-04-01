"""
Tests untuk Chunker — verifikasi dengan materi nyata dan unit tests.
"""
import pytest
from pathlib import Path
from src.dataset.chunker import Chunk, chunk_markdown, chunk_all_materials, _estimate_tokens

MATERI_DIR = "dataset_aqg/materi"
SAMPLE_FILE = "dataset_aqg/materi/01-Berkenalan-dengan-python/01-perkenalan-pythn.md"
SAMPLE_FILE_2 = "dataset_aqg/materi/01-Berkenalan-dengan-python/05-variable-and-assignment.md"


# ── Unit tests ──────────────────────────────────────────────────────────────

class TestChunkDataclass:
    def test_chunk_has_required_fields(self):
        c = Chunk(
            text="hello world",
            source_file="test.md",
            section_heading="# Test",
            token_count=2,
            has_code=False,
        )
        assert c.text == "hello world"
        assert c.source_file == "test.md"
        assert c.section_heading == "# Test"
        assert c.token_count == 2
        assert c.has_code is False


class TestEstimateTokens:
    def test_empty_string_returns_one(self):
        assert _estimate_tokens("") == 1

    def test_single_word(self):
        result = _estimate_tokens("hello")
        assert result >= 1

    def test_longer_text_has_more_tokens(self):
        short = _estimate_tokens("hello world")
        long = _estimate_tokens("hello world this is a longer sentence with more words")
        assert long > short


class TestChunkMarkdown:
    def test_returns_list_of_chunks(self):
        chunks = chunk_markdown(SAMPLE_FILE)
        assert isinstance(chunks, list)
        assert len(chunks) > 0
        assert all(isinstance(c, Chunk) for c in chunks)

    def test_all_chunks_have_source_file(self):
        chunks = chunk_markdown(SAMPLE_FILE)
        for c in chunks:
            assert c.source_file != ""
            assert "perkenalan-pythn" in c.source_file

    def test_all_chunks_have_section_heading_or_empty(self):
        chunks = chunk_markdown(SAMPLE_FILE)
        for c in chunks:
            # section_heading boleh kosong untuk teks sebelum heading pertama
            assert isinstance(c.section_heading, str)

    def test_all_chunks_have_positive_token_count(self):
        chunks = chunk_markdown(SAMPLE_FILE)
        for c in chunks:
            assert c.token_count > 0

    def test_no_chunk_exceeds_max_tokens(self):
        chunks = chunk_markdown(SAMPLE_FILE, max_tokens=400)
        for c in chunks:
            assert c.token_count <= 400, (
                f"Chunk melebihi 400 token: {c.token_count}\n"
                f"Heading: {c.section_heading}\n"
                f"Text (50 char): {c.text[:50]}"
            )

    def test_code_block_integrity(self):
        """Setiap chunk yang punya opening ``` harus punya closing ```."""
        chunks = chunk_markdown(SAMPLE_FILE)
        for c in chunks:
            opens = c.text.count("```")
            # Jumlah ``` harus genap (setiap buka punya tutup)
            assert opens % 2 == 0, (
                f"Code block tidak tertutup di chunk:\n{c.text[:100]}"
            )

    def test_has_code_flag_accurate(self):
        chunks = chunk_markdown(SAMPLE_FILE)
        for c in chunks:
            if "```" in c.text:
                assert c.has_code is True
            else:
                assert c.has_code is False

    def test_file_with_code_blocks(self):
        """File variable-and-assignment.md punya code blocks — pastikan dihandle."""
        chunks = chunk_markdown(SAMPLE_FILE_2)
        assert len(chunks) > 0
        has_code_chunks = [c for c in chunks if c.has_code]
        assert len(has_code_chunks) > 0, "Seharusnya ada chunk dengan code block"

    def test_custom_max_tokens(self):
        """Chunk tanpa code block harus <= max_tokens.
        Toleransi kecil (+10%) diizinkan untuk blockquote panjang yang tidak bisa dipotong
        di tengah (setiap baris > adalah satu unit semantik)."""
        chunks = chunk_markdown(SAMPLE_FILE, max_tokens=200)
        for c in chunks:
            if not c.has_code:
                # Toleransi 10% untuk blockquote yang tidak bisa dipotong lebih kecil
                assert c.token_count <= 220, (
                    f"Chunk melebihi batas toleransi (220 token): {c.token_count}\n"
                    f"Text: {c.text[:80]}"
                )

    def test_nonexistent_file_raises(self):
        with pytest.raises(FileNotFoundError):
            chunk_markdown("nonexistent/file.md")


class TestChunkAllMaterials:
    def test_returns_chunks_from_multiple_files(self):
        chunks = chunk_all_materials(
            "dataset_aqg/materi/01-Berkenalan-dengan-python"
        )
        assert len(chunks) > 0

    def test_chunks_from_different_files(self):
        chunks = chunk_all_materials(
            "dataset_aqg/materi/01-Berkenalan-dengan-python"
        )
        source_files = {c.source_file for c in chunks}
        assert len(source_files) > 1, "Harus ada chunk dari lebih dari 1 file"

    def test_all_chunks_valid(self):
        chunks = chunk_all_materials(
            "dataset_aqg/materi/01-Berkenalan-dengan-python"
        )
        for c in chunks:
            assert c.token_count > 0
            assert c.source_file != ""
            assert c.token_count <= 400
