"""Live tip signal must equal the research occurrence bit (shared-code parity)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagonal_sr.events import build_event_pack
from llm2.diagonal_sr.live_signal import (
    LIMIT_MOVE_MAX,
    LIMIT_MOVE_MIN,
    event_side,
    limit_price,
    tip_signal,
)


def _synthetic_ohlcv(n: int = 900, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    idx = pd.date_range("2024-01-01", periods=n, freq="1h", tz="UTC")
    # Trending base with an oscillation so swing highs/lows and channels exist.
    base = 100.0 + np.cumsum(rng.normal(0.0, 0.4, n)) + 8.0 * np.sin(np.arange(n) / 17.0)
    high = base + np.abs(rng.normal(0.6, 0.3, n))
    low = base - np.abs(rng.normal(0.6, 0.3, n))
    close = base + rng.normal(0.0, 0.2, n)
    open_ = np.concatenate([[base[0]], close[:-1]])
    high = np.maximum.reduce([high, open_, close])
    low = np.minimum.reduce([low, open_, close])
    return pd.DataFrame(
        {
            "open": open_,
            "high": high,
            "low": low,
            "close": close,
            "volume": rng.uniform(50, 150, n),
        },
        index=idx,
    )


@pytest.mark.parametrize(
    "event",
    ["bounce_upper", "bounce_lower", "channel_walk_long", "channel_walk_short"],
)
def test_tip_signal_matches_research_occurrence(event: str) -> None:
    ohlcv = _synthetic_ohlcv()
    pack = build_event_pack(ohlcv, horizon=4, generation="A")
    occ = pack.occurrence[event].to_numpy(dtype=float)

    n = len(ohlcv)
    checked = 0
    for k in range(n - 40, n):
        sig = tip_signal(ohlcv.iloc[: k + 1], event=event, generation="A")
        if sig.nan_cols:
            continue
        assert sig.fires == bool(occ[k] >= 0.5), f"bar {k} live={sig.fires} research={occ[k]}"
        checked += 1
    assert checked >= 30


def test_limit_price_clip_and_side() -> None:
    assert event_side("bounce_upper") == -1
    assert event_side("bounce_lower") == 1
    # Tiny volatility clamps up to the floor; huge volatility clamps to the cap.
    assert limit_price(100.0, 1e-6, is_short=True) == pytest.approx(100.0 * (1 + LIMIT_MOVE_MIN))
    assert limit_price(100.0, 9.0, is_short=False) == pytest.approx(100.0 * (1 - LIMIT_MOVE_MAX))
    # Short entry sits above the close, long entry below.
    assert limit_price(100.0, 0.01, is_short=True) > 100.0
    assert limit_price(100.0, 0.01, is_short=False) < 100.0


def test_tip_signal_refuses_short_history() -> None:
    with pytest.raises(ValueError):
        tip_signal(_synthetic_ohlcv(n=30), event="bounce_upper", generation="A")


def test_tip_signal_reports_nan_geometry_instead_of_filling() -> None:
    ohlcv = _synthetic_ohlcv(n=70)
    sig = tip_signal(ohlcv, event="channel_walk_long", generation="A")
    # Either geometry is available, or it is reported missing — never invented.
    if sig.nan_cols:
        assert not sig.fires
        assert not sig.ok
    else:
        assert np.isfinite(sig.limit_px)
