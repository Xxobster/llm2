"""Block bootstrap for dependence-aware expectancy."""

from __future__ import annotations

import numpy as np


def block_bootstrap_mean(
    returns: np.ndarray,
    *,
    n_samples: int = 1000,
    block_size: int = 20,
    seed: int = 42,
) -> dict[str, float]:
    r = returns[np.isfinite(returns)]
    n = len(r)
    if n == 0:
        return {"positive_frac": float("nan"), "mean": float("nan")}
    rng = np.random.default_rng(seed)
    n_blocks = max(1, n // block_size)
    means = np.empty(n_samples)
    for i in range(n_samples):
        idx_blocks = rng.integers(0, n_blocks, size=n_blocks)
        sample = np.concatenate([r[b * block_size : (b + 1) * block_size] for b in idx_blocks])
        if sample.size == 0:
            sample = r
        means[i] = float(np.mean(sample))
    return {
        "positive_frac": float((means > 0).mean()),
        "mean": float(np.mean(means)),
        "std": float(np.std(means)),
    }
