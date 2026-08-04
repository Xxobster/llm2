"""Autonomous sweep over (symbol, timeframe, target, feature space).

The earlier conclusion that the non-directional block was a NO-GO is withdrawn. Every
generation reported ``predictability_passed=false`` because the Stage-B gate probed with a
constant predictor and could not return True for any input (D-013), so no trial could
exceed tier 0 and no tradesim escalation ever ran. The prior 148 generations are marked
GATE_VOID and the target space is reopened.
"""

from __future__ import annotations

import itertools
import json
import os
import sys
import traceback

from llm2.audit.release_gates import (
    require_constant_predictor_invariant,
    require_predictability_gate_discriminates,
)
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger

SYMBOLS = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
TIMEFRAMES = ["1h", "4h", "15m"]

# D-010 (non-directional NO-GO) is retracted: it was produced by a Stage-B gate that could
# not return True for any input (D-013), so direction and fwd_return were never tested
# rather than falsified. Nothing is frozen until a working gate has ruled on it.
ACTIVE_TARGETS = ["vol_ratio", "volatility", "xs_rank", "quantile", "fwd_return", "direction"]
FROZEN_TARGETS: frozenset[str] = frozenset()

SCREEN_MODELS = ["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"]

ESCALATE_AT_TIER = 1
ALERT_AT_TIER = 2

# Generation identifiers carry the gate revision. The 148 generations run before the
# Stage-B repair are GATE_VOID (D-013), but they are still rows in the research database
# marked ``completed``, so the resume check happily skipped every one of them — the sweep
# would have "finished" without re-testing any of the reopened targets. Bumping this stamp
# forces a fresh generation while leaving the void history in place as a record rather than
# overwriting it. Any future change that invalidates prior results must bump it again.
GATE_REVISION = "g2"


def _spaces_for(target: str) -> list[str]:
    if target == "xs_rank":
        return ["xs_v1", "crosspair_v1", "ohlcv_v1"]
    return ["ohlcv_v1", "indicators_v1", "pivot_v1"]


def _combos() -> list[tuple[str, str, str, int, str]]:
    out: list[tuple[str, str, str, int, str]] = []
    for tgt in ACTIVE_TARGETS:
        for tf, sym, space in itertools.product(TIMEFRAMES, SYMBOLS, _spaces_for(tgt)):
            out.append((sym, tf, tgt, DEFAULT_HORIZON[tgt], space))
    return out


def _generation_done(db: ResearchDB, generation_id: str) -> bool:
    # Must query by generation_id: the unfiltered list is capped at the newest 500 rows.
    trials = db.list_trials(generation_id)
    return any(t.get("status") == "completed" for t in trials)


def _headline(best: dict) -> str:
    if best.get("metric_kind") == "forecast_skill" or best.get("pooled_skill") is not None:
        return f"proxy_skill={best.get('pooled_skill')}"
    return f"proxy_pf={best.get('pooled_pf')}"


def _should_escalate(summary: dict) -> bool:
    """Escalate only when the screen is real, not skill-without-predictability noise."""
    tier = int(summary.get("best_tier") or 0)
    if tier < ESCALATE_AT_TIER:
        return False
    if not summary.get("predictability_passed"):
        # Skill > 1 with a failed Stage-B predictability audit is uninteresting noise.
        return False
    return True


def main() -> int:
    require_constant_predictor_invariant()
    require_predictability_gate_discriminates()
    # Fail before the first combo if the physical train/test split cannot be written, rather
    # than logging the same traceback 162 times and reporting a completed sweep.
    from llm2.data.splits import parquet_engine

    engine = parquet_engine()
    db = ResearchDB()
    combos = _combos()
    append_ledger(
        f"AUTONOMY start {len(combos)} combos; gate_revision={GATE_REVISION}; "
        f"parquet_engine={engine}; frozen_out={sorted(FROZEN_TARGETS)}; "
        f"active={ACTIVE_TARGETS}",
        tier=0,
    )
    print(f"gate_revision={GATE_REVISION} parquet_engine={engine} combos={len(combos)}", flush=True)

    for i, (sym, tf, tgt, horizon, space) in enumerate(combos):
        gid = f"auto{GATE_REVISION}_{i:03d}_{sym}_{tf}_{tgt}_{space}"
        if _generation_done(db, gid):
            print(f"[{i + 1}/{len(combos)}] {gid} SKIP (already completed)", flush=True)
            continue

        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space=space,
            horizon=horizon,
            max_trials=len(SCREEN_MODELS),
            run_backtest=False,
            run_surrogate_challenge=True,
            models=list(SCREEN_MODELS),
        )
        try:
            s = run_nested_hunt(cfg)
        except Exception as exc:  # noqa: BLE001
            from llm2.research_policy import is_critical_failure

            append_ledger(f"AUTONOMY error {gid}: {exc}", tier=0)
            traceback.print_exc()
            # Correctness-critical failures must stop the run. The previous handler logged
            # every traceback and continued, so a broken parquet engine produced 131 silent
            # false negatives while the sweep reported healthy progress (D-018).
            if is_critical_failure(exc):
                append_ledger(
                    f"AUTONOMY HALT on critical failure at {gid}: {type(exc).__name__}: {exc}",
                    tier=0,
                )
                print(f"HALT critical failure at {gid}: {exc}", flush=True)
                return 4
            continue

        screen_tier = int(s.get("best_tier") or 0)
        best = s.get("best") or {}
        append_ledger(
            f"AUTONOMY screen {gid} tier={screen_tier} {_headline(best)} "
            f"predictability={s.get('predictability_passed')} "
            f"(proxy is a filter, not evidence)",
            tier=screen_tier,
        )
        print(
            f"[{i + 1}/{len(combos)}] {gid} screen_tier={screen_tier} "
            f"pred={s.get('predictability_passed')}",
            flush=True,
        )

        if not _should_escalate(s):
            if screen_tier >= ESCALATE_AT_TIER and not s.get("predictability_passed"):
                append_ledger(
                    f"AUTONOMY skip-escalate {gid}: tier={screen_tier} but "
                    "predictability_passed=false (skill-without-predictability is noise)",
                    tier=0,
                )
            continue

        cfg2 = HuntConfig(
            **{
                **cfg.__dict__,
                "generation_id": gid + "_ts",
                "run_backtest": True,
                "max_trials": 2,
                "models": [best.get("model", "lgbm_regressor")],
            }
        )
        try:
            s2 = run_nested_hunt(cfg2)
        except Exception as exc:  # noqa: BLE001
            from llm2.research_policy import is_critical_failure

            append_ledger(f"AUTONOMY tradesim error {gid}: {exc}", tier=0)
            traceback.print_exc()
            if is_critical_failure(exc):
                append_ledger(
                    f"AUTONOMY HALT on critical tradesim failure at {gid}: "
                    f"{type(exc).__name__}: {exc}",
                    tier=0,
                )
                print(f"HALT critical tradesim failure at {gid}: {exc}", flush=True)
                return 4
            continue

        ts_tier = int(s2.get("best_tier") or 0)
        best2 = s2.get("best") or {}
        append_ledger(
            f"AUTONOMY tradesim {gid} tier={ts_tier} {_headline(best2)}",
            tier=ts_tier,
        )

        if ts_tier >= ALERT_AT_TIER:
            append_ledger(
                f"ALERT tier>={ALERT_AT_TIER} candidate {gid}: {json.dumps(best2, default=str)[:800]} "
                "— sweep halted pending independent re-run, Finplot and gate table "
                f"(scripts/tier2_review.py --generation-id {gid}_ts)",
                tier=ts_tier,
            )
            print(f"ALERT Tier{ts_tier} {gid}", flush=True)
            return 2

    append_ledger("AUTONOMY sweep complete — no tier>=2 candidate", tier=0)
    return 0


if __name__ == "__main__":
    if os.environ.get("LLM2_SWEEP_SINGLETON") != "0":
        import socket

        _guard = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            _guard.bind(("127.0.0.1", 47311))
        except OSError:
            print("another autonomy sweep is already running; exiting", file=sys.stderr)
            raise SystemExit(3)
    raise SystemExit(main())
