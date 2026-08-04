"""Machine-enforceable research methodology policies."""

from __future__ import annotations

import pytest

from llm2.research_policy import (
    CRITICAL_STEP_MARKERS,
    EventStudySpec,
    EstimatorResult,
    LevelClaim,
    LockboxPreregGate,
    MIN_SIZE_EQUITY_CAVEAT,
    PolicyError,
    STRUCTURE_SIGNS_INSPECTED,
    WAREHOUSE_AUDIT_BOUND,
    WAREHOUSE_BACKED_SPACES,
    is_critical_failure,
    prefer_raw_return_when_disagreement,
    refuse_abc_bounce_reopen_while_underpowered,
    refuse_abc_continuation_without_lockbox_prereg,
    refuse_abc_video_claim_as_evidence,
    refuse_research_chart_as_deploy_evidence,
    refuse_structure_sign_inversion,
    refuse_wavetheory_simulator_for_abc,
    require_estimator_self_control,
    require_lockbox_prereg_frozen,
    require_matched_control,
    require_placebo_arm,
    require_warehouse_audit_bound,
    require_warehouse_legs_for_abc,
    stamp_min_size_equity_caveat,
    unbound_warehouse_spaces,
)


def test_placebo_arm_is_mandatory_for_level_claims():
    with pytest.raises(PolicyError, match="placebo"):
        require_placebo_arm(
            LevelClaim(
                name="round_number",
                real_ratios=(1000.0,),
                placebo_ratios=(),
                anchors="prior day high/low",
                proximity_band="0.5 trailing vol",
            )
        )


def test_placebo_must_not_overlap_the_claim():
    with pytest.raises(PolicyError, match="coincide"):
        require_placebo_arm(
            LevelClaim(
                name="fib",
                real_ratios=(0.618,),
                placebo_ratios=(0.618, 0.44),
                anchors="confirmed swings",
                proximity_band="0.5 trailing vol",
            )
        )


def test_a_proper_placebo_arm_passes():
    require_placebo_arm(
        LevelClaim(
            name="fib",
            real_ratios=(0.382, 0.5, 0.618),
            placebo_ratios=(0.15, 0.44, 0.70),
            anchors="confirmed swing high/low",
            proximity_band="0.5 trailing vol",
        )
    )


def test_warehouse_spaces_without_an_audit_are_refused():
    assert unbound_warehouse_spaces() == frozenset()
    require_warehouse_audit_bound("macro_v1")
    require_warehouse_audit_bound("structure_v1")
    require_warehouse_audit_bound("crosspair_v1")
    require_warehouse_audit_bound("xs_v1")
    require_warehouse_audit_bound("ohlcv_v1")  # not warehouse-backed — no-op


def test_every_bound_audit_space_is_declared_warehouse_backed():
    """A space cannot be 'audited' without being acknowledged as warehouse-backed."""
    assert WAREHOUSE_AUDIT_BOUND <= WAREHOUSE_BACKED_SPACES
    assert WAREHOUSE_BACKED_SPACES <= WAREHOUSE_AUDIT_BOUND


def test_matched_control_is_mandatory_for_event_studies():
    with pytest.raises(PolicyError, match="control arm"):
        require_matched_control(
            EventStudySpec(
                name="pulse",
                event_definition="3-sigma up move",
                treatment_arm="long_after_up_pulse",
                control_arm="",
                matching="trailing volatility within 15%",
            )
        )
    with pytest.raises(PolicyError, match="matching"):
        require_matched_control(
            EventStudySpec(
                name="pulse",
                event_definition="3-sigma up move",
                treatment_arm="long_after_up_pulse",
                control_arm="random_bars",
                matching="",
            )
        )


def test_a_volatility_matched_control_passes():
    require_matched_control(
        EventStudySpec(
            name="pulse",
            event_definition="3-sigma up move",
            treatment_arm="long_after_up_pulse",
            control_arm="random_vol_matched",
            matching="trailing volatility within 15 percent",
        )
    )


def test_estimator_self_control_is_mandatory():
    with pytest.raises(PolicyError, match="self-control"):
        require_estimator_self_control(
            EstimatorResult(
                name="wave_lead",
                statistic=0.48,
                self_control_statistic=None,
                self_control_description="",
            )
        )


def test_estimator_that_matches_its_self_control_is_refused():
    """The wave artefact: claimed r=0.48, self-lead r=0.57."""
    with pytest.raises(PolicyError, match="self-control"):
        require_estimator_self_control(
            EstimatorResult(
                name="wave_lead|ETH->BTC",
                statistic=0.48,
                self_control_statistic=0.57,
                self_control_description="BTC@15.3 vs BTC@7.1",
            )
        )


def test_estimator_that_beats_its_self_control_passes():
    require_estimator_self_control(
        EstimatorResult(
            name="genuine_lead",
            statistic=0.60,
            self_control_statistic=0.05,
            self_control_description="same series, two filter periods",
        )
    )


def test_structure_sign_inversion_is_refused_without_lockbox_prereg():
    assert "struct_HH" in STRUCTURE_SIGNS_INSPECTED
    with pytest.raises(PolicyError, match="invert"):
        refuse_structure_sign_inversion(
            feature="struct_HH",
            proposed_side_rule="short after HH",
        )
    refuse_structure_sign_inversion(
        feature="struct_HH",
        proposed_side_rule="short after HH",
        preregistered_on_lockbox=True,
    )


def test_abc_continuation_closed_without_lockbox_prereg():
    with pytest.raises(PolicyError, match="CLOSED"):
        refuse_abc_continuation_without_lockbox_prereg(claim="A_equals_C_continuation")
    refuse_abc_continuation_without_lockbox_prereg(
        claim="A_equals_C_continuation", preregistered_on_lockbox=True
    )


def test_wavetheory_simulator_refused_for_abc():
    with pytest.raises(PolicyError, match="VOID"):
        refuse_wavetheory_simulator_for_abc(
            r"C:\projects\wavetheory\src\backtest\wave_strategy.py"
        )
    with pytest.raises(PolicyError, match="VOID"):
        refuse_wavetheory_simulator_for_abc("module using fractal_pivots")
    refuse_wavetheory_simulator_for_abc("indicators.legs warehouse confirmed swings")


def test_warehouse_legs_required_for_abc_geometry():
    require_warehouse_legs_for_abc("indicators.legs")
    require_warehouse_legs_for_abc("warehouse_legs ratios")
    with pytest.raises(PolicyError, match="confirmed-swing warehouse"):
        require_warehouse_legs_for_abc("hand_drawn_chart_abc")


def test_min_size_equity_caveat_stamped_and_charts_refuse_deploy():
    stamped = stamp_min_size_equity_caveat({"pooled_pf": 1.5})
    assert stamped["equity_is_tradable_edge"] is False
    assert "MIN_EXCHANGE" in stamped["min_size_equity_caveat"]
    assert "MIN_EXCHANGE" in MIN_SIZE_EQUITY_CAVEAT
    with pytest.raises(PolicyError, match="not deploy evidence"):
        refuse_research_chart_as_deploy_evidence("finplot")


def test_lockbox_prereg_requires_frozen_exits_and_matched_control():
    require_lockbox_prereg_frozen(
        LockboxPreregGate(
            name="ok",
            status="FROZEN",
            evaluation="forward_lockbox_once",
            frozen_utc="2026-08-03T12:55:00Z",
            leverage=10,
            sl_pct=0.04,
            control_policy="require_matched_control",
            control_arm_names=("volatility_matched_random",),
        )
    )
    with pytest.raises(PolicyError, match="not FROZEN"):
        require_lockbox_prereg_frozen(
            LockboxPreregGate(
                name="draft",
                status="DRAFT",
                evaluation="forward_lockbox_once",
                frozen_utc="2026-08-03T12:55:00Z",
                leverage=10,
                sl_pct=0.04,
                control_policy="require_matched_control",
                control_arm_names=("volatility_matched_random",),
            )
        )
    with pytest.raises(PolicyError, match="matched control"):
        require_lockbox_prereg_frozen(
            LockboxPreregGate(
                name="noctrl",
                status="FROZEN",
                evaluation="forward_lockbox_once",
                frozen_utc="2026-08-03T12:55:00Z",
                leverage=10,
                sl_pct=0.04,
                control_policy="",
                control_arm_names=("volatility_matched_random",),
            )
        )


def test_abc_bounce_underpowered_hold_blocks_early_reopen():
    with pytest.raises(PolicyError, match="UNDERPOWERED"):
        refuse_abc_bounce_reopen_while_underpowered(
            family_status="UNDERPOWERED_HOLD",
            prereg_sha256="abc",
            frozen_prereg_sha256="abc",
            projected_sequential_trades=46,
        )
    with pytest.raises(PolicyError, match="hash changed"):
        refuse_abc_bounce_reopen_while_underpowered(
            family_status="UNDERPOWERED_HOLD",
            prereg_sha256="widened",
            frozen_prereg_sha256="abc",
            projected_sequential_trades=80,
        )
    # Enough projected trades under the same digest may reopen.
    refuse_abc_bounce_reopen_while_underpowered(
        family_status="UNDERPOWERED_HOLD",
        prereg_sha256="abc",
        frozen_prereg_sha256="abc",
        projected_sequential_trades=50,
    )


def test_abc_video_extraction_is_not_evidence():
    with pytest.raises(PolicyError, match="ABC_RULES_TESTED"):
        refuse_abc_video_claim_as_evidence("Wave Trading video extraction notes")
    refuse_abc_video_claim_as_evidence("indicators.legs warehouse measurement")


def test_critical_failure_detector_catches_parquet_and_conformance():
    assert is_critical_failure(ImportError("no working parquet engine"))
    assert is_critical_failure(PolicyError("placebo missing"))
    assert is_critical_failure(RuntimeError("tradesim conformance is not green"))
    assert not is_critical_failure(ValueError("fold had zero signals"))
    assert "write_fold_parquet" in CRITICAL_STEP_MARKERS


def test_wave_only_lead_is_discarded_in_favour_of_raw_returns():
    assert (
        prefer_raw_return_when_disagreement(
            wave_statistic=0.4,
            raw_return_statistic=0.01,
            wave_significant=True,
            raw_significant=False,
        )
        == "raw_preferred_wave_discarded"
    )
    assert (
        prefer_raw_return_when_disagreement(
            wave_statistic=0.4,
            raw_return_statistic=0.3,
            wave_significant=True,
            raw_significant=True,
        )
        == "raw_and_wave"
    )
