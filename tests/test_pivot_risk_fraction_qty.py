"""Pivot live qty follows pack sizing: min-lot stays min-lot; RISK_FRACTION uses stop."""

from __future__ import annotations

from llm2.live.pivot_runner import pack_uses_stop_risk_sizing, resolve_pivot_live_qty
from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
from tradesim.contracts import InstrumentSpec  # noqa: E402


def _sol() -> InstrumentSpec:
    return InstrumentSpec(
        symbol="SOLUSDT",
        tick_size=0.01,
        qty_step=0.1,
        min_qty=0.1,
        min_notional=5.0,
        max_qty=96000.0,
        max_leverage=100.0,
    )


def _decide(**kw):
    base = {
        "leverage": 29.0,
        "limit_px": 102.0,
        "sl_pct": 0.01,
        "tp_pct": 0.01,
    }
    base.update(kw)
    return base


def test_min_exchange_pack_stays_min_lot():
    strat = {"sizing": {"mode": "MIN_EXCHANGE"}}
    assert pack_uses_stop_risk_sizing(strat) is False
    qty, detail = resolve_pivot_live_qty(
        strategy=strat,
        decide=_decide(),
        instrument=_sol(),
        equity=20.0,
    )
    assert qty == 0.1
    assert detail["sizing_mode"] == "MIN_EXCHANGE"


def test_risk_fraction_pack_sizes_from_stop():
    strat = {"sizing": {"mode": "RISK_FRACTION", "risk_fraction": 0.05}}
    assert pack_uses_stop_risk_sizing(strat) is True
    qty, detail = resolve_pivot_live_qty(
        strategy=strat,
        decide=_decide(),
        instrument=_sol(),
        equity=20.4,
    )
    # floor((20.4 * 0.05) / (102 * 0.01) / 0.1) * 0.1 = 1.0
    assert qty == 1.0
    assert detail["sizing_mode"] == "RISK_FRACTION"
    assert detail["actual_risk_fraction"] <= 0.05 + 1e-12


def test_risk_fraction_skips_below_venue_min():
    strat = {"sizing": {"mode": "RISK_FRACTION", "risk_fraction": 0.05}}
    qty, detail = resolve_pivot_live_qty(
        strategy=strat,
        decide=_decide(sl_pct=0.03),
        instrument=_sol(),
        equity=2.0,
    )
    assert qty == 0.0
    assert detail.get("ok") is False or detail.get("skip_below_venue_min") is True


def test_risk_fraction_nearest_tracks_five_percent_not_min_lot():
    from llm2.sizing_policy import size_by_stop_risk

    btc = InstrumentSpec(
        symbol="BTCUSDT",
        tick_size=0.1,
        qty_step=0.001,
        min_qty=0.001,
        min_notional=5.0,
        max_qty=1500.0,
        max_leverage=150.0,
    )
    floor = size_by_stop_risk(
        equity=33.0,
        price=80945.8,
        sl_pct=0.011058287086688748,
        instrument=btc,
        risk_fraction=0.05,
        qty_round="floor",
        leverage=13.0,
    )
    nearest = size_by_stop_risk(
        equity=33.0,
        price=80945.8,
        sl_pct=0.011058287086688748,
        instrument=btc,
        risk_fraction=0.05,
        qty_round="nearest",
        leverage=13.0,
    )
    assert floor["qty"] == 0.001
    assert nearest["ok"] is True
    assert nearest["qty"] == 0.002
    assert nearest["raw_qty"] > 0.0015
    assert abs(nearest["actual_risk_fraction"] - 0.05) < abs(floor["actual_risk_fraction"] - 0.05)
