#!/usr/bin/env python3
"""Run on live-network-1: dump pivot state + 15-minute Last candles (no secrets)."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

SINCE = 1786500000000  # ~2026-08-12
DUMP = Path("/tmp/xx7_pivot_live_full.json")
CANDLES = Path("/tmp/vps_15m_eth_sol.json")
UNITS = {
    "sol": "/opt/llm2-pivot-sol-geo-p75-w4/state/pivot_live_state.sqlite",
    "eth": "/opt/llm2-pivot-eth-p75-ctrl-atr-w4/state/pivot_live_state.sqlite",
}


def dump_db(db: str) -> dict:
    p = Path(db)
    if not p.is_file():
        return {"path": db, "exists": False}
    con = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    out: dict = {"path": db, "exists": True, "tables": tables, "counts": {}}
    for t in tables:
        n = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        out["counts"][t] = n
        out[t] = [dict(r) for r in con.execute(f"SELECT * FROM {t}")]
    return out


def series(sym: str) -> list[dict]:
    con = sqlite3.connect("file:/var/lib/botsgeneral/shared_candles.db?mode=ro", uri=True)
    rows = con.execute(
        "SELECT ts_ms, open, high, low, close, volume FROM candles "
        "WHERE exchange=? AND symbol=? AND timeframe=? AND ts_ms>=? ORDER BY ts_ms",
        ("binance", sym, "15m", SINCE),
    ).fetchall()
    return [
        {"ts_ms": int(r[0]), "open": r[1], "high": r[2], "low": r[3], "close": r[4], "volume": r[5]}
        for r in rows
    ]


def main() -> int:
    report = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "sol": dump_db(UNITS["sol"]),
        "eth": dump_db(UNITS["eth"]),
    }
    DUMP.write_text(json.dumps(report, default=str), encoding="utf-8")
    candles = {"ETHUSDT_15m": series("ETHUSDT"), "SOLUSDT_15m": series("SOLUSDT")}
    CANDLES.write_text(json.dumps(candles), encoding="utf-8")
    print("wrote", DUMP, DUMP.stat().st_size, CANDLES, CANDLES.stat().st_size)
    for arm in ("sol", "eth"):
        print(arm, "exists", report[arm].get("exists"), "counts", report[arm].get("counts"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
