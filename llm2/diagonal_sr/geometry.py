"""Causal diagonal / horizontal geometry from confirmed swings on handed candles.

All line values at decision bar t use only swings with confirm_ts_ms <= t.
No warehouse join: swings are recomputed from the Open-High-Low-Close-Volume
frame that is passed in (builder-responsiveness / CAUS-WAREHOUSE-001).
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

_INDICATORS_SRC = Path(r"C:\projects\botsgeneral\packages\indicators\src")
if _INDICATORS_SRC.is_dir() and str(_INDICATORS_SRC) not in sys.path:
    sys.path.insert(0, str(_INDICATORS_SRC))

from indicators.swings import find_swings, swings_frame  # noqa: E402

SWING_LEFT = 2
SWING_RIGHT = 2
TOUCH_ATR_MULT = 0.25
PLACEBO_RANGE_WINDOW = 50
PLACEBO_LOWER_FRAC = 0.40
PLACEBO_UPPER_FRAC = 0.60


def _ts_ms_from_index(index: pd.DatetimeIndex) -> np.ndarray:
    """UTC epoch milliseconds. Force ns resolution (pandas may store us)."""
    idx = pd.DatetimeIndex(pd.to_datetime(index, utc=True)).as_unit("ns")
    return (idx.asi8 // 1_000_000).astype(np.int64)


def _wilder_atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
    prev_c = np.empty_like(close)
    prev_c[0] = close[0]
    prev_c[1:] = close[:-1]
    tr = np.maximum(high - low, np.maximum(np.abs(high - prev_c), np.abs(low - prev_c)))
    return pd.Series(tr).ewm(alpha=1.0 / period, adjust=False, min_periods=period).mean().to_numpy()


def swings_from_ohlcv(
    ohlcv: pd.DataFrame,
    *,
    left: int = SWING_LEFT,
    right: int = SWING_RIGHT,
) -> pd.DataFrame:
    """Confirmed fractal swings from handed candles only."""
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    ts = _ts_ms_from_index(ohlcv.index)
    swings = find_swings(high, low, ts, left=left, right=right)
    return swings_frame(swings)


def _asof_line_from_anchor_table(
    anchors: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
    decision_pos: np.ndarray,
    *,
    price_col: str = "price",
    slope_col: str = "slope",
    pivot_col: str = "pivot_i",
) -> tuple[pd.Series, pd.Series]:
    """Project (price, slope) anchors onto each decision bar via backward as-of join."""
    nan_line = pd.Series(np.nan, index=decision_index)
    nan_slope = pd.Series(np.nan, index=decision_index)
    if anchors.empty:
        return nan_line, nan_slope

    left = pd.DataFrame(
        {
            "decision_at": pd.DatetimeIndex(decision_index)
            .tz_convert("UTC")
            .as_unit("ns"),
            "pos": np.asarray(decision_pos, dtype=np.int64),
        }
    ).sort_values("decision_at")
    right = anchors.rename(columns={"confirm_ts_ms": "confirm_at"}).copy()
    right["confirm_at"] = pd.to_datetime(
        right["confirm_at"].to_numpy(dtype=np.int64), unit="ms", utc=True
    ).as_unit("ns")
    right = right.sort_values("confirm_at")
    merged = pd.merge_asof(
        left, right, left_on="decision_at", right_on="confirm_at", direction="backward"
    ).sort_values("pos")
    price = merged[price_col].to_numpy(dtype=float)
    slope = merged[slope_col].to_numpy(dtype=float)
    pivot = merged[pivot_col].to_numpy(dtype=float)
    pos = merged["pos"].to_numpy(dtype=float)
    value = price + slope * (pos - pivot)
    # ``merged`` is sorted by pos; map back onto original decision order.
    out_line = np.full(len(decision_index), np.nan)
    out_slope = np.full(len(decision_index), np.nan)
    ord_pos = merged["pos"].to_numpy(dtype=np.int64)
    out_line[ord_pos] = value
    out_slope[ord_pos] = slope
    return (
        pd.Series(out_line, index=decision_index),
        pd.Series(out_slope, index=decision_index),
    )


def last2_line(
    swings: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
    decision_pos: np.ndarray,
) -> tuple[pd.Series, pd.Series]:
    """Line through the last two confirmed same-kind swings (channel_line pattern)."""
    if swings.empty or len(swings) < 2:
        nan = pd.Series(np.nan, index=decision_index)
        return nan, nan.copy()
    s = swings.sort_values("confirm_ts_ms").reset_index(drop=True)
    s["prev_price"] = s["price"].shift(1)
    s["prev_pivot_i"] = s["pivot_i"].shift(1)
    denom = (s["pivot_i"] - s["prev_pivot_i"]).replace(0, np.nan)
    s["slope"] = (s["price"] - s["prev_price"]) / denom
    anchors = s.dropna(subset=["prev_price", "slope"])[
        ["confirm_ts_ms", "price", "slope", "pivot_i"]
    ]
    return _asof_line_from_anchor_table(anchors, decision_index, decision_pos)


def ols_line(
    swings: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
    decision_pos: np.ndarray,
    *,
    n_points: int,
) -> tuple[pd.Series, pd.Series]:
    """Least-squares line through the last ``n_points`` confirmed same-kind swings."""
    nan = pd.Series(np.nan, index=decision_index)
    if swings.empty or len(swings) < n_points:
        return nan, nan.copy()
    s = swings.sort_values("confirm_ts_ms").reset_index(drop=True)
    piv = s["pivot_i"].to_numpy(dtype=float)
    pr = s["price"].to_numpy(dtype=float)
    conf = s["confirm_ts_ms"].to_numpy(dtype=np.int64)
    rows = []
    for i in range(n_points - 1, len(s)):
        x = piv[i - n_points + 1 : i + 1]
        y = pr[i - n_points + 1 : i + 1]
        if np.unique(x).size < 2:
            continue
        xm = x.mean()
        ym = y.mean()
        var = np.sum((x - xm) ** 2)
        if var <= 0:
            continue
        b = float(np.sum((x - xm) * (y - ym)) / var)
        a = float(ym - b * xm)
        rows.append(
            {
                "confirm_ts_ms": int(conf[i]),
                "price": float(a + b * piv[i]),
                "slope": b,
                "pivot_i": float(piv[i]),
            }
        )
    if not rows:
        return nan, nan.copy()
    return _asof_line_from_anchor_table(pd.DataFrame(rows), decision_index, decision_pos)


def parallel_channel(
    high_swings: pd.DataFrame,
    low_swings: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
    decision_pos: np.ndarray,
) -> tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    """Upper last2 highs + parallel lower through last confirmed swing low."""
    upper, up_slope = last2_line(high_swings, decision_index, decision_pos)
    if low_swings.empty or up_slope.isna().all():
        nan = pd.Series(np.nan, index=decision_index)
        return upper, nan, up_slope, nan.copy()

    lows = low_swings.sort_values("confirm_ts_ms").reset_index(drop=True)
    left = pd.DataFrame(
        {
            "decision_at": pd.DatetimeIndex(decision_index).tz_convert("UTC").as_unit("ns"),
            "pos": np.asarray(decision_pos, dtype=np.int64),
            "slope": up_slope.to_numpy(dtype=float),
        }
    ).sort_values("decision_at")
    right = lows.rename(columns={"confirm_ts_ms": "confirm_at"}).copy()
    right["confirm_at"] = pd.to_datetime(
        right["confirm_at"].to_numpy(dtype=np.int64), unit="ms", utc=True
    ).as_unit("ns")
    right = right.sort_values("confirm_at")
    merged = pd.merge_asof(
        left, right, left_on="decision_at", right_on="confirm_at", direction="backward"
    ).sort_values("pos")
    lower = merged["price"].to_numpy(dtype=float) + merged["slope"].to_numpy(dtype=float) * (
        merged["pos"].to_numpy(dtype=float) - merged["pivot_i"].to_numpy(dtype=float)
    )
    out = np.full(len(decision_index), np.nan)
    out[merged["pos"].to_numpy(dtype=np.int64)] = lower
    return upper, pd.Series(out, index=decision_index), up_slope, up_slope.copy()


def _touch_count_since_confirm(
    ohlcv: pd.DataFrame,
    line: pd.Series,
    atr: np.ndarray,
    *,
    kind: str,
) -> pd.Series:
    """Causal cumulative touches of ``line`` within ATR band (past bars only)."""
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    lv = line.to_numpy(dtype=float)
    band = TOUCH_ATR_MULT * atr
    if kind == "high":
        touch = (high >= lv - band) & (high <= lv + band) & np.isfinite(lv) & np.isfinite(band)
    else:
        touch = (low <= lv + band) & (low >= lv - band) & np.isfinite(lv) & np.isfinite(band)
    line_change = np.zeros(len(lv), dtype=bool)
    finite = np.isfinite(lv)
    prev = np.roll(lv, 1)
    prev[0] = np.nan
    line_change[1:] = finite[1:] & (
        (~np.isfinite(prev[1:])) | (np.abs(lv[1:] - prev[1:]) > 1e-12)
    )
    seg = np.cumsum(line_change.astype(np.int64))
    out = pd.Series(touch.astype(np.int64)).groupby(seg).cumsum().to_numpy(dtype=float)
    out[~np.isfinite(lv)] = np.nan
    return pd.Series(out, index=ohlcv.index)


def validated_min3_line(
    swings: pd.DataFrame,
    ohlcv: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
    decision_pos: np.ndarray,
    atr: np.ndarray,
    *,
    kind: str,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    """last2 line inactive until 3 causal touches after the second swing confirms."""
    line, slope = last2_line(swings, decision_index, decision_pos)
    touches = _touch_count_since_confirm(ohlcv, line, atr, kind=kind)
    active = touches >= 3.0
    return line.where(active), slope.where(active), touches


def horizontal_levels(
    high_swings: pd.DataFrame,
    low_swings: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
) -> tuple[pd.Series, pd.Series]:
    """Last confirmed resistance (swing high) and support (swing low) as-of each bar."""

    def _last_price(swings: pd.DataFrame) -> pd.Series:
        if swings.empty:
            return pd.Series(np.nan, index=decision_index)
        left = pd.DataFrame(
            {
                "decision_at": pd.DatetimeIndex(decision_index).tz_convert("UTC").as_unit("ns"),
                "ord": np.arange(len(decision_index)),
            }
        ).sort_values("decision_at")
        right = swings.rename(columns={"confirm_ts_ms": "confirm_at"}).copy()
        right["confirm_at"] = pd.to_datetime(
            right["confirm_at"].to_numpy(dtype=np.int64), unit="ms", utc=True
        ).as_unit("ns")
        right = right.sort_values("confirm_at")
        merged = pd.merge_asof(
            left, right, left_on="decision_at", right_on="confirm_at", direction="backward"
        ).sort_values("ord")
        return pd.Series(merged["price"].to_numpy(dtype=float), index=decision_index)

    return _last_price(high_swings), _last_price(low_swings)


def donchian_boundaries(ohlcv: pd.DataFrame, *, window: int = 20) -> tuple[pd.Series, pd.Series]:
    high, low = ohlcv["high"], ohlcv["low"]
    return (
        high.rolling(window, min_periods=window).max().shift(1),
        low.rolling(window, min_periods=window).min().shift(1),
    )


def placebo_range_boundaries(ohlcv: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    high, low = ohlcv["high"], ohlcv["low"]
    rh = high.rolling(PLACEBO_RANGE_WINDOW, min_periods=PLACEBO_RANGE_WINDOW).max().shift(1)
    rl = low.rolling(PLACEBO_RANGE_WINDOW, min_periods=PLACEBO_RANGE_WINDOW).min().shift(1)
    span = rh - rl
    return rl + PLACEBO_UPPER_FRAC * span, rl + PLACEBO_LOWER_FRAC * span


def shuffled_slope_last2(
    swings: pd.DataFrame,
    decision_index: pd.DatetimeIndex,
    decision_pos: np.ndarray,
    *,
    seed: int = 20260821,
) -> tuple[pd.Series, pd.Series]:
    """Placebo: last2 line levels with randomly permuted slopes."""
    line, slope = last2_line(swings, decision_index, decision_pos)
    rng = np.random.default_rng(seed)
    s = slope.to_numpy(dtype=float).copy()
    finite = np.isfinite(s)
    vals = s[finite]
    if vals.size:
        s[finite] = rng.permutation(vals)
    return line, pd.Series(s, index=decision_index)


def build_geometry_frame(ohlcv: pd.DataFrame) -> pd.DataFrame:
    """All closed constructions + placebos + ATR, aligned to ``ohlcv`` index."""
    idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    pos = np.arange(len(idx), dtype=np.int64)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    atr = _wilder_atr(high, low, close)

    all_sw = swings_from_ohlcv(ohlcv)
    hi = all_sw[all_sw["kind"] == "high"].copy() if not all_sw.empty else all_sw
    lo = all_sw[all_sw["kind"] == "low"].copy() if not all_sw.empty else all_sw

    out = pd.DataFrame(index=ohlcv.index)
    out["atr"] = atr
    out["atr_frac"] = atr / np.where(close > 0, close, np.nan)

    l2u, l2us = last2_line(hi, idx, pos)
    l2l, l2ls = last2_line(lo, idx, pos)
    out["last2_upper"] = l2u.to_numpy()
    out["last2_upper_slope"] = l2us.to_numpy()
    out["last2_lower"] = l2l.to_numpy()
    out["last2_lower_slope"] = l2ls.to_numpy()

    o3u, o3us = ols_line(hi, idx, pos, n_points=3)
    o3l, o3ls = ols_line(lo, idx, pos, n_points=3)
    out["ols3_upper"] = o3u.to_numpy()
    out["ols3_upper_slope"] = o3us.to_numpy()
    out["ols3_lower"] = o3l.to_numpy()
    out["ols3_lower_slope"] = o3ls.to_numpy()

    o5u, o5us = ols_line(hi, idx, pos, n_points=5)
    o5l, o5ls = ols_line(lo, idx, pos, n_points=5)
    out["ols5_upper"] = o5u.to_numpy()
    out["ols5_upper_slope"] = o5us.to_numpy()
    out["ols5_lower"] = o5l.to_numpy()
    out["ols5_lower_slope"] = o5ls.to_numpy()

    ch_u, ch_l, ch_us, ch_ls = parallel_channel(hi, lo, idx, pos)
    out["channel_upper"] = ch_u.to_numpy()
    out["channel_lower"] = ch_l.to_numpy()
    out["channel_upper_slope"] = ch_us.to_numpy()
    out["channel_lower_slope"] = ch_ls.to_numpy()

    v3u, v3us, tcu = validated_min3_line(hi, ohlcv, idx, pos, atr, kind="high")
    v3l, v3ls, tcl = validated_min3_line(lo, ohlcv, idx, pos, atr, kind="low")
    out["valid3_upper"] = v3u.to_numpy()
    out["valid3_upper_slope"] = v3us.to_numpy()
    out["valid3_upper_touches"] = tcu.to_numpy()
    out["valid3_lower"] = v3l.to_numpy()
    out["valid3_lower_slope"] = v3ls.to_numpy()
    out["valid3_lower_touches"] = tcl.to_numpy()

    hz_u, hz_l = horizontal_levels(hi, lo, idx)
    out["horiz_resist"] = hz_u.to_numpy()
    out["horiz_support"] = hz_l.to_numpy()

    d_u, d_l = donchian_boundaries(ohlcv)
    out["donchian20_upper"] = d_u.to_numpy()
    out["donchian20_lower"] = d_l.to_numpy()

    p_u, p_l = placebo_range_boundaries(ohlcv)
    out["placebo_upper"] = p_u.to_numpy()
    out["placebo_lower"] = p_l.to_numpy()

    sh_line, sh_slope = shuffled_slope_last2(hi, idx, pos)
    out["shuffled_upper"] = sh_line.to_numpy()
    out["shuffled_upper_slope"] = sh_slope.to_numpy()

    return out
