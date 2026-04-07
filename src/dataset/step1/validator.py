"""
Domain Validator: memvalidasi RawDomainDataPoint sebelum masuk ke dataset final.
Lebih longgar dari AQG validator karena format domain adaptation lebih beragam.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from src.dataset.step1.formatter import RawDomainDataPoint

VALID_FORMATS = {"span_corruption", "summarization", "qa_generic"}
REQUIRED_METADATA_FIELDS = {"format", "source_file", "module_name"}

MIN_INPUT_TOKENS = 5   # QA input pendek seperti "Apa itu list dalam Python?" valid
MAX_INPUT_TOKENS = 1024
MIN_TARGET_CHARS = 5


def _estimate_tokens(text: str) -> int:
    return max(1, int(len(text.split()) * 1.3))


@dataclass
class DomainValidationResult:
    is_valid: bool
    failure_reasons: List[str] = field(default_factory=list)


@dataclass
class ValidDomainDataPoint:
    input: str
    target: str
    metadata: dict


def validate_domain(datapoint: RawDomainDataPoint) -> DomainValidationResult:
    """
    Validasi satu domain data point.

    Aturan:
    - input: 10–1024 token
    - target: non-empty string (minimal 5 karakter)
    - metadata.format: hanya span_corruption | summarization | qa_generic
    - metadata.source_file: non-empty string
    - metadata.module_name: non-empty string
    """
    reasons: List[str] = []

    # 1. Cek panjang input
    input_tokens = _estimate_tokens(datapoint.input)
    if input_tokens < MIN_INPUT_TOKENS:
        reasons.append(
            f"input terlalu pendek: {input_tokens} token (min {MIN_INPUT_TOKENS})"
        )
    if input_tokens > MAX_INPUT_TOKENS:
        reasons.append(
            f"input terlalu panjang: {input_tokens} token (max {MAX_INPUT_TOKENS})"
        )

    # 2. Cek target non-empty
    if not isinstance(datapoint.target, str) or len(datapoint.target.strip()) < MIN_TARGET_CHARS:
        reasons.append(
            f"target harus string non-empty minimal {MIN_TARGET_CHARS} karakter"
        )

    # 3. Cek metadata adalah dict
    if not isinstance(datapoint.metadata, dict):
        reasons.append(f"metadata harus dict, bukan {type(datapoint.metadata).__name__}")
    else:
        # 4. Cek required fields
        for fname in REQUIRED_METADATA_FIELDS:
            val = datapoint.metadata.get(fname)
            if not val or (isinstance(val, str) and not val.strip()):
                reasons.append(f"metadata.{fname} harus non-empty string")

        # 5. Cek enum format
        fmt = datapoint.metadata.get("format")
        if fmt is not None and fmt not in VALID_FORMATS:
            reasons.append(
                f"metadata.format tidak valid: '{fmt}' "
                f"(harus salah satu dari {sorted(VALID_FORMATS)})"
            )

    return DomainValidationResult(is_valid=len(reasons) == 0, failure_reasons=reasons)


def validate_domain_batch(
    datapoints: List[RawDomainDataPoint],
) -> Tuple[List[ValidDomainDataPoint], List[dict]]:
    """
    Validasi batch. Kembalikan (valid_list, failure_log).
    failure_log: list of dict dengan field 'reasons' dan 'raw_datapoint'.
    """
    valid_list: List[ValidDomainDataPoint] = []
    failure_log: List[dict] = []

    for dp in datapoints:
        result = validate_domain(dp)
        if result.is_valid:
            valid_list.append(ValidDomainDataPoint(
                input=dp.input,
                target=dp.target,
                metadata=dp.metadata,
            ))
        else:
            failure_log.append({
                "reasons": result.failure_reasons,
                "raw_datapoint": {
                    "input": dp.input[:200],
                    "target": dp.target[:200],
                    "metadata": dp.metadata,
                },
            })

    return valid_list, failure_log


def domain_validation_report(
    total: int,
    valid_list: List[ValidDomainDataPoint],
    failure_log: List[dict],
) -> dict:
    """Ringkasan laporan validasi domain."""
    reason_counts: dict = {}
    for entry in failure_log:
        for reason in entry["reasons"]:
            key = reason.split(":")[0].strip()
            reason_counts[key] = reason_counts.get(key, 0) + 1

    return {
        "total_processed": total,
        "passed": len(valid_list),
        "failed": len(failure_log),
        "pass_rate": round(len(valid_list) / total * 100, 1) if total > 0 else 0.0,
        "failure_reason_summary": reason_counts,
    }
