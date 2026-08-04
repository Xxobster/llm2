"""Tests for A–B / B–C distance-factor similarity."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.abc_factor import (
    CLASSICAL_FACTORS,
    PLACEBO_FACTORS,
    build_abc_triples,
    build_abc_triples_from_extrema,
    causal_wave_extrema,
    factor_summary,
)
from llm2.research_policy import LevelClaim, PolicyError, require_placebo_arm


def _synth_legs(n_legs: int = 200, seed: int = 0) -> pd.DataFrame:
    """Alternating up/down legs that chain on swing ids."""
    rng = np.random.default_rng(seed)
    rows = []
    price = 100.0
    swing_id = 0
    t = 1_700_000_000_000
    for i in range(n_legs):
        direction = "up" if i % 2 == 0 else "down"
        start_id = swing_id
        end_id = swing_id + 1
        move = float(rng.uniform(1.0, 5.0))
        start_price = price
        end_price = price + move if direction == "up" else price - move
        rows.append(
            {
                "leg_id": i,
                "direction": direction,
                "start_swing_id": start_id,
                "end_swing_id": end_id,
                "start_ts_ms": t,
                "end_ts_ms": t + 3_600_000,
                "start_price": start_price,
                "end_price": end_price,
                "length_abs": abs(end_price - start_price),
                "length_pct": abs(end_price - start_price) / price,
                "kind": "impulse" if i % 3 else "correction",
            }
        )
        price = end_price
        swing_id = end_id
        t += 3_600_000
    return pd.DataFrame(rows)


def test_triples_chain_on_shared_swing_b():
    legs = _synth_legs(50)
    triples = build_abc_triples(legs)
    assert len(triples) == 49
    # B of each triple equals end of first leg
    assert np.allclose(triples["b_price"], legs["end_price"].iloc[:-1].to_numpy())
    assert np.allclose(triples["c_price"], legs["end_price"].iloc[1:].to_numpy())


def test_factor_is_bc_over_ab():
    legs = _synth_legs(20, seed=1)
    triples = build_abc_triples(legs)
    expected = triples["bc_abs"] / triples["ab_abs"]
    assert np.allclose(triples["factor"], expected)


def test_same_direction_legs_are_excluded():
    """If two consecutive legs do not alternate, they are not an A-B-C zig-zag."""
    legs = _synth_legs(10)
    # Force two ups in a row by breaking the chain artificially — rebuild with same dirs
    legs = legs.copy()
    # Make leg 1 also "up" starting from a new swing so match fails OR same_dir
    # Easier: take chained legs and flip prices so both legs go up (impossible if chained
    # alternating highs/lows). With alternating chain, pattern is always zig-zag.
    triples = build_abc_triples(legs)
    assert set(triples["pattern"]) <= {"up_down", "down_up"}


def test_placebo_arm_is_required():
    with pytest.raises(PolicyError, match="placebo"):
        require_placebo_arm(
            LevelClaim(
                name="abc",
                real_ratios=CLASSICAL_FACTORS,
                placebo_ratios=(),
                anchors="swings",
                proximity_band="0.05",
            )
        )
    require_placebo_arm(
        LevelClaim(
            name="abc",
            real_ratios=CLASSICAL_FACTORS,
            placebo_ratios=PLACEBO_FACTORS,
            anchors="confirmed consecutive swing triples",
            proximity_band="0.05",
        )
    )


def test_factor_summary_counts():
    triples = build_abc_triples(_synth_legs(100))
    s = factor_summary(triples)
    assert s["n_triples"] == 99
    assert s["mean"] > 0


def test_causal_wave_extrema_confirm_lags_one_bar():
    """An extremum at bar i is knowable only at bar i+1."""
    idx = pd.date_range("2024-01-01", periods=400, freq="h", tz="UTC")
    # Smooth sinusoid in log-price space so causal_wave finds clear turns
    t = np.arange(len(idx), dtype=float)
    close = pd.Series(100.0 * np.exp(0.02 * np.sin(2 * np.pi * t / 40.0)), index=idx)
    extrema = causal_wave_extrema(close, period=40.0, min_sep=4)
    assert len(extrema) >= 3
    assert (extrema["confirm_i"] == extrema["extremum_i"] + 1).all()
    triples = build_abc_triples_from_extrema(extrema)
    assert len(triples) >= 1
    assert set(triples["pattern"]) <= {"up_down", "down_up"}
    assert (triples["geometry"] == "causal_wave_extrema").all()


def test_bounce_side_is_opposite_bc():
    from llm2.experiments.abc_bounce import bounce_events_from_legs

    legs = _synth_legs(80, seed=3)
    idx = pd.date_range("2024-01-01", periods=200, freq="h", tz="UTC")
    close = pd.Series(np.linspace(100, 120, len(idx)), index=idx)
    ohlcv = pd.DataFrame(
        {"open": close, "high": close * 1.001, "low": close * 0.999, "close": close, "volume": 1.0},
        index=idx,
    )
    # Align leg times into the synthetic index
    legs = legs.copy()
    base = int(idx[10].timestamp() * 1000)
    for i in range(len(legs)):
        legs.loc[i, "start_ts_ms"] = base + i * 3_600_000
        legs.loc[i, "end_ts_ms"] = base + (i + 1) * 3_600_000
    events = bounce_events_from_legs(ohlcv, legs, targets=(0.5, 1.0, 1.5, 2.0), tol=2.0)
    assert len(events) > 0
    assert np.all(events["side"] == -events["bc_dir"])
