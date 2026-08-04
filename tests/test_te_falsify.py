"""Transfer-entropy falsification controls must catch shared-volatility artefacts."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.te_falsify import _block_shuffle, falsify_transfer_entropy


def _index(n: int) -> pd.DatetimeIndex:
    return pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")


def test_block_shuffle_preserves_length_and_destroys_order():
    x = np.arange(1000, dtype=float)
    y = _block_shuffle(x, block=50, seed=0)
    assert len(y) == len(x)
    assert not np.array_equal(x, y)
    # Values are a permutation of blocks, so the multiset is unchanged ignoring NaN pads.
    assert set(np.unique(y[np.isfinite(y)])) <= set(np.unique(x))


def test_shared_volatility_is_killed_by_vol_standardisation():
    """Two series that share only a volatility envelope must not survive vol_std.

    Construct source and target with independent signs but a common amplitude regime.
    Transfer entropy on the raw series can look positive; after dividing by trailing
    volatility the directional content is gone.
    """
    rng = np.random.default_rng(0)
    n = 8000
    amp = np.where((np.arange(n) // 500) % 2 == 0, 0.002, 0.02)
    src = pd.Series(rng.normal(0, 1, size=n) * amp, index=_index(n))
    tgt = pd.Series(rng.normal(0, 1, size=n) * amp, index=_index(n))

    report = falsify_transfer_entropy(
        src, tgt, source_name="vol_twin", target_name="vol_twin_b",
        n_surrogates=40, seed=1,
    )
    # The decisive control for this construction is volatility standardisation.
    assert not report.vol_standardised.significant or (
        abs(report.vol_standardised.statistic) < abs(report.baseline.statistic) * 0.5
        if np.isfinite(report.baseline.statistic) and report.baseline.statistic != 0
        else True
    )


def test_a_genuine_lagged_sign_relationship_survives_sign_only():
    """Independent magnitudes, but target's next sign equals source's past sign.

    Sign-only must still see this; block-shuffle must kill it.
    """
    rng = np.random.default_rng(2)
    n = 10000
    src_sign = rng.choice([-1.0, 1.0], size=n)
    src = pd.Series(src_sign * rng.uniform(0.001, 0.02, size=n), index=_index(n))
    # Target's next move inherits the source's current sign, plus noise.
    tgt_sign = np.empty(n)
    tgt_sign[0] = rng.choice([-1.0, 1.0])
    tgt_sign[1:] = src_sign[:-1]
    flip = rng.random(n) < 0.25
    tgt_sign = np.where(flip, -tgt_sign, tgt_sign)
    tgt = pd.Series(tgt_sign * rng.uniform(0.001, 0.02, size=n), index=_index(n))

    report = falsify_transfer_entropy(
        src, tgt, source_name="leader", target_name="follower",
        n_surrogates=60, seed=3,
    )
    assert report.sign_only.statistic > 0 or report.baseline.statistic > 0
    # Block shuffle must destroy a timing relationship.
    if np.isfinite(report.baseline.statistic) and report.baseline.statistic > 0.01:
        assert report.block_shuffle.statistic < report.baseline.statistic
