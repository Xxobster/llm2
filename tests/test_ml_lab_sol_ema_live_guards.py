"""Live-path guards for Solana 1h power_ema_stack_long (not a deploy).

Locks: 1-hour + 1-minute tip freshness, research-bit identity, stop-cap leverage
(not the 1% / 29× pivot default). Gate C all-taker fail blocks a Shadow-Ready
*stamp*, not a user-authorized minimum-size Post-Only test.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.gates.evidence import leverage_from_stop
from llm2.gates.v21 import evaluate_v21_gates
from llm2.live.candle_freshness import evaluate_tip_freshness, expected_closed_open_ms
from llm2.ml_lab.idea_catalog import signals_from_ohlcv
from llm2.ml_lab.live_guards import (
    SOL_EMA_SPEC,
    refuse_shadow_ready_stamp,
    refuse_taker_entry_fallback,
)
from llm2.research_policy import PolicyError


def _ohlcv(n: int = 900, seed: int = 5) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": close * (1.0 + rng.random(n) * 0.004),
            "low": close * (1.0 - rng.random(n) * 0.004),
            "close": close,
            "volume": rng.random(n) * 1000 + 10,
        },
        index=idx,
    )


def test_ema_stack_prefix_matches_research_builder():
    df = _ohlcv(1200)
    full = signals_from_ohlcv(df, "1h")["power_ema_stack_long"]
    prefix = signals_from_ohlcv(df.iloc[:-80], "1h")["power_ema_stack_long"]
    np.testing.assert_allclose(full[:-80], prefix, rtol=1e-9, atol=1e-9)


def test_live_tip_equals_research_bit_on_last_closed_bars():
    df = _ohlcv()
    occ = signals_from_ohlcv(df, "1h")["power_ema_stack_long"]
    checked = 0
    for k in range(len(df) - 40, len(df)):
        tip = signals_from_ohlcv(df.iloc[: k + 1], "1h")["power_ema_stack_long"][-1]
        assert float(tip) == float(occ[k])
        assert float(tip) in (0.0, 1.0)
        checked += 1
    assert checked >= 30


def test_atr_cap_leverage_is_not_pivot_29x():
    """Frozen sl_cap 3% → ~13× after buffers/haircut. 1% pivot 29× would over-lever."""
    assert leverage_from_stop(0.01) == 29.0
    assert leverage_from_stop(float(SOL_EMA_SPEC["sl_cap"])) == 13.0
    assert leverage_from_stop(float(SOL_EMA_SPEC["sl_cap"])) < leverage_from_stop(0.01)


def test_gate_c_fail_blocks_shadow_ready_stamp_not_user_min_live():
    daily = np.random.default_rng(0).normal(0.001, 0.004, 400)
    gates = evaluate_v21_gates(
        fold_pnls=[8, 10, 12, 6, 9, 5],
        fold_pfs=[1.15, 1.41, 1.42, 1.11, 1.68, 1.15],
        fold_trades=[82, 100, 176, 111, 135, 79],
        daily_returns=daily,
        pooled_pf=1.357,
        pooled_trades=683,
        n_trials=449,
        n_bootstrap=200,
        stress_pnl=-24.012,
        stress_pf=0.8528,
        baseline_mdd=0.0005,
        stress_mdd=0.0024,
        margin_util=0.0004,
        liquidation=False,
    )
    assert gates["overall"] == "FAIL"
    assert gates["stress_pf"] == "FAIL"
    with pytest.raises(PolicyError, match="SHADOW_READY stamp REFUSED"):
        refuse_shadow_ready_stamp(gates)
    refuse_taker_entry_fallback(market_on_unfilled=False)
    with pytest.raises(PolicyError, match="stay flat"):
        refuse_taker_entry_fallback(market_on_unfilled=True)


def test_one_hour_and_one_minute_tip_freshness():
    """Decision timeframe 1h plus touch timeframe 1m — both must match server time."""
    server = 1_704_067_200_000  # exact 1h boundary
    exp_1h = expected_closed_open_ms("1h", server_now_ms=server)
    exp_1m = expected_closed_open_ms("1m", server_now_ms=server)
    ok_1h = evaluate_tip_freshness(
        exchange="binance",
        symbol="SOLUSDT",
        timeframe="1h",
        local_tip_ms=exp_1h,
        server_now_ms=server,
        local_wall_ms=server,
        fetch_server_time=False,
    )
    ok_1m = evaluate_tip_freshness(
        exchange="binance",
        symbol="SOLUSDT",
        timeframe="1m",
        local_tip_ms=exp_1m,
        server_now_ms=server,
        local_wall_ms=server,
        fetch_server_time=False,
    )
    assert ok_1h.ok and ok_1m.ok
    stale_1h = evaluate_tip_freshness(
        exchange="binance",
        symbol="SOLUSDT",
        timeframe="1h",
        local_tip_ms=exp_1h - 3_600_000,
        server_now_ms=server,
        local_wall_ms=server,
        fetch_server_time=False,
    )
    assert stale_1h.code == "CANDLE_STALE"
    assert stale_1h.ok is False


def test_live_signal_matches_research_bit_and_atr_bracket():
    from llm2.diagonal_sr.bar_series import make_bar_series
    from llm2.edge_lab.sim_atr import atr_brackets, limit_prices
    from llm2.ml_lab.live_signal import tip_signal

    df = _ohlcv(400)
    occ = signals_from_ohlcv(df, "1h")["power_ema_stack_long"]
    sc = make_bar_series("SOLUSDT", "1h", df)
    for k in range(len(df) - 30, len(df)):
        sig = tip_signal(df.iloc[: k + 1])
        assert float(sig.fires) == float(occ[k] >= 0.5) or (not sig.ok and not sig.fires)
        if not sig.ok:
            continue
        sl, tp = atr_brackets(
            np.asarray([sc.atr_frac[k]]),
            k_sl=1.5,
            tp_ratio=1.5,
            sl_cap=0.030,
        )
        lim = limit_prices(
            np.asarray([sc.close[k]]),
            np.asarray([sc.atr_frac[k]]),
            np.asarray([False]),
        )
        assert abs(sig.sl_pct - float(sl[0])) < 1e-12
        assert abs(sig.tp_pct - float(tp[0])) < 1e-12
        assert abs(sig.limit_px - float(lim[0])) < 1e-9
        assert sig.side == "Buy"


def test_resolve_order_qty_risk_fraction_floors_and_skips():
    from llm2.live.micro_runner import resolve_order_qty
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    from tradesim.contracts import InstrumentSpec

    spec = InstrumentSpec(
        symbol="SOLUSDT",
        tick_size=0.01,
        qty_step=0.1,
        min_qty=0.1,
        min_notional=5.0,
        max_qty=96000.0,
        max_leverage=100.0,
    )
    sizing = {"mode": "RISK_FRACTION", "risk_fraction": 0.05}
    qty, detail = resolve_order_qty(
        sizing=sizing,
        equity=20.0,
        leverage=13.0,
        price=102.34,
        size_mult=1.0,
        instrument=spec,
        min_qty_fallback=0.1,
        force_min_exchange=True,  # must NOT collapse RISK_FRACTION to min lot
        sl_pct=0.022865,
    )
    assert qty >= 0.1
    assert qty == 0.4
    assert detail["sizing_mode"] == "RISK_FRACTION"
    assert detail["actual_risk_fraction"] <= 0.05 + 1e-12

    qty0, det0 = resolve_order_qty(
        sizing=sizing,
        equity=2.0,
        leverage=13.0,
        price=102.34,
        size_mult=1.0,
        instrument=spec,
        min_qty_fallback=0.1,
        sl_pct=0.03,
    )
    assert qty0 == 0.0
    assert det0["ok"] is False


def test_ema_pack_load_requires_risk_fraction(tmp_path):
    import json

    from llm2.live.ema_stack_runner import load_pack
    from llm2.research_policy import PolicyError

    pack = tmp_path / "pack"
    pack.mkdir()
    (pack / "strategy.json").write_text(
        json.dumps(
            {
                "arm_id": "x",
                "symbol": "SOLUSDT",
                "timeframe": "1h",
                "idea": "power_ema_stack_long",
                "k_sl": 1.5,
                "tp_ratio": 1.5,
                "sl_cap": 0.03,
                "work_bars": 3,
                "max_hold_bars": 16,
                "leverage": 13.0,
                "risk_fraction": 0.05,
                "sizing": {"mode": "MIN_EXCHANGE"},
                "expired_entry": "cancel_and_flat",
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(PolicyError, match="RISK_FRACTION"):
        load_pack(pack)
