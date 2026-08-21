"""Equity×leverage notional sizing helpers."""

from __future__ import annotations

from llm2.sizing_policy import (
    DEFAULT_EQUITY_FRACTION,
    equity_leverage_notional,
    labelled_money_metrics,
    parse_pack_sizing,
    peak_concurrent_margin_util,
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
