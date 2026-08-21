"""Unit tests for limit blend / pull placement (no look-ahead)."""

from llm2.pivot.strategy.limit_placement import (
    apply_placement,
    blend_limit_return,
    pull_toward_market_lr,
)


def test_pull_toward_market_short_and_long():
    assert pull_toward_market_lr(0.02, is_short=True, pull=0.01) == 0.01
    assert pull_toward_market_lr(-0.02, is_short=False, pull=0.01) == -0.01


def test_blend_75_1pct_matches_user_weights():
    # short: raw +2%, adj = +1%, blend = 0.75*1% + 0.25*2% = 1.25%
    b = blend_limit_return(0.02, is_short=True, w_adj=0.75, pull=0.01)
    assert abs(b - 0.0125) < 1e-12
    # long: raw -2%, adj = -1%, blend = 0.75*(-1%) + 0.25*(-2%) = -1.25%
    b2 = blend_limit_return(-0.02, is_short=False, w_adj=0.75, pull=0.01)
    assert abs(b2 - (-0.0125)) < 1e-12


def test_apply_modes():
    assert apply_placement(0.02, is_short=True, mode="raw") == 0.02
    assert abs(apply_placement(0.02, is_short=True, mode="blend_75_1pct") - 0.0125) < 1e-12
    assert abs(
        apply_placement(0.02, is_short=True, mode="miss_comp", pull_bps=100.0) - 0.01
    ) < 1e-12
