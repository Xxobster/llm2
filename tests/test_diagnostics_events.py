"""Confluence tables and event studies must not invent structure from combinatorics."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.confluence import (
    build_state_frame,
    confluence_table,
    marginal_contribution,
    state_space_report,
    suggest_symbol_subsets,
    trend_sign,
)
from llm2.diagnostics.events import (
    detect_pulses,
    event_paths,
    pre_event_displacement,
    pulse_forward_outcome,
)

N = 30_000


def _make(crypto_ret: np.ndarray, externals: dict[str, np.ndarray]):
    idx = pd.date_range("2020-01-01", periods=len(crypto_ret), freq="1h", tz="UTC")
    close = 100.0 * np.exp(np.cumsum(crypto_ret))
    ohlcv = pd.DataFrame(
        {"open": close, "high": close * 1.002, "low": close * 0.998, "close": close, "volume": 1.0},
        index=idx,
    )
    panel = pd.DataFrame({k: 100.0 * np.exp(np.cumsum(v)) for k, v in externals.items()}, index=idx)
    return ohlcv, panel


# --------------------------------------------------------------------------- confluence


def test_trend_sign_is_causal():
    """Truncating the series must not change any earlier trend sign."""
    rng = np.random.default_rng(0)
    level = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=3000))))

    full = trend_sign(level, 200)
    truncated = trend_sign(level.iloc[:2000], 200)

    pd.testing.assert_series_equal(full.iloc[:2000], truncated, check_names=False)


def test_state_frame_is_binary_and_forward_filled():
    rng = np.random.default_rng(1)
    _, panel = _make(rng.normal(0, 0.01, size=5000), {"A": rng.normal(0, 0.01, size=5000)})
    states = build_state_frame(panel, ["A"], span=100)
    vals = states["A"].dropna().unique()
    assert set(vals) <= {1.0, -1.0}, vals


def test_confluence_finds_nothing_in_unrelated_series():
    rng = np.random.default_rng(2)
    ohlcv, panel = _make(
        rng.normal(0, 0.01, size=N),
        {f"X{i}": rng.normal(0, 0.01, size=N) for i in range(4)},
    )

    effects = confluence_table(ohlcv, panel, [f"X{i}" for i in range(4)], horizon=24, span=200)

    assert effects, "no states were populated at all"
    n_sig = sum(e.significant for e in effects)
    assert n_sig == 0, f"{n_sig}/{len(effects)} confluence states significant on unrelated data"


def test_confluence_recovers_an_injected_joint_condition():
    """Drift only when both externals trend down together."""
    rng = np.random.default_rng(3)
    a = np.cumsum(rng.normal(0, 0.01, size=N))
    b = np.cumsum(rng.normal(0, 0.01, size=N))
    a_down = pd.Series(a).ewm(span=200, adjust=False, min_periods=200).mean().diff() < 0
    b_down = pd.Series(b).ewm(span=200, adjust=False, min_periods=200).mean().diff() < 0
    both_down = (a_down & b_down).to_numpy()

    crypto = rng.normal(0, 0.004, size=N)
    crypto[both_down] += 0.0015

    idx = pd.date_range("2020-01-01", periods=N, freq="1h", tz="UTC")
    close = 100.0 * np.exp(np.cumsum(crypto))
    ohlcv = pd.DataFrame(
        {"open": close, "high": close, "low": close, "close": close, "volume": 1.0}, index=idx
    )
    panel = pd.DataFrame({"A": 100 * np.exp(a), "B": 100 * np.exp(b)}, index=idx)

    effects = confluence_table(ohlcv, panel, ["A", "B"], horizon=24, span=200)
    winners = [e for e in effects if e.significant and e.statistic > 0]

    assert winners, f"injected joint condition not found: {[(e.name, e.statistic) for e in effects]}"
    assert any("A-" in e.name and "B-" in e.name for e in winners), [e.name for e in winners]


def test_confluence_enforces_a_minimum_sample_floor():
    rng = np.random.default_rng(4)
    ohlcv, panel = _make(
        rng.normal(0, 0.01, size=8000), {f"X{i}": rng.normal(0, 0.01, size=8000) for i in range(6)}
    )
    effects = confluence_table(ohlcv, panel, [f"X{i}" for i in range(6)], horizon=24, min_samples=500)
    assert all(e.n >= 500 for e in effects), "a state below the sample floor was reported"


def test_state_space_report_flags_an_unanswerable_table():
    report = state_space_report([f"S{i}" for i in range(10)], n_rows=50_000)
    assert report["states_possible"] == 1024
    assert report["max_states_supportable"] < report["states_possible"], (
        "a 10-series table must be reported as beyond what the data supports"
    )


def test_subset_suggestion_stops_before_the_data_runs_out():
    subsets = suggest_symbol_subsets([f"S{i}" for i in range(8)], n_rows=50_000, max_size=6)
    assert subsets
    assert max(len(s) for s in subsets) <= 6
    for s in subsets:
        assert 50_000 / (2 ** len(s)) >= 500


def test_marginal_contribution_isolates_the_driving_series():
    rng = np.random.default_rng(5)
    a = np.cumsum(rng.normal(0, 0.01, size=N))
    a_up = (pd.Series(a).ewm(span=200, adjust=False, min_periods=200).mean().diff() > 0).to_numpy()
    crypto = rng.normal(0, 0.004, size=N)
    crypto[a_up] += 0.0015

    idx = pd.date_range("2020-01-01", periods=N, freq="1h", tz="UTC")
    close = 100.0 * np.exp(np.cumsum(crypto))
    ohlcv = pd.DataFrame(
        {"open": close, "high": close, "low": close, "close": close, "volume": 1.0}, index=idx
    )
    panel = pd.DataFrame(
        {"A": 100 * np.exp(a), "B": 100 * np.exp(np.cumsum(rng.normal(0, 0.01, size=N)))}, index=idx
    )

    effects = marginal_contribution(ohlcv, panel, ["A", "B"], horizon=24, span=200)
    by_name = {e.name: e for e in effects}

    driver = by_name["marginal[A_up_minus_down]"]
    decoy = by_name["marginal[B_up_minus_down]"]

    assert driver.statistic > 0 and driver.significant, driver
    assert not decoy.significant, decoy


def test_marginal_contribution_is_not_fooled_by_unconditional_drift():
    """With a strongly trending asset, every bucket beats zero; only the spread is evidence."""
    rng = np.random.default_rng(20)
    n = N
    crypto = rng.normal(0.0008, 0.004, size=n)  # large positive drift, no external relationship
    ohlcv, panel = _make(crypto, {"UNRELATED": rng.normal(0, 0.01, size=n)})

    effects = marginal_contribution(ohlcv, panel, ["UNRELATED"], horizon=24, span=200)
    eff = effects[0]

    assert eff.detail["up_mean_bps"] > 100, "sanity: the drift makes every bucket strongly positive"
    assert eff.detail["down_mean_bps"] > 100
    assert not eff.significant, f"drift alone produced a marginal finding: {eff}"


# ------------------------------------------------------------------------------ events


def test_pulse_detection_is_causal_and_respects_the_gap():
    rng = np.random.default_rng(6)
    ohlcv, _ = _make(rng.normal(0, 0.01, size=N), {})

    pulses = detect_pulses(ohlcv, lookback=6, threshold_sigma=3.0, min_gap=24)

    assert not pulses.empty
    assert (np.diff(pulses["bar"].to_numpy()) >= 24).all(), "overlapping pulses were kept"

    # Truncating the series must not change pulses detected before the cut.
    cut = N // 2
    truncated = detect_pulses(ohlcv.iloc[:cut], lookback=6, threshold_sigma=3.0, min_gap=24)
    shared = pulses[pulses["bar"] < cut - 6]
    assert set(truncated["bar"]) >= set(shared["bar"]), "pulse flags changed when the future was removed"


def test_pulse_detection_scales_with_volatility_not_a_fixed_percentage():
    """A fixed threshold would select only from the loud regime."""
    rng = np.random.default_rng(7)
    quiet = rng.normal(0, 0.002, size=N // 2)
    loud = rng.normal(0, 0.02, size=N // 2)
    ohlcv, _ = _make(np.concatenate([quiet, loud]), {})

    pulses = detect_pulses(ohlcv, lookback=6, threshold_sigma=3.0, min_gap=24)
    in_quiet = (pulses["bar"] < N // 2).sum()
    in_loud = (pulses["bar"] >= N // 2).sum()

    assert in_quiet > 0, "no pulses detected in the quiet regime"
    assert in_loud > 0
    assert 0.2 < in_quiet / max(1, in_loud) < 5.0, f"quiet={in_quiet} loud={in_loud} is too lopsided"


def test_event_paths_are_indexed_by_relative_offset():
    rng = np.random.default_rng(8)
    ohlcv, panel = _make(rng.normal(0, 0.01, size=N), {"A": rng.normal(0, 0.01, size=N)})
    pulses = detect_pulses(ohlcv)

    paths = event_paths(panel, pulses, before=12, after=12)

    assert list(paths.index) == list(range(-12, 13))
    assert "A" in paths.columns


def test_pre_event_displacement_quiet_when_externals_are_unrelated():
    """Everything moves around a big move; the matched null must absorb that."""
    rng = np.random.default_rng(9)
    ohlcv, panel = _make(
        rng.normal(0, 0.01, size=N), {f"X{i}": rng.normal(0, 0.01, size=N) for i in range(5)}
    )
    pulses = detect_pulses(ohlcv)

    effects = pre_event_displacement(panel, ohlcv, pulses, before=12, n_pseudo=100)

    assert effects, "no pre-event statistics produced"
    n_sig = sum(e.significant for e in effects)
    assert n_sig == 0, f"{n_sig}/{len(effects)} spurious pre-event displacements"


def test_pre_event_displacement_finds_a_planted_precursor():
    """An external series that reliably rises before crypto pulses must be recovered."""
    rng = np.random.default_rng(10)
    n = N
    crypto = rng.normal(0, 0.005, size=n)
    precursor = rng.normal(0, 0.01, size=n)

    # Plant pulses at known bars, with the precursor LEVEL bulging over the prior 12 bars
    # and returning to baseline afterwards. Adding only to the pre-window would ratchet the
    # level up permanently, which is a trend, not a precursor.
    pulse_bars = np.arange(1000, n - 100, 300)
    for b in pulse_bars:
        precursor[b - 12 : b] += 0.02
        precursor[b : b + 12] -= 0.02
        crypto[b] += 0.06

    ohlcv, panel = _make(crypto, {"PRECURSOR": precursor, "NOISE": rng.normal(0, 0.01, size=n)})
    pulses = detect_pulses(ohlcv, lookback=1, threshold_sigma=3.0, min_gap=24)
    assert len(pulses) > 30, f"only {len(pulses)} pulses detected"

    effects = pre_event_displacement(panel, ohlcv, pulses, before=12, n_pseudo=200, direction=1)
    by_name = {e.name: e for e in effects}

    assert by_name["pre_event[PRECURSOR]"].significant, by_name["pre_event[PRECURSOR]"]
    assert not by_name["pre_event[NOISE]"].significant, by_name["pre_event[NOISE]"]


def test_pulse_forward_outcome_reports_continuation_sign():
    rng = np.random.default_rng(11)
    ohlcv, _ = _make(rng.normal(0, 0.01, size=N), {})
    pulses = detect_pulses(ohlcv)

    effects = pulse_forward_outcome(ohlcv, pulses, horizons=(6, 24))

    assert effects
    assert all("continuation_bps" in e.detail for e in effects)
    assert not any(e.significant for e in effects), "random walk shows post-pulse drift"
