import sqlite3
from datetime import datetime, timezone
from pathlib import Path

db = Path("/opt/llm2-structure/pack/indicators_live_slice.sqlite")
con = sqlite3.connect(db)
print("size_mb", db.stat().st_size / 1e6)
print(
    "by_source",
    con.execute(
        "select source, count(*), min(ts_ms), max(ts_ms) from bar_features "
        "where symbol='BTCUSDT' and timeframe='1h' group by source"
    ).fetchall(),
)
rows = con.execute(
    "select ts_ms, source, dist_last_sh_pct, struct_dir from bar_features "
    "where symbol='BTCUSDT' and timeframe='1h' order by ts_ms desc limit 12"
).fetchall()
for r in rows:
    print(datetime.fromtimestamp(r[0] / 1000, tz=timezone.utc), r[1], r[2], r[3])
