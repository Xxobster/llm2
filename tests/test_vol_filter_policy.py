"""Vol forecast must not invent sides; skip-more; filter grid frozen."""

from __future__ import annotations

import pytest

from llm2.experiments.vol_filter import (
    FROZEN_VOL_FILTER_PERCENTILE,
    load_prereg,
    validate_vol_filter_prereg,
)
from llm2.models.base import Prediction
from llm2.signals.translate import predictions_to_signals
import numpy as np


def test_magnitude_family_cannot_emit_trade_sides():
    ts = np.arange(5, dtype=np.int64) * 3_600_000
    pred = Prediction(mean=np.array([0.01, 0.02, 0.03, 0.04, 0.05]))
    with pytest.raises(ValueError, match="magnitude"):
        predictions_to_signals(ts, pred, target_family="magnitude")


def test_prereg_001_frozen_and_forbids_leverage_up():
    cfg = load_prereg()
    assert cfg["status"] == "FROZEN"
    assert cfg["filter_rule"]["percentile"] == FROZEN_VOL_FILTER_PERCENTILE
    forbidden = cfg["filter_rule"]["action_forbidden"]
    assert "increase_leverage" in forbidden
    assert "emit_long_or_short_from_vol_forecast" in forbidden
    assert cfg["filter_rule"]["action_on_trigger"] == "skip_entry"


def test_prereg_002_uses_different_entry_same_frozen_percentile():
    from llm2.experiments.vol_filter import PREREG_DIR

    cfg = load_prereg(PREREG_DIR / "volfilter_002.yaml")
    assert cfg["status"] == "FROZEN"
    assert cfg["entry_rule"]["name"] == "meanrev_24_cost_gate"
    assert cfg["filter_rule"]["percentile"] == FROZEN_VOL_FILTER_PERCENTILE
    assert cfg["filter_rule"]["inherits_frozen_filter_from"] == "volfilter_001_BTCUSDT_1h"


def test_percentile_hunting_is_rejected():
    cfg = load_prereg()
    bad = dict(cfg)
    bad["filter_rule"] = dict(cfg["filter_rule"])
    bad["filter_rule"]["percentile"] = 90
    with pytest.raises(RuntimeError, match="frozen at 75"):
        validate_vol_filter_prereg(bad)
