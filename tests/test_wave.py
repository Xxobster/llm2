"""Tests for the market-strength wave, centred on the artefact it nearly produced.

The first version of `phase_lead_scan` reported "ETHUSDT leads BTCUSDT by 4 bars, r = 0.48"
with 24 of 24 pairs surviving false-discovery control. All of it was filter group delay: the
band-pass fitted to BTCUSDT's 15.3-bar cycle delays its input by 7 bars and the one fitted to
ETHUSDT's 7.1-bar cycle by 3, and 7 - 3 = 4. The tests below encode the controls that caught
it, so the same artefact cannot come back quietly.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.stats import circular_shift_max_lag_null
from llm2.diagnostics.wave import (
    NonCausalWaveError,
    WaveFit,
    _bandpass_coeffs,
    analytic_wave,
    causal_wave,
    dominant_period,
    fit_period_in_window,
    fit_wave,
    phase_lead_scan,
)


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


def _cyclic_price(n: int, period: float, amplitude: float, noise: float, seed: int = 0) -> pd.Series:
    rng = np.random.default_rng(seed)
    t = np.arange(n)
    wave = amplitude * np.sin(2 * np.pi * t / period)
    walk = np.cumsum(rng.normal(0, noise, size=n))
    return pd.Series(np.exp(4.0 + wave + walk), index=_index(n))


# --------------------------------------------------------------------------------------
# Spectral detection
# --------------------------------------------------------------------------------------


def test_dominant_period_finds_a_planted_cycle():
    price = _cyclic_price(8000, period=20.0, amplitude=0.05, noise=0.002)
    ret = np.diff(np.log(price.to_numpy()))
    period, ratio, p_val = dominant_period(ret, n_surrogates=100, seed=1)
    assert 17.0 < period < 23.0
    assert ratio > 3.0
    assert p_val <= 0.05


def test_dominant_period_is_quiet_on_a_random_walk():
    rng = np.random.default_rng(7)
    ret = rng.normal(0, 0.01, size=8000)
    _, ratio, p_val = dominant_period(ret, n_surrogates=100, seed=2)
    assert p_val > 0.05, f"pure noise produced a significant cycle (ratio {ratio:.2f})"


def test_short_series_returns_no_fit_rather_than_a_guess():
    period, ratio, p_val = dominant_period(np.random.default_rng(0).normal(size=500))
    assert np.isnan(period) and np.isnan(ratio) and np.isnan(p_val)


# --------------------------------------------------------------------------------------
# Causality of the two waves
# --------------------------------------------------------------------------------------


def test_analytic_wave_is_non_causal_and_causal_wave_is_not():
    """The decisive difference between the pretty wave and the usable one.

    Changing a value near the END of the series must not alter the causal wave near the
    START. The zero-phase analytic version fails this by construction, which is exactly
    why it is display-only.
    """
    price = _cyclic_price(4000, period=20.0, amplitude=0.05, noise=0.002)
    log_p = np.log(price)

    mutate_from = 3800
    mutated = log_p.copy()
    mutated.iloc[mutate_from:] += 0.5

    # Probe the window immediately BEFORE the mutation. A band-pass decays exponentially,
    # so a probe several hundred bars back measures nothing but floating-point dust and
    # would let a genuinely non-causal filter pass.
    probe = slice(mutate_from - 100, mutate_from)
    a_orig, _, _ = analytic_wave(log_p, 20.0)
    a_mut, _, _ = analytic_wave(mutated, 20.0)
    c_orig, _, _ = causal_wave(log_p, 20.0)
    c_mut, _, _ = causal_wave(mutated, 20.0)

    causal_delta = np.nanmax(np.abs((c_orig - c_mut).iloc[probe].to_numpy()))
    analytic_delta = np.nanmax(np.abs((a_orig - a_mut).iloc[probe].to_numpy()))

    assert causal_delta < 1e-9, "the causal wave saw the future"
    assert analytic_delta > 1e-4, "the analytic wave should be non-causal; test is not probing"


def test_causal_wave_blanks_its_filter_warmup():
    price = _cyclic_price(2000, period=20.0, amplitude=0.05, noise=0.001)
    wave, amp, phase = causal_wave(np.log(price), 20.0)
    assert wave.iloc[:60].isna().all()
    assert amp.iloc[:60].isna().all()
    assert phase.iloc[:60].isna().all()
    assert wave.iloc[100:].notna().any()


# --------------------------------------------------------------------------------------
# The group-delay artefact
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    "period,expected_delay", [(7.111111, 3), (15.283582, 7), (24.0, 12)]
)
def test_filter_group_delay_grows_with_period(period, expected_delay):
    """The mechanism behind the artefact, pinned so it cannot be forgotten."""
    from scipy.signal import lfilter

    impulse = np.zeros(600)
    impulse[0] = 1.0
    b, a = _bandpass_coeffs(period)
    peak = int(np.argmax(np.abs(lfilter(b, a, impulse))))
    assert peak == expected_delay


def test_a_series_cannot_lead_itself():
    """The control that exposed the artefact.

    One series, two filters at different periods, presented to the scan as two assets. Any
    reported lead is manufactured, because both 'assets' are the same data. With matched
    filters the scan must place the maximum at lag 0 and mark the pair as co-moving.
    """
    price = _cyclic_price(12000, period=15.0, amplitude=0.03, noise=0.004, seed=3)
    fit_a = fit_wave(price, symbol="A", timeframe="1h", period=15.0, n_surrogates=20)
    fit_b = fit_wave(price, symbol="B", timeframe="1h", period=7.0, n_surrogates=20)

    effects = phase_lead_scan(
        {"A": fit_a, "B": fit_b}, "A", closes={"A": price, "B": price}, max_lag_bars=24
    )
    assert effects, "scan produced nothing"
    eff = effects[0]
    assert eff.detail["filters_matched"] == 1.0
    assert eff.detail["leads_beyond_contemporaneous"] == 0.0, (
        "a series was reported as leading itself; the common-period refilter is not applied"
    )
    assert abs(eff.detail["corr_lag0"]) > abs(eff.statistic)


def test_unmatched_filters_are_flagged_when_prices_are_not_supplied():
    """Without prices the scan cannot refilter, and must say so rather than pretend."""
    price = _cyclic_price(12000, period=15.0, amplitude=0.03, noise=0.004, seed=4)
    fit_a = fit_wave(price, symbol="A", timeframe="1h", period=15.0, n_surrogates=20)
    fit_b = fit_wave(price, symbol="B", timeframe="1h", period=7.0, n_surrogates=20)

    effects = phase_lead_scan({"A": fit_a, "B": fit_b}, "A", max_lag_bars=24)
    assert effects
    assert effects[0].detail["filters_matched"] == 0.0


def test_a_genuine_lead_survives_the_matched_filter():
    """The control must not be so strict that it destroys a real lead.

    B is A shifted forward by 6 bars plus noise, so B genuinely leads A. With matched
    filters the scan must find roughly that lag and prefer it to lag 0.
    """
    n, lead = 12000, 6
    price = _cyclic_price(n, period=15.0, amplitude=0.03, noise=0.004, seed=5)
    rng = np.random.default_rng(6)
    log_a = np.log(price.to_numpy())
    log_b = np.concatenate([log_a[lead:], log_a[-lead:]]) + rng.normal(0, 0.002, size=n)
    leader = pd.Series(np.exp(log_b), index=price.index)

    fit_a = fit_wave(price, symbol="A", timeframe="1h", period=15.0, n_surrogates=20)
    fit_b = fit_wave(leader, symbol="B", timeframe="1h", period=15.0, n_surrogates=20)
    effects = phase_lead_scan(
        {"A": fit_a, "B": fit_b}, "A", closes={"A": price, "B": leader}, max_lag_bars=24
    )
    eff = effects[0]
    assert eff.detail["leads_beyond_contemporaneous"] == 1.0, "a real lead was suppressed"
    assert abs(eff.detail["lag_bars"] - lead) <= 2


# --------------------------------------------------------------------------------------
# Interpretation guards
# --------------------------------------------------------------------------------------


def test_a_shallow_peak_is_not_called_meaningful():
    """A 1.7x peak is describable, not tradeable, and the flag must say so."""
    weak = WaveFit(symbol="X", timeframe="1h", period_bars=15.3, peak_ratio=1.69,
                   p_value=0.005, n=60000)
    strong = WaveFit(symbol="X", timeframe="1h", period_bars=15.3, peak_ratio=4.0,
                     p_value=0.005, n=60000)
    significant_but_shallow = WaveFit(symbol="X", timeframe="1h", period_bars=15.3,
                                      peak_ratio=2.5, p_value=0.4, n=60000)
    assert not weak.is_meaningful
    assert strong.is_meaningful
    assert not significant_but_shallow.is_meaningful


def test_max_lag_null_is_calibrated_on_independent_noise():
    """Two independent series: max-over-lags p-values must not pile up near zero.

    The old single-lag-after-selection null rejected ~far above 5% on noise. This is the
    regression that keeps the lag search paid for.
    """
    rng = np.random.default_rng(11)
    p_vals = []
    for i in range(40):
        x = rng.normal(0, 1, size=3000)
        y = rng.normal(0, 1, size=3000)
        eff = circular_shift_max_lag_null(x, y, max_lag=24, n_null=200, seed=i)
        assert np.isfinite(eff.p_value)
        p_vals.append(eff.p_value)
    reject_rate = float(np.mean(np.asarray(p_vals) <= 0.05))
    assert reject_rate <= 0.15, f"max-lag null over-rejects on noise: {reject_rate:.2f}"


def test_fit_period_in_window_matches_dominant_period():
    price = _cyclic_price(8000, period=20.0, amplitude=0.05, noise=0.002)
    ret = np.diff(np.log(price.to_numpy()))
    a = fit_period_in_window(ret, n_surrogates=50, seed=1)
    b = dominant_period(ret, n_surrogates=50, seed=1)
    assert a == b


def test_analytic_wave_raises_when_called_from_mining_module(monkeypatch):
    """Mining modules must not reach the non-causal path."""
    import llm2.diagnostics.wave as wave_mod

    # Simulate a mining-module frame by temporarily renaming this test's module in the
    # refusal check via a direct call that patches the marker list to include __name__.
    monkeypatch.setattr(
        wave_mod, "_MINING_MODULE_MARKERS", (wave_mod.__name__, __name__, "tests.test_wave")
    )
    # The refusal walks the stack looking for mining markers; this test file is in the
    # patched marker list, so analytic_wave must raise.
    price = _cyclic_price(500, period=20.0, amplitude=0.05, noise=0.001)
    with pytest.raises(NonCausalWaveError):
        analytic_wave(np.log(price), 20.0)
