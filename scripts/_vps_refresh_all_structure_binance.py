"""Refresh all LLM2 pack slices from Binance (1h/4h/1w). Run on VPS."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, "/opt/llm2-structure")
sys.path.insert(0, "/opt/botsgeneral/packages/live_candles/src")
sys.path.insert(0, "/opt/botsgeneral/packages/indicators/src")

from llm2.live.refresh_structure import refresh_symbol

TARGETS = (
    ("BTCUSDT", Path("/opt/llm2-structure/pack/indicators_live_slice.sqlite")),
    ("ETHUSDT", Path("/opt/llm2-structure-eth/pack/indicators_live_slice.sqlite")),
    ("SOLUSDT", Path("/opt/llm2-structure-sol/pack/indicators_live_slice.sqlite")),
    (
        "ETHUSDT",
        Path("/opt/llm2-structure-eth-multitrade-v1_1/pack/indicators_live_slice.sqlite"),
    ),
    (
        "ETHUSDT",
        Path("/opt/llm2-structure-eth-multitrade-v1_2/pack/indicators_live_slice.sqlite"),
    ),
)


def main() -> int:
    reports = []
    rc = 0
    for symbol, db in TARGETS:
        if not db.parent.is_dir():
            print(f"SKIP missing {db}")
            continue
        rep = refresh_symbol(
            symbol=symbol,
            timeframes=("1h", "4h", "1w"),
            indicator_db=db,
            limit=1500,
            source="binance",
        )
        reports.append(rep)
        bad = [s for s in rep["series"] if s.get("error")]
        status = "FAIL" if bad else "OK"
        if bad:
            rc = 1
        print(status, symbol, db, json.dumps(rep["series"], default=str))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
