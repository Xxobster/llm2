"""Training-free Fourier mixture (MoFE-inspired), causal on closed bars.

The published Mixture-of-Financial-Experts model trains Adaptive Fourier Neural
Operators. This module does **not** claim that paper's fit. It implements the
inductive bias only: a global spectral expert and a local short-window expert,
gated by relative energy, with no gradient step.
"""

from __future__ import annotations

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

from llm2.ml_lab.kref import DEFAULT_LOOKBACK, log_returns

LOCAL_BARS = 3
N_LOW_FREQ = 4


def mofe_lite_predict(
    close: np.ndarray,
    *,
    lookback: int = DEFAULT_LOOKBACK,
    n_low: int = N_LOW_FREQ,
    local_bars: int = LOCAL_BARS,
) -> np.ndarray:
    """Mixture of a low-frequency reconstruction and a local mean return."""
    r = log_returns(close)
    L = int(lookback)
    n = int(r.size)
    pred = np.full(n, np.nan, dtype=np.float32)
    if n < L + 2:
        return pred
    win = sliding_window_view(r, L).astype(np.float32)  # (n-L+1, L)
    spec = np.fft.rfft(win, axis=1)
    keep = min(int(n_low), spec.shape[1])
    spec_low = np.zeros_like(spec)
    spec_low[:, :keep] = spec[:, :keep]
    recon = np.fft.irfft(spec_low, n=L, axis=1)
    expert_global = recon[:, -1]
    lb = min(int(local_bars), L)
    expert_local = win[:, -lb:].mean(axis=1)
    e_g = np.sum(np.abs(spec[:, :keep]) ** 2, axis=1)
    e_l = np.sum(win[:, -lb:] ** 2, axis=1)
    stacked = np.stack([e_g, e_l], axis=1)
    stacked = stacked - stacked.max(axis=1, keepdims=True)
    gate = np.exp(stacked)
    gate = gate / np.maximum(gate.sum(axis=1, keepdims=True), 1e-8)
    mix = gate[:, 0] * expert_global + gate[:, 1] * expert_local
    pred[L - 1 :] = mix
    return pred
