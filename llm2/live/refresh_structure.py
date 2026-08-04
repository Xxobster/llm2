"""Refresh structure features into the live pack indicators slice from Bybit REST.

Does not depend on the VPS shared_candles.db (collector may only serve other bots'
discovered pairs). Uses botsgeneral ``indicators.compute_structure`` when available.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

BYBIT_REST = "https://api.bybit.com"
TF_MAP = {"1h": "60", "4h": "240", "1w": "W", "1d": "D"}


def fetch_ohlcv(symbol: str, timeframe: str, *, limit: int = 1000) -> pd.DataFrame:
    iv = TF_MAP.get(timeframe, timeframe)
    # paginate newest-first pages
    frames: list[pd.DataFrame] = []
    end: int | None = None
    remaining = int(limit)
    while remaining > 0:
        batch = min(1000, remaining)
        params: dict[str, str] = {
            "category": "linear",
            "symbol": symbol.upper(),
            "interval": iv,
            "limit": str(batch),
        }
        if end is not None:
            params["end"] = str(end)
        q = urllib.parse.urlencode(params)
        req = urllib.request.Request(
            f"{BYBIT_REST}/v5/market/kline?{q}",
            headers={"User-Agent": "llm2-structure-refresh/1.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        if int(data.get("retCode", -1)) != 0:
            raise RuntimeError(data.get("retMsg"))
        rows = list(reversed(data.get("result", {}).get("list") or []))
        if not rows:
            break
        idx = pd.to_datetime([int(r[0]) for r in rows], unit="ms", utc=True)
        df = pd.DataFrame(
            {
                "ts_ms": [int(r[0]) for r in rows],
                "open": [float(r[1]) for r in rows],
                "high": [float(r[2]) for r in rows],
                "low": [float(r[3]) for r in rows],
                "close": [float(r[4]) for r in rows],
                "volume": [float(r[5]) for r in rows],
                "source": "bybit",
            },
            index=idx,
        )
        frames.append(df)
        remaining -= len(rows)
        end = int(rows[0][0]) - 1
        if len(rows) < batch:
            break
    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames).sort_index()
    return out[~out.index.duplicated(keep="last")]


def _drop_forming_bar(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    """Keep only fully closed candles (Bybit kline timestamp = bar open)."""
    if df.empty:
        return df
    from llm2.paths import TF_MS

    step = int(TF_MS[timeframe])
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    last_open = int(df["ts_ms"].iloc[-1])
    if last_open + step > now_ms:
        return df.iloc[:-1]
    return df


def refresh_symbol(
    *,
    symbol: str,
    timeframes: tuple[str, ...] = ("1h", "4h", "1w"),
    indicator_db: Path,
    limit: int = 1500,
) -> dict:
    # Prefer botsgeneral indicators package
    ind_src = Path("/opt/botsgeneral/packages/indicators/src")
    if ind_src.is_dir() and str(ind_src) not in sys.path:
        sys.path.insert(0, str(ind_src))
    win_src = Path(r"C:\projects\botsgeneral\packages\indicators\src")
    if win_src.is_dir() and str(win_src) not in sys.path:
        sys.path.insert(0, str(win_src))

    from indicators.compute import compute_structure
    from indicators.store import IndicatorDB

    ind = IndicatorDB(indicator_db)
    report: dict = {"symbol": symbol, "db": str(indicator_db), "series": []}
    try:
        for tf in timeframes:
            df = _drop_forming_bar(fetch_ohlcv(symbol, tf, limit=limit), tf)
            if df.empty or len(df) < 50:
                report["series"].append({"timeframe": tf, "error": "insufficient bars"})
                continue
            bundle = compute_structure(
                df.reset_index(drop=True),
                source="bybit",
                symbol=symbol.upper(),
                timeframe=tf,
            )
            counts = ind.upsert_bundle(bundle)
            last = int(df["ts_ms"].iloc[-1])
            report["series"].append(
                {
                    "timeframe": tf,
                    "n_bars": int(len(df)),
                    "last_ts_ms": last,
                    "last_utc": datetime.fromtimestamp(last / 1000, tz=timezone.utc).isoformat(),
                    "counts": counts,
                }
            )
    finally:
        ind.close()
    report["refreshed_utc"] = datetime.now(timezone.utc).isoformat()
    return report


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--timeframes", default="1h,4h,1w")
    args = ap.parse_args(argv)
    tfs = tuple(x.strip() for x in args.timeframes.split(",") if x.strip())
    rep = refresh_symbol(symbol=args.symbol, timeframes=tfs, indicator_db=args.db)
    print(json.dumps(rep, indent=2))
    bad = [s for s in rep["series"] if s.get("error")]
    return 1 if bad and len(bad) == len(rep["series"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
