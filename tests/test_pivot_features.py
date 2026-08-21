"""Lightweight unit tests for pivot feature packs."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.pivot.features.packs import build_feature_frame


def test_feature_packs_shapes():
    n = 100
    idx = pd.date_range("2024-01-01", periods=n, freq="15min", tz="UTC")
    rng = np.random.default_rng(0)
    close = 100 + np.cumsum(rng.normal(0, 0.1, n))
    df = pd.DataFrame(
        {
            "open": close,
            "high": close + 0.2,
            "low": close - 0.2,
            "close": close,
            "volume": rng.uniform(1, 5, n),
        },
        index=idx,
    )
    for pack in (
        "price_vol",
        "price_vol_mom",
        "price_vol_mom_phys",
        "full",
        "level_focus",
        "vsa_proxy",
        "level_vsa",
        "level_strong",
    ):
        f = build_feature_frame(df, pack=pack)
        assert len(f) == n
        assert f.shape[1] >= 5
