"""Causal multi-timeframe resample helpers for pivot research.

Never manufacture 5-minute candles from 15m or 1h bars.
Preferred path: 1m → higher timeframes via left-closed, right-open aggregation,
matching bar open ``ts_ms`` warehouse convention.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.paths import TF_MS

_FORBIDDEN_UPSAMPLE = {
    ("15m", "5m"),
    ("15m", "1m"),
    ("30m", "5m"),
    ("30m", "1m"),
    ("1h", "5m"),
    ("1h", "15m"),
    ("1h", "1m"),
    ("4h", "1h"),
    ("4h", "15m"),
    ("4h", "5m"),
    ("1d", "4h"),
    ("1d", "1h"),
}


def refuse_illegal_resample(source_tf: str, target_tf: str) -> None:
    key = (str(source_tf), str(target_tf))
    if key in _FORBIDDEN_UPSAMPLE:
        raise ValueError(
            f"Illegal manufacture of {target_tf} from {source_tf}. "
            "Use genuine 1m (preferred) or native target timeframe."
        )
    src_ms = TF_MS.get(source_tf)
    dst_ms = TF_MS.get(target_tf)
    if src_ms is None or dst_ms is None:
        raise ValueError(f"unknown timeframe pair {source_tf}->{target_tf}")
    if dst_ms < src_ms:
        raise ValueError(
            f"Cannot upsample {source_tf} ({src_ms}ms) to {target_tf} ({dst_ms}ms)"
        )
    if dst_ms % src_ms != 0:
        raise ValueError(f"{target_tf} is not an integer multiple of {source_tf}")


def resample_ohlcv_from_base(
    ohlcv: pd.DataFrame,
    *,
    source_tf: str,
    target_tf: str,
) -> pd.DataFrame:
    """Aggregate complete base bars into target TF. Vectorized resample."""
    refuse_illegal_resample(source_tf, target_tf)
    if target_tf == source_tf:
        return ohlcv.copy()
    df = ohlcv.copy()
    if "ts_ms" not in df.columns:
        idx = pd.DatetimeIndex(pd.to_datetime(df.index, utc=True))
        df = df.copy()
        df["ts_ms"] = (idx.asi8 // 1_000_000).astype(np.int64)
    src_ms = int(TF_MS[source_tf])
    dst_ms = int(TF_MS[target_tf])
    # Truncate incomplete bucket at tip
    bucket = (df["ts_ms"].to_numpy(dtype=np.int64) // dst_ms) * dst_ms
    g = df.assign(_bucket=bucket).groupby("_bucket", sort=True)
    out = g.agg(
        open=("open", "first"),
        high=("high", "max"),
        low=("low", "min"),
        close=("close", "last"),
        volume=("volume", "sum") if "volume" in df.columns else ("open", "count"),
        n_base=("ts_ms", "count"),
    )
    # Keep only complete buckets
    need = dst_ms // src_ms
    out = out.loc[out["n_base"] >= need].copy()
    out["ts_ms"] = out.index.astype(np.int64)
    out["timestamp"] = pd.to_datetime(out["ts_ms"], unit="ms", utc=True)
    out = out.set_index("timestamp")
    return out[["open", "high", "low", "close", "volume", "ts_ms", "n_base"]]
