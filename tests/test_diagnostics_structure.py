"""Structure detectors must recover known structure and stay quiet on a random walk."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.structure import (
    SESSIONS,
    autocorrelation,
    cycles,
    forward_log_return,
    mean_reversion,
    momentum,
    nonlinear_lag,
    regime_conditional,
    seasonality,
    volatility_clustering,
)

N = 20_000


def _ohlcv_from_returns(ret: np.ndarray, start: str = "2021-01-01") -> pd.DataFrame:
    close = 100.0 * np.exp(np.cumsum(ret))
    idx = pd.date_range(start, periods=len(close), freq="1h", tz="UTC")
    rng = np.random.default_rng(0)
    wiggle = np.abs(rng.normal(0, 0.001, size=len(close)))
    return pd.DataFrame(
        {
            "open": close * (1 - wiggle / 2),
            "high": close * (1 + wiggle),
            "low": close * (1 - wiggle),
            "close": close,
            "volume": rng.lognormal(10, 1, size=len(close)),
        },
        index=idx,
    )


def _random_walk(seed: int = 0) -> pd.DataFrame:
    return _ohlcv_from_returns(np.random.default_rng(seed).normal(0, 0.01, size=N))


def _find(effects, name):
    for e in effects:
        if e.name == name:
            return e
    raise AssertionError(f"{name} not among {[e.name for e in effects][:12]}")


def test_forward_return_is_forward_and_not_shifted_the_wrong_way():
    close = pd.Series([1.0, 2.0, 4.0, 8.0])
    fwd = forward_log_return(close, 1)
    assert fwd.iloc[0] == pytest.approx(np.log(2.0))
    assert np.isnan(fwd.iloc[-1]), "the last bar has no forward return"


def test_autocorrelation_detects_an_ar1_process():
    rng = np.random.default_rng(1)
    innov = rng.normal(0, 0.01, size=N)
    ret = np.zeros(N)
    for i in range(1, N):
        ret[i] = 0.3 * ret[i - 1] + innov[i]

    effects = autocorrelation(_ohlcv_from_returns(ret)["close"])

    lag1 = _find(effects, "acf_lag_1")
    assert lag1.statistic == pytest.approx(0.3, abs=0.05)
    assert lag1.significant


def test_autocorrelation_is_quiet_on_a_random_walk():
    effects = autocorrelation(_random_walk(2)["close"])
    acf = [e for e in effects if e.name.startswith("acf_lag_")]
    n_sig = sum(e.significant for e in acf)
    assert n_sig <= 2, f"{n_sig}/{len(acf)} autocorrelation lags significant on a random walk"


def test_variance_ratio_is_one_for_a_random_walk():
    effects = autocorrelation(_random_walk(3)["close"])
    vr = _find(effects, "variance_ratio_4")
    assert vr.statistic == pytest.approx(1.0, abs=0.12)


def test_variance_ratio_exceeds_one_for_a_trending_series():
    rng = np.random.default_rng(4)
    innov = rng.normal(0, 0.01, size=N)
    ret = np.zeros(N)
    for i in range(1, N):
        ret[i] = 0.35 * ret[i - 1] + innov[i]  # positive memory compounds
    effects = autocorrelation(_ohlcv_from_returns(ret)["close"])
    assert _find(effects, "variance_ratio_4").statistic > 1.3


def test_mean_reversion_detects_an_engineered_pullback():
    """Construct a series that genuinely reverts toward its moving average."""
    rng = np.random.default_rng(5)
    n = N
    close = np.zeros(n)
    close[0] = 100.0
    level = 100.0
    for i in range(1, n):
        level += rng.normal(0, 0.02)
        close[i] = close[i - 1] + 0.05 * (level - close[i - 1]) + rng.normal(0, 0.05)
    idx = pd.date_range("2021-01-01", periods=n, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {"open": close, "high": close * 1.001, "low": close * 0.999, "close": close, "volume": 1.0},
        index=idx,
    )

    effects = mean_reversion(ohlcv, horizon=6, ema_spans=(24,))
    corr = _find(effects, "stretch_ema24_vs_fwd6")
    assert corr.statistic < -0.05, f"expected negative stretch-to-forward correlation, got {corr.statistic}"


def test_momentum_detects_engineered_continuation():
    rng = np.random.default_rng(6)
    innov = rng.normal(0, 0.01, size=N)
    ret = np.zeros(N)
    for i in range(1, N):
        ret[i] = 0.25 * ret[i - 1] + innov[i]
    effects = momentum(_ohlcv_from_returns(ret), horizon=6, lookbacks=(6,))

    # Summing an AR(1) over 6 bars dilutes the lag-1 coefficient heavily, so the detectable
    # correlation is far below beta. What matters is sign and significance, not magnitude.
    eff = _find(effects, "trail6_vs_fwd6")
    assert eff.statistic > 0.0
    assert eff.significant, eff
    assert eff.ci_low > 0.0, eff


def test_momentum_is_quiet_on_a_random_walk():
    effects = momentum(_random_walk(7), horizon=6, lookbacks=(6, 24))
    corr = [e for e in effects if "_vs_fwd" in e.name]
    assert not any(e.significant for e in corr)


def test_seasonality_detects_an_injected_hour_effect():
    """The bucket for hour h holds the return earned AFTER bar h, not during it."""
    rng = np.random.default_rng(8)
    ret = rng.normal(0, 0.005, size=N)
    idx = pd.date_range("2021-01-01", periods=N, freq="1h", tz="UTC")
    # Inject into hour 14 so that conditioning on the hour-13 bar is what predicts it.
    ret[idx.hour == 14] += 0.004

    effects = seasonality(_ohlcv_from_returns(ret), horizon=1)

    hour_13 = _find(effects, "fwd1|hour_utc[13]")
    assert hour_13.statistic > 0.002, hour_13
    assert hour_13.significant, hour_13
    # The hour that merely contains the drift must not be credited with predicting it.
    assert not _find(effects, "fwd1|hour_utc[14]").significant


def test_seasonality_covers_the_named_sessions():
    effects = seasonality(_random_walk(9), horizon=6)
    names = " ".join(e.name for e in effects)
    for session in SESSIONS:
        assert session in names, f"session {session} not evaluated"
    assert "funding_hour" in names
    assert "turn_of_month" in names


def test_volatility_clustering_is_found_in_a_garch_like_series():
    rng = np.random.default_rng(10)
    n = N
    ret = np.zeros(n)
    sigma2 = 1e-4
    for i in range(n):
        sigma2 = 1e-6 + 0.1 * ret[i - 1] ** 2 + 0.88 * sigma2
        ret[i] = rng.normal(0, np.sqrt(sigma2))

    effects = volatility_clustering(_ohlcv_from_returns(ret))

    assert _find(effects, "abs_ret_acf_lag_1").statistic > 0.1
    arch = _find(effects, "arch_lm_12")
    assert arch.p_value < 0.01, "ARCH-LM should reject homoskedasticity here"


def test_volatility_clustering_absent_in_homoskedastic_noise():
    effects = volatility_clustering(_random_walk(11))
    assert _find(effects, "abs_ret_acf_lag_24").statistic < 0.05


def test_cycles_finds_no_periodicity_in_noise():
    effects = cycles(_random_walk(12)["close"], n_surrogates=100)
    assert effects, "spectral scan produced nothing"
    assert not any(e.significant for e in effects), "a wave was found in white noise"


def test_cycles_finds_an_injected_periodicity():
    rng = np.random.default_rng(13)
    t = np.arange(N)
    period = 50
    ret = rng.normal(0, 0.004, size=N) + 0.006 * np.sin(2 * np.pi * t / period)

    effects = cycles(_ohlcv_from_returns(ret)["close"], n_surrogates=100)

    global_test = _find(effects, "spectral_peak_global")
    assert global_test.significant, f"injected {period}-bar cycle not detected: {global_test}"
    assert abs(global_test.detail["peak_period_bars"] - period) / period < 0.25, global_test


def test_cycles_uses_a_global_maximum_rather_than_per_bin_tests():
    """Per-bin permutation tests across ~512 bins can never clear FDR (the D-013 class).

    Only the global test carries a p-value; individual peaks are descriptive.
    """
    effects = cycles(_random_walk(16)["close"], n_surrogates=60)

    with_p = [e for e in effects if np.isfinite(e.p_value)]
    assert len(with_p) == 1, f"expected exactly one hypothesis test, got {len(with_p)}"
    assert with_p[0].name == "spectral_peak_global"
    assert all(not np.isfinite(e.p_value) for e in effects if e.name != "spectral_peak_global")


def test_regime_conditional_separates_a_sign_flip():
    """Momentum in high volatility, reversion in low: unconditionally this averages to zero."""
    rng = np.random.default_rng(14)
    n = N
    ret = np.zeros(n)
    regime_high = (np.arange(n) // 500) % 2 == 0
    for i in range(1, n):
        scale = 0.02 if regime_high[i] else 0.002
        beta = 0.3 if regime_high[i] else -0.3
        ret[i] = beta * ret[i - 1] + rng.normal(0, scale)

    effects = regime_conditional(_ohlcv_from_returns(ret), horizon=6, lookback=24)
    named = {e.name: e for e in effects if "vol=" in e.name}

    assert named, "no volatility-conditioned effects produced"
    stats = {k: v.statistic for k, v in named.items() if np.isfinite(v.statistic)}
    assert max(stats.values()) - min(stats.values()) > 0.05, (
        f"regime conditioning did not separate the sign flip: {stats}"
    )


def test_nonlinear_lag_reports_information_where_correlation_is_blind():
    rng = np.random.default_rng(15)
    n = 20_000
    ret = rng.normal(0, 0.01, size=n)
    # Forward move depends on the SQUARE of the last return: zero linear correlation.
    close = 100.0 * np.exp(np.cumsum(ret))
    idx = pd.date_range("2021-01-01", periods=n, freq="1h", tz="UTC")
    ohlcv = pd.DataFrame(
        {"open": close, "high": close, "low": close, "close": close, "volume": 1.0}, index=idx
    )

    effects = nonlinear_lag(ohlcv, horizon=6)

    assert effects
    assert all(np.isfinite(e.statistic) for e in effects)
    assert all("linear_corr" in e.detail for e in effects)
