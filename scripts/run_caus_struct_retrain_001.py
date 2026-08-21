"""Fresh-hypothesis retrain after CAUS-STRUCT-001 (generation structure_v1_caus_retrain_001).

Order (mandatory):
  1. Hash the OPEN preregister YAML (no OOS viewed yet).
  2. Leakage audit on structure_v1 with the warehouse-recompute builder +
     builder-responsiveness probe (CAUS-WAREHOUSE-001). Refuse train if unclean.
  3. Nested hunt per symbol/target — new generation_ids, new seed root.
  4. Write a settlement report. Quote nothing from pre-2026-08-06 packs.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.guard import run_audit_for_space  # noqa: E402
from llm2.gates.v21 import format_gates_table  # noqa: E402
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "structure_v1_caus_retrain_001.yaml"
COMBOS = (
    ("BTCUSDT", "1h", "fwd_return"),
    ("ETHUSDT", "1h", "direction"),
    ("SOLUSDT", "1h", "direction"),
    ("ETHUSDT", "1h", "fwd_return"),
    ("SOLUSDT", "1h", "fwd_return"),
    ("BTCUSDT", "1h", "direction"),
)
SEED_ROOT = 20260806


def _hash_prereg() -> str:
    raw = PREREG.read_bytes()
    return hashlib.sha256(raw).hexdigest()


def _leakage_gate(symbol: str, timeframe: str) -> dict:
    ohlcv = load_ohlcv(symbol, timeframe)
    # Audit on a recent-but-deep window so recompute stays tractable.
    if len(ohlcv) > 4000:
        ohlcv = ohlcv.iloc[-4000:].copy()
    result = run_audit_for_space(
        ohlcv, interval=timeframe, space="structure_v1", symbol=symbol, cuts=2
    )
    if not result.get("ok"):
        raise RuntimeError(
            f"leakage gate FAIL for {symbol} {timeframe}: {result.get('report_text')}"
        )
    return {
        "ok": True,
        "leakage_potential": result.get("leakage_potential"),
        "n_bars": len(ohlcv),
    }


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing preregister: {PREREG}")
    text = PREREG.read_text(encoding="utf-8")
    if "status: OPEN" not in text and "status: OPEN\n" not in text:
        # Allow re-run after annotation only if hash line already present.
        if "preregister_sha256_at_run:" not in text:
            raise SystemExit("preregister is not OPEN and has no run hash — refusing")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _hash_prereg()
    append_ledger(
        f"CAUS_RETRAIN_001 start stamp={stamp} prereg_sha={prereg_sha[:16]} "
        f"fold={FOLD_GEOMETRY_VERSION} lockbox={FORWARD_LOCKBOX_START}",
        tier=0,
    )
    print(f"preregister_sha256={prereg_sha}", flush=True)

    # Annotate preregister with hash at first run (before OOS).
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(
            text.rstrip()
            + f"\n\npreregister_sha256_at_run: {prereg_sha}\n"
            + f"run_started_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n",
            encoding="utf-8",
        )

    leakage_reports: dict[str, dict] = {}
    for sym, tf, _tgt in COMBOS:
        key = f"{sym}_{tf}"
        if key in leakage_reports:
            continue
        print(f"LEAKAGE_GATE {sym} {tf} …", flush=True)
        leakage_reports[key] = _leakage_gate(sym, tf)
        print(f"LEAKAGE_GATE {sym} {tf} PASS", flush=True)

    rows = []
    for i, (sym, tf, tgt) in enumerate(COMBOS):
        gid = f"caus_retrain_001_{i:02d}_{sym}_{tf}_{tgt}_{stamp[:8]}"
        append_ledger(f"CAUS_RETRAIN_001 hunt start {gid}", tier=0)
        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space="structure_v1",
            horizon=DEFAULT_HORIZON[tgt],
            max_trials=4,
            seed=SEED_ROOT + i,
            run_backtest=True,
            run_surrogate_challenge=True,
            models=["hist_mean", "ridge", "lgbm_regressor", "lgbm_classifier"],
            tp_pct=0.01,
            sl_pct=0.02,
        )
        print(f"HUNT {gid}", flush=True)
        summary = run_nested_hunt(cfg)
        best = summary.get("best") or {}
        gates = best.get("gates") or {}
        row = {
            "symbol": sym,
            "timeframe": tf,
            "target": tgt,
            "generation_id": gid,
            "tier": best.get("tier") or summary.get("best_tier"),
            "pooled_pf": best.get("pooled_pf"),
            "pooled_trades": best.get("pooled_trades"),
            "ann_sharpe": best.get("ann_sharpe") or (gates.get("metrics") or {}).get("ann_sharpe"),
            "overall": gates.get("overall"),
            "gates": gates,
            "model": best.get("model"),
            "preregister_sha256": prereg_sha,
        }
        rows.append(row)
        print(
            f"{sym} {tf} {tgt}: tier={row['tier']} pf={row['pooled_pf']} "
            f"trades={row['pooled_trades']} overall={row['overall']} model={row['model']}",
            flush=True,
        )
        if gates:
            print(format_gates_table(gates), flush=True)

    out = {
        "generation_id": "structure_v1_caus_retrain_001",
        "stamp": stamp,
        "preregister": str(PREREG),
        "preregister_sha256": prereg_sha,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "leakage": leakage_reports,
        "rows": rows,
        "readiness_max": "RESEARCH_ONLY",
        "note": (
            "Fresh hypothesis after CAUS-STRUCT-001. No pre-2026-08-06 number is quotable. "
            "Live redeploy requires new pack freeze + certificate + Layer A parity = 0 "
            "on forward bars + explicit user auth."
        ),
    }
    out_path = ARTIFACTS / "reports" / f"structure_v1_caus_retrain_001_{stamp}.json"
    latest = ARTIFACTS / "reports" / "structure_v1_caus_retrain_001_latest.json"
    out_path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    latest.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"WROTE {out_path}", flush=True)

    # Freeze preregister status after OOS viewed.
    cur = PREREG.read_text(encoding="utf-8")
    if "status: OPEN" in cur:
        PREREG.write_text(
            cur.replace("status: OPEN", "status: FROZEN_OOS_VIEWED", 1)
            + f"frozen_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n"
            + "frozen_reason: outer-OOS of caus_retrain_001 viewed; do not re-search this space.\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
