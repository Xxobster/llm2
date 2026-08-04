"""Tests for causal wave metrics: prefix invariance, warmup inheritance, capitulation."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.wave import causal_wave
from llm2.diagnostics.wave_mining_guard import NonCausalWaveError
from llm2.diagnostics.wavemetrics import build_causal_metrics, detect_triggers

PERIOD = 20.0


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


def _cyclic_price(n: int, *, period: float = PERIOD, amplitude: float = 0.04, noise: float = 0.003, seed: int = 0) -> pd.Series:
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    wave = amplitude * np.sin(2 * np.pi * t / period)
    walk = np.cumsum(rng.normal(0, noise, size=n))
    return pd.Series(np.exp(4.0 + wave + walk), index=_index(n))


def _volume(n: int, seed: int = 1) -> pd.Series:
    rng = np.random.default_rng(seed)
    return pd.Series(np.abs(rng.normal(100.0, 20.0, size=n)), index=_index(n))


# --------------------------------------------------------------------------------------
# Prefix invariance
# --------------------------------------------------------------------------------------


def test_metrics_are_prefix_invariant():
    """Every column is built from backward-looking operations only: truncating the tail
    must not change a single earlier value."""
    n = 4000
    close = _cyclic_price(n)
    volume = _volume(n)

    full = build_causal_metrics(close, volume, PERIOD)
    cut = 3000
    truncated = build_causal_metrics(close.iloc[:cut], volume.iloc[:cut], PERIOD)

    shared_cols = [c for c in full.columns if c in truncated.columns]
    for col in shared_cols:
        pd.testing.assert_series_equal(
            full[col].iloc[:cut], truncated[col], check_names=False, atol=1e-10
        )


def test_metrics_are_prefix_invariant_without_volume():
    n = 3000
    close = _cyclic_price(n, seed=2)
    full = build_causal_metrics(close, None, PERIOD)
    cut = 2200
    truncated = build_causal_metrics(close.iloc[:cut], None, PERIOD)
    for col in full.columns:
        pd.testing.assert_series_equal(
            full[col].iloc[:cut], truncated[col], check_names=False, atol=1e-10
        )


# --------------------------------------------------------------------------------------
# Warmup inheritance
# --------------------------------------------------------------------------------------


def test_wave_columns_inherit_causal_wave_warmup_and_are_never_backfilled():
    n = 3000
    close = _cyclic_price(n, seed=3)
    metrics = build_causal_metrics(close, None, PERIOD)

    log_c = np.log(close)
    wave, amp, phase = causal_wave(log_c, PERIOD)
    warmup_mask = wave.isna()
    warmup_bars = int(warmup_mask.sum())
    assert warmup_bars > 0

    assert metrics["wave"].iloc[:warmup_bars].isna().all()
    assert metrics["amp"].iloc[:warmup_bars].isna().all()
    assert metrics["phase"].iloc[:warmup_bars].isna().all()
    # Never backfilled: the mask must line up exactly with causal_wave's own, not be shorter.
    pd.testing.assert_series_equal(metrics["wave"].isna(), warmup_mask, check_names=False)
    assert metrics["wave"].iloc[warmup_bars:].notna().any()


def test_amp_pct_rank_needs_its_own_longer_window_and_still_never_backfills():
    """A metric with a wider intrinsic window (trailing 500-bar rank) stays NaN longer than
    the raw wave warmup, but never earlier than it, and never with a seeded/backfilled value."""
    n = 3000
    close = _cyclic_price(n, seed=4)
    metrics = build_causal_metrics(close, None, PERIOD)

    wave_warmup = int(metrics["wave"].isna().sum())
    rank_warmup = int(metrics["amp_pct_rank_500"].isna().sum())
    assert rank_warmup >= wave_warmup
    # Nothing before the wave itself exists can possibly be non-NaN in a derived rank.
    assert metrics.loc[metrics["wave"].isna(), "amp_pct_rank_500"].isna().all()


# --------------------------------------------------------------------------------------
# Guard
# --------------------------------------------------------------------------------------


def test_wavemetrics_module_has_no_analytic_wave_reference():
    import llm2.diagnostics.wavemetrics as wavemetrics

    assert "analytic_wave" not in vars(wavemetrics)


def test_forbid_analytic_import_raises_when_present():
    from llm2.diagnostics.wave_mining_guard import forbid_analytic_import

    with pytest.raises(NonCausalWaveError):
        forbid_analytic_import({"__name__": "fake.mining.module", "analytic_wave": lambda: None})


# --------------------------------------------------------------------------------------
# Capitulation definition
# --------------------------------------------------------------------------------------


def _base_metrics(n: int = 200) -> pd.DataFrame:
    idx = _index(n)
    return pd.DataFrame(
        {
            "phase": np.zeros(n),
            "phase_velocity": np.zeros(n),
            "wave": np.zeros(n),
            "energy_pct_rank_500": np.full(n, 50.0),
            "volume_pct_rank_500": np.full(n, 50.0),
        },
        index=idx,
    )


def test_capitulation_requires_energy_and_volume_and_peak_turn_together():
    m = _base_metrics()
    peak_bar = 100
    half_period = int(round(PERIOD / 2))

    # Phase velocity rising then turning non-positive exactly at peak_bar.
    m.loc[m.index[peak_bar - 2], "phase_velocity"] = 0.05
    m.loc[m.index[peak_bar - 1], "phase_velocity"] = 0.10
    m.loc[m.index[peak_bar], "phase_velocity"] = -0.02

    # Wave was rising into the turn over the preceding half-period -> signed "up".
    m.loc[m.index[peak_bar - half_period], "wave"] = -1.0
    m.loc[m.index[peak_bar], "wave"] = 1.0

    m.loc[m.index[peak_bar], "energy_pct_rank_500"] = 95.0
    m.loc[m.index[peak_bar], "volume_pct_rank_500"] = 95.0

    triggers = detect_triggers(m, period=PERIOD)
    assert triggers["peak_detect"].iloc[peak_bar]
    assert triggers["capitulation"].iloc[peak_bar]
    assert triggers["capitulation_up"].iloc[peak_bar]
    assert not triggers["capitulation_down"].iloc[peak_bar]


def test_capitulation_does_not_fire_without_volume_confirmation():
    m = _base_metrics()
    peak_bar = 100
    m.loc[m.index[peak_bar - 2], "phase_velocity"] = 0.05
    m.loc[m.index[peak_bar - 1], "phase_velocity"] = 0.10
    m.loc[m.index[peak_bar], "phase_velocity"] = -0.02
    m.loc[m.index[peak_bar], "energy_pct_rank_500"] = 95.0
    m.loc[m.index[peak_bar], "volume_pct_rank_500"] = 40.0  # NOT in the top decile

    triggers = detect_triggers(m, period=PERIOD)
    assert triggers["peak_detect"].iloc[peak_bar]
    assert not triggers["capitulation"].iloc[peak_bar]


def test_capitulation_does_not_fire_without_a_peak_turn():
    m = _base_metrics()
    peak_bar = 100
    # Energy and volume both extreme, but phase velocity is still rising (no turn).
    m.loc[m.index[peak_bar - 1], "phase_velocity"] = 0.05
    m.loc[m.index[peak_bar], "phase_velocity"] = 0.10
    m.loc[m.index[peak_bar], "energy_pct_rank_500"] = 99.0
    m.loc[m.index[peak_bar], "volume_pct_rank_500"] = 99.0

    triggers = detect_triggers(m, period=PERIOD)
    assert not triggers["peak_detect"].iloc[peak_bar]
    assert not triggers["capitulation"].iloc[peak_bar]


def test_threshold_grid_fires_on_upward_phase_crossing():
    m = _base_metrics()
    m["phase"] = -3.0
    cross_bar = 50
    m.loc[m.index[cross_bar - 1], "phase"] = 1.5
    m.loc[m.index[cross_bar], "phase"] = 2.0  # crosses up through 1.8

    triggers = detect_triggers(m, period=PERIOD, phase_thresholds=(1.8,))
    assert triggers["threshold_up_1p8"].iloc[cross_bar]
    assert not triggers["threshold_up_1p8"].iloc[cross_bar - 1]
