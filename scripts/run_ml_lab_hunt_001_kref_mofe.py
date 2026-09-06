"""ML lab hunt 001 — FinVerse point skill + tradesim of KReF / MoFE-lite.

RESEARCH_ONLY. Screen is strictly before 2022-01-01. Never deploys.
Does not retune the Ether 1-hour bounce_upper live pack or hunt-003 survivors.
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
from llm2.ml_lab.finverse_score import point_metrics  # noqa: E402
from llm2.ml_lab.kref import forward_return, kref_predict, log_returns  # noqa: E402
from llm2.ml_lab.mofe_lite import mofe_lite_predict  # noqa: E402
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

PREREG = _ROOT / "configs" / "preregister" / "ml_lab_hunt_001_kref_mofe.yaml"
OUT = ARTIFACTS / "reports" / "ml_lab"
DB_DIR = ARTIFACTS / "sqlite" / "ml_lab_hunt_001_kref_mofe"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arm_id(symbol: str, tf: str, model: str) -> str:
    return f"{symbol}|{tf}|{model}"


def _predict(model: str, close: np.ndarray, cfg: dict) -> np.ndarray:
    lb = int(cfg["lookback"])
    h = int(cfg["horizon_bars"])
    if model == "naive_last":
        return log_returns(close)
    if model == "kref":
        return kref_predict(
            close,
            lookback=lb,
            archive=int(cfg["archive"]),
            neighbors=int(cfg["neighbors"]),
            horizon=h,
            purge=int(cfg["purge_bars"]),
        )
    if model == "mofe_lite":
        return mofe_lite_predict(close, lookback=lb)
    raise ValueError(model)


def _leak(symbol: str, tf: str) -> dict[str, str]:
    from leakage.ensure_source import prefer_botsgeneral_leakage
    from leakage import require_clean_audit, run_leakage_audit
    from llm2.ml_lab.features import build_features_for_guard

    prefer_botsgeneral_leakage()
    ohlcv = load_ohlcv(symbol, tf)
    ohlcv = ohlcv.iloc[-4000:].copy()
    require_clean_audit(
        run_leakage_audit(
            ohlcv=ohlcv,
            build_features=build_features_for_guard,
            interval=tf,
            symbol=symbol,
            timeframe=tf,
        )
    )
    return {"symbol": symbol, "timeframe": tf, "status": "PASS"}


def _plan(cfg: dict) -> list[dict[str, Any]]:
    plan: list[dict[str, Any]] = []
    for tf in cfg["universe"]["timeframes"]:
        for symbol in cfg["universe"]["symbols"]:
            for model in cfg["models"]:
                plan.append({"symbol": symbol, "timeframe": tf, "model": model})
    return plan


def _skill_pass(skill: dict[str, Any], gates: dict[str, Any]) -> bool:
    try:
        n = int(skill.get("n_skill") or 0)
        ic = float(skill.get("spearman_ic"))
        da = float(skill.get("directional_acc"))
    except (TypeError, ValueError):
        return False
    return (
        n >= int(gates["min_skill_n"])
        and np.isfinite(ic)
        and ic >= float(gates["min_spearman_ic"])
        and np.isfinite(da)
        and da >= float(gates["min_directional_acc"])
    )


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    gates = cfg["screen_gates"]
    for r in rows:
        skill_ok = _skill_pass(r, gates)
        trade_ok = _passes(r, gates)
        r["skill_pass"] = skill_ok
        r["trade_pass"] = trade_ok
        r["screen_pass"] = bool(skill_ok and trade_ok)
    rows.sort(key=lambda r: -(float(r.get("profit_factor") or 0) if r.get("status") == "RAN" else -1e9))
    n_pass = sum(1 for r in rows if r.get("screen_pass"))
    payload = {
        "generation_id": cfg["generation_id"],
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "inner_screen_pre_2022",
        "not_live": True,
        "n_rows": len(rows),
        "n_screen_pass": n_pass,
        "gates": gates,
        "extra": extra,
        "rows": rows,
    }
    (OUT / "hunt_001_kref_mofe_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# ML lab hunt 001 (KReF / MoFE-lite / FinVerse protocol)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Arms: {len(rows)}. Screen pass (skill and trade): **{n_pass}**.",
        "Screen window: bars strictly before 2022-01-01. Ether bounce_upper not retuned.",
        "",
        "| Symbol | TF | Model | n_skill | IC | DA | n | PF | Sharpe | ebr | t/m | screen |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        md.append(
            "| {sym} | {tf} | `{m}` | {ns} | {ic} | {da} | {n} | {pf} | {sh} | {ebr} | {tm} | {v} |".format(
                sym=r.get("symbol"),
                tf=r.get("timeframe"),
                m=r.get("model"),
                ns=r.get("n_skill"),
                ic=_fmt(r.get("spearman_ic")),
                da=_fmt(r.get("directional_acc")),
                n=r.get("n_trades"),
                pf=_fmt(r.get("profit_factor")),
                sh=_fmt(r.get("sharpe_annualised")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                tm=_fmt(r.get("trades_per_month")),
                v="PASS" if r.get("screen_pass") else "fail",
            )
        )
    (OUT / "hunt_001_kref_mofe_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--skip-leakage", action="store_true")
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
    extra = {"preregister_sha256": prereg_sha, "selection_window": f"< {SCREEN_END}"}

    if args.report_only:
        payload = write_report(con, cfg, stamp, extra)
        print(json.dumps({k: payload[k] for k in ("n_rows", "n_screen_pass")}, indent=2))
        return 0

    if not args.skip_leakage:
        leak = _leak("ETHUSDT", "1h")
        print(f"leakage {leak}", flush=True)
        extra["leakage"] = leak
        if leak.get("status") != "PASS":
            raise SystemExit(f"LEAKAGE_FAIL {leak}")

    plan = _plan(cfg)
    if args.limit:
        plan = plan[: int(args.limit)]
    append_ledger(f"ML_LAB_HUNT_001 start {stamp} arms={len(plan)}", tier=0)
    print(f"preregister_sha256={prereg_sha} arms={len(plan)}", flush=True)

    h = int(cfg["horizon_bars"])
    tau = float(cfg["abs_pred_tau"])
    k_sl = float(cfg["k_sl"][0])
    ratio = float(cfg["tp_ratio"][0])
    work_map = cfg["work_bars"]
    hold_map = cfg["max_hold_bars"]

    ctx_key: tuple[str, str] | None = None
    sc = None
    close = None
    fwd = None
    ohlcv = None

    for spec in plan:
        aid = _arm_id(spec["symbol"], spec["timeframe"], spec["model"])
        if arm_done(con, aid):
            continue
        key = (spec["symbol"], spec["timeframe"])
        if ctx_key != key:
            print(f"=== context {key} ===", flush=True)
            raw = load_ohlcv(spec["symbol"], spec["timeframe"])
            ohlcv = raw.loc[index_to_ms(raw.index) < _screen_end_ms()].copy()
            if len(ohlcv) < MIN_CONTEXT_BARS:
                raise RuntimeError(f"{key}: only {len(ohlcv)} bars before {SCREEN_END}")
            sc = make_bar_series(spec["symbol"], spec["timeframe"], ohlcv)
            close = sc.close
            fwd = forward_return(close, h)
            ctx_key = key
        assert sc is not None and close is not None and fwd is not None and ohlcv is not None
        pred = _predict(spec["model"], close, cfg)
        skill = point_metrics(pred, fwd)
        mask = np.isfinite(pred) & (np.abs(pred) >= tau)
        is_short = pred[np.flatnonzero(mask)] < 0
        tf = spec["timeframe"]
        try:
            payload = run_atr_bracket_arm(
                spec["symbol"],
                sc,
                mask,
                is_short,
                tag=aid,
                market=False,
                work=int(work_map[tf]),
                max_hold=int(hold_map[tf]),
                k_sl=k_sl,
                tp_ratio=ratio,
                sl_cap=float(cfg["sl_cap"]),
            )
        except Exception as exc:  # noqa: BLE001
            payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
        payload.update({**spec, **skill, "arm_id": aid, "recovery_factor": _recovery_factor(payload)})
        save_arm(con, aid, spec, payload)
        print(
            f"  {aid} -> {payload.get('status')} IC={_fmt(skill.get('spearman_ic'))} "
            f"DA={_fmt(skill.get('directional_acc'))} n={payload.get('n_trades')} "
            f"PF={_fmt(payload.get('profit_factor'))}",
            flush=True,
        )
        write_report(con, cfg, stamp, extra)

    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"ML_LAB_HUNT_001 done rows={payload['n_rows']} pass={payload['n_screen_pass']}",
        tier=0,
    )
    print(
        f"WROTE {OUT / 'hunt_001_kref_mofe_latest.md'} "
        f"rows={payload['n_rows']} screen_pass={payload['n_screen_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
