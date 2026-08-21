"""Rebuild every structure series in the research warehouse with the causal retrace.

CAUS-STRUCT-001 changed when a leg's retracement is published, so every stored
``last_retrace_pct`` (and its fib label) computed before the fix is look-ahead and
must be recomputed. Live pack slices are rebuilt hourly from the same code, so once
this finishes the two sides compute the identical value for a given bar.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")

from indicators import update_series  # noqa: E402
from indicators.store import IndicatorDB  # noqa: E402

FLEET_FIRST = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TIMEFRAMES = ("1h", "4h", "1w", "15m")


def existing_series() -> list[tuple[str, str]]:
    db = IndicatorDB()
    import sqlite3

    con = sqlite3.connect(f"file:{db.path}?mode=ro", uri=True)
    rows = con.execute(
        "SELECT DISTINCT symbol, timeframe FROM bar_features ORDER BY symbol, timeframe"
    ).fetchall()
    con.close()
    return [(str(s), str(t)) for s, t in rows]


def main() -> int:
    series = existing_series()
    print(f"warehouse series: {len(series)}")
    ordered = sorted(
        series,
        key=lambda st: (st[0] not in FLEET_FIRST, st[0], TIMEFRAMES.index(st[1]) if st[1] in TIMEFRAMES else 9),
    )
    t0 = time.perf_counter()
    ok = fail = 0
    for sym, tf in ordered:
        t1 = time.perf_counter()
        try:
            r = update_series(sym, tf, source="binance")
            status = r.error or "ok"
            n = r.n_bars
        except Exception as exc:  # noqa: BLE001
            status = f"EXC {type(exc).__name__}: {exc}"
            n = 0
        if status == "ok":
            ok += 1
        else:
            fail += 1
        print(
            f"{sym:10s} {tf:4s} n={n:8d} {status}  ({time.perf_counter() - t1:.1f}s)",
            flush=True,
        )
    print(f"DONE ok={ok} fail={fail} in {time.perf_counter() - t0:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
