"""Causal 30-idea catalog must ignore later bars."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.ml_lab.idea_catalog import IDEA_IDS, signals_from_ohlcv


def _ohlcv(n: int = 900, seed: int = 5) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    r = rng.normal(0.0, 0.01, size=n)
    close = 100.0 * np.exp(np.cumsum(r))
    high = close * (1.0 + rng.random(n) * 0.004)
    low = close * (1.0 - rng.random(n) * 0.004)
    idx = pd.date_range("2019-01-01", periods=n, freq="1h", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": high,
            "low": low,
            "close": close,
            "volume": rng.random(n) * 1000 + 10,
        },
        index=idx,
    )


def test_catalog_has_thirty_ideas():
    assert len(IDEA_IDS) == 30


def test_ema_stack_never_short():
    sig = signals_from_ohlcv(_ohlcv(), "1h")["power_ema_stack_long"]
    assert float(np.min(sig)) >= 0.0


def test_prefix_invariance_selected_ideas():
    df = _ohlcv(1200)
    full = signals_from_ohlcv(df, "1h")
    prefix = signals_from_ohlcv(df.iloc[:-50], "1h")
    for name in (
        "power_donchian_er",
        "power_ema_stack_long",
        "surf_bb_band",
        "mix_hurst_switch",
        "mix_er_blend",
    ):
        a = full[name][:-50]
        b = prefix[name]
        np.testing.assert_allclose(a, b, rtol=1e-9, atol=1e-9)


def test_last_bar_does_not_change_early_signals():
    df = _ohlcv(800)
    df2 = df.copy()
    df2.iloc[-1, df2.columns.get_loc("close")] *= 1.05
    df2.iloc[-1, df2.columns.get_loc("high")] *= 1.05
    a = signals_from_ohlcv(df, "1h")["surf_keltner_band"]
    b = signals_from_ohlcv(df2, "1h")["surf_keltner_band"]
    np.testing.assert_allclose(a[:-30], b[:-30], rtol=1e-9, atol=1e-9)
