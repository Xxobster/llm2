"""Trading-session, time-of-day and weekend structure (causal).

Why this exists
---------------
Crypto perpetuals trade continuously, but the *flow* that moves them is not
continuous. Three clock facts drive the "New York manipulation" folklore:

* **12:30 UTC (08:30 New York time)** — scheduled United States macro releases
  (Consumer Price Index, Non-Farm Payrolls, Producer Price Index, retail sales,
  jobless claims). The largest scheduled volatility of the day.
* **13:30 UTC (09:30 NY)** — New York Stock Exchange / Nasdaq cash open. Chicago
  Mercantile Exchange equity and Bitcoin futures liquidity steps up sharply.
* **20:00 UTC (16:00 NY)** — cash close and market-on-close imbalance.

The Inner Circle Trader (Michael J. Huddleston) claim is that early in the New
York session price makes a false move ("Judas swing") that takes out the stop
clusters resting just beyond the completed Asia / London session extreme or the
previous day's extreme, and then reverses into the real direction of the day.
The mechanical reason stops cluster there is mundane: obvious session extremes
and previous-day extremes are where retail and simple algorithms place stops, so
sweeping them supplies the liquidity a large participant needs to fill.

This module only exposes the *testable* part of that story:

* which session a bar belongs to,
* the extremes of already-**completed** sessions,
* whether the current bar swept such an extreme and closed back inside.

Causality rules enforced here
-----------------------------
* A session extreme is exposed only from the first bar **after** that session
  has finished. The Asia range of the current day is unknown at 03:00 UTC.
* Previous-day and previous-week extremes use fully closed calendar buckets.
* Nothing is centred, back-filled, or normalised on full history.

All boundaries are UTC. United States daylight-saving shifts the New York clock
by one hour twice a year; ``NY_DST_AWARE`` variants are provided so a hunt can
test whether the shift matters instead of assuming it.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# UTC session windows [start_hour, end_hour) — end exclusive.
SESSIONS: dict[str, tuple[int, int]] = {
    "asia": (0, 8),
    "london": (7, 12),
    "ny": (12, 21),
}
# Inner Circle Trader "killzones" (UTC), plus the macro-release hour.
KILLZONES: dict[str, tuple[int, int]] = {
    "asia_kz": (0, 4),
    "london_kz": (7, 10),
    "ny_am_kz": (12, 15),
    "silver_bullet": (14, 15),
    "ny_pm_kz": (18, 21),
    "macro_release": (12, 13),
    "cash_open": (13, 14),
    "cash_close": (20, 21),
}
SWEEP_LEVELS: tuple[str, ...] = (
    "prev_day_high",
    "prev_day_low",
    "asia_high",
    "asia_low",
    "london_high",
    "london_low",
    "prev_week_high",
    "prev_week_low",
)


def _utc_index(ohlcv: pd.DataFrame) -> pd.DatetimeIndex:
    return pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True)).as_unit("ns")


def _wilder_atr(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    prev_c = np.empty_like(close)
    prev_c[0] = close[0]
    prev_c[1:] = close[:-1]
    tr = np.maximum(high - low, np.maximum(np.abs(high - prev_c), np.abs(low - prev_c)))
    return (
        pd.Series(tr)
        .ewm(alpha=1.0 / period, adjust=False, min_periods=period)
        .mean()
        .to_numpy(dtype=float)
    )


def _completed_bucket_extreme(
    high: pd.Series,
    low: pd.Series,
    bucket: pd.Series,
) -> tuple[pd.Series, pd.Series]:
    """High/low of the **previous** complete bucket, held across the next bucket.

    ``bucket`` must be non-decreasing (calendar day, week, ...). The result at a
    bar inside bucket ``k`` is the extreme of bucket ``k-1`` — never ``k``.
    """
    agg = pd.DataFrame({"bucket": bucket.to_numpy(), "high": high.to_numpy(), "low": low.to_numpy()})
    per = agg.groupby("bucket", sort=True).agg(high=("high", "max"), low=("low", "min"))
    prev = per.shift(1)
    hi = bucket.map(prev["high"]).to_numpy(dtype=float)
    lo = bucket.map(prev["low"]).to_numpy(dtype=float)
    return pd.Series(hi, index=high.index), pd.Series(lo, index=high.index)


def _same_day_session_extreme(
    high: pd.Series,
    low: pd.Series,
    day: pd.Series,
    hour: np.ndarray,
    *,
    start_h: int,
    end_h: int,
) -> tuple[pd.Series, pd.Series]:
    """Extreme of today's session, exposed only from ``end_h`` onward.

    Before the session closes the value is NaN, so a signal cannot peek at a
    range that is still forming.
    """
    in_sess = (hour >= start_h) & (hour < end_h)
    hi_masked = high.where(in_sess)
    lo_masked = low.where(in_sess)
    frame = pd.DataFrame(
        {"day": day.to_numpy(), "high": hi_masked.to_numpy(), "low": lo_masked.to_numpy()}
    )
    per = frame.groupby("day", sort=True).agg(high=("high", "max"), low=("low", "min"))
    hi = day.map(per["high"]).to_numpy(dtype=float)
    lo = day.map(per["low"]).to_numpy(dtype=float)
    visible = hour >= end_h
    hi = np.where(visible, hi, np.nan)
    lo = np.where(visible, lo, np.nan)
    return pd.Series(hi, index=high.index), pd.Series(lo, index=high.index)


def session_frame(ohlcv: pd.DataFrame, *, atr_period: int = 14) -> pd.DataFrame:
    """Session flags, completed-session extremes, sweep bits and ATR distances."""
    idx = _utc_index(ohlcv)
    high = pd.Series(ohlcv["high"].to_numpy(dtype=float), index=ohlcv.index)
    low = pd.Series(ohlcv["low"].to_numpy(dtype=float), index=ohlcv.index)
    close = pd.Series(ohlcv["close"].to_numpy(dtype=float), index=ohlcv.index)

    hour = idx.hour.to_numpy()
    minute = idx.minute.to_numpy()
    dow = idx.dayofweek.to_numpy()
    day = pd.Series(idx.floor("D").astype("int64"), index=ohlcv.index)
    # Monday-anchored week bucket without the tz-dropping PeriodIndex conversion.
    week = pd.Series(
        (idx.floor("D") - pd.to_timedelta(dow, unit="D")).astype("int64"),
        index=ohlcv.index,
    )

    atr = _wilder_atr(
        high.to_numpy(), low.to_numpy(), close.to_numpy(), period=atr_period
    )
    atr_s = pd.Series(atr, index=ohlcv.index)
    atr_safe = atr_s.replace(0.0, np.nan)

    out = pd.DataFrame(index=ohlcv.index)
    out["atr"] = atr_s
    out["atr_frac"] = atr_s / close.replace(0.0, np.nan)
    out["hour_utc"] = hour.astype(float)
    out["minute_utc"] = minute.astype(float)
    out["dow"] = dow.astype(float)
    out["is_weekend"] = ((dow == 5) | (dow == 6)).astype(float)
    out["is_monday"] = (dow == 0).astype(float)
    out["is_friday"] = (dow == 4).astype(float)
    # Thin-liquidity window: Friday 21:00 UTC through Sunday 21:00 UTC.
    out["is_weekend_window"] = (
        ((dow == 4) & (hour >= 21)) | (dow == 5) | ((dow == 6) & (hour < 21))
    ).astype(float)

    for name, (a, b) in SESSIONS.items():
        out[f"in_{name}"] = ((hour >= a) & (hour < b)).astype(float)
    for name, (a, b) in KILLZONES.items():
        out[f"in_{name}"] = ((hour >= a) & (hour < b)).astype(float)

    ny_start = SESSIONS["ny"][0]
    out["hours_since_ny_open"] = np.where(
        hour >= ny_start, (hour - ny_start).astype(float), np.nan
    )

    pd_high, pd_low = _completed_bucket_extreme(high, low, day)
    pw_high, pw_low = _completed_bucket_extreme(high, low, week)
    a_high, a_low = _same_day_session_extreme(
        high, low, day, hour, start_h=SESSIONS["asia"][0], end_h=SESSIONS["asia"][1]
    )
    l_high, l_low = _same_day_session_extreme(
        high, low, day, hour, start_h=SESSIONS["london"][0], end_h=SESSIONS["london"][1]
    )

    levels = {
        "prev_day_high": pd_high,
        "prev_day_low": pd_low,
        "prev_week_high": pw_high,
        "prev_week_low": pw_low,
        "asia_high": a_high,
        "asia_low": a_low,
        "london_high": l_high,
        "london_low": l_low,
    }
    for name, series in levels.items():
        out[f"lvl_{name}"] = series
        out[f"dist_{name}_atr"] = (close - series) / atr_safe

    # Sweep = trade through a completed extreme, then close back inside it.
    # This is the only mechanically testable part of the Judas-swing story.
    for name, series in levels.items():
        lv = series.to_numpy(dtype=float)
        finite = np.isfinite(lv)
        if name.endswith("_high"):
            pierced = finite & (high.to_numpy() > lv)
            reclaimed = pierced & (close.to_numpy() < lv)
        else:
            pierced = finite & (low.to_numpy() < lv)
            reclaimed = pierced & (close.to_numpy() > lv)
        out[f"pierce_{name}"] = pierced.astype(float)
        out[f"sweep_{name}"] = reclaimed.astype(float)

    # Dealing-range position inside the completed previous day (premium/discount).
    span = (pd_high - pd_low).replace(0.0, np.nan)
    out["prev_day_range_pos"] = (close - pd_low) / span
    out["prev_day_range_atr"] = (pd_high - pd_low) / atr_safe
    out["in_premium_prev_day"] = (out["prev_day_range_pos"] > 0.5).astype(float)

    return out


def sweep_event(
    session: pd.DataFrame,
    *,
    level: str,
    killzone: str | None = "ny_am_kz",
    exclude_weekend: bool = False,
) -> np.ndarray:
    """Boolean event: swept ``level`` and closed back inside, inside ``killzone``.

    A swept *high* is a short signal (sell-side liquidity taken above, price
    rejected); a swept *low* is a long signal.
    """
    if f"sweep_{level}" not in session.columns:
        raise ValueError(f"unknown sweep level {level!r}")
    fire = session[f"sweep_{level}"].to_numpy(dtype=float) > 0.5
    if killzone:
        col = f"in_{killzone}"
        if col not in session.columns:
            raise ValueError(f"unknown killzone {killzone!r}")
        fire &= session[col].to_numpy(dtype=float) > 0.5
    if exclude_weekend:
        fire &= session["is_weekend_window"].to_numpy(dtype=float) < 0.5
    return fire


def sweep_event_side(level: str) -> int:
    """Short after a swept high, long after a swept low."""
    if level.endswith("_high"):
        return -1
    if level.endswith("_low"):
        return 1
    raise ValueError(f"level {level!r} has no side")
