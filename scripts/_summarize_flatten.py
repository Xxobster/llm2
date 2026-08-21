"""Summarize a flatten JSON report."""
from __future__ import annotations
import json
import sys
from pathlib import Path

p = Path(sys.argv[1])
d = json.loads(p.read_text(encoding="utf-8"))
print(f"host={d.get('host')} execute={d.get('execute')} utc={d.get('utc')}")
all_flat = True
for a in d.get("accounts", []):
    if a.get("error"):
        print(f"  {a['account']}: ERROR {a['error']}")
        all_flat = False
        continue
    before = a.get("before", {})
    after = a.get("after", {})
    n_close_ok = sum(1 for c in a.get("closes", []) if c.get("retCode") == 0)
    n_close_fail = sum(
        1 for c in a.get("closes", []) if c.get("retCode") not in (None, 0) or c.get("error")
    )
    n_cancel = len(a.get("cancels", []))
    flat = bool(a.get("flat"))
    all_flat = all_flat and flat
    print(
        f"  {a['account']}: flat={flat} "
        f"pos {len(before.get('positions', []))}->{len(after.get('positions', []))} "
        f"orders {before.get('n_orders')}->{after.get('n_orders')} "
        f"cancels={n_cancel} closes_ok={n_close_ok} closes_fail={n_close_fail}"
    )
    for pos in after.get("positions") or []:
        print(f"    STILL OPEN {pos}")
print("ALL_FLAT" if all_flat else "NOT_FLAT")
