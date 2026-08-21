"""Unit tests for pivot strategy EV + working-limit materialization."""

from __future__ import annotations

import numpy as np
import pandas as pd

from tradesim import Side

from llm2.pivot.strategy.ev import break_even_probability, net_bracket_magnitudes
from llm2.pivot.strategy.level_economy import level_error_stats
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits


def test_break_even_tp_sl_fee_geometry():
    b = net_bracket_magnitudes(0.02, 0.01)
    assert b.mu_plus > 0
    assert b.mu_minus > 0
    assert 0.0 < b.pi_star < 1.0
    # 2:1 TP:SL → lower break-even than 1:2
    pi_fav = break_even_probability(0.02, 0.01)
    pi_adv = break_even_probability(0.01, 0.02)
    assert pi_fav < pi_adv
    assert pi_adv > 0.6


def test_level_error_stats_mae():
    y = np.array([0.01, 0.02, -0.01])
    p = np.array([0.011, 0.015, -0.012])
    s = level_error_stats(y_level_ret=y, pred_level_ret=p)
    assert s["n"] == 3
    assert s["mae_pct"] > 0
    assert np.isfinite(s["p90_abs_pct"])


def test_materialize_working_limit_touch():
    idx = pd.date_range("2024-01-01", periods=10, freq="15min", tz="UTC")
    # flat then dip so long limit fills
    close = np.full(10, 100.0)
    high = close + 0.5
    low = close - 0.5
    low[3] = 98.0  # touch long at 99
    ohlcv = pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": 1.0},
        index=idx,
    )
    ts0 = int(idx[0].value // 1_000_000)
    intent = LimitIntent(
        decision_ts_ms=ts0,
        side=Side.LONG,
        limit_price=99.0,
        stop_offset=0.01,
        target_offset=0.02,
        max_hold_bars=4,
    )
    sigs, stats = materialize_working_limits(ohlcv, [intent], work_bars=4)
    assert stats["n_filled_path"] == 1
    assert len(sigs) == 1
    assert sigs[0].limit_price == 99.0
