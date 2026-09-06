"""ML lab hunt 009 — invented causal formulas (answer A + new math).

RESEARCH_ONLY. Screen strictly before 2022-01-01. Never deploys.
Maker 0.02% on resting legs. 1-minute fill clock (EXEC-021).
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
from llm2.ml_lab.idea_catalog import HORIZON_BARS, event_metrics  # noqa: E402
from llm2.ml_lab.idea_catalog_f import (  # noqa: E402
    IDEA_IDS_F,
    build_features_for_guard,
    signals_f,
)
from llm2.ml_lab.kref import forward_return  # noqa: E402
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402
from scripts.run_edge_lab_hunt_001 import (  # noqa: E402
    MIN_CONTEXT_BARS,
    _fmt,
    _passes,
    _recovery_factor,
    _screen_end_ms,
)

PREREG = _ROOT / "configs" / "preregister" / "ml_lab_hunt_009_formulas.yaml"
OUT = ARTIFACTS / "reports" / "ml_lab"
DB_DIR = ARTIFACTS / "sqlite" / "ml_lab_hunt_009_formulas"
COSTS = research_maker_first_costs()


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arm_id(symbol: str, tf: str, idea: str) -> str:
    return f"{symbol}|{tf}|{idea}"


def _other_close(symbol: str, tf: str, n: int, index) -> np.ndarray | None:
    other = "ETHUSDT" if symbol == "BTCUSDT" else "BTCUSDT"
    try:
        raw = load_ohlcv(other, tf)
        raw = raw.loc[index_to_ms(raw.index) < _screen_end_ms()]
        aligned = raw["close"].reindex(index).ffill()
        out = aligned.to_numpy(dtype=float)
        if out.size != n:
            return None
        return out
    except Exception:  # noqa: BLE001
        return None


def _leak() -> dict[str, str]:
    from leakage.ensure_source import prefer_botsgeneral_leakage
    from leakage import require_clean_audit, run_leakage_audit

    prefer_botsgeneral_leakage()
    ohlcv = load_ohlcv("ETHUSDT", "1h").iloc[-4000:].copy()
    require_clean_audit(
        run_leakage_audit(
            ohlcv=ohlcv,
            build_features=build_features_for_guard,
            interval="1h",
            symbol="ETHUSDT",
            timeframe="1h",
        )
    )
    return {"symbol": "ETHUSDT", "timeframe": "1h", "status": "PASS"}


def _skill_pass(row: dict[str, Any], gates: dict[str, Any]) -> bool:
    try:
        n = int(row.get("n_skill") or 0)
        da = float(row.get("directional_acc"))
        mu = float(row.get("mean_signed"))
    except (TypeError, ValueError):
        return False
    return (
        n >= int(gates["min_skill_n"])
        and np.isfinite(da)
        and da >= float(gates["min_directional_acc"])
        and np.isfinite(mu)
        and mu >= float(gates["min_mean_signed"])
    )


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    gates = cfg["screen_gates"]
    sim_tfs = set(cfg["universe"]["tradesim_timeframes"])
    for r in rows:
        r["skill_pass"] = _skill_pass(r, gates)
        r["trade_pass"] = _passes(r, gates) if r.get("status") == "RAN" else False
        r["screen_pass"] = bool(r["skill_pass"] and r["trade_pass"] and r.get("timeframe") in sim_tfs)
        r["recovery_factor"] = _recovery_factor(r)

    def _ms(r: dict[str, Any]) -> float:
        try:
            x = float(r.get("mean_signed"))
            return x if np.isfinite(x) else -9.0
        except (TypeError, ValueError):
            return -9.0

    rows.sort(key=lambda r: -_ms(r))
    n_skill = sum(1 for r in rows if r.get("skill_pass"))
    n_pass = sum(1 for r in rows if r.get("screen_pass"))
    payload = {
        "generation_id": cfg["generation_id"],
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "n_rows": len(rows),
        "n_skill_pass": n_skill,
        "n_screen_pass": n_pass,
        "extra": extra,
        "rows": rows,
    }
    (OUT / "hunt_009_formulas_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# ML lab hunt 009 (invented causal formulas)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Rows: {len(rows)}. Skill pass: **{n_skill}**. Screen pass: **{n_pass}**.",
        "Maker 0.02% resting legs. EXEC-021 1-minute fill clock. Inner screen before 2022-01-01.",
        "",
        "| Symbol | TF | Idea | n | DA | signed | PF | ebr | skill | screen |",
        "|---|---|---|---:|---:|---:|---:|---:|---|---|",
    ]
    for r in rows[:40]:
        md.append(
            "| {s} | {tf} | `{i}` | {n} | {da} | {mu} | {pf} | {ebr} | {sk} | {v} |".format(
                s=r.get("symbol"),
                tf=r.get("timeframe"),
                i=r.get("idea"),
                n=r.get("n_skill") if r.get("status") == "EVENT" else r.get("n_trades"),
                da=_fmt(r.get("directional_acc")),
                mu=_fmt(r.get("mean_signed")),
                pf=_fmt(r.get("profit_factor")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                sk="Y" if r.get("skill_pass") else "",
                v="PASS" if r.get("screen_pass") else "fail",
            )
        )
    (OUT / "hunt_009_formulas_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--skip-leakage", action="store_true")
    ap.add_argument("--skip-tradesim", action="store_true")
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
    con = open_checkpoint(DB_DIR / "hunt.sqlite")
    extra: dict[str, Any] = {"preregister_sha256": prereg_sha, "costs": "research_maker_first"}
    if args.report_only:
        write_report(con, cfg, stamp, extra)
        return 0
    if not args.skip_leakage:
        extra["leakage"] = _leak()
        print(f"leakage {extra['leakage']}", flush=True)

    plan = [
        {"symbol": s, "timeframe": tf, "idea": idea}
        for tf in cfg["universe"]["event_study_timeframes"]
        for s in cfg["universe"]["symbols"]
        for idea in IDEA_IDS_F
    ]
    append_ledger(f"ML_LAB_HUNT_009 start {stamp} arms={len(plan)}", tier=0)
    cost_floor = float(cfg["cost_floor"])
    ctx_key = None
    sigs = None
    fwd = None
    ohlcv = None
    for spec in plan:
        aid = _arm_id(spec["symbol"], spec["timeframe"], spec["idea"])
        if arm_done(con, aid):
            continue
        key = (spec["symbol"], spec["timeframe"])
        if ctx_key != key:
            print(f"=== event study {key} ===", flush=True)
            try:
                raw = load_ohlcv(spec["symbol"], spec["timeframe"])
                ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
            except Exception as exc:  # noqa: BLE001
                extra.setdefault("load_errors", []).append(f"{key}: {exc}"[:200])
                print(f"  LOAD_FAIL {key} {exc}", flush=True)
                sigs = None
                fwd = None
                ohlcv = None
                ctx_key = key
                continue
            if len(ohlcv) < MIN_CONTEXT_BARS:
                extra.setdefault("load_errors", []).append(f"{key}: bars={len(ohlcv)}")
                sigs = None
                fwd = None
                ctx_key = key
                continue
            other = _other_close(spec["symbol"], spec["timeframe"], len(ohlcv), ohlcv.index)
            sigs = signals_f(ohlcv, spec["timeframe"], other_close=other)
            fwd = forward_return(ohlcv["close"].to_numpy(dtype=float), int(HORIZON_BARS[spec["timeframe"]]))
            ctx_key = key
        if sigs is None or fwd is None or ohlcv is None:
            save_arm(con, aid, spec, {"status": "NO_DATA", "n_trades": 0, **spec})
            continue
        skill = event_metrics(sigs[spec["idea"]], fwd, cost_floor=cost_floor)
        save_arm(con, aid, spec, {"status": "EVENT", "n_trades": 0, **spec, **skill})
        print(
            f"  {aid} n={skill['n_skill']} DA={_fmt(skill['directional_acc'])} "
            f"signed={_fmt(skill['mean_signed'])}",
            flush=True,
        )
    write_report(con, cfg, stamp, extra)
    if args.skip_tradesim:
        return 0

    gates = cfg["screen_gates"]
    sim_tfs = set(cfg["universe"]["tradesim_timeframes"])
    cand = [r for r in load_arms(con) if _skill_pass(r, gates) and r.get("timeframe") in sim_tfs]
    cand.sort(key=lambda r: (-float(r.get("mean_signed") or 0), -int(r.get("n_skill") or 0)))
    picks = cand[: int(cfg["max_tradesim_arms"])]
    extra["tradesim_picks"] = [_arm_id(p["symbol"], p["timeframe"], p["idea"]) for p in picks]
    print(f"=== tradesim {len(picks)} maker-first EXEC-021 ===", flush=True)
    for p in picks:
        symbol, tf, idea = p["symbol"], p["timeframe"], p["idea"]
        aid = _arm_id(symbol, tf, idea)
        if p.get("status") == "RAN":
            print(f"  skip {aid} already RAN", flush=True)
            continue
        print(f"  sim {aid}", flush=True)
        raw = load_ohlcv(symbol, tf)
        ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
        other = _other_close(symbol, tf, len(ohlcv), ohlcv.index)
        sig = signals_f(ohlcv, tf, other_close=other)[idea]
        sc = make_bar_series(symbol, tf, ohlcv)
        mask = sig != 0
        is_short = sig[np.flatnonzero(mask)] < 0
        try:
            sim = run_atr_bracket_arm(
                symbol,
                sc,
                mask,
                is_short,
                tag=aid,
                market=False,
                work=int(cfg["work_bars"][tf]),
                max_hold=int(cfg["max_hold_bars"][tf]),
                k_sl=float(cfg["k_sl"]),
                tp_ratio=float(cfg["tp_ratio"]),
                sl_cap=float(cfg["sl_cap"]),
                costs=COSTS,
            )
        except Exception as exc:  # noqa: BLE001
            sim = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
        save_arm(con, aid, p, {**p, **sim, "arm_id": aid})
        print(
            f"  {aid} -> {sim.get('status')} n={sim.get('n_trades')} "
            f"PF={_fmt(sim.get('profit_factor'))} ebr={_fmt(sim.get('entry_bar_exit_rate'))}",
            flush=True,
        )
        write_report(con, cfg, stamp, extra)

    payload = write_report(con, cfg, stamp, extra)
    print(
        f"WROTE hunt_009_formulas_latest.md skill={payload['n_skill_pass']} "
        f"screen={payload['n_screen_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
