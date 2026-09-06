"""Freeze Solana 1h Exponential Moving Average stack live pack + four-proof + certificate.

Readiness remains RESEARCH_ONLY. User-authorized 5% equity stop-risk Post-Only test.

    python -u scripts/build_sol_ema_stack_live_pack.py --authorize
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.four_proof_ema_stack import run_four_proof_gate_ema_stack  # noqa: E402
from llm2.gates.evidence import (  # noqa: E402
    DEFAULT_LEVERAGE_HAIRCUT,
    DEFAULT_MARK_BUFFER,
    DEFAULT_MM_BUFFER,
    leverage_ceiling_from_stop,
    leverage_from_stop,
)
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.ml_lab.live_guards import SOL_EMA_SPEC  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROOT  # noqa: E402
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT, PolicyError  # noqa: E402
from llm2.sizing_policy import DEFAULT_STOP_RISK_FRACTION, SIZING_MODE_RISK_FRACTION  # noqa: E402

PACK_ROOT = ARTIFACTS / "live_packs"
CERT_DIR = ROOT / "configs" / "live"
SLUG = "sol_1h_power_ema_stack_long"
ARM_ID = "SOLUSDT|1h|power_ema_stack_long|atr1.5|slcap0.03"

# Bybit linear SOLUSDT lot rules as of 2026-09-01 (public instruments-info).
SOL_INSTRUMENT = {
    "symbol": "SOLUSDT",
    "tick_size": 0.01,
    "qty_step": 0.1,
    "min_qty": 0.1,
    "min_notional": 5.0,
    "max_qty": 96000.0,
    "max_leverage": 100.0,
    "source": "bybit_v5_instruments-info_20260901",
}


def build(args: argparse.Namespace) -> int:
    spec = dict(SOL_EMA_SPEC)
    sl_cap = float(spec["sl_cap"])
    lev = leverage_from_stop(sl_cap)
    lev_ceiling = leverage_ceiling_from_stop(sl_cap)
    if abs(lev - 13.0) > 1e-9:
        raise PolicyError(f"expected 13× from 3% cap, got {lev}")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    pack_dir = PACK_ROOT / SLUG
    pack_dir.mkdir(parents=True, exist_ok=True)

    strategy: dict[str, Any] = {
        "arm_id": ARM_ID,
        "strategy_id": SLUG,
        "family": "ml_lab_ema_stack",
        "space": "ml_lab_ema_stack_v1",
        "symbol": spec["symbol"],
        "timeframe": spec["timeframe"],
        "idea": spec["idea"],
        "side": "long",
        "entry": spec["entry"],
        "expired_entry": spec["expired_entry"],
        "k_sl": float(spec["k_sl"]),
        "tp_ratio": float(spec["tp_ratio"]),
        "sl_cap": sl_cap,
        "work_bars": int(spec["work_bars"]),
        "max_hold_bars": int(spec["max_hold_bars"]),
        "leverage": float(lev),
        "leverage_derivation": {
            "sl_pct": sl_cap,
            "note": "Leverage from the 3% stop cap (worst-case Average True Range stop), not from the 1% pivot default.",
            "mm_buffer": DEFAULT_MM_BUFFER,
            "mark_buffer": DEFAULT_MARK_BUFFER,
            "ceiling_floor_1_over_denom": int(lev_ceiling),
            "haircut": DEFAULT_LEVERAGE_HAIRCUT,
            "leverage_used_live_and_backtest": float(lev),
        },
        "risk_fraction": float(DEFAULT_STOP_RISK_FRACTION),
        "sizing": {
            "mode": SIZING_MODE_RISK_FRACTION,
            "risk_fraction": float(DEFAULT_STOP_RISK_FRACTION),
            "size_mult": 1.0,
            "note": "qty = floor((equity * 0.05) / (price * bar_sl) / qty_step) * qty_step; skip if below venue min.",
        },
        "signal_module": "llm2.ml_lab.live_signal:tip_signal",
        "runner": "llm2.live.ema_stack_runner",
        "instrument": SOL_INSTRUMENT,
        "htf_context_used": False,
        "session_filter": None,
        "frozen_at_utc": stamp,
        "readiness_max": "RESEARCH_ONLY",
        "promotion_allowed": False,
    }
    (pack_dir / "strategy.json").write_text(
        json.dumps(strategy, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    meta = {
        "strategy_id": SLUG,
        "arm_id": ARM_ID,
        "space": "ml_lab_ema_stack_v1",
        "status": "FROZEN_LIVE_PACK",
        "readiness": "RESEARCH_ONLY",
        "readiness_note": (
            "EXEC-021 maker-limit retest n=669 profit factor 1.231 Sharpe 1.17 "
            "entry-bar 0.063. Not SHADOW_READY: Gate C all-taker stress failed. "
            "User-authorized 5% equity stop-risk Post-Only live test only."
        ),
        "evidence_class": "stitched_outer_oos_pre_lockbox_plus_exec021_retest",
        "evidence_window_end": str(FORWARD_LOCKBOX_START),
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "frozen_at_utc": stamp,
    }
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )

    print("=== FOUR_PROOF_GATE_V1 SOLUSDT 1h power_ema_stack_long ===", flush=True)
    ohlcv = load_ohlcv(spec["symbol"], spec["timeframe"])
    summary = run_four_proof_gate_ema_stack(
        symbol=str(spec["symbol"]),
        timeframe=str(spec["timeframe"]),
        ohlcv=ohlcv,
        tip_bars=int(args.tip_bars),
    )
    (pack_dir / "four_proof_summary.json").write_text(
        json.dumps(summary, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not summary["ok"]:
        raise PolicyError(
            f"FOUR_PROOF_GATE_V1 FAILED: {summary['proofs_ok']}. Refusing certificate."
        )

    meta["evidence"] = {
        "four_proof_hashes": summary["artifact_hashes"],
        "four_proof_ok": True,
        "four_proof_summary_sha256": summary["summary_sha256"],
        "four_proof_artifact_dir": summary["artifact_dir"],
        "four_proof_stamp": summary["stamp"],
    }
    meta["four_proof_ok"] = True
    meta["four_proof_hashes"] = summary["artifact_hashes"]
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    (pack_dir / "README.md").write_text(
        f"# {SLUG}\n\n"
        "Solana 1-hour `power_ema_stack_long`. Post-Only entry, cancel if no touch. "
        "Stop = clip(1.5 × Average True Range %, 0.4%, 3%). Leverage 13× from the 3% cap. "
        "Size = 5% of equity at that bar's stop, floored to Bybit qty_step 0.1. "
        "Not Shadow-Ready.\n",
        encoding="utf-8",
    )

    fp = pack_fingerprint(pack_dir)
    if not fp:
        raise PolicyError("pack fingerprint failed")
    (pack_dir / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    meta["pack_hash"] = fp
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    fp2 = pack_fingerprint(pack_dir)
    meta["pack_hash"] = fp2
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    (pack_dir / "pack_hash.txt").write_text(fp2 + "\n", encoding="utf-8")

    if args.authorize:
        cert_path = CERT_DIR / "sol_1h_power_ema_stack_long_xxobster4_ln1_certificate.yaml"
        exp = args.expires
        created = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        hashes = summary["artifact_hashes"]
        cert_path.write_text(
            f"""strategy_id: {SLUG}
arm_id: {ARM_ID}
status: AUTHORIZED
authorized_by_user: true
authorized_scope: 5% equity stop-risk Post-Only (floor to Bybit qty step; skip if below min)
authorization_source: >-
  user chat 2026-09-01: replace Xxobster4 diagonal bots with Solana 1h EMA stack,
  min Post-Only, 5% of equity as risk based on stop-loss, do not treat as taker.
vps_host: {args.vps_host}
account_ref: {args.account}
pack_path: artifacts/live_packs/{SLUG}
pack_hash: {fp2}
authorized_from_utc: '{args.authorized_from}T00:00:00Z'
expires_utc: '{exp}T00:00:00Z'
created_utc: '{created}'
symbol: SOLUSDT
timeframe: 1h
idea: power_ema_stack_long
leverage: {float(lev)}
risk_fraction: {float(DEFAULT_STOP_RISK_FRACTION)}
sizing_mode: {SIZING_MODE_RISK_FRACTION}
four_proof_ok: true
four_proof_hashes:
  builder_responsiveness: {hashes.get("builder_responsiveness")}
  recompute_prefix: {hashes.get("recompute_prefix")}
  no_live_feature_fill: {hashes.get("no_live_feature_fill")}
  layer_a_pred_identity: {hashes.get("layer_a_pred_identity")}
research_readiness: RESEARCH_ONLY (not SHADOW_READY)
blockers_acknowledged:
- Gate C all-taker stress Profit Factor 0.853 FAIL (does not require market-entry live)
- fill rate ~33% on working limit; unfilled Post-Only cancels and stays flat
""",
            encoding="utf-8",
        )
        print(f"CERT {cert_path}", flush=True)

    print(f"PACK {pack_dir} hash={fp2}", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--account", default="Xxobster4")
    ap.add_argument("--vps-host", default="94.156.189.76")
    ap.add_argument("--authorized-from", default="2026-09-01")
    ap.add_argument("--expires", default="2026-10-01")
    ap.add_argument("--tip-bars", type=int, default=24)
    ap.add_argument("--authorize", action="store_true")
    return build(ap.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
