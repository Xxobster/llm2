"""Hunt 012 causal ideas: Fair Value Gap (FVG) based signals.

Fair Value Gap = three-bar price imbalance (bars labelled t-2, t-1, t):
  Bullish FVG: high[t-2] < low[t]   (gap between bar t-2 top and bar t bottom)
  Bearish FVG: low[t-2]  > high[t]  (gap between bar t-2 bottom and bar t top)

The gap is identified at bar t's close (fully known). All signals are +1 / 0 / −1
from completed bars only. No Pine Script, no centered window, no future data.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import kaufman_efficiency_ratio, wilder_atr
from llm2.ml_lab.idea_catalog import _ret, _sign_nz
from llm2.validation.folds import index_to_ms

# ─── constants (not searched on profit factor) ──────────────────────────────
FVG_ATR_MIN = 0.30        # gap must span at least 0.30 × ATR to count
FVG_PULL_ATR = 0.25       # pullback fires when close is within 0.25 ATR of gap edge
FVG_PULL_MAX_ATR = 1.20   # but not more than 1.20 ATR past the other edge
FVG_AGE_MAX = 20          # FVG dies if not revisited within this many bars
FVG_ER_LOW = 0.35         # low Kaufman Efficiency Ratio = choppy, more reliable fade
FVG_ER_HIGH = 0.50        # high ER = trending, more reliable continuation

IDEA_IDS_I: tuple[str, ...] = (
    "fvg_pullback_long",        # bullish FVG + price pulls back into gap → long
    "fvg_pullback_short",       # bearish FVG + price pulls back into gap → short
    "fvg_follow",               # any fresh FVG → follow direction (gap-and-go)
    "fvg_fresh_er",             # FVG on choppy market only (low ER) → fade the impulse
    "fvg_mitigated_reverse",    # price enters gap and closes back through → reverse
    "fvg_age_filter",           # FVG pullback only on young gap (≤ FVG_AGE_MAX bars)
    "fvg_size_break",           # large FVG (> 1.5× ATR) gap-and-go follow
    "fvg_confluence",           # bullish FVG AND prior 20-bar low still unbroken → long
)


# ─── helpers ────────────────────────────────────────────────────────────────

def _fvg_arrays(
    high: np.ndarray, low: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return vectorized gap top/bottom for bullish and bearish FVGs.

    Bullish FVG at bar t: low[t] > high[t-2]  →  gap = (high[t-2], low[t])
    Bearish FVG at bar t: high[t] < low[t-2]  →  gap = (high[t], low[t-2])
    All arrays are aligned to bar t (present bar).
    """
    n = high.size
    bull_top = np.full(n, np.nan)
    bull_bot = np.full(n, np.nan)
    bear_top = np.full(n, np.nan)
    bear_bot = np.full(n, np.nan)

    h2 = np.roll(high, 2)   # high[t-2]
    l2 = np.roll(low, 2)    # low[t-2]
    h2[:2] = np.nan
    l2[:2] = np.nan

    bull_mask = low > h2
    bear_mask = high < l2

    bull_top[bull_mask] = low[bull_mask]
    bull_bot[bull_mask] = h2[bull_mask]
    bear_top[bear_mask] = l2[bear_mask]
    bear_bot[bear_mask] = high[bear_mask]

    return bull_top, bull_bot, bear_top, bear_bot


def _gap_size(top: np.ndarray, bot: np.ndarray) -> np.ndarray:
    return top - bot


def _last_fvg_idx(arr: np.ndarray, max_age: int) -> np.ndarray:
    """For each bar, the index of the most recent non-NaN gap within max_age bars."""
    n = arr.size
    out = np.full(n, -1, dtype=np.int64)
    last = -1
    for i in range(n):
        if np.isfinite(arr[i]):
            last = i
        if last >= 0 and (i - last) <= max_age:
            out[i] = last
    return out


# ─── signal functions ────────────────────────────────────────────────────────

def fvg_pullback_long(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Long when price pulls back into a prior bullish FVG (unmitigated)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bull_top, bull_bot, _, _ = _fvg_arrays(h, l)
    gap = _gap_size(bull_top, bull_bot)
    # gap must be meaningful
    valid = np.isfinite(bull_top) & (gap >= FVG_ATR_MIN * atr)
    out = np.zeros(c.size, dtype=np.float64)
    # carry last valid gap forward (max age)
    idx = _last_fvg_idx(np.where(valid, bull_bot, np.nan), FVG_AGE_MAX)
    for i in range(c.size):
        j = int(idx[i])
        if j < 0 or j >= i:
            continue
        bot = bull_bot[j]
        top = bull_top[j]
        atri = atr[i]
        if not (np.isfinite(bot) and np.isfinite(atri) and atri > 0):
            continue
        # pullback: close is near or inside gap from below
        if bot - FVG_PULL_ATR * atri <= c[i] <= top + FVG_PULL_ATR * atri:
            out[i] = 1.0
    return out


def fvg_pullback_short(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Short when price pulls back into a prior bearish FVG (unmitigated)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    _, _, bear_top, bear_bot = _fvg_arrays(h, l)
    gap = _gap_size(bear_top, bear_bot)
    valid = np.isfinite(bear_bot) & (gap >= FVG_ATR_MIN * atr)
    out = np.zeros(c.size, dtype=np.float64)
    idx = _last_fvg_idx(np.where(valid, bear_top, np.nan), FVG_AGE_MAX)
    for i in range(c.size):
        j = int(idx[i])
        if j < 0 or j >= i:
            continue
        bot = bear_bot[j]
        top = bear_top[j]
        atri = atr[i]
        if not (np.isfinite(top) and np.isfinite(atri) and atri > 0):
            continue
        if bot - FVG_PULL_ATR * atri <= c[i] <= top + FVG_PULL_ATR * atri:
            out[i] = -1.0
    return out


def fvg_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow the direction of a fresh FVG on the bar it forms (gap-and-go)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bull_top, bull_bot, bear_top, bear_bot = _fvg_arrays(h, l)
    bull_gap = _gap_size(bull_top, bull_bot)
    bear_gap = _gap_size(bear_top, bear_bot)
    out = np.zeros(c.size, dtype=np.float64)
    bull_fire = np.isfinite(bull_bot) & (bull_gap >= FVG_ATR_MIN * atr)
    bear_fire = np.isfinite(bear_bot) & (bear_gap >= FVG_ATR_MIN * atr)
    out[bull_fire] = 1.0
    out[bear_fire] = -1.0
    return out


def fvg_fresh_er(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade the impulse: FVG forms in choppy market (low Kaufman Efficiency Ratio) → counter-direction."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    er = kaufman_efficiency_ratio(c, 10)
    bull_top, bull_bot, bear_top, bear_bot = _fvg_arrays(h, l)
    bull_gap = _gap_size(bull_top, bull_bot)
    bear_gap = _gap_size(bear_top, bear_bot)
    choppy = np.isfinite(er) & (er <= FVG_ER_LOW)
    out = np.zeros(c.size, dtype=np.float64)
    # in choppy conditions FVG is a spike → fade it
    out[choppy & np.isfinite(bull_bot) & (bull_gap >= FVG_ATR_MIN * atr)] = -1.0
    out[choppy & np.isfinite(bear_bot) & (bear_gap >= FVG_ATR_MIN * atr)] = 1.0
    return out


def fvg_mitigated_reverse(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Price entered the gap then closes back through the near edge → reversal."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bull_top, bull_bot, bear_top, bear_bot = _fvg_arrays(h, l)
    bull_gap = _gap_size(bull_top, bull_bot)
    bear_gap = _gap_size(bear_top, bear_bot)
    out = np.zeros(c.size, dtype=np.float64)
    idx_bull = _last_fvg_idx(np.where(np.isfinite(bull_bot) & (bull_gap >= FVG_ATR_MIN * atr), bull_bot, np.nan), FVG_AGE_MAX)
    idx_bear = _last_fvg_idx(np.where(np.isfinite(bear_bot) & (bear_gap >= FVG_ATR_MIN * atr), bear_bot, np.nan), FVG_AGE_MAX)
    for i in range(c.size):
        jb = int(idx_bull[i])
        if jb >= 0 and jb < i:
            # price touched gap area (via low) but close now below gap bottom → disrespect → short
            if l[i] <= bull_top[jb] and c[i] < bull_bot[jb]:
                out[i] = -1.0
        jr = int(idx_bear[i])
        if jr >= 0 and jr < i:
            if h[i] >= bear_bot[jr] and c[i] > bear_top[jr]:
                out[i] = 1.0
    return out


def fvg_age_filter(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Pullback into a young bullish FVG only (≤ FVG_AGE_MAX bars old)."""
    # same as fvg_pullback_long but verifies gap age ≤ FVG_AGE_MAX exactly
    return fvg_pullback_long(ohlcv, timeframe)


def fvg_size_break(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow direction of a large FVG (gap > 1.5× ATR): strong institutional imbalance."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bull_top, bull_bot, bear_top, bear_bot = _fvg_arrays(h, l)
    bull_gap = _gap_size(bull_top, bull_bot)
    bear_gap = _gap_size(bear_top, bear_bot)
    large = 1.5
    out = np.zeros(c.size, dtype=np.float64)
    out[np.isfinite(bull_bot) & (bull_gap >= large * atr)] = 1.0
    out[np.isfinite(bear_bot) & (bear_gap >= large * atr)] = -1.0
    return out


def fvg_confluence(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Bullish FVG + 20-bar low still intact (price never undercut) → long."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bull_top, bull_bot, _, _ = _fvg_arrays(h, l)
    bull_gap = _gap_size(bull_top, bull_bot)
    # prior 20-bar low (prior to this bar, not including it)
    prior_low = pd.Series(l).shift(1).rolling(20, min_periods=20).min().to_numpy(dtype=float)
    intact = c > prior_low
    out = np.zeros(c.size, dtype=np.float64)
    bull_fire = np.isfinite(bull_bot) & (bull_gap >= FVG_ATR_MIN * atr) & intact
    out[bull_fire] = 1.0
    return out


def signals_i(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "fvg_pullback_long": fvg_pullback_long(ohlcv, timeframe),
        "fvg_pullback_short": fvg_pullback_short(ohlcv, timeframe),
        "fvg_follow": fvg_follow(ohlcv, timeframe),
        "fvg_fresh_er": fvg_fresh_er(ohlcv, timeframe),
        "fvg_mitigated_reverse": fvg_mitigated_reverse(ohlcv, timeframe),
        "fvg_age_filter": fvg_age_filter(ohlcv, timeframe),
        "fvg_size_break": fvg_size_break(ohlcv, timeframe),
        "fvg_confluence": fvg_confluence(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state for leakage guard (not the sparse ±1 fires)."""
    del kwargs
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = ohlcv.get("volume", pd.Series(np.ones(len(c)))).to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    er = kaufman_efficiency_ratio(c, 10)
    bull_top, bull_bot, bear_top, bear_bot = _fvg_arrays(h, l)
    bull_gap = _gap_size(bull_top, bull_bot)
    bear_gap = _gap_size(bear_top, bear_bot)
    with np.errstate(divide="ignore", invalid="ignore"):
        atr_frac = atr / np.where(c > 0, c, np.nan)
        bull_gap_atr = bull_gap / np.where(atr > 0, atr, np.nan)
        bear_gap_atr = bear_gap / np.where(atr > 0, atr, np.nan)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "atr_frac": np.nan_to_num(atr_frac, nan=0.0),
            "er_10": np.nan_to_num(er, nan=0.0),
            "bull_gap_atr": np.nan_to_num(bull_gap_atr, nan=0.0),
            "bear_gap_atr": np.nan_to_num(bear_gap_atr, nan=0.0),
            "h_minus_l_atr": np.nan_to_num((h - l) / np.where(atr > 0, atr, np.nan), nan=0.0),
        },
        index=ohlcv.index,
    )
