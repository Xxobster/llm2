"""Cross-asset scan must find planted leads and reject persistent-but-unrelated series."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from llm2.diagnostics.crossasset import (
    contemporaneous_scan,
    lead_lag_scan,
    transfer_entropy,
    transfer_entropy_scan,
)
from llm2.diagnostics.stats import circular_shift_null_corr

N = 20_000


def _frames(crypto_ret: np.ndarray, external_levels: dict[str, np.ndarray]) -> tuple[pd.DataFrame, pd.DataFrame]:
    idx = pd.date_range("2021-01-01", periods=len(crypto_ret), freq="1h", tz="UTC")
    close = 100.0 * np.exp(np.cumsum(crypto_ret))
    ohlcv = pd.DataFrame(
        {"open": close, "high": close * 1.001, "low": close * 0.999, "close": close, "volume": 1.0},
        index=idx,
    )
    panel = pd.DataFrame(external_levels, index=idx)
    return ohlcv, panel


def _find(effects, needle):
    hits = [e for e in effects if needle in e.name]
    if not hits:
        raise AssertionError(f"{needle} not found in {[e.name for e in effects][:10]}")
    return hits[0]


def test_price_levels_are_refused_rather_than_mis_tested():
    """The circular null is anti-conservative on integrated series, so it refuses them.

    Measured rejection rate on independent random-walk levels is roughly 17 percent, not 5,
    because the wrap-around discontinuity distorts the null. Correlating levels is a
    spurious-regression error anyway.
    """
    rng = np.random.default_rng(0)
    a = np.cumsum(rng.normal(size=N))
    b = np.cumsum(rng.normal(size=N))

    with pytest.raises(ValueError, match="unit-root"):
        circular_shift_null_corr(a, b)

    # Differencing to returns is accepted.
    eff = circular_shift_null_corr(np.diff(a), np.diff(b))
    assert np.isfinite(eff.p_value)


def test_overlapping_window_returns_are_accepted_not_mistaken_for_levels():
    """A 96-bar overlapping return has ACF1 near 0.99 but is stationary and valid input."""
    from llm2.diagnostics.stats import looks_integrated

    rng = np.random.default_rng(42)
    ret = rng.normal(0, 0.01, size=N)
    overlapping = np.convolve(ret, np.ones(96), mode="valid")

    acf1 = np.corrcoef(overlapping[1:], overlapping[:-1])[0, 1]
    assert acf1 > 0.97, f"sanity: overlapping returns should be highly autocorrelated ({acf1:.4f})"
    assert not looks_integrated(overlapping), "a moving sum of returns was mistaken for a level"

    eff = circular_shift_null_corr(overlapping, np.convolve(rng.normal(0, 0.01, size=N), np.ones(96), mode="valid"))
    assert np.isfinite(eff.p_value)


def test_circular_null_is_calibrated_on_returns_which_is_what_the_scan_uses():
    rejections = 0
    trials = 40
    for seed in range(trials):
        rng = np.random.default_rng(2000 + seed)
        eff = circular_shift_null_corr(rng.normal(size=5000), rng.normal(size=5000))
        rejections += int(np.isfinite(eff.p_value) and eff.p_value <= 0.05)
    assert rejections <= 6, f"{rejections}/{trials} rejections on independent returns"


def test_naive_p_value_would_fail_where_the_circular_null_does_not():
    """Documents why the machinery exists, on strongly autocorrelated but stationary series."""
    from scipy.stats import pearsonr

    rng = np.random.default_rng(0)
    n = N
    a = np.zeros(n)
    b = np.zeros(n)
    for i in range(1, n):  # persistent but mean-reverting: stationary AR(1), rho = 0.98
        a[i] = 0.98 * a[i - 1] + rng.normal()
        b[i] = 0.98 * b[i - 1] + rng.normal()

    _, naive_p = pearsonr(a, b)
    circular = circular_shift_null_corr(a, b)

    naive_se = 1.0 / np.sqrt(n)
    assert naive_p < 0.01, "textbook p-value calls these unrelated series related"
    assert circular.p_value > naive_p * 100, "circular null must be far more conservative"
    assert circular.detail["null_sd"] > 5 * naive_se, (
        f"null spread {circular.detail['null_sd']:.4f} should dwarf the naive standard error "
        f"{naive_se:.4f} for series this persistent"
    )


def test_circular_null_detects_a_genuine_relationship():
    rng = np.random.default_rng(1)
    x = rng.normal(size=N)
    y = 0.3 * x + rng.normal(0, 0.5, size=N)

    eff = circular_shift_null_corr(x, y)

    assert eff.statistic > 0.3
    assert eff.p_value < 0.01


def test_lead_lag_finds_a_planted_one_bar_lead():
    """External series moves, crypto follows one bar later."""
    rng = np.random.default_rng(2)
    ext_ret = rng.normal(0, 0.01, size=N)
    crypto_ret = 0.5 * np.roll(ext_ret, 1) + rng.normal(0, 0.005, size=N)
    crypto_ret[0] = 0.0
    ext_level = 100.0 * np.exp(np.cumsum(ext_ret))

    ohlcv, panel = _frames(crypto_ret, {"LEADER": ext_level})
    effects = lead_lag_scan(ohlcv, panel, windows=(1,), horizons=(1,))

    eff = _find(effects, "LEADER|trail1->fwd1")
    assert eff.statistic > 0.3, eff
    assert eff.significant, eff


def test_lead_lag_ignores_a_series_that_only_moves_simultaneously():
    """Perfect same-bar coupling with no lead must produce no tradeable signal."""
    rng = np.random.default_rng(3)
    shared = rng.normal(0, 0.01, size=N)
    crypto_ret = shared + rng.normal(0, 0.002, size=N)
    ext_level = 100.0 * np.exp(np.cumsum(shared + rng.normal(0, 0.002, size=N)))

    ohlcv, panel = _frames(crypto_ret, {"TWIN": ext_level})

    contemp = contemporaneous_scan(ohlcv, panel, windows=(1,))
    assert _find(contemp, "TWIN|contemporaneous_w1").statistic > 0.9, "sanity: they do move together"

    effects = lead_lag_scan(ohlcv, panel, windows=(1,), horizons=(1,))
    eff = _find(effects, "TWIN|trail1->fwd1")
    assert not eff.significant, (
        f"same-bar twin produced a tradeable lead r={eff.statistic:.3f} q={eff.q_value:.3f}"
    )


def test_contemporaneous_results_are_labelled_untradeable():
    rng = np.random.default_rng(4)
    ohlcv, panel = _frames(
        rng.normal(0, 0.01, size=N), {"X": 100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=N)))}
    )
    for eff in contemporaneous_scan(ohlcv, panel, windows=(1, 6)):
        assert "NOT_TRADEABLE" in eff.name
        assert not np.isfinite(eff.p_value), "context statistics must not carry a p-value"


def test_lead_lag_scan_survives_a_wide_noise_panel_without_false_discoveries():
    """Thirty unrelated persistent series is the realistic scan; FDR must hold the line."""
    rng = np.random.default_rng(5)
    crypto_ret = rng.normal(0, 0.01, size=N)
    panel_levels = {
        f"NOISE{i}": 100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=N))) for i in range(30)
    }
    ohlcv, panel = _frames(crypto_ret, panel_levels)

    effects = lead_lag_scan(ohlcv, panel, windows=(1, 6, 24), horizons=(1, 6))

    n_sig = sum(e.significant for e in effects)
    assert len(effects) >= 150, f"scan too small to be a real test: {len(effects)}"
    assert n_sig == 0, f"{n_sig}/{len(effects)} false discoveries across an unrelated panel"


def test_lead_lag_finds_the_needle_in_the_noise_panel():
    """One real lead among thirty decoys must still be recovered after FDR."""
    rng = np.random.default_rng(6)
    signal_ret = rng.normal(0, 0.01, size=N)
    crypto_ret = 0.4 * np.roll(signal_ret, 1) + rng.normal(0, 0.008, size=N)
    crypto_ret[0] = 0.0

    levels = {"SIGNAL": 100.0 * np.exp(np.cumsum(signal_ret))}
    levels.update(
        {f"NOISE{i}": 100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=N))) for i in range(29)}
    )
    ohlcv, panel = _frames(crypto_ret, levels)

    effects = lead_lag_scan(ohlcv, panel, windows=(1, 6), horizons=(1, 6))

    survivors = [e for e in effects if e.significant]
    assert survivors, "the planted lead did not survive multiplicity correction"
    assert all(s.name.startswith("SIGNAL") for s in survivors), (
        f"decoys survived: {[s.name for s in survivors if not s.name.startswith('SIGNAL')]}"
    )


def test_transfer_entropy_detects_nonlinear_dependence_correlation_misses():
    rng = np.random.default_rng(7)
    n = 20_000
    src = rng.normal(size=n)
    # Target depends on the magnitude of the source, not its sign: correlation is ~0.
    tgt = np.abs(np.roll(src, 1)) * rng.normal(1.0, 0.3, size=n)
    tgt[0] = 0.0

    from llm2.diagnostics.stats import safe_corr

    assert abs(safe_corr(src, tgt)) < 0.05, "sanity: linear correlation should be blind here"

    eff = transfer_entropy(src, tgt, n_surrogates=60, seed=1)
    assert eff.p_value < 0.05, eff
    assert eff.statistic > 0


def test_transfer_entropy_quiet_on_independent_series():
    rng = np.random.default_rng(8)
    eff = transfer_entropy(rng.normal(size=20_000), rng.normal(size=20_000), n_surrogates=60, seed=2)
    assert eff.p_value > 0.05, eff


def test_transfer_entropy_scan_returns_fdr_adjusted_effects():
    rng = np.random.default_rng(9)
    ohlcv, panel = _frames(
        rng.normal(0, 0.01, size=N),
        {f"S{i}": 100.0 * np.exp(np.cumsum(rng.normal(0, 0.01, size=N))) for i in range(4)},
    )
    effects = transfer_entropy_scan(ohlcv, panel, n_surrogates=40)
    assert effects
    assert all(np.isfinite(e.q_value) for e in effects)
    assert not any(e.significant for e in effects)


@pytest.mark.parametrize("n", [100, 400])
def test_short_series_return_nan_rather_than_a_confident_number(n):
    rng = np.random.default_rng(10)
    eff = circular_shift_null_corr(rng.normal(size=n), rng.normal(size=n))
    assert np.isnan(eff.statistic)
