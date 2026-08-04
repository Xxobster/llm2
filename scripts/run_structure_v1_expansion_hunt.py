"""Bounded structure_v1 proxy hunt on expansion symbols (fold geometry V2).

Requires a green structure_v1_leakage_recheck_*.json with overall_ok=True.
Does not open the ETH/SOL lockbox. RESEARCH_ONLY — no deploy.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.paths import ARTIFACTS
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger

# Expansion queue + prior BNB/XRP screens. Skip HYPE (short history).
SYMBOLS = (
    "BNBUSDT", "XRPUSDT", "VETUSDT", "ADAUSDT", "DOGEUSDT",
    "AVAXUSDT", "LINKUSDT", "DOTUSDT", "TRXUSDT", "XLMUSDT",
)
TIMEFRAMES = ("1h",)
TARGETS = ("fwd_return", "direction")
SPACE = "structure_v1"
GATE_REVISION = "struct3"


def _require_clean_leakage() -> Path:
    reports = sorted((ARTIFACTS / "reports").glob("structure_v1_leakage_recheck_*.json"))
    if not reports:
        raise SystemExit("HOLD: run scripts/audit_structure_leakage_expansion.py first")
    path = reports[-1]
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not payload.get("overall_ok"):
        raise SystemExit(f"HOLD: leakage recheck FAIL ({path.name}); fix before hunt")
    return path


def main() -> int:
    leak_path = _require_clean_leakage()
    append_ledger(
        f"STRUCTURE_V1_EXPANSION_HUNT start rev={GATE_REVISION} leakage={leak_path.name}",
        tier=0,
    )
    db = ResearchDB()
    combos = [(s, tf, t) for s in SYMBOLS for tf in TIMEFRAMES for t in TARGETS]
    results = []
    best_tier = 0
    for i, (sym, tf, tgt) in enumerate(combos):
        gid = f"auto{GATE_REVISION}_{i:02d}_{sym}_{tf}_{tgt}_{SPACE}"
        trials = db.list_trials(gid)
        if any(t.get("status") == "completed" for t in trials):
            print(f"[{i+1}/{len(combos)}] {gid} SKIP", flush=True)
            continue
        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space=SPACE,
            horizon=DEFAULT_HORIZON[tgt],
            max_trials=4,
            seed=20260804 + i,
            run_backtest=False,
            run_surrogate_challenge=True,
            models=["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"],
        )
        summary = run_nested_hunt(cfg)
        tier = int(summary.get("best_tier") or 0)
        best_tier = max(best_tier, tier)
        print(f"[{i+1}/{len(combos)}] {gid} tier={tier} pred={summary.get('predictability_passed')} status={summary.get('status')}", flush=True)
        results.append({"generation_id": gid, **{k: summary.get(k) for k in ("best_tier", "predictability_passed", "status", "best")}})
        if tier >= 2 and summary.get("predictability_passed"):
            append_ledger(f"SCREEN_CANDIDATE structure_v1 {gid} proxy_tier={tier}", tier=1)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = {
        "study_id": "structure_v1_expansion_hunt_001",
        "readiness": "RESEARCH_ONLY",
        "best_tier": best_tier,
        "leakage_recheck": leak_path.name,
        "results": results,
        "stamped_utc": stamp,
        "note": "Proxy screen only. Settle tier>=2 via settle_structure_expansion.py. Lockbox D-035 contaminated for ETH/SOL.",
    }
    path = ARTIFACTS / "reports" / f"structure_v1_expansion_hunt_{stamp}.json"
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    append_ledger(f"STRUCTURE_V1_EXPANSION_HUNT complete best_tier={best_tier} report={path.name}", tier=best_tier)
    print(f"wrote {path} best_tier={best_tier}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
