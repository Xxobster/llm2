"""Vectorized causal OHLCV features (v1)."""

from __future__ import annotations

import numpy as np
import pandas as pd


def build_ohlcv_v1(ohlcv: pd.DataFrame) -> pd.DataFrame:
    """Past-only features: returns, vol, ATR%, volume ratios, momentum, range position, cyclical time."""
    df = ohlcv.sort_index()
    c = df["close"].astype(float)
    h = df["high"].astype(float)
    l = df["low"].astype(float)
    o = df["open"].astype(float)
    v = df["volume"].astype(float) if "volume" in df.columns else pd.Series(0.0, index=df.index)

    out = pd.DataFrame(index=df.index)
    log_c = np.log(c.replace(0, np.nan))
    out["logret_1"] = log_c.diff()
    for w in (3, 6, 12, 24, 48):
        out[f"logret_{w}"] = log_c.diff(w)
        out[f"vol_{w}"] = out["logret_1"].rolling(w, min_periods=max(2, w // 2)).std()
        out[f"mom_{w}"] = c.pct_change(w)
        out[f"vol_ratio_{w}"] = v / v.rolling(w, min_periods=1).mean().replace(0, np.nan)

    prev = c.shift(1)
    tr = pd.concat([(h - l), (h - prev).abs(), (l - prev).abs()], axis=1).max(axis=1)
    for w in (14, 48):
        out[f"atrpct_{w}"] = tr.rolling(w, min_periods=1).mean() / c.replace(0, np.nan)

    rng = (h - l).replace(0, np.nan)
    out["range_pct"] = rng / c.replace(0, np.nan)
    out["body_pct"] = (c - o) / c.replace(0, np.nan)
    out["close_loc"] = (c - l) / rng

    for w in (24, 48, 96):
        roll_min = l.rolling(w, min_periods=1).min()
        roll_max = h.rolling(w, min_periods=1).max()
        span = (roll_max - roll_min).replace(0, np.nan)
        out[f"range_pos_{w}"] = (c - roll_min) / span

    idx = pd.DatetimeIndex(df.index)
    if idx.tz is None:
        idx = idx.tz_localize("UTC")
    else:
        idx = idx.tz_convert("UTC")
    hour = idx.hour + idx.minute / 60.0
    dow = idx.dayofweek.astype(float)
    out["hour_sin"] = np.sin(2 * np.pi * hour / 24.0)
    out["hour_cos"] = np.cos(2 * np.pi * hour / 24.0)
    out["dow_sin"] = np.sin(2 * np.pi * dow / 7.0)
    out["dow_cos"] = np.cos(2 * np.pi * dow / 7.0)

    return out.replace([np.inf, -np.inf], np.nan)
