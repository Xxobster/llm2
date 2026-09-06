"""Hunt 011 causal ideas: second formula pack (not a 009 retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import wilder_atr
from llm2.ml_lab.causal_math import (
    WIN,
    Z_FIRE,
    amihud_illiquidity,
    bar_return,
    ewm_resid,
    hurst_rs,
    log_price,
    realized_quarticity,
    rolling_skew,
    sign_nz,
    zscore,
)

HURST_TREND = 0.58
HURST_MR = 0.42
ATR_Q = 0.25
CUSUM_Z = 1.80

IDEA_IDS_H: tuple[str, ...] = (
    "hurst_rs_switch",
    "quarticity_spike_fade",
    "amihud_illiquid_fade",
    "ewm_level_resid_fade",
    "rolling_skew_fade",
    "cusum_drift_follow",
    "volsync_follow",
    "atr_compress_break",
)


def _state(ohlcv: pd.DataFrame) -> dict[str, np.ndarray]:
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    r = bar_return(c)
    lp = log_price(c)
    atr = wilder_atr(h, l, c, 14)
    quart = realized_quarticity(r)
    ami = amihud_illiquidity(r, v)
    resid = ewm_resid(lp)
    sk = rolling_skew(r)
    return {
        "close": c,
        "high": h,
        "low": l,
        "ret": r,
        "vol": v,
        "atr": atr,
        "hurst": hurst_rs(r),
        "quart": quart,
        "quart_z": zscore(quart),
        "amihud": ami,
        "amihud_z": zscore(ami),
        "ewm_resid": resid,
        "ewm_z": zscore(resid),
        "skew": sk,
        "skew_z": zscore(sk),
    }


def hurst_rs_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """High Hurst: follow 8-bar drift. Low Hurst: fade versus a 20-bar mean."""
    del timeframe
    st = st or _state(ohlcv)
    c = st["close"]
    hst = st["hurst"]
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    mid = pd.Series(c).rolling(20, min_periods=20).mean().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    trend = np.isfinite(hst) & (hst >= HURST_TREND)
    revert = np.isfinite(hst) & (hst <= HURST_MR)
    out[trend] = sign_nz(r8)[trend]
    out[revert] = -sign_nz(c - mid)[revert]
    return out


def quarticity_spike_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade a 3-bar move after a realized-quarticity spike."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["quart_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = np.isfinite(z) & (z >= Z_FIRE)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def amihud_illiquid_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade when Amihud illiquidity is extreme (thin-book overreaction)."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["amihud_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = np.isfinite(z) & (z >= Z_FIRE)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def ewm_level_resid_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade log-price versus a causal exponential local level (Kalman proxy)."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["ewm_z"]
    out = np.zeros(z.size, dtype=np.float64)
    out[z >= Z_FIRE] = -1.0
    out[z <= -Z_FIRE] = 1.0
    return out


def rolling_skew_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade when rolling return skew is extreme."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["skew_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = np.isfinite(z) & (np.abs(z) >= Z_FIRE)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def cusum_drift_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow when a rolling cumulative sum of demeaned returns is extreme."""
    del timeframe
    st = st or _state(ohlcv)
    r = pd.Series(st["ret"])
    mu = r.rolling(WIN, min_periods=WIN).mean()
    cus = (r - mu).rolling(WIN, min_periods=WIN).sum()
    z = zscore(cus.to_numpy(dtype=float))
    out = np.zeros(z.size, dtype=np.float64)
    out[z >= CUSUM_Z] = 1.0
    out[z <= -CUSUM_Z] = -1.0
    return out


def volsync_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow when signed volume and return agree at a high z-score."""
    del timeframe
    st = st or _state(ohlcv)
    r = st["ret"]
    vz = zscore(st["vol"])
    signed = r * np.sign(vz)
    z = zscore(signed)
    out = np.zeros(z.size, dtype=np.float64)
    fire = np.isfinite(z) & (np.abs(z) >= Z_FIRE) & np.isfinite(vz) & (np.abs(vz) >= 0.50)
    out[fire] = sign_nz(r)[fire]
    return out


def atr_compress_break(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow a close through the prior 20-bar high/low after Average True Range compresses."""
    del timeframe
    st = st or _state(ohlcv)
    c = st["close"]
    h = st["high"]
    l = st["low"]
    atr = st["atr"]
    q = pd.Series(atr).rolling(WIN, min_periods=WIN).quantile(ATR_Q).to_numpy(dtype=float)
    hh = pd.Series(h).rolling(20, min_periods=20).max().shift(1).to_numpy(dtype=float)
    ll = pd.Series(l).rolling(20, min_periods=20).min().shift(1).to_numpy(dtype=float)
    quiet = np.isfinite(atr) & np.isfinite(q) & (atr <= q)
    out = np.zeros(c.size, dtype=np.float64)
    out[quiet & np.isfinite(hh) & (c > hh)] = 1.0
    out[quiet & np.isfinite(ll) & (c < ll)] = -1.0
    return out


def signals_h(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    st = _state(ohlcv)
    return {
        "hurst_rs_switch": hurst_rs_switch(ohlcv, timeframe, st=st),
        "quarticity_spike_fade": quarticity_spike_fade(ohlcv, timeframe, st=st),
        "amihud_illiquid_fade": amihud_illiquid_fade(ohlcv, timeframe, st=st),
        "ewm_level_resid_fade": ewm_level_resid_fade(ohlcv, timeframe, st=st),
        "rolling_skew_fade": rolling_skew_fade(ohlcv, timeframe, st=st),
        "cusum_drift_follow": cusum_drift_follow(ohlcv, timeframe, st=st),
        "volsync_follow": volsync_follow(ohlcv, timeframe, st=st),
        "atr_compress_break": atr_compress_break(ohlcv, timeframe, st=st),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    del kwargs
    st = _state(ohlcv)
    return pd.DataFrame(
        {
            "bar_return": st["ret"],
            "hurst": st["hurst"],
            "quart": st["quart"],
            "amihud": st["amihud"],
            "ewm_resid": st["ewm_resid"],
            "skew": st["skew"],
            "atr": st["atr"],
            "volume": st["vol"],
        },
        index=ohlcv.index,
    )
