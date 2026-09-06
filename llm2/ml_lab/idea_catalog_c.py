"""Hunt 006 causal ideas not in hunt 004–005.

Asia-range London break, UTC-day volume-weighted average price reclaim,
engulf, outside-bar follow, five-close streak follow/fade, Relative Strength
Index hook, Moving Average Convergence Divergence histogram cross.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import macd_line_signal, wilder_atr, wilder_rsi
from llm2.ml_lab.idea_catalog import _ret, _sign_nz
from llm2.validation.folds import index_to_ms

STREAK = 5
RSI_LO = 30.0
RSI_HI = 70.0

IDEA_IDS_C: tuple[str, ...] = (
    "asia_range_break",
    "utc_vwap_reclaim",
    "bull_bear_engulf",
    "outside_bar_follow",
    "close_streak_follow",
    "close_streak_fade",
    "rsi_hook",
    "macd_hist_cross",
)


def _day_hour(ohlcv: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    ms = index_to_ms(ohlcv.index)
    return ms // 86_400_000, (ms % 86_400_000) // 3_600_000


def asia_range_break(ohlcv: pd.DataFrame) -> np.ndarray:
    """After UTC 00:00–08:00, follow a close break of that frozen Asia range."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    n = c.size
    out = np.zeros(n, dtype=np.float64)
    day, hour = _day_hour(ohlcv)
    in_asia = hour < 8
    tradable = hour >= 8
    asia_h = pd.Series(np.where(in_asia, h, np.nan)).groupby(day, sort=False).transform("max").to_numpy()
    asia_l = pd.Series(np.where(in_asia, l, np.nan)).groupby(day, sort=False).transform("min").to_numpy()
    ok = tradable & np.isfinite(asia_h) & np.isfinite(asia_l)
    out[ok & (c > asia_h)] = 1.0
    out[ok & (c < asia_l)] = -1.0
    return out


def utc_vwap_reclaim(ohlcv: pd.DataFrame) -> np.ndarray:
    """Close back through UTC-day volume-weighted average price after 3 bars on the other side."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    vol = ohlcv["volume"].to_numpy(dtype=float) if "volume" in ohlcv.columns else np.ones(c.size)
    day, _hour = _day_hour(ohlcv)
    tp = (h + l + c) / 3.0
    cum_pv = pd.Series(tp * vol).groupby(day, sort=False).cumsum().to_numpy()
    cum_v = pd.Series(vol).groupby(day, sort=False).cumsum().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        vwap = cum_pv / np.where(cum_v > 0, cum_v, np.nan)
    below = c < vwap
    above = c > vwap
    same1 = day == np.roll(day, 1)
    same2 = day == np.roll(day, 2)
    same1[0] = False
    same2[:2] = False
    b1 = np.roll(below, 1)
    b2 = np.roll(below, 2)
    a1 = np.roll(above, 1)
    a2 = np.roll(above, 2)
    out = np.zeros(c.size, dtype=np.float64)
    out[above & b1 & b2 & same1 & same2] = 1.0
    out[below & a1 & a2 & same1 & same2] = -1.0
    return out


def bull_bear_engulf(ohlcv: pd.DataFrame) -> np.ndarray:
    """Current body fully covers the prior body; follow the current close."""
    o = ohlcv["open"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    po = np.roll(o, 1)
    pc = np.roll(c, 1)
    po[0] = np.nan
    pc[0] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    bull = (c > o) & (pc < po) & (c >= po) & (o <= pc)
    bear = (c < o) & (pc > po) & (c <= po) & (o >= pc)
    out[bull] = 1.0
    out[bear] = -1.0
    return out


def outside_bar_follow(ohlcv: pd.DataFrame) -> np.ndarray:
    """Outside bar (high and low beyond prior bar); follow the close."""
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ph = np.roll(h, 1)
    pl = np.roll(l, 1)
    ph[0] = np.nan
    pl[0] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    outside = (h > ph) & (l < pl)
    out[outside] = _sign_nz(c - o)[outside]
    return out


def _close_streak(ohlcv: pd.DataFrame) -> np.ndarray:
    c = ohlcv["close"].to_numpy(dtype=float)
    r = _sign_nz(c - np.roll(c, 1))
    r[0] = 0.0
    r1, r2, r3, r4 = np.roll(r, 1), np.roll(r, 2), np.roll(r, 3), np.roll(r, 4)
    r1[0] = 0.0
    r2[:2] = 0.0
    r3[:3] = 0.0
    r4[:4] = 0.0
    acc = (np.abs(r) > 0) & (r == r1) & (r == r2) & (r == r3) & (r == r4)
    acc[: STREAK - 1] = False
    return np.where(acc, r, 0.0)


def close_streak_follow(ohlcv: pd.DataFrame) -> np.ndarray:
    """Five consecutive same-sign close-to-close prints; follow that sign."""
    return _close_streak(ohlcv)


def close_streak_fade(ohlcv: pd.DataFrame) -> np.ndarray:
    """Same five-close streak; fade (frozen opposite of follow)."""
    return -_close_streak(ohlcv)


def rsi_hook(ohlcv: pd.DataFrame) -> np.ndarray:
    """Leave Relative Strength Index 70 / 30 on the first bar back inside."""
    c = ohlcv["close"].to_numpy(dtype=float)
    rsi = wilder_rsi(c, 14)
    prev = np.roll(rsi, 1)
    prev[0] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    out[(prev <= RSI_LO) & (rsi > RSI_LO)] = 1.0
    out[(prev >= RSI_HI) & (rsi < RSI_HI)] = -1.0
    return out


def macd_hist_cross(ohlcv: pd.DataFrame) -> np.ndarray:
    """Moving Average Convergence Divergence histogram crosses zero."""
    c = ohlcv["close"].to_numpy(dtype=float)
    line, sig = macd_line_signal(c, fast=12, slow=26, signal=9)
    hist = line - sig
    prev = np.roll(hist, 1)
    prev[0] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    out[(prev <= 0.0) & (hist > 0.0)] = 1.0
    out[(prev >= 0.0) & (hist < 0.0)] = -1.0
    return out


def signals_c(ohlcv: pd.DataFrame, timeframe: str | None = None) -> dict[str, np.ndarray]:
    del timeframe
    return {
        "asia_range_break": asia_range_break(ohlcv),
        "utc_vwap_reclaim": utc_vwap_reclaim(ohlcv),
        "bull_bear_engulf": bull_bear_engulf(ohlcv),
        "outside_bar_follow": outside_bar_follow(ohlcv),
        "close_streak_follow": close_streak_follow(ohlcv),
        "close_streak_fade": close_streak_fade(ohlcv),
        "rsi_hook": rsi_hook(ohlcv),
        "macd_hist_cross": macd_hist_cross(ohlcv),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    sig = signals_c(ohlcv)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "atr_frac": wilder_atr(h, l, c, 14) / np.where(c > 0, c, np.nan),
            "asia_range_break": sig["asia_range_break"],
            "utc_vwap_reclaim": sig["utc_vwap_reclaim"],
            "rsi_hook": sig["rsi_hook"],
            "macd_hist_cross": sig["macd_hist_cross"],
        },
        index=ohlcv.index,
    )
