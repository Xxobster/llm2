"""Causal perpetual-funding crowding signal.

A settlement at time T is knowable at T, not before. Features on bar i (indexed by
open time T_i) use only prints with timestamp strictly before T_i, so the bar that
opens at a settlement does not see that print.

Trade at most once per new print: the first bar whose open is after the settlement.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.validation.folds import index_to_ms


def align_funding_to_bars(
    bar_open_ms: np.ndarray,
    fund_ts_ms: np.ndarray,
    fund_rate: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Last funding strictly before each bar open, and whether that print is new."""
    opens = np.asarray(bar_open_ms, dtype=np.int64)
    fts = np.asarray(fund_ts_ms, dtype=np.int64)
    fr = np.asarray(fund_rate, dtype=np.float64)
    n = opens.size
    rate = np.full(n, np.nan, dtype=np.float64)
    new = np.zeros(n, dtype=bool)
    if n == 0 or fts.size == 0:
        return rate, new
    idx = np.searchsorted(fts, opens, side="left") - 1
    ok = idx >= 0
    rate[ok] = fr[idx[ok]]
    new[1:] = ok[1:] & (idx[1:] != idx[:-1])
    new[0] = bool(ok[0])
    return rate, new


def attach_causal_funding(ohlcv: pd.DataFrame, funding: pd.Series) -> pd.DataFrame:
    """Add ``funding_rate`` and ``funding_new`` using only prints before bar open."""
    out = ohlcv.copy()
    bar_open = index_to_ms(ohlcv.index)
    f_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    f_rt = funding.to_numpy(dtype=float)
    rate, new = align_funding_to_bars(bar_open, f_ts, f_rt)
    out["funding_rate"] = rate
    out["funding_new"] = new.astype(np.float64)
    return out


def funding_event_mask(
    rate: np.ndarray,
    new: np.ndarray,
    *,
    abs_tau: float,
) -> np.ndarray:
    r = np.asarray(rate, dtype=np.float64)
    n = np.asarray(new, dtype=bool)
    return n & np.isfinite(r) & (np.abs(r) >= float(abs_tau)) & (np.sign(r) != 0)


def funding_signal(rate: np.ndarray, mask: np.ndarray, *, fade: bool) -> np.ndarray:
    """+1 long / -1 short / 0 flat on event bars. Fade shorts positive funding."""
    r = np.asarray(rate, dtype=np.float64)
    m = np.asarray(mask, dtype=bool)
    signed = -np.sign(r) if fade else np.sign(r)
    out = np.zeros(r.size, dtype=np.float64)
    out[m] = signed[m]
    return out


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    close = ohlcv["close"].to_numpy(dtype=float)
    r = np.full(close.size, np.nan, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        r[1:] = close[1:] / np.where(close[:-1] > 0, close[:-1], np.nan) - 1.0
    if "funding_rate" in ohlcv.columns:
        rate = ohlcv["funding_rate"].to_numpy(dtype=float)
    else:
        rate = np.full(close.size, np.nan, dtype=np.float64)
    if "funding_new" in ohlcv.columns:
        new = ohlcv["funding_new"].to_numpy(dtype=float) > 0
    else:
        new = np.zeros(close.size, dtype=bool)
    mask = funding_event_mask(rate, new, abs_tau=0.0)
    return pd.DataFrame(
        {
            "bar_return": r,
            "funding_rate": rate,
            "funding_fade": funding_signal(rate, mask, fade=True),
        },
        index=ohlcv.index,
    )
