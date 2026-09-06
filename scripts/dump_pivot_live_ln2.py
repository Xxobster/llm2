#!/usr/bin/env python3
"""Run on live-network-2: dump Xxobster8/9 pivot state + 15-minute Last (no secrets)."""
from __future__ import annotations

import json
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path

SINCE = 1787241600000  # 2026-08-20 00:00 UTC
DUMP = Path("/tmp/ln2_xx89_pivot_live.json")
CANDLES = Path("/tmp/ln2_15m_eth_sol.json")
UNITS = {
    "xx8_eth": "/opt/llm2-pivot-eth-p75-ctrl-atr-w4",
    "xx8_sol": "/opt/llm2-pivot-sol-geo-p75-w4",
    "xx9_eth": "/opt/llm2-pivot-eth-p50-tp05-sl05",
    "xx9_sol": "/opt/llm2-pivot-sol-p50-tp05-sl05",
}
SYSTEMD = {
    "xx8_eth": "llm2-pivot-eth-p75-ctrl-atr-w4",
    "xx8_sol": "llm2-pivot-sol-geo-p75-w4",
    "xx9_eth": "llm2-pivot-eth-p50-tp05-sl05",
    "xx9_sol": "llm2-pivot-sol-p50-tp05-sl05",
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
    units = {}
    for k, u in SYSTEMD.items():
        units[k] = subprocess.check_output(
            ["bash", "-lc", f"systemctl is-active {u} || true"], text=True
        ).strip()
    con = sqlite3.connect("file:/var/lib/botsgeneral/shared_candles.db?mode=ro", uri=True)
    one_m = con.execute(
        "SELECT COUNT(*) FROM candles WHERE timeframe IN ('1m','1min')"
    ).fetchone()[0]
    tips = {}
    for sym in ("ETHUSDT", "SOLUSDT"):
        tips[sym] = con.execute(
            "SELECT MAX(ts_ms) FROM candles WHERE exchange='binance' AND symbol=? AND timeframe='15m'",
            (sym,),
        ).fetchone()[0]
    arms = {k: dump_db(f"{root}/state/pivot_live_state.sqlite") for k, root in UNITS.items()}
    report = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "units": units,
        "one_m_rows": one_m,
        "tips_15m": tips,
        "arms": arms,
    }
    DUMP.write_text(json.dumps(report, default=str), encoding="utf-8")
    candles = {"ETHUSDT_15m": series("ETHUSDT"), "SOLUSDT_15m": series("SOLUSDT")}
    CANDLES.write_text(json.dumps(candles), encoding="utf-8")
    print("units", units)
    print("one_m", one_m, "tips", tips)
    print("counts", {k: v.get("counts") for k, v in arms.items()})
    print("wrote", DUMP, DUMP.stat().st_size, CANDLES, CANDLES.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
