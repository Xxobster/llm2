"""Summarize LLM2 production bar-close → decision timings."""
from __future__ import annotations

import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median

log = Path("/opt/llm2-structure/logs/micro_live.log")
lines = log.read_text(errors="ignore").splitlines()
totals, refresh, decide = [], [], []
for ln in lines:
    if "timing_ms=" not in ln:
        continue
    m = re.search(r"timing_ms=(\{.*\})", ln)
    if not m:
        continue
    t = eval(m.group(1), {"__builtins__": {}})
    totals.append(float(t.get("total", 0)))
    refresh.append(float(t.get("refresh", 0)))
    decide.append(float(t.get("decide", 0)))


def stats(name: str, xs: list[float]) -> None:
    if not xs:
        print(name, "no samples")
        return
    xs2 = sorted(xs)
    print(
        f"{name}: n={len(xs)} min={min(xs):.0f} med={median(xs):.0f} "
        f"avg={mean(xs):.0f} p90={xs2[int(0.9*(len(xs2)-1))]:.0f} max={max(xs):.0f} ms"
    )


print("=== LLM2 structure_v1 micro-live hot-path (from DECISION timing_ms) ===")
stats("total", totals)
stats("refresh", refresh)
stats("decide_plus_mark", decide)

con = sqlite3.connect("/opt/llm2-structure/state/micro_live_state.sqlite")
rows = con.execute(
    "select bar_ts_ms, decided_utc, side, pred_mean, detail from decisions order by bar_ts_ms"
).fetchall()
print(f"\n=== Decisions in state DB: {len(rows)} ===")
print("bar_open_utc | lag_after_close_s | side | pred | timing | skip/order")
for bar_ms, decided, side, pred, detail in rows:
    close_ms = bar_ms + 3_600_000
    d = datetime.fromisoformat(decided)
    lag = (d - datetime.fromtimestamp(close_ms / 1000, tz=timezone.utc)).total_seconds()
    det = json.loads(detail or "{}")
    print(
        f"{datetime.fromtimestamp(bar_ms/1000, tz=timezone.utc).isoformat()} | "
        f"{lag:.1f}s | side={side} pred={pred} | timing={det.get('timing_ms')} | "
        f"skip={det.get('skip_reason')} order={det.get('order_retCode')} "
        f"order_err={det.get('order_error')}"
    )

# Estimate order REST if any later appear: currently always SKIP while Sell open.
print(
    "\nNote: when a position is already open, no new order is placed. "
    "Order place REST on Bybit is separate (~100-400 ms typical if entry path runs)."
)
