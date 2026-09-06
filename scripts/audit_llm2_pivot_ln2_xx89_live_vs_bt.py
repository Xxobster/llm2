#!/usr/bin/env python3
"""Live vs backtest for LLM2 pivot units on ln2: Xxobster8 and Xxobster9.

  python -u scripts/audit_llm2_pivot_ln2_xx89_live_vs_bt.py --i-accept-lockbox-contamination
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()
if "botsgeneral" not in __import__("tradesim").__file__.replace("\\", "/"):
    raise SystemExit("tradesim must load from botsgeneral")

from llm2.data.loader import load_ohlcv
from llm2.evidence.lockbox_guard import add_lockbox_guard_args, require_lockbox_access
from llm2.gates.evidence import leverage_from_stop
from llm2.live.pivot_runner import load_pack
from llm2.paths import ARTIFACTS

SPEC = ROOT / "scripts" / "audit_llm2_pivot_live_vs_bt.py"
_mod = importlib.util.spec_from_file_location("audit_pivot_ln1", SPEC)
assert _mod and _mod.loader
audit = importlib.util.module_from_spec(_mod)
_mod.loader.exec_module(audit)

DUMP = ARTIFACTS / "reports" / "_ln2_xx89_pivot_live.json"
VPS_15M = ARTIFACTS / "reports" / "_ln2_15m_eth_sol.json"
OUT_JSON = ARTIFACTS / "reports" / "audit_llm2_pivot_ln2_xx89_live_vs_bt_latest.json"
OUT_MD = ARTIFACTS / "reports" / "audit_llm2_pivot_ln2_xx89_live_vs_bt_latest.md"
SINCE = datetime(2026, 8, 21, tzinfo=timezone.utc)
SINCE_MS = int(SINCE.timestamp() * 1000)

ARMS = (
    {
        "name": "xx8_eth",
        "account": "Xxobster8",
        "pack": ARTIFACTS / "live_packs" / "pivot_eth_p75_ctrl_atr_w4",
        "vps_key": "ETHUSDT_15m",
        "unit": "llm2-pivot-eth-p75-ctrl-atr-w4",
        "tp_sl": "1%/1%",
    },
    {
        "name": "xx8_sol",
        "account": "Xxobster8",
        "pack": ARTIFACTS / "live_packs" / "pivot_sol_geo_tp1_sl1_p75_w4",
        "vps_key": "SOLUSDT_15m",
        "unit": "llm2-pivot-sol-geo-p75-w4",
        "tp_sl": "1%/1%",
    },
    {
        "name": "xx9_eth",
        "account": "Xxobster9",
        "pack": ARTIFACTS / "live_packs" / "pivot_eth_p50_tp05_sl05_w4",
        "vps_key": "ETHUSDT_15m",
        "unit": "llm2-pivot-eth-p50-tp05-sl05",
        "tp_sl": "0.5%/0.5%",
    },
    {
        "name": "xx9_sol",
        "account": "Xxobster9",
        "pack": ARTIFACTS / "live_packs" / "pivot_sol_p50_tp05_sl05_w4",
        "vps_key": "SOLUSDT_15m",
        "unit": "llm2-pivot-sol-p50-tp05-sl05",
        "tp_sl": "0.5%/0.5%",
    },
)


def _payloads(dump: dict, arm: str) -> list[dict]:
    rows = ((dump.get("arms") or {}).get(arm) or {}).get("pivot_decisions") or []
    out = []
    for r in rows:
        p = json.loads(r["payload_json"]) if isinstance(r.get("payload_json"), str) else r["payload_json"]
        out.append(p)
    return out


def write_md(report: dict) -> None:
    lines = [
        "# LLM2 pivot live vs backtest (live-network-2, Xxobster8 + Xxobster9)",
        "",
        f"**Maximum earned readiness:** `{report['maximum_earned_readiness']}`",
        f"**Evidence class:** `{report['evidence_class']}`",
        f"**Principal blocker:** {report['principal_blocker']}",
        f"Generated: {report['generated_utc']}",
        "",
        "Scope: this project's pivot units on live-network-2 only. Structure units ignored.",
        "Xxobster9 0.5%/0.5% remains RESEARCH_ONLY (~80% same-15-minute exits). Operational live is not a promote.",
        "",
    ]
    for arm in report["arms"]:
        lines += [
            f"## {arm['account']} `{arm['unit']}` ({arm['tp_sl']})",
            "",
            f"- Candles 15-minute VPS vs warehouse (`price_type=last`): match_rate={arm['candles'].get('match_rate')} missing={arm['candles'].get('warehouse_missing')} mismatch={arm['candles'].get('ohlc_mismatch')} tip={arm['candles'].get('warehouse_tip_utc')}",
            f"- Decision replay: action {arm['replay'].get('action_match')}/{arm['replay'].get('n_replayed')} ; p_any {arm['replay'].get('p_any_match')}/{arm['replay'].get('n_replayed')}",
            f"- Live ENTER / filled / cancelled-data-unsafe: {arm['live_counts']}",
            f"- Backtest on live ENTER intents: n={arm['bt'].get('n_trades')} PF={arm['bt'].get('profit_factor')} net={arm['bt'].get('net_pnl')}",
            f"- Fill pairs: live_fills={arm['fills'].get('n_live_fills')} bt={arm['fills'].get('n_bt_trades')} extra_bt={arm['fills'].get('n_extra_bt')}",
            f"- Live fill ledger: n={arm.get('fill_ledger_n')}",
            f"- Missed signals (BT ENTER, live not): {(arm.get('missed') or {}).get('n_missed_signals')} "
            f"(replay {(arm.get('missed') or {}).get('n_replay_bt_enter_live_not')} + no-row {(arm.get('missed') or {}).get('n_bt_enter_no_live_row')})",
            f"- Missed trades (unfilled + extra BT): {(arm.get('missed') or {}).get('n_missed_trades')}",
            "",
        ]
        if arm["replay"].get("flips"):
            lines.append("Action / probability flips:")
            for f in arm["replay"]["flips"][:8]:
                lines.append(f"- {f}")
            lines.append("")
    lines += ["## Fixes applied or refused", ""]
    for note in report.get("fix_notes") or []:
        lines.append(f"- {note}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    add_lockbox_guard_args(ap)
    args = ap.parse_args(argv)
    require_lockbox_access(
        experiment_id="audit_llm2_pivot_ln2_xx89_live_vs_bt",
        window_start=SINCE.date().isoformat(),
        window_end=datetime.now(timezone.utc).date().isoformat(),
        purpose="live_vs_bt_reconcile_ln2_xx89",
        symbols=["ETHUSDT", "SOLUSDT"],
        accepted_contamination=bool(args.i_accept_lockbox_contamination),
    )
    dump = json.loads(DUMP.read_text(encoding="utf-8"))
    vps15 = json.loads(VPS_15M.read_text(encoding="utf-8")) if VPS_15M.is_file() else {}
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "LIVE_BT_PIVOT_RECONCILE_CONTAMINATED",
        "principal_blocker": "pending",
        "scope": "ln2 Xxobster8 + Xxobster9 pivot only",
        "since_utc": SINCE.isoformat(),
        "units": dump.get("units"),
        "one_m_rows": dump.get("one_m_rows"),
        "arms": [],
        "fix_notes": [],
    }
    blockers: list[str] = []
    for spec in ARMS:
        print("ARM", spec["name"], flush=True)
        strat, blob = load_pack(spec["pack"])
        symbol = str(strat["symbol"])
        ohlcv = load_ohlcv(symbol, "15m", price_type="last")
        if str(ohlcv.attrs.get("price_type")) != "last":
            raise SystemExit(f"{symbol} loaded price_type={ohlcv.attrs.get('price_type')!r}")
        live_decs = [p for p in _payloads(dump, spec["name"]) if int(p["bar_ts_ms"]) >= SINCE_MS]
        candles = audit.compare_candles(symbol, vps15.get(spec["vps_key"]) or [], ohlcv)
        replay = audit.replay_decisions(ohlcv, strat, blob, live_decs)
        intents, live_counts = audit.live_intents(live_decs, strat)
        sigs, stats = audit.materialize_working_limits(
            ohlcv, intents, work_bars=int(strat["work_bars"])
        )
        sl = float(strat["sl_pct"])
        # Monkeypatch leverage inside run_bt by wrapping
        orig = audit.research_margin
        audit.research_margin = lambda **kw: orig(leverage=float(leverage_from_stop(sl)))
        try:
            bt = audit.run_bt(
                symbol,
                ohlcv,
                sigs,
                max_hold=int(strat["max_hold_bars"]),
                tag=f"pivot_{spec['name']}_ln2_window",
                inst=audit._instrument(strat),
            )
        finally:
            audit.research_margin = orig
        fills = audit.match_fills(live_decs, bt.get("trades") or [], sl)
        missed = audit.missed_signals_and_trades(
            ohlcv, strat, blob, live_decs, replay, live_counts, fills, since_ms=SINCE_MS
        )
        fill_ledger = ((dump.get("arms") or {}).get(spec["name"]) or {}).get("pivot_fills") or []
        if not candles.get("pass"):
            blockers.append(f"{spec['name']}_candle_mismatch")
        if not replay.get("pass"):
            blockers.append(f"{spec['name']}_signal_mismatch")
        report["arms"].append(
            {
                "name": spec["name"],
                "account": spec["account"],
                "unit": spec["unit"],
                "tp_sl": spec["tp_sl"],
                "symbol": symbol,
                "candles": candles,
                "replay": {k: v for k, v in replay.items() if k != "scored"},
                "live_counts": live_counts,
                "materialize": stats,
                "bt": bt,
                "fills": fills,
                "missed": missed,
                "fill_ledger_n": len(fill_ledger),
            }
        )
    extra_bt = sum(int(a["fills"].get("n_extra_bt") or 0) for a in report["arms"])
    unsafe = sum(int((a["live_counts"] or {}).get("cancelled_data_unsafe") or 0) for a in report["arms"])
    n_enter = sum(int((a["live_counts"] or {}).get("ENTER_LIMIT") or 0) for a in report["arms"])
    n_fill = sum(int((a["live_counts"] or {}).get("filled") or 0) for a in report["arms"])
    if any("signal_mismatch" in b for b in blockers):
        report["principal_blocker"] = "live vs backtest ENTER/FLAT action mismatch"
    elif any("candle_mismatch" in b for b in blockers):
        report["principal_blocker"] = "15-minute VPS vs warehouse Open-High-Low-Close mismatch"
    elif n_enter == 0:
        report["principal_blocker"] = (
            "No live ENTER yet on live-network-2. Signal identity can be checked; fill parity cannot."
        )
    elif unsafe:
        report["principal_blocker"] = (
            f"{unsafe} live ENTER cancelled as data-unsafe; backtest still fills those limits."
        )
    elif extra_bt:
        report["principal_blocker"] = f"{extra_bt} extra backtest fills vs live"
    else:
        report["principal_blocker"] = (
            f"none for signal identity; live fills={n_fill}. Window book is not a promote number."
        )
    report["fix_notes"] = [
        "Did not change take-profit, stop, gate, work, or hold.",
        "Did not disable live-data-001.",
        "Did not add 1-minute to the live collector.",
        "Research load used price_type=last. Mark stays under source=binance_mark.",
        "Xxobster9 0.5%/0.5% was not retuned. Research still flags ~80% same-bar exits.",
    ]
    OUT_JSON.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    write_md(report)
    print("wrote", OUT_JSON)
    print("wrote", OUT_MD)
    print("blocker", report["principal_blocker"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
