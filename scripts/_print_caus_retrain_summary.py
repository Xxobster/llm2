"""Pretty-print structure_v1_caus_retrain_001_latest.json."""
from __future__ import annotations
import json
from pathlib import Path

p = Path("artifacts/reports/structure_v1_caus_retrain_001_latest.json")
d = json.loads(p.read_text(encoding="utf-8"))
print(f"generation={d['generation_id']} stamp={d['stamp']}")
print(f"prereg_sha={d['preregister_sha256'][:24]}…")
print(f"leakage_gates={ {k: v.get('ok') for k, v in d['leakage'].items()} }")
print(f"readiness_max={d['readiness_max']}")
print()
print(f"{'symbol':8} {'target':12} {'model':16} {'pf':>8} {'trades':>7} {'overall':8}")
print("-" * 64)
for r in d["rows"]:
    pf = r.get("pooled_pf")
    print(
        f"{r['symbol']:8} {r['target']:12} {str(r.get('model') or '-'):16} "
        f"{(pf if pf is not None else float('nan')):8.3f} "
        f"{int(r.get('pooled_trades') or 0):7d} {r.get('overall')}"
    )
print()
print("All pre-2026-08-06 structure_v1 numbers remain void.")
