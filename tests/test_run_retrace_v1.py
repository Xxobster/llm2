"""Causal run_retrace feature space refuses orange columns."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.features.run_retrace_v1 import build_causal_run_retrace


def test_build_causal_run_retrace_empty_legs_safe():
    # Minimal frame — structure may have no legs; must not raise.
    n = 120
    idx = pd.date_range("2020-01-01", periods=n, freq="h", tz="UTC")
    close = 100.0 + np.cumsum(np.random.default_rng(0).normal(0, 0.1, n))
    ohlcv = pd.DataFrame(
        {
            "open": close,
            "high": close + 0.2,
            "low": close - 0.2,
            "close": close,
            "volume": 1.0,
        },
        index=idx,
    )
    out = build_causal_run_retrace(ohlcv, symbol="ETHUSDT", timeframe="1h")
    assert isinstance(out, pd.DataFrame)
    assert len(out) == n
    assert "oracle_leaky" not in out.columns
    assert "last_retrace_pct" not in out.columns
