"""Pivot live max-hold must match tradesim: flatten at entry_bar + N * tf."""

from __future__ import annotations

from pathlib import Path

from llm2.live.pivot_runner import (
    FILL_POLL_SEC,
    _clear_open_pos,
    _max_hold_due,
    _read_open_pos,
    _record_open_pos,
    _state_conn,
    entry_bar_open_ms_from_fill,
    max_hold_deadline_ms,
    record_pivot_fill,
    should_flatten_max_hold,
)
from llm2.paths import TF_MS


def test_deadline_is_entry_plus_hold_bars():
    tf = int(TF_MS["15m"])
    entry = 1_700_000_000_000
    assert max_hold_deadline_ms(entry, 6, tf) == entry + 6 * tf


def test_flatten_at_expiry_open_not_before():
    tf = int(TF_MS["15m"])
    entry = 1_786_597_200_000  # 13 Aug 2026 05:00 UTC-ish
    deadline = max_hold_deadline_ms(entry, 6, tf)
    assert should_flatten_max_hold(
        now_ms=deadline - 1, entry_bar_ms=entry, max_hold_bars=6, tf_ms=tf
    ) is False
    assert should_flatten_max_hold(
        now_ms=deadline, entry_bar_ms=entry, max_hold_bars=6, tf_ms=tf
    ) is True
    assert should_flatten_max_hold(
        now_ms=deadline + tf, entry_bar_ms=entry, max_hold_bars=6, tf_ms=tf
    ) is True


def test_zero_hold_never_flattens():
    tf = int(TF_MS["15m"])
    assert should_flatten_max_hold(
        now_ms=10**15, entry_bar_ms=0, max_hold_bars=0, tf_ms=tf
    ) is False


def test_fill_snaps_to_forming_bar_open():
    tf = int(TF_MS["15m"])
    bar_open = 1_786_597_200_000
    fill_mid = bar_open + 8 * 60 * 1000  # +8 minutes
    assert entry_bar_open_ms_from_fill(fill_mid, "15m") == bar_open
    assert entry_bar_open_ms_from_fill(bar_open, "15m") == bar_open
    assert entry_bar_open_ms_from_fill(bar_open + tf - 1, "15m") == bar_open


def test_open_pos_state_roundtrip(tmp_path: Path):
    con = _state_conn(tmp_path / "pivot_state.sqlite")
    assert _read_open_pos(con) is None
    entry = 1_786_597_200_000
    _record_open_pos(
        con, entry_bar_ms=entry, side="Sell", qty=0.1, max_hold_bars=6
    )
    pos = _read_open_pos(con)
    assert pos is not None
    assert pos["side"] == "Sell"
    assert pos["qty"] == 0.1
    assert pos["max_hold_bars"] == 6
    assert _max_hold_due(con, "15m", now_ms=entry + 5 * int(TF_MS["15m"])) is False
    assert _max_hold_due(con, "15m", now_ms=entry + 6 * int(TF_MS["15m"])) is True
    _clear_open_pos(con)
    assert _read_open_pos(con) is None
    con.close()


def test_fill_poll_is_not_ten_seconds():
    assert 0 < FILL_POLL_SEC <= 2.0


def test_record_pivot_fill(tmp_path: Path):
    con = _state_conn(tmp_path / "pivot_state.sqlite")
    record_pivot_fill(con, "entry_filled", {"avg_price": 79.14, "side": "Sell"})
    n, event, payload = con.execute(
        "SELECT COUNT(*), event, payload_json FROM pivot_fills"
    ).fetchone()
    assert n == 1
    assert event == "entry_filled"
    assert "79.14" in payload
    con.close()
