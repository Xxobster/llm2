"""Quantile regression targets — same forward return series."""

from __future__ import annotations

import pandas as pd

from llm2.labels.fwd_return import build_fwd_return_labels


def build_quantile_labels(ohlcv: pd.DataFrame, *, horizon: int = 1) -> pd.DataFrame:
    base = build_fwd_return_labels(ohlcv, horizon=horizon)
    return base.rename(columns={"fwd_return": "quantile_target"})
