from pathlib import Path
import sqlite3

from llm2.data.loader import load_ohlcv

df = load_ohlcv("ETHUSDT", "15m")
print("loader tip", df.index.max(), "n", len(df))
p = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
con = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
rows = con.execute(
    "SELECT source, timeframe, MAX(ts_ms), COUNT(*) FROM market_ohlcv "
    "WHERE symbol='ETHUSDT' AND timeframe IN ('15m','1h','1m','4h') "
    "GROUP BY source, timeframe ORDER BY timeframe, source"
).fetchall()
for r in rows:
    print(r)
con.close()
