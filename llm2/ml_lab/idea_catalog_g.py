"""Hunt 010: contaminated near-miss retunes (parent hunts 004/007/008 viewed).

New *event definitions*, not a stop search. Hunt 010's contaminated runner
scores the pre-lockbox window (nested out-of-sample already viewed). Do not
stamp Shadow-Ready from this family.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import donchian_prior, ema, kaufman_efficiency_ratio, wilder_atr
from llm2.ml_lab.idea_catalog import ATR_FRAC_COMPRESS, _ret
from llm2.ml_lab.idea_catalog_d import DONCHIAN_N, ny_cash_orb_follow
from llm2.ml_lab.idea_catalog_e import asia_open_fade_us, utc_calendar, weekend_range_break

DONCHIAN_SLOW = 55
ER_LOW = 0.35
IMPULSE_N = 5

IDEA_IDS_G: tuple[str, ...] = (
    "failed_break_hold2",
    "failed_break_wick",
    "failed_break_n55",
    "asia_fade_low_er",
    "weekend_break_hold",
    "impulse_stall_5",
    "ny_orb_hold",
    "stealth_er_break",
    "ema_stack_pullback",
    "ema_stack_first_on",
)


def failed_break_hold2(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade only after two consecutive closes back inside a prior Donchian break."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ll, hh = donchian_prior(h, l, DONCHIAN_N)
    broke_up = c > hh
    broke_dn = c < ll
    prev2_up = np.roll(broke_up, 2)
    prev2_dn = np.roll(broke_dn, 2)
    prev2_up[:2] = False
    prev2_dn[:2] = False
    inside = (c <= hh) & (c >= ll)
    prev_inside = np.roll(inside, 1)
    prev_inside[0] = False
    out = np.zeros(c.size, dtype=np.float64)
    out[prev2_up & prev_inside & inside] = -1.0
    out[prev2_dn & prev_inside & inside] = 1.0
    return out


def failed_break_wick(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Same-bar failed break: wick through prior Donchian, close back inside."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ll, hh = donchian_prior(h, l, DONCHIAN_N)
    inside = (c <= hh) & (c >= ll)
    out = np.zeros(c.size, dtype=np.float64)
    out[inside & (h > hh)] = -1.0
    out[inside & (l < ll)] = 1.0
    return out


def failed_break_n55(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Same failed-break event as hunt 007, frozen Donchian 55 instead of 20."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ll, hh = donchian_prior(h, l, DONCHIAN_SLOW)
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


def asia_fade_low_er(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Hunt-008 Asia-open fade only when Kaufman Efficiency Ratio is low."""
    sig = asia_open_fade_us(ohlcv, timeframe)
    er = kaufman_efficiency_ratio(ohlcv["close"].to_numpy(dtype=float), 10)
    out = np.zeros(sig.size, dtype=np.float64)
    ok = np.isfinite(er) & (er <= ER_LOW)
    out[ok] = sig[ok]
    return out


def weekend_break_hold(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a Monday weekend-range break only if Tuesday's first bar still holds."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    _day, _hour, weekday, week_monday = utc_calendar(ohlcv)
    from llm2.ml_lab.idea_catalog_e import _first_true_per_group, _prev_weekend_hl

    we_h, we_l = _prev_weekend_hl(h, l, weekday, week_monday)
    mon = weekend_range_break(ohlcv)
    tue = weekday == 1
    first_tue = _first_true_per_group(tue, week_monday)
    mon_sig = pd.Series(np.where(weekday == 0, mon, np.nan)).groupby(week_monday, sort=False).ffill()
    held = mon_sig.to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    long_ok = first_tue & (held > 0) & np.isfinite(we_h) & (c > we_h)
    short_ok = first_tue & (held < 0) & np.isfinite(we_l) & (c < we_l)
    out[long_ok] = 1.0
    out[short_ok] = -1.0
    return out


def impulse_stall_5(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a five-close impulse that stalls as an inside bar (hunt 007 used three)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    lags = np.stack([np.roll(c, k) for k in range(1, IMPULSE_N + 2)], axis=0)
    up = np.all(lags[:-1] > lags[1:], axis=0)
    dn = np.all(lags[:-1] < lags[1:], axis=0)
    up[: IMPULSE_N + 1] = False
    dn[: IMPULSE_N + 1] = False
    prev_h = np.roll(h, 1)
    prev_l = np.roll(l, 1)
    inside = (h <= prev_h) & (l >= prev_l)
    out = np.zeros(c.size, dtype=np.float64)
    out[inside & up] = -1.0
    out[inside & dn] = 1.0
    return out


def ny_orb_hold(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """New York cash opening-range follow only if the next bar still holds outside."""
    prev = np.roll(ny_cash_orb_follow(ohlcv, timeframe), 1)
    prev[0] = 0.0
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, _wd, _wm = utc_calendar(ohlcv)
    same_day = day == np.roll(day, 1)
    same_day[0] = False
    out = np.zeros(c.size, dtype=np.float64)
    out[same_day & (prev > 0) & (c > np.roll(h, 1))] = 1.0
    out[same_day & (prev < 0) & (c < np.roll(l, 1))] = -1.0
    return out


def stealth_er_break(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Donchian break only when Efficiency Ratio is low (quiet break, not a trend run)."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    er = kaufman_efficiency_ratio(c, 10)
    atr = wilder_atr(h, l, c, 14)
    ll, hh = donchian_prior(h, l, DONCHIAN_N)
    with np.errstate(divide="ignore", invalid="ignore"):
        quiet = ((h - l) <= (0.85 * atr)) | (
            (h - l) / np.where(c > 0, c, np.nan) <= ATR_FRAC_COMPRESS
        )
    ok = np.isfinite(er) & (er <= ER_LOW) & quiet
    out = np.zeros(c.size, dtype=np.float64)
    out[ok & (c > hh)] = 1.0
    out[ok & (c < ll)] = -1.0
    return out


def ema_stack_pullback(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Hunt-004 stack, only when close has pulled back to the 48-span exponential mean."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    e12 = ema(c, 12)
    e48 = ema(c, 48)
    e192 = ema(c, 192)
    atr = wilder_atr(h, l, c, 14)
    stack = (e12 > e48) & (e48 > e192)
    dist = (c - e48) / np.where(atr > 0, atr, np.nan)
    touch = (dist <= 0.35) & (dist >= -0.55)
    out = np.zeros(c.size, dtype=np.float64)
    out[stack & touch] = 1.0
    return out


def ema_stack_first_on(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """First bar the hunt-004 long stack turns on."""
    del timeframe
    c = ohlcv["close"].to_numpy(dtype=float)
    e12 = ema(c, 12)
    e48 = ema(c, 48)
    e192 = ema(c, 192)
    stack = (e12 > e48) & (e48 > e192)
    prev = np.roll(stack, 1)
    prev[0] = False
    out = np.zeros(c.size, dtype=np.float64)
    out[stack & ~prev] = 1.0
    return out


def signals_g(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "failed_break_hold2": failed_break_hold2(ohlcv, timeframe),
        "failed_break_wick": failed_break_wick(ohlcv, timeframe),
        "failed_break_n55": failed_break_n55(ohlcv, timeframe),
        "asia_fade_low_er": asia_fade_low_er(ohlcv, timeframe),
        "weekend_break_hold": weekend_break_hold(ohlcv, timeframe),
        "impulse_stall_5": impulse_stall_5(ohlcv, timeframe),
        "ny_orb_hold": ny_orb_hold(ohlcv, timeframe),
        "stealth_er_break": stealth_er_break(ohlcv, timeframe),
        "ema_stack_pullback": ema_stack_pullback(ohlcv, timeframe),
        "ema_stack_first_on": ema_stack_first_on(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    tf = str(kwargs.get("timeframe") or kwargs.get("interval") or "1h")
    if tf not in ("15m", "1h", "4h"):
        tf = "1h"
    del tf
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ll, hh = donchian_prior(h, l, DONCHIAN_N)
    er = kaufman_efficiency_ratio(c, 10)
    atr = wilder_atr(h, l, c, 14)
    e12 = ema(c, 12)
    e48 = ema(c, 48)
    e192 = ema(c, 192)
    with np.errstate(divide="ignore", invalid="ignore"):
        pos = (c - ll) / np.where((hh - ll) > 1e-15, hh - ll, np.nan)
        atr_frac = atr / np.where(c > 0, c, np.nan)
        ema48_dist = (c - e48) / np.where(atr > 0, atr, np.nan)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "donchian_pos": np.where(np.isfinite(pos), pos, 0.0),
            "er_10": np.where(np.isfinite(er), er, 0.0),
            "atr_frac": np.where(np.isfinite(atr_frac), atr_frac, 0.0),
            "ema_stack_gap": np.where(np.isfinite(e12 - e192), e12 - e192, 0.0),
            "ema48_atr_dist": np.where(np.isfinite(ema48_dist), ema48_dist, 0.0),
        },
        index=ohlcv.index,
    )
