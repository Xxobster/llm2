"""Null surrogate generators for predictability tests."""

from __future__ import annotations

import numpy as np


def row_shuffle(y: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    out = y.copy()
    finite = np.isfinite(out)
    vals = out[finite]
    rng.shuffle(vals)
    out[finite] = vals
    return out


def block_shuffle(y: np.ndarray, rng: np.random.Generator, *, block_size: int = 24) -> np.ndarray:
    n = len(y)
    if n == 0:
        return y.copy()
    n_blocks = max(1, n // block_size)
    blocks = [y[i * block_size : (i + 1) * block_size].copy() for i in range(n_blocks)]
    if n_blocks * block_size < n:
        blocks.append(y[n_blocks * block_size :].copy())
    order = rng.permutation(len(blocks))
    return np.concatenate([blocks[i] for i in order])


def fourier_phase_randomize(y: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    x = np.nan_to_num(y.astype(float), nan=0.0)
    spec = np.fft.rfft(x)
    phases = rng.uniform(0, 2 * np.pi, size=spec.shape)
    mag = np.abs(spec)
    randomized = mag * np.exp(1j * phases)
    out = np.fft.irfft(randomized, n=len(x))
    out[~np.isfinite(y)] = np.nan
    return out


def circular_shift(y: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    n = len(y)
    if n == 0:
        return y.copy()
    k = int(rng.integers(1, n))
    return np.roll(y, k)


def cross_series_timing_destroy(panel: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Destroy cross-series timing while preserving each series' marginal distribution.

    ``panel`` shape: (n_timesteps, n_series). Each column is circularly shifted
    by an independent random lag.
    """
    out = np.asarray(panel, dtype=float).copy()
    if out.ndim == 1:
        return circular_shift(out, rng)
    n, k = out.shape
    if n == 0:
        return out
    lags = rng.integers(0, n, size=k)
    # vectorized: for each column apply roll — use advanced indexing
    idx = (np.arange(n)[:, None] - lags[None, :]) % n
    return np.take_along_axis(out, idx, axis=0)


SURROGATES = {
    "row_shuffle": row_shuffle,
    "block_shuffle": block_shuffle,
    "fourier_phase": fourier_phase_randomize,
    "circular_shift": circular_shift,
}


def list_surrogates() -> list[str]:
    return sorted(SURROGATES.keys())


def apply_surrogate(y: np.ndarray, name: str, *, rng: np.random.Generator) -> np.ndarray:
    fn = SURROGATES.get(name)
    if fn is None:
        raise KeyError(name)
    return fn(y, rng)
