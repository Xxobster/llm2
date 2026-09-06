"""Volatility-scaled bracket arms for the edge lab.

Why
---
Edge lab hunt 001 froze fixed percentage brackets (1.0% / 1.5% / 2.0% take-profit
against a 0.75% / 1.0% stop). Its diagnostics showed entry-bar exit rates of
0.47-0.66 on 1-hour arms: with 1-hour Average True Range near 1%, both the
take-profit and the stop sit **inside a single candle's range**, so most trades
were decided in the bar that filled them. Per the project standard that is a
report-and-stop finding, not something to tune away.

This module scores the same events with a bracket expressed in Average True Range
units at the decision bar, so the stop is placed outside single-bar noise by
construction:

    stop_offset   = clip(k_sl  * atr_frac[t], sl_floor, sl_cap)
    target_offset = clip(tp_ratio * stop_offset, sl_floor, tp_cap)

Leverage uses the **worst-case** (capped) stop, so margin and liquidation
distance are conservative for every trade in the arm and identical between
research and any later live pack.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from llm2.confluence.sim_arms import run_signals_bt
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits
from tradesim import Side, Signal

SL_FLOOR = 0.004
SL_CAP = 0.030
TP_CAP = 0.090
LIMIT_MOVE_MIN = 0.0015
LIMIT_MOVE_MAX = 0.03
MIN_GATED = 15


def atr_brackets(
    atr_frac: np.ndarray,
    *,
    k_sl: float,
    tp_ratio: float,
    sl_floor: float = SL_FLOOR,
    sl_cap: float = SL_CAP,
    tp_cap: float = TP_CAP,
) -> tuple[np.ndarray, np.ndarray]:
    """Per-signal stop and target offsets in return space."""
    base = np.where(np.isfinite(atr_frac), atr_frac, 0.01)
    sl = np.clip(base * float(k_sl), float(sl_floor), float(sl_cap))
    tp = np.clip(sl * float(tp_ratio), float(sl_floor), float(tp_cap))
    return sl.astype(float), tp.astype(float)


def limit_prices(close: np.ndarray, atr_frac: np.ndarray, is_short: np.ndarray) -> np.ndarray:
    move = np.clip(
        np.where(np.isfinite(atr_frac), atr_frac, 0.005), LIMIT_MOVE_MIN, LIMIT_MOVE_MAX
    )
    return np.where(is_short, close * (1.0 + move), close * (1.0 - move))


def run_atr_bracket_arm(
    symbol: str,
    sc,
    mask: np.ndarray,
    is_short: np.ndarray,
    *,
    tag: str,
    market: bool,
    work: int,
    max_hold: int,
    k_sl: float,
    tp_ratio: float,
    sl_cap: float = SL_CAP,
    costs=None,
    return_bundle: bool = False,
) -> dict[str, Any]:
    """Score one event arm with an Average-True-Range-scaled bracket."""
    n_intent = int(mask.sum())
    if n_intent < MIN_GATED:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent, "n_trades": 0}

    idx = np.flatnonzero(mask)
    ts = sc.ts_ms[idx]
    atr = sc.atr_frac[idx]
    close = sc.close[idx]
    short = np.asarray(is_short, dtype=bool).reshape(-1)
    if short.size != idx.size:
        raise ValueError(f"is_short length {short.size} != gated {idx.size}")

    sl_arr, tp_arr = atr_brackets(atr, k_sl=k_sl, tp_ratio=tp_ratio, sl_cap=sl_cap)

    if market:
        signals = [
            Signal(
                ts_ms=int(ts[j]),
                side=Side.SHORT if short[j] else Side.LONG,
                stop_offset=float(sl_arr[j]),
                target_offset=float(tp_arr[j]),
                max_hold_bars=int(max_hold),
                tag=tag,
            )
            for j in range(idx.size)
        ]
        fill_pct = 1.0
    else:
        lim = limit_prices(close, atr, short)
        intents = [
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=float(sl_arr[j]),
                target_offset=float(tp_arr[j]),
                max_hold_bars=int(max_hold),
                work_bars=int(work),
            )
            for j in range(idx.size)
        ]
        signals, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=int(work))
        fill_pct = float(fill["fill_rate"])

    out = run_signals_bt(
        symbol,
        sc.timeframe,
        sc.ohlcv,
        signals,
        tag=tag,
        max_hold=int(max_hold),
        # Worst-case stop drives leverage: conservative margin for every trade.
        sl=float(sl_cap),
        market=bool(market),
        n_intent=n_intent,
        fill_pct=fill_pct,
        costs=costs,
        return_bundle=return_bundle,
    )
    out["bracket_mode"] = "atr_scaled"
    out["k_sl"] = float(k_sl)
    out["tp_ratio"] = float(tp_ratio)
    out["sl_cap"] = float(sl_cap)
    out["sl_pct_mean"] = float(np.nanmean(sl_arr))
    out["sl_pct_p05"] = float(np.nanpercentile(sl_arr, 5))
    out["sl_pct_p95"] = float(np.nanpercentile(sl_arr, 95))
    out["tp_pct_mean"] = float(np.nanmean(tp_arr))
    return out


def run_offset_bracket_arm(
    symbol: str,
    sc,
    mask: np.ndarray,
    is_short: np.ndarray,
    sl_arr: np.ndarray,
    tp_arr: np.ndarray,
    *,
    tag: str,
    market: bool,
    work: int,
    max_hold: int,
    sl_cap: float = SL_CAP,
) -> dict[str, Any]:
    """Score one arm with per-bar frozen stop/target offsets (adaptive channel)."""
    n_intent = int(mask.sum())
    if n_intent < MIN_GATED:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n_intent, "n_trades": 0}

    idx = np.flatnonzero(mask)
    ts = sc.ts_ms[idx]
    close = sc.close[idx]
    short = np.asarray(is_short, dtype=bool).reshape(-1)
    sl_use = np.asarray(sl_arr, dtype=float).reshape(-1)
    tp_use = np.asarray(tp_arr, dtype=float).reshape(-1)
    if short.size != idx.size or sl_use.size != idx.size or tp_use.size != idx.size:
        raise ValueError("offset arrays must match gated length")

    if market:
        signals = [
            Signal(
                ts_ms=int(ts[j]),
                side=Side.SHORT if short[j] else Side.LONG,
                stop_offset=float(sl_use[j]),
                target_offset=float(tp_use[j]),
                max_hold_bars=int(max_hold),
                tag=tag,
            )
            for j in range(idx.size)
        ]
        fill_pct = 1.0
    else:
        atr = sc.atr_frac[idx]
        lim = limit_prices(close, atr, short)
        intents = [
            LimitIntent(
                decision_ts_ms=int(ts[j]),
                side=Side.SHORT if short[j] else Side.LONG,
                limit_price=float(lim[j]),
                stop_offset=float(sl_use[j]),
                target_offset=float(tp_use[j]),
                max_hold_bars=int(max_hold),
                work_bars=int(work),
            )
            for j in range(idx.size)
        ]
        signals, fill = materialize_working_limits(sc.ohlcv, intents, work_bars=int(work))
        fill_pct = float(fill["fill_rate"])

    out = run_signals_bt(
        symbol,
        sc.timeframe,
        sc.ohlcv,
        signals,
        tag=tag,
        max_hold=int(max_hold),
        sl=float(sl_cap),
        market=bool(market),
        n_intent=n_intent,
        fill_pct=fill_pct,
    )
    out["bracket_mode"] = "frozen_offset"
    out["sl_cap"] = float(sl_cap)
    out["sl_pct_mean"] = float(np.nanmean(sl_use))
    out["tp_pct_mean"] = float(np.nanmean(tp_use))
    return out

