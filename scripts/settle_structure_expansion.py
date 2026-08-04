"""Full-gate settle for structure_v1 expansion screens (BNB/XRP/VET/...)."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

from llm2.gates.v21 import format_gates_table
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.paths import ARTIFACTS
from llm2.registry.ledger import append_ledger
from llm2.research_policy import stamp_min_size_equity_caveat
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES

# Priority order: user-requested first, then remaining proxy tier>=2 direction arms.
PRIORITY = (
    ("VETUSDT", "1h", "direction"),
    ("VETUSDT", "1h", "fwd_return"),
    ("XRPUSDT", "1h", "direction"),
    ("XRPUSDT", "1h", "fwd_return"),
    ("BNBUSDT", "1h", "direction"),
    ("BNBUSDT", "1h", "fwd_return"),
    ("ADAUSDT", "1h", "direction"),
    ("DOGEUSDT", "1h", "direction"),
    ("AVAXUSDT", "1h", "direction"),
    ("LINKUSDT", "1h", "direction"),
    ("DOTUSDT", "1h", "direction"),
    ("TRXUSDT", "1h", "direction"),
    ("XLMUSDT", "1h", "direction"),
)


def _eligible() -> set[tuple[str, str, str]]:
    reports = sorted((ARTIFACTS / "reports").glob("structure_v1_expansion_hunt_*.json"))
    if not reports:
        return set()
    payload = json.loads(reports[-1].read_text(encoding="utf-8"))
    out = set()
    for row in payload.get("results") or []:
        if int(row.get("best_tier") or 0) < 2 or not row.get("predictability_passed"):
            continue
        gid = str(row.get("generation_id") or "")
        parts = gid.split("_")
        try:
            sym = next(p for p in parts if p.endswith("USDT"))
            tf = next(p for p in parts if p in ("1h", "4h", "15m"))
            tgt = "fwd_return" if "fwd_return" in gid else "direction"
        except StopIteration:
            continue
        out.add((sym, tf, tgt))
    return out


def main() -> int:
    leak_reports = sorted((ARTIFACTS / "reports").glob("structure_v1_leakage_recheck_*.json"))
    if not leak_reports or not json.loads(leak_reports[-1].read_text(encoding="utf-8")).get("overall_ok"):
        print("HOLD: need green structure_v1_leakage_recheck", flush=True)
        return 5

    eligible = _eligible()
    combos = [c for c in PRIORITY if c in eligible]
    if not combos:
        print("HOLD: no eligible tier>=2 combos from expansion hunt", flush=True)
        return 5

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = ARTIFACTS / "reports" / f"structure_v1_expansion_settle_{stamp}.json"
    rows = []
    best_overall = None
    for i, (sym, tf, tgt) in enumerate(combos):
        gid = f"settle_struct3_{i:02d}_{sym}_{tf}_{tgt}_{stamp[:8]}"
        append_ledger(f"STRUCTURE_EXPANSION_SETTLE start {gid}", tier=0)
        cfg = HuntConfig(
            generation_id=gid, symbol=sym, timeframe=tf, target=tgt,
            feature_space="structure_v1", horizon=DEFAULT_HORIZON[tgt],
            max_trials=4, seed=20260804 + 100 + i,
            run_backtest=True, run_surrogate_challenge=True,
            models=["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"],
            tp_pct=0.01, sl_pct=0.02,
        )
        summary = run_nested_hunt(cfg)
        best = summary.get("best") or {}
        gates = best.get("gates") or {}
        row = {
            "symbol": sym, "timeframe": tf, "target": tgt, "generation_id": gid,
            "tier": best.get("tier") or summary.get("best_tier"),
            "pooled_pf": best.get("pooled_pf"), "pooled_trades": best.get("pooled_trades"),
            "overall": gates.get("overall"), "gates": gates, "model": best.get("model"),
            "status": summary.get("status"),
        }
        rows.append(row)
        # checkpoint after each combo
        payload = stamp_min_size_equity_caveat({
            "stamped_utc": stamp, "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES, "readiness": "RESEARCH_ONLY",
            "vps_deploy": "FORBIDDEN_without_separate_live_pack_and_auth",
            "combos": rows, "best_pass": best_overall,
            "in_progress": True if i + 1 < len(combos) else False,
            "note": "Expansion settles research-only. ETH/SOL lockbox D-035 contaminated.",
        })
        if row["overall"] == "PASS" and (
            best_overall is None or float(row["pooled_pf"] or 0) > float(best_overall.get("pooled_pf") or 0)
        ):
            best_overall = row
            payload["best_pass"] = best_overall
        out_path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
        print(f"{sym} {tf} {tgt}: tier={row['tier']} pf={row['pooled_pf']} overall={row['overall']}", flush=True)
        print(format_gates_table(gates), flush=True)

    payload = stamp_min_size_equity_caveat({
        "stamped_utc": stamp, "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES, "readiness": "RESEARCH_ONLY",
        "vps_deploy": "FORBIDDEN_without_separate_live_pack_and_auth",
        "combos": rows, "best_pass": best_overall, "in_progress": False,
        "note": "Expansion settles research-only. ETH/SOL lockbox D-035 contaminated.",
    })
    out_path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"wrote {out_path}", flush=True)
    append_ledger(f"STRUCTURE_EXPANSION_SETTLE done best_pass={bool(best_overall)} path={out_path}", tier=2 if best_overall else 0)
    return 0 if best_overall else 2


if __name__ == "__main__":
    raise SystemExit(main())
