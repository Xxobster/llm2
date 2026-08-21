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


def strength_scale_factor(
    abs_mean: float,
    *,
    ref: float = 0.5,
    factor_min: float = 1.0,
    factor_max: float = 2.0,
) -> float:
    """Clip ``|pred_mean|/ref`` into ``[factor_min, factor_max]``.

    Shared kernel for take-profit and size proportional strength scaling.
    """
    r = float(ref)
    if r <= 0.0:
        raise ValueError(f"strength scale ref must be > 0, got {r}")
    fmin = float(factor_min)
    fmax = float(factor_max)
    if fmin <= 0.0 or fmax < fmin:
        raise ValueError(f"invalid strength scale bounds min={fmin} max={fmax}")
    factor = float(abs_mean) / r
    return float(min(fmax, max(fmin, factor)))


def scale_tp_by_abs_mean(
    base_tp: float,
    abs_mean: float,
    *,
    ref: float = 0.5,
    factor_min: float = 1.0,
    factor_max: float = 2.0,
) -> float:
    """Proportional take-profit: ``base_tp * clip(|mean|/ref, factor_min, factor_max)``.

    Frozen nested formula (research): TP = 1% × min(2, max(1, |pred_mean|/0.5)).
    Stronger |pred_mean| → higher TP factor; never below base, never above 2× base.
    """
    return float(base_tp) * strength_scale_factor(
        abs_mean, ref=ref, factor_min=factor_min, factor_max=factor_max
    )


def scale_size_mult_by_abs_mean(
    abs_mean: float,
    *,
    ref: float = 0.5,
    factor_min: float = 1.0,
    factor_max: float = 2.0,
) -> float:
    """Proportional size multiplier: ``clip(|mean|/ref, factor_min, factor_max)``.

    Research diagnostic formula (same clip as TP scaling without base TP):
    size_mult = min(2, max(1, |pred_mean|/0.5)). Stronger signal → larger qty.
    Engine applies via Signal.meta['size_mult'] on MIN_EXCHANGE or equity sizing.
    """
    return strength_scale_factor(
        abs_mean, ref=ref, factor_min=factor_min, factor_max=factor_max
    )


def mean_strength_ok(
    abs_mean: float,
    past_abs: list[float] | np.ndarray,
    *,
    strength_quantile: float = 0.5,
) -> bool:
    """Allow when |mean| ≥ quantile of prior non-empty strength history.

    Default ``strength_quantile=0.5`` is the historical median gate used by live packs.
    Empty history always passes (first observations seed the histogram).
    """
    if past_abs is None or len(past_abs) == 0:
        return True
    q = float(strength_quantile)
    if not (0.0 < q <= 1.0):
        raise ValueError(f"strength_quantile must be in (0, 1], got {q}")
    arr = np.asarray(past_abs, dtype=float)
    thr = float(np.quantile(arr, q))
    return float(abs_mean) >= thr


def slot_release_ts_ms(
    entry_bar_ts_ms: int,
    side: int,
    *,
    tp_pct: float,
    sl_pct: float,
    max_hold_bars: int,
    bar_ts_ms: np.ndarray,
    bar_open: np.ndarray,
    bar_high: np.ndarray,
    bar_low: np.ndarray,
    tf_ms: int,
) -> int:
    """When a concurrent book stops occupying a slot.

    Live frees the slot as soon as the exchange reports the take-profit or stop
    filled (observed by the next decision-bar reconcile). A research pre-pass that
    keeps the slot until max-hold instead will skip entries live actually took, so
    both sides must use this one rule. Adverse-first inside a bar; this only decides
    occupancy, never profit and loss.
    """
    i = int(np.searchsorted(bar_ts_ms, int(entry_bar_ts_ms), side="right"))
    hold_deadline = int(entry_bar_ts_ms) + int(max_hold_bars) * int(tf_ms)
    if i >= len(bar_ts_ms):
        return hold_deadline
    entry_px = float(bar_open[i])
    if not np.isfinite(entry_px) or entry_px <= 0:
        return hold_deadline
    s = 1 if int(side) > 0 else -1
    tp_px = entry_px * (1.0 + s * float(tp_pct))
    sl_px = entry_px * (1.0 - s * float(sl_pct))
    last = min(len(bar_ts_ms) - 1, i + int(max_hold_bars) - 1)
    for j in range(i, last + 1):
        hit_sl = bar_low[j] <= sl_px if s > 0 else bar_high[j] >= sl_px
        hit_tp = bar_high[j] >= tp_px if s > 0 else bar_low[j] <= tp_px
        if hit_sl or hit_tp:
            return min(hold_deadline, int(bar_ts_ms[j]) + int(tf_ms))
    return hold_deadline


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
            # 0.5 = median (legacy); 0.75 = p75 expectancy arm
            "strength_quantile": float(cfg.get("strength_quantile", 0.5) or 0.5),
            # Variable TP: stronger |pred_mean| → higher TP (capped). Off by default.
            "tp_scale_by_abs_mean": bool(cfg.get("tp_scale_by_abs_mean", False)),
            "tp_scale_ref": float(cfg.get("tp_scale_ref", 0.5) or 0.5),
            "tp_scale_factor_min": float(cfg.get("tp_scale_factor_min", 1.0) or 1.0),
            "tp_scale_factor_max": float(cfg.get("tp_scale_factor_max", 2.0) or 2.0),
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
    strength_q = float(cfg.get("strength_quantile", 0.5) or 0.5)
    apply_clarity = clarity == "mean_strength" and (
        scope == "all" or (scope == "addon" and is_addon)
    )

    if apply_clarity:
        if not mean_strength_ok(abs_m, recent, strength_quantile=strength_q):
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
    if bool(cfg.get("tp_scale_by_abs_mean", False)):
        tp = scale_tp_by_abs_mean(
            float(tp),
            abs_m,
            ref=float(cfg.get("tp_scale_ref", 0.5) or 0.5),
            factor_min=float(cfg.get("tp_scale_factor_min", 1.0) or 1.0),
            factor_max=float(cfg.get("tp_scale_factor_max", 2.0) or 2.0),
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
