"""Ops gate: closed-candle tip + live pack indicators + pred_mean vs research warehouse.

Production **1h** fleet signal identity (candles + pack structure + pred_mean vs research).
For a fast **1m** indicator-only diagnostic (no model, no trades, not a readiness gate),
use ``scripts/run_1m_indicator_parity_bot.py`` instead.

**All active bots (ln1 94.x + ln3 185.x) in one shot** — live ``pred_mean`` vs local
warehouse recompute for the last closed hour (named gate: **Fleet Live Signal Parity**)::

  python scripts/ops_fleet_live_signal_parity.py

After collector restart / history_schema bump / candle heal, for a *single* unit run::

  python scripts/ops_live_research_parity_gate.py --host ln3 --unit llm2-structure-eth

Default compares the latest *closed* 1h bar. Use ``--wait-next-close`` to block until
the next 1h close, then re-pull live decision + recompute.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.verify_llm2_live_warehouse_after_bake import (  # noqa: E402
    warehouse_closed,
)

WH = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
IND = Path(r"D:\projectsdata\indicators\indicators.sqlite")
REPORTS = ROOT / "artifacts" / "reports"
TF_MS_1H = 3_600_000


def _ssh(host: str, remote: str) -> str:
    return subprocess.check_output(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=25", host, remote],
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def _unit_env(host: str, unit: str) -> dict[str, str]:
    blob = _ssh(host, f"systemctl show {unit} -p Environment --value")
    out: dict[str, str] = {}
    for part in blob.split():
        if "=" in part:
            k, v = part.split("=", 1)
            out[k] = v
    return out


def _wait_next_1h_close(*, lead_sec: float = 5.0) -> int:
    now = time.time()
    # next hour boundary UTC
    next_close = (int(now) // 3600 + 1) * 3600
    sleep_s = max(0.0, next_close - now + lead_sec)
    print(
        json.dumps(
            {
                "waiting_sec": sleep_s,
                "next_close_utc": datetime.fromtimestamp(
                    next_close, tz=timezone.utc
                ).isoformat(),
            }
        )
    )
    time.sleep(sleep_s)
    return int(next_close * 1000) - TF_MS_1H  # open ts of just-closed bar


def pull_live_decision(host: str, unit: str, *, bar_ts_ms: int | None) -> dict:
    env = _unit_env(host, unit)
    wd = _ssh(host, f"systemctl show {unit} -p WorkingDirectory --value").strip()
    ind = env.get("LLM2_INDICATORS_DB", "")
    # ensure helper on host
    helper = ROOT / "scripts" / "_vps_pull_live_decision.py"
    subprocess.check_call(
        ["scp", "-o", "BatchMode=yes", str(helper), f"{host}:/tmp/_vps_pull_live_decision.py"]
    )
    bar_env = "none" if bar_ts_ms is None else str(int(bar_ts_ms))
    raw = _ssh(
        host,
        "export LLM2_WD="
        + json.dumps(wd)
        + f" LLM2_INDICATORS_DB={json.dumps(ind)} LLM2_BAR_TS_MS={bar_env}; "
        f"cd {wd} && ./venv/bin/python /tmp/_vps_pull_live_decision.py",
    )
    lines = [ln for ln in raw.splitlines() if ln.strip().startswith("{")]
    if not lines:
        raise RuntimeError(f"no JSON from live decision pull: {raw[-500:]}")
    return json.loads(lines[-1])


def compare_pack_tip_to_research(
    pack_tip_row: dict,
    *,
    symbol: str,
    ts_ms: int,
    timeframe: str = "1h",
    abs_eps: float = 1e-9,
) -> dict:
    con = sqlite3.connect(f"file:{IND}?mode=ro", uri=True)
    try:
        cols = [r[1] for r in con.execute("PRAGMA table_info(bar_features)").fetchall()]
        use = [c for c in cols if c in pack_tip_row]
        if not use:
            return {"error": "no_common_columns"}
        row = con.execute(
            f"SELECT {','.join(use)} FROM bar_features "
            "WHERE symbol=? AND timeframe=? AND source='binance' AND ts_ms=?",
            (symbol.upper(), str(timeframe), int(ts_ms)),
        ).fetchone()
        if not row:
            return {"error": "research_tip_missing", "ts_ms": ts_ms, "n_cols": len(use)}
        research = dict(zip(use, row))
        mismatches = []
        for c in use:
            a, b = pack_tip_row.get(c), research.get(c)
            if a is None and b is None:
                continue
            try:
                fa, fb = float(a), float(b)
                if abs(fa - fb) > abs_eps:
                    mismatches.append({"col": c, "pack": fa, "research": fb, "abs": abs(fa - fb)})
            except (TypeError, ValueError):
                if a != b:
                    mismatches.append({"col": c, "pack": a, "research": b})
        return {
            "n_cols": len(use),
            "n_mismatch": len(mismatches),
            "max_abs": max((m["abs"] for m in mismatches if "abs" in m), default=0.0),
            "first_mismatches": mismatches[:8],
            "identical": len(mismatches) == 0,
            "research_close": research.get("close"),
            "pack_close": pack_tip_row.get("close"),
        }
    finally:
        con.close()


def recompute_pred_mean(
    *,
    pack_dir: Path,
    symbol: str,
    timeframe: str,
    bar_ts_ms: int,
) -> dict:
    from tradesim.ensure_source import prefer_botsgeneral_tradesim

    prefer_botsgeneral_tradesim()
    os.environ["LLM2_INDICATORS_DB"] = str(IND)
    os.environ["LLM2_STRUCTURE_SOURCE"] = "binance"
    import joblib

    from llm2.data.indicators import clear_indicator_cache
    from llm2.data.loader import load_ohlcv
    from llm2.features.registry import build_space
    from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family
    from llm2.paths import ROUND_TRIP_COST

    strategy = json.loads((pack_dir / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(pack_dir / "model.joblib")
    cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    # include the decision bar
    ohlcv = ohlcv.loc[ohlcv["ts_ms"] <= int(bar_ts_ms)].copy()
    if int(ohlcv["ts_ms"].iloc[-1]) != int(bar_ts_ms):
        return {
            "error": "bar_missing_in_warehouse_ohlcv",
            "want": bar_ts_ms,
            "got": int(ohlcv["ts_ms"].iloc[-1]) if len(ohlcv) else None,
        }
    clear_indicator_cache()
    feats = build_space(
        ohlcv, "structure_v1", symbol=symbol, timeframe=timeframe, recent_only=False
    )
    row = feats.reindex(columns=cols).iloc[[-1]].copy()
    for c in row.columns:
        if c == "last_retrace_pct" or str(c).startswith("last_retrace_pct_"):
            row[c] = row[c].fillna(0.0)
    pred = blob["model"].predict(row.to_numpy(dtype=float))
    mean = float(np.asarray(pred.mean if hasattr(pred, "mean") else pred).reshape(-1)[0])
    family = target_family(str(strategy.get("target", "fwd_return")))
    edge = float(
        strategy.get(
            "min_edge",
            DIRECTION_BAND if family == "directional" else ROUND_TRIP_COST,
        )
    )
    if family == "directional" and abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    side = int(proxy_side(np.asarray([mean]), family)[0])
    if abs(mean) < edge:
        side = 0
    snap = {c: (None if pd.isna(row.iloc[0][c]) else float(row.iloc[0][c])) for c in cols}
    return {
        "pred_mean": mean,
        "side": side,
        "edge": edge,
        "feature_snapshot_values": snap,
        "bar_ts_ms": bar_ts_ms,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--host", default="ln3", help="ssh host alias (ln1/ln3)")
    ap.add_argument("--unit", default="llm2-structure-eth")
    ap.add_argument(
        "--local-pack",
        type=Path,
        default=ROOT / "artifacts/live_packs/structure_v1_ethusdt_direction",
    )
    ap.add_argument("--symbol", default="ETHUSDT")
    ap.add_argument("--timeframe", default="1h")
    ap.add_argument("--wait-next-close", action="store_true")
    ap.add_argument("--bar-ts-ms", type=int, default=None)
    ap.add_argument("--skip-candles", action="store_true")
    args = ap.parse_args(argv)

    REPORTS.mkdir(parents=True, exist_ok=True)
    out: dict = {
        "evidence_class": "OPS_LIVE_RESEARCH_PARITY_GATE",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "host": args.host,
        "unit": args.unit,
    }
    blockers: list[str] = []

    bar_ts = args.bar_ts_ms
    if args.wait_next_close:
        bar_ts = _wait_next_1h_close(lead_sec=5.0)

    # 1) Candle tip gate (reuse tip50 / tip OHLC) — after wait so tip is the new close
    if not args.skip_candles:
        tip_js = _ssh(
            args.host,
            "python3 - <<'PY'\n"
            "import json,sqlite3,hashlib,time\n"
            "from datetime import datetime,timezone\n"
            "now=int(time.time()*1000); step=3600000\n"
            "con=sqlite3.connect('/var/lib/botsgeneral/shared_candles.db')\n"
            "rows=con.execute(\"SELECT ts_ms,open,high,low,close FROM candles WHERE exchange='binance' AND symbol='ETHUSDT' AND timeframe='1h' ORDER BY ts_ms\").fetchall()\n"
            "closed=[r for r in rows if r[0]+step<=now]\n"
            "tip=closed[-1]; tip50=closed[-50:]\n"
            "blob=''.join(f'{r[0]}|{r[1]}|{r[2]}|{r[3]}|{r[4]}\\n' for r in tip50).encode()\n"
            "print(json.dumps({'tip_ts_ms':tip[0],'tip_ohlc':[float(x) for x in tip[1:]],'tip50':hashlib.sha256(blob).hexdigest(),'n_closed':len(closed)}))\n"
            "PY",
        )
        live_tip = json.loads([ln for ln in tip_js.splitlines() if ln.startswith("{")][-1])
        wh = warehouse_closed("ETHUSDT", "1h")
        candle_ok = (
            live_tip["tip_ohlc"] == wh["tip_ohlc"]
            and live_tip["tip_ts_ms"] == wh["tip_ts_ms"]
            and live_tip["tip50"] == wh["tip50_ohlc_sha256"]
        )
        out["candles"] = {"live": live_tip, "warehouse": wh, "ok": candle_ok}
        if not candle_ok:
            blockers.append("CANDLE_TIP_MISMATCH")

    # 2) Live decision + pack tip — poll after close (structure refresh can take minutes)
    live = None
    poll_deadline = time.time() + (8 * 60 if args.wait_next_close else 0)
    while True:
        live = pull_live_decision(args.host, args.unit, bar_ts_ms=bar_ts)
        if live.get("row"):
            break
        if time.time() >= poll_deadline:
            break
        print(json.dumps({"polling_decision_for_bar_ts_ms": bar_ts}))
        time.sleep(20)
    out["live_pull"] = {
        "ledger": live.get("ledger"),
        "pack_1h": live.get("pack_1h"),
        "decision": {
            k: live.get("row", {}).get(k) if live.get("row") else None
            for k in ("bar_ts_ms", "decided_utc", "side", "pred_mean")
        },
    }
    if not live.get("row"):
        blockers.append("LIVE_DECISION_MISSING")
        out["principal_blocker"] = blockers[0]
        out["blockers"] = blockers
        out["all_ok"] = False
        path = REPORTS / "ops_live_research_parity_gate_latest.json"
        path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
        print(json.dumps(out, indent=2, default=str))
        return 1

    dec = live["row"]
    bar_ts = int(dec["bar_ts_ms"])
    symbol = args.symbol.upper()

    # 3) Pack tip / decision-bar vs research indicators
    pack_row = live.get("pack_decision_row") or live.get("pack_tip_row")
    pack_tip_ts = (live.get("pack_1h") or {}).get("max_ts")
    if pack_row:
        ts_cmp = bar_ts
        # Prefer exact decision-bar row; else pack tip ts
        if live.get("pack_decision_row"):
            ts_cmp = bar_ts
        elif pack_tip_ts:
            ts_cmp = int(pack_tip_ts)
        ind_cmp = compare_pack_tip_to_research(pack_row, symbol=symbol, ts_ms=int(ts_cmp))
        out["indicators_pack_vs_research"] = ind_cmp
        if not ind_cmp.get("identical"):
            blockers.append("INDICATOR_PACK_NE_RESEARCH")
    else:
        out["indicators_pack_vs_research"] = {"error": "pack_row_missing"}
        blockers.append("PACK_INDICATOR_ROW_MISSING")

    # 4) Signal recompute from research warehouse
    if not args.local_pack.is_dir():
        blockers.append("LOCAL_PACK_MISSING")
        recompute = {"error": "local_pack_missing"}
    else:
        recompute = recompute_pred_mean(
            pack_dir=args.local_pack,
            symbol=symbol,
            timeframe=args.timeframe,
            bar_ts_ms=bar_ts,
        )
    out["warehouse_recompute"] = {
        k: recompute.get(k)
        for k in ("pred_mean", "side", "edge", "bar_ts_ms", "error")
        if k in recompute or k == "error"
    }
    live_pred = float(dec["pred_mean"])
    live_side = int(dec["side"]) if dec["side"] is not None else None
    if recompute.get("pred_mean") is not None:
        abs_diff = abs(float(recompute["pred_mean"]) - live_pred)
        side_match = int(recompute["side"]) == live_side
        close_match = abs_diff < 1e-6
        # feature_snapshot compare if present
        snap = (dec.get("detail") or {}).get("feature_snapshot") or {}
        snap_vals = snap.get("values") if isinstance(snap, dict) else None
        snap_cmp = None
        if snap_vals and recompute.get("feature_snapshot_values"):
            mism = []
            for k, v in recompute["feature_snapshot_values"].items():
                if k not in snap_vals:
                    continue
                try:
                    if abs(float(snap_vals[k]) - float(v)) > 1e-9:
                        mism.append(k)
                except (TypeError, ValueError):
                    if snap_vals[k] != v:
                        mism.append(k)
            snap_cmp = {"n_mismatch": len(mism), "sample": mism[:10], "ok": len(mism) == 0}
            # If pack indicators already match research but the stored snapshot does not,
            # the ledger row was decided before a structure heal — soft warning only when
            # pred/side already match.
            if (
                not snap_cmp["ok"]
                and out.get("indicators_pack_vs_research", {}).get("identical")
                and close_match
                and side_match
            ):
                snap_cmp["ok"] = True
                snap_cmp["note"] = (
                    "snapshot_stale_vs_healed_pack_indicators; pred/side match warehouse"
                )
            elif not snap_cmp["ok"]:
                blockers.append("FEATURE_SNAPSHOT_MISMATCH")
        out["signal"] = {
            "live_pred_mean": live_pred,
            "live_side": live_side,
            "warehouse_pred_mean": recompute["pred_mean"],
            "warehouse_side": recompute["side"],
            "abs_diff": abs_diff,
            "side_match": side_match,
            "pred_close_match_1e6": close_match,
            "feature_snapshot": snap_cmp,
        }
        if not side_match:
            blockers.append("SIDE_MISMATCH")
        if not close_match:
            blockers.append("PRED_MEAN_MISMATCH")
    else:
        blockers.append(str(recompute.get("error") or "RECOMPUTE_FAILED"))

    # Drop soft-resolved blockers that may have been appended earlier wrongly
    blockers = [b for b in blockers if b != "FEATURE_SNAPSHOT_MISMATCH" or not (
        out.get("signal", {}).get("feature_snapshot", {}) or {}
    ).get("ok")]
    # Rebuild blockers cleanly from remaining hard fails
    hard: list[str] = []
    if out.get("candles") and not out["candles"].get("ok"):
        hard.append("CANDLE_TIP_MISMATCH")
    ind = out.get("indicators_pack_vs_research") or {}
    if ind.get("identical") is False:
        hard.append("INDICATOR_PACK_NE_RESEARCH")
    if ind.get("error"):
        hard.append("PACK_INDICATOR_ROW_MISSING")
    sig = out.get("signal") or {}
    if sig.get("side_match") is False:
        hard.append("SIDE_MISMATCH")
    if sig.get("pred_close_match_1e6") is False:
        hard.append("PRED_MEAN_MISMATCH")
    fs = sig.get("feature_snapshot") or {}
    if fs and fs.get("ok") is False:
        hard.append("FEATURE_SNAPSHOT_MISMATCH")
    if not live.get("row"):
        hard.append("LIVE_DECISION_MISSING")
    blockers = hard
    out["principal_blocker"] = blockers[0] if blockers else None
    out["blockers"] = blockers
    out["all_ok"] = not blockers
    path = REPORTS / "ops_live_research_parity_gate_latest.json"
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(json.dumps(out, indent=2, default=str))
    return 0 if out["all_ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
