"""Translate model predictions to tradesim signals."""

from __future__ import annotations

import numpy as np

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, Signal  # noqa: E402

from llm2.audit.cost_hurdle import CostHurdle  # noqa: E402
from llm2.models.base import Prediction  # noqa: E402
from llm2.paths import ROUND_TRIP_COST  # noqa: E402
from llm2.signals.rules import direction_gate, probability_gate  # noqa: E402

DEFAULT_TP = 0.01
DEFAULT_SL = 0.02


def predictions_to_signals(
    ts_ms: np.ndarray,
    pred: Prediction,
    *,
    tp_pct: float = DEFAULT_TP,
    sl_pct: float = DEFAULT_SL,
    vol_scale: np.ndarray | None = None,
    min_edge: float | None = None,
    max_signals: int | None = None,
    target_family: str | None = None,
) -> list[Signal]:
    """Convert predictions to causal Signal list.

    ``min_edge`` defaults to the frozen round-trip cost hurdle so we do not
    trade microscopic predicted edges that cannot survive fees.

    A ``magnitude`` target family must never emit a long/short side — volatility
    forecasts are filter/sizing inputs only (skip-more, never leverage-more).
    """
    n = len(ts_ms)
    edge = ROUND_TRIP_COST if min_edge is None else float(min_edge)

    if target_family == "magnitude":
        raise ValueError(
            "magnitude forecasts cannot be translated into trade sides; "
            "use them as a skip/size filter on a separately justified entry rule"
        )

    if pred.side is not None:
        side_arr = np.asarray(pred.side, dtype=int).copy()
        if pred.mean is not None:
            # require |mean| > edge even if side is set
            side_arr[np.abs(pred.mean) < edge] = 0
    elif pred.proba is not None and pred.proba.ndim == 2:
        p = pred.proba[:, -1] if pred.proba.shape[1] == 2 else pred.proba.max(axis=1)
        hurdle = CostHurdle()
        long_ok = probability_gate(p, hurdle)
        short_ok = probability_gate(1.0 - p, hurdle)
        side_arr = np.where(long_ok == 1, 1, np.where(short_ok == 1, -1, 0))
    elif pred.mean is not None:
        side_arr = direction_gate(pred.mean, threshold=edge)
    else:
        side_arr = np.zeros(n, dtype=int)

    # Optional sparsity: keep strongest |mean| signals only
    if max_signals is not None and pred.mean is not None and np.sum(side_arr != 0) > max_signals:
        strength = np.abs(pred.mean)
        strength = np.where(side_arr != 0, strength, -1.0)
        keep_idx = np.argsort(strength)[-max_signals:]
        mask = np.zeros(n, dtype=bool)
        mask[keep_idx] = True
        side_arr = np.where(mask, side_arr, 0)

    signals: list[Signal] = []
    for i in range(n):
        s = int(side_arr[i])
        if s == 0:
            continue
        tp = tp_pct
        sl = sl_pct
        if vol_scale is not None and np.isfinite(vol_scale[i]) and vol_scale[i] > 0:
            tp = max(tp_pct * float(vol_scale[i]), edge * 2)
            sl = max(sl_pct * float(vol_scale[i]), edge * 2)
        side = Side.LONG if s > 0 else Side.SHORT
        signals.append(
            Signal(
                ts_ms=int(ts_ms[i]),
                side=side,
                stop_offset=sl,
                target_offset=tp,
            )
        )
    return signals
