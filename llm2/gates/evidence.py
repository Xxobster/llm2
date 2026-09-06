"""Compute the V2.1 evidence fields the hunt previously left UNKNOWN.

Stress = 2× baseline entry slippage via tradesim ``slippage_stress_multiplier``.
Baseline / stress MDD come from mark-to-market equity. Margin utilisation is the peak of
open initial margin over equity. PBO needs a candidate-by-time return matrix; when that
matrix is unavailable the gate is labelled, not silently passed.
"""

from __future__ import annotations

from typing import Any, Sequence

import numpy as np
import pandas as pd


def mdd_fraction_from_equity(equity: np.ndarray) -> float:
    """Peak-to-trough drawdown as a fraction of the prior peak (0..1+)."""
    eq = np.asarray(equity, dtype=float)
    eq = eq[np.isfinite(eq)]
    if eq.size < 2:
        return float("nan")
    peak = np.maximum.accumulate(eq)
    dd = (peak - eq) / np.maximum(peak, 1e-12)
    return float(np.nanmax(dd))


def daily_returns_from_bundle(bundle) -> np.ndarray:
    """Chronological daily mark-to-market wallet returns from a tradesim bundle."""
    result = getattr(bundle, "result", None)
    de = getattr(result, "daily_equity", None) if result is not None else None
    if de is None:
        return np.asarray([], dtype=float)
    if isinstance(de, pd.DataFrame) and "equity" in de.columns:
        eq = de["equity"].to_numpy(dtype=float)
    else:
        eq = np.asarray(de, dtype=float).reshape(-1)
    eq = eq[np.isfinite(eq)]
    if eq.size < 2:
        return np.asarray([], dtype=float)
    return (np.diff(eq) / np.maximum(eq[:-1], 1e-12)).astype(float)


def mdd_fraction_from_daily_returns(returns: np.ndarray) -> float:
    r = np.asarray(returns, dtype=float)
    r = r[np.isfinite(r)]
    if r.size < 2:
        return float("nan")
    equity = np.cumprod(1.0 + r)
    return mdd_fraction_from_equity(equity)


def peak_margin_utilization(
    trades: Sequence[Any],
    *,
    equity: pd.DataFrame | np.ndarray | None,
    starting_equity: float,
) -> float:
    """Peak open-margin / equity while any position is open.

    Uses each trade's ``initial_margin`` and entry/exit timestamps against the equity
    curve when available; otherwise falls back to ``initial_margin / starting_equity``.
    """
    if not trades:
        return 0.0
    start = float(starting_equity) if starting_equity and starting_equity > 0 else 1.0

    eq_times: np.ndarray | None = None
    eq_vals: np.ndarray | None = None
    if equity is not None:
        if isinstance(equity, pd.DataFrame):
            if "ts_ms" in equity.columns and "equity" in equity.columns:
                eq_times = equity["ts_ms"].to_numpy(dtype=np.int64)
                eq_vals = equity["equity"].to_numpy(dtype=float)
            elif "equity" in equity.columns:
                eq_vals = equity["equity"].to_numpy(dtype=float)
        else:
            eq_vals = np.asarray(equity, dtype=float)

    events: list[tuple[int, float]] = []
    for t in trades:
        entry = int(getattr(t, "entry_ts_ms", 0))
        exit_ = int(getattr(t, "exit_ts_ms", entry))
        im = float(getattr(t, "initial_margin", 0.0) or 0.0)
        if im <= 0:
            # qty * entry / leverage fallback
            qty = float(getattr(t, "qty", 0.0) or 0.0)
            px = float(getattr(t, "entry_price", 0.0) or 0.0)
            lev = float(getattr(t, "leverage", 1.0) or 1.0)
            im = abs(qty * px) / max(lev, 1e-9)
        events.append((entry, +im))
        events.append((exit_, -im))
    if not events:
        return 0.0
    events.sort(key=lambda x: (x[0], x[1]))

    open_margin = 0.0
    peak = 0.0
    for ts, delta in events:
        open_margin = max(0.0, open_margin + delta)
        if eq_times is not None and eq_vals is not None and eq_times.size:
            pos = int(np.searchsorted(eq_times, ts, side="right") - 1)
            pos = max(0, min(pos, len(eq_vals) - 1))
            eq = float(eq_vals[pos]) if np.isfinite(eq_vals[pos]) else start
        elif eq_vals is not None and eq_vals.size:
            eq = float(eq_vals[-1]) if np.isfinite(eq_vals[-1]) else start
        else:
            eq = start
        peak = max(peak, open_margin / max(eq, 1e-12))
    return float(peak)


def research_costs_baseline():
    from tradesim import research_costs

    return research_costs()


def research_maker_first_costs():
    """Live product preference: maker on resting entry, take-profit and stop.

    Pair with Post-Only live entry and limit TP/SL. Still run
    ``research_costs_baseline`` (all-taker) as stress. Last-resort market
    flatten (gap, max-hold) is taker and is not this schedule.
    """
    from tradesim import Liquidity, research_limit_entry_costs

    return research_limit_entry_costs(
        take_profit_liquidity=Liquidity.MAKER,
        stop_liquidity=Liquidity.MAKER,
    )


def research_costs_moderate_stress(*, slip_mult: float = 2.0):
    """Moderate stress: 2× baseline directional slippage (Gate C)."""
    from tradesim import research_costs

    base = research_costs()
    return research_costs(
        entry_slippage=float(base.entry_slippage),
        slippage_stress_multiplier=float(slip_mult),
    )


# Buffers that keep liquidation beyond the stop under Mark/maintenance noise.
DEFAULT_MM_BUFFER = 0.005  # maintenance-margin buffer (~0.5%)
DEFAULT_MARK_BUFFER = 0.002  # mark/index dislocation buffer (~0.2%)
DEFAULT_LEVERAGE_HAIRCUT = 0.5  # extra security margin on the SL-implied ceiling


def leverage_from_stop(
    sl_pct: float,
    *,
    mm_buffer: float = DEFAULT_MM_BUFFER,
    mark_buffer: float = DEFAULT_MARK_BUFFER,
    haircut: float = DEFAULT_LEVERAGE_HAIRCUT,
) -> float:
    """Lowest operational leverage from stop-loss with security margin.

    ``floor(1 / (sl_pct + mm_buffer + mark_buffer))`` then ``floor(ceiling * haircut)``.
    Matches research / live (D-001): leverage is survival, not alpha. Min 1.
    """
    sl = float(sl_pct)
    if not np.isfinite(sl) or sl <= 0:
        raise ValueError(f"sl_pct must be positive finite, got {sl_pct!r}")
    denom = sl + float(mm_buffer) + float(mark_buffer)
    if denom <= 0:
        raise ValueError(f"leverage denominator must be positive, got {denom}")
    ceiling = int(np.floor(1.0 / denom))
    lev = max(1.0, float(int(ceiling * float(haircut))))
    return lev


def leverage_ceiling_from_stop(
    sl_pct: float,
    *,
    mm_buffer: float = DEFAULT_MM_BUFFER,
    mark_buffer: float = DEFAULT_MARK_BUFFER,
) -> int:
    """Raw SL-implied ceiling before haircut (for audits / pack stamps)."""
    denom = float(sl_pct) + float(mm_buffer) + float(mark_buffer)
    return int(np.floor(1.0 / denom))


def cap_leverage_by_risk_tiers(
    leverage: float,
    *,
    notional: float,
    tiers: Sequence[dict[str, Any]] | None,
    instrument_max: float | None = None,
) -> float:
    """Cap operational leverage by Bybit risk-tier / instrument max for the notional."""
    lev = float(leverage)
    if instrument_max is not None and np.isfinite(instrument_max) and instrument_max > 0:
        lev = min(lev, float(instrument_max))
    if not tiers:
        return max(1.0, lev)
    applicable = [
        t
        for t in tiers
        if float(t.get("notional_floor", 0.0) or 0.0) <= float(notional)
    ]
    if not applicable:
        return max(1.0, lev)
    tier = max(applicable, key=lambda t: float(t.get("notional_floor", 0.0) or 0.0))
    tier_max = float(tier.get("max_leverage", lev) or lev)
    if np.isfinite(tier_max) and tier_max > 0:
        lev = min(lev, tier_max)
    return max(1.0, lev)


def resolve_operational_leverage(
    sl_pct: float,
    *,
    pack_leverage: float | None = None,
    notional: float | None = None,
    tiers: Sequence[dict[str, Any]] | None = None,
    instrument_max: float | None = None,
    mm_buffer: float = DEFAULT_MM_BUFFER,
    mark_buffer: float = DEFAULT_MARK_BUFFER,
    haircut: float = DEFAULT_LEVERAGE_HAIRCUT,
) -> dict[str, float | int]:
    """Derive live/research leverage from SL; refuse silent pack mismatch."""
    ceiling = leverage_ceiling_from_stop(
        sl_pct, mm_buffer=mm_buffer, mark_buffer=mark_buffer
    )
    derived = leverage_from_stop(
        sl_pct, mm_buffer=mm_buffer, mark_buffer=mark_buffer, haircut=haircut
    )
    capped = cap_leverage_by_risk_tiers(
        derived,
        notional=float(notional or 0.0),
        tiers=tiers,
        instrument_max=instrument_max,
    )
    if pack_leverage is not None and np.isfinite(float(pack_leverage)):
        pack_lev = float(pack_leverage)
        if abs(pack_lev - derived) > 1e-9:
            raise ValueError(
                f"pack leverage {pack_lev} != SL-derived {derived} "
                f"(sl={sl_pct}, ceiling={ceiling}, haircut={haircut})"
            )
    return {
        "sl_pct": float(sl_pct),
        "ceiling": int(ceiling),
        "derived": float(derived),
        "leverage": float(capped),
        "mm_buffer": float(mm_buffer),
        "mark_buffer": float(mark_buffer),
        "haircut": float(haircut),
    }


def pooled_profit_factor(trade_pnls: Sequence[float]) -> float:
    """Pooled gross profit / abs pooled gross loss — never a mean of fold PFs."""
    pnls = np.asarray(list(trade_pnls), dtype=float)
    pnls = pnls[np.isfinite(pnls)]
    gp = float(pnls[pnls > 0].sum())
    gl = float(-pnls[pnls < 0].sum())
    if gl > 0:
        return gp / gl
    if gp > 0:
        return float("inf")
    return 0.0


def build_candidate_return_matrix(
    model_daily: dict[str, list[float]],
) -> pd.DataFrame | None:
    """Build a PBO matrix only from calendar-aligned candidate returns.

    Independently stitched per-model daily lists must not be truncated to a common
    length and treated as parallel time — that manufactures a spurious PBO (often 0).
    """
    if len(model_daily) < 2:
        return None
    lengths = {k: len(v) for k, v in model_daily.items()}
    if len(set(lengths.values())) != 1:
        return None
    n = next(iter(lengths.values()))
    if n < 16:
        return None
    return pd.DataFrame({k: np.asarray(v, dtype=float) for k, v in model_daily.items()})


def build_fold_return_matrix(
    model_fold_pnls: dict[str, list[float]],
) -> pd.DataFrame | None:
    """Candidate-by-fold PnL matrix (honest alignment). Small n → PBO unavailable."""
    if len(model_fold_pnls) < 2:
        return None
    lengths = {k: len(v) for k, v in model_fold_pnls.items()}
    if len(set(lengths.values())) != 1:
        return None
    n = next(iter(lengths.values()))
    if n < 2:
        return None
    return pd.DataFrame({k: np.asarray(v, dtype=float) for k, v in model_fold_pnls.items()})
