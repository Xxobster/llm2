"""Edge lab hunt 001 — screen session / Smart Money Concepts / momentum events.

RESEARCH_ONLY. Never deploys. Resumable: every arm result is checkpointed in
SQLite, so a restart continues instead of recomputing.

The screen is scored **strictly before 2022-01-01**, which is where the first
outer out-of-sample fold begins. Outer folds therefore stay unseen during
selection, and `run_edge_lab_settle_001.py` can later settle the survivors on
genuinely fresh data.

Usage:

    python -u scripts/run_edge_lab_hunt_001.py
    python -u scripts/run_edge_lab_hunt_001.py --limit 200      # bounded slice
    python -u scripts/run_edge_lab_hunt_001.py --report-only
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
    run_limit_arm,
    run_market_arm,
    save_arm,
)
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.diagonal_sr.bar_series import make_bar_series  # noqa: E402
from llm2.edge_lab.events import EVENT_SIDE, build_edge_pack, session_mask  # noqa: E402
from llm2.paths import ARTIFACTS  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

PREREG = _ROOT / "configs" / "preregister" / "edge_lab_hunt_001.yaml"
OUT = ARTIFACTS / "reports" / "edge_lab"
DB_DIR = ARTIFACTS / "sqlite" / "edge_lab_hunt_001"
SCREEN_END = "2022-01-01"
MIN_CONTEXT_BARS = 600


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _screen_end_ms() -> int:
    return int(pd.Timestamp(SCREEN_END, tz="UTC").value // 1_000_000)


def _is_market(event: str) -> bool:
    return any(tok in event for tok in ("breakout", "ignition", "choch"))


def _limit_prices(sc, mask: np.ndarray, is_short: np.ndarray) -> np.ndarray:
    idx = np.flatnonzero(mask)
    c = sc.close[idx]
    atr = sc.atr_frac[idx]
    move = np.clip(np.where(np.isfinite(atr), atr, 0.005), 0.0015, 0.03)
    return np.where(is_short, c * (1.0 + move), c * (1.0 - move))


class Context:
    """Pre-2022 candles plus the causal edge pack for one symbol/timeframe."""

    def __init__(self, symbol: str, timeframe: str) -> None:
        self.symbol = symbol
        self.timeframe = timeframe
        ohlcv = load_ohlcv(symbol, timeframe)
        ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < _screen_end_ms()].copy()
        if len(ohlcv) < MIN_CONTEXT_BARS:
            raise RuntimeError(
                f"{symbol} {timeframe}: only {len(ohlcv)} bars before {SCREEN_END}"
            )
        self.ohlcv = ohlcv
        self.sc = make_bar_series(symbol, timeframe, ohlcv)
        self.pack = build_edge_pack(ohlcv)
        self.n = len(ohlcv)


def _arm_id(symbol: str, tf: str, event: str, filt: str, tp: float, sl: float) -> str:
    return f"{symbol}|{tf}|{event}|{filt}|tp{tp}|sl{sl}"


def _plan(cfg: dict) -> list[dict[str, Any]]:
    """Deterministic frozen arm order: context-major so each pack is built once."""
    symbols = list(cfg["universe"]["symbols"])
    tfs = list(cfg["universe"]["timeframes"])
    filters = list(cfg["session_filters"])
    brackets = [(float(b["tp"]), float(b["sl"])) for b in cfg["brackets"]]
    events = [e for fam in cfg["event_families"].values() for e in fam]
    unknown = [e for e in events if e not in EVENT_SIDE]
    if unknown:
        raise RuntimeError(f"preregistered events missing from catalogue: {unknown}")

    plan: list[dict[str, Any]] = []
    for tf in tfs:
        for symbol in symbols:
            for tp, sl in brackets:
                for filt in filters:
                    for event in events:
                        plan.append(
                            {
                                "symbol": symbol,
                                "timeframe": tf,
                                "event": event,
                                "session_filter": filt,
                                "tp": tp,
                                "sl": sl,
                            }
                        )
    return plan


def _recovery_factor(row: dict[str, Any]) -> float:
    ret = row.get("total_return")
    mdd = row.get("max_drawdown_pct")
    try:
        ret = float(ret)
        mdd = abs(float(mdd))
    except (TypeError, ValueError):
        return float("nan")
    if not np.isfinite(ret) or not np.isfinite(mdd) or mdd <= 0:
        return float("nan")
    return ret / mdd


def _passes(row: dict[str, Any], gates: dict[str, Any]) -> bool:
    if row.get("status") != "RAN":
        return False
    try:
        n = int(row.get("n_trades") or 0)
        tpm = float(row.get("trades_per_month"))
        pf = float(row.get("profit_factor"))
        ebr = float(row.get("entry_bar_exit_rate"))
        sh = float(row.get("sharpe_annualised"))
    except (TypeError, ValueError):
        return False
    return (
        n >= int(gates["min_trades"])
        and float(gates["min_trades_per_month"]) <= tpm <= float(gates["max_trades_per_month"])
        and np.isfinite(pf)
        and pf >= float(gates["min_profit_factor"])
        and np.isfinite(ebr)
        and ebr <= float(gates["max_entry_bar_exit_rate"])
        and np.isfinite(sh)
        and sh >= float(gates["min_sharpe_annualised"])
    )


def _fmt(v: Any) -> str:
    try:
        x = float(v)
    except (TypeError, ValueError):
        return ""
    return f"{x:.3f}" if np.isfinite(x) else ""


def write_report(con, cfg: dict, stamp: str, extra: dict) -> dict[str, Any]:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_arms(con)
    for r in rows:
        r["recovery_factor"] = _recovery_factor(r)
    ran = [r for r in rows if r.get("status") == "RAN"]
    gates = cfg["screen_gates"]
    passing = [r for r in ran if _passes(r, gates)]
    passing.sort(key=lambda r: -(float(r.get("profit_factor") or 0)))
    ran.sort(key=lambda r: -(float(r.get("profit_factor") or 0)))

    status_counts: dict[str, int] = {}
    for r in rows:
        status_counts[str(r.get("status"))] = status_counts.get(str(r.get("status")), 0) + 1

    payload = {
        "generation_id": "edge_lab_hunt_001",
        "stamp": stamp,
        "readiness_max": "LIVE_STOP / RESEARCH_ONLY",
        "evidence_class": "inner_screen_pre_2022_only",
        "not_live": True,
        "selection_window": f"< {SCREEN_END}",
        "n_rows": len(rows),
        "status_counts": status_counts,
        "n_screen_pass": len(passing),
        "screen_gates": gates,
        "extra": extra,
        "screen_pass": passing,
        "top_ran": ran[:200],
    }
    (OUT / "hunt_001_latest.json").write_text(
        json.dumps(jsonable(payload), indent=2), encoding="utf-8"
    )

    md = [
        "# Edge lab hunt 001 — screen leaderboard",
        "",
        f"**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `{stamp}`.",
        f"**Evidence class:** inner screen on bars **before {SCREEN_END}** only. "
        "Outer folds (2022-01-01 onward) were not scored and remain unseen.",
        "",
        f"Arms recorded: {len(rows)}. Status: "
        + ", ".join(f"{k}={v}" for k, v in sorted(status_counts.items()))
        + f". Screen passes: {len(passing)}.",
        "",
        "| Symbol | TF | Event | Session | TP | SL | n | /mo | PF | WR | Sharpe | HAC | Sortino | Recovery | MDD% | ebr |",
        "|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in (passing or ran[:40]):
        md.append(
            "| {sym} | {tf} | `{ev}` | {ses} | {tp} | {sl} | {n} | {tpm} | {pf} | {wr} | "
            "{sh} | {hac} | {so} | {rf} | {mdd} | {ebr} |".format(
                sym=r.get("symbol"),
                tf=r.get("timeframe"),
                ev=r.get("event"),
                ses=r.get("session_filter"),
                tp=r.get("tp"),
                sl=r.get("sl"),
                n=r.get("n_trades"),
                tpm=_fmt(r.get("trades_per_month")),
                pf=_fmt(r.get("profit_factor")),
                wr=_fmt(r.get("win_rate")),
                sh=_fmt(r.get("sharpe_annualised")),
                hac=_fmt(r.get("sharpe_hac_annualised")),
                so=_fmt(r.get("sortino_annualised")),
                rf=_fmt(r.get("recovery_factor")),
                mdd=_fmt(r.get("max_drawdown_pct")),
                ebr=_fmt(r.get("entry_bar_exit_rate")),
            )
        )
    if not passing:
        md.append("")
        md.append(
            "_No arm clears the frozen screen gates yet. The rows above are the "
            "best scored arms so far and are **not** candidates._"
        )
    (OUT / "hunt_001_latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0, help="Max arms this process runs (0 = all).")
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
    extra = {
        "preregister_sha256": prereg_sha,
        "n_planned_arms": len(plan),
        "screen_end": SCREEN_END,
    }

    if args.report_only:
        payload = write_report(con, cfg, stamp, extra)
        print(json.dumps({k: payload[k] for k in ("n_rows", "status_counts", "n_screen_pass")}, indent=2))
        return 0

    append_ledger(f"EDGE_LAB_HUNT_001 start {stamp} planned={len(plan)}", tier=0)
    print(f"preregister_sha256={prereg_sha} planned_arms={len(plan)}", flush=True)

    work = [
        (i, spec)
        for i, spec in enumerate(plan)
        if not arm_done(
            con,
            _arm_id(
                spec["symbol"], spec["timeframe"], spec["event"],
                spec["session_filter"], spec["tp"], spec["sl"],
            ),
        )
    ]
    print(f"remaining_arms={len(work)}", flush=True)
    if args.limit:
        work = work[: int(args.limit)]

    work_bars = cfg["work_bars"]
    max_hold = cfg["max_hold_bars"]
    ctx: Context | None = None
    ctx_key: tuple[str, str] | None = None
    done_since_report = 0

    for i, spec in work:
        symbol, tf = spec["symbol"], spec["timeframe"]
        event, filt = spec["event"], spec["session_filter"]
        tp, sl = float(spec["tp"]), float(spec["sl"])
        aid = _arm_id(symbol, tf, event, filt, tp, sl)

        if ctx_key != (symbol, tf):
            print(f"=== context {symbol} {tf} ===", flush=True)
            try:
                ctx = Context(symbol, tf)
            except Exception as exc:  # noqa: BLE001
                print(f"  CONTEXT_FAIL {symbol} {tf}: {exc}", flush=True)
                ctx = None
            ctx_key = (symbol, tf)
        if ctx is None:
            save_arm(
                con, aid, spec,
                {"status": "NO_CONTEXT", "n_trades": 0, "arm_id": aid, **spec},
            )
            continue

        occ = ctx.pack.occurrence[event].to_numpy(dtype=np.int8) > 0
        mask = occ & session_mask(ctx.pack.session, filt)
        side = int(EVENT_SIDE[event])
        is_short_all = side < 0
        n_gated = int(mask.sum())
        payload: dict[str, Any]
        if n_gated < 15:
            payload = {"status": "TOO_FEW_GATED", "n_intent": n_gated, "n_trades": 0}
        else:
            is_short = np.full(n_gated, is_short_all, dtype=bool)
            try:
                if _is_market(event):
                    payload = run_market_arm(
                        symbol, ctx.sc, mask, is_short, tag=aid,
                        max_hold=int(max_hold[tf]), tp=tp, sl=sl,
                    )
                else:
                    lim = _limit_prices(ctx.sc, mask, is_short)
                    payload = run_limit_arm(
                        symbol, ctx.sc, mask, is_short, lim, tag=aid,
                        work=int(work_bars[tf]), max_hold=int(max_hold[tf]), tp=tp, sl=sl,
                    )
            except Exception as exc:  # noqa: BLE001
                payload = {"status": "ERROR", "error": str(exc)[:400], "n_trades": 0}

        payload.update(
            {
                "symbol": symbol,
                "timeframe": tf,
                "event": event,
                "session_filter": filt,
                "tp": tp,
                "sl": sl,
                "side": side,
                "entry_style": "market" if _is_market(event) else "working_limit",
                "arm_id": aid,
                "plan_index": i,
            }
        )
        payload["recovery_factor"] = _recovery_factor(payload)
        save_arm(con, aid, spec, payload)
        done_since_report += 1
        print(
            f"[{i + 1}/{len(plan)}] {aid} -> {payload.get('status')} "
            f"n={payload.get('n_trades')} PF={_fmt(payload.get('profit_factor'))} "
            f"tpm={_fmt(payload.get('trades_per_month'))} "
            f"Sh={_fmt(payload.get('sharpe_annualised'))} "
            f"ebr={_fmt(payload.get('entry_bar_exit_rate'))}",
            flush=True,
        )
        if done_since_report >= 40:
            write_report(con, cfg, stamp, extra)
            done_since_report = 0

    payload = write_report(con, cfg, stamp, extra)
    append_ledger(
        f"EDGE_LAB_HUNT_001 report rows={payload['n_rows']} pass={payload['n_screen_pass']}",
        tier=0,
    )
    print(
        f"WROTE {OUT / 'hunt_001_latest.md'} rows={payload['n_rows']} "
        f"pass={payload['n_screen_pass']}",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
