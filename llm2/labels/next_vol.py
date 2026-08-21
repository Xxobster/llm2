"""Forward realized-volatility labels for the multi-task arm."""

from __future__ import annotations

import pandas as pd

from llm2.labels.volatility import build_volatility_labels


def build_next_vol_labels(ohlcv: pd.DataFrame, *, horizon: int = 24) -> pd.Series:
    """Forward realized range / close over ``horizon`` bars (knowable at T+horizon)."""
    return build_volatility_labels(ohlcv, horizon=horizon)["volatility"].rename("next_vol")
