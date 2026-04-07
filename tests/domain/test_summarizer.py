"""
Unit tests untuk Summarizer di src/dataset/step1/formatter.py
Menggunakan mock LLM — tidak membutuhkan API key.
"""
from unittest.mock import MagicMock, patch

import pytest

from src.dataset.step2.chunker import Chunk
from src.dataset.step1.formatter import (
    RawDomainDataPoint,
    summarize_chunk,
    MIN_TOKENS_FOR_SUMMARIZATION,
    _estimate_tokens,
)


def make_chunk(text: str, token_count: int = None) -> Chunk:
    tc = token_count if token_count is not None else _estimate_tokens(text)
    return Chunk(
        text=text,
        source_file="01-modul/lesson.md",
        section_heading="## Test",
        token_count=tc,
        has_code=False,
    )


def make_llm_mock(response_text: str):
    """Buat mock LLM yang mengembalikan response_text."""
    mock = MagicMock()
    mock_response = MagicMock()
    mock_response.content = response_text
    mock.invoke.return_value = mock_response
    return mock


# ---------------------------------------------------------------------------
# Test: input prefix
# ---------------------------------------------------------------------------

class TestSummarizerInputPrefix:

    def test_input_starts_with_rangkum(self):
        """Property 6: input selalu diawali 'Rangkum teks berikut:'"""
        chunk = make_chunk(
            "Python adalah bahasa pemrograman tingkat tinggi yang mudah dipelajari. "
            "Python dirilis pada tahun 1991 oleh Guido van Rossum dan sejak saat itu "
            "menjadi salah satu bahasa pemrograman paling populer di dunia.",
            token_count=150,
        )
        llm = make_llm_mock("Python adalah bahasa pemrograman populer yang mudah dipelajari.")
        result = summarize_chunk(chunk, llm)
        assert result is not None
        assert result.input.startswith("Rangkum teks berikut:")

    def test_input_contains_chunk_text(self):
        """Input harus mengandung teks chunk asli."""
        text = (
            "Tipe data boolean hanya bernilai True atau False. "
            "Boolean digunakan untuk merepresentasikan nilai kebenaran dalam Python. "
            "Nilai False mencakup None, angka nol, dan koleksi kosong."
        )
        chunk = make_chunk(text, token_count=120)
        llm = make_llm_mock("Boolean adalah tipe data dengan nilai True atau False.")
        result = summarize_chunk(chunk, llm)
        assert result is not None
        assert chunk.text in result.input


# ---------------------------------------------------------------------------
# Test: skip chunk pendek
# ---------------------------------------------------------------------------

class TestSummarizerSkipShortChunk:

    def test_skip_chunk_below_min_tokens(self):
        """Chunk dengan token_count < MIN_TOKENS_FOR_SUMMARIZATION harus di-skip (return None)."""
        chunk = make_chunk("Python mudah dipelajari.", token_count=MIN_TOKENS_FOR_SUMMARIZATION - 1)
        llm = make_llm_mock("Ringkasan singkat.")
        result = summarize_chunk(chunk, llm)
        assert result is None

    def test_skip_chunk_exactly_at_boundary(self):
        """Chunk dengan token_count == MIN_TOKENS_FOR_SUMMARIZATION - 1 harus di-skip."""
        chunk = make_chunk("teks", token_count=MIN_TOKENS_FOR_SUMMARIZATION - 1)
        llm = make_llm_mock("Ringkasan.")
        result = summarize_chunk(chunk, llm)
        assert result is None

    def test_process_chunk_at_min_tokens(self):
        """Chunk dengan token_count == MIN_TOKENS_FOR_SUMMARIZATION harus diproses."""
        chunk = make_chunk("teks panjang", token_count=MIN_TOKENS_FOR_SUMMARIZATION)
        llm = make_llm_mock("Ringkasan valid.")
        result = summarize_chunk(chunk, llm)
        assert result is not None


# ---------------------------------------------------------------------------
# Test: retry logic
# ---------------------------------------------------------------------------

class TestSummarizerRetry:

    def test_retry_once_then_succeed(self):
        """LLM gagal 1x lalu berhasil — harus return hasil."""
        chunk = make_chunk("teks materi Python", token_count=150)

        call_count = 0
        def side_effect(messages):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise Exception("API timeout")
            mock_resp = MagicMock()
            mock_resp.content = "Ringkasan berhasil."
            return mock_resp

        llm = MagicMock()
        llm.invoke.side_effect = side_effect

        result = summarize_chunk(chunk, llm, max_retries=2)
        assert result is not None
        assert result.target == "Ringkasan berhasil."
        assert call_count == 2

    def test_all_retries_fail_returns_none(self):
        """LLM selalu gagal — harus return None setelah max_retries."""
        chunk = make_chunk("teks materi Python", token_count=150)
        llm = MagicMock()
        llm.invoke.side_effect = Exception("API error")

        result = summarize_chunk(chunk, llm, max_retries=2)
        assert result is None
        assert llm.invoke.call_count == 3  # 1 attempt + 2 retries

    def test_empty_response_triggers_retry(self):
        """Response kosong dianggap gagal dan trigger retry."""
        chunk = make_chunk("teks materi Python", token_count=150)

        call_count = 0
        def side_effect(messages):
            nonlocal call_count
            call_count += 1
            mock_resp = MagicMock()
            mock_resp.content = "" if call_count == 1 else "Ringkasan valid."
            return mock_resp

        llm = MagicMock()
        llm.invoke.side_effect = side_effect

        result = summarize_chunk(chunk, llm, max_retries=2)
        assert result is not None
        assert result.target == "Ringkasan valid."


# ---------------------------------------------------------------------------
# Test: output format
# ---------------------------------------------------------------------------

class TestSummarizerOutput:

    def test_format_tag_is_summarization(self):
        chunk = make_chunk("teks materi Python yang cukup panjang", token_count=150)
        llm = make_llm_mock("Ringkasan materi Python.")
        result = summarize_chunk(chunk, llm)
        assert result is not None
        assert result.metadata["format"] == "summarization"

    def test_metadata_has_required_fields(self):
        chunk = make_chunk("teks materi Python yang cukup panjang", token_count=150)
        llm = make_llm_mock("Ringkasan materi Python.")
        result = summarize_chunk(chunk, llm)
        assert result is not None
        for field in ("format", "source_file", "module_name", "section_heading", "token_count", "has_code"):
            assert field in result.metadata, f"Missing field: {field}"

    def test_target_is_llm_response(self):
        chunk = make_chunk("teks materi Python yang cukup panjang", token_count=150)
        expected = "Python adalah bahasa pemrograman yang populer dan mudah dipelajari."
        llm = make_llm_mock(expected)
        result = summarize_chunk(chunk, llm)
        assert result is not None
        assert result.target == expected
