"""Tests for the amplitude-event study: trailing percentiles, vol-clustering, group delay."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.waveevent import (
    detect_amplitude_events,
    group_delay_bars,
    run_amplitude_event_study,
    trailing_move_control_events,
)
from llm2.diagnostics.wavemetrics import build_causal_metrics
from llm2.research_policy import PolicyError

PERIOD = 20.0


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


def _make_ohlcv(close: np.ndarray, volume: np.ndarray | None = None) -> pd.DataFrame:
    idx = _index(close.size)
    vol = volume if volume is not None else np.full(close.size, 100.0)
    return pd.DataFrame(
        {"open": close, "high": close * 1.001, "low": close * 0.999, "close": close, "volume": vol},
        index=idx,
    )


# --------------------------------------------------------------------------------------
# Group delay
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("period,expected_delay", [(7.111111, 3), (15.283582, 7), (24.0, 12)])
def test_group_delay_matches_the_known_filter_values(period, expected_delay):
    assert group_delay_bars(period) == expected_delay


# --------------------------------------------------------------------------------------
# Trailing-percentile event detection
# --------------------------------------------------------------------------------------


def test_amp_surge_and_collapse_fire_on_opposite_extremes():
    rng = np.random.default_rng(0)
    n = 6000
    t = np.arange(n)
    # Amplitude modulated by a slow envelope so amplitude itself has real high/low regimes.
    envelope = 1.0 + 0.8 * np.sin(2 * np.pi * t / 1500.0)
    wave = envelope * np.sin(2 * np.pi * t / PERIOD)
    walk = np.cumsum(rng.normal(0, 0.002, size=n))
    close = np.exp(4.0 + 0.05 * wave + walk)
    ohlcv = _make_ohlcv(close)

    metrics = build_causal_metrics(ohlcv["close"], ohlcv["volume"], PERIOD)
    events = detect_amplitude_events(metrics, period=PERIOD)

    assert events["amp_surge_95"].sum() > 0
    assert events["amp_collapse_5"].sum() > 0
    # A bar cannot be both a surge and a collapse crossing at once.
    both = events["amp_surge_95"] & events["amp_collapse_5"]
    assert not both.any()


def test_signed_events_partition_into_up_and_down_and_never_both():
    rng = np.random.default_rng(1)
    n = 5000
    close = np.exp(4.0 + np.cumsum(rng.normal(0, 0.004, size=n)))
    close = close * (1.0 + 0.04 * np.sin(2 * np.pi * np.arange(n) / PERIOD))
    ohlcv = _make_ohlcv(close)
    metrics = build_causal_metrics(ohlcv["close"], ohlcv["volume"], PERIOD)
    events = detect_amplitude_events(metrics, period=PERIOD)

    up_down_overlap = events["amp_surge_85_up"] & events["amp_surge_85_down"]
    assert not up_down_overlap.any()


# --------------------------------------------------------------------------------------
# Synthetic vol-clustering: magnitude fires, direction does not
# --------------------------------------------------------------------------------------


def test_magnitude_fires_but_direction_does_not_under_pure_vol_clustering():
    """Alternating quiet/loud volatility blocks, zero directional bias: amplitude surges
    should predict bigger |forward return| (magnitude) without predicting its sign
    (direction). Vectorized block construction rather than a step-by-step GARCH loop."""
    rng = np.random.default_rng(2)
    block, n_blocks = 400, 40
    sigmas = np.tile(np.array([0.0015, 0.02]), n_blocks // 2)
    sigma_series = np.repeat(sigmas, block)
    n = sigma_series.size
    ret = rng.normal(0, 1, size=n) * sigma_series
    close = 100.0 * np.exp(np.cumsum(ret))
    ohlcv = _make_ohlcv(close)

    metrics = build_causal_metrics(ohlcv["close"], ohlcv["volume"], PERIOD)
    events = {"amp_surge_85": detect_amplitude_events(metrics, period=PERIOD)["amp_surge_85"]}

    from llm2.diagnostics.stats import apply_fdr
    from llm2.diagnostics.waveevent import score_events

    effects = apply_fdr(score_events(ohlcv["close"], events, horizons=(24,), min_events=20))
    by_kind = {e.name.split("|")[1]: e for e in effects if e.name.startswith("amp_surge_85|")}

    assert "magnitude" in by_kind, "no magnitude effect computed at all"
    assert by_kind["magnitude"].statistic > 0, "amplitude surge did not predict bigger moves"
    assert by_kind["magnitude"].significant, by_kind["magnitude"]
    if "direction" in by_kind:
        assert abs(by_kind["direction"].statistic) < abs(by_kind["magnitude"].statistic), (
            "direction effect was as large as the magnitude effect under an unbiased "
            "vol-clustering process"
        )


# --------------------------------------------------------------------------------------
# Group delay is actually used by the control
# --------------------------------------------------------------------------------------


def test_trailing_move_control_window_scales_with_group_delay():
    rng = np.random.default_rng(3)
    n = 4000
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=n))), index=_index(n))

    small_delay_events = trailing_move_control_events(close, group_delay=1, threshold_sigma=2.0)
    large_delay_events = trailing_move_control_events(close, group_delay=20, threshold_sigma=2.0)

    # Different windows must produce different event sets; the control is not a fixed,
    # delay-independent detector wearing the group-delay parameter as decoration.
    assert not small_delay_events.equals(large_delay_events)


def test_run_amplitude_event_study_uses_group_delay_in_every_effect():
    rng = np.random.default_rng(4)
    n = 6000
    close = 100.0 * np.exp(np.cumsum(rng.normal(0, 0.005, size=n)))
    close = close * (1.0 + 0.03 * np.sin(2 * np.pi * np.arange(n) / PERIOD))
    ohlcv = _make_ohlcv(close)

    effects = run_amplitude_event_study(ohlcv, PERIOD, horizons=(24,))
    assert effects
    delay = group_delay_bars(PERIOD)
    assert all(e.detail.get("group_delay_bars") == float(delay) for e in effects)


# --------------------------------------------------------------------------------------
# Policy: matched control is mandatory
# --------------------------------------------------------------------------------------


def test_amplitude_event_study_spec_has_a_valid_matched_control():
    from llm2.diagnostics.waveevent import AMPLITUDE_EVENT_STUDY_SPEC
    from llm2.research_policy import require_matched_control

    require_matched_control(AMPLITUDE_EVENT_STUDY_SPEC)  # must not raise


def test_missing_control_arm_is_refused():
    from llm2.research_policy import EventStudySpec, require_matched_control

    with pytest.raises(PolicyError):
        require_matched_control(
            EventStudySpec(
                name="broken",
                event_definition="amp surge",
                treatment_arm="amp_surge",
                control_arm="",
                matching="",
            )
        )
