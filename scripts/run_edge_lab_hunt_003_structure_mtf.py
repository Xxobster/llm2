"""Edge lab hunt 003 — multi-timeframe swing structure, Average-True-Range brackets.

RESEARCH_ONLY. Never deploys. Resumable via SQLite checkpoint.
Screen window is strictly before 2022-01-01, so outer folds stay unseen.

Usage:

    python -u scripts/run_edge_lab_hunt_003_structure_mtf.py
    python -u scripts/run_edge_lab_hunt_003_structure_mtf.py --limit 12
    python -u scripts/run_edge_lab_hunt_003_structure_mtf.py --report-only
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

import numpy as np
import pandas as pd
import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from llm2.confluence.sim_arms import (  # noqa: E402
    arm_done,
    jsonable,
    load_arms,
    open_checkpoint,
    save_arm,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.edge_lab.events import session_mask  # noqa: E402
from llm2.edge_lab.sessions import session_frame  # noqa: E402
from llm2.edge_lab.sim_atr import run_atr_bracket_arm  # noqa: E402
from llm2.edge_lab.structure_mtf import (  # noqa: E402
    STRUCTURE_EVENT_SIDE,
    structure_mtf_events,
    structure_mtf_frame,
)
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402
from scripts.run_edge_lab_hunt_001 import (  # noqa: E402
    MIN_CONTEXT_BARS,
    SCREEN_END,
    _fmt,
    _passes,
    _recovery_factor,
    _screen_end_ms,
)

PREREG = _ROOT / "configs" / "preregister" / "edge_lab_hunt_003_structure_mtf.yaml"
OUT = ARTIFACTS / "reports" / "edge_lab"
DB_DIR = ARTIFACTS / "sqlite" / "edge_lab_hunt_003_structure_mtf"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _is_market(event: str) -> bool:
    return "break" in event


def _arm_id(symbol: str, tf: str, event: str, filt: str, k_sl: float, ratio: float) -> str:
    return f"{symbol}|{tf}|{event}|{filt}|ksl{k_sl}|r{ratio}"


class Context:
    """Pre-2022 candles plus the causal structure frame for one symbol/timeframe."""

    def __init__(self, symbol: str, timeframe: str, *, htf: str, wing: int) -> None:
        self.symbol = symbol
        self.timeframe = timeframe
        ohlcv = load_ohlcv(symbol, timeframe)
        ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < _screen_end_ms()].copy()
        if len(ohlcv) < MIN_CONTEXT_BARS:
            raise RuntimeError(f"{symbol} {timeframe}: only {len(ohlcv)} bars before {SCREEN_END}")
        self.ohlcv = ohlcv
        self.sc = make_bar_series(symbol, timeframe, ohlcv)
        self.frame = structure_mtf_frame(ohlcv, wing=int(wing), htf=htf, htf_wing=5)
        self.events = structure_mtf_events(self.frame)
        self.session = session_frame(ohlcv)
        self.n = len(ohlcv)


def _plan(cfg: dict) -> list[dict[str, Any]]:
    events = list(cfg["events"])
    unknown = [e for e in events if e not in STRUCTURE_EVENT_SIDE]
    if unknown:
        raise RuntimeError(f"preregistered events missing from catalogue: {unknown}")
    plan: list[dict[str, Any]] = []
    for tf in cfg["universe"]["timeframes"]:
        for symbol in cfg["universe"]["symbols"]:
            for k_sl in cfg["k_sl"]:
                for ratio in cfg["tp_ratio"]:
                    for filt in cfg["session_filters"]:
                        for event in events:
                            plan.append(
                                {
                                    "symbol": symbol,
                                    "timeframe": tf,
                                    "event": event,
                                    "session_filter": filt,
                                    "k_sl": float(k_sl),
                                    "tp_ratio": float(ratio),
                                }
                            )
    return plan


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    for r in rows:
        r["recovery_factor"] = _recovery_factor(r)
    ran = [r for r in rows if r.get("status") == "RAN"]
    gates = cfg["screen_gates"]
    passing = sorted(
        (r for r in ran if _passes(r, gates)), key=lambda r: -(float(r.get("profit_factor") or 0))
    )
    ran.sort(key=lambda r: -(float(r.get("profit_factor") or 0)))
    status_counts: dict[str, int] = {}
    for r in rows:
        status_counts[str(r.get("status"))] = status_counts.get(str(r.get("status")), 0) + 1

    payload = {
        "generation_id": "edge_lab_hunt_003_structure_mtf",
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "inner_screen_pre_2022_only",
        "not_live": True,
        "n_rows": len(rows),
        "status_counts": status_counts,
        "n_screen_pass": len(passing),
        "screen_gates": gates,
        "extra": extra,
        "screen_pass": passing,
        "top_ran": ran[:200],
    }
    (OUT / "hunt_003_structure_mtf_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# Edge lab hunt 003 — multi-timeframe swing structure",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"**Evidence class:** inner screen on bars before {SCREEN_END} only.",
        "",
        "Concepts ported from `C:\\projects\\wavetheory`; **no numeric result inherited** "
        "(its own proxy failed out of sample and had a pivot look-ahead).",
        "",
        f"Arms recorded: {len(rows)}. Status: "
        + ", ".join(f"{k}={v}" for k, v in sorted(status_counts.items()))
        + f". Screen passes: {len(passing)}.",
        "",
        "| Symbol | TF | Event | Session | k_sl | tp:sl | n | /mo | PF | WR | Sharpe | HAC | "
        "Sortino | Recovery | MDD% | ebr | mean SL |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in (passing or ran[:40]):
        md.append(
            "| {sym} | {tf} | `{ev}` | {ses} | {k} | {r} | {n} | {tpm} | {pf} | {wr} | "
            "{sh} | {hac} | {so} | {rf} | {mdd} | {ebr} | {slm} |".format(
                sym=r.get("symbol"), tf=r.get("timeframe"), ev=r.get("event"),
                ses=r.get("session_filter"), k=r.get("k_sl"), r=r.get("tp_ratio"),
                n=r.get("n_trades"), tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")), wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")), hac=_fmt(r.get("sharpe_hac_annualised")),
                so=_fmt(r.get("sortino_annualised")), rf=_fmt(r.get("recovery_factor")),
                mdd=_fmt(r.get("max_drawdown_pct")), ebr=_fmt(r.get("entry_bar_exit_rate")),
                slm=_fmt(r.get("sl_pct_mean")),
            )
        )
    if not passing:
        md.append("")
        md.append(
            "_No arm clears the frozen screen gates yet. Rows above are the best scored "
            "arms so far and are **not** candidates._"
        )
    (OUT / "hunt_003_structure_mtf_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    text = PREREG.read_text(encoding="utf-8")
    prereg_sha = _sha(PREREG)
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(
            text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8"
        )
        prereg_sha = _sha(PREREG)
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))

    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "hunt.sqlite")
    plan = _plan(cfg)
    extra = {"preregister_sha256": prereg_sha, "n_planned_arms": len(plan), "screen_end": SCREEN_END}

    if args.report_only:
        payload = write_report(con, cfg, stamp, extra)
        print(json.dumps({k: payload[k] for k in ("n_rows", "status_counts", "n_screen_pass")}, indent=2))
        return 0

    append_ledger(f"EDGE_LAB_HUNT_003_STRUCTURE_MTF start {stamp} planned={len(plan)}", tier=0)
    print(f"preregister_sha256={prereg_sha} planned_arms={len(plan)}", flush=True)

    work = [
        (i, s)
        for i, s in enumerate(plan)
        if not arm_done(
            con,
            _arm_id(
                s["symbol"], s["timeframe"], s["event"], s["session_filter"],
                s["k_sl"], s["tp_ratio"],
            ),
        )
    ]
    print(f"remaining_arms={len(work)}", flush=True)
    if args.limit:
        work = work[: int(args.limit)]

    htf_map = cfg["higher_timeframe_map"]
    wing_map = cfg["swing_wing"]
    work_bars = cfg["work_bars"]
    max_hold = cfg["max_hold_bars"]
    sl_cap = float(cfg["sl_cap"])
    ctx: Context | None = None
    ctx_key: tuple[str, str] | None = None
    since_report = 0

    for i, spec in work:
        symbol, tf = spec["symbol"], spec["timeframe"]
        event, filt = spec["event"], spec["session_filter"]
        k_sl, ratio = float(spec["k_sl"]), float(spec["tp_ratio"])
        aid = _arm_id(symbol, tf, event, filt, k_sl, ratio)

        if ctx_key != (symbol, tf):
            print(f"=== context {symbol} {tf} htf={htf_map[tf]} wing={wing_map[tf]} ===", flush=True)
            try:
                ctx = Context(symbol, tf, htf=str(htf_map[tf]), wing=int(wing_map[tf]))
            except Exception as exc:  # noqa: BLE001
                print(f"  CONTEXT_FAIL {symbol} {tf}: {exc}", flush=True)
                ctx = None
            ctx_key = (symbol, tf)
        if ctx is None:
            save_arm(con, aid, spec, {"status": "NO_CONTEXT", "n_trades": 0, "arm_id": aid, **spec})
            continue

        occ = ctx.events[event].to_numpy(dtype=np.int8) > 0
        mask = occ & session_mask(ctx.session, filt)
        side = int(STRUCTURE_EVENT_SIDE[event])
        n_gated = int(mask.sum())
        if n_gated < 15:
            payload: dict[str, Any] = {"status": "TOO_FEW_GATED", "n_intent": n_gated, "n_trades": 0}
        else:
            try:
                payload = run_atr_bracket_arm(
                    symbol,
                    ctx.sc,
                    mask,
                    np.full(n_gated, side < 0, dtype=bool),
                    tag=aid,
                    market=_is_market(event),
                    work=int(work_bars[tf]),
                    max_hold=int(max_hold[tf]),
                    k_sl=k_sl,
                    tp_ratio=ratio,
                    sl_cap=sl_cap,
                )
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}

        payload.update(
            {
                "symbol": symbol, "timeframe": tf, "event": event,
                "session_filter": filt, "k_sl": k_sl, "tp_ratio": ratio, "side": side,
                "entry_style": "market" if _is_market(event) else "working_limit",
                "htf": str(htf_map[tf]), "swing_wing": int(wing_map[tf]),
                "arm_id": aid, "plan_index": i,
            }
        )
        payload["recovery_factor"] = _recovery_factor(payload)
        save_arm(con, aid, spec, payload)
        since_report += 1
        print(
            f"[{i + 1}/{len(plan)}] {aid} -> {payload.get('status')} "
            f"n={payload.get('n_trades')} PF={_fmt(payload.get('profit_factor'))} "
            f"tpm={_fmt(payload.get('trades_per_month'))} "
            f"Sh={_fmt(payload.get('sharpe_annualised'))} "
            f"ebr={_fmt(payload.get('entry_bar_exit_rate'))} "
            f"slm={_fmt(payload.get('sl_pct_mean'))}",
            flush=True,
        )
        if since_report >= 40:
            write_report(con, cfg, stamp, extra)
            since_report = 0

    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"EDGE_LAB_HUNT_003_STRUCTURE_MTF report rows={payload['n_rows']} "
        f"pass={payload['n_screen_pass']}",
        tier=0,
    )
    print(
        f"WROTE {OUT / 'hunt_003_structure_mtf_latest.md'} rows={payload['n_rows']} "
        f"pass={payload['n_screen_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
