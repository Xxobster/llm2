"""Build supervised first-pivot samples (causal features + multi-head labels)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.paths import FORWARD_LOCKBOX_START, TF_MS
from llm2.pivot.features.packs import build_feature_frame
from llm2.pivot.labels.config import PivotLabelConfig
from llm2.pivot.labels.fractal import (
    first_pivot_target_at_decisions,
    label_fractal_pivots,
    next_opposite_pivot_at_decisions,
)
from llm2.validation.folds import index_to_ms


def _lock_cut(ohlcv: pd.DataFrame) -> pd.DataFrame:
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    return ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()


def _attach_event_fields(
    ydf: pd.DataFrame,
    events: pd.DataFrame,
    *,
    decision_ts_ms: np.ndarray,
    decision_close: np.ndarray,
    tf_ms: int,
) -> pd.DataFrame:
    """Add time_to_event_bars and level_ret_pct vs decision close for first hit."""
    out = ydf.copy()
    n = len(out)
    time_bars = np.full(n, np.nan, dtype=float)
    level_ret = np.full(n, np.nan, dtype=float)
    pivot_price = np.full(n, np.nan, dtype=float)
    if events is None or len(events) == 0:
        out["time_to_event_bars"] = time_bars
        out["level_ret_pct"] = level_ret
        out["pivot_price"] = pivot_price
        return out
    e_ts = events["pivot_origin_ts_ms"].to_numpy(dtype=np.int64)
    e_px = events["pivot_price"].to_numpy(dtype=float)
    price_map = dict(zip(e_ts.tolist(), e_px.tolist()))
    # Vectorized lookup
    ori = out["origin_ts_ms"].to_numpy(dtype=np.int64)
    hit = ori >= 0
    time_bars[hit] = (ori[hit] - decision_ts_ms[hit].astype(np.int64)) / float(tf_ms)
    # prices for hits
    for i in np.flatnonzero(hit):
        px = price_map.get(int(ori[i]), np.nan)
        pivot_price[i] = px
        c = float(decision_close[i])
        if np.isfinite(px) and c > 0:
            level_ret[i] = px / c - 1.0
    out["time_to_event_bars"] = time_bars
    out["level_ret_pct"] = level_ret
    out["pivot_price"] = pivot_price
    return out


def build_samples(
    *,
    symbol: str,
    timeframe: str,
    feature_pack: str,
    label_cfg: PivotLabelConfig,
    horizon_bars: int,
    source: str = "binance",
    max_rows: int | None = None,
) -> dict[str, Any]:
    """Features + multi-head labels (any / side / time / level).

    y_class: 0=none, 1=high, 2=low within horizon bars
    y_any: 1 if any pivot
    y_high_given: only defined on event rows (1 high / 0 low); -1 if none
    y_time_bars: bars until first pivot origin (NaN if none)
    y_level_ret: (pivot_price / decision_close) - 1 (NaN if none)
    y_next_*: first opposite-side pivot after the first origin (NaN / -1 if none)
    """
    ohlcv = _lock_cut(load_ohlcv(symbol, timeframe, source=source))
    if max_rows is not None and len(ohlcv) > max_rows:
        ohlcv = ohlcv.iloc[-max_rows:].copy()
    feats = build_feature_frame(ohlcv, pack=feature_pack)
    events = label_fractal_pivots(ohlcv, label_cfg)
    ts = index_to_ms(ohlcv.index)
    close = ohlcv["close"].to_numpy(dtype=float)
    tf_ms = int(TF_MS[timeframe])
    horizon_ms = int(horizon_bars) * tf_ms
    next_horizon_bars = max(int(horizon_bars) * 2, int(horizon_bars) + 4)
    extra_ms = int(next_horizon_bars) * tf_ms
    ydf = first_pivot_target_at_decisions(ts, events, horizon_ms=horizon_ms)
    ydf = _attach_event_fields(
        ydf, events, decision_ts_ms=ts, decision_close=close, tf_ms=tf_ms
    )
    nxt = next_opposite_pivot_at_decisions(
        ydf["origin_ts_ms"].to_numpy(dtype=np.int64),
        ydf["side"].to_numpy(),
        events,
        extra_horizon_ms=extra_ms,
    )
    y_next_any = (nxt["side"].to_numpy() != "none").astype(np.int64)
    y_next_time = np.full(len(ts), np.nan, dtype=float)
    y_next_level = np.full(len(ts), np.nan, dtype=float)
    hit_n = y_next_any == 1
    if hit_n.any():
        y_next_time[hit_n] = (
            nxt["origin_ts_ms"].to_numpy(dtype=np.int64)[hit_n] - ts[hit_n]
        ) / float(tf_ms)
        px = nxt["pivot_price"].to_numpy(dtype=float)[hit_n]
        c = close[hit_n]
        with np.errstate(divide="ignore", invalid="ignore"):
            y_next_level[hit_n] = np.where(c > 0, px / c - 1.0, np.nan)
    side_map = {"none": 0, "high": 1, "low": 2}
    y = np.array([side_map.get(str(s), 0) for s in ydf["side"]], dtype=np.int64)
    y_any = (y != 0).astype(np.int64)
    y_high_given = np.where(y == 1, 1, np.where(y == 2, 0, -1)).astype(np.int64)
    y_time = ydf["time_to_event_bars"].to_numpy(dtype=float)
    y_level = ydf["level_ret_pct"].to_numpy(dtype=float)
    too_late_next = np.arange(len(ts)) >= (len(ts) - next_horizon_bars)
    y_next_any[too_late_next] = 0
    y_next_time[too_late_next] = np.nan
    y_next_level[too_late_next] = np.nan
    usable = np.arange(len(ts)) < (len(ts) - horizon_bars)
    X = feats.to_numpy(dtype=float)
    finite = np.all(np.isfinite(X), axis=1) & usable
    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "feature_pack": feature_pack,
        "label_config_version": label_cfg.version,
        "horizon_bars": horizon_bars,
        "next_horizon_bars": int(next_horizon_bars),
        "X": X[finite],
        "y": y[finite],
        "y_any": y_any[finite],
        "y_high_given": y_high_given[finite],
        "y_time_bars": y_time[finite],
        "y_level_ret": y_level[finite],
        "y_next_any": y_next_any[finite],
        "y_next_time_bars": y_next_time[finite],
        "y_next_level_ret": y_next_level[finite],
        "ts_ms": ts[finite],
        "feature_names": list(feats.columns),
        "n_events": int(len(events)),
        "class_counts": {
            "none": int((y[finite] == 0).sum()),
            "high": int((y[finite] == 1).sum()),
            "low": int((y[finite] == 2).sum()),
        },
        "frac_any": float(y_any[finite].mean()) if finite.any() else float("nan"),
        "frac_next": float(y_next_any[finite].mean()) if finite.any() else float("nan"),
        "n_rows": int(finite.sum()),
    }
