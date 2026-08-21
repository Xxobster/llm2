"""Four-proof gate must be mandatory and fail closed."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from llm2.evidence.four_proof import (
    PROOF_KEYS,
    attach_four_proof_to_pack,
    micro_runner_has_no_fill_ast,
    proof_no_live_feature_fill,
    refuse_pred_mismatch_hard_stop,
    refuse_warehouse_leakage_pass_alone,
    require_four_proof_hashes_on_pack,
)
from llm2.research_policy import PolicyError


def test_no_live_feature_fill_proof_passes():
    p = proof_no_live_feature_fill()
    assert p["ok"], p
    assert micro_runner_has_no_fill_ast()


def test_warehouse_leakage_pass_alone_refused():
    with pytest.raises(PolicyError, match="not sufficient"):
        refuse_warehouse_leakage_pass_alone(
            space="structure_v1",
            leakage_passed=True,
            four_proof_ok=False,
        )


def test_pred_mismatch_hard_stop():
    with pytest.raises(PolicyError, match="PRED_MISMATCH_HARD_STOP"):
        refuse_pred_mismatch_hard_stop(n_bars_pred_differ=3, context="test")


def test_freeze_requires_four_proof_hashes(tmp_path: Path):
    pack = tmp_path / "pack"
    pack.mkdir()
    (pack / "pack_meta.json").write_text(json.dumps({"version_id": "t"}), encoding="utf-8")
    with pytest.raises(PolicyError, match="four_proof"):
        require_four_proof_hashes_on_pack(pack)


def test_attach_four_proof_writes_hashes(tmp_path: Path):
    pack = tmp_path / "pack"
    pack.mkdir()
    (pack / "pack_meta.json").write_text(json.dumps({"version_id": "t"}), encoding="utf-8")
    summary = {
        "ok": True,
        "artifact_hashes": {k: "a" * 64 for k in PROOF_KEYS},
        "summary_sha256": "b" * 64,
        "artifact_dir": "artifacts/evidence/four_proof/x",
        "stamp": "20260806T000000Z",
        "proofs_ok": {k: True for k in PROOF_KEYS},
    }
    meta = attach_four_proof_to_pack(pack, summary)
    assert meta["four_proof_ok"] is True
    require_four_proof_hashes_on_pack(pack)
