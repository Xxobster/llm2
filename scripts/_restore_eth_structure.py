"""Restore ETHUSDT structure series after a short-window upsert wiped history.

Recomputes 1h/4h from full market_ohlcv warehouse + Binance REST tip, then upserts.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_ind = Path(r"C:\projects\botsgeneral\packages\indicators\src")
if _ind.is_dir() and str(_ind) not in sys.path:
    sys.path.insert(0, str(_ind))

from indicators.compute import compute_structure  # noqa: E402
from indicators.store import IndicatorDB  # noqa: E402

from llm2.data.indicators import indicators_db_path, load_bar_features  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.live.refresh_structure import fetch_ohlcv_binance_rest  # noqa: E402


def _merge_warehouse_and_rest(symbol: str, timeframe: str, *, rest_limit: int) -> pd.DataFrame:
    wh = load_ohlcv(symbol, timeframe, source="binance")
    if wh.index.tz is None:
        wh.index = wh.index.tz_localize("UTC")
    rest = fetch_ohlcv_binance_rest(symbol, timeframe, limit=rest_limit)
    if rest.empty:
        out = wh.copy()
    else:
        if "ts_ms" not in rest.columns:
            rest = rest.copy()
            rest["ts_ms"] = (rest.index.asi8 // 1_000_000).astype("int64")
        # Align columns
        cols = ["open", "high", "low", "close", "volume", "ts_ms"]
        for c in cols:
            if c not in wh.columns and c == "ts_ms":
                wh = wh.copy()
                wh["ts_ms"] = (wh.index.asi8 // 1_000_000).astype("int64")
        a = wh[cols].copy()
        b = rest[cols].copy()
        out = pd.concat([a, b]).sort_index()
        out = out[~out.index.duplicated(keep="last")]
    # Drop forming bar
    from llm2.paths import TF_MS
    from datetime import datetime, timezone

    step = int(TF_MS[timeframe])
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    last_open = int(out["ts_ms"].iloc[-1])
    if last_open + step > now_ms:
        out = out.iloc[:-1]
    return out


def restore(symbol: str = "ETHUSDT", timeframes: tuple[str, ...] = ("1h", "4h")) -> dict:
    db_path = indicators_db_path()
    ind = IndicatorDB(db_path)
    report: dict = {"symbol": symbol, "db": str(db_path), "series": []}
    try:
        for tf in timeframes:
            # 1h needs ~60k bars; REST tip 3000 is enough to extend warehouse
            df = _merge_warehouse_and_rest(symbol, tf, rest_limit=3000 if tf != "1w" else 500)
            print(f"{symbol} {tf}: bars={len(df)} {df.index.min()} -> {df.index.max()}")
            bundle = compute_structure(
                df.reset_index(drop=True),
                source="binance",
                symbol=symbol.upper(),
                timeframe=tf,
            )
            counts = ind.upsert_bundle(bundle)
            report["series"].append(
                {
                    "timeframe": tf,
                    "n_bars": int(len(df)),
                    "first": str(df.index.min()),
                    "last": str(df.index.max()),
                    "counts": counts,
                }
            )
    finally:
        ind.close()
    # clear caches
    load_bar_features.cache_clear()
    return report


if __name__ == "__main__":
    rep = restore()
    print(json.dumps(rep, indent=2))
