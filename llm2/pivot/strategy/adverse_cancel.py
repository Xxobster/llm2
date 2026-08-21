"""Adverse-path cancel rules for resting LIMIT intents (execution only)."""

from __future__ import annotations

import numpy as np


def adverse_threshold(
    *,
    atr_frac: float,
    mode: str,
    pct: float = 0.005,
    atr_mult: float = 1.0,
) -> float:
    """Return fractional adverse move from decision close that cancels the rest."""
    if mode == "pct":
        return float(max(pct, 1e-6))
    if mode == "atr":
        a = float(atr_frac) if np.isfinite(atr_frac) else float("nan")
        if not np.isfinite(a) or a <= 0:
            return float(max(pct, 1e-6))
        return float(max(atr_mult * a, 1e-6))
    raise ValueError(f"unknown adverse mode {mode!r}")


def first_touch_or_adverse(
    *,
    side_is_short: bool,
    lim: float,
    i0: int,
    i1: int,
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    decision_close: float,
    adverse_frac: float,
) -> tuple[int, str]:
    """Scan bars [i0, i1). Return (bar_index, reason) with reason touch|adverse|none.

    Adverse: price runs away from the limit (against the fill direction) by
    ``adverse_frac`` of decision close before the limit is touched.
    """
    if not np.isfinite(decision_close) or decision_close <= 0 or adverse_frac <= 0:
        # fall back to touch-only
        if side_is_short:
            for k in range(i0, i1):
                if high[k] >= lim:
                    return k, "touch"
        else:
            for k in range(i0, i1):
                if low[k] <= lim:
                    return k, "touch"
        return -1, "none"

    if side_is_short:
        adv_px = decision_close * (1.0 - adverse_frac)
        for k in range(i0, i1):
            if high[k] >= lim:
                return k, "touch"
            if low[k] <= adv_px or close[k] <= adv_px:
                return k, "adverse"
    else:
        adv_px = decision_close * (1.0 + adverse_frac)
        for k in range(i0, i1):
            if low[k] <= lim:
                return k, "touch"
            if high[k] >= adv_px or close[k] >= adv_px:
                return k, "adverse"
    return -1, "none"
