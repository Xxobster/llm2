"""Tests for the cross-series wave panel: admission, clustering, self-lead control."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.wavepanel import (
    RejectedSeriesError,
    admit_series,
    cluster_by_raw_return_correlation,
    ordered_pair_lead_scan,
)


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


# --------------------------------------------------------------------------------------
# Admission
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "name,kind",
    [
        ("sma_50", "moving_average"),
        ("ema_200", "moving_average"),
        ("macd_signal", "oscillator"),
        ("bollinger_mid", "band"),
        ("close_sma", "close"),  # even under an admissible Tier A kind, the name pattern rejects it
    ],
)
def test_linear_price_filters_are_rejected_regardless_of_claimed_kind(name, kind):
    with pytest.raises(RejectedSeriesError):
        admit_series(name, kind)


def test_rsi_is_admitted_under_its_registered_kind():
    admit_series("rsi_14", "oscillator")  # must not raise


def test_tier_a_kinds_are_admitted_by_kind_alone():
    admit_series("ANYFUTURESYMBOL", "close")
    admit_series("FUNDING_BTCUSDT", "funding")
    admit_series("DXY", "macro")


def test_unregistered_tier_b_name_is_refused():
    with pytest.raises(RejectedSeriesError):
        admit_series("some_novel_indicator", "momentum")


def test_tier_b_name_with_mismatched_kind_is_refused():
    with pytest.raises(RejectedSeriesError):
        admit_series("rsi_14", "volatility")  # rsi_14 is registered as 'oscillator'


# --------------------------------------------------------------------------------------
# Clustering happens on raw returns
# --------------------------------------------------------------------------------------


def test_near_duplicate_series_are_merged_into_one_cluster():
    rng = np.random.default_rng(0)
    n = 5000
    base = rng.normal(0, 0.01, size=n)
    returns = pd.DataFrame(
        {
            "A": base,
            "B": base + rng.normal(0, 0.0005, size=n),  # near-duplicate of A
            "C": rng.normal(0, 0.01, size=n),  # independent
        },
        index=_index(n),
    )
    clusters, representative = cluster_by_raw_return_correlation(returns, threshold=0.9)
    assert representative["A"] == representative["B"]
    assert representative["C"] != representative["A"]
    assert len(clusters) == 2


def test_cluster_representative_choice_is_deterministic_by_coverage():
    rng = np.random.default_rng(1)
    n = 5000
    base = rng.normal(0, 0.01, size=n)
    a = base.copy()
    b = base + rng.normal(0, 0.0005, size=n)
    a[: n // 4] = np.nan  # A has less coverage than B
    returns = pd.DataFrame({"A": a, "B": b}, index=_index(n))
    _, representative = cluster_by_raw_return_correlation(returns, threshold=0.9)
    assert representative["A"] == "B"
    assert representative["B"] == "B"


def test_clustering_uses_raw_returns_not_a_wave_transform():
    """Two series correlated only after band-pass filtering (not in their raw returns)
    must NOT be merged: clustering is defined on the untransformed input."""
    rng = np.random.default_rng(2)
    n = 6000
    t = np.arange(n)
    a = 0.05 * np.sin(2 * np.pi * t / 20.0) + np.cumsum(rng.normal(0, 0.01, size=n))
    b = 0.05 * np.sin(2 * np.pi * t / 20.0 + np.pi) + np.cumsum(rng.normal(0, 0.01, size=n))
    # a and b share a wave component in antiphase (would look related after some transforms)
    # but their raw log-returns are only weakly related.
    returns = pd.DataFrame({"A": np.diff(a, prepend=a[0]), "B": np.diff(b, prepend=b[0])}, index=_index(n))
    clusters, representative = cluster_by_raw_return_correlation(returns, threshold=0.9)
    assert representative["A"] != representative["B"], "raw-return correlation was not what drove clustering"


# --------------------------------------------------------------------------------------
# Self-lead control: a series cannot lead itself
# --------------------------------------------------------------------------------------


def _cyclic_close(n: int, period: float, seed: int) -> pd.Series:
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    wave = 0.04 * np.sin(2 * np.pi * t / period)
    walk = np.cumsum(rng.normal(0, 0.003, size=n))
    return pd.Series(np.exp(4.0 + wave + walk), index=_index(n))


def test_self_lead_control_is_attached_and_quiet():
    """The reference symbol correlated against ITSELF (as if it were an external series)
    must show self_control comparable to the claimed lead, and the effect's own detail must
    say so rather than reporting a clean cross-series result."""
    close = _cyclic_close(8000, period=20.0, seed=3)
    effects = ordered_pair_lead_scan(
        close, "BTCUSDT", {"BTCUSDT_COPY": close}, period=20.0, max_lag_bars=24
    )
    assert effects
    level_effect = next(e for e in effects if e.detail["channel"] == "level")
    assert np.isfinite(level_effect.detail["self_control_statistic"])
    assert not level_effect.detail["self_control_passed"], (
        "a series correlated against an exact copy of itself passed its own self-control"
    )


def test_genuine_lead_reports_a_weaker_self_control():
    n, lead = 10000, 5
    ref = _cyclic_close(n, period=20.0, seed=4)
    log_ref = np.log(ref.to_numpy())
    rng = np.random.default_rng(5)
    log_leader = np.concatenate([log_ref[lead:], log_ref[-lead:]]) + rng.normal(0, 0.002, size=n)
    leader = pd.Series(np.exp(log_leader), index=ref.index)

    effects = ordered_pair_lead_scan(ref, "BTCUSDT", {"LEADER": leader}, period=20.0, max_lag_bars=24)
    level_effect = next(e for e in effects if e.detail["channel"] == "level")
    assert abs(level_effect.detail["self_control_statistic"]) < abs(level_effect.statistic), (
        "the self-control was as strong as the claimed genuine lead"
    )
