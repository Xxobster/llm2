"""Fetch ETH/SOL 15m+1m Last and Mark without overwriting Last.

Last  -> source=binance,      price_type=last
Mark  -> source=binance_mark, price_type=mark_price
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
if "botsgeneral" not in __import__("tradesim").__file__.replace("\\", "/"):
    raise SystemExit("tradesim must load from botsgeneral")

from market_data.db import ResearchCandleDB
from market_data.fetch_binance import fetch_klines
from llm2.paths import MARKET_DB

START = int(datetime(2026, 8, 1, tzinfo=timezone.utc).timestamp() * 1000)
SYMBOLS = ("ETHUSDT", "SOLUSDT")
TFS = ("15m", "1m")
JOBS = (
    ("last", "binance", "last", "/fapi/v1/klines"),
    ("mark", "binance_mark", "mark_price", "/fapi/v1/markPriceKlines"),
)


def main() -> int:
    db = ResearchCandleDB(MARKET_DB)
    for sym in SYMBOLS:
        for tf in TFS:
            for pt, source, label, endpoint in JOBS:
                print(f"fetch {sym} {tf} {pt} -> {source}", flush=True)
                df = fetch_klines(
                    sym,
                    tf,
                    market="binance",
                    price_type=pt,
                    start_ms=START,
                    drop_incomplete=True,
                    drop_junk=True,
                )
                n = db.upsert_df(
                    df,
                    source=source,
                    symbol=sym,
                    timeframe=tf,
                    price_type=label,
                    product="USDⓈ-M",
                    source_endpoint=endpoint,
                )
                tip = int(df["ts_ms"].iloc[-1]) if len(df) else 0
                print(
                    f"  upserted={n} tip={datetime.fromtimestamp(tip / 1000, timezone.utc).isoformat() if tip else None}",
                    flush=True,
                )
    db.close()
    print("ok", MARKET_DB)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
