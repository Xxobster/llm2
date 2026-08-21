"""Nested hunt: structure_v1_run_retrace (causal run depth; never orange).

Orange / oracle_leaky imitation is sealed (D-058). This generation tests whether
knowable running-retrace state is tradable under V2.1.
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
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.v21 import format_gates_table  # noqa: E402
from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import FOLD_GEOMETRY_VERSION  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "structure_v1_run_retrace_alpha_001.yaml"
GENERATION = "structure_v1_run_retrace_alpha_001"
SPACE = "structure_v1_run_retrace"
COMBOS = (
    ("BTCUSDT", "1h", "fwd_return"),
    ("ETHUSDT", "1h", "direction"),
    ("SOLUSDT", "1h", "direction"),
    ("ETHUSDT", "1h", "fwd_return"),
    ("SOLUSDT", "1h", "fwd_return"),
    ("BTCUSDT", "1h", "direction"),
)
SEED_ROOT = 20260808


def _hash_prereg() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def _assert_clean_features(symbol: str, timeframe: str) -> None:
    ohlcv = load_ohlcv(symbol, timeframe)
    if len(ohlcv) > 800:
        ohlcv = ohlcv.iloc[-800:].copy()
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=timeframe)
    bad = [
        c
        for c in feats.columns
        if "oracle_leaky" in str(c).lower()
        or str(c).startswith("pred_leaky")
        or "last_retrace" in str(c).lower()
    ]
    if bad:
        raise RuntimeError(f"{SPACE} must not expose {bad}")
    need = ("run_retrace", "run_retrace_expand_max")
    missing = [c for c in need if c not in feats.columns]
    if missing:
        raise RuntimeError(f"{SPACE} missing causal run columns: {missing}")


def _leakage_gate(symbol: str, timeframe: str) -> dict:
    ohlcv = load_ohlcv(symbol, timeframe)
    if len(ohlcv) > 4000:
        ohlcv = ohlcv.iloc[-4000:].copy()
    result = run_audit_for_space(
        ohlcv, interval=timeframe, space=SPACE, symbol=symbol, cuts=2
    )
    if not result.get("ok"):
        raise RuntimeError(
            f"leakage gate FAIL for {symbol} {timeframe}: {result.get('report_text')}"
        )
    return {
        "ok": True,
        "leakage_potential": result.get("leakage_potential"),
        "n_bars": len(ohlcv),
        "space": SPACE,
    }


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing preregister: {PREREG}")
    text = PREREG.read_text(encoding="utf-8")
    if "status: OPEN" not in text and "preregister_sha256_at_run:" not in text:
        raise SystemExit("preregister is not OPEN and has no run hash — refusing")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    prereg_sha = _hash_prereg()
    append_ledger(
        f"RUN_RETRACE_ALPHA_001 start stamp={stamp} prereg_sha={prereg_sha[:16]} "
        f"space={SPACE} fold={FOLD_GEOMETRY_VERSION} lockbox={FORWARD_LOCKBOX_START}",
        tier=0,
    )
    print(f"preregister_sha256={prereg_sha}", flush=True)
    print(f"feature_space={SPACE} (causal run_retrace; orange forbidden)", flush=True)

    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(
            text.rstrip()
            + f"\n\npreregister_sha256_at_run: {prereg_sha}\n"
            + f"run_started_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n",
            encoding="utf-8",
        )

    print("ASSERT clean features …", flush=True)
    _assert_clean_features("ETHUSDT", "1h")
    print("ASSERT PASS", flush=True)

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
        gid = f"run_retrace_alpha_001_{i:02d}_{sym}_{tf}_{tgt}_{stamp[:8]}"
        append_ledger(f"RUN_RETRACE_ALPHA_001 hunt start {gid}", tier=0)
        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space=SPACE,
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
            "feature_space": SPACE,
            "tier": best.get("tier") or summary.get("best_tier"),
            "pooled_pf": best.get("pooled_pf"),
            "pooled_trades": best.get("pooled_trades"),
            "ann_sharpe": best.get("ann_sharpe") or (gates.get("metrics") or {}).get("ann_sharpe"),
            "overall": gates.get("overall"),
            "gates": gates,
            "model": best.get("model"),
            "status": summary.get("status"),
            "preregister_sha256": prereg_sha,
        }
        rows.append(row)
        print(
            f"{sym} {tf} {tgt}: tier={row['tier']} pf={row['pooled_pf']} "
            f"trades={row['pooled_trades']} overall={row['overall']} model={row['model']} "
            f"status={row['status']}",
            flush=True,
        )
        if gates:
            print(format_gates_table(gates), flush=True)

    out = {
        "generation_id": GENERATION,
        "stamp": stamp,
        "preregister": str(PREREG),
        "preregister_sha256": prereg_sha,
        "feature_space": SPACE,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "leakage": leakage_reports,
        "rows": rows,
        "readiness_max": "RESEARCH_ONLY",
        "promotion_allowed": False,
        "note": (
            "Causal running-retrace features only. Oracle/pred leaky sealed. "
            "Do not freeze packs with orange reconstructions."
        ),
    }
    out_path = ARTIFACTS / "reports" / f"{GENERATION}_{stamp}.json"
    latest = ARTIFACTS / "reports" / f"{GENERATION}_latest.json"
    out_path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    latest.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"WROTE {out_path}", flush=True)

    cur = PREREG.read_text(encoding="utf-8")
    if "status: OPEN" in cur:
        PREREG.write_text(
            cur.replace("status: OPEN", "status: FROZEN_OOS_VIEWED", 1)
            + f"frozen_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n"
            + "frozen_reason: outer-OOS of run_retrace_alpha_001 viewed; do not re-search.\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
