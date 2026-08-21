"""Fast coverage probe: per-key aggregates using primary key lookup patterns."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from llm2.paths import ARTIFACTS, MARKET_DB, MARKET_OI_DB, PROJECTSDATA

SYMBOLS = ("BTCUSDT", "ETHUSDT", "SOLUSDT")
TFS = ("1m", "5m", "15m", "30m", "1h", "4h", "1d")
SOURCES = ("binance", "bybit")


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    con = sqlite3.connect(f"file:{MARKET_DB}?mode=ro", uri=True, timeout=120.0)
    con.execute("PRAGMA busy_timeout=120000")
    schema = list(con.execute("PRAGMA table_info(market_ohlcv)"))
    indexes = list(
        con.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name='market_ohlcv'"
        )
    )
    # Distinct price types present for our keys via constrained samples
    rows = []
    for source in SOURCES:
        for symbol in SYMBOLS:
            for tf in TFS:
                q = """
                SELECT price_type, COUNT(*) AS n, MIN(ts_ms), MAX(ts_ms)
                FROM market_ohlcv
                WHERE source=? AND symbol=? AND timeframe=?
                  AND (is_complete=1 OR is_complete IS NULL)
                GROUP BY price_type
                """
                t0 = datetime.now(timezone.utc)
                got = con.execute(q, (source, symbol, tf)).fetchall()
                elapsed = (datetime.now(timezone.utc) - t0).total_seconds()
                if not got:
                    rows.append(
                        {
                            "source": source,
                            "symbol": symbol,
                            "timeframe": tf,
                            "status": "MISSING",
                            "elapsed_s": elapsed,
                        }
                    )
                    continue
                # pick densest last-ish series
                best = max(got, key=lambda r: r[1])
                for pt, n, mn, mx in got:
                    status = "OK" if n >= 500 else "SPARSE"
                    kind = "last" if "last" in str(pt) else ("mark" if "mark" in str(pt) else "other")
                    rows.append(
                        {
                            "source": source,
                            "symbol": symbol,
                            "timeframe": tf,
                            "price_type": pt,
                            "n_bars": int(n),
                            "min_utc": datetime.fromtimestamp(mn / 1000, tz=timezone.utc).isoformat(),
                            "max_utc": datetime.fromtimestamp(mx / 1000, tz=timezone.utc).isoformat(),
                            "status": status,
                            "series_kind": kind,
                            "elapsed_s": elapsed,
                            "is_best_for_key": (pt == best[0] and n == best[1]),
                        }
                    )
                print(
                    f"{source:8} {symbol:8} {tf:4} types={len(got)} best_n={best[1]} {elapsed:.1f}s",
                    flush=True,
                )
    con.close()

    # projectsdata presence
    def list_dir(p: Path, n: int = 25) -> list[dict]:
        if not p.is_dir():
            return [{"error": str(p)}]
        out = []
        for child in sorted(p.iterdir())[:n]:
            out.append(
                {
                    "name": child.name,
                    "is_dir": child.is_dir(),
                    "size": None if child.is_dir() else child.stat().st_size,
                }
            )
        return out

    # Minimal OI
    oi = {}
    if MARKET_OI_DB.is_file():
        oic = sqlite3.connect(f"file:{MARKET_OI_DB}?mode=ro", uri=True, timeout=60)
        oi["tables"] = [
            r[0]
            for r in oic.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        ]
        oic.close()

    # Matrix of last-series OK/MISSING for primary decision path
    matrix = []
    for source in SOURCES:
        for symbol in SYMBOLS:
            for tf in TFS:
                cands = [
                    r
                    for r in rows
                    if r.get("source") == source
                    and r.get("symbol") == symbol
                    and r.get("timeframe") == tf
                    and r.get("status") != "MISSING"
                    and r.get("series_kind") == "last"
                ]
                if not cands:
                    cands = [
                        r
                        for r in rows
                        if r.get("source") == source
                        and r.get("symbol") == symbol
                        and r.get("timeframe") == tf
                        and r.get("status") != "MISSING"
                    ]
                if not cands:
                    matrix.append(
                        {
                            "source": source,
                            "symbol": symbol,
                            "timeframe": tf,
                            "status": "MISSING",
                        }
                    )
                else:
                    best = max(cands, key=lambda r: r.get("n_bars", 0))
                    matrix.append(
                        {
                            "source": source,
                            "symbol": symbol,
                            "timeframe": tf,
                            "status": best["status"],
                            "price_type": best.get("price_type"),
                            "n_bars": best.get("n_bars"),
                            "min_utc": best.get("min_utc"),
                            "max_utc": best.get("max_utc"),
                        }
                    )

    # Critical for 5m forecasts
    needs_1m_or_5m = []
    for source in SOURCES:
        for symbol in SYMBOLS:
            m1 = next(
                (
                    m
                    for m in matrix
                    if m["source"] == source
                    and m["symbol"] == symbol
                    and m["timeframe"] == "1m"
                    and m["status"] == "OK"
                ),
                None,
            )
            m5 = next(
                (
                    m
                    for m in matrix
                    if m["source"] == source
                    and m["symbol"] == symbol
                    and m["timeframe"] == "5m"
                    and m["status"] == "OK"
                ),
                None,
            )
            needs_1m_or_5m.append(
                {
                    "source": source,
                    "symbol": symbol,
                    "has_1m_ok": m1 is not None,
                    "has_5m_ok": m5 is not None,
                    "can_forecast_5m": (m1 is not None) or (m5 is not None),
                    "note": "Must NOT manufacture 5m from 15m/1h",
                }
            )

    report = {
        "stamp": stamp,
        "market_db": str(MARKET_DB),
        "size_gb": round(MARKET_DB.stat().st_size / 1e9, 3),
        "schema_columns": [c[1] for c in schema],
        "indexes": [{"name": i[0], "sql": i[1]} for i in indexes],
        "detailed_rows": rows,
        "matrix_best_last": matrix,
        "five_minute_readiness": needs_1m_or_5m,
        "oi_db": str(MARKET_OI_DB),
        "oi": oi,
        "layout": {
            "trades": list_dir(PROJECTSDATA / "trades"),
            "tradeshistory": list_dir(PROJECTSDATA / "tradeshistory"),
            "orderbook": list_dir(PROJECTSDATA / "orderbook"),
            "cryptodb": list_dir(PROJECTSDATA / "cryptodb"),
        },
        "repo_notes": {
            "package": "llm2 (no crypto_alpha/ package present)",
            "signal_default": "binance last via load_ohlcv",
            "structure": "botsgeneral indicators: pivot_ts_ms vs confirm_ts_ms (CAUS-STRUCT-001 lesson)",
            "lockbox": "FORWARD_LOCKBOX_START=2026-05-01",
            "readiness_default": "LIVE_STOP / RESEARCH_ONLY — no live orders from pivot module",
        },
    }
    out_dir = ARTIFACTS / "reports" / "pivot_forecast"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"data_coverage_{stamp}.json"
    latest = out_dir / "data_coverage_latest.json"
    text = json.dumps(report, indent=2)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print("\n=== MATRIX (last series) ===")
    for m in matrix:
        print(
            f"{m['source']:8} {m['symbol']:8} {m['timeframe']:4} {m['status']:8} "
            f"n={m.get('n_bars','-')} {str(m.get('min_utc',''))[:10]}..{str(m.get('max_utc',''))[:10]} "
            f"{m.get('price_type','')}"
        )
    print("\n=== 5m readiness ===")
    for r in needs_1m_or_5m:
        print(r)
    print(f"WROTE {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
