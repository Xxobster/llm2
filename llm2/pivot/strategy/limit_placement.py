"""Limit price placement: blend / miss-overshoot compensation (train-fit only)."""

from __future__ import annotations

from typing import Literal

import numpy as np

PlacementMode = Literal[
    "raw",
    "blend_75_1pct",
    "miss_comp",
    "miss_minus_overshoot",
]


def pull_toward_market_lr(level_ret: float, *, is_short: bool, pull: float) -> float:
    """Move limit return toward 0 (closer to decision close) by ``pull`` (≥0)."""
    p = max(0.0, float(pull))
    lr = float(level_ret)
    if is_short:
        # short rests above: pull down → subtract from positive lr
        return lr - p
    return lr + p  # long rests below: pull up


def blend_limit_return(
    level_ret: float,
    *,
    is_short: bool,
    w_adj: float = 0.75,
    pull: float = 0.01,
) -> float:
    """One entry: w_adj * (pred pulled by ``pull``) + (1-w_adj) * pred.

    User idea: 75% weight on a level ~1% closer to market than the raw pivot
    prediction, 25% weight on the raw predicted pivot return.
    """
    w = float(np.clip(w_adj, 0.0, 1.0))
    raw = float(level_ret)
    adj = pull_toward_market_lr(raw, is_short=is_short, pull=pull)
    return w * adj + (1.0 - w) * raw


def limit_price_from_return(close: float, level_ret: float) -> float:
    return float(close) * (1.0 + float(level_ret))


def apply_placement(
    level_ret: float,
    *,
    is_short: bool,
    mode: PlacementMode,
    pull_bps: float = 0.0,
) -> float:
    """Return adjusted level return for resting limit."""
    raw = float(level_ret)
    if mode == "raw":
        return raw
    if mode == "blend_75_1pct":
        return blend_limit_return(raw, is_short=is_short, w_adj=0.75, pull=0.01)
    if mode == "miss_comp":
        return pull_toward_market_lr(raw, is_short=is_short, pull=max(0.0, pull_bps) / 1e4)
    if mode == "miss_minus_overshoot":
        # net = miss - overshoot (in bps); only pull if net>0 (limits too far)
        return pull_toward_market_lr(raw, is_short=is_short, pull=max(0.0, pull_bps) / 1e4)
    raise ValueError(f"unknown placement mode {mode!r}")


def estimate_miss_overshoot_bps(
    *,
    closes: np.ndarray,
    limits: np.ndarray,
    is_short: np.ndarray,
    touched: np.ndarray,
    window_ext: np.ndarray,
) -> tuple[float, float, float]:
    """Train-only diagnostics → (median_miss_bps, median_overshoot_bps, net_pull_bps)."""
    c = np.asarray(closes, dtype=float)
    lim = np.asarray(limits, dtype=float)
    short = np.asarray(is_short, dtype=bool)
    touch = np.asarray(touched, dtype=bool)
    ext = np.asarray(window_ext, dtype=float)
    miss = []
    over = []
    for j in range(len(c)):
        if not (np.isfinite(c[j]) and c[j] > 0 and np.isfinite(lim[j]) and np.isfinite(ext[j])):
            continue
        if short[j]:
            if touch[j]:
                over.append(1e4 * (ext[j] - lim[j]) / c[j])
            else:
                miss.append(1e4 * (lim[j] - ext[j]) / c[j])
        else:
            if touch[j]:
                over.append(1e4 * (lim[j] - ext[j]) / c[j])
            else:
                miss.append(1e4 * (ext[j] - lim[j]) / c[j])
    med_m = float(np.median(miss)) if miss else 0.0
    med_o = float(np.median(over)) if over else 0.0
    # compensate: pull toward market by miss, give back overshoot (don't chase past wick)
    net = max(0.0, med_m - med_o)
    return med_m, med_o, net
