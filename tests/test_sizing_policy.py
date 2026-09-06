"""Equity×leverage notional sizing helpers."""

from __future__ import annotations

from llm2.sizing_policy import (
    DEFAULT_EQUITY_FRACTION,
    DEFAULT_STOP_RISK_FRACTION,
    SIZING_MODE_RISK_FRACTION,
    equity_leverage_notional,
    labelled_money_metrics,
    min_equity_for_stop_risk,
    parse_pack_sizing,
    peak_concurrent_margin_util,
    size_by_stop_risk,
)


def test_notional_formula():
    assert equity_leverage_notional(equity=10_000, equity_fraction=0.01, leverage=15) == 1500.0
    assert equity_leverage_notional(
        equity=10_000, equity_fraction=0.01, leverage=15, size_mult=2
    ) == 3000.0


def test_parse_pack_sizing_equity():
    p = parse_pack_sizing(
        {"sizing": {"mode": "EQUITY_LEVERAGE_NOTIONAL", "equity_fraction": 0.02}}
    )
    assert p["mode"] == "EQUITY_LEVERAGE_NOTIONAL"
    assert p["equity_fraction"] == 0.02


def test_parse_pack_sizing_legacy_min():
    p = parse_pack_sizing({"sizing": "MIN_EXCHANGE"})
    assert p["mode"] == "MIN_EXCHANGE"
    assert p["equity_fraction"] == DEFAULT_EQUITY_FRACTION


def test_labelled_money_metrics_keys():
    class M:
        starting_equity = 100.0
        ending_equity = 134.5
        net_pnl = 34.5
        invested_notional = 7285.0
        return_on_invested = 34.5 / 7285.0

    lab = labelled_money_metrics(M())
    assert abs(lab["wallet_return"] - 0.345) < 1e-9
    assert lab["roi_on_invested_notional"] is not None
    assert "wallet_return_note" in lab


def test_peak_margin_two_overlapping():
    class T:
        def __init__(self, e, x, q, px, pnl):
            self.entry_ts_ms = e
            self.exit_ts_ms = x
            self.qty = q
            self.entry_price = px
            self.realized_pnl = pnl

    # two overlapping books notional 1500 each, lev 15 → margin 100 each
    trades = [T(0, 100, 1.5, 1000.0, 1.0), T(10, 110, 1.5, 1000.0, 1.0)]
    peak = peak_concurrent_margin_util(trades, starting_equity=10_000.0, leverage=15.0)
    assert peak["peak_concurrent_books"] == 2
    assert abs(peak["peak_margin_usdt"] - 200.0) < 1e-6
    assert abs(peak["peak_margin_utilisation"] - 0.02) < 1e-9


def _sol_spec():
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    from tradesim.contracts import InstrumentSpec

    return InstrumentSpec(
        symbol="SOLUSDT",
        tick_size=0.01,
        qty_step=0.1,
        min_qty=0.1,
        min_notional=5.0,
        max_qty=96000.0,
        max_leverage=100.0,
    )


def test_parse_pack_sizing_risk_fraction():
    p = parse_pack_sizing({"sizing": {"mode": "RISK_FRACTION", "risk_fraction": 0.05}})
    assert p["mode"] == SIZING_MODE_RISK_FRACTION
    assert p["risk_fraction"] == 0.05
    assert DEFAULT_STOP_RISK_FRACTION == 0.05


def test_min_equity_for_stop_risk_average_sl():
    spec = _sol_spec()
    price = 200.0
    sl = 0.015
    # min lot 0.1 SOL * 200 USDT * 1.5% = 0.30 USDT stop-risk. 5% of equity = 0.30 → 6 USDT.
    e = min_equity_for_stop_risk(price=price, sl_pct=sl, instrument=spec, risk_fraction=0.05)
    assert abs(e - 6.0) < 1e-9


def test_size_by_stop_risk_floors_and_never_rounds_up():
    spec = _sol_spec()
    price = 200.0
    sl = 0.01
    # 5% of 250 = 12.5 USDT risk. raw qty = 12.5 / (200*0.01) = 6.25 → floor 6.2
    out = size_by_stop_risk(equity=250.0, price=price, sl_pct=sl, instrument=spec)
    assert out["ok"] is True
    assert abs(out["qty"] - 6.2) < 1e-9
    assert out["actual_risk_fraction"] <= 0.05 + 1e-12


def test_size_by_stop_risk_skips_when_min_lot_exceeds_cap():
    spec = _sol_spec()
    price = 200.0
    sl = 0.03
    # min lot risks 0.1*200*0.03=0.60 USDT. 5% of 5 = 0.25 < 0.60 → skip, do not round up.
    e_min = min_equity_for_stop_risk(price=price, sl_pct=sl, instrument=spec)
    assert abs(e_min - 12.0) < 1e-9
    out = size_by_stop_risk(equity=5.0, price=price, sl_pct=sl, instrument=spec)
    assert out["ok"] is False
    assert out["qty"] == 0.0
    assert out["skip_reason"] == "SKIP_MIN_QTY_RISK_CAP"
