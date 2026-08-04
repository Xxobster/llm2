"""Forward log-return labels."""

from __future__ import annotations

import numpy as np
import pandas as pd


def build_fwd_return_labels(ohlcv: pd.DataFrame, *, horizon: int = 1) -> pd.DataFrame:
    c = ohlcv["close"].astype(float)
    fwd = np.log(c.shift(-horizon) / c.replace(0, np.nan))
    return pd.DataFrame({"fwd_return": fwd, "horizon": horizon}, index=ohlcv.index)
