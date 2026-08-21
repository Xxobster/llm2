"""Unit tests for confirmation, confidence size, and next-opposite labels."""

from __future__ import annotations

import numpy as np
import pandas as pd

from tradesim import Side
from tradesim.contracts import EntryOrder

from llm2.pivot.labels.fractal import next_opposite_pivot_at_decisions
from llm2.pivot.strategy.confidence_size import size_mult_linear, size_mult_tertile
from llm2.pivot.strategy.confirm_addon import (
    addon_signals_after_fill,
    delay_intents_until_confirm,
    pivot_shape_confirmed,
)
from llm2.pivot.strategy.score_oos import default_label_cfg
from llm2.pivot.strategy.working_limit import LimitIntent, materialize_working_limits


def test_confirm_bars_not_below_right_bars():
    cfg = default_label_cfg(confirm_bars=2)
    assert cfg.confirm_bars >= cfg.right_bars
    cfg5 = default_label_cfg(confirm_bars=5)
    assert cfg5.confirm_bars == 5


def test_next_opposite_after_first_high():
    events = pd.DataFrame(
        {
            "pivot_origin_ts_ms": [1000, 1500, 2500],
            "pivot_side": ["high", "low", "high"],
            "pivot_price": [110.0, 90.0, 120.0],
        }
    )
    first_origin = np.array([1000, 1000, 2500], dtype=np.int64)
    first_side = np.array(["high", "high", "high"])
    nxt = next_opposite_pivot_at_decisions(
        first_origin, first_side, events, extra_horizon_ms=600
    )
    assert nxt.loc[0, "side"] == "low"
    assert nxt.loc[0, "origin_ts_ms"] == 1500
    assert nxt.loc[0, "pivot_price"] == 90.0
    # 1500 is outside 1000+400
    nxt2 = next_opposite_pivot_at_decisions(
        first_origin, first_side, events, extra_horizon_ms=400
    )
    assert nxt2.loc[0, "side"] == "none"
    # last high has no later low
    assert nxt.loc[2, "side"] == "none"


def test_size_mult_linear_at_threshold_is_one():
    p = np.array([0.4, 0.8, 1.0])
    thr = np.array([0.4, 0.4, 0.4])
    m = size_mult_linear(p, thr, lo=0.5, hi=2.0)
    assert abs(m[0] - 1.0) < 1e-12
    assert m[1] == 2.0
    assert m[2] == 2.0


def test_size_mult_tertile_train_only_edges():
    rng = np.random.default_rng(0)
    p = np.concatenate([np.linspace(0.4, 0.9, 90), np.array([0.99, 0.99])])
    g = np.ones(len(p), dtype=bool)
    m, info = size_mult_tertile(p, g, train_frac=0.7)
    assert info["status"] == "OK"
    assert m.min() == 0.5
    assert m.max() == 1.5
    # last two high p(any) rows are outside the train cut and still get a bucket
    assert m[-1] == 1.5
    _ = rng


def test_pivot_shape_confirm_k1_and_k2():
    close = np.array([100.0, 101.0, 99.0, 98.0])
    high = np.array([100.5, 102.0, 100.0, 99.0])
    low = np.array([99.5, 100.0, 98.0, 97.5])
    # short, k=1: close[1]=101 > 100 → not confirmed
    assert not pivot_shape_confirmed(
        is_short=True, i_dec=0, k=1, high=high, low=low, close=close
    )
    # short, k=2: max high in bars 1..2 is bar1 (102), last close 99 < 102
    assert pivot_shape_confirmed(
        is_short=True, i_dec=0, k=2, high=high, low=low, close=close
    )


def _ohlcv_dip() -> pd.DataFrame:
    idx = pd.date_range("2024-01-01", periods=12, freq="15min", tz="UTC")
    close = np.full(12, 100.0)
    high = close + 0.5
    low = close - 0.5
    # after bar 0, make a high then reverse down (short confirm k=2)
    high[1] = 102.0
    close[2] = 99.0
    low[3] = 98.0  # later long-limit touch unused
    return pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": 1.0},
        index=idx,
    )


def test_delay_intents_keeps_confirmed_short():
    ohlcv = _ohlcv_dip()
    ts0 = int(ohlcv.index[0].value // 1_000_000)
    intent = LimitIntent(
        decision_ts_ms=ts0,
        side=Side.SHORT,
        limit_price=101.5,
        stop_offset=0.01,
        target_offset=0.01,
        max_hold_bars=4,
        work_bars=4,
    )
    kept, stats = delay_intents_until_confirm(ohlcv, [intent], confirm_k=2)
    assert stats["n_confirmed"] == 1
    assert len(kept) == 1
    assert kept[0].decision_ts_ms == int(ohlcv.index[2].value // 1_000_000)


def test_addon_emits_when_in_profit_and_not_stopped():
    idx = pd.date_range("2024-01-01", periods=10, freq="15min", tz="UTC")
    close = np.full(10, 100.0)
    high = close + 0.4
    low = close - 0.4
    low[2] = 98.5  # long limit 99 touches on bar 2
    close[3] = 100.6
    close[4] = 101.0
    ohlcv = pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": 1.0},
        index=idx,
    )
    ts0 = int(idx[0].value // 1_000_000)
    intent = LimitIntent(
        decision_ts_ms=ts0,
        side=Side.LONG,
        limit_price=99.0,
        stop_offset=0.02,
        target_offset=0.02,
        max_hold_bars=4,
        work_bars=4,
        meta={"size_mult": 1.5},
    )
    sigs, stats = materialize_working_limits(ohlcv, [intent], work_bars=4)
    assert stats["n_filled_path"] == 1
    add, ast = addon_signals_after_fill(ohlcv, sigs, confirm_k=2)
    assert ast["n_addon"] == 1
    assert add[0].meta["size_mult"] == 1.5
    assert add[0].entry_order == EntryOrder.MARKET
