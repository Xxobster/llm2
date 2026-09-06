"""Answer A pivot trio on tradesim 1.1.0 EXEC-021 + frozen contaminated retunes.

Research trio from exec_improve_002 (2026-08-12):
  BTC_ctrl_ret_w4, ETH_level_q50_w4, SOL_level_atr_clip_w5

Those prints used the older cost/fill path. This script re-scores the exact
trio on maker 0.02% + 1-minute fill clock, then a tiny frozen retune list.
Evidence class: CONTAMINATED_OOS_VIEWED. Inner = before 2022-01-01.
Nested = 2022-01-01 .. lockbox. Not Shadow-Ready. Not a deploy.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

from tradesim.ensure_source import prefer_botsgeneral_tradesim  # noqa: E402

prefer_botsgeneral_tradesim()

from llm2.confluence.sim_arms import arm_done, jsonable, load_arms, open_checkpoint, save_arm  # noqa: E402
from llm2.confluence.sim_arms import run_limit_arm  # noqa: E402
from llm2.gates.evidence import research_maker_first_costs  # noqa: E402
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START  # noqa: E402
from llm2.pivot.strategy.score_oos import (  # noqa: E402
    gate_mask,
    limit_price_side,
    score_symbol_oos,
)
from llm2.registry.ledger import append_ledger  # noqa: E402
from scripts.run_edge_lab_hunt_001 import _fmt, _passes  # noqa: E402
from scripts.run_pivot_exec_improve_002 import _atr_clip_level, _pull_level  # noqa: E402

TF, H, TP, SL = "15m", 4, 0.01, 0.01
PACK = "level_vsa"
MAX_ROWS = 120_000
INNER_END = "2022-01-01"
PREREG = _ROOT / "configs" / "preregister" / "pivot_answer_a_exec021.yaml"
OUT = ARTIFACTS / "reports" / "pivot_forecast"
DB_DIR = ARTIFACTS / "sqlite" / "pivot_answer_a_exec021"
COSTS = research_maker_first_costs()
GATES = {
    "min_trades": 80,
    "min_trades_per_month": 2.0,
    "max_trades_per_month": 90.0,
    "min_profit_factor": 1.20,
    "max_entry_bar_exit_rate": 0.25,
    "min_sharpe_annualised": 0.50,
}


def _ms(stamp: str) -> int:
    return int(pd.Timestamp(stamp, tz="UTC").value // 1_000_000)


def _window(sc, name: str) -> np.ndarray:
    inner = _ms(INNER_END)
    lock = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ts = np.asarray(sc.ts_ms, dtype=np.int64)
    if name == "inner":
        return ts < inner
    return (ts >= inner) & (ts < lock)


def _side_lim(sc, mask: np.ndarray, level_override=None):
    if level_override is not None:
        old = sc.level_ret
        sc.level_ret = level_override
        _, is_s, lim = limit_price_side(sc, mask)
        sc.level_ret = old
        return is_s, lim
    _, is_s, lim = limit_price_side(sc, mask)
    return is_s, lim


def _run(symbol: str, sc, mask, *, tag: str, work: int, level_override=None) -> dict:
    n = int(mask.sum())
    if n < 15:
        return {"tag": tag, "status": "TOO_FEW_GATED", "n_intent": n, "n_trades": 0}
    is_s, lim = _side_lim(sc, mask, level_override)
    return run_limit_arm(
        symbol,
        sc,
        mask,
        is_s,
        lim,
        tag=tag,
        work=work,
        max_hold=H + 2,
        tp=TP,
        sl=SL,
        costs=COSTS,
    )


def _attach_symbol(sc, symbol: str):
    if not hasattr(sc, "symbol"):
        sc.symbol = symbol
    if not hasattr(sc, "timeframe"):
        sc.timeframe = TF
    return sc


def main() -> int:
    print(f"priority={raise_current_process(high=True)} demoted={demote_competitors()}", flush=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    DB_DIR.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    con = open_checkpoint(DB_DIR / "hunt.sqlite")
    append_ledger(f"PIVOT_ANSWER_A start {stamp}", tier=0)

    cache: dict[tuple[str, str], object] = {}

    def scored(symbol: str, level_mode: str):
        key = (symbol, level_mode)
        if key not in cache:
            print(f"SCORE {symbol} level={level_mode}", flush=True)
            sc = score_symbol_oos(
                symbol,
                timeframe=TF,
                horizon_bars=H,
                feature_pack=PACK,
                max_rows=MAX_ROWS,
                level_mode=level_mode,
                atr_min=2.0,
            )
            cache[key] = _attach_symbol(sc, symbol)
        return cache[key]

    specs = list(cfg["arms"])
    extra = {"stamp": stamp, "costs": "research_maker_first", "engine": "tradesim_limit_entry"}
    for spec in specs:
        for window in ("inner", "nested"):
            aid = f"{spec['id']}|{window}"
            if arm_done(con, aid):
                print(f"  skip {aid}", flush=True)
                continue
            print(f"  arm {aid}", flush=True)
            sc = scored(spec["symbol"], spec["level_mode"])
            wmask = _window(sc, window)
            if spec.get("gate") == "p80_inner":
                inner = _window(sc, "inner")
                base = np.isfinite(sc.p_any) & inner
                thr = float(np.nanpercentile(sc.p_any[base], 80)) if int(base.sum()) >= 50 else np.nan
                g = np.isfinite(sc.p_any) & (sc.p_any >= thr)
            elif spec.get("gate") == "pi_star":
                g = gate_mask(sc, mode="pi_star", tp=TP, sl=SL, pi_star=float(spec["pi_star"]))
            else:
                g = gate_mask(sc, mode="p75", tp=TP, sl=SL)
            mask = g & wmask
            override = None
            if spec.get("clip"):
                lo, hi = spec["clip"]
                override = _atr_clip_level(sc, lo=float(lo), hi=float(hi))
            if spec.get("pull"):
                override = _pull_level(sc, float(spec["pull"]))
            try:
                sim = _run(
                    spec["symbol"],
                    sc,
                    mask,
                    tag=aid,
                    work=int(spec["work"]),
                    level_override=override,
                )
            except Exception as exc:  # noqa: BLE001
                sim = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0, "tag": aid}
            row = {
                **spec,
                **sim,
                "arm_id": aid,
                "window": window,
                "idea": spec["id"],
                "timeframe": TF,
            }
            row["screen_pass"] = bool(window == "inner" and row.get("status") == "RAN" and _passes(row, GATES))
            spec_row = {**spec, "timeframe": TF, "event": spec["id"]}
            save_arm(con, aid, spec_row, row)
            print(
                f"    {aid} {sim.get('status')} n={sim.get('n_trades')} "
                f"PF={_fmt(sim.get('profit_factor'))} ebr={_fmt(sim.get('entry_bar_exit_rate'))}",
                flush=True,
            )

    rows = load_arms(con)
    payload = {
        "generation_id": cfg["generation_id"],
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "CONTAMINATED_OOS_VIEWED",
        "extra": extra,
        "rows": rows,
    }
    (OUT / "answer_a_exec021_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    md = [
        "# Answer A pivot trio — EXEC-021 maker retest + frozen retunes",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        "**Evidence class:** `CONTAMINATED_OOS_VIEWED`. Not Shadow-Ready. Not a deploy.",
        "Maker 0.02% resting legs. 1-minute fill clock. Lockbox excluded.",
        "",
        "| Arm | window | n | PF | Sharpe | ebr | fill% |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        md.append(
            f"| `{r.get('id') or r.get('idea')}` | {r.get('window')} | {r.get('n_trades')} | "
            f"{_fmt(r.get('profit_factor'))} | {_fmt(r.get('sharpe_annualised'))} | "
            f"{_fmt(r.get('entry_bar_exit_rate'))} | {_fmt(r.get('fill_pct'))} |"
        )
    (OUT / "answer_a_exec021_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("WROTE answer_a_exec021_latest.md", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
