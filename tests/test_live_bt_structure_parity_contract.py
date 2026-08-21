"""Contracts: single-book max-hold + live/BT structure parity."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from llm2.live.feature_parity_contract import (
    BACKTEST_USES_TRUNCATED_STRUCTURE_REFRESH,
    FORBIDDEN_LIVE_STRUCTURE_LIMIT,
    LIVE_MUST_MATCH_FULL_HISTORY_WAREHOUSE,
)
from llm2.live.micro_runner import (
    _expired_books,
    _insert_open_book,
    _required_completed_htf_open_ms,
    _state_conn,
    _structure_ready_for_decide,
)
from llm2.live.refresh_structure import MIN_STRUCTURE_HISTORY_BARS, refresh_symbol


def test_contract_backtest_not_truncated():
    assert BACKTEST_USES_TRUNCATED_STRUCTURE_REFRESH is False
    assert LIVE_MUST_MATCH_FULL_HISTORY_WAREHOUSE is True
    assert FORBIDDEN_LIVE_STRUCTURE_LIMIT == 800
    assert MIN_STRUCTURE_HISTORY_BARS["1h"] > FORBIDDEN_LIVE_STRUCTURE_LIMIT


def test_refresh_refuses_limit_800(tmp_path: Path):
    rep = refresh_symbol(
        symbol="ETHUSDT",
        timeframes=("1h", "4h", "1w"),
        indicator_db=tmp_path / "slice.sqlite",
        limit=800,
        source="binance",
    )
    assert all(s.get("error") == "structure_history_too_short" for s in rep["series"])


def test_singlebook_writes_open_books_and_expires(tmp_path: Path):
    """Single-book must track open_books so max-hold can fire (was multitrade-only)."""
    con = _state_conn(tmp_path / "state.sqlite")
    entry = 1_700_000_000_000
    hold = 6
    _insert_open_book(
        con,
        book_id=f"{entry}_1_1",
        side=1,
        entry_bar_ms=entry,
        max_hold_bars=hold,
        qty=0.01,
        tp_pct=0.01,
        sl_pct=0.02,
        book_idx=1,
        order_id="oid",
    )
    assert _expired_books(con, bar_ms=entry + 5 * 3_600_000, timeframe="1h") == []
    exp = _expired_books(con, bar_ms=entry + hold * 3_600_000, timeframe="1h")
    assert len(exp) == 1
    assert exp[0]["book_id"] == f"{entry}_1_1"
    assert exp[0]["qty"] == 0.01
    con.close()


def test_required_completed_htf_open_ms_15m():
    # 15m bar open 14:15 → only sees 1h bar open 13:00 (completion join).
    bar = int(pd.Timestamp("2026-08-05 14:15:00", tz="UTC").value // 10**6)
    need = _required_completed_htf_open_ms(bar, "1h")
    assert need == int(pd.Timestamp("2026-08-05 13:00:00", tz="UTC").value // 10**6)


def test_structure_ready_refuses_refresh_errors_and_shallow_slice(tmp_path: Path):
    import sqlite3

    db = tmp_path / "slice.sqlite"
    con = sqlite3.connect(str(db))
    con.execute(
        "CREATE TABLE series (symbol TEXT, timeframe TEXT, source TEXT, "
        "n_bars INTEGER, computed_at_ms INTEGER)"
    )
    con.execute(
        "CREATE TABLE bar_features (symbol TEXT, timeframe TEXT, source TEXT, ts_ms INTEGER)"
    )
    # Shallow 15m + missing HTF depth → not ready.
    con.execute(
        "INSERT INTO series VALUES ('ETHUSDT','15m','binance',100,1)"
    )
    bar = int(pd.Timestamp("2026-08-05 14:00:00", tz="UTC").value // 10**6)
    con.execute(
        "INSERT INTO bar_features VALUES ('ETHUSDT','15m','binance',?)", (bar,)
    )
    con.commit()
    con.close()

    ok, why = _structure_ready_for_decide(
        db,
        symbol="ETHUSDT",
        timeframe="15m",
        bar_open_ms=bar,
        source="binance",
        refresh_errors=[{"timeframe": "1h", "error": "structure_history_too_short"}],
    )
    assert ok is False
    assert why == "structure_refresh_errors"

    ok2, why2 = _structure_ready_for_decide(
        db,
        symbol="ETHUSDT",
        timeframe="15m",
        bar_open_ms=bar,
        source="binance",
        refresh_errors=None,
    )
    assert ok2 is False
    assert why2 == "structure_depth_insufficient"


def test_timeframes_needing_refresh_only_decision_when_htf_covered(tmp_path: Path):
    """Mid-hour 15m tip lag should not force 1h/4h full rebuild."""
    import sqlite3

    from llm2.live.micro_runner import _timeframes_needing_structure_refresh

    db = tmp_path / "slice.sqlite"
    con = sqlite3.connect(str(db))
    con.execute(
        "CREATE TABLE series (symbol TEXT, timeframe TEXT, source TEXT, "
        "n_bars INTEGER, computed_at_ms INTEGER)"
    )
    con.execute(
        "CREATE TABLE bar_features (symbol TEXT, timeframe TEXT, source TEXT, ts_ms INTEGER)"
    )
    # Deep series.
    for tf, n in (("15m", 10_000), ("1h", 6_000), ("4h", 3_000)):
        con.execute(
            "INSERT INTO series VALUES ('ETHUSDT',?,?,?,1)",
            (tf, "binance", n),
        )
    # Tips: 15m stuck at 16:00, 1h at 15:00, 4h at 12:00 — enough for bar 16:15.
    t_16_00 = int(pd.Timestamp("2026-08-05 16:00:00", tz="UTC").value // 10**6)
    t_16_15 = int(pd.Timestamp("2026-08-05 16:15:00", tz="UTC").value // 10**6)
    t_15_00 = int(pd.Timestamp("2026-08-05 15:00:00", tz="UTC").value // 10**6)
    t_12_00 = int(pd.Timestamp("2026-08-05 12:00:00", tz="UTC").value // 10**6)
    con.execute(
        "INSERT INTO bar_features VALUES ('ETHUSDT','15m','binance',?)", (t_16_00,)
    )
    con.execute(
        "INSERT INTO bar_features VALUES ('ETHUSDT','1h','binance',?)", (t_15_00,)
    )
    con.execute(
        "INSERT INTO bar_features VALUES ('ETHUSDT','4h','binance',?)", (t_12_00,)
    )
    con.commit()
    con.close()

    need = _timeframes_needing_structure_refresh(
        db,
        symbol="ETHUSDT",
        timeframe="15m",
        bar_open_ms=t_16_15,
        source="binance",
    )
    assert need == ("15m",)
