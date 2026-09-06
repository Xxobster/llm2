"""Maker-first live requests: Post-Only entry, limit take-profit/stop, gap flatten.

No exchange calls. Request bodies are inspected after the signed-request layer
is stubbed.
"""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from llm2.gates.evidence import research_costs_baseline, research_maker_first_costs
from llm2.live import micro_runner as mr
from llm2.live import pivot_runner as pr
from tradesim import Liquidity


def test_place_working_limit_is_post_only(monkeypatch):
    captured: dict = {}

    monkeypatch.setattr(pr, "ensure_hedge_mode", lambda **k: None)
    monkeypatch.setattr(pr, "ensure_exchange_leverage", lambda **k: None)
    monkeypatch.setattr(pr, "_load_account_keys", lambda account: ("k", "s"))
    monkeypatch.setattr(
        pr, "research_instrument", lambda symbol: SimpleNamespace(tick_size=0.01)
    )

    def _signed(**kw):
        captured.update(kw)
        return {"retCode": 0, "retMsg": "OK", "result": {"orderId": "1"}}

    monkeypatch.setattr(pr, "_bybit_signed_request", _signed)

    out = pr.place_working_limit(
        account="Xxobster4",
        symbol="ETHUSDT",
        side="Sell",
        qty=0.01,
        price=2490.39,
        leverage=29,
    )
    body = out["request"]
    assert body["timeInForce"] == "PostOnly"
    assert body["orderType"] == "Limit"
    assert body["side"] == "Sell"
    assert captured["path"] == "/v5/order/create"


def test_place_maker_exit_bracket_postonly_tp_and_stop_limit(monkeypatch):
    """Full trading-stop is Market-only. Live product is independent maker exits."""
    calls: list[dict] = []
    monkeypatch.setattr(mr, "_load_account_keys", lambda account: ("k", "s"))
    monkeypatch.setattr(mr, "_instrument_tick", lambda symbol: 0.01)
    monkeypatch.setattr(mr, "_list_open_orders", lambda **k: [])
    monkeypatch.setattr(mr, "_list_stop_orders", lambda **k: [])

    def _signed(**kw):
        calls.append(kw)
        return {"retCode": 0, "retMsg": "OK", "result": {"orderId": str(len(calls))}}

    monkeypatch.setattr(mr, "_bybit_signed_request", _signed)

    out = mr.place_maker_exit_bracket(
        account="Xxobster4",
        symbol="ETHUSDT",
        side=-1,
        avg_price=2500.0,
        tp_pct=0.015,
        sl_pct=0.01,
        qty=0.01,
    )
    assert out["retCode"] == 0
    assert out["mode"] == "maker_exit_bracket"
    assert out["tp_ok"] is True
    assert out["sl_ok"] is True
    assert out["tp_price"] == pytest.approx(2462.50)
    assert out["sl_price"] == pytest.approx(2525.00)
    creates = [c for c in calls if c["path"] == "/v5/order/create"]
    assert len(creates) == 2
    tp = next(c for c in creates if c["body"].get("timeInForce") == "PostOnly")
    sl = next(c for c in creates if "triggerPrice" in c["body"])
    assert tp["body"]["reduceOnly"] is True
    assert tp["body"]["orderType"] == "Limit"
    assert tp["body"]["side"] == "Buy"
    assert tp["body"]["price"] == "2462.50"
    assert sl["body"]["reduceOnly"] is True
    assert sl["body"]["orderType"] == "Limit"
    assert sl["body"]["triggerPrice"] == "2525.00"
    assert sl["body"]["price"] == "2525.00"
    assert sl["body"]["triggerDirection"] == 1
    assert sl["body"]["triggerBy"] == "MarkPrice"
    assert sl["body"]["timeInForce"] == "GTC"
    clears = [c for c in calls if c["path"] == "/v5/position/trading-stop"]
    assert len(clears) == 1
    assert clears[0]["body"]["takeProfit"] == "0"
    assert clears[0]["body"]["stopLoss"] == "0"
    assert clears[0]["body"]["tpslMode"] == "Full"


def test_place_maker_exit_bracket_skips_existing(monkeypatch):
    monkeypatch.setattr(mr, "_load_account_keys", lambda account: ("k", "s"))
    monkeypatch.setattr(mr, "_instrument_tick", lambda symbol: 0.01)
    monkeypatch.setattr(
        mr,
        "_list_open_orders",
        lambda **k: [
            {
                "side": "Sell",
                "orderType": "Limit",
                "timeInForce": "PostOnly",
                "reduceOnly": True,
                "positionIdx": 1,
                "price": "103.00",
                "orderId": "tp1",
            }
        ],
    )
    monkeypatch.setattr(
        mr,
        "_list_stop_orders",
        lambda **k: [
            {
                "side": "Sell",
                "orderType": "Limit",
                "positionIdx": 1,
                "triggerPrice": "99.00",
                "price": "99.00",
                "orderId": "sl1",
            }
        ],
    )
    called = []

    def _signed(**kw):
        called.append(kw["path"])
        return {"retCode": 0, "retMsg": "OK"}

    monkeypatch.setattr(mr, "_bybit_signed_request", _signed)
    out = mr.place_maker_exit_bracket(
        account="A",
        symbol="SOLUSDT",
        side=1,
        avg_price=100.0,
        tp_pct=0.03,
        sl_pct=0.01,
        qty=0.1,
    )
    assert out["tp"]["skipped"] is True
    assert out["sl"]["skipped"] is True
    assert "/v5/order/create" not in called
    assert called == ["/v5/position/trading-stop"]


def test_gap_flatten_fires_when_mark_through_short_stop(monkeypatch, tmp_path):
    con = pr._state_conn(tmp_path / "s.sqlite")
    closes: list[dict] = []
    monkeypatch.setattr(
        pr,
        "_position_list",
        lambda **k: [
            {
                "size": "0.01",
                "side": "Sell",
                "stopLoss": "2525.00",
                "markPrice": "2530.00",
            }
        ],
    )
    monkeypatch.setattr(
        pr,
        "close_reduce_only",
        lambda **k: closes.append(k) or {"retCode": 0, "retMsg": "OK"},
    )
    pr._record_open_pos(con, entry_bar_ms=1, side="Sell", qty=0.01, max_hold_bars=8)
    out = pr.maybe_gap_flatten_taker(account="A", symbol="ETHUSDT", con=con)
    assert out["action"] == "flattened"
    assert closes == [{"account": "A", "symbol": "ETHUSDT", "side": -1, "qty": 0.01}]
    assert pr._read_open_pos(con) is None
    con.close()


def test_gap_flatten_is_noop_when_mark_inside_stop(monkeypatch, tmp_path):
    con = pr._state_conn(tmp_path / "s.sqlite")
    monkeypatch.setattr(
        pr,
        "_position_list",
        lambda **k: [
            {
                "size": "0.01",
                "side": "Sell",
                "stopLoss": "2525.00",
                "markPrice": "2490.00",
            }
        ],
    )
    monkeypatch.setattr(
        pr, "close_reduce_only", lambda **k: pytest.fail("must not flatten inside the stop")
    )
    out = pr.maybe_gap_flatten_taker(account="A", symbol="ETHUSDT", con=con)
    assert out["action"] == "none"
    assert out["reason"] == "mark_inside_stop"
    con.close()


def test_gap_flatten_uses_stop_limit_when_position_stop_blank(monkeypatch, tmp_path):
    con = pr._state_conn(tmp_path / "s.sqlite")
    closes: list[dict] = []
    monkeypatch.setattr(
        pr,
        "_position_list",
        lambda **k: [
            {
                "size": "0.01",
                "side": "Sell",
                "stopLoss": "0",
                "markPrice": "2530.00",
            }
        ],
    )
    monkeypatch.setattr(
        pr, "stop_trigger_px_from_open_orders", lambda **k: 2525.0
    )
    monkeypatch.setattr(
        pr,
        "close_reduce_only",
        lambda **k: closes.append(k) or {"retCode": 0, "retMsg": "OK"},
    )
    out = pr.maybe_gap_flatten_taker(account="A", symbol="ETHUSDT", con=con)
    assert out["action"] == "flattened"
    assert out["sl"] == pytest.approx(2525.0)
    assert closes
    con.close()


def test_research_maker_first_costs_are_maker_on_resting_legs():
    base = research_costs_baseline()
    maker = research_maker_first_costs()
    assert base.role_liquidity["entry"] == Liquidity.TAKER
    assert maker.role_liquidity["entry"] == Liquidity.MAKER
    assert maker.role_liquidity["take_profit"] == Liquidity.MAKER
    assert maker.role_liquidity["stop"] == Liquidity.MAKER
    assert maker.role_liquidity["timeout"] == Liquidity.TAKER
    assert maker.entry_slippage == 0.0
    assert maker.maker_rate == pytest.approx(0.0002)
    assert maker.taker_rate == pytest.approx(0.00055)
