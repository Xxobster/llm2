"""Causal 15-minute sign-reversal control (paper 22 Aug 2026).

signal[t] = -sign(close[t]/close[t-1] - 1)  # known at the close of bar t
confidence[t] = |rolling_hit_rate[t] - 0.5|  # hit rate uses only completed pairs

This is a falsification / market-state baseline, not a strategy to promote.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

DEFAULT_ROLL = 96  # one day of 15-minute bars


def bar_return(close: np.ndarray) -> np.ndarray:
    c = np.asarray(close, dtype=np.float64)
    r = np.full(c.size, np.nan, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        r[1:] = c[1:] / np.where(c[:-1] > 0, c[:-1], np.nan) - 1.0
    return r


def reversal_signal(close: np.ndarray) -> np.ndarray:
    """+1 long / -1 short / 0 flat. Uses return of bar t only."""
    r = bar_return(close)
    s = -np.sign(r)
    s = np.where(np.isfinite(r) & (np.sign(r) != 0), s, 0.0)
    s[0] = 0.0
    return s.astype(np.float64)


def reversal_hit(close: np.ndarray) -> np.ndarray:
    """hit[i] = 1 if the signal issued at i was correct on bar i+1. Known at i+1."""
    r = bar_return(close)
    s = reversal_signal(close)
    nxt = np.sign(np.roll(r, -1))
    nxt[-1] = np.nan
    hit = np.full(r.size, np.nan, dtype=np.float64)
    ok = (s != 0) & np.isfinite(nxt) & (nxt != 0)
    hit[ok] = (s[ok] == nxt[ok]).astype(np.float64)
    hit[-1] = np.nan
    return hit


def reversal_confidence(close: np.ndarray, *, roll: int = DEFAULT_ROLL) -> np.ndarray:
    """|P(reversal) - 0.5| from a causal rolling hit rate.

    At bar t the window is completed hits ``hit[t-roll : t]`` (last value ``hit[t-1]``),
    so the current bar's own next return is never inside the confidence.
    """
    hit = reversal_hit(close)
    known = np.roll(hit, 1)
    known[0] = np.nan
    p = pd.Series(known).rolling(int(roll), min_periods=int(roll)).mean().to_numpy(dtype=np.float64)
    return np.abs(p - 0.5)


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    close = ohlcv["close"].to_numpy(dtype=float)
    return pd.DataFrame(
        {
            "reversal_signal": reversal_signal(close),
            "reversal_confidence": reversal_confidence(close),
        },
        index=ohlcv.index,
    )
