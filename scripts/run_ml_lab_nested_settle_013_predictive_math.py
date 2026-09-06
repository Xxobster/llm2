"""Nested outer settle of hunt-013 inner screen passers.

RESEARCH_ONLY. Scores 2022-01-01 .. 2026-05-01 once. Never retunes. Never deploys.
Maker 0.02% resting legs. EXEC-021 1-minute fill clock.
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
from llm2.edge_lab.sim_atr import run_atr_bracket_arm  # noqa: E402
from llm2.gates.evidence import research_maker_first_costs  # noqa: E402
from llm2.ml_lab.idea_catalog_j import signals_j  # noqa: E402
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import OUTER_FOLD_RANGES, build_outer_folds, index_to_ms  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "ml_lab_nested_settle_013_predictive_math.yaml"
OUT = ARTIFACTS / "reports" / "ml_lab"
DB_DIR = ARTIFACTS / "sqlite" / "ml_lab_nested_settle_013_predictive_math"
COSTS = research_maker_first_costs()
CATALOGS = {"j": signals_j}


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _lock_ms() -> int:
    return int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)


def _fmt(v: Any, nd: int = 3) -> str:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ""
    return f"{x:.{nd}f}" if np.isfinite(x) else ""


def _arm_id(spec: dict, kind: str, fold: int | None = None) -> str:
    base = f"{spec['symbol']}|{spec['timeframe']}|{spec['idea']}|{kind}"
    return f"{base}|fold{fold}" if fold is not None else base


def gate_verdict(r: dict[str, Any], g: dict[str, Any]) -> tuple[bool, list[str]]:
    fails: list[str] = []

    def num(k: str) -> float:
        try:
            return float(r.get(k))
        except (TypeError, ValueError):
            return float("nan")

    if int(r.get("n_trades") or 0) < int(g["min_pooled_oos_trades"]):
        fails.append(f"pooled_trades<{g['min_pooled_oos_trades']}")
    if not (num("profit_factor") >= float(g["min_pooled_profit_factor"])):
        fails.append(f"pf<{g['min_pooled_profit_factor']}")
    if not (num("sharpe_annualised") >= float(g["min_sharpe_annualised"])):
        fails.append(f"sharpe<{g['min_sharpe_annualised']}")
    if not (num("sharpe_hac_annualised") >= float(g["min_sharpe_hac_annualised"])):
        fails.append(f"hac_sharpe<{g['min_sharpe_hac_annualised']}")
    if not (num("entry_bar_exit_rate") <= float(g["max_entry_bar_exit_rate"])):
        fails.append(f"entry_bar>{g['max_entry_bar_exit_rate']}")
    ran = int(r.get("n_folds_ran") or 0)
    pos = int(r.get("n_folds_positive") or 0)
    if ran < int(g["min_eligible_folds"]):
        fails.append(f"eligible_folds<{g['min_eligible_folds']}")
    elif ran and pos / ran < float(g["min_fraction_positive_folds"]):
        fails.append(f"positive_folds<{g['min_fraction_positive_folds']:.0%}")
    return (not fails), fails


class Ctx:
    def __init__(self, symbol: str, tf: str, catalog: str) -> None:
        ohlcv = load_ohlcv(symbol, tf)
        ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < _lock_ms()].copy()
        self.ohlcv = ohlcv
        self.sc = make_bar_series(symbol, tf, ohlcv)
        self.sig = CATALOGS[catalog](ohlcv, tf)
        self.folds = build_outer_folds(self.sc.ts_ms, purge_bars=24, embargo_bars=24)
        self.oos_union = np.zeros(len(self.sc.ts_ms), dtype=bool)
        for f in self.folds:
            self.oos_union |= (self.sc.ts_ms >= f.oos_start_ms) & (self.sc.ts_ms < f.oos_end_ms)


def _run(ctx: Ctx, spec: dict, window: np.ndarray, tag: str, cfg: dict) -> dict[str, Any]:
    sig = ctx.sig[spec["idea"]]
    mask = (sig != 0) & window
    is_short = sig[np.flatnonzero(mask)] < 0
    tf = spec["timeframe"]
    return run_atr_bracket_arm(
        spec["symbol"],
        ctx.sc,
        mask,
        is_short,
        tag=tag,
        market=False,
        work=int(cfg["work_bars"][tf]),
        max_hold=int(cfg["max_hold_bars"][tf]),
        k_sl=float(cfg["k_sl"]),
        tp_ratio=float(cfg["tp_ratio"]),
        sl_cap=float(cfg["sl_cap"]),
        costs=COSTS,
    )


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    stitched = [r for r in rows if r.get("kind") == "stitched"]
    gates = cfg["gates_for_shadow_ready"]
    for r in stitched:
        ok, fails = gate_verdict(r, gates)
        r["gate_pass"] = ok and r.get("evidence_class") == "inner_screen_pass"
        r["gate_fails"] = fails if r.get("evidence_class") == "inner_screen_pass" else ["failed_screen_diagnostic"]
        if r.get("evidence_class") != "inner_screen_pass":
            r["gate_pass"] = False
    payload = {
        "generation_id": cfg["generation_id"],
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "stitched_outer_oos_pre_lockbox",
        "not_live": True,
        "n_rows": len(rows),
        "n_stitched": len(stitched),
        "n_gate_pass": sum(1 for r in stitched if r.get("gate_pass")),
        "gates": gates,
        "extra": extra,
        "stitched": stitched,
        "all": rows,
    }
    (OUT / "nested_settle_013_predictive_math_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# ML lab nested settle 013 (predictive math screen passers)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Stitched arms: {len(stitched)}. Subset gate pass: **{payload['n_gate_pass']}**.",
        "Window: 2022-01-01 to lockbox 2026-05-01. Maker 0.02%. EXEC-021. No retune.",
        "",
        "| Symbol | TF | Idea | class | n | /mo | PF | WR | Sharpe | HAC | ebr | folds+ | gate |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for r in stitched:
        md.append(
            "| {s} | {tf} | `{i}` | {c} | {n} | {tpm} | {pf} | {wr} | {sh} | {hac} | {ebr} | {p}/{ran} | {g} |".format(
                s=r.get("symbol"),
                tf=r.get("timeframe"),
                i=r.get("idea"),
                c=r.get("evidence_class"),
                n=r.get("n_trades"),
                tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                hac=_fmt(r.get("sharpe_hac_annualised")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                p=r.get("n_folds_positive"),
                ran=r.get("n_folds_ran"),
                g="PASS" if r.get("gate_pass") else ",".join(r.get("gate_fails") or []),
            )
        )
    (OUT / "nested_settle_013_predictive_math_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()
    print(f"priority={raise_current_process(high=True)} demoted={demote_competitors()}", flush=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    text = PREREG.read_text(encoding="utf-8")
    prereg_sha = _sha(PREREG)
    if "preregister_sha256_at_run:" not in text:
        PREREG.write_text(text.rstrip() + f"\n\npreregister_sha256_at_run: {prereg_sha}\n", encoding="utf-8")
        prereg_sha = _sha(PREREG)
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    DB_DIR.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "settle.sqlite")
    extra = {"preregister_sha256": prereg_sha, "fold_ranges": list(OUTER_FOLD_RANGES)}
    if args.report_only:
        write_report(con, cfg, stamp, extra)
        return 0

    survivors = list(cfg["survivors"])
    append_ledger(f"ML_LAB_NESTED_SETTLE_013 start {stamp} arms={len(survivors)}", tier=0)
    print(f"preregister_sha256={prereg_sha} survivors={len(survivors)}", flush=True)
    cache: dict[tuple[str, str, str], Ctx] = {}
    for spec in survivors:
        key = (spec["symbol"], spec["timeframe"], spec["catalog"])
        print(f"=== context {key} idea={spec['idea']} ===", flush=True)
        ctx = cache.get(key)
        if ctx is None:
            ctx = Ctx(spec["symbol"], spec["timeframe"], spec["catalog"])
            cache[key] = ctx
        print(f"  folds={len(ctx.folds)} oos_bars={int(ctx.oos_union.sum())}", flush=True)
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
                f"  fold{f.fold_index} -> {payload.get('status')} n={payload.get('n_trades')} "
                f"PF={_fmt(payload.get('profit_factor'))} tpm={_fmt(payload.get('trades_per_month'))}",
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
                {**spec, "kind": "stitched", "n_folds_ran": ran, "n_folds_positive": pos, "arm_id": aid}
            )
            save_arm(con, aid, spec, payload)
            ok, fails = gate_verdict(payload, cfg["gates_for_shadow_ready"])
            if spec.get("evidence_class") != "inner_screen_pass":
                ok, fails = False, ["failed_screen_diagnostic"]
            print(
                f"  STITCHED -> {payload.get('status')} n={payload.get('n_trades')} "
                f"tpm={_fmt(payload.get('trades_per_month'))} PF={_fmt(payload.get('profit_factor'))} "
                f"sharpe={_fmt(payload.get('sharpe_annualised'))} ebr={_fmt(payload.get('entry_bar_exit_rate'))} "
                f"folds+={pos}/{ran} gate={'PASS' if ok else ','.join(fails)}",
                flush=True,
            )
    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"ML_LAB_NESTED_SETTLE_013 done stitched={payload['n_stitched']} pass={payload['n_gate_pass']}",
        tier=0,
    )
    print(f"WROTE {OUT / 'nested_settle_013_predictive_math_latest.md'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
