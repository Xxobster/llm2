import sqlite3
from datetime import datetime, timezone

db = "/var/lib/botsgeneral/shared_candles.db"
con = sqlite3.connect(db)
tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print("tables", tables)
# try common schemas
for sql in (
    "SELECT symbol, timeframe, COUNT(*), MAX(ts_ms) FROM candles GROUP BY 1,2 ORDER BY 1,2",
    "SELECT symbol, interval, COUNT(*), MAX(open_time) FROM ohlcv GROUP BY 1,2 ORDER BY 1,2",
    "SELECT symbol, tf, COUNT(*), MAX(ts) FROM bars GROUP BY 1,2 ORDER BY 1,2",
):
    try:
        rows = con.execute(sql).fetchall()
        print("SQL_OK", sql.split("FROM")[1].split()[0], "n=", len(rows))
        for r in rows[:50]:
            ts = r[3]
            if ts and ts > 10_000_000_000:
                ts = ts / 1000
            dt = datetime.fromtimestamp(ts, tz=timezone.utc) if ts else None
            print(r[0], r[1], r[2], dt)
        break
    except Exception as e:
        print("SQL_FAIL", type(e).__name__, e)
