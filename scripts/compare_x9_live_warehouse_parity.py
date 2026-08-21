"""Xxobster9 multitrade p75: last N live decisions vs warehouse recompute.

Downloads expected at artifacts/reports/_x9_micro_live_state.sqlite
(or pass --ledger). Gold path: research indicators + market_ohlcv warehouse.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

os.environ.setdefault("LLM2_INDICATORS_DB", r"D:\projectsdata\indicators\indicators.sqlite")
os.environ.setdefault("LLM2_STRUCTURE_SOURCE", "binance")

from llm2.data.indicators import clear_indicator_cache  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.paths import ARTIFACTS, ROUND_TRIP_COST  # noqa: E402

PACK_DEFAULT = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_p75_v1"
LEDGER_DEFAULT = ARTIFACTS / "reports" / "_x9_micro_live_state.sqlite"
OUT_DEFAULT = ARTIFACTS / "reports" / "x9_live_warehouse_parity_latest.json"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ledger", type=Path, default=LEDGER_DEFAULT)
    ap.add_argument("--pack", type=Path, default=PACK_DEFAULT)
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--out", type=Path, default=OUT_DEFAULT)
    ap.add_argument("--abs-eps", type=float, default=1e-6)
    ap.add_argument("--feat-eps", type=float, default=1e-9)
    args = ap.parse_args(argv)

    if not args.ledger.is_file():
        raise SystemExit(f"missing ledger {args.ledger} — scp state from VPS first")

    con = sqlite3.connect(f"file:{args.ledger}?mode=ro", uri=True)
    rows = con.execute(
        "SELECT bar_ts_ms, decided_utc, side, pred_mean, mark, mode, detail "
        "FROM decisions ORDER BY bar_ts_ms DESC LIMIT ?",
        (int(args.n),),
    ).fetchall()
    states = dict(con.execute("SELECT key, value FROM state").fetchall())
    con.close()

    strength_err = None
    try:
        strength_hist = json.loads(states.get("strength_hist_json") or "[]")
        strength_hist = [float(x) for x in strength_hist]
    except Exception as exc:  # noqa: BLE001
        strength_hist = []
        strength_err = str(exc)

    strategy = json.loads((args.pack / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(args.pack / "model.joblib")
    cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    symbol = str(strategy.get("symbol") or "ETHUSDT").upper()
    timeframe = str(strategy.get("timeframe") or "1h")
    family = target_family(str(strategy.get("target", "direction")))
    edge = float(strategy.get("min_edge") or DIRECTION_BAND)
    if abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND

    clear_indicator_cache()
    ohlcv_full = load_ohlcv(symbol, timeframe)
    if ohlcv_full.index.tz is None:
        ohlcv_full.index = ohlcv_full.index.tz_localize("UTC")
    feats_full = build_space(
        ohlcv_full,
        "structure_v1",
        symbol=symbol,
        timeframe=timeframe,
        recent_only=False,
    )
    feats_full = feats_full.reindex(columns=cols)
    if "last_retrace_pct" in feats_full.columns:
        feats_full["last_retrace_pct"] = feats_full["last_retrace_pct"].fillna(0.0)
    for c in feats_full.columns:
        if str(c).startswith("last_retrace_pct_"):
            feats_full[c] = feats_full[c].fillna(0.0)

    from llm2.validation.folds import index_to_ms  # noqa: E402

    # Prefer not to drop sparse HTF NaNs on the tip for this diagnostic — live fills
    # last_retrace and scores bars that still have core 1h geometry. If residual NaNs
    # remain, fall back to per-column fill 0 for model matrix only when those columns
    # match the live pack convention (last_retrace already filled).
    residual_na = feats_full.isna().sum()
    bad_cols = {c: int(residual_na[c]) for c in residual_na.index if residual_na[c] > 0}
    if bad_cols:
        # Fill residual structure cols only on tip diagnostic path (match live snapshot).
        feats_full = feats_full.fillna(0.0)

    aligned = feats_full
    feat_ts = index_to_ms(pd.DatetimeIndex(aligned.index))
    ts_to_i = {int(t): i for i, t in enumerate(feat_ts)}
    X_all = aligned.to_numpy(dtype=float)
    # drop rows that are still entirely empty (unlikely)
    finite_row = np.isfinite(X_all).all(axis=1)
    aligned = aligned.loc[finite_row]
    X_all = aligned.to_numpy(dtype=float)
    feat_ts = index_to_ms(pd.DatetimeIndex(aligned.index))
    ts_to_i = {int(t): i for i, t in enumerate(feat_ts)}
    pred_all = blob["model"].predict(X_all)
    means_all = np.asarray(
        pred_all.mean if hasattr(pred_all, "mean") else pred_all, dtype=float
    ).reshape(-1)

    comparisons: list[dict] = []
    for bar_ts_ms, decided_utc, side, pred_mean, mark, mode, detail in reversed(rows):
        det: dict = {}
        try:
            det = json.loads(detail) if isinstance(detail, str) else (detail or {})
        except Exception:  # noqa: BLE001
            det = {}
        i = ts_to_i.get(int(bar_ts_ms))
        if i is None:
            comparisons.append(
                {
                    "bar_ts_ms": int(bar_ts_ms),
                    "error": "bar_missing_in_warehouse_feats",
                    "live_pred_mean": pred_mean,
                }
            )
            continue
        wh_mean = float(means_all[i])
        wh_side = int(proxy_side(np.asarray([wh_mean]), family)[0])
        if abs(wh_mean) < edge:
            wh_side = 0
        live_side = int(side) if side is not None else None
        live_pred = float(pred_mean) if pred_mean is not None else float("nan")
        abs_diff = abs(wh_mean - live_pred) if np.isfinite(live_pred) else float("nan")
        snap = det.get("feature_snapshot") or {}
        snap_vals = snap.get("values") if isinstance(snap, dict) else None
        mism: list[dict] = []
        max_abs = 0.0
        if snap_vals:
            row_vals = aligned.iloc[i]
            for c in cols:
                if c not in snap_vals:
                    continue
                try:
                    a = float(snap_vals[c])
                    b = (
                        float(row_vals[c])
                        if pd.notna(row_vals[c])
                        else float("nan")
                    )
                    d = (
                        abs(a - b)
                        if np.isfinite(a) and np.isfinite(b)
                        else float("inf")
                    )
                    if d > float(args.feat_eps):
                        mism.append(
                            {
                                "col": c,
                                "live_snap": a,
                                "warehouse": b,
                                "abs": d,
                            }
                        )
                        if np.isfinite(d):
                            max_abs = max(max_abs, d)
                except (TypeError, ValueError):
                    if snap_vals[c] != row_vals[c]:
                        mism.append(
                            {
                                "col": c,
                                "live_snap": snap_vals[c],
                                "warehouse": row_vals[c],
                            }
                        )
        gate = det.get("multitrade_gate") or {}
        comparisons.append(
            {
                "bar_ts_ms": int(bar_ts_ms),
                "bar_utc": pd.to_datetime(int(bar_ts_ms), unit="ms", utc=True).isoformat(),
                "decided_utc": decided_utc,
                "live_pred_mean": live_pred,
                "live_side": live_side,
                "warehouse_pred_mean": wh_mean,
                "warehouse_side": wh_side,
                "abs_diff": abs_diff,
                "pred_close_match_1e6": bool(abs_diff < float(args.abs_eps))
                if np.isfinite(abs_diff)
                else False,
                "side_match": live_side == wh_side,
                "mark": mark,
                "mode": mode,
                "skip_reason": det.get("skip_reason") or gate.get("skip_reason"),
                "gate_allow": gate.get("allow"),
                "feature_snapshot": {
                    "present": bool(snap_vals),
                    "n_mismatch": len(mism),
                    "max_abs": max_abs,
                    "sample": mism[:8],
                    "ok": len(mism) == 0,
                },
            }
        )

    ok_rows = [c for c in comparisons if "error" not in c]
    n = len(ok_rows)
    n_side = sum(1 for c in ok_rows if c.get("side_match"))
    n_pred = sum(1 for c in ok_rows if c.get("pred_close_match_1e6"))
    n_snap = sum(1 for c in ok_rows if (c.get("feature_snapshot") or {}).get("ok"))
    skips: dict[str, int] = {}
    for c in ok_rows:
        r = str(c.get("skip_reason") or "none")
        skips[r] = skips.get(r, 0) + 1

    structure_first = (
        "ok"
        if n and n_side == n and n_pred == n
        else ("STRUCTURE_OR_PRED_DRIFT" if n else "NO_BARS")
    )
    lookback = int(
        (strategy.get("multitrade") or {}).get("mean_lookback") or 168
    )

    report = {
        "evidence_class": "LIVE_WAREHOUSE_PARITY_XXOBSTER9",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "account": "Xxobster9",
        "host": "185.203.119.52",
        "service": "llm2-structure-eth-multitrade-p75-v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "n_decisions_compared": n,
        "n_requested": int(args.n),
        "pack": str(args.pack),
        "ledger": str(args.ledger),
        "strength_hist": {
            "n": len(strength_hist),
            "target_lookback": lookback,
            "fraction_of_target": (len(strength_hist) / lookback) if lookback else None,
            "min": float(np.min(strength_hist)) if strength_hist else None,
            "max": float(np.max(strength_hist)) if strength_hist else None,
            "mean": float(np.mean(strength_hist)) if strength_hist else None,
            "note": (
                "Score buffer only (not OHLCV depth). Caps at mean_lookback. "
                "Short deploy age ⇒ n << 168 until enough eligible |pred| samples."
            ),
            "error": strength_err,
            "state_keys": sorted(states.keys()),
        },
        "headline": {
            "side_match_rate": (n_side / n) if n else None,
            "pred_close_match_rate": (n_pred / n) if n else None,
            "feature_snapshot_ok_rate": (n_snap / n) if n else None,
            "max_abs_pred_diff": max(
                (float(c["abs_diff"]) for c in ok_rows if c.get("abs_diff") is not None),
                default=None,
            ),
            "median_abs_pred_diff": float(
                np.median([float(c["abs_diff"]) for c in ok_rows if c.get("abs_diff") is not None])
            )
            if ok_rows
            else None,
        },
        "gate_skip_counts_live": skips,
        "structure_first": structure_first,
        "comparisons": comparisons,
        "note": (
            "Warehouse gold path (indicators.sqlite + market OHLCV). "
            "Live pack uses shared_candles full-history structure after D-parity fix. "
            "Residual tip noise possible. Diagnostic only."
        ),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "structure_first": structure_first,
                "headline": report["headline"],
                "strength_hist": report["strength_hist"],
                "gate_skip_counts_live": skips,
                "n": n,
                "out": str(args.out),
            },
            indent=2,
            default=str,
        ),
        flush=True,
    )
    print("--- bars ---", flush=True)
    for c in comparisons:
        if "error" in c:
            print(c, flush=True)
            continue
        print(
            f"{c['bar_utc']} live={c['live_pred_mean']:+.6f} wh={c['warehouse_pred_mean']:+.6f} "
            f"d={c['abs_diff']:.3e} side {c['live_side']}/{c['warehouse_side']} "
            f"snap_mis={c['feature_snapshot']['n_mismatch']} skip={c['skip_reason']}",
            flush=True,
        )
    return 0 if structure_first == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
