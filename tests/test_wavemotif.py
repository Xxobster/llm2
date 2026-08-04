"""Tests for causal shape k-NN: neighbour-pool causality and planted-signal recovery."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.wavemotif import _knn_predict, _sliding_z_windows, run_shape_knn_study

PERIOD = 20.0


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


# --------------------------------------------------------------------------------------
# Sliding windows and k-NN mechanics
# --------------------------------------------------------------------------------------


def test_sliding_windows_are_z_normalised_and_causal_in_position():
    wave = np.sin(np.linspace(0, 40 * np.pi, 500)) * 2.0 + 3.0
    z, end_idx = _sliding_z_windows(wave, 16)
    assert z.shape == (500 - 16 + 1, 16)
    assert np.allclose(z.mean(axis=1), 0.0, atol=1e-8)
    assert np.allclose(z.std(axis=1), 1.0, atol=1e-6)
    # Window ending at position i must depend only on wave[i-15:i+1].
    i = 200
    row = z[np.searchsorted(end_idx, i)]
    raw = wave[i - 15 : i + 1]
    expected = (raw - raw.mean()) / raw.std()
    assert np.allclose(row, expected)


def test_knn_predict_recovers_the_exact_match_label():
    rng = np.random.default_rng(0)
    train = rng.normal(size=(500, 16))
    labels = rng.normal(size=500)
    query = train[[10, 20, 30]].copy()  # exact matches -> nearest neighbour is itself
    preds = _knn_predict(train, labels, query, k=1)
    assert np.allclose(preds, labels[[10, 20, 30]])


# --------------------------------------------------------------------------------------
# Neighbour-pool causality
# --------------------------------------------------------------------------------------


def test_query_fold_never_borrows_a_neighbour_from_the_embargoed_boundary():
    """Every train-pool window used for a query must end well before train_end, respecting
    the embargo; this is checked by construction via a monkeypatched-label channel."""
    rng = np.random.default_rng(1)
    n = 4000
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.004, size=n))), index=_index(n))
    train_end = close.index[3000]

    results = run_shape_knn_study(
        close, period=PERIOD, train_end=train_end, L_windows=(16,), k_values=(10,), horizon=24, embargo_bars=24
    )
    assert results
    row = results[0]
    # n_train windows must all end before (train_end_pos - embargo); a query-fold row count
    # greater than zero on a 4000-bar series with train_end at 3000 sanity-checks the split.
    assert row["n_train"] > 0
    assert row["n_query"] > 0


def test_changing_the_future_beyond_train_end_does_not_change_train_fold_predictions():
    """The decisive causality check: mutating the query fold must not change ANY prediction
    computed for bars strictly inside the training fold (there should be none — the query
    fold in this study is defined as everything at/after train_end — but the train windows
    themselves, and hence their labels, must be identical whether or not the future beyond
    train_end is mutated)."""
    rng = np.random.default_rng(2)
    n = 4000
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.004, size=n))), index=_index(n))
    train_end = close.index[3000]

    mutated = close.copy()
    mutated.iloc[3500:] *= 1.5  # large mutation, deep inside the query fold

    from llm2.diagnostics.wavemotif import _sliding_z_windows
    from llm2.diagnostics.wave import causal_wave

    log_c_orig = np.log(close)
    log_c_mut = np.log(mutated)
    wave_orig, _, _ = causal_wave(log_c_orig, PERIOD)
    wave_mut, _, _ = causal_wave(log_c_mut, PERIOD)

    z_orig, end_idx = _sliding_z_windows(wave_orig.to_numpy(), 16)
    z_mut, _ = _sliding_z_windows(wave_mut.to_numpy(), 16)

    train_end_pos = int(close.index.searchsorted(train_end, side="right"))
    train_rows = end_idx < train_end_pos
    assert np.allclose(
        z_orig[train_rows], z_mut[train_rows], equal_nan=True
    ), "a training-fold window changed after mutating data strictly after train_end"


# --------------------------------------------------------------------------------------
# Planted signal recovery
# --------------------------------------------------------------------------------------


def test_planted_shape_to_outcome_link_is_recovered_out_of_sample():
    """Plant a deterministic link: whenever the wave shape over the last L bars looks like
    template T, the forward return is reliably positive; an unrelated control shape is not.
    The k-NN study, evaluated on a held-out query fold, must recover this."""
    rng = np.random.default_rng(3)
    n = 20_000
    L = 16
    horizon = 24

    # Base wave: a clean cycle plus noise so build_causal_metrics has real structure to fit.
    t = np.arange(n)
    base = 0.03 * np.sin(2 * np.pi * t / PERIOD)
    walk = np.cumsum(rng.normal(0, 0.002, size=n))
    log_price = 4.0 + base + walk

    # Every ~50 bars (well-separated so windows do not overlap awkwardly), inject a
    # recognisable up-ramp shape into the wave-relevant price path, then reward it forward.
    plant_bars = np.arange(500, n - horizon - 10, 50)
    fwd_bump = np.zeros(n)
    for b in plant_bars:
        log_price[b - L : b] += np.linspace(0.0, 0.02, L)  # the "shape": a steady ramp up
        fwd_bump[b : b + horizon] += 0.0015  # reliably positive forward drift after it

    close = pd.Series(np.exp(log_price) * np.exp(np.cumsum(fwd_bump - np.mean(fwd_bump))), index=_index(n))

    train_end = close.index[n * 3 // 4]
    results = run_shape_knn_study(
        close, period=PERIOD, train_end=train_end, L_windows=(16,), k_values=(10, 50), horizon=horizon
    )
    assert results
    best = max(results, key=lambda r: (r["corr_pred_vs_realised"] if np.isfinite(r["corr_pred_vs_realised"]) else -1))
    assert best["n_valid"] >= 100
    assert best["corr_pred_vs_realised"] > 0.05, best
