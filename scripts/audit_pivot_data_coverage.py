"""Data-coverage audit for pivot forecasting (research warehouse).

Additive: read-only against D:/projectsdata; writes report under artifacts/reports.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from llm2.paths import ARTIFACTS, MARKET_DB, MARKET_OI_DB, PROJECTSDATA

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TIMEFRAMES = ("1m", "5m", "15m", "30m", "1h", "4h", "1d")
SOURCES = ("binance", "bybit")
PRICE_TYPES_LAST = ("last", "last_price", "mark", "mark_price", "index", "index_price")


def _query_coverage(db: Path) -> list[dict]:
    if not db.is_file():
        return [{"error": f"missing {db}"}]
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=120.0)
    try:
        tables = [
            r[0]
            for r in con.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY 1"
            ).fetchall()
        ]
        # Prefer known market_ohlcv shape
        if "market_ohlcv" not in tables:
            return [{"tables": tables, "db": str(db)}]
        sql = """
        SELECT source, symbol, timeframe, price_type,
               COUNT(*) AS n_bars,
               MIN(ts_ms) AS min_ts_ms,
               MAX(ts_ms) AS max_ts_ms,
               SUM(CASE WHEN is_complete = 0 THEN 1 ELSE 0 END) AS n_incomplete
        FROM market_ohlcv
        WHERE symbol IN ('BTCUSDT','ETHUSDT','SOLUSDT')
          AND timeframe IN ('1m','5m','15m','30m','1h','4h','1d')
        GROUP BY source, symbol, timeframe, price_type
        ORDER BY source, symbol, timeframe, n_bars DESC
        """
        df = pd.read_sql(sql, con)
    finally:
        con.close()
    rows = []
    for r in df.itertuples(index=False):
        rows.append(
            {
                "source": r.source,
                "symbol": r.symbol,
                "timeframe": r.timeframe,
                "price_type": r.price_type,
                "n_bars": int(r.n_bars),
                "min_utc": datetime.fromtimestamp(r.min_ts_ms / 1000, tz=timezone.utc).isoformat(),
                "max_utc": datetime.fromtimestamp(r.max_ts_ms / 1000, tz=timezone.utc).isoformat(),
                "n_incomplete": int(r.n_incomplete or 0),
            }
        )
    return rows


def _oi_coverage() -> list[dict]:
    db = MARKET_OI_DB
    if not db.is_file():
        return [{"error": f"missing {db}"}]
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=120.0)
    try:
        tables = [
            r[0]
            for r in con.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY 1"
            ).fetchall()
        ]
        if not tables:
            return [{"tables": []}]
        # discover table with symbol+ts
        out = [{"tables": tables}]
        for t in tables[:5]:
            cols = [
                c[1]
                for c in con.execute(f"PRAGMA table_info({t})").fetchall()
            ]
            if "symbol" in cols and any(x in cols for x in ("ts_ms", "timestamp", "ts")):
                ts_col = "ts_ms" if "ts_ms" in cols else ("timestamp" if "timestamp" in cols else "ts")
                try:
                    df = pd.read_sql(
                        f"""
                        SELECT symbol, COUNT(*) n, MIN({ts_col}) mn, MAX({ts_col}) mx
                        FROM {t}
                        WHERE symbol IN ('BTCUSDT','ETHUSDT','SOLUSDT')
                        GROUP BY symbol
                        """,
                        con,
                    )
                    out.append({"table": t, "cols": cols, "rows": df.to_dict(orient="records")})
                except Exception as exc:  # noqa: BLE001
                    out.append({"table": t, "error": str(exc)[:200]})
        return out
    finally:
        con.close()


def _dir_snapshot(path: Path, max_entries: int = 40) -> list[dict]:
    if not path.is_dir():
        return [{"error": f"missing {path}"}]
    items = []
    for p in sorted(path.iterdir())[:max_entries]:
        items.append(
            {
                "name": p.name,
                "is_dir": p.is_dir(),
                "size": None if p.is_dir() else int(p.stat().st_size),
            }
        )
    return items


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    ohlcv = _query_coverage(MARKET_DB)
    # Pivot matrix: best last-price series coverage
    matrix = {}
    for row in ohlcv:
        if "error" in row:
            continue
        key = (row["source"], row["symbol"], row["timeframe"])
        if row["price_type"] not in ("last", "last_price", "mark", "mark_price"):
            continue
        prev = matrix.get(key)
        if prev is None or row["n_bars"] > prev["n_bars"]:
            matrix[key] = row

    # Flag gaps for pivot program targets
    required_tf = ("1m", "5m", "15m", "1h", "4h", "1d")
    gaps = []
    for src in SOURCES:
        for sym in SYMBOLS:
            for tf in required_tf:
                r = matrix.get((src, sym, tf))
                if r is None:
                    gaps.append(
                        {
                            "source": src,
                            "symbol": sym,
                            "timeframe": tf,
                            "status": "MISSING",
                        }
                    )
                else:
                    # Sufficient bars heuristic: >> 500
                    status = "OK" if r["n_bars"] >= 500 else "SPARSE"
                    gaps.append({**r, "status": status})

    report = {
        "stamp": stamp,
        "market_db": str(MARKET_DB),
        "market_db_size_gb": round(MARKET_DB.stat().st_size / 1e9, 3)
        if MARKET_DB.is_file()
        else None,
        "ohlcv_rows": ohlcv,
        "best_last_or_mark_matrix": list(matrix.values()),
        "coverage_status": gaps,
        "oi": _oi_coverage(),
        "projectsdata_layout": {
            "trades": _dir_snapshot(PROJECTSDATA / "trades"),
            "tradeshistory": _dir_snapshot(PROJECTSDATA / "tradeshistory"),
            "orderbook": _dir_snapshot(PROJECTSDATA / "orderbook"),
            "cryptodb": _dir_snapshot(PROJECTSDATA / "cryptodb"),
        },
        "notes": [
            "Loader defaults source=binance last-trade. Bybit may exist or be sparse.",
            "Never manufacture 5m from 15m/1h — require genuine 1m or 5m.",
            "crypto_alpha/research not present in this mono-repo (llm2 is the package).",
        ],
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"data_coverage_{stamp}.json"
    latest = out_dir / "data_coverage_latest.json"
    text = json.dumps(report, indent=2, default=str)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    # Human matrix print
    print(f"DB {MARKET_DB} size_gb={report['market_db_size_gb']}")
    print(f"{'src':8} {'sym':8} {'tf':4} {'status':8} {'n':>10} {'min':22} {'max':22} type")
    for g in sorted(gaps, key=lambda x: (x.get("source", ""), x.get("symbol", ""), x.get("timeframe", ""))):
        print(
            f"{g.get('source','?'):8} {g.get('symbol','?'):8} {g.get('timeframe','?'):4} "
            f"{g.get('status','?'):8} {g.get('n_bars',0):10} "
            f"{str(g.get('min_utc',''))[:19]:22} {str(g.get('max_utc',''))[:19]:22} "
            f"{g.get('price_type','')}"
        )
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
