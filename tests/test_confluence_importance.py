"""Helpers for confluence importance (correlation prune)."""

from __future__ import annotations

import pandas as pd

from llm2.confluence.importance import prune_duplicates


def test_prune_keeps_higher_intent_exp():
    corr = pd.DataFrame(
        [[1.0, 0.91, 0.1], [0.91, 1.0, 0.05], [0.1, 0.05, 1.0]],
        index=["rsi_cross_up_30", "stoch_cross_up_20", "pulse_extend"],
        columns=["rsi_cross_up_30", "stoch_cross_up_20", "pulse_extend"],
    )
    out = prune_duplicates(
        corr,
        {"rsi_cross_up_30": 0.01, "stoch_cross_up_20": 0.02, "pulse_extend": 0.0},
        abs_thr=0.8,
    )
    assert "stoch_cross_up_20" in out["keep"]
    assert "rsi_cross_up_30" not in out["keep"]
    assert "pulse_extend" in out["keep"]
