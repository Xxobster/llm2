"""Guardrails for the pulse-continuation experiment.

The experiment itself is closed (D-021). These tests protect the machinery that produced
the answer, because every one of them corresponds to a way the answer could have been wrong
in a flattering direction.
"""

from __future__ import annotations

import copy

import numpy as np
import pandas as pd
import pytest
import yaml

from llm2.experiments.pulse_continuation import (
    PREREG_PATH,
    load_prereg,
    sequential_entries,
    validate_prereg,
    volatility_matched_control,
)


@pytest.fixture()
def cfg() -> dict:
    return yaml.safe_load(PREREG_PATH.read_text(encoding="utf-8"))


def test_the_shipped_preregistration_validates(cfg):
    validate_prereg(cfg)


def test_a_null_stop_is_refused(cfg):
    """An unset stop means the first run would choose it, which is selection on the result."""
    bad = copy.deepcopy(cfg)
    bad["entry_rule"]["sl_pct"] = None
    with pytest.raises(RuntimeError, match="sl_pct"):
        validate_prereg(bad)


def test_missing_fold_design_is_refused(cfg):
    bad = copy.deepcopy(cfg)
    bad["fold_design"].pop("design_hash")
    with pytest.raises(RuntimeError, match="design_hash"):
        validate_prereg(bad)


def test_leverage_above_the_stop_implied_ceiling_is_refused(cfg):
    """At too much leverage the stop sits outside liquidation and never gets a chance."""
    bad = copy.deepcopy(cfg)
    bad["exit_design"]["leverage"] = 20
    with pytest.raises(RuntimeError, match="ceiling"):
        validate_prereg(bad)


def test_frozen_leverage_matches_its_own_derivation(cfg):
    sl = float(cfg["entry_rule"]["sl_pct"])
    expected = int(np.floor(1.0 / (sl + 0.005 + 0.002)))
    assert int(cfg["exit_design"]["leverage"]) == expected


def test_no_take_profit_is_frozen(cfg):
    """A take-profit would truncate the 96-bar return the hypothesis is about."""
    assert cfg["entry_rule"]["tp_pct"] is None
    assert "no_take_profit_because" in cfg["exit_design"]


def test_loaded_prereg_carries_a_hash():
    loaded = load_prereg()
    assert len(loaded["_sha256"]) == 64


# --------------------------------------------------------------------------------------
# Entry construction
# --------------------------------------------------------------------------------------


def test_sequential_entries_never_overlap():
    """Signals firing inside an open position must be dropped, not stacked.

    The pulse detector enforces a 24-bar gap while the rule holds for 96, so without this
    the fold trade count is inflated roughly fourfold against the ten-trade floor.
    """
    bars = np.array([0, 10, 30, 96, 100, 200, 250, 300], dtype=int)
    kept = sequential_entries(bars, 96)
    assert np.all(np.diff(kept) >= 96)
    assert kept[0] == 0
    assert 10 not in kept and 30 not in kept


def test_sequential_entries_is_order_independent():
    rng = np.random.default_rng(0)
    bars = np.unique(rng.integers(0, 5000, size=300))
    a = sequential_entries(bars, 96)
    b = sequential_entries(rng.permutation(bars), 96)
    assert np.array_equal(a, b)


# --------------------------------------------------------------------------------------
# The control arm
# --------------------------------------------------------------------------------------


def _synthetic(n: int = 8000, seed: int = 0) -> pd.DataFrame:
    """A series with two volatility regimes, so a matched control has work to do."""
    rng = np.random.default_rng(seed)
    vol = np.where(np.arange(n) % 2000 < 1000, 0.002, 0.02)
    ret = rng.normal(0, vol)
    close = 100 * np.exp(np.cumsum(ret))
    idx = pd.date_range("2020-01-01", periods=n, freq="1h", tz="UTC")
    return pd.DataFrame(
        {"open": close, "high": close * 1.001, "low": close * 0.999,
         "close": close, "volume": 1.0},
        index=idx,
    )


def test_control_matches_the_volatility_of_the_events():
    """A uniformly random control would compare volatile bars against quiet ones.

    Pulses cluster in volatile regimes, which have their own drift and their own costs.
    Unless the control is drawn from comparable bars, beating it proves nothing.
    """
    ohlcv = _synthetic()
    log_r = np.log(ohlcv["close"]).diff()
    vol = log_r.rolling(168, min_periods=84).std().shift(1)

    # Events taken deliberately from the high-volatility stretches only. A percentile is
    # used rather than a multiple of the median: this series is bimodal, so twice the
    # median exceeds the achievable maximum and would select nothing.
    v_arr = vol.to_numpy()
    cutoff = np.nanpercentile(v_arr, 80)
    high = np.flatnonzero(v_arr > cutoff)
    events = high[:: max(1, len(high) // 60)][:60]
    assert events.size >= 20, "test setup produced too few events to be meaningful"

    ctrl = volatility_matched_control(ohlcv, events, seed=1)
    assert ctrl.size > 10

    v = vol.to_numpy()
    ev_vol = float(np.nanmedian(v[events]))
    ct_vol = float(np.nanmedian(v[ctrl]))
    all_vol = float(np.nanmedian(v[np.isfinite(v)]))

    assert abs(ct_vol - ev_vol) / ev_vol < 0.25, "control volatility does not match the events"
    assert abs(ct_vol - ev_vol) < abs(all_vol - ev_vol), (
        "the matched control is no closer than an unmatched one would be"
    )


def test_control_does_not_reuse_the_event_bars():
    ohlcv = _synthetic()
    events = np.arange(500, 4000, 60)
    ctrl = volatility_matched_control(ohlcv, events, seed=2)
    assert not set(ctrl.tolist()) & set(events.tolist())


def test_control_is_reproducible_from_its_seed():
    ohlcv = _synthetic()
    events = np.arange(500, 4000, 60)
    a = volatility_matched_control(ohlcv, events, seed=7)
    b = volatility_matched_control(ohlcv, events, seed=7)
    assert np.array_equal(a, b)
