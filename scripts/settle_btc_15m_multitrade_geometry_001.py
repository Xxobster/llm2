"""Settle BTC 15m multitrade geometry arms (same knobs as ETH D-047).

Requires prior warehouse build + leakage PASS
(``scripts/build_btc_15m_structure_and_audit.py``).
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
from llm2.evidence.pack_registry import ensure_registry_schema, register_compare_report  # noqa: E402
from llm2.experiments.eth_multitrade_nested import stitch_arm  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES  # noqa: E402

GEN = "structure_v1_btc_15m_multitrade_geometry_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
AUDIT = ARTIFACTS / "reports" / "structure_v1_btc_15m_warehouse_audit_latest.json"
TIMEFRAME = "15m"
SYMBOL = "BTCUSDT"

ARMS: dict[str, dict[str, Any]] = {
    "wall_clock_q50": {
        "geometry": "wall_clock",
        "strength_quantile": 0.5,
        "base_hold": 24,
        "hold_addon": 48,
        "mean_lookback": 672,
        "label_horizon": 24,
    },
    "wall_clock_q75": {
        "geometry": "wall_clock",
        "strength_quantile": 0.75,
        "base_hold": 24,
        "hold_addon": 48,
        "mean_lookback": 672,
        "label_horizon": 24,
    },
    "bar_count_q75": {
        "geometry": "bar_count",
        "strength_quantile": 0.75,
        "base_hold": 6,
        "hold_addon": 12,
        "mean_lookback": 168,
        "label_horizon": 6,
    },
}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arm_cfg(spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "max_positions_per_side": 7,
        "clarity": "mean_strength",
        "clarity_scope": "all",
        "fib_ext": 1.618,
        "hold_addon": int(spec["hold_addon"]),
        "base_hold": int(spec["base_hold"]),
        "base_tp": 0.01,
        "base_sl": 0.02,
        "mean_lookback": int(spec["mean_lookback"]),
        "uniform_books": False,
        "bar_ms": int(TF_MS[TIMEFRAME]),
        "strength_quantile": float(spec["strength_quantile"]),
        "geometry": str(spec["geometry"]),
    }


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing prereg {PREREG}")
    if not AUDIT.is_file():
        raise SystemExit(
            f"missing warehouse audit {AUDIT}; run "
            "scripts/build_btc_15m_structure_and_audit.py first"
        )
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    if not (audit.get("leakage") or {}).get("passed"):
        raise SystemExit("warehouse leakage not PASS — refuse settle")

    prereg_sha = _sha(PREREG)
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    ensure_registry_schema()

    results: dict[str, Any] = {}
    for name, spec in ARMS.items():
        print(f"[{GEN}] arm={name} …", flush=True)
        cfg = _arm_cfg(spec)
        out = stitch_arm(
            cfg,
            label=f"{GEN}_{name}",
            timeframe=TIMEFRAME,
            symbol=SYMBOL,
            label_horizon=int(spec["label_horizon"]),
        )
        results[name] = out
        st = out["stitched"]
        print(
            f"  {name}: n={st['n_trades']} pf={st['profit_factor']} "
            f"exp_ru={st.get('expectancy_return_units')} "
            f"sharpe_fold_mean={st.get('sharpe_annualised_fold_mean')}",
            flush=True,
        )

    ranked = []
    for name, out in results.items():
        eru = out["stitched"].get("expectancy_return_units")
        n = int(out["stitched"].get("n_trades") or 0)
        if n > 0 and eru is not None and math.isfinite(float(eru)):
            ranked.append((float(eru), name))
    ranked.sort(reverse=True)
    best_name = ranked[0][1] if ranked else None
    best = results[best_name] if best_name else None
    control = results["wall_clock_q50"]

    def _beat(a: dict, b: dict) -> bool | None:
        ae = a["stitched"].get("expectancy_return_units")
        be = b["stitched"].get("expectancy_return_units")
        if ae is None or be is None:
            return None
        if not (math.isfinite(float(ae)) and math.isfinite(float(be))):
            return None
        return float(ae) > float(be)

    best_pf = best["stitched"]["profit_factor"] if best else float("nan")
    best_eru = best["stitched"].get("expectancy_return_units") if best else None
    pf_ok = math.isfinite(float(best_pf)) and float(best_pf) >= 1.20 if best else False
    no_liq = int(best["stitched"]["n_liquidations"]) == 0 if best else False
    eru_pos = (
        best_eru is not None
        and math.isfinite(float(best_eru))
        and float(best_eru) > 0
    )
    passed = bool(best and eru_pos and pf_ok and no_liq)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
            "warehouse_audit": str(AUDIT.relative_to(_ROOT)).replace("\\", "/"),
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
            "phase": "BTC_PHASE2",
            "eth_parent_generation": "structure_v1_eth_15m_multitrade_geometry_001",
            "arms": results,
            "compare": {
                "ranking_by_exp_ru": [
                    {"arm": n, "expectancy_return_units": e} for e, n in ranked
                ],
                "best_arm": best_name,
                "best_expectancy_return_units": best_eru,
                "best_pf": best_pf if best else None,
                "best_sharpe_fold_mean": (
                    best["stitched"].get("sharpe_annualised_fold_mean") if best else None
                ),
                "wall_clock_q75_beats_q50": _beat(
                    results["wall_clock_q75"], results["wall_clock_q50"]
                ),
                "bar_count_q75_beats_wall_clock_q75": _beat(
                    results["bar_count_q75"], results["wall_clock_q75"]
                ),
                "best_eru_positive": eru_pos,
                "best_pf_ge_1_20": pf_ok,
                "best_no_liquidation": no_liq,
                "passed_success_criteria": passed,
                "control_arm": "wall_clock_q50",
                "control_stitched": control["stitched"],
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "note": (
                "BTC Phase 2 separate generation. Same knobs as ETH D-047. "
                "MIN_EXCHANGE dust caveat. Do not reopen 1h clarity×hold×TP."
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
        candidate_metrics=(best["stitched"] if best else {}),
        tradesim_run_ids=[],
        control_version_id="btc_15m_wall_clock_q50",
    )
    print(json.dumps(report["compare"], indent=2))
    print(f"wrote {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
