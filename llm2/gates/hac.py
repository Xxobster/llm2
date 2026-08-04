"""HAC Newey-West Sharpe adjustment."""

from __future__ import annotations

import numpy as np


def newey_west_sharpe(returns: np.ndarray, *, lags: int | None = None) -> float:
    r = returns[np.isfinite(returns)]
    n = len(r)
    if n < 3:
        return float("nan")
    mu = float(np.mean(r))
    if mu == 0 and np.std(r) == 0:
        return 0.0
    lags = lags or int(np.floor(4 * (n / 100) ** (2 / 9)))
    lags = max(1, min(lags, n - 2))
    demeaned = r - mu
    gamma0 = float(np.dot(demeaned, demeaned) / n)
    var_nw = gamma0
    for lag in range(1, lags + 1):
        w = 1.0 - lag / (lags + 1)
        cov = float(np.dot(demeaned[lag:], demeaned[:-lag]) / n)
        var_nw += 2 * w * cov
    if var_nw <= 0:
        return float("nan")
    return float(mu / np.sqrt(var_nw) * np.sqrt(252))
