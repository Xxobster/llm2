"""V2.1 remainder on frozen Solana 1-hour EMA-stack (nested-settle 004).

RESEARCH_ONLY. No retune of Exponential Moving Average spans, Kaufman
efficiency ratio, stop, or target. Never deploys.

Always runs: Deflated Sharpe Ratio (trial count = hunt-004 event-study rows),
10,000-sample block bootstrap, moderate stress (2× slippage), mark-to-market
drawdown, peak margin, liquidation check.
"""

from __future__ import annotations

import argparse
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

from llm2.confluence.sim_arms import jsonable, load_arms, open_checkpoint  # noqa: E402
from llm2.edge_lab.sim_atr import run_atr_bracket_arm  # noqa: E402
from llm2.gates.evidence import research_costs_baseline, research_costs_moderate_stress  # noqa: E402
from llm2.ml_lab.v21_battery import (  # noqa: E402
    HUNT004_EVENT_ROWS,
    evaluate_nested_v21,
)
from llm2.ops.process_priority import demote_competitors, raise_current_process  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from scripts.run_ml_lab_nested_settle_004_ema_stack import Ctx, PREREG, _fmt  # noqa: E402

OUT = ARTIFACTS / "reports" / "ml_lab"
SETTLE_DB = ARTIFACTS / "sqlite" / "ml_lab_nested_settle_004_ema_stack" / "settle.sqlite"
SPEC = {"symbol": "SOLUSDT", "timeframe": "1h", "idea": "power_ema_stack_long"}


def _slim(sim: dict[str, Any]) -> dict[str, Any]:
    skip = {"daily_returns", "trade_pnls"}
    return {k: v for k, v in sim.items() if k not in skip}


def _run_book(ctx: Ctx, cfg: dict, *, tag: str, costs, market: bool = False) -> dict[str, Any]:
    sig = ctx.sig[SPEC["idea"]]
    mask = (sig != 0) & ctx.oos_union
    gated = np.flatnonzero(mask)
    is_short = sig[gated] < 0
    tf = SPEC["timeframe"]
    return run_atr_bracket_arm(
        SPEC["symbol"],
        ctx.sc,
        mask,
        is_short,
        tag=tag,
        market=bool(market),
        work=int(cfg["work_bars"][tf]),
        max_hold=int(cfg["max_hold_bars"][tf]),
        k_sl=float(cfg["k_sl"]),
        tp_ratio=float(cfg["tp_ratio"]),
        sl_cap=float(cfg["sl_cap"]),
        costs=costs,
    )


def write_report(payload: dict[str, Any]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "v21_sol_ema_stack_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )
    g = payload["gates"]
    md = [
        "# V2.1 remainder — Solana 1-hour EMA stack",
        "",
        f"**Max readiness:** `{payload['readiness_max']}`. Stamp `{payload['stamp']}`.",
        "Frozen name only. No Exponential Moving Average / efficiency-ratio / stop search.",
        f"Deflated Sharpe Ratio trial count = **{HUNT004_EVENT_ROWS}** (hunt-004 event-study rows).",
        "Probability of Backtest Overfitting: unavailable (single frozen arm).",
        "",
        f"**Overall V2.1 blocking:** **{g.get('overall')}**.",
        "",
        "| Gate | Status | Value |",
        "|---|---|---|",
    ]
    keys = [
        ("outer_folds", "outer_folds_value"),
        ("trades_per_fold", "trades_per_fold_min"),
        ("pooled_trades", "pooled_trades_value"),
        ("pooled_pf", "pooled_pf_value"),
        ("daily_mtm_sharpe", "daily_mtm_sharpe_value"),
        ("hac_sharpe", "hac_sharpe_value"),
        ("dsr", "dsr_value"),
        ("bootstrap_positive_frac", "bootstrap_positive_frac_value"),
        ("positive_fold_frac", "positive_fold_frac_value"),
        ("stress_pnl", "stress_pnl_value"),
        ("stress_pf", "stress_pf_value"),
        ("baseline_mdd", "baseline_mdd_value"),
        ("stress_mdd", "stress_mdd_value"),
        ("margin_utilization", "margin_utilization_value"),
        ("liquidation", None),
        ("pbo", "pbo_note"),
    ]
    for k, vk in keys:
        val = g.get(vk) if vk else ""
        if isinstance(val, float):
            val = f"{val:.4f}"
        md.append(f"| {k} | {g.get(k)} | {val} |")
    md += [
        "",
        "### Headline (baseline working-limit, all-taker fee book)",
        "",
        f"- Trades: {payload['baseline'].get('n_trades')}  "
        f"(**{ _fmt(payload['gates'].get('baseline_trades_per_month')) } per month**)",
        f"- Profit factor: {_fmt(payload['baseline'].get('profit_factor'))}",
        f"- Win rate: {_fmt(payload['baseline'].get('win_rate'))}",
        f"- Entry-bar exit rate: {_fmt(payload['baseline'].get('entry_bar_exit_rate'))}",
        f"- Fill rate: {_fmt(payload['baseline'].get('fill_pct'))}",
        f"- Fees: {_fmt(payload['baseline'].get('total_fees'))}  "
        f"Funding: {_fmt(payload['baseline'].get('total_funding'))}",
        "",
        "### Deflated Sharpe Ratio sensitivity (same daily returns)",
        "",
        "| n_trials | DSR |",
        "|---:|---:|",
    ]
    for k, v in (g.get("dsr_sensitivity") or {}).items():
        if k.startswith("dsr_n"):
            md.append(f"| {k.replace('dsr_n', '')} | {_fmt(v, 4)} |")
    md += [
        "",
        "### Moderate stress (all-taker fills + 2× slippage)",
        "",
        f"- Trades: {payload['stress'].get('n_trades')}  "
        f"({_fmt(g.get('stress_trades_per_month'))} / month)",
        f"- Net PnL: {_fmt(payload['stress'].get('net_pnl'))}",
        f"- Profit factor: {_fmt(payload['stress'].get('profit_factor'))}",
        f"- Liquidations: {payload['stress'].get('n_liquidations')}",
        "",
    ]
    (OUT / "v21_sol_ema_stack_latest.md").write_text("\n".join(md), encoding="utf-8")


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    print(f"priority={raise_current_process(high=True)} demoted={demote_competitors()}", flush=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    cfg = yaml.safe_load(PREREG.read_text(encoding="utf-8"))
    if not SETTLE_DB.exists():
        raise SystemExit(f"missing settle sqlite: {SETTLE_DB}")
    con = open_checkpoint(SETTLE_DB)
    rows = load_arms(con)
    fold_rows = [
        r
        for r in rows
        if r.get("symbol") == SPEC["symbol"]
        and r.get("timeframe") == SPEC["timeframe"]
        and r.get("idea") == SPEC["idea"]
        and r.get("kind") == "fold"
        and r.get("status") == "RAN"
    ]
    fold_rows.sort(key=lambda r: int(r.get("fold_index") or 0))
    if len(fold_rows) < 5:
        raise SystemExit(f"need >=5 outer folds in sqlite, got {len(fold_rows)}")
    print(f"=== context {SPEC['symbol']} {SPEC['timeframe']} folds={len(fold_rows)} ===", flush=True)
    ctx = Ctx(SPEC["symbol"], SPEC["timeframe"])
    print("=== baseline stitched (working limit, baseline costs) ===", flush=True)
    baseline = _run_book(ctx, cfg, tag="SOL-ema-v21-base", costs=research_costs_baseline())
    print(
        f"  n={baseline.get('n_trades')} PF={_fmt(baseline.get('profit_factor'))} "
        f"tpm={_fmt(baseline.get('trades_per_month'))} daily={baseline.get('n_daily_returns')}",
        flush=True,
    )
    print("=== moderate stress (all-taker fills, 2× slippage) ===", flush=True)
    stress = _run_book(
        ctx, cfg, tag="SOL-ema-v21-stress", costs=research_costs_moderate_stress(), market=True
    )
    print(
        f"  n={stress.get('n_trades')} PF={_fmt(stress.get('profit_factor'))} "
        f"pnl={_fmt(stress.get('net_pnl'))}",
        flush=True,
    )
    gates = evaluate_nested_v21(
        fold_rows=fold_rows,
        baseline=baseline,
        stress=stress,
        n_trials=HUNT004_EVENT_ROWS,
    )
    payload = {
        "generation_id": "ml_lab_v21_sol_ema_stack",
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "stitched_outer_oos_v21_remainder",
        "not_live": True,
        "spec": SPEC,
        "n_trials_dsr": HUNT004_EVENT_ROWS,
        "baseline": _slim(baseline),
        "stress": _slim(stress),
        "fold_n_trades": [int(r.get("n_trades") or 0) for r in fold_rows],
        "fold_profit_factor": [r.get("profit_factor") for r in fold_rows],
        "gates": gates,
    }
    write_report(payload)
    append_ledger(
        f"ML_LAB_V21_SOL_EMA overall={gates.get('overall')} dsr={gates.get('dsr_value')}",
        tier=2 if gates.get("overall") == "PASS" else 0,
    )
    print(f"OVERALL {gates.get('overall')} DSR={gates.get('dsr_value')} wrote v21_sol_ema_stack_latest.md", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
