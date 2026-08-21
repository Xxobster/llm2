"""Nested settle: skip weak short book1 vs eth_multitrade_v1_2 (outer folds)."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.evidence.pack_registry import (  # noqa: E402
    ensure_registry_schema,
    register_compare_report,
    register_freeze,
)
from llm2.experiments.eth_multitrade_nested import live_control_cfg, stitch_arm  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES  # noqa: E402

GEN = "structure_v1_eth_multitrade_skip_weak_short_book1_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
CONTROL_PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1_2"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing prereg {PREREG}")
    prereg_sha = _sha(PREREG)
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    ensure_registry_schema()

    control_cfg = live_control_cfg()
    control_cfg.update(
        {
            "clarity_scope": "all",
            "max_positions_per_side": 7,
            "strength_quantile": 0.5,
            "skip_weak_short_book1": False,
        }
    )
    cand_cfg = dict(control_cfg)
    cand_cfg["skip_weak_short_book1"] = True
    cand_cfg["weak_short_book1_strength_quantile"] = 2.0 / 3.0

    print(f"[{GEN}] control …", flush=True)
    control = stitch_arm(control_cfg, label=f"{GEN}_control")
    print(
        f"  control PF={control['stitched']['profit_factor']} "
        f"exp_ru={control['stitched'].get('expectancy_return_units')} "
        f"n={control['stitched']['n_trades']}",
        flush=True,
    )
    print(f"[{GEN}] candidate skip_weak_short_book1 …", flush=True)
    candidate = stitch_arm(cand_cfg, label=f"{GEN}_candidate")
    print(
        f"  candidate PF={candidate['stitched']['profit_factor']} "
        f"exp_ru={candidate['stitched'].get('expectancy_return_units')} "
        f"n={candidate['stitched']['n_trades']} "
        f"skips={candidate['signal_stats_total'].get('n_skipped_weak_short_book1')}",
        flush=True,
    )

    c_exp = control["stitched"].get("expectancy_return_units")
    k_exp = candidate["stitched"].get("expectancy_return_units")
    c_pf = control["stitched"]["profit_factor"]
    k_pf = candidate["stitched"]["profit_factor"]
    beat_exp = (
        c_exp is not None
        and k_exp is not None
        and math.isfinite(float(c_exp))
        and math.isfinite(float(k_exp))
        and float(k_exp) > float(c_exp)
    )
    pf_ok = math.isfinite(float(k_pf)) and float(k_pf) >= 1.20
    no_liq = int(candidate["stitched"]["n_liquidations"]) == 0
    passed = bool(beat_exp and pf_ok and no_liq)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
            "autopsy_generation": "structure_v1_fleet_streak_autopsy_001",
            "evidence_class": "OUTER_TRANSFER_COMPARE",
            "max_readiness": "RESEARCH_ONLY",
            "promotion_allowed": False,
            "live_deploy": "FORBIDDEN",
            "primary_metric": "expectancy_return_units",
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "conformance_passed": bool(conf.get("passed")),
            "control": control,
            "candidate": candidate,
            "compare": {
                "control_expectancy_return_units": c_exp,
                "candidate_expectancy_return_units": k_exp,
                "exp_ru_delta": (
                    float(k_exp) - float(c_exp)
                    if c_exp is not None
                    and k_exp is not None
                    and math.isfinite(float(c_exp))
                    and math.isfinite(float(k_exp))
                    else None
                ),
                "control_pf": c_pf,
                "candidate_pf": k_pf,
                "control_net_pnl": control["stitched"]["net_pnl"],
                "candidate_net_pnl": candidate["stitched"]["net_pnl"],
                "control_win_rate": control["stitched"].get("win_rate"),
                "candidate_win_rate": candidate["stitched"].get("win_rate"),
                "n_skipped_weak_short_book1": int(
                    candidate["signal_stats_total"].get("n_skipped_weak_short_book1")
                    or 0
                ),
                "candidate_beats_control_exp_ru": beat_exp,
                "candidate_pf_ge_1_20": pf_ok,
                "candidate_no_liquidation": no_liq,
                "passed_success_criteria": passed,
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
        }
    )
    out = ARTIFACTS / "reports"
    out.mkdir(parents=True, exist_ok=True)
    latest = out / f"{GEN}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out / f"{GEN}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )

    text = PREREG.read_text(encoding="utf-8")
    if "status: FROZEN" in text:
        PREREG.write_text(
            text.replace(
                "status: FROZEN",
                f"status: OOS_COMPARE_COMPLETE\nsettled_utc: \"{stamp}\"\n"
                f"preregister_sha256_at_run: {prereg_sha}",
                1,
            ),
            encoding="utf-8",
        )

    register_compare_report(
        GEN,
        report_path=latest,
        control_metrics=control["stitched"],
        candidate_metrics=candidate["stitched"],
        control_version_id="eth_multitrade_v1_2",
    )
    if CONTROL_PACK.is_dir():
        register_freeze(
            CONTROL_PACK,
            evidence={
                "report_paths": [str(latest.relative_to(_ROOT)).replace("\\", "/")],
                "generation_id": GEN,
            },
            require_run_id=False,
            ledger=False,
        )

    print(json.dumps(report["compare"], indent=2))
    print(f"wrote {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
