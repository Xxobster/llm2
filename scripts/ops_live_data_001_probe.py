"""Ops probe for LIVE-DATA-001 tip freshness (server time vs local tip).

Examples:
  python scripts/ops_live_data_001_probe.py --symbol ETHUSDT --timeframe 15m
  python scripts/ops_live_data_001_probe.py --symbol BTCUSDT --timeframe 15m --persist
  python scripts/ops_live_data_001_probe.py --demo-cases
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

_LC = Path(r"C:\projects\botsgeneral\packages\live_candles\src")
if _LC.is_dir() and str(_LC) not in sys.path:
    sys.path.insert(0, str(_LC))


def _demo() -> int:
    from live_candles.freshness import evaluate_tip_freshness, expected_closed_open_ms

    server = 1_704_067_620_000
    expected = expected_closed_open_ms("15m", server_now_ms=server)
    cases = [
        ("PASS", expected, server),
        ("CANDLE_STALE", expected - 900_000, server),
        ("CANDLE_AHEAD", expected + 900_000, server),
        ("CLOCK_SKEW", expected, server + 60_000),
        ("CANDLE_MISSING", None, server),
    ]
    rows = []
    for name, tip, wall in cases:
        r = evaluate_tip_freshness(
            exchange="binance",
            symbol="ETHUSDT",
            timeframe="15m",
            local_tip_ms=tip,
            server_now_ms=server,
            local_wall_ms=wall,
            clock_skew_max_ms=5_000,
            fetch_server_time=False,
        )
        rows.append({"case": name, "got": r.code, "ok": r.ok})
        assert r.code == name, rows[-1]
    print(json.dumps({"demo": "PASS", "rows": rows}, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--symbol", default="ETHUSDT")
    ap.add_argument("--timeframe", default="15m")
    ap.add_argument("--exchange", default="binance")
    ap.add_argument("--db", default=None, help="shared_candles.db path")
    ap.add_argument(
        "--persist",
        action="store_true",
        help="Write/clear DATA_UNSAFE meta from this probe",
    )
    ap.add_argument(
        "--demo-cases",
        action="store_true",
        help="Offline unit-style tip-behind/ahead/skew cases (no network)",
    )
    args = ap.parse_args(argv)
    if args.demo_cases:
        return _demo()

    from live_candles.freshness import (
        LIVE_DATA_001,
        check_series_live_data_001,
        read_data_unsafe,
    )
    from live_candles.reader import newest_ts_ms as tip_read

    tip = tip_read(args.exchange, args.symbol, args.timeframe, db_path=args.db)
    result = check_series_live_data_001(
        exchange=args.exchange,
        symbol=args.symbol,
        timeframe=args.timeframe,
        local_tip_ms=tip,
        db_path=args.db,
        persist_flag=bool(args.persist),
    )
    flagged = read_data_unsafe(
        exchange=args.exchange,
        symbol=args.symbol,
        timeframe=args.timeframe,
        db_path=args.db,
    )
    coll = read_data_unsafe(
        exchange=args.exchange, symbol="COLLECTOR", timeframe="1m", db_path=args.db
    )
    out = {
        "conformance": LIVE_DATA_001,
        "tip_result": result.to_dict(),
        "data_unsafe_series": flagged,
        "data_unsafe_collector": coll,
        "allow_new_entries": bool(result.ok) and coll is None,
        "policy": "fail_closed_new_entries_keep_protective_exits",
    }
    print(json.dumps(out, indent=2, default=str))
    return 0 if result.ok and coll is None else 2


if __name__ == "__main__":
    raise SystemExit(main())
