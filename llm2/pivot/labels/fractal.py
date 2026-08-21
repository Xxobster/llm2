"""Vectorized fractal / ATR-prominence pivot labels (family A).

Historical pivots may use future bars inside this builder only.
Features must never see a pivot before ``confirmed_at_ts_ms``.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from llm2.pivot.labels.config import PivotLabelConfig


@dataclass(frozen=True)
class PivotEvent:
    pivot_origin_ts_ms: int
    confirmed_at_ts_ms: int
    pivot_side: str  # high | low
    pivot_price: float
    pivot_strength: float
    left_prominence_atr: float
    right_reversal_atr: float
    reversal_pct: float
    ambiguous: int = 0


def _true_range(high: np.ndarray, low: np.ndarray, close: np.ndarray) -> np.ndarray:
    prev_close = np.empty_like(close)
    prev_close[0] = close[0]
    prev_close[1:] = close[:-1]
    hl = high - low
    hc = np.abs(high - prev_close)
    lc = np.abs(low - prev_close)
    return np.maximum(hl, np.maximum(hc, lc))


def wilder_atr(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, *, period: int
) -> np.ndarray:
    """Vectorized Wilder ATR (recursive — documented sequential EMA-style)."""
    tr = _true_range(high, low, close)
    atr = np.full(len(tr), np.nan, dtype=float)
    if len(tr) < period:
        return atr
    # Seed with SMA of first ``period`` TRs.
    atr[period - 1] = float(np.mean(tr[:period]))
    alpha = 1.0 / float(period)
    # Path-dependent Wilder smoothing: one forward pass (O(n), unavoidable for RMA).
    for i in range(period, len(tr)):
        atr[i] = atr[i - 1] * (1.0 - alpha) + tr[i] * alpha
    return atr


def _local_extrema_mask(
    values: np.ndarray,
    *,
    left: int,
    right: int,
    mode: str,
    tie_break: str,
) -> np.ndarray:
    """True at indices that are unique local max/min of the window.

    Equality: for ``leftmost``, only the first index of an equal plateau that is
    also window-extreme is kept.
    """
    n = len(values)
    out = np.zeros(n, dtype=bool)
    if n < left + right + 1:
        return out
    s = pd.Series(values)
    win = left + right + 1
    if mode == "max":
        roll = s.rolling(win, center=False).max().to_numpy()
        # roll at index i covers [i-win+1, i]; center candidate at i-right
        # so window is [i-right-left, i-right+right] = [i-left-right, i]
        # candidate index c = i - right requires roll index i = c + right
        for c in range(left, n - right):
            i = c + right
            if not np.isfinite(values[c]) or not np.isfinite(roll[i]):
                continue
            if values[c] < roll[i] - 1e-15:
                continue
            # equal plateau: keep leftmost or rightmost extreme in window
            w0, w1 = c - left, c + right + 1
            window = values[w0:w1]
            if mode == "max":
                m = float(np.nanmax(window))
                idxs = np.flatnonzero(np.isclose(window, m, rtol=0.0, atol=1e-12))
            else:
                m = float(np.nanmin(window))
                idxs = np.flatnonzero(np.isclose(window, m, rtol=0.0, atol=1e-12))
            if idxs.size == 0:
                continue
            chosen = int(idxs[0] if tie_break == "leftmost" else idxs[-1])
            if w0 + chosen == c and np.isclose(values[c], m, rtol=0.0, atol=1e-12):
                out[c] = True
    else:
        roll = s.rolling(win, center=False).min().to_numpy()
        for c in range(left, n - right):
            i = c + right
            if not np.isfinite(values[c]) or not np.isfinite(roll[i]):
                continue
            if values[c] > roll[i] + 1e-15:
                continue
            w0, w1 = c - left, c + right + 1
            window = values[w0:w1]
            m = float(np.nanmin(window))
            idxs = np.flatnonzero(np.isclose(window, m, rtol=0.0, atol=1e-12))
            if idxs.size == 0:
                continue
            chosen = int(idxs[0] if tie_break == "leftmost" else idxs[-1])
            if w0 + chosen == c and np.isclose(values[c], m, rtol=0.0, atol=1e-12):
                out[c] = True
    return out


def local_extrema_mask_vectorized(
    values: np.ndarray,
    *,
    left: int,
    right: int,
    mode: str,
    tie_break: str = "leftmost",
) -> np.ndarray:
    """Local extrema using rolling window comparison (vectorized core + small plateau pass).

    The rolling max/min comparison is fully vectorized. Plateau tie resolution walks
    candidates only (sparse), not every bar via DataFrame.apply.
    """
    n = len(values)
    out = np.zeros(n, dtype=bool)
    if n < left + right + 1:
        return out
    s = pd.Series(values.astype(float))
    win = left + right + 1
    if mode == "max":
        roll = s.rolling(win, min_periods=win).max().to_numpy()
    else:
        roll = s.rolling(win, min_periods=win).min().to_numpy()
    # candidate c at index; rolling completed at i = c + right
    c_idx = np.arange(left, n - right, dtype=np.int64)
    i_idx = c_idx + right
    vals_c = values[c_idx]
    rolls = roll[i_idx]
    if mode == "max":
        cand = np.isfinite(vals_c) & np.isfinite(rolls) & (vals_c >= rolls - 1e-15)
    else:
        cand = np.isfinite(vals_c) & np.isfinite(rolls) & (vals_c <= rolls + 1e-15)
    cands = c_idx[cand]
    # Sparse plateau resolution only on candidates
    for c in cands:
        w0 = int(c - left)
        w1 = int(c + right + 1)
        window = values[w0:w1]
        if mode == "max":
            m = float(np.nanmax(window))
            idxs = np.flatnonzero(np.isclose(window, m, rtol=0.0, atol=1e-12))
        else:
            m = float(np.nanmin(window))
            idxs = np.flatnonzero(np.isclose(window, m, rtol=0.0, atol=1e-12))
        if idxs.size == 0:
            continue
        chosen = int(idxs[0] if tie_break == "leftmost" else idxs[-1])
        if w0 + chosen == int(c):
            out[int(c)] = True
    return out


def _suppress_neighbors(mask: np.ndarray, strength: np.ndarray, *, radius: int) -> np.ndarray:
    """Keep strongest events within ±radius (sequential but on sparse index set)."""
    if radius <= 0:
        return mask
    idx = np.flatnonzero(mask)
    if idx.size == 0:
        return mask
    order = idx[np.argsort(-strength[idx], kind="mergesort")]
    keep = np.zeros(len(mask), dtype=bool)
    taken = np.zeros(len(mask), dtype=bool)
    for i in order:
        lo = max(0, int(i) - radius)
        hi = min(len(mask), int(i) + radius + 1)
        if taken[lo:hi].any():
            continue
        keep[i] = True
        taken[lo:hi] = True
    return keep


def label_fractal_pivots(
    ohlcv: pd.DataFrame,
    cfg: PivotLabelConfig,
    *,
    ts_ms: np.ndarray | None = None,
) -> pd.DataFrame:
    """Return pivot events as a DataFrame (one row per qualified pivot).

    Requires columns open/high/low/close. Index may be DatetimeIndex; ts_ms optional.
    """
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    n = len(ohlcv)
    if ts_ms is None:
        if "ts_ms" in ohlcv.columns:
            ts = ohlcv["ts_ms"].to_numpy(dtype=np.int64)
        else:
            idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
            ts = (idx.asi8 // 1_000_000).astype(np.int64)
    else:
        ts = np.asarray(ts_ms, dtype=np.int64)

    atr = wilder_atr(high, low, close, period=int(cfg.atr_period))
    left, right = int(cfg.left_bars), int(cfg.right_bars)
    is_high = local_extrema_mask_vectorized(
        high, left=left, right=right, mode="max", tie_break=cfg.tie_break
    )
    is_low = local_extrema_mask_vectorized(
        low, left=left, right=right, mode="min", tie_break=cfg.tie_break
    )

    # Left prominence: for high, high[c] - min(low[c-left:c]); for low, max(high[c-left:c]) - low[c]
    # Vectorized via rolling on shifted series.
    s_low = pd.Series(low)
    s_high = pd.Series(high)
    left_min_low = s_low.shift(1).rolling(left, min_periods=left).min().to_numpy()
    left_max_high = s_high.shift(1).rolling(left, min_periods=left).max().to_numpy()
    # Right reversal: for high, high[c] - min(low[c+1:c+1+right]); for low, max(high[c+1:c+1+right]) - low[c]
    right_min_low = s_low.iloc[::-1].shift(1).rolling(right, min_periods=right).min().iloc[::-1].to_numpy()
    right_max_high = s_high.iloc[::-1].shift(1).rolling(right, min_periods=right).max().iloc[::-1].to_numpy()

    prom_high = (high - left_min_low) / np.where(atr > 0, atr, np.nan)
    rev_high_atr = (high - right_min_low) / np.where(atr > 0, atr, np.nan)
    rev_high_pct = (high - right_min_low) / np.where(high > 0, high, np.nan)

    prom_low = (left_max_high - low) / np.where(atr > 0, atr, np.nan)
    rev_low_atr = (right_max_high - low) / np.where(atr > 0, atr, np.nan)
    rev_low_pct = (right_max_high - low) / np.where(low > 0, low, np.nan)

    ok_high = (
        is_high
        & np.isfinite(prom_high)
        & np.isfinite(rev_high_atr)
        & (prom_high >= cfg.min_left_prominence_atr)
        & (rev_high_atr >= cfg.min_right_reversal_atr)
        & (rev_high_pct >= cfg.min_reversal_pct)
    )
    ok_low = (
        is_low
        & np.isfinite(prom_low)
        & np.isfinite(rev_low_atr)
        & (prom_low >= cfg.min_left_prominence_atr)
        & (rev_low_atr >= cfg.min_right_reversal_atr)
        & (rev_low_pct >= cfg.min_reversal_pct)
    )

    strength_high = np.nan_to_num(prom_high + rev_high_atr, nan=0.0)
    strength_low = np.nan_to_num(prom_low + rev_low_atr, nan=0.0)
    ok_high = _suppress_neighbors(
        ok_high, strength_high, radius=int(cfg.suppress_neighbor_bars)
    )
    ok_low = _suppress_neighbors(
        ok_low, strength_low, radius=int(cfg.suppress_neighbor_bars)
    )

    confirm_off = int(cfg.confirm_bars)
    rows: list[dict] = []
    for c in np.flatnonzero(ok_high):
        conf = int(c) + confirm_off
        if conf >= n:
            continue
        rows.append(
            {
                "pivot_origin_ts_ms": int(ts[c]),
                "confirmed_at_ts_ms": int(ts[conf]),
                "pivot_side": "high",
                "pivot_price": float(high[c]),
                "pivot_strength": float(strength_high[c]),
                "left_prominence_atr": float(prom_high[c]),
                "right_reversal_atr": float(rev_high_atr[c]),
                "reversal_pct": float(rev_high_pct[c]),
                "ambiguous": 0,
                "label_family": cfg.label_family,
                "label_config_version": cfg.version,
                "pivot_timeframe": cfg.timeframe,
                "origin_bar_index": int(c),
                "confirm_bar_index": conf,
            }
        )
    for c in np.flatnonzero(ok_low):
        conf = int(c) + confirm_off
        if conf >= n:
            continue
        rows.append(
            {
                "pivot_origin_ts_ms": int(ts[c]),
                "confirmed_at_ts_ms": int(ts[conf]),
                "pivot_side": "low",
                "pivot_price": float(low[c]),
                "pivot_strength": float(strength_low[c]),
                "left_prominence_atr": float(prom_low[c]),
                "right_reversal_atr": float(rev_low_atr[c]),
                "reversal_pct": float(rev_low_pct[c]),
                "ambiguous": 0,
                "label_family": cfg.label_family,
                "label_config_version": cfg.version,
                "pivot_timeframe": cfg.timeframe,
                "origin_bar_index": int(c),
                "confirm_bar_index": conf,
            }
        )
    if not rows:
        return pd.DataFrame(
            columns=[
                "pivot_origin_ts_ms",
                "confirmed_at_ts_ms",
                "pivot_side",
                "pivot_price",
                "pivot_strength",
                "left_prominence_atr",
                "right_reversal_atr",
                "reversal_pct",
                "ambiguous",
                "label_family",
                "label_config_version",
                "pivot_timeframe",
                "origin_bar_index",
                "confirm_bar_index",
            ]
        )
    out = pd.DataFrame(rows).sort_values(
        ["pivot_origin_ts_ms", "pivot_side"]
    ).reset_index(drop=True)
    # Knowability: confirmed_at must be strictly after origin for right_window confirmation.
    assert (out["confirmed_at_ts_ms"] >= out["pivot_origin_ts_ms"]).all()
    return out


def first_pivot_target_at_decisions(
    decision_ts_ms: np.ndarray,
    events: pd.DataFrame,
    *,
    horizon_ms: int,
) -> pd.DataFrame:
    """Vectorized label: first pivot origin in (t, t+H] for each decision t."""
    decision_ts_ms = np.asarray(decision_ts_ms, dtype=np.int64)
    n = len(decision_ts_ms)
    if n == 0:
        return pd.DataFrame(
            columns=["decision_ts_ms", "side", "origin_ts_ms", "event_index"]
        )
    if events is None or len(events) == 0:
        return pd.DataFrame(
            {
                "decision_ts_ms": decision_ts_ms,
                "side": np.array(["none"] * n, dtype=object),
                "origin_ts_ms": np.full(n, -1, dtype=np.int64),
                "event_index": np.full(n, -1, dtype=np.int64),
            }
        )
    order = np.argsort(events["pivot_origin_ts_ms"].to_numpy(dtype=np.int64), kind="mergesort")
    e_ts = events["pivot_origin_ts_ms"].to_numpy(dtype=np.int64)[order]
    e_side = events["pivot_side"].to_numpy()[order]
    left = np.searchsorted(e_ts, decision_ts_ms, side="right")
    hi = decision_ts_ms + int(horizon_ms)
    right = np.searchsorted(e_ts, hi, side="right")
    valid = left < right
    first_idx = np.where(valid, left, -1)
    # Bound: origin must be > t (searchsorted right) and <= t+H (left < right)
    sides = np.array(["none"] * n, dtype=object)
    origins = np.full(n, -1, dtype=np.int64)
    if valid.any():
        fi = first_idx[valid]
        sides[valid] = e_side[fi]
        origins[valid] = e_ts[fi]
    return pd.DataFrame(
        {
            "decision_ts_ms": decision_ts_ms,
            "side": sides,
            "origin_ts_ms": origins,
            "event_index": first_idx,
        }
    )


def next_opposite_pivot_at_decisions(
    first_origin_ts_ms: np.ndarray,
    first_side: np.ndarray,
    events: pd.DataFrame,
    *,
    extra_horizon_ms: int,
) -> pd.DataFrame:
    """First opposite-side pivot after the first origin, inside ``extra_horizon_ms``.

    Search window is ``(first_origin, first_origin + extra_horizon]``. Rows with no
    first pivot stay ``none``. Vectorized via ``searchsorted`` on each side book.
    """
    first_origin_ts_ms = np.asarray(first_origin_ts_ms, dtype=np.int64)
    first_side = np.asarray(first_side)
    n = len(first_origin_ts_ms)
    empty = {
        "side": np.array(["none"] * n, dtype=object),
        "origin_ts_ms": np.full(n, -1, dtype=np.int64),
        "pivot_price": np.full(n, np.nan, dtype=float),
    }
    if n == 0 or events is None or len(events) == 0:
        return pd.DataFrame(empty)

    e_ts = events["pivot_origin_ts_ms"].to_numpy(dtype=np.int64)
    e_side = events["pivot_side"].to_numpy()
    e_px = events["pivot_price"].to_numpy(dtype=float)
    order = np.argsort(e_ts, kind="mergesort")
    e_ts, e_side, e_px = e_ts[order], e_side[order], e_px[order]

    hi = e_side == "high"
    lo = e_side == "low"
    hi_ts, hi_px = e_ts[hi], e_px[hi]
    lo_ts, lo_px = e_ts[lo], e_px[lo]

    sides = np.array(["none"] * n, dtype=object)
    origins = np.full(n, -1, dtype=np.int64)
    prices = np.full(n, np.nan, dtype=float)
    extra = int(extra_horizon_ms)

    is_high = (first_side == "high") & (first_origin_ts_ms >= 0)
    is_low = (first_side == "low") & (first_origin_ts_ms >= 0)

    def _fill(mask: np.ndarray, book_ts: np.ndarray, book_px: np.ndarray, out_side: str) -> None:
        if not mask.any() or book_ts.size == 0:
            return
        fo = first_origin_ts_ms[mask]
        left = np.searchsorted(book_ts, fo, side="right")
        right = np.searchsorted(book_ts, fo + extra, side="right")
        valid = left < right
        if not valid.any():
            return
        idx_all = np.flatnonzero(mask)
        take = idx_all[valid]
        li = left[valid]
        sides[take] = out_side
        origins[take] = book_ts[li]
        prices[take] = book_px[li]

    _fill(is_high, lo_ts, lo_px, "low")
    _fill(is_low, hi_ts, hi_px, "high")
    return pd.DataFrame(
        {"side": sides, "origin_ts_ms": origins, "pivot_price": prices}
    )
