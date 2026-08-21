"""Pull ETHUSDT tip candles from VPS shared_candles into local market_ohlcv (price_type=last)."""

from __future__ import annotations

import json
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from llm2.paths import MARKET_DB  # noqa: E402

HOST = "185.203.119.52"
TFS = ("15m", "1h", "4h", "1m")
SYMBOL = "ETHUSDT"

REMOTE = r"""
import json, sqlite3
con = sqlite3.connect('/var/lib/botsgeneral/shared_candles.db')
out = {}
for tf in ['15m','1h','4h','1m']:
    rows = con.execute(
        "SELECT ts_ms,open,high,low,close,volume FROM candles "
        "WHERE exchange='binance' AND symbol='ETHUSDT' AND timeframe=? "
        "ORDER BY ts_ms DESC LIMIT 8000",
        (tf,),
    ).fetchall()
    out[tf] = [list(r) for r in rows]
    mx = con.execute(
        "SELECT MAX(ts_ms), COUNT(*) FROM candles WHERE exchange='binance' "
        "AND symbol='ETHUSDT' AND timeframe=?",
        (tf,),
    ).fetchone()
    out[tf + '_meta'] = {'max_ts': mx[0], 'n': mx[1]}
print(json.dumps(out))
"""


def main() -> int:
    helper = Path(tempfile.gettempdir()) / "_pull_eth_shared.py"
    helper.write_text(REMOTE, encoding="utf-8", newline="\n")
    subprocess.check_call(
        ["scp", "-o", "BatchMode=yes", str(helper), f"root@{HOST}:/tmp/_pull_eth_shared.py"]
    )
    raw = subprocess.check_output(
        [
            "ssh",
            "-o",
            "BatchMode=yes",
            f"root@{HOST}",
            "sed -i 's/\\r$//' /tmp/_pull_eth_shared.py; python3 /tmp/_pull_eth_shared.py",
        ],
        text=True,
        encoding="utf-8",
    )
    lines = [ln for ln in raw.splitlines() if ln.strip().startswith("{")]
    data = json.loads(lines[-1])
    now = int(time.time() * 1000)
    con = sqlite3.connect(str(MARKET_DB), timeout=120)
    con.execute("PRAGMA journal_mode=WAL")
    n_up = 0
    for tf in TFS:
        rows = data.get(tf) or []
        for ts, o, h, l, c, v in rows:
            # PK is (source,symbol,timeframe,ts_ms) — overwrite tip rows as last.
            con.execute(
                "INSERT INTO market_ohlcv("
                "source,symbol,timeframe,ts_ms,open,high,low,close,volume,"
                "price_type,is_complete,downloaded_at,product,source_endpoint"
                ") VALUES(?,?,?,?,?,?,?,?,?,?,1,?,?,?) "
                "ON CONFLICT(source,symbol,timeframe,ts_ms) DO UPDATE SET "
                "open=excluded.open, high=excluded.high, low=excluded.low, "
                "close=excluded.close, volume=excluded.volume, "
                "price_type='last', is_complete=1, downloaded_at=excluded.downloaded_at",
                (
                    "binance",
                    SYMBOL,
                    tf,
                    int(ts),
                    float(o),
                    float(h),
                    float(l),
                    float(c),
                    float(v or 0),
                    "last",
                    now,
                    "spot",
                    "vps_shared_candles",
                ),
            )
            n_up += 1
        print(tf, "meta", data.get(tf + "_meta"), "upserted", len(rows))
    con.commit()
    # show densest tip
    for tf in ("15m", "1h"):
        print(
            tf,
            con.execute(
                "SELECT price_type, MAX(ts_ms), COUNT(*) FROM market_ohlcv "
                "WHERE symbol=? AND timeframe=? AND source='binance' GROUP BY price_type",
                (SYMBOL, tf),
            ).fetchall(),
        )
    con.close()
    print("total_upserts", n_up)

    from llm2.data.loader import load_ohlcv

    df = load_ohlcv(SYMBOL, "15m")
    print("loader tip now", df.index.max(), "n", len(df), "price_type", df.attrs.get("price_type"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
