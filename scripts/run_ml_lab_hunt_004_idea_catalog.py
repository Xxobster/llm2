"""ML lab hunt 004 — 30 named ideas, event study first, tradesim cap 12.

RESEARCH_ONLY. Screen strictly before 2022-01-01. Never deploys.
Does not retune hunts 001–003, bounce_upper, or WaveTheory.
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
from llm2.edge_lab.sim_atr import run_atr_bracket_arm, run_offset_bracket_arm  # noqa: E402
from llm2.ml_lab.idea_catalog import (  # noqa: E402
    CHANNEL_IDEAS,
    HORIZON_BARS,
    IDEA_IDS,
    MIX,
    POWER,
    SURF,
    build_features_for_guard,
    channel_levels,
    channel_offsets,
    event_metrics,
    signals_from_ohlcv,
)
from llm2.ml_lab.kref import forward_return  # noqa: E402
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
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

PREREG = _ROOT / "configs" / "preregister" / "ml_lab_hunt_004_idea_catalog.yaml"
OUT = ARTIFACTS / "reports" / "ml_lab"
DB_DIR = ARTIFACTS / "sqlite" / "ml_lab_hunt_004_idea_catalog"

_FAMILY = {i: "power" for i in POWER}
_FAMILY.update({i: "surf" for i in SURF})
_FAMILY.update({i: "mix" for i in MIX})


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arm_id(symbol: str, tf: str, idea: str) -> str:
    return f"{symbol}|{tf}|{idea}"


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


def _family(idea: str) -> str:
    return _FAMILY.get(idea, "other")


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    gates = cfg["screen_gates"]
    sim_tfs = set(cfg["universe"]["tradesim_timeframes"])
    for r in rows:
        r["family"] = _family(str(r.get("idea")))
        r["skill_pass"] = _skill_pass(r, gates)
        r["trade_pass"] = _passes(r, gates) if r.get("status") == "RAN" else False
        r["screen_pass"] = bool(
            r["skill_pass"] and r["trade_pass"] and r.get("timeframe") in sim_tfs
        )
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
        "evidence_class": "inner_screen_pre_2022_event_study",
        "not_live": True,
        "failure_is_success": True,
        "n_rows": len(rows),
        "n_skill_pass": n_skill,
        "n_screen_pass": n_pass,
        "gates": gates,
        "extra": extra,
        "rows": rows,
    }
    (OUT / "hunt_004_idea_catalog_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# ML lab hunt 004 (30 named ideas)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Rows: {len(rows)}. Event-study skill pass: **{n_skill}**. Tradesim screen pass: **{n_pass}**.",
        "Screen: bars before 2022-01-01. Adaptive channel offsets are frozen at the decision bar.",
        "",
        "| Symbol | TF | Family | Idea | n | DA | signed | net | PF | ebr | skill | screen |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    show = rows[:40]
    for r in show:
        md.append(
            "| {sym} | {tf} | {fam} | `{idea}` | {n} | {da} | {mu} | {net} | {pf} | {ebr} | {sk} | {v} |".format(
                sym=r.get("symbol"),
                tf=r.get("timeframe"),
                fam=r.get("family"),
                idea=r.get("idea"),
                n=r.get("n_skill"),
                da=_fmt(r.get("directional_acc")),
                mu=_fmt(r.get("mean_signed")),
                net=_fmt(r.get("mean_signed_net")),
                pf=_fmt(r.get("profit_factor")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                sk="Y" if r.get("skill_pass") else "",
                v="PASS" if r.get("screen_pass") else "fail",
            )
        )
    (OUT / "hunt_004_idea_catalog_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


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


def _pick_tradesim(rows: list[dict[str, Any]], cfg: dict) -> list[dict[str, Any]]:
    gates = cfg["screen_gates"]
    sim_tfs = set(cfg["universe"]["tradesim_timeframes"])
    cap = int(cfg["max_tradesim_arms"])
    cand = [r for r in rows if _skill_pass(r, gates) and r.get("timeframe") in sim_tfs]
    cand.sort(key=lambda r: (-float(r.get("mean_signed") or 0), -int(r.get("n_skill") or 0)))
    return cand[:cap]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--skip-leakage", action="store_true")
    ap.add_argument("--skip-tradesim", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
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
    extra: dict[str, Any] = {"preregister_sha256": prereg_sha, "selection_window": f"< {SCREEN_END}"}
    cost_floor = float(cfg["cost_floor"])

    if args.report_only:
        payload = write_report(con, cfg, stamp, extra)
        print(json.dumps({k: payload[k] for k in ("n_rows", "n_skill_pass", "n_screen_pass")}, indent=2))
        return 0

    if not args.skip_leakage:
        leak = _leak()
        print(f"leakage {leak}", flush=True)
        extra["leakage"] = leak

    symbols = list(cfg["universe"]["symbols"])
    tfs = list(cfg["universe"]["event_study_timeframes"])
    plan = [{"symbol": s, "timeframe": tf, "idea": idea} for tf in tfs for s in symbols for idea in IDEA_IDS]
    if args.limit:
        plan = plan[: int(args.limit)]
    append_ledger(f"ML_LAB_HUNT_004 start {stamp} arms={len(plan)}", tier=0)
    print(f"preregister_sha256={prereg_sha} event_rows={len(plan)}", flush=True)

    ctx_key: tuple[str, str] | None = None
    sigs: dict[str, np.ndarray] | None = None
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
                ohlcv = None
                sigs = None
                fwd = None
                ctx_key = key
                extra.setdefault("load_errors", []).append(f"{key}: {exc}"[:200])
                print(f"  LOAD_FAIL {key} {exc}", flush=True)
                continue
            if ohlcv is None or len(ohlcv) < MIN_CONTEXT_BARS:
                extra.setdefault("load_errors", []).append(f"{key}: bars={0 if ohlcv is None else len(ohlcv)}")
                sigs = None
                fwd = None
                ctx_key = key
                continue
            other = _other_close(spec["symbol"], spec["timeframe"], len(ohlcv), ohlcv.index)
            sigs = signals_from_ohlcv(ohlcv, spec["timeframe"], other_close=other)
            h = int(HORIZON_BARS[spec["timeframe"]])
            fwd = forward_return(ohlcv["close"].to_numpy(dtype=float), h)
            ctx_key = key
        if sigs is None or fwd is None or ohlcv is None:
            save_arm(con, aid, spec, {"status": "NO_DATA", "n_trades": 0, **spec})
            continue
        skill = event_metrics(sigs[spec["idea"]], fwd, cost_floor=cost_floor)
        payload = {
            "status": "EVENT",
            "n_trades": 0,
            "idea": spec["idea"],
            "family": _family(spec["idea"]),
            **spec,
            **skill,
        }
        save_arm(con, aid, spec, payload)
        print(
            f"  {aid} n={skill['n_skill']} DA={_fmt(skill['directional_acc'])} "
            f"signed={_fmt(skill['mean_signed'])}",
            flush=True,
        )

    write_report(con, cfg, stamp, extra)
    if args.skip_tradesim:
        payload = write_report(con, cfg, stamp, extra)
        print(f"event-study only rows={payload['n_rows']} skill_pass={payload['n_skill_pass']}", flush=True)
        return 0

    rows = load_arms(con)
    picks = _pick_tradesim(rows, cfg)
    extra["tradesim_picks"] = [p.get("arm_id") or _arm_id(p["symbol"], p["timeframe"], p["idea"]) for p in picks]
    print(f"=== tradesim {len(picks)} / cap {cfg['max_tradesim_arms']} ===", flush=True)

    k_sl = float(cfg["k_sl"])
    ratio = float(cfg["tp_ratio"])
    sl_cap = float(cfg["sl_cap"])
    work_map = cfg["work_bars"]
    hold_map = cfg["max_hold_bars"]

    for p in picks:
        symbol, tf, idea = p["symbol"], p["timeframe"], p["idea"]
        aid = _arm_id(symbol, tf, idea)
        print(f"  SIM {aid}", flush=True)
        raw = load_ohlcv(symbol, tf)
        ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
        other = _other_close(symbol, tf, len(ohlcv), ohlcv.index)
        sigs = signals_from_ohlcv(ohlcv, tf, other_close=other)
        sc = make_bar_series(symbol, tf, ohlcv)
        sig = sigs[idea]
        mask = sig != 0
        gated = np.flatnonzero(mask)
        is_short = sig[gated] < 0
        try:
            if idea in CHANNEL_IDEAS:
                lv = channel_levels(ohlcv, idea, timeframe=tf)
                if lv is None:
                    raise RuntimeError("no channel levels")
                lo, hi = lv
                sl_arr, tp_arr = channel_offsets(sc.close[gated], lo[gated], hi[gated], is_short)
                sim = run_offset_bracket_arm(
                    symbol,
                    sc,
                    mask,
                    is_short,
                    sl_arr,
                    tp_arr,
                    tag=aid,
                    market=False,
                    work=int(work_map[tf]),
                    max_hold=int(hold_map[tf]),
                    sl_cap=sl_cap,
                )
            else:
                sim = run_atr_bracket_arm(
                    symbol,
                    sc,
                    mask,
                    is_short,
                    tag=aid,
                    market=False,
                    work=int(work_map[tf]),
                    max_hold=int(hold_map[tf]),
                    k_sl=k_sl,
                    tp_ratio=ratio,
                    sl_cap=sl_cap,
                )
        except Exception as exc:  # noqa: BLE001
            sim = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
        merged = {**p, **sim, "arm_id": aid, "recovery_factor": _recovery_factor(sim)}
        save_arm(con, aid, p, merged)
        print(
            f"  {aid} -> {merged.get('status')} n={merged.get('n_trades')} PF={_fmt(merged.get('profit_factor'))}",
            flush=True,
        )
        write_report(con, cfg, stamp, extra)

    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"ML_LAB_HUNT_004 done rows={payload['n_rows']} skill={payload['n_skill_pass']} pass={payload['n_screen_pass']}",
        tier=0,
    )
    print(
        f"WROTE {OUT / 'hunt_004_idea_catalog_latest.md'} "
        f"skill_pass={payload['n_skill_pass']} screen_pass={payload['n_screen_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
