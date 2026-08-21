"""Run structure_v1_forecast_filter_on_direction_001 (nested filters on baseline).

Forecast skill and trading Profit Factor are hard-separated.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
for _p in (
    Path(r"C:\projects\botsgeneral\packages\leakage\src"),
    Path(r"C:\projects\botsgeneral\packages\indicators\src"),
    Path(r"C:\projects\botsgeneral\packages\tradesim\src"),
):
    if _p.is_dir() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.four_proof import (  # noqa: E402
    refuse_warehouse_leakage_pass_alone,
    require_four_proof_ok,
    run_four_proof_gate,
)
from llm2.experiments.forecast_filter_on_direction import run_symbol  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, index_to_ms  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "structure_v1_forecast_filter_on_direction_001.yaml"
SYMBOLS = ("ETHUSDT", "BTCUSDT", "SOLUSDT")
SPACE = "structure_v1"
TF = "1h"


def main() -> int:
    from llm2.research.forecast_filter_seal import refuse_nest_filter_retune

    # D-060: trading branch CLOSED — refuse silent retune / re-promotions.
    refuse_nest_filter_retune(context="scripts/run_forecast_filter_on_direction_001.py")
    if not PREREG.is_file():
        raise SystemExit(f"missing {PREREG}")
    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    text = PREREG.read_text(encoding="utf-8")
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(
            text.rstrip()
            + f"\n\npreregister_sha256_at_run: {sha}\n"
            + f"run_started_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n",
            encoding="utf-8",
        )
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(
        f"FORECAST_FILTER_ON_DIRECTION_001 start sha={sha[:16]} fold={FOLD_GEOMETRY_VERSION}",
        tier=0,
    )
    print(f"preregister_sha256={sha}", flush=True)

    print("FOUR_PROOF ETHUSDT (pre-lockbox) …", flush=True)
    ohlcv_eth = load_ohlcv("ETHUSDT", TF)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv_eth = ohlcv_eth.loc[index_to_ms(ohlcv_eth.index) < lock_ms].copy()
    fp = run_four_proof_gate(
        space=SPACE, symbol="ETHUSDT", timeframe=TF, ohlcv=ohlcv_eth
    )
    refuse_warehouse_leakage_pass_alone(
        space=SPACE, leakage_passed=True, four_proof_ok=bool(fp.get("ok"))
    )
    require_four_proof_ok(fp)
    print(f"FOUR_PROOF PASS artifacts={fp.get('artifact_dir')}", flush=True)

    rows = []
    for sym in SYMBOLS:
        print(f"RUN {sym} …", flush=True)
        out = run_symbol(sym)
        rows.append(out)
        skill = out.get("forecast_skill") or {}
        print(
            f"  skill retrace_ic={skill.get('next_retrace_pct', {}).get('mean_outer_spearman_ic')} "
            f"vol_ic={skill.get('next_vol', {}).get('mean_outer_spearman_ic')}",
            flush=True,
        )
        for arm, blob in (out.get("arms") or {}).items():
            print(
                f"  {arm}: mean_fold_pf={blob.get('mean_fold_pf')} "
                f"sum_pnl={blob.get('sum_net_pnl')} n_sig={blob.get('n_signals')}",
                flush=True,
            )
        for arm, cmp_ in (out.get("vs_control") or {}).items():
            print(
                f"  vs_control {arm}: methodology_win={cmp_.get('methodology_win')} "
                f"beats_pf={cmp_.get('beats_control_pf')} beats_pnl={cmp_.get('beats_control_pnl')}",
                flush=True,
            )

    text = PREREG.read_text(encoding="utf-8")
    if "status: OPEN" in text:
        PREREG.write_text(
            text.replace("status: OPEN", "status: FROZEN_OOS_VIEWED", 1)
            + f"frozen_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n"
            + "frozen_reason: outer-OOS of forecast_filter_on_direction_001 viewed.\n",
            encoding="utf-8",
        )

    any_method_win = any(
        bool(v.get("methodology_win"))
        for r in rows
        for v in (r.get("vs_control") or {}).values()
    )
    report = {
        "generation_id": "structure_v1_forecast_filter_on_direction_001",
        "stamp": stamp,
        "preregister_sha256": sha,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "four_proof": {
            "ok": fp.get("ok"),
            "artifact_dir": fp.get("artifact_dir"),
            "proofs_ok": fp.get("proofs_ok"),
            "artifact_hashes": fp.get("artifact_hashes"),
        },
        "symbols": rows,
        "any_methodology_win_vs_control": any_method_win,
        "readiness_max": "RESEARCH_ONLY",
        "note": (
            "Nested filters on causal direction baseline (pack geometry only). "
            "Forecast IC ≠ trading PF. No pre-CAUS model.joblib. No live deploy."
        ),
    }
    out = ARTIFACTS / "reports" / f"structure_v1_forecast_filter_on_direction_001_{stamp}.json"
    latest = ARTIFACTS / "reports" / "structure_v1_forecast_filter_on_direction_001_latest.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"WROTE {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
