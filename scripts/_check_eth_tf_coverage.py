import sqlite3
from datetime import datetime, timezone

CANDLE = r"D:\projectsdata\candles\market_ohlcv.sqlite"
IND = r"D:\projectsdata\indicators\indicators.sqlite"


def _fmt(ms: int | None) -> str:
    if ms is None:
        return "None"
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat()


c = sqlite3.connect(CANDLE)
tabs = [r[0] for r in c.execute("select name from sqlite_master where type='table'")]
print("candle tables", tabs)
# guess table
for t in tabs:
    cols = [r[1] for r in c.execute(f"pragma table_info({t})")]
    print(" ", t, cols[:12])
    if "symbol" in cols and "timeframe" in cols:
        for tf in ("1m", "15m", "1h", "4h", "1w"):
            q = (
                f"select source, count(*), min(ts_ms), max(ts_ms) from {t} "
                "where symbol=? and timeframe=? group by 1"
            )
            try:
                rows = c.execute(q, ("ETHUSDT", tf)).fetchall()
            except Exception:
                q = (
                    f"select exchange, count(*), min(ts_ms), max(ts_ms) from {t} "
                    "where symbol=? and timeframe=? group by 1"
                )
                try:
                    rows = c.execute(q, ("ETHUSDT", tf)).fetchall()
                except Exception as e:
                    print("  query fail", tf, e)
                    continue
            for r in rows:
                print("ETH", tf, r[0], "n=", r[1], "min=", _fmt(r[2]), "max=", _fmt(r[3]))
c.close()

i = sqlite3.connect(IND)
print("=== bar_features ETHUSDT ===")
rows = i.execute(
    "select source, timeframe, count(*), min(ts_ms), max(ts_ms) from bar_features "
    "where symbol=? group by 1,2 order by 2",
    ("ETHUSDT",),
).fetchall()
for r in rows:
    print(r[0], r[1], "n=", r[2], "min=", _fmt(r[3]), "max=", _fmt(r[4]))
i.close()
