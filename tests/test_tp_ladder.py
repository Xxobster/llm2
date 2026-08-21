from tradesim import Side, Signal

from llm2.backtest.run import run_strategy_backtest
from llm2.gates.evidence import research_costs_baseline
from llm2.signals.tp_ladder import attach_tp1_be_tp2_hold24


def test_tp1_be_tp2_ladder_preserves_entry_signal():
    original = Signal(
        ts_ms=1_700_000_000_000,
        side=Side.LONG,
        stop_offset=0.02,
        target_offset=0.01,
        max_hold_bars=12,
        tag="k5",
        meta={"size_mult": 2.0},
    )
    ladder = attach_tp1_be_tp2_hold24([original])

    assert len(ladder) == 1
    signal = ladder[0]
    assert signal.side == original.side
    assert signal.stop_offset == 0.02
    assert signal.target_offset is None
    assert signal.max_hold_bars == 24
    assert len(signal.tp_legs) == 2
    assert [leg.qty_fraction for leg in signal.tp_legs] == [0.5, 0.5]
    assert [leg.price_offset for leg in signal.tp_legs] == [0.01, 0.02]
    assert signal.break_even is not None
    assert signal.break_even.trigger_on_leg == 0
    assert signal.break_even.stop_offset == 0.0
    assert signal.meta["size_mult"] == 2.0
    assert signal.meta["post_tp1_hold_reset_supported"] is False
    assert original.target_offset == 0.01
    assert original.max_hold_bars == 12


def test_tp1_be_tp2_ladder_is_accepted_by_botsgeneral_tradesim():
    import pandas as pd
    from tradesim import research_instrument, research_margin, research_sizing, research_sim_hedge

    index = pd.date_range("2026-01-01", periods=5, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {
            "ts_ms": (index.as_unit("ns").asi8 // 1_000_000).astype("int64"),
            "open": [100.0, 100.0, 101.0, 102.0, 101.0],
            "high": [100.5, 101.5, 102.5, 103.0, 101.5],
            "low": [99.5, 99.5, 100.5, 101.0, 99.5],
            "close": [100.0, 101.0, 102.0, 101.0, 100.0],
            "volume": [1.0] * 5,
        },
        index=index,
    )
    signal = Signal(
        ts_ms=int(index[0].value // 1_000_000),
        side=Side.LONG,
        stop_offset=0.02,
        target_offset=0.01,
        max_hold_bars=12,
        tag="smoke",
    )
    ladder = attach_tp1_be_tp2_hold24([signal])
    bundle = run_strategy_backtest(
        ohlcv,
        ladder,
        symbol="ETHUSDT",
        timeframe="1h",
        costs=research_costs_baseline(),
        margin=research_margin(leverage=10),
        sizing=research_sizing(),
        sim=research_sim_hedge(decision_timeframe="1h"),
        instrument=research_instrument("ETHUSDT"),
        plot=False,
        print_headline=False,
        store_path=None,
    )

    assert bundle.result.n_trades == 1
