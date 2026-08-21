"""Causal next-retrace labels: knowable only after successor leg confirms."""

from __future__ import annotations

import numpy as np
import pytest

from llm2.labels.next_retrace import (
    build_next_retrace_leg_table,
    build_next_retrace_sparse_frame,
)


@pytest.mark.parametrize("symbol", ["ETHUSDT"])
def test_next_retrace_known_after_decision(symbol: str):
    tab = build_next_retrace_leg_table(symbol, "1h")
    assert len(tab) > 50
    assert (tab["known_ts_ms"] > tab["decision_ts_ms"]).all()
    assert np.isfinite(tab["next_retrace_pct"]).all()
    assert set(tab["leg_dir"].unique()).issubset({-1, 1})


def test_sparse_frame_index_utc():
    frame = build_next_retrace_sparse_frame("ETHUSDT", "1h")
    assert str(frame.index.tz) == "UTC"
    assert "next_retrace_pct" in frame.columns
