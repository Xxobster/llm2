"""Fill-wait LIVE-DATA-001 cancel policy (thresholds unchanged)."""

from llm2.live.pivot_runner import (
    CONFIRM_TIMEOUT_SEC,
    fill_wait_gate_action,
)


def test_instant_cancel_collector_and_ahead():
    assert (
        fill_wait_gate_action("COLLECTOR_ERROR", first_fail_mono=None, now_mono=0.0)
        == "cancel"
    )
    assert (
        fill_wait_gate_action("CANDLE_AHEAD", first_fail_mono=10.0, now_mono=10.1)
        == "cancel"
    )


def test_clock_skew_waits_confirm_then_cancels():
    assert (
        fill_wait_gate_action("CLOCK_SKEW", first_fail_mono=None, now_mono=0.0)
        == "wait"
    )
    assert (
        fill_wait_gate_action(
            "CLOCK_SKEW", first_fail_mono=0.0, now_mono=CONFIRM_TIMEOUT_SEC - 1
        )
        == "wait"
    )
    assert (
        fill_wait_gate_action(
            "CLOCK_SKEW", first_fail_mono=0.0, now_mono=CONFIRM_TIMEOUT_SEC
        )
        == "cancel"
    )


def test_stale_and_server_time_wait():
    assert (
        fill_wait_gate_action("CANDLE_STALE", first_fail_mono=1.0, now_mono=2.0)
        == "wait"
    )
    assert (
        fill_wait_gate_action("SERVER_TIME_FAIL", first_fail_mono=1.0, now_mono=2.0)
        == "wait"
    )


def test_unknown_code_cancels():
    assert fill_wait_gate_action("WEIRD", first_fail_mono=None, now_mono=0.0) == "cancel"
