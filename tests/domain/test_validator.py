"""
Tests untuk src/dataset/step1/validator.py
Unit tests + property-based tests (Property 10, 11).
"""
import math

import pytest
from hypothesis import given, settings, HealthCheck
from hypothesis import strategies as st

from src.dataset.step1.formatter import RawDomainDataPoint
from src.dataset.step1.validator import (
    DomainValidationResult,
    ValidDomainDataPoint,
    validate_domain,
    validate_domain_batch,
    MIN_INPUT_TOKENS,
    MAX_INPUT_TOKENS,
    VALID_FORMATS,
    _estimate_tokens,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_valid_dp(
    input_text: str = None,
    target: str = "Ini adalah target yang valid dan cukup panjang.",
    fmt: str = "span_corruption",
    source_file: str = "01-modul/lesson.md",
    module_name: str = "01-modul",
) -> RawDomainDataPoint:
    if input_text is None:
        # Buat input yang pasti lolos validasi (>= 10 token)
        input_text = " ".join(["kata"] * 15)
    return RawDomainDataPoint(
        input=input_text,
        target=target,
        metadata={
            "format": fmt,
            "source_file": source_file,
            "module_name": module_name,
        },
    )


def make_long_input(n_tokens: int) -> str:
    """Buat string dengan estimasi n_tokens token."""
    # _estimate_tokens = len(words) * 1.3, jadi butuh ceil(n/1.3) kata
    n_words = math.ceil(n_tokens / 1.3) + 1
    return " ".join(["kata"] * n_words)


# ---------------------------------------------------------------------------
# Unit Tests — validate_domain
# ---------------------------------------------------------------------------

class TestValidateDomainUnit:

    def test_valid_datapoint_passes(self):
        dp = make_valid_dp()
        result = validate_domain(dp)
        assert result.is_valid
        assert result.failure_reasons == []

    def test_all_valid_formats_pass(self):
        for fmt in VALID_FORMATS:
            dp = make_valid_dp(fmt=fmt)
            result = validate_domain(dp)
            assert result.is_valid, f"Format '{fmt}' seharusnya valid: {result.failure_reasons}"

    def test_invalid_format_fails(self):
        dp = make_valid_dp(fmt="invalid_format")
        result = validate_domain(dp)
        assert not result.is_valid
        assert any("format" in r for r in result.failure_reasons)

    def test_input_too_short_fails(self):
        """Input < MIN_INPUT_TOKENS token harus gagal."""
        # Buat input yang pasti di bawah MIN_INPUT_TOKENS (1-2 kata)
        dp = make_valid_dp(input_text="x")
        result = validate_domain(dp)
        assert not result.is_valid

    def test_input_too_long_fails(self):
        """Input > 1024 token harus gagal."""
        long_input = make_long_input(MAX_INPUT_TOKENS + 10)
        dp = make_valid_dp(input_text=long_input)
        result = validate_domain(dp)
        assert not result.is_valid
        assert any("terlalu panjang" in r for r in result.failure_reasons)

    def test_empty_target_fails(self):
        dp = make_valid_dp(target="")
        result = validate_domain(dp)
        assert not result.is_valid

    def test_short_target_fails(self):
        dp = make_valid_dp(target="ok")  # < 5 karakter
        result = validate_domain(dp)
        assert not result.is_valid

    def test_missing_source_file_fails(self):
        dp = RawDomainDataPoint(
            input=" ".join(["kata"] * 15),
            target="Target yang valid dan cukup panjang.",
            metadata={"format": "span_corruption", "module_name": "01-modul"},
        )
        result = validate_domain(dp)
        assert not result.is_valid
        assert any("source_file" in r for r in result.failure_reasons)

    def test_missing_module_name_fails(self):
        dp = RawDomainDataPoint(
            input=" ".join(["kata"] * 15),
            target="Target yang valid dan cukup panjang.",
            metadata={"format": "span_corruption", "source_file": "01-modul/lesson.md"},
        )
        result = validate_domain(dp)
        assert not result.is_valid
        assert any("module_name" in r for r in result.failure_reasons)

    def test_boundary_input_min_passes(self):
        """Input tepat di batas minimum harus lolos."""
        # Buat input dengan token_count tepat MIN_INPUT_TOKENS
        input_text = make_long_input(MIN_INPUT_TOKENS)
        dp = make_valid_dp(input_text=input_text)
        result = validate_domain(dp)
        assert result.is_valid, f"Boundary min gagal: {result.failure_reasons}"

    def test_boundary_input_max_passes(self):
        """Input tepat di batas maksimum harus lolos."""
        # make_long_input bisa menghasilkan sedikit lebih dari MAX_INPUT_TOKENS
        # karena estimasi token = ceil(n_words/1.3)+1 — gunakan n_words yang lebih konservatif
        n_words = int(MAX_INPUT_TOKENS / 1.3) - 2  # sedikit di bawah batas
        input_text = " ".join(["kata"] * n_words)
        dp = make_valid_dp(input_text=input_text)
        result = validate_domain(dp)
        assert result.is_valid, f"Boundary max gagal: {result.failure_reasons}"


# ---------------------------------------------------------------------------
# Unit Tests — validate_domain_batch
# ---------------------------------------------------------------------------

class TestValidateDomainBatch:

    def test_all_valid_returns_full_list(self):
        dps = [make_valid_dp() for _ in range(5)]
        valid, failures = validate_domain_batch(dps)
        assert len(valid) == 5
        assert len(failures) == 0

    def test_all_invalid_returns_empty_valid(self):
        dps = [make_valid_dp(input_text="x") for _ in range(3)]
        valid, failures = validate_domain_batch(dps)
        assert len(valid) == 0
        assert len(failures) == 3

    def test_mixed_batch(self):
        dps = [make_valid_dp(), make_valid_dp(input_text="x"), make_valid_dp()]
        valid, failures = validate_domain_batch(dps)
        assert len(valid) == 2
        assert len(failures) == 1

    def test_failure_log_has_reasons(self):
        dps = [make_valid_dp(input_text="x")]
        _, failures = validate_domain_batch(dps)
        assert len(failures) == 1
        assert "reasons" in failures[0]
        assert len(failures[0]["reasons"]) > 0

    def test_valid_datapoint_is_valid_domain_datapoint(self):
        dps = [make_valid_dp()]
        valid, _ = validate_domain_batch(dps)
        assert isinstance(valid[0], ValidDomainDataPoint)


# ---------------------------------------------------------------------------
# Property-Based Tests
# ---------------------------------------------------------------------------

# Strategies
valid_format = st.sampled_from(sorted(VALID_FORMATS))

# Generate teks dengan panjang yang pasti dalam range [MIN_INPUT_TOKENS, MAX_INPUT_TOKENS]
# Gunakan list kata dengan panjang yang dikontrol
@st.composite
def valid_input(draw) -> str:
    # n_words * 1.3 harus antara MIN_INPUT_TOKENS dan MAX_INPUT_TOKENS
    min_words = math.ceil(MIN_INPUT_TOKENS / 1.3) + 1
    max_words = int(MAX_INPUT_TOKENS / 1.3) - 2
    n_words = draw(st.integers(min_value=min_words, max_value=max_words))
    words = draw(st.lists(
        st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=2, max_size=8),
        min_size=n_words, max_size=n_words,
    ))
    return " ".join(words)

valid_target = st.text(min_size=5, max_size=200)


@st.composite
def valid_domain_dp(draw) -> RawDomainDataPoint:
    inp = draw(valid_input())
    tgt = draw(valid_target)
    fmt = draw(valid_format)
    return RawDomainDataPoint(
        input=inp,
        target=tgt,
        metadata={
            "format": fmt,
            "source_file": "01-modul/lesson.md",
            "module_name": "01-modul",
        },
    )


@st.composite
def out_of_range_input_dp(draw) -> RawDomainDataPoint:
    """Data point dengan input di luar range (< MIN atau > MAX token)."""
    too_short = draw(st.booleans())
    if too_short:
        # < MIN_INPUT_TOKENS: 1 kata saja (estimasi 1 token)
        inp = draw(st.text(min_size=1, max_size=3).filter(lambda t: t.strip() and len(t.split()) == 1))
    else:
        # > 1024 token: banyak kata
        n_words = math.ceil((MAX_INPUT_TOKENS + 50) / 1.3)
        words = draw(st.lists(
            st.text(min_size=2, max_size=6),
            min_size=n_words, max_size=n_words + 10,
        ))
        inp = " ".join(words)

    return RawDomainDataPoint(
        input=inp,
        target="Target yang valid dan cukup panjang.",
        metadata={
            "format": "span_corruption",
            "source_file": "01-modul/lesson.md",
            "module_name": "01-modul",
        },
    )


class TestValidatorProperties:

    # Feature: domain-adaptation-dataset, Property 10: Validator rejects out-of-range inputs
    @given(out_of_range_input_dp())
    @settings(max_examples=100, deadline=None)
    def test_property10_rejects_out_of_range_input(self, dp: RawDomainDataPoint):
        """Input < 10 atau > 1024 token → is_valid = False dengan failure_reasons non-empty."""
        token_count = _estimate_tokens(dp.input)
        # Pastikan memang di luar range
        if token_count < MIN_INPUT_TOKENS or token_count > MAX_INPUT_TOKENS:
            result = validate_domain(dp)
            assert not result.is_valid, (
                f"Property 10 gagal: token_count={token_count} seharusnya ditolak"
            )
            assert len(result.failure_reasons) > 0

    # Feature: domain-adaptation-dataset, Property 11: Metadata format enum validity
    @given(valid_domain_dp())
    @settings(max_examples=100, deadline=None)
    def test_property11_valid_dp_has_valid_format(self, dp: RawDomainDataPoint):
        """Setiap data point yang lolos validasi punya metadata.format yang valid."""
        result = validate_domain(dp)
        if result.is_valid:
            assert dp.metadata["format"] in VALID_FORMATS, (
                f"Property 11 gagal: format '{dp.metadata['format']}' tidak valid"
            )
