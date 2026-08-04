"""Feature leakage guard smoke tests."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.features.guard import build_features_for_guard, run_audit_for_space
from llm2.features.ohlcv_v1 import build_ohlcv_v1


def _ohlcv(n: int = 300) -> pd.DataFrame:
    idx = pd.date_range("2023-01-01", periods=n, freq="1h", tz="UTC")
    rng = np.random.default_rng(1)
    c = 100 + np.cumsum(rng.normal(0, 0.3, n))
    return pd.DataFrame(
        {
            "open": c,
            "high": c + 0.5,
            "low": c - 0.5,
            "close": c,
            "volume": rng.uniform(1, 10, n),
        },
        index=idx,
    )


def test_build_features_for_guard_matches_ohlcv_v1():
    df = _ohlcv()
    a = build_ohlcv_v1(df)
    b = build_features_for_guard(df, interval="1h", space="ohlcv_v1")
    pd.testing.assert_frame_equal(a, b)


def test_prefix_invariance_ohlcv_v1():
    df = _ohlcv()
    cut = 200
    full = build_ohlcv_v1(df)
    partial = build_ohlcv_v1(df.iloc[:cut])
    shared_cols = full.columns.intersection(partial.columns)
    pd.testing.assert_frame_equal(
        full.iloc[: cut - 1][shared_cols],
        partial.iloc[: cut - 1][shared_cols],
        check_dtype=False,
        rtol=1e-5,
        atol=1e-8,
    )


def test_run_audit_for_space_integration():
    """Requires botsgeneral leakage package (editable-installed in LLM2 venv)."""
    try:
        from leakage.ensure_source import prefer_botsgeneral_leakage

        prefer_botsgeneral_leakage()
        import leakage
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"leakage unavailable: {exc}")

    assert "botsgeneral" in str(leakage.__file__).replace("\\", "/")
    res = run_audit_for_space(_ohlcv(800), interval="1h", space="ohlcv_v1", cuts=2)
    assert res["passed"] is True
    assert res["ok"] is True
