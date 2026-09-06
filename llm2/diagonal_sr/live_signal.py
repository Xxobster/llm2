"""One shared tip-signal function for diagonal S/R rule-event arms.

Research (``scripts/run_diagonal_sr_nested_settle_001.py``) and live
(``llm2.live.diagonal_sr_runner``) must resolve a bar through this module so a
live decide cannot drift from the settled occurrence bits.

No model, no calibrator: the arm is the causal occurrence bit plus a fixed
bracket. Missing geometry is refused, never filled.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from llm2.diagonal_sr.bar_series import _atr_frac
from llm2.diagonal_sr.events import (
    LONG_EVENTS,
    MARKET_ENTRY_EVENTS,
    SHORT_EVENTS,
    build_known_now_features,
    occurrence_bits,
)

# Same clip as llm2.confluence.sim_arms / settle _limit_atr.
LIMIT_MOVE_MIN = 0.0015
LIMIT_MOVE_MAX = 0.03
LIMIT_MOVE_FALLBACK = 0.005

# Geometry columns each event needs finite at the decision bar.
EVENT_REQUIRED_GEOMETRY: dict[str, tuple[str, ...]] = {
    "bounce_upper": ("_upper", "_atr"),
    "bounce_lower": ("_lower", "_atr"),
    "break_upper": ("_upper", "_atr"),
    "break_lower": ("_lower", "_atr"),
    "retest_after_break_up": ("_upper", "_atr"),
    "retest_after_break_down": ("_lower", "_atr"),
    "channel_walk_long": ("_lower", "_ch_u", "_ch_l", "_atr"),
    "channel_walk_short": ("_upper", "_ch_u", "_ch_l", "_atr"),
    "confluence_bounce_long": ("_lower", "_atr"),
    "confluence_bounce_short": ("_upper", "_atr"),
    "confluence_break_up": ("_upper", "_atr"),
    "confluence_break_down": ("_lower", "_atr"),
}


@dataclass(frozen=True)
class TipSignal:
    fires: bool
    event: str
    side: str
    is_short: bool
    market_entry: bool
    bar_ts_ms: int
    close: float
    atr_frac: float
    limit_px: float
    n_prefix_bars: int
    nan_cols: tuple[str, ...] = ()
    geometry: dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return len(self.nan_cols) == 0


def event_side(event: str) -> int:
    if event in LONG_EVENTS:
        return 1
    if event in SHORT_EVENTS:
        return -1
    raise ValueError(f"event {event!r} has no frozen side")


def limit_price(close: float, atr_frac: float, *, is_short: bool) -> float:
    """Working-LIMIT price used by the settle arms (ATR-offset from the close)."""
    move = float(atr_frac) if np.isfinite(atr_frac) else LIMIT_MOVE_FALLBACK
    move = float(np.clip(move, LIMIT_MOVE_MIN, LIMIT_MOVE_MAX))
    return float(close * (1.0 + move)) if is_short else float(close * (1.0 - move))


def occurrence_series(
    ohlcv: pd.DataFrame,
    *,
    event: str,
    generation: str = "A",
) -> tuple[pd.Series, pd.DataFrame]:
    """Causal occurrence bit for ``event`` plus the raw geometry carrier frame."""
    gen = str(generation).upper()
    feat = build_known_now_features(ohlcv, generation=gen)
    occ = occurrence_bits(feat, generation=gen)
    if event not in occ.columns:
        raise ValueError(f"event {event!r} not produced by generation {gen}")
    return occ[event], feat


def tip_signal(
    ohlcv: pd.DataFrame,
    *,
    event: str,
    generation: str = "A",
) -> TipSignal:
    """Resolve the last (closed) bar of ``ohlcv`` for one diagonal S/R arm."""
    if ohlcv is None or len(ohlcv) < 60:
        raise ValueError(f"need >=60 closed bars for diagonal geometry, got {0 if ohlcv is None else len(ohlcv)}")
    occ, feat = occurrence_series(ohlcv, event=event, generation=generation)
    side_i = event_side(event)
    is_short = side_i < 0
    tip = feat.iloc[-1]

    nan_cols: list[str] = []
    for col in EVENT_REQUIRED_GEOMETRY.get(event, ("_atr",)):
        val = float(tip[col]) if col in feat.columns else float("nan")
        if not np.isfinite(val):
            nan_cols.append(col)

    close = float(ohlcv["close"].iloc[-1])
    atr_f = float(_atr_frac(ohlcv)[-1])
    if not np.isfinite(atr_f):
        nan_cols.append("atr_frac")
    bar_ts_ms = int(
        pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True)).as_unit("ns").asi8[-1] // 1_000_000
    )
    fires = bool(float(occ.iloc[-1]) >= 0.5) and not nan_cols

    return TipSignal(
        fires=fires,
        event=str(event),
        side="Sell" if is_short else "Buy",
        is_short=bool(is_short),
        market_entry=event in MARKET_ENTRY_EVENTS,
        bar_ts_ms=bar_ts_ms,
        close=close,
        atr_frac=atr_f,
        limit_px=limit_price(close, atr_f, is_short=is_short),
        n_prefix_bars=int(len(ohlcv)),
        nan_cols=tuple(nan_cols),
        geometry={
            "upper": float(tip["_upper"]) if "_upper" in feat.columns else None,
            "lower": float(tip["_lower"]) if "_lower" in feat.columns else None,
            "channel_upper": float(tip["_ch_u"]) if "_ch_u" in feat.columns else None,
            "channel_lower": float(tip["_ch_l"]) if "_ch_l" in feat.columns else None,
            "atr": float(tip["_atr"]) if "_atr" in feat.columns else None,
        },
    )
