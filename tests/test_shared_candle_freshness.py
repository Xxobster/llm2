"""Shared candle tip must cover the latest closed bar, not only tip age."""

from __future__ import annotations

import pandas as pd

from llm2.live.refresh_structure import (
    _latest_closed_bar_open_ms,
    _shared_is_fresh_enough,
)


def test_shared_is_fresh_enough_requires_latest_closed_coverage():
    # At 15:39 the 15:30 bar is still forming; latest closed open is 15:15.
    now = int(pd.Timestamp("2026-08-05 15:39:00", tz="UTC").value // 10**6)
    need = _latest_closed_bar_open_ms("15m", now_ms=now)
    assert need == int(pd.Timestamp("2026-08-05 15:15:00", tz="UTC").value // 10**6)

    ok = pd.DataFrame({"ts_ms": [need - 15 * 60_000, need]})
    assert _shared_is_fresh_enough(ok, "15m", now_ms=now) is True

    # Stuck one bar behind latest closed.
    behind = pd.DataFrame({"ts_ms": [need - 30 * 60_000, need - 15 * 60_000]})
    assert _shared_is_fresh_enough(behind, "15m", now_ms=now) is False


def test_merge_ohlcv_tip_keeps_deep_history():
    from llm2.live.refresh_structure import _merge_ohlcv_tip

    base_ts = [1_000, 2_000, 3_000]
    tip_ts = [3_000, 4_000]
    base = pd.DataFrame(
        {"ts_ms": base_ts, "close": [1.0, 2.0, 3.0]},
        index=pd.to_datetime(base_ts, unit="ms", utc=True),
    )
    tip = pd.DataFrame(
        {"ts_ms": tip_ts, "close": [3.5, 4.0]},
        index=pd.to_datetime(tip_ts, unit="ms", utc=True),
    )
    merged = _merge_ohlcv_tip(base, tip)
    assert list(merged["ts_ms"].astype(int)) == [1_000, 2_000, 3_000, 4_000]
    assert float(merged.loc[merged["ts_ms"] == 3_000, "close"].iloc[0]) == 3.5
