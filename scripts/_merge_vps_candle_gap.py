"""Merge VPS-fetched Binance gap bars into the local research warehouse."""
from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from market_data.db import ResearchCandleDB
from llm2.paths import MARKET_DB

GAP = Path(r"d:\projects\LLM2\artifacts\reports\_research_gap_eth_sol.sqlite")


def main() -> int:
    src = sqlite3.connect(f"file:{GAP}?mode=ro", uri=True)
    rows = src.execute(
        "SELECT source, symbol, timeframe, price_type, COUNT(*), MAX(ts_ms) "
        "FROM market_ohlcv GROUP BY 1,2,3,4"
    ).fetchall()
    print("gap series", rows)
    db = ResearchCandleDB(MARKET_DB)
    total = 0
    for source, symbol, timeframe, price_type, _n, _tip in rows:
        df = pd.read_sql_query(
            "SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
            "WHERE source=? AND symbol=? AND timeframe=? AND IFNULL(price_type,'')=IFNULL(?, '') "
            "ORDER BY ts_ms",
            src,
            params=(source, symbol, timeframe, price_type),
        )
        n = db.upsert_df(
            df,
            source=str(source),
            symbol=str(symbol),
            timeframe=str(timeframe),
            price_type=str(price_type) if price_type is not None else None,
            product="USDⓈ-M",
        )
        total += n
        tip = int(df["ts_ms"].iloc[-1]) if len(df) else 0
        print(
            symbol,
            timeframe,
            price_type,
            "upserted",
            n,
            "tip",
            datetime.fromtimestamp(tip / 1000, timezone.utc).isoformat() if tip else None,
            flush=True,
        )
    db.close()
    src.close()
    print("merged_rows", total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
