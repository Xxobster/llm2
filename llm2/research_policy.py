"""Research methodology policies that are machine-enforceable.

These are the standing rules that were learned the hard way. Encoding them as functions
that raise, rather than as prose in a decision log, means a future experiment cannot quietly
skip them.

Policies covered:

- **Placebo arm for level claims.** Round numbers, pivot points, VWAP bands, moving averages
  as support — all have the same confound the Fibonacci test exposed. A level claim without
  a placebo control is not evidence.
- **Confirmation-time audit for warehouse features.** A green leakage report is insufficient:
  it passed on the weekly look-ahead bug because truncating OHLCV does not truncate the
  database the features are loaded from.
- **Matched control for event studies.** The pulse effect was real, survived FDR, and was
  still drift — only the volatility-matched random-entry control revealed it.
- **Estimator self-control.** When a result comes out of a filter or an estimator, run that
  estimator against itself before believing it. The wave "lead" was a series leading itself.
- **Do not invert non-significant signs.** The structure point estimates lean the wrong way;
  fitting a contrarian rule to them after seeing the results is selection on the same data.
- **Min-exchange equity caveat.** Smooth wallet equity under research_sizing MIN_EXCHANGE on a
  large wallet is dust-size accounting, not a tradable edge or deployable sizing evidence.
- **No research-chart VPS deploy.** Finplot / settle charts never authorize live; require a
  live certificate with funding + Mark parity and explicit user deploy authorization.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable, Mapping, Sequence

MIN_SIZE_EQUITY_CAVEAT = (
    "Wallet equity / maximum drawdown under research_sizing MIN_EXCHANGE "
    "(minimum exchange size) on a large wallet is not tradable-edge evidence. "
    "Smooth curves are expected at dust size; do not treat them as deployable sizing."
)

# Feature spaces that load from a warehouse rather than being computed from the OHLCV the
# leakage audit truncates. Each must carry a confirmation-time / publication-time audit
# bound as a test; a green prefix-invariance report alone is not sufficient.
WAREHOUSE_BACKED_SPACES: frozenset[str] = frozenset(
    {
        "macro_v1",
        "structure_v1",
        "crosspair_v1",  # loads peer OHLCV from the warehouse
        "xs_v1",
    }
)

# Spaces that already have a direct confirmation-time / truncation audit bound as a
# regression test. Adding a space to WAREHOUSE_BACKED_SPACES without also adding it here
# must fail the build.
WAREHOUSE_AUDIT_BOUND: frozenset[str] = frozenset(
    {
        "macro_v1",  # tests/test_macro_causality.py
        "structure_v1",  # tests/test_structure_causality.py
        "crosspair_v1",  # tests/test_panel_causality.py
        "xs_v1",  # tests/test_panel_causality.py
    }
)

# Structural sign patterns that were inspected on the training window and must not be
# inverted into a trading rule without a fresh preregistration on the forward lockbox.
STRUCTURE_SIGNS_INSPECTED: frozenset[str] = frozenset(
    {
        "struct_HH",
        "struct_HL",
        "struct_LH",
        "struct_LL",
        "struct_dir",
        "structure_bias",
        "last_structure_label",
    }
)


class PolicyError(RuntimeError):
    """A research-methodology rule was violated."""


# --------------------------------------------------------------------------------------
# Placebo arms for level claims
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class LevelClaim:
    """A claim that price reacts at a named level.

    ``real_ratios`` are the ratios or offsets under test. ``placebo_ratios`` must be
    non-empty, drawn from the same anchors, through the same proximity band, and must not
    include any of the real ratios. The Fibonacci diagnostic is the reference implementation.
    """

    name: str
    real_ratios: tuple[float, ...]
    placebo_ratios: tuple[float, ...]
    anchors: str  # free-text description of the shared anchor construction
    proximity_band: str


def require_placebo_arm(claim: LevelClaim) -> None:
    """Refuse a level claim that has no placebo arm, or whose placebos overlap the claim."""
    if not claim.placebo_ratios:
        raise PolicyError(
            f"level claim {claim.name!r} has no placebo arm. Round numbers, pivots, VWAP "
            "bands and moving averages as support all have the same confound the Fibonacci "
            "test exposed: reacting near a level can be the mere fact of sitting inside a "
            "range. A level claim without a placebo control is not evidence."
        )
    overlap = set(claim.real_ratios) & set(claim.placebo_ratios)
    if overlap:
        raise PolicyError(
            f"level claim {claim.name!r} has placebo ratios that coincide with the real "
            f"ones: {sorted(overlap)}. Placebos must be deliberately unremarkable."
        )
    if not claim.anchors.strip():
        raise PolicyError(
            f"level claim {claim.name!r} must name the shared anchor construction so the "
            "placebo arm is computed from the same points."
        )


# --------------------------------------------------------------------------------------
# Warehouse confirmation-time audits
# --------------------------------------------------------------------------------------


def require_warehouse_audit_bound(space: str) -> None:
    """Refuse to trust a warehouse-backed space that has no confirmation-time audit test."""
    if space not in WAREHOUSE_BACKED_SPACES:
        return
    if space not in WAREHOUSE_AUDIT_BOUND:
        raise PolicyError(
            f"feature space {space!r} loads from a warehouse, but no confirmation-time / "
            "publication-time audit is bound as a regression test. A green leakage report is "
            "insufficient: prefix-invariance truncates OHLCV and does not truncate the "
            "database the features are loaded from (D-016 weekly look-ahead). Add the space "
            "to WAREHOUSE_AUDIT_BOUND only after the audit test exists."
        )


def unbound_warehouse_spaces() -> frozenset[str]:
    return WAREHOUSE_BACKED_SPACES - WAREHOUSE_AUDIT_BOUND


# --------------------------------------------------------------------------------------
# Min-exchange equity caveat (standing research honesty rule)
# --------------------------------------------------------------------------------------


def stamp_min_size_equity_caveat(report: dict[str, Any]) -> dict[str, Any]:
    """Attach the standing MIN_EXCHANGE equity caveat to a settlement / pack report."""
    report = dict(report)
    report["min_size_equity_caveat"] = MIN_SIZE_EQUITY_CAVEAT
    report["equity_is_tradable_edge"] = False
    return report


def refuse_research_chart_as_deploy_evidence(source: str = "finplot") -> None:
    """Fail closed if a research chart is treated as VPS / live authorization."""
    raise PolicyError(
        f"{source} / research charts are not deploy evidence. Require a frozen live pack, "
        "funding + Mark/tier parity, configs/live certificate status=AUTHORIZED with "
        "authorized_by_user=true, and an explicit user deploy command naming host and account."
    )


def refuse_silent_lockbox_peek(
    *,
    accepted_contamination: bool,
    window_start: str,
    open_finplot: bool = False,
    accepted_finplot: bool = False,
    experiment_id: str = "unspecified",
) -> None:
    """Delegate to the sealed lockbox gate (Finplot double opt-in)."""
    from llm2.evidence.lockbox_guard import require_lockbox_access

    require_lockbox_access(
        experiment_id=experiment_id,
        window_start=window_start,
        purpose="policy_refuse_silent_lockbox_peek",
        accepted_contamination=accepted_contamination,
        open_finplot=open_finplot,
        accepted_finplot=accepted_finplot,
        notes="via refuse_silent_lockbox_peek",
    )


# --------------------------------------------------------------------------------------
# Matched controls for event studies
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class EventStudySpec:
    """An event-study hypothesis that must carry a matched control arm."""

    name: str
    event_definition: str
    treatment_arm: str
    control_arm: str
    matching: str  # e.g. "trailing volatility within 15 percent"


def require_matched_control(spec: EventStudySpec) -> None:
    """Refuse an event study whose control is missing or is just 'random bars'."""
    if not spec.control_arm.strip():
        raise PolicyError(
            f"event study {spec.name!r} has no control arm. The pulse continuation effect "
            "was real, survived FDR, and was still the return to being long BTCUSDT for "
            "four days — only the volatility-matched random-entry control revealed it."
        )
    if not spec.matching.strip():
        raise PolicyError(
            f"event study {spec.name!r} names a control but not a matching rule. A "
            "uniformly random control compares volatile events against quiet bars and "
            "proves nothing."
        )
    lowered = spec.matching.lower()
    if "volatil" not in lowered and "match" not in lowered and "stratif" not in lowered:
        raise PolicyError(
            f"event study {spec.name!r} matching={spec.matching!r} does not look like a "
            "regime match. Say how the control is drawn from comparable bars."
        )


# --------------------------------------------------------------------------------------
# Estimator self-controls
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class EstimatorResult:
    """A result that came out of a filter, transform or information-theoretic estimator."""

    name: str
    statistic: float
    self_control_statistic: float | None
    self_control_description: str


def require_estimator_self_control(result: EstimatorResult, *, tolerance: float = 0.5) -> None:
    """Refuse to believe an estimator result that was never run against itself.

    The wave phase-lead scan reported ETHUSDT leading BTCUSDT by 4 bars at r = 0.48 with
    24 of 24 pairs surviving FDR. BTCUSDT filtered at 15.3 bars against *the same* BTCUSDT
    series filtered at 7.1 showed an apparent lead of 4 bars at r = 0.57 — and a series
    cannot lead itself. That is the control this rule demands.
    """
    if result.self_control_statistic is None or not result.self_control_description.strip():
        raise PolicyError(
            f"estimator result {result.name!r} has no self-control. When a result comes "
            "out of a filter or an estimator, run that estimator against itself (same "
            "series, two settings) before believing a cross-series finding."
        )
    # If the self-control produces a statistic of comparable magnitude to the claimed
    # result, the claim is an artefact of the estimator, not a finding about the data.
    if abs(result.statistic) > 0 and abs(result.self_control_statistic) >= abs(
        result.statistic
    ) * tolerance:
        raise PolicyError(
            f"estimator result {result.name!r} is not distinguishable from its own "
            f"self-control ({result.self_control_description}): claimed "
            f"{result.statistic:+.4f}, self-control {result.self_control_statistic:+.4f}. "
            "The estimator is manufacturing the finding."
        )


# --------------------------------------------------------------------------------------
# Do not invert inspected non-significant signs
# --------------------------------------------------------------------------------------


def refuse_structure_sign_inversion(
    *,
    feature: str,
    proposed_side_rule: str,
    preregistered_on_lockbox: bool = False,
) -> None:
    """Refuse a contrarian rule fitted to the inspected structure point estimates.

    Higher highs were mildly negative and lower highs mildly positive on the training
    window. Neither survived FDR. Fitting a contrarian rule to that pattern after seeing it
    is selection on the same data. A fresh preregistration tested on the forward lockbox is
    the only legitimate path.
    """
    if feature not in STRUCTURE_SIGNS_INSPECTED:
        return
    if preregistered_on_lockbox:
        return
    raise PolicyError(
        f"refusing to invert inspected structure sign for {feature!r} via "
        f"{proposed_side_rule!r}. The point estimates lean the wrong way and are not "
        "significant (D-017). A contrarian rule needs a preregistered hypothesis tested on "
        "the forward lockbox, not a re-reading of the same diagnostic."
    )


# --------------------------------------------------------------------------------------
# ABC / wave-structure family policies (D-026, D-030)
# --------------------------------------------------------------------------------------


ABC_CONTINUATION_CLOSED: frozenset[str] = frozenset(
    {
        "abc_equal_legs_continuation",
        "abc_0618_continuation",
        "abc_1618_continuation",
        "bc_continuation",
        "A_equals_C_continuation",
    }
)

WAVETHEORY_SIMULATOR_MARKERS: frozenset[str] = frozenset(
    {
        "wavetheory.simulate_long_trades",
        "wavetheory.src.backtest.wave_strategy",
        "fractal_pivots",
        "WaveStrategyConfig",
    }
)


def refuse_abc_continuation_without_lockbox_prereg(
    *,
    claim: str,
    preregistered_on_lockbox: bool = False,
) -> None:
    """Refuse classical ABC continuation claims closed on the training window (D-030).

    Equal-leg / 0.618 / 1.618 continuation failed FDR; survivors were wrong-sign (bounce).
    A continuation rule needs a separate lockbox preregistration — not a re-reading of
    ``abc_factor`` training diagnostics.
    """
    if claim not in ABC_CONTINUATION_CLOSED and "continuation" not in claim.lower():
        return
    if preregistered_on_lockbox:
        return
    raise PolicyError(
        f"ABC continuation claim {claim!r} is CLOSED on BTCUSDT 1h/4h training evidence "
        "(D-030). Do not promote equal-leg or golden-ratio continuation without a fresh "
        "lockbox preregistration. The bounce alternative is preregistered separately as "
        "abc_bounce_001."
    )


def refuse_wavetheory_simulator_for_abc(module_or_path: str) -> None:
    """Refuse any ABC / structure number that came from the void wavetheory simulator (D-026)."""
    text = module_or_path.replace("\\", ".")
    for marker in WAVETHEORY_SIMULATOR_MARKERS:
        if marker in text or marker.replace(".", "/") in module_or_path.replace("\\", "/"):
            raise PolicyError(
                f"refusing ABC/structure evidence from {module_or_path!r}. The wavetheory "
                "private backtest is VOID (D-026): fractal pivot look-ahead and entry-bar "
                "immunity. Rebuild on the confirmed-swing warehouse + tradesim only."
            )


def require_warehouse_legs_for_abc(geometry_source: str) -> None:
    """ABC geometry must come from audited warehouse legs / confirmed swings."""
    allowed = ("indicators.legs", "warehouse_legs", "confirmed_swings", "structure_frame")
    lowered = geometry_source.lower().replace("\\", ".")
    if any(a in lowered for a in allowed):
        return
    raise PolicyError(
        f"ABC geometry source {geometry_source!r} is not the confirmed-swing warehouse. "
        "Prefer indicators.legs ratios over hand-drawn A/B/C or private fractal pivots "
        "(D-023, D-026). Same geometry, audited confirmation times."
    )


# --------------------------------------------------------------------------------------
# Lockbox prereg + underpowered hold (D-031)
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class LockboxPreregGate:
    """Minimum freeze checklist before any forward-lockbox evaluation may open."""

    name: str
    status: str
    evaluation: str
    frozen_utc: str | None
    leverage: float | None
    sl_pct: float | None
    control_policy: str
    control_arm_names: tuple[str, ...]


def require_lockbox_prereg_frozen(gate: LockboxPreregGate) -> None:
    """Refuse to open a lockbox run unless exits and a matched control were frozen first."""
    if str(gate.status).upper() not in {"FROZEN", "UNDERPOWERED_HOLD"}:
        raise PolicyError(
            f"lockbox prereg {gate.name!r} status={gate.status!r} is not FROZEN. "
            "Freeze exits and the matched control before opening the lockbox."
        )
    if gate.evaluation not in {"forward_lockbox_once", "nested_walk_forward"}:
        raise PolicyError(
            f"lockbox prereg {gate.name!r} evaluation={gate.evaluation!r} is not a "
            "recognised lockbox evaluation mode."
        )
    if not gate.frozen_utc:
        raise PolicyError(
            f"lockbox prereg {gate.name!r} missing exit_design.frozen_utc — freeze before open."
        )
    if gate.leverage is None or gate.sl_pct is None:
        raise PolicyError(
            f"lockbox prereg {gate.name!r} must freeze leverage and sl_pct before open."
        )
    policy = (gate.control_policy or "").lower()
    if "require_matched_control" not in policy and "matched" not in policy:
        raise PolicyError(
            f"lockbox prereg {gate.name!r} must require a matched control "
            "(policy require_matched_control). Uniform random is not enough (D-025)."
        )
    if not gate.control_arm_names:
        raise PolicyError(
            f"lockbox prereg {gate.name!r} lists no control arms. Name the volatility- "
            "or regime-matched control before opening the lockbox."
        )


def refuse_abc_bounce_reopen_while_underpowered(
    *,
    family_status: str,
    prereg_sha256: str,
    frozen_prereg_sha256: str,
    projected_sequential_trades: int,
    min_pooled_trades: int = 50,
    force: bool = False,
) -> None:
    """Keep abc_bounce_family open only as UNDERPOWERED — no retune, no early re-open.

    A second frozen one-shot is allowed only when the same prereg hash can project at
    least ``min_pooled_trades`` sequential lockbox trades. Widening tolerance / changing
    targets changes the hash and is refused.
    """
    status = str(family_status).upper()
    if status not in {"UNDERPOWERED", "UNDERPOWERED_HOLD"}:
        return
    if force:
        # Escape hatch for tests only — never use to widen tolerance after a peek.
        return
    if prereg_sha256 != frozen_prereg_sha256:
        raise PolicyError(
            "abc_bounce prereg hash changed while family_status is UNDERPOWERED_HOLD. "
            "That usually means tolerance/targets/hold/stop were edited after the first "
            "lockbox open — forbidden (D-031). Restore the frozen file."
        )
    if int(projected_sequential_trades) < int(min_pooled_trades):
        raise PolicyError(
            f"abc_bounce_family is UNDERPOWERED_HOLD ({projected_sequential_trades} "
            f"projected sequential trades < {min_pooled_trades}). Leave it open only as "
            "UNDERPOWERED; wait for more lockbox bars before a second frozen one-shot. "
            "Do not widen factor_tolerance."
        )


def refuse_abc_video_claim_as_evidence(claim_source: str) -> None:
    """Video / extraction notes are inventory only — not measured evidence."""
    text = claim_source.lower()
    markers = (
        "wave trading video",
        "wavetheory/reports",
        "video extraction",
        "youtube",
        "extracted from video",
    )
    if any(m in text for m in markers):
        raise PolicyError(
            f"refusing to treat {claim_source!r} as evidence. Record the claim in "
            "ABC_RULES_TESTED.md as untested/extracted; only FDR-controlled or void-"
            "labelled measurements count."
        )


# --------------------------------------------------------------------------------------
# Wave vs raw-return disagreement
# --------------------------------------------------------------------------------------


def prefer_raw_return_when_disagreement(
    *,
    wave_statistic: float,
    raw_return_statistic: float,
    wave_significant: bool,
    raw_significant: bool,
    name: str = "wave_lead",
) -> str:
    """When the wave channel and the unfiltered returns disagree, believe the returns.

    A lead that exists only after band-pass filtering and vanishes on raw returns is the
    filter talking (D-020 group-delay artefact class). Returns the verdict label that must
    be attached to the effect: ``wave``, ``raw_preferred``, or ``neither``.
    """
    if wave_significant and raw_significant:
        # Both see it — prefer the simpler measurement's magnitude for reporting, but the
        # finding stands on raw returns.
        return "raw_and_wave"
    if wave_significant and not raw_significant:
        return "raw_preferred_wave_discarded"
    if raw_significant and not wave_significant:
        return "raw_only"
    _ = (wave_statistic, raw_return_statistic, name)
    return "neither"


# --------------------------------------------------------------------------------------
# Contaminated lockbox multitrade peeks (D-035 / D-036)
# --------------------------------------------------------------------------------------


def refuse_copy_as_pristine_holdout(
    *,
    claimed_pristine: bool,
    same_calendar_window: bool = True,
) -> None:
    """Refuse 'we copied the DB so the holdout is clean again'."""
    if claimed_pristine and same_calendar_window:
        raise PolicyError(
            "Copying candles / indicators / reports into a new path does not re-seal a "
            "peeked holdout. Contamination is selection information used on that calendar "
            "window, not path uniqueness. For a clean claim: preregister first, then use "
            "only data after POST_MULTITRADE_FREEZE_START (or outer-fold settle never "
            "ranked for that claim)."
        )


def refuse_lockbox_multitrade_knob_as_promotion(
    *,
    claim: str,
    evidence_class: str | None,
    window_start: str | None = None,
    window_end: str | None = None,
) -> None:
    """Multitrade K / switch / TP grids on May→post-freeze peek are diagnostic only."""
    from llm2.evidence.peek_log import (
        POST_MULTITRADE_FREEZE_START,
        window_overlaps_contaminated_lockbox,
    )
    from llm2.paths import FORWARD_LOCKBOX_START

    ec = (evidence_class or "").upper()
    if "CONTAMINAT" in ec or "LOCKBOX" in ec:
        if window_start and window_end:
            if not window_overlaps_contaminated_lockbox(window_start, window_end):
                return
        raise PolicyError(
            f"claim {claim!r} cannot use evidence_class={evidence_class!r} for multitrade "
            f"parameter promotion. Quotable historical edge remains outer-fold settle; "
            f"lockbox multitrade knobs on [{FORWARD_LOCKBOX_START}, "
            f"{POST_MULTITRADE_FREEZE_START}) are diagnostic only (D-036). "
            f"Next real parameter claim: prereg + window starting "
            f">={POST_MULTITRADE_FREEZE_START}, or live post-freeze reconciliation."
        )


def require_post_freeze_for_multitrade_param_claim(
    *,
    claim: str,
    window_start: str,
    prereg_path: str | None = None,
) -> None:
    """New multitrade parameter claims need post-freeze calendar (or use outer folds)."""
    from llm2.evidence.peek_log import POST_MULTITRADE_FREEZE_START, is_post_freeze_window

    if is_post_freeze_window(window_start):
        if not prereg_path:
            raise PolicyError(
                f"claim {claim!r} is post-freeze but has no prereg_path. Register the "
                "candidate space before opening the unsealed forward window."
            )
        return
    raise PolicyError(
        f"claim {claim!r} window_start={window_start!r} is before "
        f"POST_MULTITRADE_FREEZE_START={POST_MULTITRADE_FREEZE_START}. "
        "Do not promote multitrade K/TP/switch/clarity changes from the peeked "
        "May-2026→2026-08-04 diagnostic window. Prereg + wait, or evaluate on outer folds "
        "without lockbox ranking."
    )


def classify_evidence_for_window(
    *,
    window_start: str,
    window_end: str,
    experiment_family: str = "multitrade_knob",
) -> str:
    """Stamp reports with the standing evidence class for a calendar slice."""
    from llm2.evidence.peek_log import (
        POST_MULTITRADE_FREEZE_START,
        is_post_freeze_window,
        window_overlaps_contaminated_lockbox,
    )

    if experiment_family in {
        "multitrade_knob",
        "lockbox_grid",
        "concurrent_grid",
        "expansion_lockbox",
    }:
        if window_overlaps_contaminated_lockbox(window_start, window_end):
            return "LOCKBOX_OPENED_CONTAMINATED_DIAGNOSTIC_ONLY"
        if is_post_freeze_window(window_start):
            return "POST_FREEZE_FORWARD_CANDIDATE"
    _ = POST_MULTITRADE_FREEZE_START
    return "UNSPECIFIED"


# --------------------------------------------------------------------------------------
# Expansion lockbox one-shot (D-037)
# --------------------------------------------------------------------------------------

EXPANSION_LOCKBOX_FINAL_GENERATION = "structure_v1_expansion_lockbox_final_001"

# Symbols already peeeed for charts / multitrade before the sealed expansion open.
EXPANSION_LOCKBOX_ALREADY_PEEKED: frozenset[str] = frozenset(
    {
        "ETHUSDT",
        "SOLUSDT",
        "LINKUSDT",
        "VETUSDT",
        "ADAUSDT",
        "BTCUSDT",
    }
)


def refuse_expansion_lockbox_multi_arm(
    *,
    n_arms: int | None = None,
    argv: Sequence[str] | None = None,
    generation_id: str = EXPANSION_LOCKBOX_FINAL_GENERATION,
) -> None:
    """Expansion sealed lockbox is one frozen arm only — no grids on the open (D-037)."""
    if n_arms is not None and int(n_arms) > 1:
        raise PolicyError(
            f"generation {generation_id}: multi-arm lockbox search is forbidden "
            f"(n_arms={n_arms}). One frozen single-book arm only (D-037)."
        )
    if argv is None:
        return
    joined = " ".join(str(a) for a in argv).lower()
    for bad in (
        "--grid",
        "--k ",
        "--k=",
        "fib_ext",
        "switch_book",
        "--multi",
        "--hunt",
        "clarity=",
        "--n-arms",
        "--arms",
    ):
        if bad in joined:
            raise PolicyError(
                f"generation {generation_id}: search flag {bad!r} refused on sealed "
                "expansion lockbox. One frozen single-book arm only (D-037)."
            )


def refuse_promotion_from_expansion_lockbox_pf(
    *,
    claim: str,
    evidence_class: str | None,
    quote_settle: bool = False,
) -> None:
    """Do not promote expansion packs from lockbox PF alone (D-037)."""
    if quote_settle:
        return
    ec = (evidence_class or "").upper()
    if "LOCKBOX" in ec or "CONTAMINAT" in ec:
        raise PolicyError(
            f"claim {claim!r} cannot promote from expansion lockbox "
            f"evidence_class={evidence_class!r}. Quote outer-fold settle pooled "
            "Profit Factor only; lockbox is diagnostic one-shot (D-037)."
        )


def refuse_already_peeked_on_expansion_pristine_set(
    *,
    symbol: str,
    generation_id: str = EXPANSION_LOCKBOX_FINAL_GENERATION,
    already_peeked: frozenset[str] = EXPANSION_LOCKBOX_ALREADY_PEEKED,
) -> None:
    """Refuse LINK/VET/ADA etc. in the 'pristine' expansion open set."""
    sym = str(symbol).upper()
    if sym in already_peeked:
        raise PolicyError(
            f"{sym} is already peeeed (charts / prior lockbox) and cannot enter "
            f"the pristine candidate set for {generation_id} (D-037)."
        )


# --------------------------------------------------------------------------------------
# Critical-step exception handling
# --------------------------------------------------------------------------------------


CRITICAL_STEP_MARKERS: frozenset[str] = frozenset(
    {
        "split_and_materialize",
        "write_fold_parquet",
        "parquet_engine",
        "require_constant_predictor_invariant",
        "require_predictability_gate_discriminates",
        "ensure_green_stamp",
        "run_conformance_check",
        "prefer_botsgeneral_tradesim",
        "prefer_botsgeneral_leakage",
    }
)


def is_critical_failure(exc: BaseException) -> bool:
    """True when an exception came from a correctness-critical step and must stop the run.

    The autonomy sweep's per-combo ``try/except`` turned a missing parquet engine into 131
    silent false negatives while the sweep reported healthy progress. Correctness-critical
    failures must re-raise; only per-combo data/model failures may be logged and skipped.
    """
    if isinstance(exc, (PolicyError, ImportError, MemoryError, SystemExit, KeyboardInterrupt)):
        return True
    text = f"{type(exc).__name__}: {exc}"
    # Walk the cause chain; the outer wrapper is often a generic Exception.
    seen: set[int] = set()
    cur: BaseException | None = exc
    while cur is not None and id(cur) not in seen:
        seen.add(id(cur))
        text += f" | {type(cur).__name__}: {cur}"
        tb = getattr(cur, "__traceback__", None)
        while tb is not None:
            name = tb.tb_frame.f_code.co_name
            if name in CRITICAL_STEP_MARKERS:
                return True
            mod = tb.tb_frame.f_globals.get("__name__", "")
            if any(m in mod for m in ("llm2.data.splits", "llm2.backtest.conformance", "llm2.audit.release_gates")):
                return True
            tb = tb.tb_next
        cur = cur.__cause__ or cur.__context__
    # Message-level fallback for when the stack was already formatted.
    lowered = text.lower()
    for marker in (
        "parquet",
        "conformance",
        "botsgeneral",
        "constant predictor",
        "predictability gate",
        "no working parquet",
    ):
        if marker in lowered:
            return True
    return False
