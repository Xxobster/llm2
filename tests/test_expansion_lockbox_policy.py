"""D-037 expansion lockbox one-shot policy + pack train cut."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest
import yaml

from llm2.paths import FORWARD_LOCKBOX_START, ROOT
from llm2.research_policy import (
    EXPANSION_LOCKBOX_FINAL_GENERATION,
    PolicyError,
    refuse_already_peeked_on_expansion_pristine_set,
    refuse_expansion_lockbox_multi_arm,
    refuse_promotion_from_expansion_lockbox_pf,
)
from llm2.validation.folds import OUTER_FOLD_RANGES

PREREG = ROOT / "configs" / "preregister" / f"{EXPANSION_LOCKBOX_FINAL_GENERATION}.yaml"


def test_prereg_exists_and_frozen():
    assert PREREG.is_file()
    data = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    assert data["generation_id"] == EXPANSION_LOCKBOX_FINAL_GENERATION
    assert data["status"] == "FROZEN"
    assert data["open_rules"]["multi_arm_search"] == "FORBIDDEN"
    assert data["train_rules"]["pack_bars_strictly_before"] == FORWARD_LOCKBOX_START
    excluded = {str(x).upper() for x in data["excluded_already_peeked"]}
    for bad in ("ETHUSDT", "LINKUSDT", "VETUSDT", "ADAUSDT"):
        assert bad in excluded
    cands = {str(c["symbol"]).upper() for c in data["pristine_candidates"]}
    assert cands.isdisjoint(excluded)
    assert "BNBUSDT" in cands and "XRPUSDT" in cands


def test_refuse_multi_arm_n_arms():
    with pytest.raises(PolicyError, match="multi-arm"):
        refuse_expansion_lockbox_multi_arm(n_arms=8)
    refuse_expansion_lockbox_multi_arm(n_arms=1)


def test_refuse_multi_arm_argv():
    with pytest.raises(PolicyError, match="search flag"):
        refuse_expansion_lockbox_multi_arm(argv=["--symbols", "BNBUSDT", "--grid"])
    with pytest.raises(PolicyError, match="search flag"):
        refuse_expansion_lockbox_multi_arm(argv=["--k=7"])
    refuse_expansion_lockbox_multi_arm(argv=["--symbols", "BNBUSDT,XRPUSDT"])


def test_refuse_already_peeked():
    with pytest.raises(PolicyError, match="already peeeed"):
        refuse_already_peeked_on_expansion_pristine_set(symbol="LINKUSDT")
    refuse_already_peeked_on_expansion_pristine_set(symbol="BNBUSDT")


def test_refuse_promotion_from_lockbox_pf():
    with pytest.raises(PolicyError, match="outer-fold settle"):
        refuse_promotion_from_expansion_lockbox_pf(
            claim="deploy_BNB",
            evidence_class="LOCKBOX_OPENED_CONTAMINATED",
        )
    refuse_promotion_from_expansion_lockbox_pf(
        claim="quote_settle",
        evidence_class="LOCKBOX_OPENED_CONTAMINATED",
        quote_settle=True,
    )


def test_runner_imports_refuse_on_multi_arm():
    from scripts.run_expansion_lockbox_once import refuse_multi_arm

    with pytest.raises(PolicyError):
        refuse_multi_arm(["--grid", "true"])


def test_pack_train_masks_match_fold_v2(tmp_path: Path):
    """Document the exact cuts used by build_structure_symbol_pack (D-037)."""
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    last_oos = pd.Timestamp(OUTER_FOLD_RANGES[-1][0], tz="UTC")
    assert last_oos < lock
    # Synthetic bars: train only before last_oos; features/package drop lockbox
    idx = pd.date_range("2024-01-01", periods=48, freq="h", tz="UTC")
    # include dates straddling both cuts
    idx = idx.union(pd.date_range("2025-09-01", periods=48, freq="h", tz="UTC"))
    idx = idx.union(pd.date_range("2025-10-01", periods=48, freq="h", tz="UTC"))
    idx = idx.union(pd.date_range("2026-04-01", periods=48, freq="h", tz="UTC"))
    idx = idx.union(pd.date_range("2026-05-01", periods=48, freq="h", tz="UTC"))
    pre_lock = idx[idx < lock]
    train = pre_lock[pre_lock < last_oos]
    assert (train < last_oos).all()
    assert (pre_lock < lock).all()
    assert not (idx[idx >= lock] < lock).any()
    # strategy fields expected on frozen packs
    strategy = {
        "trained_until_exclusive": str(last_oos),
        "lockbox_start": FORWARD_LOCKBOX_START,
    }
    t = pd.Timestamp(strategy["trained_until_exclusive"], tz="UTC")
    assert t < pd.Timestamp(strategy["lockbox_start"], tz="UTC")
    _ = tmp_path  # keep fixture available for future pack write tests


def test_assert_pack_train_cut_helper():
    from scripts.run_expansion_lockbox_once import assert_pack_train_cut

    pack = ROOT / "artifacts" / "live_packs" / "structure_v1_ethusdt_direction"
    if not (pack / "strategy.json").is_file():
        pytest.skip("ETH direction pack not present")
    notes = assert_pack_train_cut(pack)
    assert notes["train_cut_ok"] is True
