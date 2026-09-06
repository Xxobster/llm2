"""EXEC-021 retest helpers: engine pin and min-size live vote."""

from __future__ import annotations

import pytest

from scripts.run_exec021_maker_limit_retest import min_live_vote, require_engine


def test_require_engine_is_tradesim_1_1_0_botsgeneral():
    extra = require_engine()
    assert extra["tradesim_version"] == "1.1.0"
    assert "botsgeneral" in extra["tradesim_file"].lower()


@pytest.mark.parametrize(
    "row, want",
    [
        ({"status": "ERROR"}, "no"),
        (
            {
                "status": "RAN",
                "window": "inner_pre_2022",
                "n_trades": 400,
                "profit_factor": 2.0,
                "entry_bar_exit_rate": 0.1,
                "trades_per_month": 10,
            },
            "no_inner_only",
        ),
        (
            {
                "status": "RAN",
                "window": "pre_lockbox_oos",
                "n_trades": 683,
                "profit_factor": 1.36,
                "entry_bar_exit_rate": 0.09,
                "trades_per_month": 13.3,
            },
            "yes_min_size_limit_only",
        ),
        (
            {
                "status": "RAN",
                "window": "pre_lockbox_oos",
                "n_trades": 490,
                "profit_factor": 1.96,
                "entry_bar_exit_rate": 0.47,
                "trades_per_month": 12.0,
            },
            "no_entry_bar_noise",
        ),
        (
            {
                "status": "RAN",
                "window": "pre_lockbox_oos",
                "n_trades": 80,
                "profit_factor": 1.05,
                "entry_bar_exit_rate": 0.10,
                "trades_per_month": 8.0,
            },
            "no",
        ),
    ],
)
def test_min_live_vote(row, want):
    assert min_live_vote(row) == want
