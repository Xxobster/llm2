"""Block bootstrap for dependence-aware expectancy."""

from __future__ import annotations

import numpy as np

# Frozen Default Gates V2.1: at least 10,000 resamples. Block length was the
# library default before any nested-settle 004 outer numbers were viewed.
DEFAULT_N_SAMPLES = 10_000
DEFAULT_BLOCK_SIZE = 20
DEFAULT_SEED = 42


def block_bootstrap_mean(
    returns: np.ndarray,
    *,
    n_samples: int = DEFAULT_N_SAMPLES,
    block_size: int = DEFAULT_BLOCK_SIZE,
    seed: int = DEFAULT_SEED,
) -> dict[str, float]:
    r = np.asarray(returns, dtype=float)
    r = r[np.isfinite(r)]
    n = int(r.size)
    n_samples = int(n_samples)
    if n == 0 or n_samples <= 0:
        return {"positive_frac": float("nan"), "mean": float("nan"), "std": float("nan")}
    rng = np.random.default_rng(int(seed))
    bs = max(1, int(block_size))
    n_blocks = max(1, n // bs)
    if n < bs:
        means = np.full(n_samples, float(np.mean(r)))
    else:
        blocks = r[: n_blocks * bs].reshape(n_blocks, bs)
        idx = rng.integers(0, n_blocks, size=(n_samples, n_blocks))
        means = blocks[idx].reshape(n_samples, -1).mean(axis=1)
    return {
        "positive_frac": float((means > 0).mean()),
        "mean": float(np.mean(means)),
        "std": float(np.std(means, ddof=0)),
    }
