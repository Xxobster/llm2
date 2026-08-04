"""Tests for the collapsed dollar/commodity factor."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.dollarfactor import COMMODITY_BLOCK, DOLLAR_BLOCK, fit_factor


def test_sign_convention_covers_both_quote_directions():
    """A block with every sign the same would mean the alignment step was forgotten.

    EURUSD rising and USDJPY rising say opposite things about the dollar. If the map did not
    invert one of them, the first principal component would largely encode which way each
    pair is quoted rather than the dollar itself.
    """
    assert DOLLAR_BLOCK["EURUSD"] == -DOLLAR_BLOCK["DXY"]
    assert DOLLAR_BLOCK["USDJPY"] == DOLLAR_BLOCK["DXY"]
    assert set(DOLLAR_BLOCK.values()) == {1, -1}
    assert set(COMMODITY_BLOCK.values()) == {-1}


def test_factor_recovers_a_planted_common_move():
    rng = np.random.default_rng(0)
    n = 5000
    common = rng.normal(0, 1, size=n)
    cols = {f"s{i}": common + rng.normal(0, 0.3, size=n) for i in range(6)}
    load, explained = fit_factor(pd.DataFrame(cols))
    assert explained > 0.8, "a block that is one factor should be recognised as one factor"
    assert np.all(load > 0), "loadings should share a sign when the series share a driver"


def test_independent_series_do_not_collapse_to_one_factor():
    rng = np.random.default_rng(1)
    cols = {f"s{i}": rng.normal(0, 1, size=5000) for i in range(6)}
    _, explained = fit_factor(pd.DataFrame(cols))
    assert explained < 0.35, "unrelated series must not be described as a single factor"


def test_loading_orientation_is_stable():
    """Sign of the first component is arbitrary in SVD; the code must pin it."""
    rng = np.random.default_rng(2)
    common = rng.normal(0, 1, size=3000)
    df = pd.DataFrame({f"s{i}": common + rng.normal(0, 0.2, size=3000) for i in range(4)})
    load_a, _ = fit_factor(df)
    load_b, _ = fit_factor(df * -1.0)
    assert load_a.sum() > 0 and load_b.sum() > 0


def test_scaling_one_series_does_not_hijack_the_factor():
    """Without standardisation the loudest series becomes the factor."""
    rng = np.random.default_rng(3)
    common = rng.normal(0, 1, size=4000)
    df = pd.DataFrame(
        {
            "quiet_a": common + rng.normal(0, 0.2, size=4000),
            "quiet_b": common + rng.normal(0, 0.2, size=4000),
            "quiet_c": common + rng.normal(0, 0.2, size=4000),
            "loud": 500.0 * rng.normal(0, 1, size=4000),
        }
    )
    load, _ = fit_factor(df)
    assert abs(load[3]) < max(abs(load[:3])), "the high-variance series dominated the factor"
