"""Hunt 015 causal ideas: bar-shape, session VWAP, prior-day, trail (not a 012–014 retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import close_location_value, kaufman_efficiency_ratio, wilder_atr
from llm2.ml_lab.causal_math import bar_return, sign_nz, zscore
from llm2.paths import TF_MS
from llm2.validation.folds import index_to_ms

STREAK_N = 6
WICK_Z = 1.50
RELVOL_K = 2.50
VOL_WIN = 48
TRAIL_K = 2.0
VWAP_ATR = 0.60
ER_CHOP = 0.35
CLV_TH = 0.80
NR_LEN = 7
DAY_MS = 86_400_000

IDEA_IDS_L: tuple[str, ...] = (
    "close_streak_fade",
    "wick_exhaust_fade",
    "relvol_spike_fade",
    "atr_trail_flip",
    "utc_vwap_pullback",
    "prior_day_fade",
    "clv_extreme_fade",
    "nr7_break",
)


def _utc_day_id(ohlcv: pd.DataFrame) -> np.ndarray:
    return index_to_ms(ohlcv.index).astype(np.int64) // DAY_MS


def close_streak_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade after STREAK_N consecutive same-sign closes."""
    del timeframe
    r = bar_return(ohlcv["close"].to_numpy(dtype=float))
    s = sign_nz(r)
    chg = np.ones(s.size, dtype=bool)
    chg[1:] = s[1:] != s[:-1]
    run = pd.Series(np.ones(s.size, dtype=np.int64)).groupby(np.cumsum(chg)).cumsum().to_numpy()
    run = np.where(s != 0, run, 0)
    out = np.zeros(s.size, dtype=np.float64)
    fire = run >= STREAK_N
    out[fire] = -s[fire]
    return out


def wick_exhaust_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade the wick side when that wick is large versus the bar range."""
    del timeframe
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    rng = h - l
    with np.errstate(divide="ignore", invalid="ignore"):
        upper = (h - np.maximum(o, c)) / np.where(rng > 0, rng, np.nan)
        lower = (np.minimum(o, c) - l) / np.where(rng > 0, rng, np.nan)
    zu = zscore(upper)
    zl = zscore(lower)
    out = np.zeros(c.size, dtype=np.float64)
    out[np.isfinite(zu) & (zu >= WICK_Z)] = -1.0
    out[np.isfinite(zl) & (zl >= WICK_Z)] = 1.0
    return out


def relvol_spike_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade the bar return when volume is a spike versus its rolling median."""
    del timeframe
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    med = pd.Series(v).rolling(VOL_WIN, min_periods=VOL_WIN).median().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        rel = v / np.where(med > 0, med, np.nan)
    r = bar_return(c)
    out = np.zeros(c.size, dtype=np.float64)
    fire = np.isfinite(rel) & (rel >= RELVOL_K)
    out[fire] = -sign_nz(r)[fire]
    return out


def atr_trail_flip(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow when close is outside a prior-bar Average True Range envelope around close."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    prev_c = np.roll(c, 1)
    prev_a = np.roll(atr, 1)
    prev_c[0] = np.nan
    prev_a[0] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    up = np.isfinite(prev_c) & np.isfinite(prev_a) & (c > prev_c + TRAIL_K * prev_a)
    dn = np.isfinite(prev_c) & np.isfinite(prev_a) & (c < prev_c - TRAIL_K * prev_a)
    out[up] = 1.0
    out[dn] = -1.0
    return out


def utc_vwap_pullback(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Pull toward the UTC-day volume-weighted typical price when the market is choppy."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    er = kaufman_efficiency_ratio(c, 10)
    tp = (h + l + c) / 3.0
    day = _utc_day_id(ohlcv)
    pv = pd.Series(tp * v).groupby(day).cumsum().to_numpy(dtype=float)
    cv = pd.Series(v).groupby(day).cumsum().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        vwap = pv / np.where(cv > 0, cv, np.nan)
        dist = (c - vwap) / np.where(atr > 0, atr, np.nan)
    out = np.zeros(c.size, dtype=np.float64)
    chop = np.isfinite(er) & (er <= ER_CHOP)
    far = np.isfinite(dist) & (np.abs(dist) >= VWAP_ATR)
    out[chop & far] = -sign_nz(dist)[chop & far]
    return out


def prior_day_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a touch of the previous UTC day's high or low."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    n = h.size
    day = _utc_day_id(ohlcv)
    g = pd.DataFrame({"d": day, "h": h, "l": l})
    daily = g.groupby("d", sort=True).agg(hh=("h", "max"), ll=("l", "min"))
    prev_h = daily["hh"].shift(1)
    prev_l = daily["ll"].shift(1)
    ph = prev_h.reindex(day).to_numpy(dtype=float)
    pl = prev_l.reindex(day).to_numpy(dtype=float)
    out = np.zeros(n, dtype=np.float64)
    out[np.isfinite(ph) & (h >= ph)] = -1.0
    out[np.isfinite(pl) & (l <= pl)] = 1.0
    both = np.isfinite(ph) & np.isfinite(pl) & (h >= ph) & (l <= pl)
    out[both] = 0.0
    return out


def clv_extreme_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade when close sits at the extreme of the bar (Close Location Value)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    clv = close_location_value(h, l, c)
    out = np.zeros(c.size, dtype=np.float64)
    out[np.isfinite(clv) & (clv >= CLV_TH)] = -1.0
    out[np.isfinite(clv) & (clv <= -CLV_TH)] = 1.0
    return out


def nr7_break(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow the close after a 7-bar narrow-range compression expands."""
    del timeframe
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    rng = h - l
    nr = rng <= pd.Series(rng).rolling(NR_LEN, min_periods=NR_LEN).min().to_numpy(dtype=float)
    was_nr = np.roll(nr, 1)
    was_nr[0] = False
    out = np.zeros(c.size, dtype=np.float64)
    expand = was_nr & (~nr)
    out[expand] = sign_nz(c - o)[expand]
    return out


def signals_l(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "close_streak_fade": close_streak_fade(ohlcv, timeframe),
        "wick_exhaust_fade": wick_exhaust_fade(ohlcv, timeframe),
        "relvol_spike_fade": relvol_spike_fade(ohlcv, timeframe),
        "atr_trail_flip": atr_trail_flip(ohlcv, timeframe),
        "utc_vwap_pullback": utc_vwap_pullback(ohlcv, timeframe),
        "prior_day_fade": prior_day_fade(ohlcv, timeframe),
        "clv_extreme_fade": clv_extreme_fade(ohlcv, timeframe),
        "nr7_break": nr7_break(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state for leakage (not the sparse ±1 fires)."""
    del kwargs
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv["volume"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    rng = h - l
    with np.errstate(divide="ignore", invalid="ignore"):
        upper = (h - np.maximum(o, c)) / np.where(rng > 0, rng, np.nan)
        relvol = v / pd.Series(v).rolling(VOL_WIN, min_periods=VOL_WIN).median().to_numpy(dtype=float)
        atr_frac = atr / np.where(c > 0, c, np.nan)
    return pd.DataFrame(
        {
            "bar_return": bar_return(c),
            "atr_frac": atr_frac,
            "upper_wick_frac": upper,
            "relvol": relvol,
            "clv": close_location_value(h, l, c),
            "er_10": kaufman_efficiency_ratio(c, 10),
        },
        index=ohlcv.index,
    )
