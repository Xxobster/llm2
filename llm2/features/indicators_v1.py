"""Portable technical indicators pack (v1), causal only."""

from __future__ import annotations

import numpy as np
import pandas as pd

if not hasattr(np, "NaN"):
    np.NaN = np.nan  # type: ignore[attr-defined]

if not hasattr(pd.Series, "append"):

    def _series_append(self, to_append, ignore_index=False, verify_integrity=False, sort=False):
        return pd.concat(
            [self, to_append],
            ignore_index=ignore_index,
            verify_integrity=verify_integrity,
            sort=sort,
        )

    pd.Series.append = _series_append  # type: ignore[attr-defined]

import pandas_ta as ta


def build_indicators_v1(ohlcv: pd.DataFrame) -> pd.DataFrame:
    """RSI, ATR, MACD, Bollinger, EMAs — under ~80 columns."""
    df = ohlcv.sort_index()
    h, l, c, v = df["high"], df["low"], df["close"], df["volume"]
    out = pd.DataFrame(index=df.index)

    for length in (7, 14, 21):
        rsi = ta.rsi(c, length=length)
        if rsi is not None:
            out[f"rsi_{length}"] = rsi

    atr = ta.atr(high=h, low=l, close=c, length=14)
    if atr is not None:
        out["atr_14"] = atr
        out["atrpct_14"] = atr / c.replace(0, np.nan)

    macd = ta.macd(c, fast=12, slow=26, signal=9)
    if macd is not None and not macd.empty:
        for col in macd.columns:
            out[f"macd_{col.lower()}"] = macd[col]

    for length in (20, 50):
        bb = ta.bbands(c, length=length, std=2.0)
        if bb is not None and not bb.empty:
            for col in bb.columns:
                safe = col.replace("%", "pct").replace(" ", "_").lower()
                out[f"bb{length}_{safe}"] = bb[col]
            mid_col = [x for x in bb.columns if "BBM" in x.upper()]
            if mid_col:
                out[f"bb{length}_width"] = (bb[bb.columns[0]] - bb[bb.columns[2]]) / bb[mid_col[0]].replace(0, np.nan)

    for span in (9, 21, 55, 100):
        ema = ta.ema(c, length=span)
        if ema is not None:
            out[f"ema_{span}"] = ema
            out[f"ema_dist_{span}"] = (c - ema) / c.replace(0, np.nan)

    dpo = ta.dpo(c, length=20, centered=False)
    if dpo is not None:
        out["dpo_20"] = dpo

    adx = ta.adx(high=h, low=l, close=c, length=14)
    if adx is not None and not adx.empty:
        for col in adx.columns:
            out[f"adx_{col.lower()}"] = adx[col]

    obv = ta.obv(c, v)
    if obv is not None:
        out["obv"] = obv
        out["obv_z_48"] = (obv - obv.rolling(48, min_periods=1).mean()) / obv.rolling(48, min_periods=1).std()

    # Cap column count for speed
    if out.shape[1] > 80:
        out = out.iloc[:, :80]

    return out.replace([np.inf, -np.inf], np.nan)
