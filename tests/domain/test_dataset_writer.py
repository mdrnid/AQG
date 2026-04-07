"""
Tests untuk src/dataset/step1/dataset_writer.py
Unit tests + property-based tests (Property 8, 9).
"""
import json
import tempfile
from pathlib import Path

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

from src.dataset.step1.validator import ValidDomainDataPoint
from src.dataset.step1.dataset_writer import write_domain_dataset, load_domain_jsonl
from src.dataset.step1.validator import VALID_FORMATS


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_valid_dp(
    input_text: str = "input teks yang cukup panjang untuk diproses",
    target: str = "target teks yang valid",
    fmt: str = "span_corruption",
    module_name: str = "01-modul",
) -> ValidDomainDataPoint:
    return ValidDomainDataPoint(
        input=input_text,
        target=target,
        metadata={
            "format": fmt,
            "source_file": f"{module_name}/lesson.md",
            "module_name": module_name,
        },
    )


def make_dataset_all_formats(n_per_format: int = 5) -> list:
    """Buat dataset dengan semua format terwakili."""
    dps = []
    for fmt in sorted(VALID_FORMATS):
        for i in range(n_per_format):
            dps.append(make_valid_dp(
                input_text=f"input {fmt} {i} " + "kata " * 10,
                target=f"target {fmt} {i}",
                fmt=fmt,
            ))
    return dps


# ---------------------------------------------------------------------------
# Unit Tests — write_domain_dataset
# ---------------------------------------------------------------------------

class TestWriteDomainDataset:

    def test_creates_three_jsonl_files(self):
        dps = make_dataset_all_formats(5)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            assert (Path(tmpdir) / "train.jsonl").exists()
            assert (Path(tmpdir) / "validation.jsonl").exists()
            assert (Path(tmpdir) / "test.jsonl").exists()

    def test_creates_dataset_info_json(self):
        dps = make_dataset_all_formats(5)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            info_path = Path(tmpdir) / "dataset_info.json"
            assert info_path.exists()
            with open(info_path) as f:
                info = json.load(f)
            assert "total" in info
            assert "splits" in info
            assert "format_distribution" in info
            assert "module_distribution" in info
            assert "generated_at" in info

    def test_total_count_matches(self):
        dps = make_dataset_all_formats(4)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_domain_dataset(dps, tmpdir)
            total_in_splits = (
                info["splits"]["train"]
                + info["splits"]["validation"]
                + info["splits"]["test"]
            )
            assert total_in_splits == len(dps)

    def test_each_line_has_three_keys(self):
        dps = make_dataset_all_formats(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            for split in ("train", "validation", "test"):
                records = load_domain_jsonl(str(Path(tmpdir) / f"{split}.jsonl"))
                for rec in records:
                    assert set(rec.keys()) == {"input", "target", "metadata"}, (
                        f"Split {split}: keys tidak sesuai: {set(rec.keys())}"
                    )

    def test_target_is_string_in_jsonl(self):
        dps = make_dataset_all_formats(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            for split in ("train", "validation", "test"):
                records = load_domain_jsonl(str(Path(tmpdir) / f"{split}.jsonl"))
                for rec in records:
                    assert isinstance(rec["target"], str)

    def test_metadata_is_dict_in_jsonl(self):
        dps = make_dataset_all_formats(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            for split in ("train", "validation", "test"):
                records = load_domain_jsonl(str(Path(tmpdir) / f"{split}.jsonl"))
                for rec in records:
                    assert isinstance(rec["metadata"], dict)

    def test_ratio_assertion_error(self):
        dps = make_dataset_all_formats(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(AssertionError):
                write_domain_dataset(dps, tmpdir, train_ratio=0.5, val_ratio=0.3, test_ratio=0.3)


# ---------------------------------------------------------------------------
# Unit Tests — stratification
# ---------------------------------------------------------------------------

class TestStratification:

    def test_all_formats_in_train_split(self):
        """Setiap format harus ada di train split."""
        dps = make_dataset_all_formats(5)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            train_records = load_domain_jsonl(str(Path(tmpdir) / "train.jsonl"))
            train_formats = {r["metadata"]["format"] for r in train_records}
            assert train_formats == VALID_FORMATS

    def test_format_distribution_in_info(self):
        dps = make_dataset_all_formats(4)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_domain_dataset(dps, tmpdir)
            for fmt in VALID_FORMATS:
                assert fmt in info["format_distribution"]


# ---------------------------------------------------------------------------
# Property-Based Tests
# ---------------------------------------------------------------------------

@st.composite
def dataset_with_all_formats(draw) -> list:
    """Generate dataset yang mengandung semua format, minimal 3 per format."""
    n_per_format = draw(st.integers(min_value=3, max_value=10))
    dps = []
    for fmt in sorted(VALID_FORMATS):
        for i in range(n_per_format):
            dps.append(ValidDomainDataPoint(
                input=f"input {fmt} {i} " + "kata " * 10,
                target=f"target {fmt} {i} yang cukup panjang",
                metadata={
                    "format": fmt,
                    "source_file": f"01-modul/lesson_{i}.md",
                    "module_name": "01-modul",
                },
            ))
    return dps


class TestDatasetWriterProperties:

    # Feature: domain-adaptation-dataset, Property 8: JSONL round-trip consistency
    @given(dataset_with_all_formats())
    @settings(max_examples=50, deadline=None)
    def test_property8_jsonl_roundtrip(self, dps: list):
        """Write then load menghasilkan data equivalent dengan tipe yang benar."""
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            for split in ("train", "validation", "test"):
                fpath = str(Path(tmpdir) / f"{split}.jsonl")
                records = load_domain_jsonl(fpath)
                for rec in records:
                    # Tiga key persis
                    assert set(rec.keys()) == {"input", "target", "metadata"}, (
                        f"Property 8 gagal: keys={set(rec.keys())}"
                    )
                    # input dan target adalah string
                    assert isinstance(rec["input"], str), "Property 8: input bukan string"
                    assert isinstance(rec["target"], str), "Property 8: target bukan string"
                    # metadata adalah dict
                    assert isinstance(rec["metadata"], dict), "Property 8: metadata bukan dict"

    # Feature: domain-adaptation-dataset, Property 9: Split stratification by format
    @given(dataset_with_all_formats())
    @settings(max_examples=50, deadline=None)
    def test_property9_split_stratification(self, dps: list):
        """Setiap split mengandung minimal satu entry per format yang ada di dataset."""
        formats_in_dataset = {dp.metadata["format"] for dp in dps}
        with tempfile.TemporaryDirectory() as tmpdir:
            write_domain_dataset(dps, tmpdir)
            for split in ("train", "validation", "test"):
                fpath = str(Path(tmpdir) / f"{split}.jsonl")
                records = load_domain_jsonl(fpath)
                if not records:
                    continue  # skip split kosong (dataset sangat kecil)
                formats_in_split = {r["metadata"]["format"] for r in records}
                for fmt in formats_in_dataset:
                    assert fmt in formats_in_split, (
                        f"Property 9 gagal: format '{fmt}' tidak ada di split '{split}'"
                    )
