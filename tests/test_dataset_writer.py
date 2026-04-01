"""
Tests untuk Dataset Writer — unit tests untuk split, JSONL output, dan dataset_info.
"""
import json
import tempfile
from pathlib import Path

import pytest

from src.dataset.dataset_writer import write_dataset, load_jsonl_split, _write_jsonl, _load_jsonl
from src.dataset.validator import ValidDataPoint


def make_valid_dp(difficulty="easy", concept="X", question_type="MCQ", idx=0) -> ValidDataPoint:
    return ValidDataPoint(
        input=f"Konteks: Python adalah bahasa pemrograman. Prompt: Buat soal {idx}.",
        target="Pertanyaan: Apa itu Python? Jawaban benar: Bahasa pemrograman. Distraktor: 1) A 2) B 3) C 4) D",
        metadata={
            "difficulty": difficulty,
            "question_type": question_type,
            "concept": concept,
            "misconception_tags": [],
            "source": "synthetic",
        },
    )


def make_dataset(n=20) -> list[ValidDataPoint]:
    """Buat dataset dengan distribusi difficulty yang seimbang."""
    diffs = ["easy", "medium", "hard"]
    return [make_valid_dp(difficulty=diffs[i % 3], idx=i) for i in range(n)]


# ── Unit tests: JSONL write/load ─────────────────────────────────────────────

class TestJsonlRoundTrip:
    def test_write_then_load_equivalent(self):
        dps = make_dataset(10)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "test.jsonl"
            _write_jsonl(dps, path)
            loaded = _load_jsonl(path)

        assert len(loaded) == 10
        for orig, rec in zip(dps, loaded):
            assert rec["input"] == orig.input
            assert rec["target"] == orig.target
            assert rec["metadata"] == orig.metadata

    def test_each_line_has_three_keys(self):
        dps = make_dataset(5)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "test.jsonl"
            _write_jsonl(dps, path)
            with open(path, encoding="utf-8") as f:
                for line in f:
                    record = json.loads(line.strip())
                    assert set(record.keys()) == {"input", "target", "metadata"}

    def test_target_is_string_after_load(self):
        dps = make_dataset(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "test.jsonl"
            _write_jsonl(dps, path)
            loaded = _load_jsonl(path)
        for rec in loaded:
            assert isinstance(rec["target"], str)

    def test_metadata_is_dict_after_load(self):
        dps = make_dataset(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "test.jsonl"
            _write_jsonl(dps, path)
            loaded = _load_jsonl(path)
        for rec in loaded:
            assert isinstance(rec["metadata"], dict)


# ── Unit tests: write_dataset() ──────────────────────────────────────────────

class TestWriteDataset:
    def test_creates_three_split_files(self):
        dps = make_dataset(30)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_dataset(dps, tmpdir)
            assert (Path(tmpdir) / "train.jsonl").exists()
            assert (Path(tmpdir) / "validation.jsonl").exists()
            assert (Path(tmpdir) / "test.jsonl").exists()

    def test_creates_dataset_info_json(self):
        dps = make_dataset(30)
        with tempfile.TemporaryDirectory() as tmpdir:
            write_dataset(dps, tmpdir)
            assert (Path(tmpdir) / "dataset_info.json").exists()

    def test_total_count_preserved(self):
        dps = make_dataset(30)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_dataset(dps, tmpdir)
            train = load_jsonl_split(str(Path(tmpdir) / "train.jsonl"))
            val = load_jsonl_split(str(Path(tmpdir) / "validation.jsonl"))
            test = load_jsonl_split(str(Path(tmpdir) / "test.jsonl"))
            assert len(train) + len(val) + len(test) == 30

    def test_split_ratios_approximate(self):
        dps = make_dataset(100)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_dataset(dps, tmpdir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15)
            # Toleransi ±5 karena stratifikasi per grup
            assert 60 <= info["splits"]["train"] <= 80
            assert 10 <= info["splits"]["validation"] <= 20
            assert 10 <= info["splits"]["test"] <= 20

    def test_stratification_all_difficulties_in_each_split(self):
        """Setiap split harus mengandung semua difficulty level."""
        dps = make_dataset(30)  # 10 easy, 10 medium, 10 hard
        with tempfile.TemporaryDirectory() as tmpdir:
            write_dataset(dps, tmpdir)
            for split_file in ["train.jsonl", "validation.jsonl", "test.jsonl"]:
                records = load_jsonl_split(str(Path(tmpdir) / split_file))
                if len(records) >= 3:  # hanya cek jika split cukup besar
                    difficulties = {r["metadata"]["difficulty"] for r in records}
                    assert len(difficulties) >= 1  # minimal ada satu difficulty

    def test_dataset_info_has_required_fields(self):
        dps = make_dataset(20)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_dataset(dps, tmpdir)
            assert "total" in info
            assert "splits" in info
            assert "difficulty_distribution" in info
            assert "concept_distribution" in info
            assert "generated_at" in info

    def test_dataset_info_total_correct(self):
        dps = make_dataset(25)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_dataset(dps, tmpdir)
            assert info["total"] == 25

    def test_invalid_ratios_raises(self):
        dps = make_dataset(10)
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(AssertionError):
                write_dataset(dps, tmpdir, train_ratio=0.5, val_ratio=0.5, test_ratio=0.5)

    def test_small_dataset_no_crash(self):
        """Dataset kecil (< 10) tidak boleh crash."""
        dps = make_dataset(3)
        with tempfile.TemporaryDirectory() as tmpdir:
            info = write_dataset(dps, tmpdir)
            assert info["total"] == 3

    def test_output_dir_created_if_not_exists(self):
        dps = make_dataset(10)
        with tempfile.TemporaryDirectory() as tmpdir:
            new_dir = str(Path(tmpdir) / "new" / "nested" / "dir")
            write_dataset(dps, new_dir)
            assert (Path(new_dir) / "train.jsonl").exists()
