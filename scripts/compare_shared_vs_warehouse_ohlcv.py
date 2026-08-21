"""Compare shared_candles vs research market_ohlcv for exact OHLCV identity.

Proves (or falsifies) whether live signal candles match backtest candles.

Examples (PowerShell-friendly — no heredocs required):

  # 1) On VPS: export closed-bar Binance series
  python scripts/compare_shared_vs_warehouse_ohlcv.py export-shared \\
    --shared /var/lib/botsgeneral/shared_candles.db \\
    --symbol ETHUSDT --timeframe 1h \\
    --out /tmp/shared_ETHUSDT_1h.parquet

  # 2) Locally: compare export to research warehouse
  python scripts/compare_shared_vs_warehouse_ohlcv.py compare \\
    --shared-export /tmp/shared_ETHUSDT_1h.parquet \\
    --warehouse D:/projectsdata/candles/market_ohlcv.sqlite \\
    --symbol ETHUSDT --timeframe 1h

  # Or one-shot if both DBs are local:
  python scripts/compare_shared_vs_warehouse_ohlcv.py compare \\
    --shared C:/path/shared_candles.db \\
    --warehouse D:/projectsdata/candles/market_ohlcv.sqlite \\
    --symbol ETHUSDT --timeframe 1h
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from llm2.paths import MARKET_DB, TF_MS


def _drop_forming(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    if df.empty:
        return df
    step = int(TF_MS[timeframe])
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    last_open = int(df["ts_ms"].iloc[-1])
    if last_open + step > now_ms:
        return df.iloc[:-1].copy()
    return df


def _resolve_warehouse_price_type(
    con: sqlite3.Connection, *, symbol: str, timeframe: str, source: str
) -> str:
    rows = con.execute(
        "SELECT price_type, COUNT(*) AS n FROM market_ohlcv "
        "WHERE symbol=? AND timeframe=? AND source=? "
        "AND (is_complete=1 OR is_complete IS NULL) "
        "GROUP BY price_type ORDER BY n DESC",
        (symbol, timeframe, source),
    ).fetchall()
    if not rows:
        raise ValueError(f"no warehouse rows for {symbol} {timeframe} {source}")
    available = {str(r[0]): int(r[1]) for r in rows}
    for pref in ("last_price", "last"):
        if available.get(pref, 0) > 0:
            # densest synonym among last/last_price
            syn = [(p, available[p]) for p in ("last_price", "last") if available.get(p, 0) > 0]
            return max(syn, key=lambda x: x[1])[0]
    return str(rows[0][0])


def load_shared(
    path: Path, *, symbol: str, timeframe: str, exchange: str = "binance"
) -> pd.DataFrame:
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    rows = con.execute(
        "SELECT ts_ms, open, high, low, close, volume FROM candles "
        "WHERE exchange=? AND symbol=? AND timeframe=? "
        "ORDER BY ts_ms ASC",
        (exchange, symbol.upper(), timeframe),
    ).fetchall()
    con.close()
    if not rows:
        raise ValueError(f"no shared rows for {exchange} {symbol} {timeframe}")
    df = pd.DataFrame(
        rows, columns=["ts_ms", "open", "high", "low", "close", "volume"]
    )
    return _drop_forming(df, timeframe)


def load_warehouse(
    path: Path, *, symbol: str, timeframe: str, source: str = "binance"
) -> tuple[pd.DataFrame, str]:
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    pt = _resolve_warehouse_price_type(
        con, symbol=symbol.upper(), timeframe=timeframe, source=source
    )
    rows = con.execute(
        "SELECT ts_ms, open, high, low, close, volume FROM market_ohlcv "
        "WHERE symbol=? AND timeframe=? AND source=? AND price_type=? "
        "AND (is_complete=1 OR is_complete IS NULL) "
        "ORDER BY ts_ms ASC",
        (symbol.upper(), timeframe, source, pt),
    ).fetchall()
    con.close()
    if not rows:
        raise ValueError(f"no warehouse rows for {symbol} {timeframe} {source}/{pt}")
    df = pd.DataFrame(
        rows, columns=["ts_ms", "open", "high", "low", "close", "volume"]
    )
    return _drop_forming(df, timeframe), pt


def load_shared_export(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".parquet":
        df = pd.read_parquet(path)
    else:
        df = pd.read_csv(path)
    need = ["ts_ms", "open", "high", "low", "close", "volume"]
    missing = [c for c in need if c not in df.columns]
    if missing:
        raise ValueError(f"export missing columns {missing}")
    return df[need].sort_values("ts_ms").reset_index(drop=True)


def series_hash(df: pd.DataFrame) -> str:
    arr = df[["ts_ms", "open", "high", "low", "close", "volume"]].to_numpy()
    # float64 bytes — exact identity check
    return hashlib.sha256(arr.astype(np.float64).tobytes()).hexdigest()


def _mismatch_row(
    ts: int,
    so: pd.DataFrame,
    wo: pd.DataFrame,
    abs_diff: pd.DataFrame,
    cols: list[str],
) -> dict[str, Any]:
    return {
        "ts_ms": ts,
        "utc": datetime.fromtimestamp(ts / 1000, tz=timezone.utc).isoformat(),
        "shared": so.loc[ts, cols].astype(float).to_dict(),
        "warehouse": wo.loc[ts, cols].astype(float).to_dict(),
        "abs_diff": abs_diff.loc[ts].astype(float).to_dict(),
    }


def compare_frames(
    shared: pd.DataFrame,
    warehouse: pd.DataFrame,
    *,
    price_eps: float = 1e-8,
    volume_eps: float = 1e-4,
    tip_bars: int = 500,
) -> dict[str, Any]:
    """Compare closed-bar OHLCV. Price and volume use separate tolerances.

    Exact byte identity still reported via SHA-256 of float64 payload on overlap.
    """
    s = shared.set_index("ts_ms")
    w = warehouse.set_index("ts_ms")
    overlap = s.index.intersection(w.index).sort_values()
    only_s = s.index.difference(w.index)
    only_w = w.index.difference(s.index)
    so = s.loc[overlap]
    wo = w.loc[overlap]
    ohlc = ["open", "high", "low", "close"]
    cols = ohlc + ["volume"]
    abs_diff = (so[cols] - wo[cols]).abs()
    price_mis = (abs_diff[ohlc] > price_eps).any(axis=1)
    vol_mis = abs_diff["volume"] > volume_eps
    any_mis = price_mis | vol_mis
    n_price = int(price_mis.sum())
    n_vol_only = int((~price_mis & vol_mis).sum())
    n_mismatch = int(any_mis.sum())

    def _first(mask: pd.Series) -> dict[str, Any] | None:
        if not bool(mask.any()):
            return None
        return _mismatch_row(int(overlap[mask][0]), so, wo, abs_diff, cols)

    tip = overlap[-tip_bars:] if len(overlap) else overlap
    tip_price_mis = int(price_mis.loc[tip].sum()) if len(tip) else 0
    tip_any_mis = int(any_mis.loc[tip].sum()) if len(tip) else 0

    identical = (
        n_mismatch == 0
        and len(only_s) == 0
        and len(only_w) == 0
        and len(overlap) > 0
    )
    # Signal-relevant gate: OHLC identical on overlap (volume float noise ignored via volume_eps)
    overlap_ohlc_identical = n_price == 0 and len(overlap) > 0
    return {
        "n_shared": int(len(s)),
        "n_warehouse": int(len(w)),
        "n_overlap": int(len(overlap)),
        "n_only_shared": int(len(only_s)),
        "n_only_warehouse": int(len(only_w)),
        "n_mismatch_bars": n_mismatch,
        "n_price_mismatch_bars": n_price,
        "n_volume_only_mismatch_bars": n_vol_only,
        "max_abs_diff": {
            c: float(abs_diff[c].max()) if len(overlap) else None for c in cols
        },
        "overlap_hash_shared": series_hash(so.reset_index()) if len(overlap) else None,
        "overlap_hash_warehouse": series_hash(wo.reset_index()) if len(overlap) else None,
        "hashes_equal": (
            series_hash(so.reset_index()) == series_hash(wo.reset_index())
            if len(overlap)
            else False
        ),
        "first_mismatch": _first(any_mis),
        "first_price_mismatch": _first(price_mis),
        "tip_bars": int(tip_bars),
        "tip_n_price_mismatch": tip_price_mis,
        "tip_n_any_mismatch": tip_any_mis,
        "tip_ohlc_identical": tip_price_mis == 0 and len(tip) > 0,
        "overlap_first_ts_ms": int(overlap[0]) if len(overlap) else None,
        "overlap_last_ts_ms": int(overlap[-1]) if len(overlap) else None,
        "exact_same_series": identical,
        "overlap_values_identical": overlap_ohlc_identical and n_vol_only == 0,
        "overlap_ohlc_identical": overlap_ohlc_identical,
        "price_eps": price_eps,
        "volume_eps": volume_eps,
        # backward-compat key used by older reports
        "abs_eps": price_eps,
    }


def cmd_export_shared(args: argparse.Namespace) -> int:
    df = load_shared(
        Path(args.shared),
        symbol=args.symbol,
        timeframe=args.timeframe,
        exchange=args.exchange,
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() == ".parquet":
        df.to_parquet(out, index=False)
    else:
        df.to_csv(out, index=False)
    meta = {
        "n_bars": len(df),
        "first_ts_ms": int(df["ts_ms"].iloc[0]),
        "last_ts_ms": int(df["ts_ms"].iloc[-1]),
        "sha256": series_hash(df),
        "out": str(out),
    }
    print(json.dumps(meta, indent=2))
    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    if args.shared_export:
        shared = load_shared_export(Path(args.shared_export))
        # export already dropped forming at export time; drop again for safety
        shared = _drop_forming(shared, args.timeframe)
    elif args.shared:
        shared = load_shared(
            Path(args.shared),
            symbol=args.symbol,
            timeframe=args.timeframe,
            exchange=args.exchange,
        )
    else:
        raise SystemExit("need --shared or --shared-export")

    warehouse, price_type = load_warehouse(
        Path(args.warehouse),
        symbol=args.symbol,
        timeframe=args.timeframe,
        source=args.source,
    )
    rep = compare_frames(
        shared,
        warehouse,
        price_eps=float(args.price_eps),
        volume_eps=float(args.volume_eps),
        tip_bars=int(args.tip_bars),
    )
    out = {
        "evidence_class": "OHLCV_SHARED_VS_WAREHOUSE",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "principal_blocker": (
            None
            if rep["overlap_ohlc_identical"] and rep["tip_ohlc_identical"]
            else "SHARED_CANDLES_NE_RESEARCH_MARKET_OHLCV"
        ),
        "symbol": args.symbol.upper(),
        "timeframe": args.timeframe,
        "shared_exchange": args.exchange,
        "warehouse_source": args.source,
        "warehouse_price_type": price_type,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        **rep,
        "howto_keep_identical": [
            "Both sides must use Binance USD-M futures Last (fapi), not spot.",
            "Exclude forming bar on both sides before compare.",
            "Pin warehouse price_type to densest of last_price/last — never mix.",
            "Refresh warehouse: python -m botsgeneral research-candles --only binance "
            f"--symbols {args.symbol.upper()} --timeframes {args.timeframe} --price-type last",
            "Refresh shared: ensure botsgeneral collector healthy (sitrep) / force backfill if gaps.",
            "Re-run this compare; require overlap_ohlc_identical=true and tip_ohlc_identical=true.",
            "For byte-exact hashes_equal=true, also reconcile volume float storage / re-ingest.",
            "Gold path (strongest): one store — sync market_ohlcv or indicators.sqlite to VPS "
            "and make live read that file (no dual independent collectors).",
        ],
    }
    if args.out:
        Path(args.out).write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))
    # Pass gate for ops: OHLC identity on full overlap + tip (volume float may still differ)
    ok = bool(out["overlap_ohlc_identical"] and out["tip_ohlc_identical"])
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    ex = sub.add_parser("export-shared", help="Export closed shared bars")
    ex.add_argument("--shared", required=True)
    ex.add_argument("--symbol", default="ETHUSDT")
    ex.add_argument("--timeframe", default="1h")
    ex.add_argument("--exchange", default="binance")
    ex.add_argument("--out", required=True)
    ex.set_defaults(func=cmd_export_shared)

    cp = sub.add_parser("compare", help="Compare shared vs warehouse")
    cp.add_argument("--shared", default=None, help="Path to shared_candles.db")
    cp.add_argument("--shared-export", default=None, help="Parquet/CSV from export-shared")
    cp.add_argument("--warehouse", default=str(MARKET_DB))
    cp.add_argument("--symbol", default="ETHUSDT")
    cp.add_argument("--timeframe", default="1h")
    cp.add_argument("--exchange", default="binance")
    cp.add_argument("--source", default="binance")
    cp.add_argument("--price-eps", type=float, default=1e-8)
    cp.add_argument("--volume-eps", type=float, default=1e-4)
    cp.add_argument("--tip-bars", type=int, default=500)
    cp.add_argument("--out", default=None)
    cp.set_defaults(func=cmd_compare)

    args = ap.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
