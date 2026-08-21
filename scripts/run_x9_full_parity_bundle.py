"""Full Xxobster9 live ops bundle: warehouse parity, column diffs, candle tip, strength, gate."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
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
from llm2.validation.folds import index_to_ms  # noqa: E402

HOST = "185.203.119.52"
UNIT_ROOT = "/opt/llm2-structure-eth-multitrade-p75-v1"
LEDGER_LOCAL = ARTIFACTS / "reports" / "_x9_micro_live_state.sqlite"
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_p75_v1"
OUT = ARTIFACTS / "reports" / "x9_live_full_parity_bundle_latest.json"
WH_CANDLES = Path(r"D:\projectsdata\candles\market_ohlcv.sqlite")
ABS_EPS = 1e-6
FEAT_EPS = 1e-9
PRED_DRIFT_EPS = 1e-4


def _ssh(cmd: str) -> str:
    return subprocess.check_output(
        ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=30", f"root@{HOST}", cmd],
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def fetch_shared_tip() -> dict:
    remote = r"""
import json, sqlite3, time, hashlib
now = int(time.time() * 1000)
step = 3_600_000
con = sqlite3.connect("/var/lib/botsgeneral/shared_candles.db")
rows = con.execute(
    "SELECT ts_ms, open, high, low, close FROM candles "
    "WHERE exchange='binance' AND symbol='ETHUSDT' AND timeframe='1h' "
    "ORDER BY ts_ms"
).fetchall()
closed = [r for r in rows if r[0] + step <= now]
tip = closed[-1]
tip50 = closed[-50:]
blob = "".join(f"{r[0]}|{r[1]}|{r[2]}|{r[3]}|{r[4]}\n" for r in tip50).encode()
print(json.dumps({
    "source": "shared_candles",
    "tip_ts_ms": tip[0],
    "tip_ohlc": [float(x) for x in tip[1:]],
    "tip50_sha256": hashlib.sha256(blob).hexdigest(),
    "n_closed": len(closed),
    "max_raw_ts": rows[-1][0] if rows else None,
}))
"""
    # write via python on remote without shell quoting hell
    helper = ROOT / "artifacts" / "reports" / "_x9_remote_tip.py"
    helper.write_text(remote, encoding="utf-8", newline="\n")
    subprocess.check_call(
        ["scp", "-o", "BatchMode=yes", str(helper), f"root@{HOST}:/tmp/_x9_remote_tip.py"]
    )
    raw = _ssh("sed -i 's/\\r$//' /tmp/_x9_remote_tip.py; python3 /tmp/_x9_remote_tip.py")
    line = [ln for ln in raw.splitlines() if ln.strip().startswith("{")][-1]
    return json.loads(line)


def warehouse_tip_1h() -> dict:
    """Research warehouse tip for closed 1h ETHUSDT last_price series."""
    # Prefer market_ohlcv via loader (canonical path) and also raw sqlite if available.
    ohlcv = load_ohlcv("ETHUSDT", "1h")
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    step = 3_600_000
    if "ts_ms" in ohlcv.columns:
        ts = ohlcv["ts_ms"].astype(np.int64).to_numpy()
    else:
        ts = index_to_ms(ohlcv.index)
    closed_mask = ts + step <= now_ms
    closed = ohlcv.loc[closed_mask].copy()
    if closed.empty:
        raise RuntimeError("warehouse has no closed 1h bars")
    last = closed.iloc[-1]
    last_ts = int(ts[closed_mask][-1])
    tip50 = closed.iloc[-50:]
    if "ts_ms" in tip50.columns:
        t50 = tip50["ts_ms"].astype(np.int64).to_numpy()
    else:
        t50 = index_to_ms(tip50.index)
    o = tip50["open"].to_numpy(dtype=float)
    h = tip50["high"].to_numpy(dtype=float)
    l = tip50["low"].to_numpy(dtype=float)
    c = tip50["close"].to_numpy(dtype=float)
    blob = "".join(f"{int(t)}|{oo}|{hh}|{ll}|{cc}\n" for t, oo, hh, ll, cc in zip(t50, o, h, l, c)).encode()
    return {
        "source": "research_market_ohlcv",
        "tip_ts_ms": last_ts,
        "tip_ohlc": [
            float(last["open"]),
            float(last["high"]),
            float(last["low"]),
            float(last["close"]),
        ],
        "tip50_sha256": hashlib.sha256(blob).hexdigest(),
        "n_closed": int(len(closed)),
    }


def rebuild_warehouse_preds(cols: list[str], symbol: str, timeframe: str):
    clear_indicator_cache()
    ohlcv = load_ohlcv(symbol, timeframe)
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    feats = build_space(
        ohlcv,
        "structure_v1",
        symbol=symbol,
        timeframe=timeframe,
        recent_only=False,
    )
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    for c in feats.columns:
        if str(c).startswith("last_retrace_pct_"):
            feats[c] = feats[c].fillna(0.0)
    # Do NOT zero-fill real structure columns — that invents swings and false pred drift.
    aligned = feats.dropna()
    X = aligned.to_numpy(dtype=float)
    feat_ts = index_to_ms(pd.DatetimeIndex(aligned.index))
    return aligned, feat_ts, X


def column_diff(snap: dict, row: pd.Series, cols: list[str], eps: float) -> list[dict]:
    out = []
    for c in cols:
        if c not in snap:
            continue
        try:
            a = float(snap[c])
            b = float(row[c]) if pd.notna(row[c]) else float("nan")
            if not (np.isfinite(a) and np.isfinite(b)):
                if snap[c] != row[c]:
                    out.append({"col": c, "live": snap[c], "warehouse": None if pd.isna(row[c]) else row[c]})
                continue
            d = abs(a - b)
            if d > eps:
                out.append(
                    {
                        "col": c,
                        "live": a,
                        "warehouse": b,
                        "abs": d,
                        "rel": d / max(abs(b), 1e-12),
                    }
                )
        except (TypeError, ValueError):
            if snap[c] != row[c]:
                out.append({"col": c, "live": snap[c], "warehouse": row[c]})
    out.sort(key=lambda x: float(x.get("abs") or 0), reverse=True)
    return out


def main() -> int:
    # 1) scp ledger
    subprocess.check_call(
        [
            "scp",
            "-o",
            "BatchMode=yes",
            f"root@{HOST}:{UNIT_ROOT}/state/micro_live_state.sqlite",
            str(LEDGER_LOCAL),
        ]
    )

    shared = fetch_shared_tip()
    wh_tip = warehouse_tip_1h()
    candle_ok = (
        shared["tip_ts_ms"] == wh_tip["tip_ts_ms"]
        and shared["tip_ohlc"] == wh_tip["tip_ohlc"]
        and shared["tip50_sha256"] == wh_tip["tip50_sha256"]
    )
    candle = {
        "ok": candle_ok,
        "shared": shared,
        "warehouse": wh_tip,
        "tip_ts_match": shared["tip_ts_ms"] == wh_tip["tip_ts_ms"],
        "tip_ohlc_match": shared["tip_ohlc"] == wh_tip["tip_ohlc"],
        "tip50_sha_match": shared["tip50_sha256"] == wh_tip["tip50_sha256"],
        "ohlc_abs_diffs": [
            abs(float(a) - float(b))
            for a, b in zip(shared["tip_ohlc"], wh_tip["tip_ohlc"])
        ]
        if shared["tip_ts_ms"] == wh_tip["tip_ts_ms"]
        else None,
    }

    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(PACK / "model.joblib")
    cols = list(blob.get("feature_columns") or strategy.get("feature_columns") or [])
    symbol = str(strategy.get("symbol") or "ETHUSDT").upper()
    timeframe = str(strategy.get("timeframe") or "1h")
    family = target_family(str(strategy.get("target") or "direction"))
    edge = float(strategy.get("min_edge") or DIRECTION_BAND)
    if abs(edge - ROUND_TRIP_COST) < 1e-12:
        edge = DIRECTION_BAND
    lookback = int((strategy.get("multitrade") or {}).get("mean_lookback") or 168)

    con = sqlite3.connect(f"file:{LEDGER_LOCAL}?mode=ro", uri=True)
    decisions = con.execute(
        "SELECT bar_ts_ms, decided_utc, side, pred_mean, mark, mode, detail "
        "FROM decisions ORDER BY bar_ts_ms"
    ).fetchall()
    states = dict(con.execute("SELECT key, value FROM state").fetchall())
    con.close()

    try:
        strength_hist = [float(x) for x in json.loads(states.get("strength_hist_json") or "[]")]
    except Exception as exc:  # noqa: BLE001
        strength_hist = []
        strength_err = str(exc)
    else:
        strength_err = None

    aligned, feat_ts, X_all = rebuild_warehouse_preds(cols, symbol, timeframe)
    ts_to_i = {int(t): i for i, t in enumerate(feat_ts)}
    means_all = np.asarray(
        blob["model"].predict(X_all).mean
        if hasattr(blob["model"].predict(X_all), "mean")
        else blob["model"].predict(X_all),
        dtype=float,
    ).reshape(-1)
    # call predict once only
    pred_raw = blob["model"].predict(X_all)
    means_all = np.asarray(
        pred_raw.mean if hasattr(pred_raw, "mean") else pred_raw, dtype=float
    ).reshape(-1)

    comparisons: list[dict] = []
    drift_feature_tables: dict[str, list] = {}
    gate_skips: dict[str, int] = {}
    snap_model_ok = 0
    snap_model_n = 0

    for bar_ts_ms, decided_utc, side, pred_mean, mark, mode, detail in decisions:
        try:
            det = json.loads(detail) if isinstance(detail, str) else (detail or {})
        except Exception:  # noqa: BLE001
            det = {}
        skip = det.get("skip_reason") or (det.get("multitrade_gate") or {}).get("skip_reason")
        gate_skips[str(skip or "none")] = gate_skips.get(str(skip or "none"), 0) + 1

        snap = (det.get("feature_snapshot") or {}).get("values")
        live_pred = float(pred_mean) if pred_mean is not None else float("nan")
        live_side = int(side) if side is not None else None

        # model integrity from snapshot
        snap_replay = None
        if snap:
            snap_model_n += 1
            X = np.array([[float(snap[c]) for c in cols]], dtype=float)
            pr = blob["model"].predict(X)
            m_snap = float(np.asarray(pr.mean if hasattr(pr, "mean") else pr).reshape(-1)[0])
            d_snap = abs(m_snap - live_pred) if np.isfinite(live_pred) else float("nan")
            snap_replay = {
                "pred_from_snapshot": m_snap,
                "abs_diff_vs_live": d_snap,
                "ok": bool(np.isfinite(d_snap) and d_snap < ABS_EPS),
            }
            if snap_replay["ok"]:
                snap_model_ok += 1

        i = ts_to_i.get(int(bar_ts_ms))
        if i is None:
            comparisons.append(
                {
                    "bar_ts_ms": int(bar_ts_ms),
                    "error": "bar_missing_in_warehouse",
                    "live_pred_mean": live_pred,
                    "live_side": live_side,
                    "skip_reason": skip,
                    "snapshot_model_replay": snap_replay,
                }
            )
            continue

        wh_mean = float(means_all[i])
        wh_side = int(proxy_side(np.asarray([wh_mean]), family)[0])
        if abs(wh_mean) < edge:
            wh_side = 0
        abs_diff = abs(wh_mean - live_pred) if np.isfinite(live_pred) else float("nan")
        mism = column_diff(snap, aligned.iloc[i], cols, FEAT_EPS) if snap else []
        bar_key = pd.to_datetime(int(bar_ts_ms), unit="ms", utc=True).isoformat()
        if mism and (not np.isfinite(abs_diff) or abs_diff > PRED_DRIFT_EPS):
            drift_feature_tables[bar_key] = mism

        comparisons.append(
            {
                "bar_ts_ms": int(bar_ts_ms),
                "bar_utc": bar_key,
                "decided_utc": decided_utc,
                "live_pred_mean": live_pred if np.isfinite(live_pred) else None,
                "live_side": live_side,
                "warehouse_pred_mean": wh_mean,
                "warehouse_side": wh_side,
                "abs_diff": abs_diff if np.isfinite(abs_diff) else None,
                "pred_match_1e6": bool(np.isfinite(abs_diff) and abs_diff < ABS_EPS),
                "pred_close_1e4": bool(np.isfinite(abs_diff) and abs_diff < PRED_DRIFT_EPS),
                "side_match": live_side == wh_side,
                "mark": mark,
                "mode": mode,
                "skip_reason": skip,
                "gate_allow": (det.get("multitrade_gate") or {}).get("allow"),
                "snapshot_model_replay": snap_replay,
                "feature_snapshot": {
                    "present": bool(snap),
                    "n_mismatch": len(mism),
                    "max_abs": max((float(m["abs"]) for m in mism if "abs" in m), default=0.0),
                    "top": mism[:12],
                    "ok": len(mism) == 0,
                },
            }
        )

    scored = [c for c in comparisons if c.get("live_pred_mean") is not None]
    n_scored = len(scored)
    n_side = sum(1 for c in scored if c.get("side_match"))
    n_pred = sum(1 for c in scored if c.get("pred_match_1e6"))
    n_pred_loose = sum(1 for c in scored if c.get("pred_close_1e4"))

    structure_first = (
        "ok"
        if n_scored and n_side == n_scored and n_pred == n_scored
        else (
            "PARTIAL_TIP_DRIFT"
            if n_scored and n_pred_loose < n_scored
            else ("OK_LOOSE" if n_scored and n_side == n_scored else "STRUCTURE_OR_PRED_DRIFT")
        )
    )
    if n_scored and n_side == n_scored and n_pred == n_scored:
        structure_first = "ok"

    report = {
        "evidence_class": "LIVE_WAREHOUSE_FULL_PARITY_BUNDLE_XXOBSTER9",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "account": "Xxobster9",
        "host": HOST,
        "service": "llm2-structure-eth-multitrade-p75-v1",
        "n_decisions_total": len(comparisons),
        "n_scored_decisions": n_scored,
        "candles_shared_vs_warehouse": candle,
        "strength_hist": {
            "n": len(strength_hist),
            "target_lookback": lookback,
            "fraction_of_target": len(strength_hist) / lookback if lookback else None,
            "min": float(min(strength_hist)) if strength_hist else None,
            "max": float(max(strength_hist)) if strength_hist else None,
            "mean": float(np.mean(strength_hist)) if strength_hist else None,
            "values": strength_hist,
            "error": strength_err,
            "note": "Score buffer only; warm-up until n≈168 (~1 week of eligible candidates).",
        },
        "model_from_snapshot_integrity": {
            "n": snap_model_n,
            "exact_match": snap_model_ok,
            "ok_rate": (snap_model_ok / snap_model_n) if snap_model_n else None,
            "note": "Live pred is fully determined by stored feature_snapshot + frozen model.",
        },
        "headline": {
            "structure_first": structure_first,
            "side_match_rate_scored": (n_side / n_scored) if n_scored else None,
            "pred_exact_rate_scored": (n_pred / n_scored) if n_scored else None,
            "pred_close_1e4_rate_scored": (n_pred_loose / n_scored) if n_scored else None,
            "max_abs_pred_diff_scored": max(
                (float(c["abs_diff"]) for c in scored if c.get("abs_diff") is not None),
                default=None,
            ),
        },
        "gate_skip_counts_live": gate_skips,
        "feature_column_diffs_on_drift_bars": drift_feature_tables,
        "comparisons": comparisons,
        "actions": {
            "candle_tip": "PASS" if candle_ok else "REFRESH_WAREHOUSE_OR_CHECK_SHARED",
            "strength_hist": (
                "WARMUP"
                if len(strength_hist) < lookback
                else "FULL"
            ),
            "structure": structure_first,
            "do_not_retune_p75": True,
        },
        "note": (
            "Diagnostic only. Prefer warehouse gold. 800-bar rebuild forbidden. "
            "Do not retune strength_quantile from this window."
        ),
    }
    OUT.write_text(json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8")
    # also update thin latest pointer
    (ARTIFACTS / "reports" / "x9_live_warehouse_parity_latest.json").write_text(
        json.dumps(report, indent=2, default=str) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "out": str(OUT),
                "headline": report["headline"],
                "candles_ok": candle_ok,
                "strength_n": len(strength_hist),
                "gate_skips": gate_skips,
                "n_scored": n_scored,
                "n_total": len(comparisons),
                "model_snapshot_ok_rate": report["model_from_snapshot_integrity"]["ok_rate"],
                "drift_bars": list(drift_feature_tables.keys()),
                "actions": report["actions"],
            },
            indent=2,
            default=str,
        ),
        flush=True,
    )
    print("--- bars ---", flush=True)
    for c in comparisons:
        if "error" in c:
            print(c.get("bar_ts_ms"), "ERR", c["error"], "live", c.get("live_pred_mean"), flush=True)
            continue
        print(
            f"{c['bar_utc']} live={c.get('live_pred_mean')} wh={c.get('warehouse_pred_mean'):+.6f} "
            f"d={c.get('abs_diff')} side {c.get('live_side')}/{c.get('warehouse_side')} "
            f"snap_mis={c['feature_snapshot']['n_mismatch']} skip={c.get('skip_reason')} "
            f"model_snap={c.get('snapshot_model_replay')}",
            flush=True,
        )
    return 0 if structure_first in {"ok", "OK_LOOSE", "WARMUP"} and candle_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
