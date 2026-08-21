"""Frozen multi-target ladder helpers for tradesim Signals."""

from __future__ import annotations

from dataclasses import replace
from typing import Iterable

from tradesim import Signal
from tradesim.contracts import BreakEvenConfig, TakeProfitLeg


def attach_tp1_be_tp2_hold24(
    signals: Iterable[Signal],
    *,
    tp1_pct: float = 0.01,
    tp2_pct: float = 0.02,
    first_fraction: float = 0.50,
    initial_sl_pct: float = 0.02,
    max_hold_bars: int = 24,
) -> list[Signal]:
    """Attach the frozen TP1/BE/TP2 ladder to already-gated signals.

    The fixed hold starts at entry. It is explicitly *not* a post-TP1 timer reset.
    """
    second_fraction = 1.0 - float(first_fraction)
    if not 0.0 < float(first_fraction) < 1.0:
        raise ValueError("first_fraction must be strictly between 0 and 1")
    if min(float(tp1_pct), float(tp2_pct), float(initial_sl_pct)) <= 0:
        raise ValueError("TP/SL percentages must be positive")
    if int(max_hold_bars) < 1:
        raise ValueError("max_hold_bars must be positive")

    legs = (
        TakeProfitLeg(
            qty_fraction=float(first_fraction),
            price_offset=float(tp1_pct),
            label="tp1",
        ),
        TakeProfitLeg(
            qty_fraction=float(second_fraction),
            price_offset=float(tp2_pct),
            label="tp2",
        ),
    )
    be = BreakEvenConfig(trigger_on_leg=0, stop_offset=0.0)
    out: list[Signal] = []
    for signal in signals:
        meta = dict(signal.meta)
        meta.update(
            {
                "tp_ladder": "tp1_50pct_1pct_be_tp2_50pct_2pct",
                "tp1_pct": float(tp1_pct),
                "tp2_pct": float(tp2_pct),
                "break_even_after_leg": 0,
                "fixed_max_hold_bars_from_entry": int(max_hold_bars),
                "post_tp1_hold_reset_supported": False,
            }
        )
        out.append(
            replace(
                signal,
                stop_offset=float(initial_sl_pct),
                target_offset=None,
                tp_legs=legs,
                break_even=be,
                max_hold_bars=int(max_hold_bars),
                tag=f"{signal.tag}_tp1be_tp2_h{int(max_hold_bars)}",
                meta=meta,
            )
        )
    return out
