"""CASM-A + phase router: three frozen ideas, prefix-stable, signed signals."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_casm import IDEA_IDS_CASM, phase_router, signals_casm


def _ohlcv(n: int = 1400, seed: int = 19) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    op = np.empty_like(close)
    op[0] = close[0]
    op[1:] = close[:-1]
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    oi = np.cumsum(rng.normal(0.0, 0.002, size=n))
    fund = np.sin(np.arange(n) / 40.0) * 0.0008
    return pd.DataFrame(
        {
            "open": op,
            "high": np.maximum(op, close) * 1.004,
            "low": np.minimum(op, close) * 0.996,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
            "oi_logret_1": np.concatenate([[np.nan], np.diff(oi)]),
            "funding_rate": fund,
        },
        index=idx,
    )


def test_three_ideas():
    assert IDEA_IDS_CASM == ("casm_healthy_follow", "casm_exhaust_fade", "phase_router")


def test_signals_are_signed():
    sigs = signals_casm(_ohlcv(), "1h", symbol="ETHUSDT")
    assert set(sigs) == set(IDEA_IDS_CASM)
    for name, arr in sigs.items():
        uniq = set(np.unique(arr[np.isfinite(arr)]))
        assert uniq <= {-1.0, 0.0, 1.0}, name


def test_router_silent_without_hilbert_and_state():
    df = _ohlcv(400, seed=1)
    df["oi_logret_1"] = 0.0
    df["funding_rate"] = 0.0
    out = phase_router(df, "1h", symbol="ETHUSDT")
    assert np.all(out == 0.0)


def test_prefix_injected_oi_funding():
    df = _ohlcv(1500)
    full = signals_casm(df, "1h", symbol="ETHUSDT")
    prefix = signals_casm(df.iloc[:-80], "1h", symbol="ETHUSDT")
    for name in IDEA_IDS_CASM:
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-8, atol=1e-8)
