"""Peek log + D-036 contamination policy."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from llm2.evidence.peek_log import (
    POST_MULTITRADE_FREEZE_START,
    append_peek,
    is_post_freeze_window,
    read_peeks,
    seed_known_multitrade_peeks,
    window_overlaps_contaminated_lockbox,
)
from llm2.paths import FORWARD_LOCKBOX_START
from llm2.research_policy import (
    PolicyError,
    classify_evidence_for_window,
    refuse_copy_as_pristine_holdout,
    refuse_lockbox_multitrade_knob_as_promotion,
    require_post_freeze_for_multitrade_param_claim,
)


def test_copy_does_not_reset_pristine():
    with pytest.raises(PolicyError, match="Copying"):
        refuse_copy_as_pristine_holdout(claimed_pristine=True, same_calendar_window=True)


def test_lockbox_multitrade_promotion_refused():
    with pytest.raises(PolicyError, match="diagnostic"):
        refuse_lockbox_multitrade_knob_as_promotion(
            claim="promote_K8",
            evidence_class="LOCKBOX_OPENED_CONTAMINATED",
            window_start=FORWARD_LOCKBOX_START,
            window_end="2026-08-04",
        )


def test_post_freeze_required_for_new_param_claim():
    with pytest.raises(PolicyError, match="POST_MULTITRADE_FREEZE"):
        require_post_freeze_for_multitrade_param_claim(
            claim="new_K",
            window_start=FORWARD_LOCKBOX_START,
            prereg_path="configs/preregister/structure_v1_eth_multitrade_v1_1_post_freeze_001.yaml",
        )
    require_post_freeze_for_multitrade_param_claim(
        claim="new_K",
        window_start=POST_MULTITRADE_FREEZE_START,
        prereg_path="configs/preregister/structure_v1_eth_multitrade_v1_1_post_freeze_001.yaml",
    )


def test_post_freeze_needs_prereg():
    with pytest.raises(PolicyError, match="prereg"):
        require_post_freeze_for_multitrade_param_claim(
            claim="new_K",
            window_start=POST_MULTITRADE_FREEZE_START,
            prereg_path=None,
        )


def test_window_overlap_and_classify():
    assert window_overlaps_contaminated_lockbox("2026-05-01", "2026-08-04")
    assert not window_overlaps_contaminated_lockbox("2026-08-05", "2026-09-01")
    assert is_post_freeze_window("2026-08-05")
    assert not is_post_freeze_window("2026-08-04")
    assert (
        classify_evidence_for_window(
            window_start="2026-05-01",
            window_end="2026-08-04",
            experiment_family="multitrade_knob",
        )
        == "LOCKBOX_OPENED_CONTAMINATED_DIAGNOSTIC_ONLY"
    )


def test_append_and_seed(tmp_path: Path, monkeypatch):
    log = tmp_path / "peek_log.jsonl"
    monkeypatch.setenv("LLM2_PEEK_LOG", str(log))
    append_peek(
        experiment_id="unit_test_peek",
        window_start=FORWARD_LOCKBOX_START,
        window_end="2026-08-04",
        purpose="unit",
        arms="a,b",
        n_arms=2,
        path=log,
    )
    rows = read_peeks(path=log)
    assert len(rows) == 1
    assert rows[0]["experiment_id"] == "unit_test_peek"
    n = seed_known_multitrade_peeks(path=log, force=True)
    assert n >= 4
    # force re-seed adds more lines; second non-force on fresh path with marker
    log2 = tmp_path / "peek2.jsonl"
    seed_known_multitrade_peeks(path=log2, force=False)
    again = seed_known_multitrade_peeks(path=log2, force=False)
    assert again == 0
    meta = json.loads((log2.parent / "peek_log_meta.json").read_text(encoding="utf-8"))
    assert meta["post_multitrade_freeze_start"] == POST_MULTITRADE_FREEZE_START
