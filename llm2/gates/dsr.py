"""Deflated Sharpe Ratio (Bailey & Lopez de Prado)."""

from __future__ import annotations

import math

import numpy as np
from scipy import stats

EULER = 0.5772156649015329


def expected_max_sharpe(var_sr: float, n_trials: int) -> float:
    if n_trials < 2 or var_sr <= 0:
        return 0.0
    sd = math.sqrt(var_sr)
    a = stats.norm.ppf(1.0 - 1.0 / n_trials)
    b = stats.norm.ppf(1.0 - 1.0 / (n_trials * math.e))
    return sd * ((1.0 - EULER) * a + EULER * b)


def deflated_sharpe_ratio(
    returns: np.ndarray,
    sr_obs: float,
    *,
    n_trials: int = 1,
    sr_variance: float | None = None,
) -> float:
    r = returns[np.isfinite(returns)]
    t = len(r)
    if t < 3:
        return float("nan")
    skew = float(stats.skew(r))
    kurt = float(stats.kurtosis(r, fisher=False))
    denom = 1.0 - skew * sr_obs + ((kurt - 1.0) / 4.0) * sr_obs**2
    if denom <= 0:
        return float("nan")
    var_sr = sr_variance if sr_variance is not None else max(float(np.var(r)), 1e-12)
    sr0 = expected_max_sharpe(var_sr, n_trials)
    z = (sr_obs - sr0) * math.sqrt(t - 1) / math.sqrt(denom)
    return float(stats.norm.cdf(z))
