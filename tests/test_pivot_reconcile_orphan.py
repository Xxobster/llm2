"""Regression: an entry that fills during an exception must still get protected.

Live incident 2026-08-26 (LIVE-RECONCILE-001): the Ethereum diagonal S/R unit
placed its entry LIMIT, then ``manage_working_limit`` raised
``URLError: handshake operation timed out`` before the fill-wait step. The order
filled on Bybit anyway, so the account held a 29x short with no Take-Profit, no
Stop-Loss and no max-hold deadline, while local state still called the order
"working". Nothing in the loop could see it.
"""

from __future__ import annotations

import sqlite3

import pytest

from llm2.live import pivot_runner as pr


@pytest.fixture()
def con(tmp_path):
    c = pr._state_conn(tmp_path / "s.sqlite")
    yield c
    c.close()


def _fake_position(**over):
    row = {"size": "0.01", "avgPrice": "2490.39", "side": "Sell", "stopLoss": "0", "takeProfit": "0"}
    row.update(over)
    return row


def test_orphan_position_gets_bracket_and_max_hold(monkeypatch, con):
    """The exact incident: exchange has exposure, local state does not."""
    calls: list[dict] = []
    monkeypatch.setattr(pr, "_position_list", lambda **k: [_fake_position()])
    monkeypatch.setattr(pr, "maker_exit_bracket_present", lambda **k: False)
    monkeypatch.setattr(
        pr,
        "ensure_full_position_tpsl",
        lambda **k: calls.append(k) or {"retCode": 0, "retMsg": "OK", "sl_price": 2515.3, "tp_price": 2453.0},
    )
    # State as the incident left it: a "working" order that had actually filled.
    pr._state_set(con, "working_order_id", "f12650f7")
    pr._state_set(con, "working_deadline_ms", "1787785200000")
    assert pr._read_open_pos(con) is None, "precondition: bot is blind to the position"

    out = pr.reconcile_exchange_position(
        account="Xxobster4",
        symbol="ETHUSDT",
        timeframe="1h",
        con=con,
        tp_pct=0.015,
        sl_pct=0.01,
        max_hold_bars=8,
    )

    assert out["action"] == "reconciled"
    assert out["local_known"] is False
    # Protective bracket attached on the frozen percentages, short side.
    assert len(calls) == 1
    assert calls[0]["side"] == -1
    assert calls[0]["avg_price"] == pytest.approx(2490.39)
    assert calls[0]["tp_pct"] == pytest.approx(0.015)
    assert calls[0]["sl_pct"] == pytest.approx(0.01)
    # Position is now tracked, so max-hold can fire.
    pos = pr._read_open_pos(con)
    assert pos is not None
    assert pos["side"] == "Sell"
    assert pos["qty"] == pytest.approx(0.01)
    assert pos["max_hold_bars"] == 8
    # The phantom working order is cleared so a later cancel cannot fail forever.
    assert (pr._state_get(con, "working_order_id") or "") == ""
    rows = con.execute("SELECT event FROM pivot_fills").fetchall()
    assert [r[0] for r in rows] == ["reconciled_orphan_entry"]


def test_tracked_and_protected_is_a_noop(monkeypatch, con):
    monkeypatch.setattr(pr, "_position_list", lambda **k: [_fake_position(stopLoss="2515.3")])
    monkeypatch.setattr(pr, "maker_exit_bracket_present", lambda **k: True)
    monkeypatch.setattr(
        pr, "ensure_full_position_tpsl", lambda **k: pytest.fail("must not re-attach")
    )
    pr._record_open_pos(con, entry_bar_ms=1787770800000, side="Sell", qty=0.01, max_hold_bars=8)
    out = pr.reconcile_exchange_position(
        account="A", symbol="ETHUSDT", timeframe="1h", con=con,
        tp_pct=0.015, sl_pct=0.01, max_hold_bars=8,
    )
    assert out["action"] == "none"
    assert out["reason"] == "tracked_and_protected"


def test_flat_exchange_is_a_noop(monkeypatch, con):
    monkeypatch.setattr(pr, "_position_list", lambda **k: [])
    monkeypatch.setattr(
        pr, "ensure_full_position_tpsl", lambda **k: pytest.fail("must not touch a flat account")
    )
    out = pr.reconcile_exchange_position(
        account="A", symbol="ETHUSDT", timeframe="1h", con=con,
        tp_pct=0.015, sl_pct=0.01, max_hold_bars=8,
    )
    assert out == {"action": "none", "reason": "exchange_flat"}


def test_tracked_but_stop_missing_reattaches(monkeypatch, con):
    """Protection can also vanish after a manual cancel; re-attach, keep tracking."""
    calls: list[dict] = []
    monkeypatch.setattr(pr, "_position_list", lambda **k: [_fake_position()])
    monkeypatch.setattr(pr, "maker_exit_bracket_present", lambda **k: False)
    monkeypatch.setattr(
        pr,
        "ensure_full_position_tpsl",
        lambda **k: calls.append(k) or {"retCode": 0, "retMsg": "OK", "sl_price": 2515.3, "tp_price": 2453.0},
    )
    pr._record_open_pos(con, entry_bar_ms=1787770800000, side="Sell", qty=0.01, max_hold_bars=8)
    out = pr.reconcile_exchange_position(
        account="A", symbol="ETHUSDT", timeframe="1h", con=con,
        tp_pct=0.015, sl_pct=0.01, max_hold_bars=8,
    )
    assert out["action"] == "reconciled"
    assert len(calls) == 1
    # Original entry bar preserved: max-hold must not be silently extended.
    assert pr._read_open_pos(con)["entry_bar_ms"] == 1787770800000


def test_tpsl_failure_is_reported_not_swallowed(monkeypatch, con):
    monkeypatch.setattr(pr, "_position_list", lambda **k: [_fake_position()])
    monkeypatch.setattr(pr, "maker_exit_bracket_present", lambda **k: False)
    monkeypatch.setattr(
        pr, "ensure_full_position_tpsl", lambda **k: {"retCode": 10001, "retMsg": "nope"}
    )
    out = pr.reconcile_exchange_position(
        account="A", symbol="ETHUSDT", timeframe="1h", con=con,
        tp_pct=0.015, sl_pct=0.01, max_hold_bars=8,
    )
    assert out["action"] == "tpsl_failed"
    # Must not claim to track a position it failed to protect.
    assert pr._read_open_pos(con) is None
