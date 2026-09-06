"""Hunt 017 causal ideas: channels and volume oscillators (not a 016 RSI retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import (
    aroon,
    bollinger,
    chaikin_ad_osc,
    keltner_channel,
    money_flow_index,
    parabolic_sar,
    percent_b,
    vortex_indicator,
    williams_r,
)
from llm2.ml_lab.causal_math import bar_return, sign_nz

WR_HI = -20.0
WR_LO = -80.0
MFI_HI = 80.0
MFI_LO = 20.0
PCTB_HI = 1.0
PCTB_LO = 0.0

IDEA_IDS_N: tuple[str, ...] = (
    "williams_r_fade",
    "keltner_break_follow",
    "bollinger_pctb_fade",
    "aroon_cross_follow",
    "psar_flip_follow",
    "mfi_extreme_fade",
    "vortex_cross_follow",
    "chaikin_osc_flip",
)


def williams_r_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Larry Williams percent-R at −20 / −80."""
    del timeframe
    wr = williams_r(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        ohlcv["close"].to_numpy(dtype=float),
        period=14,
    )
    out = np.zeros(wr.size, dtype=np.float64)
    out[np.isfinite(wr) & (wr >= WR_HI)] = -1.0
    out[np.isfinite(wr) & (wr <= WR_LO)] = 1.0
    return out


def keltner_break_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow the first close outside the Keltner channel (not every bar while outside)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    lo, _mid, hi = keltner_channel(h, l, c, period=20, atr_mult=2.0)
    outside_up = np.isfinite(hi) & (c > hi)
    outside_dn = np.isfinite(lo) & (c < lo)
    prev_up = np.roll(outside_up, 1)
    prev_dn = np.roll(outside_dn, 1)
    prev_up[0] = False
    prev_dn[0] = False
    out = np.zeros(c.size, dtype=np.float64)
    out[outside_up & ~prev_up] = 1.0
    out[outside_dn & ~prev_dn] = -1.0
    return out


def bollinger_pctb_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a close outside the 20-bar, 2-sigma Bollinger bands (percent-B)."""
    del timeframe
    c = ohlcv["close"].to_numpy(dtype=float)
    lo, _mid, hi, _w = bollinger(c, period=20, n_std=2.0)
    pb = percent_b(c, lo, hi)
    out = np.zeros(c.size, dtype=np.float64)
    out[np.isfinite(pb) & (pb >= PCTB_HI)] = -1.0
    out[np.isfinite(pb) & (pb <= PCTB_LO)] = 1.0
    return out


def aroon_cross_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a new sign of Aroon-up minus Aroon-down (25-bar)."""
    del timeframe
    up, dn = aroon(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        period=25,
    )
    osc = up - dn
    prev = np.roll(osc, 1)
    prev[0] = np.nan
    out = np.zeros(osc.size, dtype=np.float64)
    flip = np.isfinite(osc) & np.isfinite(prev) & (np.sign(osc) != np.sign(prev)) & (osc != 0)
    out[flip] = sign_nz(osc)[flip]
    return out


def psar_flip_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow Wilder Parabolic Stop and Reverse when its direction flips."""
    del timeframe
    _sar, direction = parabolic_sar(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        step=0.02,
        max_af=0.2,
    )
    prev = np.roll(direction, 1)
    prev[0] = np.nan
    out = np.zeros(direction.size, dtype=np.float64)
    flip = np.isfinite(direction) & np.isfinite(prev) & (direction != prev)
    out[flip] = direction[flip]
    return out


def mfi_extreme_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Money Flow Index at 80 / 20 (volume-weighted, not Relative Strength Index)."""
    del timeframe
    mfi = money_flow_index(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        ohlcv["close"].to_numpy(dtype=float),
        ohlcv["volume"].to_numpy(dtype=float),
        period=14,
    )
    out = np.zeros(mfi.size, dtype=np.float64)
    out[np.isfinite(mfi) & (mfi >= MFI_HI)] = -1.0
    out[np.isfinite(mfi) & (mfi <= MFI_LO)] = 1.0
    return out


def vortex_cross_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a new sign of +VI minus −VI (Botes / Siepman vortex)."""
    del timeframe
    plus_vi, minus_vi = vortex_indicator(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        ohlcv["close"].to_numpy(dtype=float),
        period=14,
    )
    osc = plus_vi - minus_vi
    prev = np.roll(osc, 1)
    prev[0] = np.nan
    out = np.zeros(osc.size, dtype=np.float64)
    flip = np.isfinite(osc) & np.isfinite(prev) & (np.sign(osc) != np.sign(prev)) & (osc != 0)
    out[flip] = sign_nz(osc)[flip]
    return out


def chaikin_osc_flip(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a sign flip of the Chaikin Accumulation/Distribution oscillator."""
    del timeframe
    osc = chaikin_ad_osc(
        ohlcv["high"].to_numpy(dtype=float),
        ohlcv["low"].to_numpy(dtype=float),
        ohlcv["close"].to_numpy(dtype=float),
        ohlcv["volume"].to_numpy(dtype=float),
    )
    prev = np.roll(osc, 1)
    prev[0] = np.nan
    out = np.zeros(osc.size, dtype=np.float64)
    flip = np.isfinite(osc) & np.isfinite(prev) & (np.sign(osc) != np.sign(prev)) & (osc != 0)
    out[flip] = sign_nz(osc)[flip]
    return out


def signals_n(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "williams_r_fade": williams_r_fade(ohlcv, timeframe),
        "keltner_break_follow": keltner_break_follow(ohlcv, timeframe),
        "bollinger_pctb_fade": bollinger_pctb_fade(ohlcv, timeframe),
        "aroon_cross_follow": aroon_cross_follow(ohlcv, timeframe),
        "psar_flip_follow": psar_flip_follow(ohlcv, timeframe),
        "mfi_extreme_fade": mfi_extreme_fade(ohlcv, timeframe),
        "vortex_cross_follow": vortex_cross_follow(ohlcv, timeframe),
        "chaikin_osc_flip": chaikin_osc_flip(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state for leakage (not the sparse ±1 fires)."""
    del kwargs
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    lo, _mid, hi, _w = bollinger(c, period=20, n_std=2.0)
    plus_vi, minus_vi = vortex_indicator(h, l, c, period=14)
    return pd.DataFrame(
        {
            "bar_return": bar_return(c),
            "williams_r": williams_r(h, l, c, period=14),
            "percent_b": percent_b(c, lo, hi),
            "mfi": money_flow_index(h, l, c, v, period=14),
            "vortex_osc": plus_vi - minus_vi,
            "chaikin_osc": chaikin_ad_osc(h, l, c, v),
        },
        index=ohlcv.index,
    )
