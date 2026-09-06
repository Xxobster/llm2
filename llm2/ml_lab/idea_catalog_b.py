"""Hunt 005 causal ideas not in the hunt-004 thirty.

Opening-range follow, swing structure, wick rejection follow, rising Average
Directional Index, NR7 break, volume spring, cumulative-volume-delta slope,
UTC-day open drive.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import wilder_dmi
from llm2.ml_lab.idea_catalog import _ret, _sign_nz, _zscore
from llm2.validation.folds import index_to_ms

ORB_BARS = {"5m": 48, "15m": 16, "1h": 4, "4h": 1, "1d": 1}
IDEA_IDS_B: tuple[str, ...] = (
    "utc_orb_follow",
    "structure_swings",
    "wick_reject_follow",
    "adx_rising",
    "nr7_break",
    "vol_spring",
    "cvd_slope",
    "utc_open_drive",
)
IDEA_IDS_B5: tuple[str, ...] = ("cvd_slope_cross", "cvd_z_fire")


def utc_orb_follow(ohlcv: pd.DataFrame, timeframe: str) -> np.ndarray:
    """After the first K bars of the UTC day, follow a break of that frozen range."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    n = c.size
    out = np.zeros(n, dtype=np.float64)
    k = int(ORB_BARS.get(timeframe, 4))
    if n < k + 2:
        return out
    day = index_to_ms(ohlcv.index) // 86_400_000
    cum = pd.Series(np.arange(n)).groupby(day, sort=False).cumcount().to_numpy()
    in_open = cum < k
    orh = pd.Series(np.where(in_open, h, np.nan)).groupby(day, sort=False).transform("max").to_numpy()
    orl = pd.Series(np.where(in_open, l, np.nan)).groupby(day, sort=False).transform("min").to_numpy()
    tradable = cum >= k
    out[tradable & (c > orh)] = 1.0
    out[tradable & (c < orl)] = -1.0
    return out


def structure_swings(ohlcv: pd.DataFrame) -> np.ndarray:
    """Higher lows then close through prior swing high (and mirror)."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    n = c.size
    out = np.zeros(n, dtype=np.float64)
    if n < 40:
        return out
    l10 = np.roll(l, 10)
    l20 = np.roll(l, 20)
    h10 = np.roll(h, 10)
    h20 = np.roll(h, 20)
    l10[:20] = np.nan
    h10[:20] = np.nan
    hh = (l > l10) & (l10 > l20) & (c > h10)
    ll = (h < h10) & (h10 < h20) & (c < l10)
    out[hh] = 1.0
    out[ll] = -1.0
    return out


def wick_reject_follow(ohlcv: pd.DataFrame) -> np.ndarray:
    """Long lower-wick rejection at a 20-bar low; short upper-wick at a 20-bar high."""
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    rng = h - l
    with np.errstate(divide="ignore", invalid="ignore"):
        lw = (np.minimum(o, c) - l) / np.where(rng > 1e-15, rng, np.nan)
        uw = (h - np.maximum(o, c)) / np.where(rng > 1e-15, rng, np.nan)
    lo20 = pd.Series(l).rolling(20, min_periods=20).min().shift(1).to_numpy()
    hi20 = pd.Series(h).rolling(20, min_periods=20).max().shift(1).to_numpy()
    out = np.zeros(c.size, dtype=np.float64)
    out[(lw >= 0.60) & (l <= lo20) & (c > o)] = 1.0
    out[(uw >= 0.60) & (h >= hi20) & (c < o)] = -1.0
    return out


def adx_rising(ohlcv: pd.DataFrame) -> np.ndarray:
    """Follow +DI/−DI only while Average Directional Index is rising."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    plus_di, minus_di, adx = wilder_dmi(h, l, c, 14)
    prev = np.roll(adx, 5)
    prev[:5] = np.nan
    rising = adx > prev
    out = np.zeros(c.size, dtype=np.float64)
    out[rising & (plus_di > minus_di)] = 1.0
    out[rising & (minus_di > plus_di)] = -1.0
    return out


def nr7_break(ohlcv: pd.DataFrame) -> np.ndarray:
    """Inside the 7-bar narrowest range, follow a close break of that bar."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    rng = h - l
    rmin = pd.Series(rng).rolling(7, min_periods=7).min().to_numpy()
    is_nr7 = np.isfinite(rmin) & (rng <= rmin * 1.0000001)
    prev_nr = np.roll(is_nr7, 1)
    prev_nr[0] = False
    prev_h = np.roll(h, 1)
    prev_l = np.roll(l, 1)
    out = np.zeros(c.size, dtype=np.float64)
    out[prev_nr & (c > prev_h)] = 1.0
    out[prev_nr & (c < prev_l)] = -1.0
    return out


def vol_spring(ohlcv: pd.DataFrame) -> np.ndarray:
    """Quiet volume then a shock bar: follow the shock close."""
    c = ohlcv["close"].to_numpy(dtype=float)
    vol = ohlcv["volume"].to_numpy(dtype=float) if "volume" in ohlcv.columns else np.ones(c.size)
    quiet = pd.Series(vol).rolling(8, min_periods=8).mean() / pd.Series(vol).rolling(
        96, min_periods=96
    ).mean().replace(0, np.nan)
    z = _zscore(vol, 96)
    r = _ret(c)
    q = quiet.to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    m = (q <= 0.55) & (z >= 1.5)
    out[m] = _sign_nz(r)[m]
    return out


def cvd_slope_raw(ohlcv: pd.DataFrame) -> np.ndarray:
    """24-bar close-location volume slope (not a trade signal)."""
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    vol = ohlcv["volume"].to_numpy(dtype=float) if "volume" in ohlcv.columns else np.ones(c.size)
    rng = h - l
    with np.errstate(divide="ignore", invalid="ignore"):
        clv = ((c - l) - (h - c)) / np.where(rng > 1e-15, rng, np.nan)
    cvd = np.cumsum(np.nan_to_num(clv * vol, nan=0.0))
    slope = cvd - np.roll(cvd, 24)
    slope[:24] = np.nan
    return slope


def cvd_slope(ohlcv: pd.DataFrame) -> np.ndarray:
    """Sign of a 24-bar slope of close-location times volume (always-on; hunt-005)."""
    return _sign_nz(cvd_slope_raw(ohlcv))


def cvd_slope_cross(ohlcv: pd.DataFrame) -> np.ndarray:
    """Fire only when the 24-bar slope *changes sign* (sparse; hunt-005b)."""
    slope = cvd_slope_raw(ohlcv)
    prev = np.roll(slope, 1)
    prev[0] = np.nan
    out = np.zeros(slope.size, dtype=np.float64)
    out[(prev <= 0.0) & (slope > 0.0)] = 1.0
    out[(prev >= 0.0) & (slope < 0.0)] = -1.0
    return out


def cvd_z_fire(ohlcv: pd.DataFrame) -> np.ndarray:
    """Follow slope sign only when |96-bar z-score of slope| >= 1.5 (sparse; hunt-005b)."""
    slope = cvd_slope_raw(ohlcv)
    z = _zscore(slope, 96)
    out = np.zeros(slope.size, dtype=np.float64)
    hot = np.abs(z) >= 1.5
    out[hot] = _sign_nz(slope)[hot]
    return out


def utc_open_drive(ohlcv: pd.DataFrame) -> np.ndarray:
    """First bar of the UTC day sets direction; follow it for the rest of that day."""
    o = ohlcv["open"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    n = c.size
    out = np.zeros(n, dtype=np.float64)
    day = index_to_ms(ohlcv.index) // 86_400_000
    cum = pd.Series(np.arange(n)).groupby(day, sort=False).cumcount().to_numpy()
    drive = _sign_nz(c - o)
    first = np.where(cum == 0, drive, np.nan)
    filled = pd.Series(first).groupby(day, sort=False).transform("first").to_numpy()
    out[cum >= 1] = np.nan_to_num(filled[cum >= 1], nan=0.0)
    return out


def signals_b(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "utc_orb_follow": utc_orb_follow(ohlcv, timeframe),
        "structure_swings": structure_swings(ohlcv),
        "wick_reject_follow": wick_reject_follow(ohlcv),
        "adx_rising": adx_rising(ohlcv),
        "nr7_break": nr7_break(ohlcv),
        "vol_spring": vol_spring(ohlcv),
        "cvd_slope": cvd_slope(ohlcv),
        "utc_open_drive": utc_open_drive(ohlcv),
    }


def signals_b5(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    del timeframe
    return {
        "cvd_slope_cross": cvd_slope_cross(ohlcv),
        "cvd_z_fire": cvd_z_fire(ohlcv),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    from llm2.autonomy.public_formulas import wilder_atr

    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    tf = str(_kwargs.get("timeframe") or _kwargs.get("interval") or "1h")
    _plus, _minus, adx = wilder_dmi(h, l, c, 14)
    sig = signals_b(ohlcv, tf)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "adx": adx,
            "atr_frac": wilder_atr(h, l, c, 14) / np.where(c > 0, c, np.nan),
            "utc_orb_follow": sig["utc_orb_follow"],
            "nr7_break": sig["nr7_break"],
            "adx_rising": sig["adx_rising"],
        },
        index=ohlcv.index,
    )


def build_features_for_guard_b5(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    from llm2.autonomy.public_formulas import wilder_atr

    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    sig = signals_b5(ohlcv, str(_kwargs.get("timeframe") or _kwargs.get("interval") or "1h"))
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "atr_frac": wilder_atr(h, l, c, 14) / np.where(c > 0, c, np.nan),
            "cvd_slope_cross": sig["cvd_slope_cross"],
            "cvd_z_fire": sig["cvd_z_fire"],
        },
        index=ohlcv.index,
    )
