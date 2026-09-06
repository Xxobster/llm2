"""Causal Open-High-Low-Close builders for the ML lab leakage guard."""

from __future__ import annotations

import pandas as pd

from llm2.ml_lab.kref import DEFAULT_LOOKBACK, kref_predict
from llm2.ml_lab.mofe_lite import mofe_lite_predict


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    close = ohlcv["close"].to_numpy(dtype=float)
    return pd.DataFrame(
        {
            "kref_pred_h8": kref_predict(close, lookback=DEFAULT_LOOKBACK, horizon=8),
            "mofe_lite_pred": mofe_lite_predict(close, lookback=DEFAULT_LOOKBACK),
        },
        index=ohlcv.index,
    )
