"""Hunt 008 causal ideas: US-hours inventory and weekend range.

Not in hunts 003–007. Every signal is +1 / 0 / −1 from completed bars only.
Hour maps are frozen module constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import wilder_atr
from llm2.ml_lab.idea_catalog import _ret, _sign_nz
from llm2.validation.folds import index_to_ms

# 15-minute / 1-hour: US cash ≈ 13:00–20:00 UTC. 4-hour bars sit on 00/04/08/12/16/20.
US_OPEN_HOUR = {"15m": 13, "1h": 13, "4h": 12}
US_CLOSE_HOUR = {"15m": 19, "1h": 19, "4h": 16}
NY_LUNCH_HOUR = {"15m": 16, "1h": 16, "4h": 16}
LONDON_OPEN_HOUR = {"15m": 8, "1h": 8, "4h": 8}
FRIDAY_UNWIND_HOUR = {"15m": 18, "1h": 18, "4h": 16}

IDEA_IDS_E: tuple[str, ...] = (
    "us_open_drive",
    "us_close_fade",
    "ny_lunch_fade",
    "london_ny_agree",
    "weekend_range_break",
    "weekend_failed_break",
    "friday_late_fade",
    "asia_open_fade_us",
)


def utc_calendar(ohlcv: pd.DataFrame) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Unix-day, UTC hour, Monday=0 weekday, Monday unix-day of that week."""
    ms = index_to_ms(ohlcv.index)
    day = ms // 86_400_000
    hour = (ms % 86_400_000) // 3_600_000
    weekday = (day + 3) % 7
    week_monday = day - weekday
    return day, hour, weekday, week_monday


def _first_true_per_group(mask: np.ndarray, group: np.ndarray) -> np.ndarray:
    seq = pd.Series(mask.astype(np.int8)).groupby(group, sort=False).cumsum().to_numpy()
    return mask & (seq == 1)


def _ffill_day(values: np.ndarray, day: np.ndarray, seed: np.ndarray) -> np.ndarray:
    seeded = np.where(seed, values, np.nan)
    return pd.Series(seeded).groupby(day, sort=False).ffill().to_numpy(dtype=float)


def _prev_weekend_hl(
    high: np.ndarray,
    low: np.ndarray,
    weekday: np.ndarray,
    week_monday: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    we = weekday >= 5
    hi = pd.Series(np.where(we, high, np.nan)).groupby(week_monday, sort=False).max()
    lo = pd.Series(np.where(we, low, np.nan)).groupby(week_monday, sort=False).min()
    key = week_monday - 7
    return (
        pd.Series(key).map(hi).to_numpy(dtype=float),
        pd.Series(key).map(lo).to_numpy(dtype=float),
    )


def us_open_drive(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """First completed US-cash bar: follow that bar's close versus open."""
    o = ohlcv["open"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, _wd, _wm = utc_calendar(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    fire = _first_true_per_group(hour == int(US_OPEN_HOUR[timeframe]), day)
    with np.errstate(divide="ignore", invalid="ignore"):
        bar = c / np.where(o > 0, o, np.nan) - 1.0
    out[fire] = _sign_nz(bar)[fire]
    return out


def us_close_fade(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """First US-close bar: fade the move from the US-open bar close."""
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, _wd, _wm = utc_calendar(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    oh = int(US_OPEN_HOUR[timeframe])
    ch = int(US_CLOSE_HOUR[timeframe])
    if oh == ch:
        return out
    open_px = _ffill_day(c, day, _first_true_per_group(hour == oh, day))
    fire = _first_true_per_group(hour == ch, day)
    with np.errstate(divide="ignore", invalid="ignore"):
        sess = c / open_px - 1.0
    out[fire] = -_sign_nz(sess)[fire]
    return out


def ny_lunch_fade(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """First New York lunch bar: fade the US-open-to-lunch move. Zero on 4-hour (same bar as close)."""
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, _wd, _wm = utc_calendar(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    oh = int(US_OPEN_HOUR[timeframe])
    lh = int(NY_LUNCH_HOUR[timeframe])
    ch = int(US_CLOSE_HOUR[timeframe])
    if lh == oh or lh == ch:
        return out
    open_px = _ffill_day(c, day, _first_true_per_group(hour == oh, day))
    fire = _first_true_per_group(hour == lh, day)
    with np.errstate(divide="ignore", invalid="ignore"):
        move = c / open_px - 1.0
    out[fire] = -_sign_nz(move)[fire]
    return out


def london_ny_agree(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """US-open bar: follow only when London session return agrees with that bar."""
    o = ohlcv["open"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, _wd, _wm = utc_calendar(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    lon_h = int(LONDON_OPEN_HOUR[timeframe])
    oh = int(US_OPEN_HOUR[timeframe])
    if lon_h >= oh:
        return out
    in_lon = (hour >= lon_h) & (hour < oh)
    rev = in_lon[::-1].astype(np.int8)
    seq = pd.Series(rev).groupby(day[::-1], sort=False).cumsum().to_numpy()[::-1]
    last_lon = in_lon & (seq == 1)
    lon_end = _ffill_day(c, day, last_lon)
    lon_open = _ffill_day(o, day, _first_true_per_group(hour == lon_h, day))
    fire = _first_true_per_group(hour == oh, day)
    with np.errstate(divide="ignore", invalid="ignore"):
        lon_ret = lon_end / lon_open - 1.0
        us_ret = c / np.where(o > 0, o, np.nan) - 1.0
    lon_s = _sign_nz(lon_ret)
    us_s = _sign_nz(us_ret)
    ok = fire & (lon_s != 0) & (us_s != 0) & (lon_s == us_s)
    out[ok] = us_s[ok]
    return out


def weekend_range_break(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Monday: first close through the completed Saturday–Sunday range."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, _hour, weekday, week_monday = utc_calendar(ohlcv)
    we_h, we_l = _prev_weekend_hl(h, l, weekday, week_monday)
    mon = weekday == 0
    out = np.zeros(c.size, dtype=np.float64)
    up = mon & np.isfinite(we_h) & (c > we_h)
    dn = mon & np.isfinite(we_l) & (c < we_l)
    out[_first_true_per_group(up, day)] = 1.0
    out[_first_true_per_group(dn, day)] = -1.0
    return out


def weekend_failed_break(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Monday: fade a same-Monday weekend-range break that closes back inside."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, _hour, weekday, week_monday = utc_calendar(ohlcv)
    we_h, we_l = _prev_weekend_hl(h, l, weekday, week_monday)
    mon = weekday == 0
    prev_mon = np.roll(mon, 1)
    prev_mon[0] = False
    prev_c = np.roll(c, 1)
    inside = mon & np.isfinite(we_h) & np.isfinite(we_l) & (c <= we_h) & (c >= we_l)
    fade_up = inside & prev_mon & (prev_c > we_h)
    fade_dn = inside & prev_mon & (prev_c < we_l)
    out = np.zeros(c.size, dtype=np.float64)
    out[_first_true_per_group(fade_up, day)] = -1.0
    out[_first_true_per_group(fade_dn, day)] = 1.0
    return out


def friday_late_fade(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """First Friday unwind bar: fade the Monday-open to now week move."""
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, weekday, week_monday = utc_calendar(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    first_of_day = _first_true_per_group(np.ones(c.size, dtype=bool), day)
    week_seed = (weekday == 0) & first_of_day
    week_px = pd.Series(np.where(week_seed, c, np.nan)).groupby(week_monday, sort=False).ffill()
    week_px = week_px.to_numpy(dtype=float)
    fire = (weekday == 4) & _first_true_per_group(hour == int(FRIDAY_UNWIND_HOUR[timeframe]), day)
    with np.errstate(divide="ignore", invalid="ignore"):
        wret = c / week_px - 1.0
    out[fire] = -_sign_nz(wret)[fire]
    return out


def asia_open_fade_us(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """First bar of the UTC day: fade the prior day's 16:00 UTC-to-close US afternoon."""
    del timeframe
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, _wd, _wm = utc_calendar(ohlcv)
    out = np.zeros(c.size, dtype=np.float64)
    first_pm = _first_true_per_group(hour >= 16, day)
    pm_start = pd.Series(np.where(first_pm, c, np.nan)).groupby(day, sort=False).max()
    day_last = pd.Series(c).groupby(day, sort=False).last()
    with np.errstate(divide="ignore", invalid="ignore"):
        pm_ret = day_last / pm_start - 1.0
    prev_pm = pm_ret.shift(1)
    mapped = pd.Series(day).map(prev_pm).to_numpy(dtype=float)
    fire = _first_true_per_group(np.ones(c.size, dtype=bool), day)
    out[fire] = -_sign_nz(mapped)[fire]
    return out


def signals_e(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "us_open_drive": us_open_drive(ohlcv, timeframe),
        "us_close_fade": us_close_fade(ohlcv, timeframe),
        "ny_lunch_fade": ny_lunch_fade(ohlcv, timeframe),
        "london_ny_agree": london_ny_agree(ohlcv, timeframe),
        "weekend_range_break": weekend_range_break(ohlcv, timeframe),
        "weekend_failed_break": weekend_failed_break(ohlcv, timeframe),
        "friday_late_fade": friday_late_fade(ohlcv, timeframe),
        "asia_open_fade_us": asia_open_fade_us(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state the hunt-008 events are built from (not the sparse ±1 fires).

    Sparse Monday/hour fires are unchanged by a random tip shock and would false-trip
    CAUS-WAREHOUSE-001. These series still recompute from the handed candles.
    """
    tf = str(kwargs.get("timeframe") or kwargs.get("interval") or "1h")
    if tf not in US_OPEN_HOUR:
        tf = "1h"
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day, hour, weekday, week_monday = utc_calendar(ohlcv)
    oh = int(US_OPEN_HOUR[tf])
    open_px = _ffill_day(c, day, _first_true_per_group(hour == oh, day))
    first_of_day = _first_true_per_group(np.ones(c.size, dtype=bool), day)
    week_px = pd.Series(np.where((weekday == 0) & first_of_day, c, np.nan)).groupby(
        week_monday, sort=False
    ).ffill().to_numpy(dtype=float)
    we_h, we_l = _prev_weekend_hl(h, l, weekday, week_monday)
    span = we_h - we_l
    first_pm = _first_true_per_group(hour >= 16, day)
    pm_start = pd.Series(np.where(first_pm, c, np.nan)).groupby(day, sort=False).max()
    day_last = pd.Series(c).groupby(day, sort=False).last()
    with np.errstate(divide="ignore", invalid="ignore"):
        sess = c / open_px - 1.0
        wret = c / week_px - 1.0
        we_pos = (c - we_l) / np.where(np.abs(span) > 1e-15, span, np.nan)
        pm_ret = day_last / pm_start - 1.0
        atr_frac = wilder_atr(h, l, c, 14) / np.where(c > 0, c, np.nan)
    prior_pm = pd.Series(day).map(pm_ret.shift(1)).to_numpy(dtype=float)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "atr_frac": atr_frac,
            "us_session_ret": np.where(np.isfinite(sess), sess, 0.0),
            "week_ret": np.where(np.isfinite(wret), wret, 0.0),
            "weekend_pos": np.where(np.isfinite(we_pos), we_pos, 0.0),
            "prior_us_pm_ret": np.where(np.isfinite(prior_pm), prior_pm, 0.0),
        },
        index=ohlcv.index,
    )
