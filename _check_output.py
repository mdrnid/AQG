import json
from pathlib import Path
from collections import Counter

output_dir = Path("dataset_aqg/output_domain")

print("=== FILES ===")
for f in sorted(output_dir.iterdir()):
    if f.is_file():
        print(f"  {f.name:35s} {f.stat().st_size:>8} bytes")

acc = output_dir / "accumulated.jsonl"
if acc.exists():
    records = [json.loads(l) for l in acc.read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"\n=== ACCUMULATED: {len(records)} records ===")
    fmt_dist = Counter(r["metadata"]["format"] for r in records)
    mod_dist = Counter(r["metadata"]["module_name"] for r in records)
    print("Format distribution:")
    for k, v in sorted(fmt_dist.items()):
        print(f"  {k:25s}: {v}")
    print("Module distribution:")
    for k, v in sorted(mod_dist.items()):
        print(f"  {k:40s}: {v}")

for split in ["train", "validation", "test"]:
    f = output_dir / f"{split}.jsonl"
    if f.exists():
        n = sum(1 for l in f.read_text(encoding="utf-8").splitlines() if l.strip())
        print(f"{split:12s}: {n} records")

info_f = output_dir / "dataset_info.json"
if info_f.exists():
    info = json.loads(info_f.read_text(encoding="utf-8"))
    print("\n=== DATASET INFO ===")
    print(json.dumps(info, indent=2, ensure_ascii=False))
