"""Multitrade (concurrent-book) helpers for structure live packs.

Distinct from single-book micro-live (max one open book per symbol).
Book 1–2: base take-profit / hold. Book 3+: Fibonacci-extended take-profit + longer hold.
Clarity ``mean_strength`` gates add-ons only.
"""

from __future__ import annotations

from typing import Any

import numpy as np

BASE_TP = 0.01
BASE_SL = 0.02
BASE_HOLD = 6
FIB_EXT_MAX = 1.618
MEAN_LOOKBACK = 168


def extended_tp_offset(fib_ext: float, *, base_tp: float = BASE_TP) -> float:
    """Usual take-profit + fib*(usual_TP − entry) as a return fraction of entry."""
    fib = min(max(float(fib_ext), 0.0), FIB_EXT_MAX)
    return float(base_tp * (1.0 + fib))


def book_tp_hold(
    book_idx: int,
    *,
    fib_ext: float,
    hold_addon: int,
    base_tp: float = BASE_TP,
    base_hold: int = BASE_HOLD,
) -> tuple[float, int]:
    """1-based book index → (tp_pct, max_hold_bars)."""
    if int(book_idx) <= 2:
        return float(base_tp), int(base_hold)
    return extended_tp_offset(float(fib_ext), base_tp=base_tp), int(hold_addon)


def mean_strength_ok(abs_mean: float, past_abs: list[float] | np.ndarray) -> bool:
    """Add-on allowed when |mean| ≥ median of prior non-empty strength history."""
    if past_abs is None or len(past_abs) == 0:
        return True
    thr = float(np.median(np.asarray(past_abs, dtype=float)))
    return float(abs_mean) >= thr


def parse_multitrade_config(strategy: dict[str, Any]) -> dict[str, Any] | None:
    """Return multitrade block if pack is concurrent; else None (single-book)."""
    mode = str(strategy.get("execution_mode") or "").strip().lower()
    mt = strategy.get("multitrade")
    if mode in {"multitrade", "concurrent", "hedge_multi"} or isinstance(mt, dict):
        cfg = dict(mt or {})
        return {
            "max_positions_per_side": int(cfg.get("max_positions_per_side", strategy.get("max_positions_per_side", 1))),
            "clarity": str(cfg.get("clarity", "none")),
            "fib_ext": float(cfg.get("fib_ext", 0.0)),
            "hold_addon": int(cfg.get("hold_addon", BASE_HOLD)),
            "base_tp": float(cfg.get("base_tp", strategy.get("tp_pct", BASE_TP))),
            "base_sl": float(cfg.get("base_sl", strategy.get("sl_pct", BASE_SL))),
            "base_hold": int(cfg.get("base_hold", strategy.get("horizon_bars", BASE_HOLD))),
            "mean_lookback": int(cfg.get("mean_lookback", MEAN_LOOKBACK)),
            "version_id": str(cfg.get("version_id") or strategy.get("version_id") or "multitrade"),
        }
    return None


def decide_entry_gate(
    *,
    side: int,
    pred_mean: float,
    n_open_same_side: int,
    strength_hist: list[float],
    cfg: dict[str, Any],
) -> dict[str, Any]:
    """Apply cap + clarity for multitrade; return allow / book_idx / tp / hold / skip_reason."""
    if int(side) == 0:
        return {
            "allow": False,
            "skip_reason": "flat_signal",
            "book_idx": 0,
            "tp_pct": float(cfg["base_tp"]),
            "sl_pct": float(cfg["base_sl"]),
            "max_hold_bars": int(cfg["base_hold"]),
            "append_strength": False,
        }
    cap = int(cfg["max_positions_per_side"])
    n_open = int(n_open_same_side)
    is_addon = n_open >= 1
    abs_m = abs(float(pred_mean))
    lookback = int(cfg["mean_lookback"])
    recent = strength_hist[-lookback:] if strength_hist else []

    if is_addon and str(cfg["clarity"]) == "mean_strength":
        if not mean_strength_ok(abs_m, recent):
            return {
                "allow": False,
                "skip_reason": "clarity_mean_strength",
                "book_idx": 0,
                "tp_pct": float(cfg["base_tp"]),
                "sl_pct": float(cfg["base_sl"]),
                "max_hold_bars": int(cfg["base_hold"]),
                "append_strength": True,
                "abs_mean": abs_m,
            }
    if n_open >= cap:
        return {
            "allow": False,
            "skip_reason": f"cap_reached:{cap}",
            "book_idx": 0,
            "tp_pct": float(cfg["base_tp"]),
            "sl_pct": float(cfg["base_sl"]),
            "max_hold_bars": int(cfg["base_hold"]),
            "append_strength": True,
            "abs_mean": abs_m,
        }
    book_idx = n_open + 1
    tp, hold = book_tp_hold(
        book_idx,
        fib_ext=float(cfg["fib_ext"]),
        hold_addon=int(cfg["hold_addon"]),
        base_tp=float(cfg["base_tp"]),
        base_hold=int(cfg["base_hold"]),
    )
    return {
        "allow": True,
        "skip_reason": None,
        "book_idx": book_idx,
        "tp_pct": float(tp),
        "sl_pct": float(cfg["base_sl"]),
        "max_hold_bars": int(hold),
        "append_strength": True,
        "abs_mean": abs_m,
        "is_addon": is_addon,
    }
