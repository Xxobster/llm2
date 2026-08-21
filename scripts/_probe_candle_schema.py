import sqlite3
from pathlib import Path

p = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
c = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print("tables", tables)
for t in tables:
    cols = [x[1] for x in c.execute(f"PRAGMA table_info({t})")]
    print(t, cols)
    if "symbol" in cols:
        try:
            print(
                "ETH rows",
                c.execute(
                    f"SELECT source, timeframe, COUNT(*) FROM {t} "
                    "WHERE symbol='ETHUSDT' GROUP BY 1,2"
                ).fetchall()[:20],
            )
        except Exception as exc:
            print("err", exc)
