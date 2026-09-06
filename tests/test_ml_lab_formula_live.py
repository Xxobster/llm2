"""Live-path guards for hunt-009 / hunt-012 formula packs (not a deploy)."""

from __future__ import annotations

import json

import numpy as np
import pandas as pd
import pytest

from llm2.diagonal_sr.bar_series import make_bar_series
from llm2.edge_lab.sim_atr import atr_brackets, limit_prices
from llm2.gates.evidence import leverage_from_stop
from llm2.live.ema_stack_runner import load_pack
from llm2.ml_lab.idea_catalog_f import signals_f
from llm2.ml_lab.idea_catalog_i import signals_i
from llm2.ml_lab.idea_catalog_j import signals_j
from llm2.ml_lab.live_guards import (
    BTC_QUAD_SLOPE_SPEC,
    SOL_EMA_SPEC,
    SOL_FVG_CONFLUENCE_SPEC,
    SOL_HILBERT_AMP_FADE_SPEC,
    live_spec_for,
    refuse_taker_entry_fallback,
    refuse_venue_min_qty_fallback,
)
from llm2.ml_lab.live_signal import tip_signal
from llm2.research_policy import PolicyError


def _ohlcv(n: int = 900, seed: int = 7, freq: str = "1h") -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq=freq, tz="UTC")
    return pd.DataFrame(
        {
            "open": op,
            "high": np.maximum(op, close) * 1.004,
            "low": np.minimum(op, close) * 0.996,
            "close": close,
            "volume": rng.random(n) * 1000 + 10,
        },
        index=idx,
    )


def _write_pack(
    tmp_path, spec: dict, *, sizing_mode: str = "RISK_FRACTION", qty_round: str | None = None
):
    pack = tmp_path / "pack"
    pack.mkdir(parents=True)
    sizing: dict = {"mode": sizing_mode}
    if qty_round is not None:
        sizing["qty_round"] = qty_round
    (pack / "strategy.json").write_text(
        json.dumps(
            {
                "arm_id": f"{spec['symbol']}|{spec['timeframe']}|{spec['idea']}",
                "symbol": spec["symbol"],
                "timeframe": spec["timeframe"],
                "idea": spec["idea"],
                "k_sl": spec["k_sl"],
                "tp_ratio": spec["tp_ratio"],
                "sl_cap": spec["sl_cap"],
                "work_bars": spec["work_bars"],
                "max_hold_bars": spec["max_hold_bars"],
                "leverage": 13.0,
                "risk_fraction": 0.05,
                "sizing": sizing,
                "expired_entry": "cancel_and_flat",
            }
        ),
        encoding="utf-8",
    )
    return pack


def test_live_spec_lookup():
    assert live_spec_for("BTCUSDT", "1h", "quad_slope_follow")["catalog"] == "f"
    assert live_spec_for("SOLUSDT", "1h", "fvg_confluence")["catalog"] == "i"
    assert live_spec_for("SOLUSDT", "1h", "hilbert_amp_fade")["catalog"] == "j"
    assert live_spec_for("SOLUSDT", "1h", "power_ema_stack_long")["idea"] == SOL_EMA_SPEC["idea"]
    assert live_spec_for("ETHUSDT", "1h", "quad_slope_follow") is None


def test_leverage_from_3pct_cap_is_13x():
    assert leverage_from_stop(float(BTC_QUAD_SLOPE_SPEC["sl_cap"])) == 13.0
    assert leverage_from_stop(float(SOL_FVG_CONFLUENCE_SPEC["sl_cap"])) == 13.0
    assert leverage_from_stop(float(SOL_HILBERT_AMP_FADE_SPEC["sl_cap"])) == 13.0


def test_quad_slope_tip_matches_research_signed_bit():
    df = _ohlcv(500, seed=11)
    spec = dict(BTC_QUAD_SLOPE_SPEC)
    spec["symbol"] = "BTCUSDT"
    occ = signals_f(df, "1h")["quad_slope_follow"]
    sc = make_bar_series("BTCUSDT", "1h", df)
    n_short = 0
    n_long = 0
    for k in range(len(df) - 40, len(df)):
        sig = tip_signal(df.iloc[: k + 1], spec=spec)
        bit = float(occ[k])
        research_fires = bool(np.isfinite(bit) and abs(bit) >= 0.5)
        research_short = bool(np.isfinite(bit) and bit <= -0.5)
        if not sig.ok:
            assert not sig.fires
            continue
        assert bool(sig.fires) == research_fires
        assert bool(sig.is_short) == research_short
        sl, tp = atr_brackets(
            np.asarray([sc.atr_frac[k]]), k_sl=1.5, tp_ratio=1.5, sl_cap=0.030
        )
        lim = limit_prices(
            np.asarray([sc.close[k]]),
            np.asarray([sc.atr_frac[k]]),
            np.asarray([research_short]),
        )
        assert abs(sig.sl_pct - float(sl[0])) < 1e-12
        assert abs(sig.tp_pct - float(tp[0])) < 1e-12
        assert abs(sig.limit_px - float(lim[0])) < 1e-9
        if research_short:
            n_short += 1
            assert sig.side == "Sell"
        elif research_fires:
            n_long += 1
            assert sig.side == "Buy"
    assert n_short + n_long >= 1


def test_fvg_confluence_tip_is_long_only():
    df = _ohlcv(500, seed=21)
    spec = dict(SOL_FVG_CONFLUENCE_SPEC)
    occ = signals_i(df, "1h")["fvg_confluence"]
    for k in range(len(df) - 40, len(df)):
        sig = tip_signal(df.iloc[: k + 1], spec=spec)
        bit = float(occ[k])
        if not sig.ok:
            continue
        assert bit >= -1e-12
        assert sig.is_short is False
        assert bool(sig.fires) == bool(bit >= 0.5)


def test_hilbert_amp_fade_tip_matches_research_signed_bit():
    df = _ohlcv(500, seed=31)
    spec = dict(SOL_HILBERT_AMP_FADE_SPEC)
    occ = signals_j(df, "1h")["hilbert_amp_fade"]
    sc = make_bar_series("SOLUSDT", "1h", df)
    n_short = 0
    n_long = 0
    for k in range(len(df) - 200, len(df)):
        sig = tip_signal(df.iloc[: k + 1], spec=spec)
        bit = float(occ[k])
        research_fires = bool(np.isfinite(bit) and abs(bit) >= 0.5)
        research_short = bool(np.isfinite(bit) and bit <= -0.5)
        if not sig.ok:
            assert not sig.fires
            continue
        assert bool(sig.fires) == research_fires
        assert bool(sig.is_short) == research_short
        sl, tp = atr_brackets(
            np.asarray([sc.atr_frac[k]]), k_sl=1.5, tp_ratio=1.5, sl_cap=0.030
        )
        lim = limit_prices(
            np.asarray([sc.close[k]]),
            np.asarray([sc.atr_frac[k]]),
            np.asarray([research_short]),
        )
        assert abs(sig.sl_pct - float(sl[0])) < 1e-12
        assert abs(sig.tp_pct - float(tp[0])) < 1e-12
        assert abs(sig.limit_px - float(lim[0])) < 1e-9
        if research_short:
            n_short += 1
            assert sig.side == "Sell"
        elif research_fires:
            n_long += 1
            assert sig.side == "Buy"
    assert n_short + n_long >= 1


def test_formula_pack_load_requires_risk_fraction(tmp_path):
    pack = _write_pack(tmp_path, BTC_QUAD_SLOPE_SPEC, sizing_mode="MIN_EXCHANGE")
    with pytest.raises(PolicyError, match="RISK_FRACTION"):
        load_pack(pack)


def test_quad_slope_pack_requires_nearest_qty_round(tmp_path):
    pack = _write_pack(tmp_path, BTC_QUAD_SLOPE_SPEC, sizing_mode="RISK_FRACTION")
    with pytest.raises(PolicyError, match="qty_round=nearest"):
        load_pack(pack)


def test_fvg_pack_requires_min_exchange(tmp_path):
    pack = _write_pack(tmp_path, SOL_FVG_CONFLUENCE_SPEC, sizing_mode="RISK_FRACTION")
    with pytest.raises(PolicyError, match="MIN_EXCHANGE"):
        load_pack(pack)


def test_hilbert_pack_requires_five_pct_not_min_exchange(tmp_path):
    pack = _write_pack(tmp_path, SOL_HILBERT_AMP_FADE_SPEC, sizing_mode="MIN_EXCHANGE")
    with pytest.raises(PolicyError, match="5% of equity"):
        load_pack(pack)
    pack = _write_pack(
        tmp_path / "floor",
        SOL_HILBERT_AMP_FADE_SPEC,
        sizing_mode="RISK_FRACTION",
        qty_round="floor",
    )
    with pytest.raises(PolicyError, match="qty_round=nearest"):
        load_pack(pack)


def test_hilbert_wallet_qty_is_five_pct_not_venue_min():
    from llm2.sizing_policy import size_by_stop_risk
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    from tradesim.contracts import InstrumentSpec

    inst = InstrumentSpec(
        symbol="SOLUSDT",
        tick_size=0.01,
        qty_step=0.1,
        min_qty=0.1,
        min_notional=5.0,
        max_qty=96000.0,
        max_leverage=100.0,
    )
    out = size_by_stop_risk(
        equity=26.33,
        price=105.24,
        sl_pct=0.013168209840858534,
        instrument=inst,
        risk_fraction=0.05,
        qty_round="nearest",
        leverage=13.0,
    )
    assert out["ok"] is True
    assert out["qty"] == 0.9
    assert out["qty"] > inst.min_qty + 1e-12
    assert abs(out["actual_risk_fraction"] - 0.05) < abs(0.1 * 105.24 * 0.013168209840858534 / 26.33 - 0.05)


def test_refuse_venue_min_qty_fallback():
    refuse_venue_min_qty_fallback(qty=0.9, raw_qty=0.95, min_qty=0.1, qty_step=0.1)
    with pytest.raises(PolicyError, match="venue-min"):
        refuse_venue_min_qty_fallback(qty=0.1, raw_qty=0.95, min_qty=0.1, qty_step=0.1)


def test_formula_pack_load_accepts_authorized_ideas(tmp_path):
    refuse_taker_entry_fallback(market_on_unfilled=False)
    for spec in (
        BTC_QUAD_SLOPE_SPEC,
        SOL_FVG_CONFLUENCE_SPEC,
        SOL_HILBERT_AMP_FADE_SPEC,
        SOL_EMA_SPEC,
    ):
        if spec["idea"] == "quad_slope_follow":
            pack = _write_pack(
                tmp_path / spec["idea"],
                spec,
                sizing_mode="RISK_FRACTION",
                qty_round="nearest",
            )
        elif spec["idea"] == "fvg_confluence":
            pack = _write_pack(tmp_path / spec["idea"], spec, sizing_mode="MIN_EXCHANGE")
        elif spec["idea"] == "hilbert_amp_fade":
            pack = _write_pack(
                tmp_path / spec["idea"],
                spec,
                sizing_mode="RISK_FRACTION",
                qty_round="nearest",
            )
        else:
            pack = _write_pack(tmp_path / spec["idea"], spec)
        loaded = load_pack(pack)
        assert loaded["idea"] == spec["idea"]
        assert loaded["symbol"] == spec["symbol"]


def test_unknown_idea_pack_refused(tmp_path):
    spec = dict(BTC_QUAD_SLOPE_SPEC)
    spec["idea"] = "not_a_real_idea"
    pack = _write_pack(tmp_path, spec)
    with pytest.raises(PolicyError, match="authorized live formula"):
        load_pack(pack)
