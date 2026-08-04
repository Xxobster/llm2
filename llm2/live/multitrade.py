"""Multitrade (concurrent-book) helpers for structure live packs.

Distinct from single-book micro-live (max one open book per symbol).
Default (fib multitrade): Book 1–2 base TP/hold; Book 3+: Fibonacci TP + addon hold;
  clarity mean_strength on add-ons only.
K5 double arm: uniform base TP/hold on every book; clarity on all entries;
  qty = 2× min-exchange when signal ≤ size_double_within_bars of last same-side entry.
"""

from __future__ import annotations

from typing import Any

import numpy as np

BASE_TP = 0.01
BASE_SL = 0.02
BASE_HOLD = 6
FIB_EXT_MAX = 1.618
MEAN_LOOKBACK = 168
BAR_MS_1H = 3_600_000


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
    uniform_books: bool = False,
) -> tuple[float, int]:
    """1-based book index → (tp_pct, max_hold_bars)."""
    if uniform_books or int(book_idx) <= 2:
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
            "max_positions_per_side": int(
                cfg.get("max_positions_per_side", strategy.get("max_positions_per_side", 1))
            ),
            "clarity": str(cfg.get("clarity", "none")),
            # addon = historical multitrade; all = research k5 style (primary+addon)
            "clarity_scope": str(cfg.get("clarity_scope", "addon")).strip().lower(),
            "fib_ext": float(cfg.get("fib_ext", 0.0)),
            "hold_addon": int(cfg.get("hold_addon", BASE_HOLD)),
            "base_tp": float(cfg.get("base_tp", strategy.get("tp_pct", BASE_TP))),
            "base_sl": float(cfg.get("base_sl", strategy.get("sl_pct", BASE_SL))),
            "base_hold": int(cfg.get("base_hold", strategy.get("horizon_bars", BASE_HOLD))),
            "mean_lookback": int(cfg.get("mean_lookback", MEAN_LOOKBACK)),
            "version_id": str(cfg.get("version_id") or strategy.get("version_id") or "multitrade"),
            # 0 = no size double; 3 = research double-within-3h
            "size_double_within_bars": int(cfg.get("size_double_within_bars", 0) or 0),
            "size_double_mult": float(cfg.get("size_double_mult", 2.0) or 2.0),
            # True → every book uses base_tp/base_hold (no fib tiering)
            "uniform_books": bool(cfg.get("uniform_books", False)),
            "bar_ms": int(cfg.get("bar_ms", BAR_MS_1H)),
        }
    return None


def decide_entry_gate(
    *,
    side: int,
    pred_mean: float,
    n_open_same_side: int,
    strength_hist: list[float],
    cfg: dict[str, Any],
    bar_ts_ms: int | None = None,
    last_entry_ts_ms: int | None = None,
) -> dict[str, Any]:
    """Apply cap + clarity for multitrade; return allow / book_idx / tp / hold / size_mult."""
    base = {
        "tp_pct": float(cfg["base_tp"]),
        "sl_pct": float(cfg["base_sl"]),
        "max_hold_bars": int(cfg["base_hold"]),
        "size_mult": 1.0,
    }
    if int(side) == 0:
        return {
            "allow": False,
            "skip_reason": "flat_signal",
            "book_idx": 0,
            "append_strength": False,
            **base,
        }
    cap = int(cfg["max_positions_per_side"])
    n_open = int(n_open_same_side)
    is_addon = n_open >= 1
    abs_m = abs(float(pred_mean))
    lookback = int(cfg["mean_lookback"])
    recent = strength_hist[-lookback:] if strength_hist else []
    clarity = str(cfg.get("clarity", "none"))
    scope = str(cfg.get("clarity_scope", "addon"))
    apply_clarity = clarity == "mean_strength" and (
        scope == "all" or (scope == "addon" and is_addon)
    )

    if apply_clarity:
        if not mean_strength_ok(abs_m, recent):
            return {
                "allow": False,
                "skip_reason": "clarity_mean_strength",
                "book_idx": 0,
                "append_strength": True,
                "abs_mean": abs_m,
                **base,
            }
    if n_open >= cap:
        return {
            "allow": False,
            "skip_reason": f"cap_reached:{cap}",
            "book_idx": 0,
            "append_strength": True,
            "abs_mean": abs_m,
            **base,
        }
    book_idx = n_open + 1
    tp, hold = book_tp_hold(
        book_idx,
        fib_ext=float(cfg["fib_ext"]),
        hold_addon=int(cfg["hold_addon"]),
        base_tp=float(cfg["base_tp"]),
        base_hold=int(cfg["base_hold"]),
        uniform_books=bool(cfg.get("uniform_books", False)),
    )
    size_mult = 1.0
    double_bars = int(cfg.get("size_double_within_bars", 0) or 0)
    if (
        double_bars > 0
        and last_entry_ts_ms is not None
        and bar_ts_ms is not None
    ):
        bar_ms = int(cfg.get("bar_ms", BAR_MS_1H))
        gap = int(bar_ts_ms) - int(last_entry_ts_ms)
        if 0 <= gap <= int(double_bars) * bar_ms:
            size_mult = float(cfg.get("size_double_mult", 2.0) or 2.0)
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
        "size_mult": float(size_mult),
    }
