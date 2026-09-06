"""Hunt 007 causal ideas: failed Donchian break, NY cash range, confirm bars.

Frozen for `ml_lab_hunt_007_confirm_session`. Every signal is +1 / 0 / −1
from completed bars only. Thresholds are module constants.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import donchian_prior, wilder_atr
from llm2.ml_lab.idea_catalog import ATR_FRAC_COMPRESS, GAP_TH, _ret, _sign_nz
from llm2.validation.folds import index_to_ms

DONCHIAN_N = 20
CLV_OUTER = 0.60
IMPULSE_N = 3
GAP_WAIT = {"15m": 32, "1h": 8, "4h": 2}
PARENT_MS = {"15m": 3_600_000, "1h": 14_400_000, "4h": 86_400_000}

IDEA_IDS_D: tuple[str, ...] = (
    "failed_break_fade",
    "inside_break_follow",
    "ny_cash_orb_follow",
    "outside_hold_follow",
    "impulse_stall_fade",
    "stealth_break_follow",
    "htf_clv_first_fade",
    "gap_unfilled_follow",
)


def _parts(ohlcv: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ms = index_to_ms(ohlcv.index)
    day = ms // 86_400_000
    hour = (ms % 86_400_000) // 3_600_000
    minute = (ms % 3_600_000) // 60_000
    return day, hour, minute


def failed_break_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a prior-bar Donchian break that closes back inside on this bar."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ll, hh = donchian_prior(h, l, DONCHIAN_N)
    broke_up = c > hh
    broke_dn = c < ll
    prev_up = np.roll(broke_up, 1)
    prev_dn = np.roll(broke_dn, 1)
    prev_up[0] = False
    prev_dn[0] = False
    inside = (c <= hh) & (c >= ll)
    out = np.zeros(c.size, dtype=np.float64)
    out[prev_up & inside] = -1.0
    out[prev_dn & inside] = 1.0
    return out


def inside_break_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """After an inside bar of the mother, follow a close through the mother range."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    mother_h = np.roll(h, 2)
    mother_l = np.roll(l, 2)
    prev_h = np.roll(h, 1)
    prev_l = np.roll(l, 1)
    mother_h[:2] = np.nan
    mother_l[:2] = np.nan
    inside_prev = (prev_h <= mother_h) & (prev_l >= mother_l)
    out = np.zeros(c.size, dtype=np.float64)
    out[inside_prev & (c > mother_h)] = 1.0
    out[inside_prev & (c < mother_l)] = -1.0
    return out


def ny_cash_orb_follow(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """After the New York cash first-hour range (not UTC-day opening range), follow a close break."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, minute = _parts(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    utc_min = hour * 60 + minute
    if timeframe == "15m":
        in_open = (utc_min >= 810) & (utc_min < 870)
        tradable = utc_min >= 870
    elif timeframe == "1h":
        in_open = hour == 13
        tradable = hour >= 14
    else:
        in_open = hour == 12
        tradable = hour >= 16
    orh = pd.Series(np.where(in_open, h, np.nan)).groupby(day, sort=False).transform("max").to_numpy()
    orl = pd.Series(np.where(in_open, l, np.nan)).groupby(day, sort=False).transform("min").to_numpy()
    ok = tradable & np.isfinite(orh) & np.isfinite(orl)
    out[ok & (c > orh)] = 1.0
    out[ok & (c < orl)] = -1.0
    return out


def outside_hold_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow an outside bar only if the next close holds beyond that bar's range."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    prev_h = np.roll(h, 1)
    prev_l = np.roll(l, 1)
    p2_h = np.roll(h, 2)
    p2_l = np.roll(l, 2)
    prev_h[:1] = np.nan
    p2_h[:2] = np.nan
    p2_l[:2] = np.nan
    outside = (prev_h > p2_h) & (prev_l < p2_l)
    out = np.zeros(c.size, dtype=np.float64)
    out[outside & (c > prev_h)] = 1.0
    out[outside & (c < prev_l)] = -1.0
    return out


def impulse_stall_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a three-close impulse that stalls as an inside bar."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    c1 = np.roll(c, 1)
    c2 = np.roll(c, 2)
    c3 = np.roll(c, 3)
    c4 = np.roll(c, 4)
    up3 = (c1 > c2) & (c2 > c3) & (c3 > c4)
    dn3 = (c1 < c2) & (c2 < c3) & (c3 < c4)
    up3[: IMPULSE_N + 1] = False
    dn3[: IMPULSE_N + 1] = False
    prev_h = np.roll(h, 1)
    prev_l = np.roll(l, 1)
    inside = (h <= prev_h) & (l >= prev_l)
    out = np.zeros(c.size, dtype=np.float64)
    out[inside & up3] = -1.0
    out[inside & dn3] = 1.0
    return out


def stealth_break_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a Donchian break only while this bar's range is quiet versus Average True Range."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    ll, hh = donchian_prior(h, l, DONCHIAN_N)
    with np.errstate(divide="ignore", invalid="ignore"):
        quiet = ((h - l) / np.where(c > 0, c, np.nan)) <= ATR_FRAC_COMPRESS
        quiet = quiet | ((h - l) <= (0.85 * atr))
    out = np.zeros(c.size, dtype=np.float64)
    out[quiet & (c > hh)] = 1.0
    out[quiet & (c < ll)] = -1.0
    return out


def htf_clv_first_fade(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """Fade the first child bar after a parent bar that closed in the outer 20% of its range."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ms = index_to_ms(ohlcv.index)
    pid = ms // int(PARENT_MS[timeframe])
    p_high = pd.Series(h).groupby(pid, sort=False).max()
    p_low = pd.Series(l).groupby(pid, sort=False).min()
    p_close = pd.Series(c).groupby(pid, sort=False).last()
    span = p_high - p_low
    with np.errstate(divide="ignore", invalid="ignore"):
        clv = (2.0 * p_close - p_high - p_low) / np.where(np.abs(span) > 1e-15, span, np.nan)
    prev_clv = clv.shift(1)
    mapped = pd.Series(pid).map(prev_clv).to_numpy(dtype=float)
    seq = pd.Series(np.ones(c.size, dtype=np.int8)).groupby(pid, sort=False).cumsum().to_numpy()
    first = seq == 1
    out = np.zeros(c.size, dtype=np.float64)
    out[first & (mapped >= CLV_OUTER)] = -1.0
    out[first & (mapped <= -CLV_OUTER)] = 1.0
    return out


def gap_unfilled_follow(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """Follow a UTC-day gap that is still unfilled after a frozen wait (crypto gaps are rare)."""
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, _hour, _minute = _parts(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    wait = int(GAP_WAIT[timeframe])
    first = pd.Series(np.ones(c.size, dtype=np.int8)).groupby(day, sort=False).cumsum().to_numpy() == 1
    day_open = pd.Series(np.where(first, o, np.nan)).groupby(day, sort=False).transform("max").to_numpy()
    last_by_day = pd.Series(c).groupby(day, sort=False).last()
    prior = pd.Series(day).map(last_by_day.shift(1)).to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        gap = day_open / np.where(prior > 0, prior, np.nan) - 1.0
    cum = pd.Series(np.ones(c.size, dtype=np.int8)).groupby(day, sort=False).cumsum().to_numpy()
    fire = cum == (wait + 1)
    run_h = pd.Series(h).groupby(day, sort=False).cummax().to_numpy()
    run_l = pd.Series(l).groupby(day, sort=False).cummin().to_numpy()
    unfilled_up = (gap >= GAP_TH) & (run_l > prior)
    unfilled_dn = (gap <= -GAP_TH) & (run_h < prior)
    out[fire & unfilled_up] = 1.0
    out[fire & unfilled_dn] = -1.0
    return out


def signals_d(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "failed_break_fade": failed_break_fade(ohlcv, timeframe),
        "inside_break_follow": inside_break_follow(ohlcv, timeframe),
        "ny_cash_orb_follow": ny_cash_orb_follow(ohlcv, timeframe),
        "outside_hold_follow": outside_hold_follow(ohlcv, timeframe),
        "impulse_stall_fade": impulse_stall_fade(ohlcv, timeframe),
        "stealth_break_follow": stealth_break_follow(ohlcv, timeframe),
        "htf_clv_first_fade": htf_clv_first_fade(ohlcv, timeframe),
        "gap_unfilled_follow": gap_unfilled_follow(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    tf = str(kwargs.get("timeframe") or kwargs.get("interval") or "1h")
    if tf not in PARENT_MS:
        tf = "1h"
    c = ohlcv["close"].to_numpy(dtype=float)
    sig = signals_d(ohlcv, tf)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "failed_break_fade": sig["failed_break_fade"],
            "inside_break_follow": sig["inside_break_follow"],
            "ny_cash_orb_follow": sig["ny_cash_orb_follow"],
            "outside_hold_follow": sig["outside_hold_follow"],
            "impulse_stall_fade": sig["impulse_stall_fade"],
            "stealth_break_follow": sig["stealth_break_follow"],
            "htf_clv_first_fade": sig["htf_clv_first_fade"],
            "gap_unfilled_follow": sig["gap_unfilled_follow"],
        },
        index=ohlcv.index,
    )
