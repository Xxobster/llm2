"""Primary-entry clarity helpers for single-book structure execution grids.

Unlike multitrade (add-on-only mean_strength), these gates the single open book.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, Signal  # noqa: E402

from llm2.live.multitrade import MEAN_LOOKBACK, mean_strength_ok  # noqa: E402

ClarityName = Literal["none", "mean_strength"]
DEFAULT_SL = 0.02


@dataclass(frozen=True)
class SingleBookArm:
    clarity: ClarityName
    horizon_bars: int
    tp_pct: float
    sl_pct: float = DEFAULT_SL

    @property
    def key(self) -> str:
        return f"{self.clarity}|hold{self.horizon_bars}|tp{self.tp_pct:.5f}"


def build_singlebook_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    *,
    arm: SingleBookArm,
    min_edge: float,
    lookback: int = MEAN_LOOKBACK,
    strength_quantile: float = 0.5,
) -> tuple[list[Signal], dict[str, int]]:
    """Emit single-book Signals with optional primary mean_strength gate."""
    strength_hist: list[float] = []
    stats = {
        "n_candidates": 0,
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_edge": 0,
    }
    out: list[Signal] = []
    side_a = np.asarray(side, dtype=int)
    mean_a = np.asarray(mean, dtype=float)
    for i in range(len(ts_ms)):
        s = int(side_a[i])
        m = float(mean_a[i])
        if s == 0:
            continue
        if not np.isfinite(m) or abs(m) < float(min_edge):
            stats["n_skipped_edge"] += 1
            continue
        stats["n_candidates"] += 1
        abs_m = abs(m)
        if arm.clarity == "mean_strength":
            recent = strength_hist[-int(lookback) :] if strength_hist else []
            if not mean_strength_ok(
                abs_m, recent, strength_quantile=float(strength_quantile)
            ):
                stats["n_skipped_clarity"] += 1
                strength_hist.append(abs_m)
                continue
        strength_hist.append(abs_m)
        out.append(
            Signal(
                ts_ms=int(ts_ms[i]),
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(arm.sl_pct),
                target_offset=float(arm.tp_pct),
                max_hold_bars=int(arm.horizon_bars),
                tag=arm.key,
                meta={
                    "pred_mean": float(m),
                    "abs_mean": float(abs_m),
                    "clarity": arm.clarity,
                    "tp_pct": arm.tp_pct,
                    "sl_pct": arm.sl_pct,
                    "horizon_bars": arm.horizon_bars,
                    "strength_quantile": float(strength_quantile),
                },
            )
        )
        stats["n_emitted"] += 1
    return out, stats


def arm_grid(
    *,
    clarity: tuple[ClarityName, ...] = ("none", "mean_strength"),
    holds: tuple[int, ...] = (6, 12),
    tps: tuple[float, ...] = (0.01, 0.015, 0.02618),
    sl_pct: float = DEFAULT_SL,
) -> list[SingleBookArm]:
    from itertools import product

    return [
        SingleBookArm(clarity=c, horizon_bars=h, tp_pct=t, sl_pct=sl_pct)  # type: ignore[arg-type]
        for c, h, t in product(clarity, holds, tps)
    ]
