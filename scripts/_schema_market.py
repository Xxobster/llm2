import sqlite3
from pathlib import Path

p = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
c = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
print(c.execute("pragma table_info(market_ohlcv)").fetchall())
print(c.execute("select sql from sqlite_master where name='market_ohlcv'").fetchone()[0])
print(
    c.execute(
        "select price_type, max(ts_ms), count(*) from market_ohlcv "
        "where symbol='ETHUSDT' and timeframe='15m' and source='binance' group by price_type"
    ).fetchall()
)
