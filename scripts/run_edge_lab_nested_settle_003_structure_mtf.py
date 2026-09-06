"""Edge lab nested outer out-of-sample settle 003 (WaveTheory structure events).

RESEARCH_ONLY. Scores the 24 mechanically frozen hunt 003 survivors once per
outer fold and once on the stitched outer out-of-sample union. Never deploys.
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
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES, build_outer_folds, index_to_ms  # noqa: E402
from scripts.run_edge_lab_nested_settle_002_atr import (  # noqa: E402
    _fmt,
    _gate_verdict,
)

PREREG = _ROOT / "configs" / "preregister" / "edge_lab_nested_settle_003_structure_mtf.yaml"
OUT = ARTIFACTS / "reports" / "edge_lab"
DB_DIR = ARTIFACTS / "sqlite" / "edge_lab_nested_settle_003_structure_mtf"
MAX_ROWS = {"5m": 400_000, "15m": 150_000, "1h": 45_000, "4h": 20_000}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _lock_ms() -> int:
    return int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)


def _is_market(event: str) -> bool:
    return "break" in event


class Ctx:
    def __init__(self, symbol: str, tf: str, *, htf: str, wing: int) -> None:
        self.symbol = symbol
        self.tf = tf
        ohlcv = load_ohlcv(symbol, tf)
        ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < _lock_ms()].copy()
        cap = MAX_ROWS.get(tf, 60_000)
        if len(ohlcv) > cap:
            ohlcv = ohlcv.iloc[-cap:].copy()
        self.ohlcv = ohlcv
        self.sc = make_bar_series(symbol, tf, ohlcv)
        print(
            f"  structure frame {symbol} {tf} htf={htf} wing={wing} bars={len(ohlcv)}",
            flush=True,
        )
        self.frame = structure_mtf_frame(ohlcv, wing=int(wing), htf=htf, htf_wing=5)
        self.events = structure_mtf_events(self.frame)
        self.session = session_frame(ohlcv)
        self.folds = build_outer_folds(self.sc.ts_ms, purge_bars=24, embargo_bars=24)
        self.oos_union = np.zeros(len(self.sc.ts_ms), dtype=bool)
        for f in self.folds:
            self.oos_union |= (self.sc.ts_ms >= f.oos_start_ms) & (self.sc.ts_ms < f.oos_end_ms)
        print(
            f"  folds={len(self.folds)} oos_bars={int(self.oos_union.sum())} "
            f"span={ohlcv.index[0].date()}..{ohlcv.index[-1].date()}",
            flush=True,
        )


def _arm_id(spec: dict, kind: str, fold: int | None = None) -> str:
    base = (
        f"{spec['symbol']}|{spec['timeframe']}|{spec['event']}|{spec['session_filter']}|"
        f"ksl{spec['k_sl']}|r{spec['tp_ratio']}|{kind}"
    )
    return f"{base}|fold{fold}" if fold is not None else base


def _run(ctx: Ctx, spec: dict, window: np.ndarray, tag: str, cfg: dict) -> dict[str, Any]:
    event = spec["event"]
    tf = spec["timeframe"]
    occ = ctx.events[event].to_numpy(dtype=np.int8) > 0
    mask = occ & session_mask(ctx.session, spec["session_filter"]) & window
    n_gated = int(mask.sum())
    if n_gated < 5:
        return {"status": "TOO_FEW_GATED", "n_intent": n_gated, "n_trades": 0}
    is_short = np.full(n_gated, int(STRUCTURE_EVENT_SIDE[event]) < 0, dtype=bool)
    return run_atr_bracket_arm(
        spec["symbol"],
        ctx.sc,
        mask,
        is_short,
        tag=tag,
        market=_is_market(event),
        work=int(cfg["work_bars"][tf]),
        max_hold=int(cfg["max_hold_bars"][tf]),
        k_sl=float(spec["k_sl"]),
        tp_ratio=float(spec["tp_ratio"]),
        sl_cap=float(cfg["sl_cap"]),
    )


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    stitched = [r for r in rows if r.get("kind") == "stitched"]
    gates = cfg["gates_for_shadow_ready"]
    for r in stitched:
        ok, fails = _gate_verdict(r, gates)
        r["gate_pass"] = ok
        r["gate_fails"] = fails
    stitched.sort(key=lambda r: -(float(r.get("profit_factor") or 0)))
    n_pass = sum(1 for r in stitched if r.get("gate_pass"))
    payload = {
        "generation_id": "edge_lab_nested_settle_003_structure_mtf",
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "stitched_outer_oos_pre_lockbox",
        "not_live": True,
        "n_rows": len(rows),
        "n_stitched": len(stitched),
        "n_gate_pass": n_pass,
        "gates": gates,
        "selection": cfg["selection"],
        "extra": extra,
        "stitched": stitched,
        "all": rows,
    }
    (OUT / "nested_settle_003_structure_mtf_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# Edge lab nested outer out-of-sample settle 003 (WaveTheory structure)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Arms: {len(stitched)} stitched. Clearing all gates: **{n_pass}**.",
        "",
        "| Symbol | TF | Event | Session | k_sl | r | n | PF | HAC | ebr | folds+ | inner PF | gate |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in stitched:
        verdict = "PASS" if r.get("gate_pass") else "fail: " + ",".join(r.get("gate_fails") or [])
        md.append(
            "| {sym} | {tf} | `{ev}` | {ses} | {k} | {r} | {n} | {pf} | {hac} | {ebr} | "
            "{fo} | {ipf} | {v} |".format(
                sym=r.get("symbol"), tf=r.get("timeframe"), ev=r.get("event"),
                ses=r.get("session_filter"), k=r.get("k_sl"), r=r.get("tp_ratio"),
                n=r.get("n_trades"), pf=_fmt(r.get("profit_factor"), 2),
                hac=_fmt(r.get("sharpe_hac_annualised"), 2),
                ebr=_fmt(r.get("entry_bar_exit_rate"), 2),
                fo=f"{r.get('n_folds_positive')}/{r.get('n_folds_ran')}",
                ipf=_fmt(r.get("inner_profit_factor"), 2), v=verdict,
            )
        )
    (OUT / "nested_settle_003_structure_mtf_latest.md").write_text(
        "\n".join(md) + "\n", encoding="utf-8"
    )
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument(
        "--skip-timeframes",
        default="",
        help="Comma-separated timeframes to skip (e.g. 5m) when memory is tight.",
    )
    ap.add_argument(
        "--checkpoint-db",
        default="",
        help="SQLite filename under the settle dir (default settle.sqlite). "
        "Use a separate file for the 5-minute batch so a crash cannot rewrite 15m/1h rows.",
    )
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
    db_name = str(args.checkpoint_db).strip() or "settle.sqlite"
    con = open_checkpoint(DB_DIR / db_name)
    extra = {
        "preregister_sha256": prereg_sha,
        "fold_ranges": list(OUTER_FOLD_RANGES),
        "checkpoint_db": db_name,
    }

    if args.report_only:
        payload = write_report(con, cfg, stamp, extra)
        print(json.dumps({k: payload[k] for k in ("n_rows", "n_stitched", "n_gate_pass")}, indent=2))
        return 0

    survivors = list(cfg["survivors"])
    skip = {t.strip() for t in str(args.skip_timeframes).split(",") if t.strip()}
    if skip:
        survivors = [s for s in survivors if str(s["timeframe"]) not in skip]
        print(f"skip_timeframes={sorted(skip)} remaining={len(survivors)}", flush=True)
    htf_map = cfg["higher_timeframe_map"]
    wing_map = cfg["swing_wing"]
    append_ledger(f"EDGE_LAB_NESTED_SETTLE_003 start {stamp} arms={len(survivors)}", tier=0)
    print(f"preregister_sha256={prereg_sha} survivors={len(survivors)}", flush=True)

    survivors.sort(key=lambda s: (s["timeframe"], s["symbol"]))
    ctx: Ctx | None = None
    ctx_key: tuple[str, str] | None = None

    for spec in survivors:
        key = (spec["symbol"], spec["timeframe"])
        if ctx_key != key:
            print(f"=== context {key} ===", flush=True)
            try:
                ctx = Ctx(
                    *key,
                    htf=str(htf_map[spec["timeframe"]]),
                    wing=int(wing_map[spec["timeframe"]]),
                )
            except Exception as exc:  # noqa: BLE001
                print(f"  CONTEXT_FAIL {key}: {exc}", flush=True)
                ctx = None
            ctx_key = key
        if ctx is None:
            continue

        for f in ctx.folds:
            aid = _arm_id(spec, "fold", f.fold_index)
            if arm_done(con, aid):
                continue
            window = (ctx.sc.ts_ms >= f.oos_start_ms) & (ctx.sc.ts_ms < f.oos_end_ms)
            try:
                payload = _run(ctx, spec, window, aid, cfg)
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
            payload.update({**spec, "kind": "fold", "fold_index": f.fold_index, "arm_id": aid})
            save_arm(con, aid, spec, payload)
            print(
                f"  fold{f.fold_index} {spec['symbol']} {spec['timeframe']} {spec['event']} "
                f"-> {payload.get('status')} n={payload.get('n_trades')} "
                f"PF={_fmt(payload.get('profit_factor'), 2)}",
                flush=True,
            )

        aid = _arm_id(spec, "stitched")
        if not arm_done(con, aid):
            try:
                payload = _run(ctx, spec, ctx.oos_union, aid, cfg)
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
            prefix = _arm_id(spec, "fold").rsplit("|fold", 1)[0] + "|fold"
            ran = pos = 0
            for arm_id, raw in con.execute("SELECT arm_id, payload FROM arms"):
                if not str(arm_id).startswith(prefix):
                    continue
                fr = json.loads(raw)
                if fr.get("status") != "RAN":
                    continue
                ran += 1
                if float(fr.get("net_pnl") or 0) > 0 and float(fr.get("profit_factor") or 0) > 1:
                    pos += 1
            payload.update(
                {**spec, "kind": "stitched", "n_folds_ran": ran, "n_folds_positive": pos,
                 "arm_id": aid}
            )
            save_arm(con, aid, spec, payload)
            ok, fails = _gate_verdict(payload, cfg["gates_for_shadow_ready"])
            print(
                f"  STITCHED {spec['symbol']} {spec['timeframe']} {spec['event']} -> "
                f"{payload.get('status')} n={payload.get('n_trades')} "
                f"PF={_fmt(payload.get('profit_factor'), 2)} "
                f"(inner {_fmt(spec.get('inner_profit_factor'), 2)}) "
                f"HAC={_fmt(payload.get('sharpe_hac_annualised'), 2)} "
                f"ebr={_fmt(payload.get('entry_bar_exit_rate'), 2)} "
                f"folds+={pos}/{ran} gate={'PASS' if ok else ','.join(fails)}",
                flush=True,
            )
            write_report(con, cfg, stamp, extra)

    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"EDGE_LAB_NESTED_SETTLE_003 done stitched={payload['n_stitched']} "
        f"pass={payload['n_gate_pass']}",
        tier=0,
    )
    print(
        f"WROTE {OUT / 'nested_settle_003_structure_mtf_latest.md'} "
        f"stitched={payload['n_stitched']} gate_pass={payload['n_gate_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
