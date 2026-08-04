"""Print LLM2 production refresh timings and why skips may fail."""
from __future__ import annotations

import re
import sqlite3
from pathlib import Path
from statistics import median

log = Path("/opt/llm2-structure/logs/micro_live.log")
rows = []
for ln in log.read_text(errors="ignore").splitlines():
    if "timing_ms=" not in ln:
        continue
    m = re.search(r"DECISION bar=([^ ]+ [^ ]+) .*timing_ms=(\{.*\})", ln)
    if not m:
        continue
    t = eval(m.group(2), {"__builtins__": {}})
    rows.append(
        (
            m.group(1),
            float(t.get("refresh", 0)),
            float(t.get("decide", 0)),
            float(t.get("total", 0)),
            t.get("refresh_skipped"),
        )
    )

print("bar | refresh_ms | decide_ms | total_ms | skipped")
for bar, r, d, tot, sk in rows:
    flag = "SLOW" if r >= 5000 else ("ok" if r < 2000 else "mid")
    print(f"{bar} | {r:7.0f} | {d:6.0f} | {tot:7.0f} | skip={sk} | {flag}")

fast = [r for _, r, _, _, _ in rows if r < 2000]
slow = [r for _, r, _, _, _ in rows if r >= 5000]
print()
print(f"n={len(rows)} fast(<2s)={len(fast)} slow(>=5s)={len(slow)}")
if fast:
    print(f"fast refresh median={median(fast):.0f}ms")
if slow:
    print(f"slow refresh median={median(slow):.0f}ms first_slow={next(b for b,r,_,_,_ in rows if r>=5000)}")

db = Path("/opt/llm2-structure/pack/indicators_live_slice.sqlite")
print(f"\ndb_size_mb={db.stat().st_size/1e6:.1f}")
con = sqlite3.connect(db)
print(
    "by source/tf:",
    con.execute(
        "select source, timeframe, count(*) n from bar_features "
        "group by source, timeframe order by source, timeframe"
    ).fetchall(),
)
# show unit env
unit = Path("/etc/systemd/system/llm2-structure-micro.service").read_text()
print("\nunit env lines:")
for ln in unit.splitlines():
    if "Environment=" in ln or "ExecStart=" in ln:
        print(ln)
