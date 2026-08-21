"""Guards for the three live-vs-backtest signal parity defects found on 2026-08-06.

1. DATA-CANDLE-001  ``last`` / ``last_price`` are disjoint slices of one series;
   pinning one label silently deleted 49,807 ETHUSDT 1h bars.
2. GATE-SLOT-001    a concurrent book must release its slot when the take-profit or
   stop fills, as live does, not at max-hold as the research pre-pass did.
3. GATE-CLARITY-001 the clarity quantile must come from a candle-derived history, not
   from whatever bars the process happened to observe since its last restart.
"""

from __future__ import annotations

import numpy as np
import pytest

from llm2.data.loader import load_ohlcv
from llm2.live.multitrade import decide_entry_gate, slot_release_ts_ms
from llm2.paths import TF_MS

HOUR = TF_MS["1h"]


# --------------------------------------------------------------------------------------
# DATA-CANDLE-001
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("symbol", ["ETHUSDT", "BTCUSDT", "SOLUSDT"])
def test_research_1h_series_has_no_holes(symbol: str):
    """A pinned price_type label must never hide part of the history."""
    try:
        df = load_ohlcv(symbol, "1h")
    except (FileNotFoundError, ValueError) as exc:
        pytest.skip(f"warehouse unavailable: {exc}")
    ts = df["ts_ms"].to_numpy(dtype=np.int64)
    missing = int(((np.diff(ts) - HOUR) // HOUR).clip(0).sum())
    assert missing == 0, (
        f"{symbol} 1h research series has {missing} missing bars — the loader is "
        "pinning one price_type label instead of the whole last-trade series"
    )


# --------------------------------------------------------------------------------------
# GATE-SLOT-001
# --------------------------------------------------------------------------------------


def _bars(n: int, *, high: float, low: float, open_: float = 100.0):
    ts = np.arange(n, dtype=np.int64) * HOUR
    return {
        "ts_ms": ts,
        "open": np.full(n, open_),
        "high": np.full(n, high),
        "low": np.full(n, low),
    }


def test_slot_is_released_when_target_is_touched():
    b = _bars(10, high=102.0, low=99.9)  # +2% high clears a 1% take-profit
    release = slot_release_ts_ms(
        0,
        1,
        tp_pct=0.01,
        sl_pct=0.02,
        max_hold_bars=6,
        bar_ts_ms=b["ts_ms"],
        bar_open=b["open"],
        bar_high=b["high"],
        bar_low=b["low"],
        tf_ms=HOUR,
    )
    assert release < 0 + 6 * HOUR, "target touch must free the slot before max-hold"


def test_slot_is_held_to_max_hold_when_nothing_is_touched():
    b = _bars(10, high=100.2, low=99.8)  # neither 1% nor 2% is reached
    release = slot_release_ts_ms(
        0,
        1,
        tp_pct=0.01,
        sl_pct=0.02,
        max_hold_bars=6,
        bar_ts_ms=b["ts_ms"],
        bar_open=b["open"],
        bar_high=b["high"],
        bar_low=b["low"],
        tf_ms=HOUR,
    )
    assert release == 6 * HOUR


def test_slot_release_never_exceeds_max_hold():
    b = _bars(30, high=100.1, low=99.9)
    release = slot_release_ts_ms(
        0,
        -1,
        tp_pct=0.01,
        sl_pct=0.02,
        max_hold_bars=4,
        bar_ts_ms=b["ts_ms"],
        bar_open=b["open"],
        bar_high=b["high"],
        bar_low=b["low"],
        tf_ms=HOUR,
    )
    assert release <= 4 * HOUR


# --------------------------------------------------------------------------------------
# GATE-CLARITY-001
# --------------------------------------------------------------------------------------


def _cfg(**over):
    base = {
        "max_positions_per_side": 5,
        "clarity": "mean_strength",
        "clarity_scope": "all",
        "fib_ext": 0.0,
        "hold_addon": 12,
        "base_tp": 0.01,
        "base_sl": 0.02,
        "base_hold": 12,
        "mean_lookback": 168,
        "strength_quantile": 0.5,
        "uniform_books": True,
        "bar_ms": HOUR,
        "size_double_within_bars": 0,
        "size_double_mult": 2.0,
    }
    base.update(over)
    return base


def test_clarity_gate_depends_on_the_seeded_history():
    """A cold history passes everything; a warm one applies the real quantile.

    This is the whole reason live and research disagreed on clarity skips: the bot
    restarted with an empty histogram and waved through signals the backtest gated.
    """
    weak = 0.12
    cold = decide_entry_gate(
        side=1,
        pred_mean=weak,
        n_open_same_side=0,
        strength_hist=[],
        cfg=_cfg(),
    )
    warm = decide_entry_gate(
        side=1,
        pred_mean=weak,
        n_open_same_side=0,
        strength_hist=[0.4, 0.5, 0.6, 0.7],
        cfg=_cfg(),
    )
    assert cold["allow"] is True
    assert warm["allow"] is False
    assert warm["skip_reason"] == "clarity_mean_strength"


def test_size_double_matches_between_gate_and_config():
    cfg = _cfg(size_double_within_bars=3, size_double_mult=2.0)
    inside = decide_entry_gate(
        side=1,
        pred_mean=0.5,
        n_open_same_side=1,
        strength_hist=[0.1],
        cfg=cfg,
        bar_ts_ms=5 * HOUR,
        last_entry_ts_ms=3 * HOUR,
    )
    outside = decide_entry_gate(
        side=1,
        pred_mean=0.5,
        n_open_same_side=1,
        strength_hist=[0.1],
        cfg=cfg,
        bar_ts_ms=9 * HOUR,
        last_entry_ts_ms=3 * HOUR,
    )
    assert inside["size_mult"] == 2.0
    assert outside["size_mult"] == 1.0
