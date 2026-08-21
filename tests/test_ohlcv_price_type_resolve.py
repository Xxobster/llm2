"""``last`` and ``last_price`` are one series, so loading must return both.

``price_type`` is not part of the ``market_ohlcv`` primary key, so a bar exists once
and the two labels are disjoint slices split wherever the downloader changed its
label. The previous rule picked the freshest single label, which on ETHUSDT 1h threw
away the 49,807 bars covering 2020-01 to 2025-09.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from llm2.data.loader import _resolve_price_types


def _seed(con: sqlite3.Connection) -> None:
    con.execute(
        "CREATE TABLE market_ohlcv("
        "source TEXT, symbol TEXT, timeframe TEXT, ts_ms INTEGER, "
        "open REAL, high REAL, low REAL, close REAL, volume REAL, "
        "price_type TEXT, is_complete INTEGER)"
    )
    # Dense but stale last_price, then a short current last continuing the same series.
    for i in range(100):
        con.execute(
            "INSERT INTO market_ohlcv VALUES("
            "'binance','ETHUSDT','1h',?,?,?,?,?,?, 'last_price',1)",
            (1_600_000_000_000 + i * 3_600_000, 1, 1, 1, 1, 1),
        )
    for i in range(10):
        con.execute(
            "INSERT INTO market_ohlcv VALUES("
            "'binance','ETHUSDT','1h',?,?,?,?,?,?, 'last',1)",
            (1_780_000_000_000 + i * 3_600_000, 1, 1, 1, 1, 1),
        )
    con.commit()


def test_both_last_trade_labels_are_treated_as_one_series(tmp_path: Path):
    db = tmp_path / "m.sqlite"
    con = sqlite3.connect(str(db))
    _seed(con)
    chosen = _resolve_price_types(con, symbol="ETHUSDT", timeframe="1h", source="binance")
    con.close()
    assert set(chosen) == {"last", "last_price"}


def test_mark_price_is_never_mixed_into_the_last_trade_series(tmp_path: Path):
    db = tmp_path / "m.sqlite"
    con = sqlite3.connect(str(db))
    _seed(con)
    for i in range(50):
        con.execute(
            "INSERT INTO market_ohlcv VALUES("
            "'binance','ETHUSDT','1h',?,?,?,?,?,?, 'mark_price',1)",
            (1_900_000_000_000 + i * 3_600_000, 1, 1, 1, 1, 1),
        )
    con.commit()
    chosen = _resolve_price_types(con, symbol="ETHUSDT", timeframe="1h", source="binance")
    con.close()
    assert "mark_price" not in chosen


def test_explicit_last_does_not_join_stale_last_price(tmp_path: Path, monkeypatch):
    db = tmp_path / "m.sqlite"
    con = sqlite3.connect(str(db))
    _seed(con)
    con.close()
    import llm2.data.loader as loader

    monkeypatch.setattr(loader, "MARKET_DB", db)
    df = loader.load_ohlcv("ETHUSDT", "1h", price_type="last")
    assert df.attrs["price_type"] == "last"
    assert int(df["ts_ms"].iloc[0]) >= 1_780_000_000_000
