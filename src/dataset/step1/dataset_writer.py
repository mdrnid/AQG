"""
Domain Dataset Writer: split 80/10/10 dan simpan ke JSONL + dataset_info.json.
Stratifikasi berdasarkan 'format' untuk memastikan semua format terwakili di setiap split.
"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

from src.dataset.step1.validator import ValidDomainDataPoint


def _write_jsonl(datapoints: List[ValidDomainDataPoint], filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        for dp in datapoints:
            record = {
                "input": dp.input,
                "target": dp.target,
                "metadata": dp.metadata,
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def load_domain_jsonl(filepath: str) -> List[dict]:
    """Load JSONL file dan kembalikan list of dict."""
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def _stratified_split(
    datapoints: List[ValidDomainDataPoint],
    train_ratio: float,
    val_ratio: float,
    stratify_by: str,
    seed: int = 42,
) -> Tuple[List[ValidDomainDataPoint], List[ValidDomainDataPoint], List[ValidDomainDataPoint]]:
    """
    Split dengan stratifikasi — memastikan setiap nilai stratify_by ada di setiap split.
    """
    rng = random.Random(seed)

    groups: Dict[str, List[ValidDomainDataPoint]] = defaultdict(list)
    for dp in datapoints:
        key = dp.metadata.get(stratify_by, "unknown")
        groups[key].append(dp)

    train_all, val_all, test_all = [], [], []

    for key, group in groups.items():
        rng.shuffle(group)
        n = len(group)
        n_train = max(1, int(n * train_ratio))
        n_val = max(1, int(n * val_ratio))

        if n == 1:
            train_all.extend(group)
        elif n == 2:
            train_all.append(group[0])
            val_all.append(group[1])
        else:
            train_all.extend(group[:n_train])
            val_all.extend(group[n_train:n_train + n_val])
            test_all.extend(group[n_train + n_val:])

    rng.shuffle(train_all)
    rng.shuffle(val_all)
    rng.shuffle(test_all)

    return train_all, val_all, test_all


def _compute_distribution(datapoints: List[ValidDomainDataPoint], field: str) -> Dict[str, int]:
    dist: Dict[str, int] = defaultdict(int)
    for dp in datapoints:
        key = dp.metadata.get(field, "unknown")
        dist[str(key)] += 1
    return dict(sorted(dist.items()))


def write_domain_dataset(
    datapoints: List[ValidDomainDataPoint],
    output_dir: str,
    train_ratio: float = 0.80,
    val_ratio: float = 0.10,
    test_ratio: float = 0.10,
    stratify_by: str = "format",
    seed: int = 42,
) -> dict:
    """
    Split dan simpan dataset domain adaptation ke JSONL files.

    Returns:
        dict: dataset_info yang disimpan ke dataset_info.json
    """
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6, \
        "train_ratio + val_ratio + test_ratio harus = 1.0"

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    train, val, test = _stratified_split(
        datapoints, train_ratio, val_ratio, stratify_by, seed
    )

    _write_jsonl(train, out_path / "train.jsonl")
    _write_jsonl(val, out_path / "validation.jsonl")
    _write_jsonl(test, out_path / "test.jsonl")

    info = {
        "total": len(datapoints),
        "splits": {
            "train": len(train),
            "validation": len(val),
            "test": len(test),
        },
        "format_distribution": _compute_distribution(datapoints, "format"),
        "module_distribution": _compute_distribution(datapoints, "module_name"),
        "generated_at": str(date.today()),
    }

    with open(out_path / "dataset_info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

    return info
