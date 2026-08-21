"""Freeze RESEARCH_ONLY ETH 15m multitrade wall-clock p75 pack (D-047).

Trains LightGBM on structure_v1 @ 15m through last-fold boundary (2025-10-01).
Live deploy FORBIDDEN.
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from llm2.evidence.pack_registry import (  # noqa: E402
    ensure_registry_schema,
    regenerate_versions_md,
    register_freeze,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROOT  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

PARENT = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_p75_v1"
DST = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_15m_multitrade_wall_clock_p75_v1"
VERSION_ID = "eth_15m_multitrade_wall_clock_p75_v1"
GEN = "structure_v1_eth_15m_multitrade_geometry_001"
REPORT = ARTIFACTS / "reports" / f"{GEN}_latest.json"
SYMBOL = "ETHUSDT"
TIMEFRAME = "15m"
LABEL_HORIZON = 24
TRAIN_UNTIL = "2025-10-01"  # last outer fold start (v2)


def main() -> int:
    if not PARENT.is_dir():
        raise SystemExit(f"missing parent pack {PARENT}")
    if not REPORT.is_file():
        raise SystemExit(f"missing settle report {REPORT}")
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    best = (report.get("arms") or {}).get("wall_clock_q75") or {}
    stitched = best.get("stitched") or {}
    compare = report.get("compare") or {}
    if compare.get("best_arm") != "wall_clock_q75":
        print("WARNING: best_arm is not wall_clock_q75 in report", flush=True)

    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    # Copy risk / mark scaffolding only
    for name in ("risk_tiers.json", "mark_snapshot.json", "structure_refresh_bootstrap.json"):
        src = PARENT / name
        if src.is_file():
            shutil.copy2(src, DST / name)

    from llm2.data.loader import load_ohlcv

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    train_end = pd.Timestamp(TRAIN_UNTIL, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, "structure_v1", symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    ts_ms = index_to_ms(aligned.index)
    train_end_ms = int(train_end.value // 1_000_000)
    tr = np.where(ts_ms < train_end_ms)[0]
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    model.fit(X[tr], yv[tr])
    joblib.dump(
        {
            "model": model,
            "feature_columns": cols,
            "model_name": "lgbm_regressor",
            "trained_until": f"{TRAIN_UNTIL} 00:00:00+00:00",
            "n_train": int(tr.size),
            "symbol": SYMBOL,
            "target": "direction",
        },
        DST / "model.joblib",
    )

    parent_strat = json.loads((PARENT / "strategy.json").read_text(encoding="utf-8"))
    strat = dict(parent_strat)
    strat.update(
        {
            "symbol": SYMBOL,
            "timeframe": TIMEFRAME,
            "horizon_bars": LABEL_HORIZON,
            "trained_until_exclusive": f"{TRAIN_UNTIL} 00:00:00+00:00",
            "lockbox_start": FORWARD_LOCKBOX_START,
            "feature_columns": cols,
            "strategy_id": (
                "structure_v1_lgbm_ETHUSDT_15m_direction_multitrade_wall_clock_p75_v1"
            ),
            "version_id": VERSION_ID,
            "execution_mode": "multitrade",
            "max_positions_per_side": 7,
            "tp_pct": 0.01,
            "sl_pct": 0.02,
            "sizing": "MIN_EXCHANGE",
            "signal_source": "binance",
            "touch_timeframe": "1m",
        }
    )
    strat["version_lineage"] = {
        "parent_pack": "structure_v1_ethusdt_multitrade_p75_v1",
        "research_arm": (
            "15m|wall_clock|K=7|fib1.618|base_hold24|addon48|lookback672|"
            "label24|strength_q=0.75|touch1m"
        ),
        "generation_id": GEN,
        "evidence_class": "OUTER_TRANSFER_COMPARE",
        "note": (
            "D-047 best arm. RESEARCH_ONLY. Live deploy FORBIDDEN without "
            "new certificate + explicit user auth."
        ),
    }
    strat["multitrade"] = {
        "version_id": VERSION_ID,
        "max_positions_per_side": 7,
        "clarity": "mean_strength",
        "clarity_scope": "all",
        "fib_ext": 1.618,
        "base_hold": 24,
        "hold_addon": 48,
        "base_tp": 0.01,
        "base_sl": 0.02,
        "mean_lookback": 672,
        "uniform_books": False,
        "bar_ms": 900_000,
        "strength_quantile": 0.75,
        "geometry": "wall_clock",
        "size_double_within_bars": 0,
    }
    strat["what_it_does"] = (
        "RESEARCH_ONLY ETH 15m multitrade wall-clock p75. K=7; mean_strength "
        "q=0.75 of 672-bar |mean|; base hold 24 / addon 48 (6h/12h); TP1%/SL2%; "
        "fib 1.618 books 3+; touch 1m. Not live."
    )
    strat.pop("account", None)
    if "live_auth" in (strat.get("version_lineage") or {}):
        strat["version_lineage"].pop("live_auth", None)
    (DST / "strategy.json").write_text(json.dumps(strat, indent=2) + "\n", encoding="utf-8")

    meta = {
        "version_id": VERSION_ID,
        "parent_pack": "structure_v1_ethusdt_multitrade_p75_v1",
        "research_arm": "15m_wall_clock_q75",
        "frozen_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "strategy_id": strat["strategy_id"],
        "status": "FROZEN_RESEARCH_ONLY",
        "readiness": "RESEARCH_ONLY",
        "timeframe": TIMEFRAME,
        "touch_timeframe": "1m",
        "live": {
            "deployed": False,
            "account_ref": None,
            "service": None,
            "note": "live_deploy FORBIDDEN until certificate + explicit user auth",
        },
        "metrics": {
            "profit_factor": stitched.get("profit_factor"),
            "expectancy_return_units": stitched.get("expectancy_return_units"),
            "n_trades": stitched.get("n_trades"),
            "win_rate": stitched.get("win_rate"),
            "window": "outer_v2_hard_end_2026-05-01",
            "source_report": str(REPORT.relative_to(ROOT)).replace("\\", "/"),
        },
        "evidence": {
            "report_paths": [str(REPORT.relative_to(ROOT)).replace("\\", "/")],
            "generation_id": GEN,
        },
    }
    (DST / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    (DST / "README.md").write_text(
        f"# {VERSION_ID}\n\n"
        "Frozen RESEARCH_ONLY: ETHUSDT 15m multitrade **wall-clock p75** (D-047).\n\n"
        f"Evidence: `{GEN}`. Touch=1m. **Live deploy FORBIDDEN**.\n",
        encoding="utf-8",
    )

    for name in ("certificate.yaml", "pack_hash.txt"):
        p = DST / name
        if p.is_file():
            p.unlink()
    fp = pack_fingerprint(DST)
    assert fp
    (DST / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8", newline="\n")
    meta["pack_hash"] = fp
    (DST / "pack_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    ensure_registry_schema()
    register_freeze(
        DST,
        evidence=meta["evidence"],
        metrics=meta["metrics"],
        status="FROZEN_RESEARCH_ONLY",
        readiness="RESEARCH_ONLY",
        require_run_id=False,
        ledger=True,
    )
    regenerate_versions_md()
    print(
        json.dumps(
            {
                "pack": str(DST.relative_to(ROOT)).replace("\\", "/"),
                "version_id": VERSION_ID,
                "pack_hash": fp,
                "n_train": int(tr.size),
                "n_features": len(cols),
                "metrics": meta["metrics"],
                "live_deploy": "FORBIDDEN",
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
