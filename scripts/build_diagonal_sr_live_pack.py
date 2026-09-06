"""Freeze a diagonal S/R rule-event live pack + four-proof + certificate.

RESEARCH readiness is NOT changed by this script. It only assembles the frozen
artifacts a live runner needs, and refuses to write an AUTHORIZED certificate
unless FOUR_PROOF_GATE_V1 is green.

Usage (one arm):

    python -u scripts/build_diagonal_sr_live_pack.py \
        --symbol ETHUSDT --timeframe 1h --event bounce_upper --generation A \
        --tp 0.015 --sl 0.01 \
        --account Xxobster4 --vps-host 94.156.189.76 \
        --authorized-from 2026-08-27 --expires 2026-09-26 --authorize
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

import yaml  # noqa: E402

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.four_proof_diagonal_sr import (  # noqa: E402
    run_four_proof_gate_diagonal_sr,
)
from llm2.gates.evidence import (  # noqa: E402
    DEFAULT_LEVERAGE_HAIRCUT,
    DEFAULT_MARK_BUFFER,
    DEFAULT_MM_BUFFER,
    leverage_ceiling_from_stop,
    leverage_from_stop,
)
from llm2.live.certificate import pack_fingerprint  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROOT  # noqa: E402
from llm2.research_policy import MIN_SIZE_EQUITY_CAVEAT, PolicyError  # noqa: E402

SETTLE_DB = ARTIFACTS / "sqlite" / "diagonal_sr_nested_settle_001" / "settle.sqlite"
PREREG = ROOT / "configs" / "preregister" / "diagonal_sr_nested_settle_001.yaml"
PACK_ROOT = ARTIFACTS / "live_packs"
CERT_DIR = ROOT / "configs" / "live"

# Frozen bracket geometry from the settle runner (do not diverge).
WORK_BARS = {"15m": 4, "1h": 3, "4h": 2}
MAX_HOLD_BARS = {"15m": 6, "1h": 8, "4h": 6}


def _settle_row(symbol: str, tf: str, gen: str, event: str, tp: float, sl: float) -> dict[str, Any]:
    if not SETTLE_DB.is_file():
        raise PolicyError(f"settle checkpoint missing: {SETTLE_DB}")
    arm_id = f"{symbol}|{tf}|{gen}|{event}|tp{tp}|sl{sl}|stitched"
    con = sqlite3.connect(str(SETTLE_DB))
    try:
        row = con.execute("SELECT payload FROM arms WHERE arm_id=?", (arm_id,)).fetchone()
    finally:
        con.close()
    if row is None:
        raise PolicyError(f"no stitched settle row for {arm_id}")
    return json.loads(row[0])


def _fold_rows(symbol: str, tf: str, gen: str, event: str, tp: float, sl: float) -> list[dict[str, Any]]:
    prefix = f"{symbol}|{tf}|{gen}|{event}|tp{tp}|sl{sl}|fold"
    con = sqlite3.connect(str(SETTLE_DB))
    try:
        out = [
            json.loads(payload)
            for arm_id, payload in con.execute("SELECT arm_id, payload FROM arms")
            if str(arm_id).startswith(prefix)
        ]
    finally:
        con.close()
    return sorted(out, key=lambda r: int(r.get("fold_index") or 0))


def _keep(row: dict[str, Any]) -> dict[str, Any]:
    keys = (
        "status",
        "n_intent",
        "fill_pct",
        "n_trades",
        "n_longs",
        "n_shorts",
        "trades_per_month",
        "profit_factor",
        "win_rate",
        "win_rate_ci_low",
        "win_rate_ci_high",
        "expectancy",
        "net_pnl",
        "total_return",
        "payoff_ratio",
        "sharpe_annualised",
        "sharpe_raw",
        "sharpe_hac_annualised",
        "sortino_annualised",
        "max_drawdown_pct",
        "exposure",
        "total_fees",
        "total_funding",
        "n_liquidations",
        "entry_bar_exit_rate",
        "avg_hold_bars",
        "n_exits_tp",
        "n_exits_sl",
        "span_days",
        "touch_timeframe",
        "touch_resolved_rate",
        "ambiguous_rate",
        "n_folds_ran",
        "n_folds_positive",
        "fold_index",
    )
    return {k: row.get(k) for k in keys if k in row}


def build(args: argparse.Namespace) -> int:
    symbol = args.symbol.upper()
    tf = args.timeframe
    event = args.event
    gen = args.generation.upper()
    tp = float(args.tp)
    sl = float(args.sl)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    survivors = (yaml.safe_load(PREREG.read_text(encoding="utf-8")) or {}).get("survivors") or []
    if not any(
        s["symbol"] == symbol
        and s["timeframe"] == tf
        and s["event"] == event
        and s["generation"] == gen
        and float(s["tp"]) == tp
        and float(s["sl"]) == sl
        for s in survivors
    ):
        raise PolicyError(
            f"{symbol} {tf} {gen} {event} tp{tp} sl{sl} is not in the frozen "
            f"survivor list of {PREREG.name}. Refusing to invent a new arm at deploy time."
        )

    stitched = _settle_row(symbol, tf, gen, event, tp, sl)
    folds = _fold_rows(symbol, tf, gen, event, tp, sl)
    if str(stitched.get("status")) != "RAN":
        raise PolicyError(f"settle status {stitched.get('status')} — refuse pack")

    lev = leverage_from_stop(sl)
    lev_ceiling = leverage_ceiling_from_stop(sl)
    slug = f"diagonal-sr-{symbol[:3].lower()}-{event.replace('_', '-')}-{tf}"
    arm_id = f"{symbol}|{tf}|{gen}|{event}|tp{tp}|sl{sl}"
    pack_dir = PACK_ROOT / slug.replace("-", "_")
    pack_dir.mkdir(parents=True, exist_ok=True)

    strategy = {
        "arm_id": arm_id,
        "strategy_id": slug,
        "family": "diagonal_sr_rule_event",
        "space": "diagonal_sr_v1",
        "symbol": symbol,
        "timeframe": tf,
        "event": event,
        "generation": gen,
        "side": "short" if event in {"bounce_upper", "channel_walk_short", "break_lower"} else "long",
        "entry": "working_limit_atr_offset",
        "tp_pct": tp,
        "sl_pct": sl,
        "work_bars": int(WORK_BARS[tf]),
        "max_hold_bars": int(MAX_HOLD_BARS[tf]),
        "leverage": float(lev),
        "leverage_derivation": {
            "sl_pct": sl,
            "mm_buffer": DEFAULT_MM_BUFFER,
            "mark_buffer": DEFAULT_MARK_BUFFER,
            "ceiling_floor_1_over_denom": int(lev_ceiling),
            "haircut": DEFAULT_LEVERAGE_HAIRCUT,
            "leverage_used_live_and_backtest": float(lev),
            "note": "Backtest margin used research_margin(leverage=leverage_from_stop(sl)) — identical value.",
        },
        "sizing": {"mode": "MIN_EXCHANGE", "size_mult": 1.0},
        "signal_module": "llm2.diagonal_sr.live_signal:tip_signal",
        "runner": "llm2.live.diagonal_sr_runner",
        "limit_move_clip": [0.0015, 0.03],
        "limit_move_fallback": 0.005,
        "htf_context_used": False,
        "session_filter": None,
        "frozen_at_utc": stamp,
    }
    (pack_dir / "strategy.json").write_text(
        json.dumps(strategy, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    meta = {
        "strategy_id": slug,
        "arm_id": arm_id,
        "space": "diagonal_sr_v1",
        "status": "FROZEN_LIVE_PACK",
        "readiness": "RESEARCH_ONLY",
        "readiness_note": (
            "Nested outer out-of-sample settle before lockbox. NOT SHADOW_READY: "
            "the survivor list was selected after viewing hunt-001 inner test "
            "metrics, and there is no forward shadow reconciliation yet. "
            "User-authorized minimum-size live test only."
        ),
        "evidence_class": "nested_outer_oos_pre_lockbox",
        "evidence_window_end": str(FORWARD_LOCKBOX_START),
        "preregister": str(PREREG.relative_to(ROOT)),
        "preregister_sha256": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
        "settle_db": str(SETTLE_DB.relative_to(ROOT)),
        "stitched_outer_oos": _keep(stitched),
        "folds": [_keep(f) for f in folds],
        "min_size_equity_caveat": MIN_SIZE_EQUITY_CAVEAT,
        "known_risks": [
            f"entry_bar_exit_rate={stitched.get('entry_bar_exit_rate')} "
            "(stops resolved inside the entry bar; >0.25 means the stop sits in single-bar noise)",
            "fold0 (2022) carries the highest entry-bar rate and the largest share of profit",
            "selection touched inner-test metrics before this settle",
        ],
        "frozen_at_utc": stamp,
    }
    (pack_dir / "pack_meta.json").write_text(
        json.dumps(meta, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(f"=== FOUR_PROOF_GATE_V1 {symbol} {tf} {event} ===", flush=True)
    ohlcv = load_ohlcv(symbol, tf)
    summary = run_four_proof_gate_diagonal_sr(
        symbol=symbol,
        timeframe=tf,
        event=event,
        generation=gen,
        ohlcv=ohlcv,
        tip_bars=int(args.tip_bars),
    )
    (pack_dir / "four_proof_summary.json").write_text(
        json.dumps(summary, indent=2, default=str, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not summary["ok"]:
        raise PolicyError(
            f"FOUR_PROOF_GATE_V1 FAILED for {arm_id}: {summary['proofs_ok']}. "
            "Refusing to write an AUTHORIZED certificate."
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
        f"# {slug}\n\n"
        f"Diagonal support/resistance rule event `{event}` on {symbol} {tf} "
        f"(take-profit {tp:.3%} / stop-loss {sl:.3%}, leverage {lev:g}x).\n\n"
        "No model. The decide is the causal occurrence bit from "
        "`llm2.diagonal_sr.live_signal:tip_signal` — the same function the nested "
        "settle scores.\n\n"
        f"**Readiness: RESEARCH_ONLY.** Evidence is stitched outer out-of-sample "
        f"before {FORWARD_LOCKBOX_START}. Profit factor "
        f"{stitched.get('profit_factor')}, {stitched.get('n_trades')} trades, "
        f"entry-bar exit rate {stitched.get('entry_bar_exit_rate')}.\n",
        encoding="utf-8",
    )

    pack_hash = pack_fingerprint(pack_dir)
    if not pack_hash:
        raise PolicyError(f"pack_fingerprint empty for {pack_dir}")

    cert_path = CERT_DIR / f"{slug.replace('-', '_')}_certificate.yaml"
    cert = {
        "strategy_id": slug,
        "arm_id": arm_id,
        "status": "AUTHORIZED" if args.authorize else "BLOCKED",
        "authorized_by_user": bool(args.authorize),
        "authorized_scope": "MICRO / MIN_EXCHANGE quantity only",
        "authorization_source": args.authorization_source,
        "vps_host": args.vps_host,
        "account_ref": args.account,
        "pack_dir": str(pack_dir.relative_to(ROOT)),
        "pack_hash": pack_hash,
        "authorized_from_utc": f"{args.authorized_from}T00:00:00Z",
        "expires_utc": f"{args.expires}T00:00:00Z",
        "symbol": symbol,
        "timeframe": tf,
        "event": event,
        "tp_pct": tp,
        "sl_pct": sl,
        "leverage": float(lev),
        "sizing_mode": "MIN_EXCHANGE",
        "four_proof_ok": True,
        "four_proof_hashes": summary["artifact_hashes"],
        "research_readiness": "RESEARCH_ONLY (not SHADOW_READY)",
        "blockers_acknowledged": meta["known_risks"],
        "created_utc": stamp,
    }
    CERT_DIR.mkdir(parents=True, exist_ok=True)
    cert_path.write_text(yaml.safe_dump(cert, sort_keys=False), encoding="utf-8")

    print(
        json.dumps(
            {
                "pack_dir": str(pack_dir),
                "pack_hash": pack_hash,
                "cert": str(cert_path),
                "leverage": lev,
                "four_proof_ok": summary["ok"],
                "stitched_pf": stitched.get("profit_factor"),
                "stitched_n": stitched.get("n_trades"),
                "entry_bar_exit_rate": stitched.get("entry_bar_exit_rate"),
            },
            indent=2,
        ),
        flush=True,
    )
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--timeframe", required=True)
    ap.add_argument("--event", required=True)
    ap.add_argument("--generation", default="A")
    ap.add_argument("--tp", type=float, required=True)
    ap.add_argument("--sl", type=float, required=True)
    ap.add_argument("--account", required=True)
    ap.add_argument("--vps-host", required=True)
    ap.add_argument("--authorized-from", required=True, help="YYYY-MM-DD")
    ap.add_argument("--expires", required=True, help="YYYY-MM-DD")
    ap.add_argument("--tip-bars", type=int, default=24)
    ap.add_argument(
        "--authorization-source",
        default="user chat instruction",
        help="Free-text record of who authorized and when.",
    )
    ap.add_argument("--authorize", action="store_true")
    return build(ap.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
