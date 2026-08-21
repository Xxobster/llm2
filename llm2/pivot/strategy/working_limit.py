"""Materialize multi-bar resting limit intents into single-bar tradesim fills.

tradesim only attempts LIMIT entry on the next executable bar. For working-time
tests we stamp a signal on the bar immediately before the first touch so the
engine fills on the touch bar at the resting price.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np
import pandas as pd  # noqa: F401 — kept for type parity with callers

from tradesim import Side, Signal
from tradesim.contracts import EntryOrder

from llm2.pivot.strategy.adverse_cancel import adverse_threshold, first_touch_or_adverse
from llm2.validation.folds import index_to_ms


@dataclass(frozen=True)
class LimitIntent:
    decision_ts_ms: int
    side: Side
    limit_price: float
    stop_offset: float
    target_offset: float
    max_hold_bars: int
    work_bars: int | None = None  # per-intent cancel horizon; None → default
    meta: dict | None = None


def materialize_working_limits(
    ohlcv: pd.DataFrame,
    intents: Sequence[LimitIntent],
    *,
    work_bars: int,
    adverse_mode: str | None = None,
    adverse_pct: float = 0.005,
    adverse_atr_mult: float = 1.0,
    atr_frac: np.ndarray | None = None,
) -> tuple[list[Signal], dict]:
    """Convert intents into fillable LIMIT signals or drop if never touched.

    Returns (signals, stats) where stats counts intents / fills / no_touch /
    adverse cancels. Per-intent ``work_bars`` overrides the default.

    ``adverse_mode``: None (off) | ``pct`` | ``atr`` — cancel rest if price runs
    away from the limit before touch (drops current time-head adaptive cancel).
    """
    bar_ts = index_to_ms(ohlcv.index)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    n_bars = len(bar_ts)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    atr = None if atr_frac is None else np.asarray(atr_frac, dtype=float)

    out: list[Signal] = []
    n_touch = 0
    n_no = 0
    n_bad = 0
    n_adverse = 0
    work_used: list[int] = []
    for it in intents:
        i_dec = pos.get(int(it.decision_ts_ms))
        if i_dec is None:
            n_bad += 1
            continue
        wb = int(it.work_bars) if it.work_bars is not None else int(work_bars)
        if wb <= 0:
            n_no += 1
            continue
        work_used.append(wb)
        i0 = i_dec + 1
        i1 = min(n_bars, i0 + wb)
        lim = float(it.limit_price)
        if lim <= 0 or i0 >= n_bars:
            n_bad += 1
            continue
        if adverse_mode is None:
            touch_i = -1
            reason = "none"
            if it.side == Side.SHORT:
                for k in range(i0, i1):
                    if high[k] >= lim:
                        touch_i = k
                        reason = "touch"
                        break
            else:
                for k in range(i0, i1):
                    if low[k] <= lim:
                        touch_i = k
                        reason = "touch"
                        break
        else:
            a_i = float(atr[i_dec]) if atr is not None and i_dec < len(atr) else float("nan")
            thr = adverse_threshold(
                atr_frac=a_i, mode=str(adverse_mode), pct=adverse_pct, atr_mult=adverse_atr_mult
            )
            touch_i, reason = first_touch_or_adverse(
                side_is_short=it.side == Side.SHORT,
                lim=lim,
                i0=i0,
                i1=i1,
                high=high,
                low=low,
                close=close,
                decision_close=float(close[i_dec]),
                adverse_frac=thr,
            )
        if reason == "adverse":
            n_adverse += 1
            continue
        if touch_i < 0:
            n_no += 1
            continue
        # Signal known at prior bar close so exec bar == touch_i
        if touch_i <= 0:
            n_bad += 1
            continue
        sig_ts = int(bar_ts[touch_i - 1])
        n_touch += 1
        out.append(
            Signal(
                ts_ms=sig_ts,
                side=it.side,
                stop_offset=float(it.stop_offset),
                target_offset=float(it.target_offset),
                max_hold_bars=int(it.max_hold_bars),
                entry_order=EntryOrder.LIMIT,
                limit_price=float(lim),
                tag="pivot_work_limit",
                meta={
                    **(it.meta or {}),
                    "decision_ts_ms": int(it.decision_ts_ms),
                    "touch_bar_offset": int(touch_i - i0),
                    "work_bars": wb,
                    "cancel_reason": reason,
                },
            )
        )
    stats = {
        "n_intent": len(intents),
        "n_filled_path": n_touch,
        "n_no_touch": n_no,
        "n_adverse_cancel": n_adverse,
        "n_bad": n_bad,
        "fill_rate": float(n_touch / len(intents)) if intents else float("nan"),
        "work_bars_default": int(work_bars),
        "work_bars_mean_used": float(np.mean(work_used)) if work_used else float("nan"),
        "adverse_mode": adverse_mode,
        "adverse_pct": float(adverse_pct),
        "adverse_atr_mult": float(adverse_atr_mult),
    }
    return out, stats
