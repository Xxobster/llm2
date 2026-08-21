"""Nested settle: ETH 15m wall_clock p75 + TP∝|pred_mean| vs fixed TP.

Control = D-047 winner. Candidate adds frozen proportional TP after book TP.
Outer folds only; lockbox unused. Evidence OUTER_TRANSFER_COMPARE.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.evidence.pack_registry import (  # noqa: E402
    ensure_registry_schema,
    register_compare_report,
)
from llm2.experiments.eth_multitrade_nested import stitch_arm  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES  # noqa: E402

GEN = "structure_v1_eth_15m_wall_clock_p75_tp_scale_absmean_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
SYMBOL = "ETHUSDT"
TIMEFRAME = "15m"
LABEL_HORIZON = 24

BASE_CFG: dict[str, Any] = {
    "max_positions_per_side": 7,
    "clarity": "mean_strength",
    "clarity_scope": "all",
    "fib_ext": 1.618,
    "hold_addon": 48,
    "base_hold": 24,
    "base_tp": 0.01,
    "base_sl": 0.02,
    "mean_lookback": 672,
    "uniform_books": False,
    "bar_ms": int(TF_MS[TIMEFRAME]),
    "strength_quantile": 0.75,
    "geometry": "wall_clock",
}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    t0 = time.perf_counter()
    if not PREREG.is_file():
        raise SystemExit(f"missing preregister {PREREG}")
    prereg_sha = _sha(PREREG)
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    ensure_registry_schema()

    control_cfg = {**BASE_CFG, "tp_scale_by_abs_mean": False}
    cand_cfg = {
        **BASE_CFG,
        "tp_scale_by_abs_mean": True,
        "tp_scale_ref": 0.5,
        "tp_scale_factor_min": 1.0,
        "tp_scale_factor_max": 2.0,
    }

    print(f"[{GEN}] control (wall_clock p75 fixed TP) …", flush=True)
    control = stitch_arm(
        control_cfg,
        label=f"{GEN}_control",
        timeframe=TIMEFRAME,
        symbol=SYMBOL,
        label_horizon=LABEL_HORIZON,
    )
    print(
        f"  control PF={control['stitched']['profit_factor']} "
        f"exp_ru={control['stitched']['expectancy_return_units']} "
        f"n={control['stitched']['n_trades']}",
        flush=True,
    )
    print(f"[{GEN}] candidate (p75 + TP∝|mean|) …", flush=True)
    candidate = stitch_arm(
        cand_cfg,
        label=f"{GEN}_candidate",
        timeframe=TIMEFRAME,
        symbol=SYMBOL,
        label_horizon=LABEL_HORIZON,
    )
    print(
        f"  candidate PF={candidate['stitched']['profit_factor']} "
        f"exp_ru={candidate['stitched']['expectancy_return_units']} "
        f"mean_tp={candidate['stitched'].get('mean_tp_pct')} "
        f"n={candidate['stitched']['n_trades']}",
        flush=True,
    )

    c_exp = control["stitched"]["expectancy_return_units"]
    k_exp = candidate["stitched"]["expectancy_return_units"]
    c_pf = control["stitched"]["profit_factor"]
    k_pf = candidate["stitched"]["profit_factor"]
    beat_exp = (
        c_exp is not None
        and k_exp is not None
        and math.isfinite(float(c_exp))
        and math.isfinite(float(k_exp))
        and float(k_exp) > float(c_exp)
    )
    pf_ok = k_pf is not None and math.isfinite(float(k_pf)) and float(k_pf) >= 1.20
    no_liq = int(candidate["stitched"]["n_liquidations"]) == 0
    passed = bool(beat_exp and pf_ok and no_liq)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
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
            "timeframe": TIMEFRAME,
            "touch_timeframe": "1m",
            "symbol": SYMBOL,
            "parent_generation": "structure_v1_eth_15m_multitrade_geometry_001",
            "parent_arm": "wall_clock_q75",
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
                "candidate_mean_tp_pct": candidate["stitched"].get("mean_tp_pct"),
                "candidate_beats_control_exp_ru": beat_exp,
                "candidate_pf_ge_1_20": pf_ok,
                "candidate_no_liquidation": no_liq,
                "passed_success_criteria": passed,
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "note": (
                "Nested on ETH 15m wall_clock p75 only. Formula "
                "TP=book_tp*min(2,max(1,|mean|/0.5)). No 1h grid reopen. "
                "MIN_EXCHANGE dust caveat."
            ),
        }
    )
    out_dir = ARTIFACTS / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    latest = out_dir / f"{GEN}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out_dir / f"{GEN}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )

    text = PREREG.read_text(encoding="utf-8")
    if "status: FROZEN" in text:
        text = text.replace(
            "status: FROZEN",
            f"status: OOS_COMPARE_COMPLETE\nsettled_utc: \"{stamp}\"\n"
            f"preregister_sha256_at_run: {prereg_sha}",
            1,
        )
        PREREG.write_text(text, encoding="utf-8")

    register_compare_report(
        GEN,
        report_path=latest,
        control_metrics=control["stitched"],
        candidate_metrics=candidate["stitched"],
        tradesim_run_ids=[],
        control_version_id="eth_15m_multitrade_wall_clock_p75_v1",
    )
    print(json.dumps(report["compare"], indent=2))
    print(f"wrote {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
