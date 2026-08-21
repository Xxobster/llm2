from __future__ import annotations

import sqlite3
from datetime import datetime, timezone


def main() -> None:
    con = sqlite3.connect(r"file:D:/projectsdata/candles/market_ohlcv.sqlite?mode=ro", uri=True)
    for tf in ("15m", "1h", "4h"):
        rows = con.execute(
            """
            SELECT price_type, COUNT(*), MAX(ts_ms), MIN(ts_ms)
            FROM market_ohlcv
            WHERE symbol='ETHUSDT' AND timeframe=? AND source='binance'
            GROUP BY price_type
            """,
            (tf,),
        ).fetchall()
        print(tf)
        for r in rows:
            mx = datetime.fromtimestamp(r[2] / 1000, tz=timezone.utc) if r[2] else None
            mn = datetime.fromtimestamp(r[3] / 1000, tz=timezone.utc) if r[3] else None
            print(f"  {r[0]} n={r[1]} max={mx} min={mn}")
    con.close()


if __name__ == "__main__":
    main()
