"""Causal hunt-005 signals must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog_b import IDEA_IDS_B, signals_b


def _ohlcv(n: int = 900, seed: int = 9) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": close * 1.002,
            "low": close * 0.998,
            "close": close,
            "volume": rng.random(n) * 100 + 1,
        },
        index=idx,
    )


def test_eight_ideas():
    assert len(IDEA_IDS_B) == 8


def test_prefix_orb_and_nr7():
    df = _ohlcv(1500)
    full = signals_b(df, "1h")
    prefix = signals_b(df.iloc[:-80], "1h")
    for name in ("utc_orb_follow", "nr7_break", "adx_rising"):
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)


def test_sparse_cvd_prefix_and_not_always_on():
    from llm2.ml_lab.idea_catalog_b import cvd_slope, cvd_slope_cross, signals_b5

    df = _ohlcv(1500)
    always = cvd_slope(df)
    cross = cvd_slope_cross(df)
    assert int(np.count_nonzero(cross)) < int(np.count_nonzero(always))
    full = signals_b5(df, "1h")
    prefix = signals_b5(df.iloc[:-80], "1h")
    for name in ("cvd_slope_cross", "cvd_z_fire"):
        np.testing.assert_allclose(full[name][:-80], prefix[name], rtol=1e-9, atol=1e-9)
