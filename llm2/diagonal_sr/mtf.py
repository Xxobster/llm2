"""Higher-timeframe geometry aligned causally onto a decision timeframe."""

from __future__ import annotations

import pandas as pd
import numpy as np

from llm2.data.indicators import align_multi_timeframe
from llm2.diagonal_sr.geometry import build_geometry_frame

# Columns that are safe to expose as scale-free / slope features after HTF align.
_HTF_COLS = (
    "atr_frac",
    "last2_upper_slope",
    "last2_lower_slope",
    "ols3_upper_slope",
    "ols3_lower_slope",
    "channel_upper_slope",
    "channel_lower_slope",
    "valid3_upper_touches",
    "valid3_lower_touches",
)


def geometry_context_map(decision_tf: str) -> tuple[str, ...]:
    if decision_tf == "15m":
        return ("1h", "4h")
    if decision_tf == "1h":
        return ("4h", "1d")
    if decision_tf == "4h":
        return ("1d",)
    return ()


def dist_atr(close: pd.Series, level: pd.Series, atr: pd.Series) -> pd.Series:
    atr_safe = atr.replace(0, np.nan)
    return (close - level) / atr_safe


def attach_mtf_geometry(
    decision_ohlcv: pd.DataFrame,
    htf_ohlcv_by_tf: dict[str, pd.DataFrame],
    *,
    decision_tf: str,
) -> pd.DataFrame:
    """Build same-TF geometry then append causal HTF distances and slopes.

    ``htf_ohlcv_by_tf`` must contain only completed candles for each higher timeframe.
    Alignment shifts each HTF bar to its completion instant before as-of join.
    """
    base = build_geometry_frame(decision_ohlcv)
    close = decision_ohlcv["close"]
    atr = base["atr"]

    # Same-TF scale-free distances for primary lines.
    for name in (
        "last2_upper",
        "last2_lower",
        "ols3_upper",
        "ols3_lower",
        "channel_upper",
        "channel_lower",
        "valid3_upper",
        "valid3_lower",
        "horiz_resist",
        "horiz_support",
        "donchian20_upper",
        "donchian20_lower",
        "placebo_upper",
        "placebo_lower",
    ):
        if name in base.columns:
            base[f"dist_{name}_atr"] = dist_atr(close, base[name], atr)

    for htf in geometry_context_map(decision_tf):
        htf_ohlcv = htf_ohlcv_by_tf.get(htf)
        if htf_ohlcv is None or htf_ohlcv.empty:
            continue
        g = build_geometry_frame(htf_ohlcv)
        # Distances recomputed on HTF then aligned (price levels not joined raw).
        htf_close = htf_ohlcv["close"]
        htf_atr = g["atr"]
        pack = pd.DataFrame(index=g.index)
        for col in _HTF_COLS:
            if col in g.columns:
                pack[col] = g[col]
        for name in ("last2_upper", "last2_lower", "channel_upper", "channel_lower", "horiz_resist", "horiz_support"):
            if name in g.columns:
                pack[f"dist_{name}_atr"] = dist_atr(htf_close, g[name], htf_atr)
        aligned = align_multi_timeframe(pack, decision_ohlcv.index, htf)
        for col in aligned.columns:
            base[f"htf_{htf}_{col}"] = aligned[col].to_numpy(dtype=float)

    return base
