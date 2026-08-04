"""Direction labels from forward return."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.labels.fwd_return import build_fwd_return_labels


def build_direction_labels(ohlcv: pd.DataFrame, *, horizon: int = 1) -> pd.DataFrame:
    fwd = build_fwd_return_labels(ohlcv, horizon=horizon)["fwd_return"]
    direction = np.sign(fwd).astype(float)
    direction[fwd.abs() < 1e-12] = 0.0
    return pd.DataFrame({"direction": direction, "horizon": horizon}, index=ohlcv.index)
