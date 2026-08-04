"""Print lag from bar close to decision for llm2 structure micro-live."""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

con = sqlite3.connect("/opt/llm2-structure/state/micro_live_state.sqlite")
rows = con.execute(
    "select bar_ts_ms, decided_utc, side, pred_mean from decisions order by bar_ts_ms"
).fetchall()
print("bar_open_utc | bar_close_utc | decided_utc | lag_after_close_s | side | pred")
for bar_ms, decided, side, pred in rows:
    close_ms = bar_ms + 3_600_000
    open_utc = datetime.fromtimestamp(bar_ms / 1000, tz=timezone.utc).isoformat()
    close_utc = datetime.fromtimestamp(close_ms / 1000, tz=timezone.utc).isoformat()
    d = datetime.fromisoformat(decided)
    lag = (d - datetime.fromtimestamp(close_ms / 1000, tz=timezone.utc)).total_seconds()
    print(f"{open_utc} | {close_utc} | {decided} | {lag:.1f}s | side={side} | pred={pred}")
