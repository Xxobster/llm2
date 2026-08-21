"""D-060 seal: nest-filter retune refused by default."""

from __future__ import annotations

import pytest

from llm2.research.forecast_filter_seal import (
    FROZEN_NEST_THRESHOLDS,
    refuse_nest_filter_retune,
)


def test_frozen_thresholds_are_documented():
    assert FROZEN_NEST_THRESHOLDS["vol_skip_percentile"] == 75
    assert FROZEN_NEST_THRESHOLDS["status"] == "CLOSED_TRADING_FAIL"
    assert FROZEN_NEST_THRESHOLDS["deep_retrace_thresh"] == 0.5


def test_refuse_without_allow_flags():
    with pytest.raises(SystemExit) as ei:
        refuse_nest_filter_retune(context="unit_test", argv=[])
    assert ei.value.code == 3


def test_refuse_threshold_retune_even_with_flags(monkeypatch):
    monkeypatch.setenv("LLM2_ALLOW_CLOSED_NEST_FILTER_RERUN", "1")
    with pytest.raises(SystemExit) as ei:
        refuse_nest_filter_retune(
            context="unit_test",
            argv=["--i-accept-closed-trading-fail-rerun"],
            proposed={"vol_skip_percentile": 80},
        )
    assert ei.value.code == 3


def test_allow_exact_frozen_rerun(monkeypatch, capsys):
    monkeypatch.setenv("LLM2_ALLOW_CLOSED_NEST_FILTER_RERUN", "1")
    refuse_nest_filter_retune(
        context="unit_test",
        argv=["--i-accept-closed-trading-fail-rerun"],
        proposed={"vol_skip_percentile": 75},
    )
    assert "CLOSED_NEST_FILTER_RERUN" in capsys.readouterr().out
