"""ML lab hunt 002 — 15-minute sign-reversal control (falsification).

RESEARCH_ONLY. Screen is strictly before 2022-01-01. Never deploys.
Expect statistical directional accuracy and post-cost profit-factor failure.
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
    run_limit_arm,
    run_market_arm,
    save_arm,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.gates.evidence import (  # noqa: E402
    research_costs_baseline,
    research_maker_first_costs,
)
from llm2.ml_lab.finverse_score import point_metrics  # noqa: E402
from llm2.ml_lab.kref import forward_return, kref_predict  # noqa: E402
from llm2.ml_lab.regime_audit import (  # noqa: E402
    fit_assign_regimes,
    regime_features,
    regime_skill_table,
)
from llm2.ml_lab.reversal import reversal_confidence, reversal_signal  # noqa: E402
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402
from scripts.run_edge_lab_hunt_001 import (  # noqa: E402
    MIN_CONTEXT_BARS,
    SCREEN_END,
    _fmt,
    _recovery_factor,
    _screen_end_ms,
)

PREREG = _ROOT / "configs" / "preregister" / "ml_lab_hunt_002_reversal_control.yaml"
OUT = ARTIFACTS / "reports" / "ml_lab"
DB_DIR = ARTIFACTS / "sqlite" / "ml_lab_hunt_002_reversal_control"


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arm_id(symbol: str, tf: str, cost_mode: str, conf_min: float) -> str:
    return f"{symbol}|{tf}|rev|{cost_mode}|c{conf_min:.2f}"


def _leak(symbol: str, tf: str) -> dict[str, str]:
    from leakage.ensure_source import prefer_botsgeneral_leakage
    from leakage import require_clean_audit, run_leakage_audit
    from llm2.ml_lab.reversal import build_features_for_guard

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
            for cost_mode in cfg["cost_modes"]:
                for conf_min in cfg["conf_min"]:
                    plan.append(
                        {
                            "symbol": symbol,
                            "timeframe": tf,
                            "cost_mode": str(cost_mode),
                            "conf_min": float(conf_min),
                        }
                    )
    return plan


def _skill_pass(skill: dict[str, Any], gates: dict[str, Any]) -> bool:
    try:
        n = int(skill.get("n_skill") or 0)
        da = float(skill.get("directional_acc"))
    except (TypeError, ValueError):
        return False
    return n >= int(gates["min_skill_n"]) and np.isfinite(da) and da >= float(gates["min_directional_acc"])


def _economic_pass(row: dict[str, Any], gates: dict[str, Any]) -> bool:
    if row.get("status") != "RAN":
        return False
    try:
        n = int(row.get("n_trades") or 0)
        pf = float(row.get("profit_factor"))
        sh = float(row.get("sharpe_annualised"))
    except (TypeError, ValueError):
        return False
    return (
        n >= int(gates["min_trades"])
        and np.isfinite(pf)
        and pf >= float(gates["min_profit_factor"])
        and np.isfinite(sh)
        and sh >= float(gates["min_sharpe_annualised"])
    )


def _regime_table(ohlcv, close: np.ndarray, cfg: dict) -> list[dict[str, Any]]:
    ra = cfg["regime_audit"]
    feat = regime_features(ohlcv, vol_win=int(ra["vol_win"]))
    n = int(close.size)
    train_end = max(int(ra["vol_win"]) + 50, int(n * float(ra["train_frac"])))
    train_end = min(train_end, n - 50)
    labels = fit_assign_regimes(feat, train_end=train_end, k=int(ra["k"]))
    nxt = forward_return(close, 1)
    return regime_skill_table(labels, reversal_signal(close), nxt, eval_start=train_end)


def _kref_feature_table(close: np.ndarray, conf: np.ndarray, cfg: dict) -> dict[str, Any]:
    kd = cfg["kref_feature_diagnostic"]
    pred = kref_predict(
        close,
        lookback=int(kd["lookback"]),
        archive=int(kd["archive"]),
        neighbors=int(kd["neighbors"]),
        horizon=int(kd["horizon"]),
        purge=int(kd["purge"]),
    )
    y = forward_return(close, int(kd["horizon"]))
    overall = point_metrics(pred, y)
    bins = [
        ("conf_lt_0.05", conf < 0.05),
        ("conf_0.05_0.10", (conf >= 0.05) & (conf < 0.10)),
        ("conf_ge_0.10", conf >= 0.10),
    ]
    out: dict[str, Any] = {"overall": overall}
    for name, mbin in bins:
        m = mbin & np.isfinite(pred) & np.isfinite(y) & np.isfinite(conf)
        p = np.where(m, pred, np.nan)
        out[name] = point_metrics(p, y)
    return out


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    gates = cfg["screen_gates"]
    for r in rows:
        skill_ok = _skill_pass(r, gates)
        trade_ok = _economic_pass(r, gates)
        r["skill_pass"] = skill_ok
        r["trade_pass"] = trade_ok
        r["screen_pass"] = bool(skill_ok and trade_ok)
        r["recovery_factor"] = _recovery_factor(r)
    rows.sort(key=lambda r: -(float(r.get("profit_factor") or 0) if r.get("status") == "RAN" else -1e9))
    n_pass = sum(1 for r in rows if r.get("screen_pass"))
    payload = {
        "generation_id": cfg["generation_id"],
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "inner_screen_pre_2022_falsification",
        "not_live": True,
        "failure_is_success": True,
        "n_rows": len(rows),
        "n_screen_pass": n_pass,
        "gates": gates,
        "extra": extra,
        "rows": rows,
    }
    (OUT / "hunt_002_reversal_control_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# ML lab hunt 002 (15-minute sign-reversal control)",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"Arms: {len(rows)}. Screen pass (skill and post-cost economic): **{n_pass}**.",
        "This family is a falsification: directional accuracy may pass; profit factor after Bybit costs is expected to fail.",
        "Screen window: bars strictly before 2022-01-01. One-bar hold; entry-bar exit rate is a diagnostic, not a gate.",
        "",
        "| Symbol | Cost | conf_min | n_skill | DA | n | PF | Sharpe | fees | ebr | t/m | fill | screen |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        md.append(
            "| {sym} | {cm} | {c} | {ns} | {da} | {n} | {pf} | {sh} | {fe} | {ebr} | {tm} | {fp} | {v} |".format(
                sym=r.get("symbol"),
                cm=r.get("cost_mode"),
                c=r.get("conf_min"),
                ns=r.get("n_skill"),
                da=_fmt(r.get("directional_acc")),
                n=r.get("n_trades"),
                pf=_fmt(r.get("profit_factor")),
                sh=_fmt(r.get("sharpe_annualised")),
                fe=_fmt(r.get("total_fees")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
                tm=_fmt(r.get("trades_per_month")),
                fp=_fmt(r.get("fill_pct")),
                v="PASS" if r.get("screen_pass") else "fail",
            )
        )
    (OUT / "hunt_002_reversal_control_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
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
    extra: dict[str, Any] = {
        "preregister_sha256": prereg_sha,
        "selection_window": f"< {SCREEN_END}",
        "regimes": {},
        "kref_feature": {},
    }

    if args.report_only:
        payload = write_report(con, cfg, stamp, extra)
        print(json.dumps({k: payload[k] for k in ("n_rows", "n_screen_pass")}, indent=2))
        return 0

    if not args.skip_leakage:
        leak = _leak("ETHUSDT", "15m")
        print(f"leakage {leak}", flush=True)
        extra["leakage"] = leak
        if leak.get("status") != "PASS":
            raise SystemExit(f"LEAKAGE_FAIL {leak}")

    plan = _plan(cfg)
    if args.limit:
        plan = plan[: int(args.limit)]
    append_ledger(f"ML_LAB_HUNT_002 start {stamp} arms={len(plan)}", tier=0)
    print(f"preregister_sha256={prereg_sha} arms={len(plan)}", flush=True)

    tp = float(cfg["tp"])
    sl = float(cfg["sl"])
    hold = int(cfg["max_hold_bars"])
    work = int(cfg["work_bars_maker"])
    roll = int(cfg["roll_bars"])

    ctx_key: tuple[str, str] | None = None
    sc = None
    close = None
    sig = None
    conf = None
    fwd = None
    ohlcv = None

    for spec in plan:
        aid = _arm_id(spec["symbol"], spec["timeframe"], spec["cost_mode"], spec["conf_min"])
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
            sig = reversal_signal(close)
            conf = reversal_confidence(close, roll=roll)
            fwd = forward_return(close, 1)
            extra["regimes"][f"{key[0]}|{key[1]}"] = _regime_table(ohlcv, close, cfg)
            if cfg.get("kref_feature_diagnostic", {}).get("enabled"):
                extra["kref_feature"][f"{key[0]}|{key[1]}"] = _kref_feature_table(close, conf, cfg)
            ctx_key = key
        assert sc is not None and close is not None and sig is not None
        assert conf is not None and fwd is not None and ohlcv is not None
        tau = float(spec["conf_min"])
        mask = (sig != 0) & np.isfinite(conf) & (conf >= tau) & np.isfinite(fwd)
        gated_idx = np.flatnonzero(mask)
        skill = point_metrics(sig[gated_idx], fwd[gated_idx]) if gated_idx.size else {
            "n_skill": 0,
            "spearman_ic": float("nan"),
            "directional_acc": float("nan"),
        }
        is_short = sig[gated_idx] < 0
        print(
            f"  {aid} intents={int(mask.sum())} skill_n={skill.get('n_skill')} "
            f"DA={_fmt(skill.get('directional_acc'))} — simulating",
            flush=True,
        )
        try:
            if spec["cost_mode"] == "taker":
                payload = run_market_arm(
                    spec["symbol"],
                    sc,
                    mask,
                    is_short,
                    tag=aid,
                    max_hold=hold,
                    tp=tp,
                    sl=sl,
                    costs=research_costs_baseline(),
                )
            elif spec["cost_mode"] == "maker":
                lim = sc.close[gated_idx]
                payload = run_limit_arm(
                    spec["symbol"],
                    sc,
                    mask,
                    is_short,
                    lim,
                    tag=aid,
                    work=work,
                    max_hold=hold,
                    tp=tp,
                    sl=sl,
                    costs=research_maker_first_costs(),
                )
            else:
                raise ValueError(spec["cost_mode"])
        except Exception as exc:  # noqa: BLE001
            payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}
        payload.update({**spec, **skill, "arm_id": aid, "recovery_factor": _recovery_factor(payload)})
        save_arm(con, aid, spec, payload)
        print(
            f"  {aid} -> {payload.get('status')} DA={_fmt(skill.get('directional_acc'))} "
            f"n={payload.get('n_trades')} PF={_fmt(payload.get('profit_factor'))}",
            flush=True,
        )
        write_report(con, cfg, stamp, extra)

    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"ML_LAB_HUNT_002 done rows={payload['n_rows']} pass={payload['n_screen_pass']}",
        tier=0,
    )
    print(
        f"WROTE {OUT / 'hunt_002_reversal_control_latest.md'} "
        f"rows={payload['n_rows']} screen_pass={payload['n_screen_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
