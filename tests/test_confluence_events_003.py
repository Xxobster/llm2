"""Generation-003 Supertrend / Ichimoku / Commodity Channel Index regimes."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.confluence.events import (
    EVENT_IDS,
    EVENT_IDS_002,
    EVENT_IDS_003,
    build_event_pack,
    build_known_now_features,
)


def _trend(n: int = 500, seed: int = 3) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    close = 100.0 + np.cumsum(rng.normal(0.05, 0.4, size=n))
    high = close + rng.uniform(0.05, 0.4, size=n)
    low = close - rng.uniform(0.05, 0.4, size=n)
    idx = pd.date_range("2023-01-01", periods=n, freq="15min", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": high,
            "low": low,
            "close": close,
            "volume": rng.uniform(10, 40, size=n),
        },
        index=idx,
    )


def test_001_002_unchanged_without_003_flag():
    pack = build_event_pack(_trend(300), horizon=4, include_002=True, include_003=False)
    assert list(pack.labels.columns) == list(EVENT_IDS + EVENT_IDS_002)


def test_003_columns_present_with_flag():
    pack = build_event_pack(_trend(400), horizon=4, include_002=False, include_003=True)
    assert list(pack.labels.columns) == list(EVENT_IDS + EVENT_IDS_003)
    assert pack.labels.iloc[-4:].isna().all().all()


def test_003_regimes_fire_on_trending_series():
    pack = build_event_pack(_trend(), horizon=8, include_003=True)
    for eid in EVENT_IDS_003:
        n = int(np.nansum(pack.labels[eid].to_numpy()))
        assert n >= 1, eid


def test_003_features_prefix_invariant():
    df = _trend(600)
    full = build_known_now_features(df)
    trunc = build_known_now_features(df.iloc[:400])
    for c in (
        "supertrend_dir",
        "supertrend_dist",
        "ichimoku_tk_spread",
        "ichimoku_tk_bull",
        "cci_20",
        "cci_oversold",
        "cci_overbought",
    ):
        a = full[c].iloc[:400].to_numpy(dtype=float)
        b = trunc[c].to_numpy(dtype=float)
        both = np.isfinite(a) & np.isfinite(b)
        assert both.sum() >= 20, c
        np.testing.assert_allclose(a[both], b[both], rtol=1e-9, atol=1e-9, err_msg=c)


def test_supertrend_mutually_exclusive_at_h():
    pack = build_event_pack(_trend(), horizon=4, include_003=True)
    up = pack.labels["supertrend_up_at_h"].to_numpy(dtype=float)
    dn = pack.labels["supertrend_down_at_h"].to_numpy(dtype=float)
    both = np.isfinite(up) & np.isfinite(dn)
    assert not np.any((up[both] > 0.5) & (dn[both] > 0.5))
