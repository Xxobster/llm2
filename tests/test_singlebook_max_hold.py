"""Unit tests for single-book max-hold ledger helpers (no exchange)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from llm2.live.micro_runner import (
    _expired_books,
    _insert_open_book,
    _last_live_entry_bar_ms,
    _mark_book_closed,
    _state_conn,
)


def test_state_conn_creates_open_books(tmp_path: Path):
    con = _state_conn(tmp_path / "state.sqlite")
    _insert_open_book(
        con,
        book_id="b1",
        side=1,
        entry_bar_ms=1_000_000,
        max_hold_bars=6,
        qty=0.01,
        tp_pct=0.01,
        sl_pct=0.02,
        book_idx=1,
        order_id="oid",
    )
    n = con.execute(
        "SELECT COUNT(*) FROM open_books WHERE status='open'"
    ).fetchone()[0]
    assert n == 1
    con.close()


def test_expired_books_after_horizon(tmp_path: Path):
    con = _state_conn(tmp_path / "state.sqlite")
    tf = "1h"
    entry = 1_700_000_000_000
    _insert_open_book(
        con,
        book_id="eth_buy",
        side=1,
        entry_bar_ms=entry,
        max_hold_bars=6,
        qty=0.01,
        tp_pct=0.01,
        sl_pct=0.02,
        book_idx=1,
        order_id=None,
    )
    assert _expired_books(con, bar_ms=entry + 5 * 3_600_000, timeframe=tf) == []
    exp = _expired_books(con, bar_ms=entry + 6 * 3_600_000, timeframe=tf)
    assert len(exp) == 1 and exp[0]["book_id"] == "eth_buy" and exp[0]["qty"] == 0.01
    con.close()


def test_last_live_entry_prefers_filled_order(tmp_path: Path):
    con = _state_conn(tmp_path / "state.sqlite")
    con.execute(
        "INSERT INTO decisions VALUES (100, 't', 1, 0.1, 1.0, 'LIVE', ?)",
        ('{"order_retCode":0}',),
    )
    con.execute(
        "INSERT INTO decisions VALUES (200, 't', 1, 0.1, 1.0, 'LIVE', ?)",
        ('{"skip_reason":"position_already_open:Buy"}',),
    )
    con.execute(
        "INSERT INTO decisions VALUES (300, 't', -1, -0.1, 1.0, 'LIVE', ?)",
        ('{"order_retCode":0}',),
    )
    con.commit()
    assert _last_live_entry_bar_ms(con, side=1) == 100
    assert _last_live_entry_bar_ms(con, side=-1) == 300
    con.close()


def test_mark_book_closed(tmp_path: Path):
    con = _state_conn(tmp_path / "state.sqlite")
    _insert_open_book(
        con,
        book_id="x",
        side=-1,
        entry_bar_ms=1,
        max_hold_bars=6,
        qty=0.1,
        tp_pct=0.01,
        sl_pct=0.02,
        book_idx=1,
        order_id=None,
    )
    _mark_book_closed(con, "x")
    st = con.execute("SELECT status FROM open_books WHERE book_id='x'").fetchone()[0]
    assert st == "closed"
    assert _expired_books(con, bar_ms=10**15, timeframe="1h") == []
    con.close()


def test_bybit_retcode_zero_is_success():
    from llm2.live.micro_runner import _bybit_retcode

    assert _bybit_retcode({"retCode": 0}) == 0
    assert _bybit_retcode({"retCode": "0"}) == 0
    assert _bybit_retcode({"retCode": 110061}) == 110061
    assert _bybit_retcode({}) == -1
    assert _bybit_retcode(None) == -1
