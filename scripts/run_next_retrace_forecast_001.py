"""Stage-1 next-leg retrace forecast + optional Stage-2 filter + multi-task arm.

Generation: structure_v1_next_retrace_forecast_001
Preregister BEFORE any outer-OOS view. Forecast skill and trade PF are separate gates.
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
for _p in (
    Path(r"C:\projects\botsgeneral\packages\leakage\src"),
    Path(r"C:\projects\botsgeneral\packages\indicators\src"),
    Path(r"C:\projects\botsgeneral\packages\tradesim\src"),
):
    if _p.is_dir() and str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.evidence.four_proof import (  # noqa: E402
    refuse_warehouse_leakage_pass_alone,
    require_four_proof_ok,
    run_four_proof_gate,
)
from llm2.features.registry import build_space  # noqa: E402
from llm2.hunt.runner import _make_model  # noqa: E402
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.labels.next_retrace import build_next_retrace_sparse_frame  # noqa: E402
from llm2.labels.next_vol import build_next_vol_labels  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, ROUND_TRIP_COST  # noqa: E402
from llm2.registry.ledger import append_ledger  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    index_to_ms,
)

PREREG = _ROOT / "configs" / "preregister" / "structure_v1_next_retrace_forecast_001.yaml"
SYMBOLS = ("ETHUSDT", "BTCUSDT", "SOLUSDT")
TF = "1h"
SPACE = "structure_v1"
SEED = 20260806
MODELS = ("hist_mean", "ridge", "lgbm_regressor")
# Stage-1 skill hurdle (preregistered)
IC_MIN = 0.05
IC_POS_FRAC = 0.66
ACC_MIN = 0.55
DEEP_THRESH = 0.5  # retrace >= 0.5 = "deep"


@dataclass
class FoldScore:
    fold: int
    n: int
    spearman_ic: float
    mae: float
    deep_shallow_acc: float
    r2: float


def _hash_prereg() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def _annotate_prereg(sha: str) -> None:
    text = PREREG.read_text(encoding="utf-8")
    if "preregister_sha256_at_run:" in text:
        return
    PREREG.write_text(
        text.rstrip()
        + f"\n\npreregister_sha256_at_run: {sha}\n"
        + f"run_started_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n",
        encoding="utf-8",
    )


def _outer_masks(ts_ms: np.ndarray) -> list[tuple[int, np.ndarray, np.ndarray]]:
    """Return (fold_i, train_mask, test_mask) for each outer fold."""
    out = []
    for i, (start, end) in enumerate(OUTER_FOLD_RANGES):
        lo = int(pd.Timestamp(start, tz="UTC").value // 1_000_000)
        hi = int(pd.Timestamp(end, tz="UTC").value // 1_000_000)
        test = (ts_ms >= lo) & (ts_ms < hi)
        train = ts_ms < lo
        if int(test.sum()) < 20 or int(train.sum()) < 50:
            continue
        out.append((i, train, test))
    return out


def _metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    m = np.isfinite(y_true) & np.isfinite(y_pred)
    yt, yp = y_true[m], y_pred[m]
    if len(yt) < 10:
        return {
            "n": float(len(yt)),
            "spearman_ic": float("nan"),
            "mae": float("nan"),
            "deep_shallow_acc": float("nan"),
            "r2": float("nan"),
        }
    if float(np.std(yp)) < 1e-12 or float(np.std(yt)) < 1e-12:
        ic = float("nan")
    else:
        ic = float(stats.spearmanr(yt, yp).statistic)
    mae = float(np.mean(np.abs(yt - yp)))
    deep_t = yt >= DEEP_THRESH
    deep_p = yp >= DEEP_THRESH
    acc = float(np.mean(deep_t == deep_p))
    ss_res = float(np.sum((yt - yp) ** 2))
    ss_tot = float(np.sum((yt - np.mean(yt)) ** 2))
    r2 = float("nan") if ss_tot <= 0 else 1.0 - ss_res / ss_tot
    return {
        "n": float(len(yt)),
        "spearman_ic": ic,
        "mae": mae,
        "deep_shallow_acc": acc,
        "r2": r2,
    }


def _fit_predict(
    model_name: str,
    X_tr: np.ndarray,
    y_tr: np.ndarray,
    X_te: np.ndarray,
) -> np.ndarray:
    model = _make_model(model_name)
    model.fit(X_tr, y_tr)
    pred = model.predict(X_te)
    return np.asarray(pred.mean if hasattr(pred, "mean") else pred, dtype=float).reshape(-1)


def stage1_symbol(symbol: str, *, four_proof: dict | None) -> dict:
    ohlcv = load_ohlcv(symbol, TF)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    sparse = build_next_retrace_sparse_frame(symbol, TF)
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TF)
    # Align features to sparse decision times (as-of: last feature row at/before decision).
    feat_ms = index_to_ms(feats.index)
    dec_ms = sparse["decision_ts_ms"].to_numpy(dtype=np.int64)
    cols = list(feats.columns)
    feat_vals = feats.to_numpy(dtype=float)
    j = np.searchsorted(feat_ms, dec_ms, side="right") - 1
    ok = j >= 0
    j_ok = j[ok]
    X_all = feat_vals[j_ok]
    finite = np.all(np.isfinite(X_all), axis=1)
    idx = np.flatnonzero(ok)[finite]
    data = pd.DataFrame(X_all[finite], columns=cols)
    data["next_retrace_pct"] = sparse["next_retrace_pct"].to_numpy(dtype=float)[idx]
    data["leg_dir"] = sparse["leg_dir"].to_numpy(dtype=float)[idx]
    data["decision_ts_ms"] = dec_ms[idx]
    data["known_ts_ms"] = sparse["known_ts_ms"].to_numpy(dtype=np.int64)[idx]
    if len(data) < 200:
        return {"symbol": symbol, "status": "INSUFFICIENT", "n": len(data)}

    X_cols = list(cols)
    X = data[X_cols].to_numpy(dtype=float)
    y = data["next_retrace_pct"].to_numpy(dtype=float)
    ts = data["decision_ts_ms"].to_numpy(dtype=np.int64)
    leg_dir = data["leg_dir"].to_numpy(dtype=float)

    model_rows = []
    best = None
    for mi, model_name in enumerate(MODELS):
        fold_scores: list[dict] = []
        oos_pred = np.full(len(y), np.nan)
        for fold_i, tr, te in _outer_masks(ts):
            # Purge: drop train rows whose label realizes inside/after test start.
            te_start = int(ts[te].min()) if te.any() else 0
            known = data["known_ts_ms"].to_numpy(dtype=np.int64)
            tr_use = tr & (known < te_start)
            if int(tr_use.sum()) < 40 or int(te.sum()) < 15:
                continue
            yp = _fit_predict(model_name, X[tr_use], y[tr_use], X[te])
            oos_pred[te] = yp
            m = _metrics(y[te], yp)
            m["fold"] = fold_i
            fold_scores.append(m)
        if not fold_scores:
            continue
        ics = [f["spearman_ic"] for f in fold_scores if np.isfinite(f["spearman_ic"])]
        accs = [f["deep_shallow_acc"] for f in fold_scores if np.isfinite(f["deep_shallow_acc"])]
        summary = {
            "model": model_name,
            "n_folds": len(fold_scores),
            "mean_spearman_ic": float(np.mean(ics)) if ics else float("nan"),
            "frac_folds_ic_positive": float(np.mean(np.asarray(ics) > 0)) if ics else 0.0,
            "mean_deep_shallow_acc": float(np.mean(accs)) if accs else float("nan"),
            "mean_mae": float(np.nanmean([f["mae"] for f in fold_scores])),
            "mean_r2": float(np.nanmean([f["r2"] for f in fold_scores])),
            "folds": fold_scores,
            "n_samples": int(len(y)),
        }
        summary["stage1_hurdle_pass"] = bool(
            np.isfinite(summary["mean_spearman_ic"])
            and summary["mean_spearman_ic"] >= IC_MIN
            and summary["frac_folds_ic_positive"] >= IC_POS_FRAC
            and np.isfinite(summary["mean_deep_shallow_acc"])
            and summary["mean_deep_shallow_acc"] >= ACC_MIN
        )
        model_rows.append(summary)
        blob = {**summary, "oos_pred": oos_pred, "leg_dir": leg_dir, "y": y, "ts": ts}
        # Select by IC; hurdle is a separate boolean (not used for ranking).
        if best is None or (
            np.nan_to_num(summary["mean_spearman_ic"], nan=-np.inf)
            > np.nan_to_num(best["mean_spearman_ic"], nan=-np.inf)
        ):
            best = blob

    return {
        "symbol": symbol,
        "status": "OK",
        "four_proof_ok": None if four_proof is None else bool(four_proof.get("ok")),
        "models": [{k: v for k, v in m.items() if k != "folds"} | {"folds": m["folds"]} for m in model_rows],
        "best_model": None
        if best is None
        else {k: best[k] for k in best if k not in {"oos_pred", "leg_dir", "y", "ts"}},
        "_best_blob": best,
        "X_cols": X_cols,
        "n_legs": int(len(data)),
    }


def stage2_simple_trade(symbol: str, stage1: dict) -> dict:
    """Continuation/fade rule from predicted retrace — reported separately from skill."""
    blob = stage1.get("_best_blob")
    if blob is None:
        return {"symbol": symbol, "status": "NO_MODEL"}
    if not stage1.get("best_model", {}).get("stage1_hurdle_pass"):
        return {
            "symbol": symbol,
            "status": "SKIPPED_STAGE1_HURDLE_FAIL",
            "note": "Stage-2 only runs if Stage-1 skill hurdle passes (preregistered).",
        }

    from tradesim import (
        Side,
        Signal,
        research_instrument,
        research_margin,
        research_sizing,
    )

    from llm2.backtest.run import run_strategy_backtest
    from llm2.gates.evidence import leverage_from_stop, research_costs_baseline

    ohlcv = load_ohlcv(symbol, TF)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    pred = np.asarray(blob["oos_pred"], dtype=float)
    leg_dir = np.asarray(blob["leg_dir"], dtype=float)
    ts = np.asarray(blob["ts"], dtype=np.int64)
    # score > 0 → long: after up-leg, shallow retrace (continuation); after down-leg, deep retrace (bounce)
    score = leg_dir * (DEEP_THRESH - pred)
    bar_ms = index_to_ms(ohlcv.index)
    valid = np.isfinite(score) & (np.abs(score) >= 0.05)
    ts_v = ts[valid]
    score_v = score[valid]
    # Map each decision to the last bar at/before decision (vectorized).
    j = np.searchsorted(bar_ms, ts_v, side="right") - 1
    keep = j >= 0
    ts_use = bar_ms[j[keep]]
    score_use = score_v[keep]
    signals = [
        Signal(
            ts_ms=int(t_use),
            side=Side.LONG if float(s) > 0 else Side.SHORT,
            stop_offset=0.02,
            target_offset=0.01,
            max_hold_bars=6,
            tag="next_retrace_filter",
            meta={"score": float(s)},
        )
        for t_use, s in zip(ts_use, score_use)
    ]
    if len(signals) < 30:
        return {"symbol": symbol, "status": "TOO_FEW_SIGNALS", "n_signals": len(signals)}

    sl = 0.02
    lev = leverage_from_stop(sl)
    try:
        bundle = run_strategy_backtest(
            ohlcv,
            signals,
            symbol=symbol,
            timeframe=TF,
            strategy_id=f"next_retrace_filter_{symbol.lower()}",
            strategy_meta={
                "name": "next_retrace_filter_stage2",
                "symbol": symbol,
                "tp_pct": 0.01,
                "sl_pct": sl,
            },
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            instrument=research_instrument(symbol),
            plot=False,
            print_headline=False,
            store_path=None,
        )
    except Exception as exc:  # noqa: BLE001
        return {"symbol": symbol, "status": "BT_ERROR", "error": str(exc)[:400]}
    m = bundle.metrics
    return {
        "symbol": symbol,
        "status": "RAN",
        "n_signals": len(signals),
        "metrics": {
            "n_trades": int(m.n_trades),
            "profit_factor": float(m.profit_factor),
            "net_pnl": float(m.net_pnl),
            "win_rate": float(getattr(m, "win_rate", float("nan"))),
        },
        "note": "Diagnostic trade rule only — not a readiness claim. Skill gate is Stage-1.",
    }


def _multitask_eval(
    *,
    model_name: str,
    X: np.ndarray,
    y: np.ndarray,
    tsm: np.ndarray,
    known: np.ndarray | None,
    embargo_ms: int,
) -> dict:
    fold_ics: list[float] = []
    for _fold_i, tr, te in _outer_masks(tsm):
        if int(te.sum()) < 15:
            continue
        te_start = int(tsm[te].min()) if te.any() else 0
        if known is not None:
            tr_use = tr & (known < te_start)
        else:
            tr_use = tr & (tsm < te_start - int(embargo_ms))
        if int(tr_use.sum()) < 40:
            continue
        yp = _fit_predict(model_name, X[tr_use], y[tr_use], X[te])
        m = _metrics(y[te], yp)
        if np.isfinite(m["spearman_ic"]):
            fold_ics.append(float(m["spearman_ic"]))
    return {
        "n": int(len(y)),
        "mean_spearman_ic": float(np.mean(fold_ics)) if fold_ics else float("nan"),
        "frac_folds_ic_positive": float(np.mean(np.asarray(fold_ics) > 0)) if fold_ics else 0.0,
        "n_folds": len(fold_ics),
    }


def multitask_symbol(symbol: str) -> dict:
    """Parallel arm: separate heads on {fwd_return, next_retrace, next_vol}."""
    ohlcv = load_ohlcv(symbol, TF)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TF)
    y_ret = build_fwd_return_labels(ohlcv, horizon=6)["fwd_return"]
    y_vol = build_next_vol_labels(ohlcv, horizon=24)
    sparse = build_next_retrace_sparse_frame(symbol, TF)

    aligned = feats.join(y_ret.rename("fwd_return"), how="inner")
    aligned = aligned.join(y_vol.rename("next_vol"), how="left")
    aligned = aligned.replace([np.inf, -np.inf], np.nan)

    # Sparse next_retrace at leg confirm (same geometry as Stage-1).
    feat_ms = index_to_ms(feats.index)
    dec_ms = sparse["decision_ts_ms"].to_numpy(dtype=np.int64)
    j = np.searchsorted(feat_ms, dec_ms, side="right") - 1
    ok = j >= 0
    X_sp = feats.to_numpy(dtype=float)[j[ok]]
    finite = np.all(np.isfinite(X_sp), axis=1)
    idx = np.flatnonzero(ok)[finite]
    X_sp = X_sp[finite]
    y_sp = sparse["next_retrace_pct"].to_numpy(dtype=float)[idx]
    known_sp = sparse["known_ts_ms"].to_numpy(dtype=np.int64)[idx]
    ts_sp = dec_ms[idx]

    models = ("lgbm_regressor",)
    try:
        _make_model("torch_mlp")
        models = ("lgbm_regressor", "torch_mlp")
    except Exception:  # noqa: BLE001
        pass

    X_cols = list(feats.columns)
    out_models = []
    for model_name in models:
        per_target: dict = {}
        # Dense heads
        for tgt, embargo_h in (("fwd_return", 6), ("next_vol", 24)):
            sub = aligned.dropna(subset=X_cols + [tgt])
            if len(sub) < 500:
                per_target[tgt] = {"status": "INSUFFICIENT", "n": len(sub)}
                continue
            per_target[tgt] = _multitask_eval(
                model_name=model_name,
                X=sub[X_cols].to_numpy(dtype=float),
                y=sub[tgt].to_numpy(dtype=float),
                tsm=index_to_ms(sub.index),
                known=None,
                embargo_ms=embargo_h * 3_600_000,
            )
        # Sparse next_retrace head
        if len(y_sp) < 200:
            per_target["next_retrace_pct"] = {"status": "INSUFFICIENT", "n": int(len(y_sp))}
        else:
            per_target["next_retrace_pct"] = _multitask_eval(
                model_name=model_name,
                X=X_sp,
                y=y_sp,
                tsm=ts_sp,
                known=known_sp,
                embargo_ms=0,
            )
            per_target["next_retrace_pct"]["sample"] = "sparse_at_leg_confirm"
        out_models.append({"model": model_name, "targets": per_target})
    return {"symbol": symbol, "models": out_models, "n_sparse_legs": int(len(sparse))}


def main() -> int:
    if not PREREG.is_file():
        raise SystemExit(f"missing {PREREG}")
    sha = _hash_prereg()
    _annotate_prereg(sha)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    append_ledger(
        f"NEXT_RETRACE_FORECAST_001 start sha={sha[:16]} fold={FOLD_GEOMETRY_VERSION}",
        tier=0,
    )
    print(f"preregister_sha256={sha}", flush=True)

    # Four-proof once on ETH (canonical), on the pre-lockbox research window tip.
    # Refuse train if fail. Live tip warehouse freshness is a separate ops concern.
    print("FOUR_PROOF ETHUSDT (pre-lockbox) …", flush=True)
    ohlcv_eth = load_ohlcv("ETHUSDT", TF)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv_eth = ohlcv_eth.loc[index_to_ms(ohlcv_eth.index) < lock_ms].copy()
    fp = run_four_proof_gate(
        space=SPACE, symbol="ETHUSDT", timeframe=TF, ohlcv=ohlcv_eth
    )
    refuse_warehouse_leakage_pass_alone(
        space=SPACE, leakage_passed=True, four_proof_ok=bool(fp.get("ok"))
    )
    require_four_proof_ok(fp)
    print(f"FOUR_PROOF PASS artifacts={fp.get('artifact_dir')}", flush=True)

    stage1_rows = []
    stage2_rows = []
    for sym in SYMBOLS:
        print(f"STAGE1 {sym} …", flush=True)
        s1 = stage1_symbol(sym, four_proof=fp)
        # Drop heavy blob from JSON later
        stage1_rows.append(s1)
        best = s1.get("best_model") or {}
        print(
            f"  best={best.get('model')} ic={best.get('mean_spearman_ic')} "
            f"acc={best.get('mean_deep_shallow_acc')} hurdle={best.get('stage1_hurdle_pass')}",
            flush=True,
        )
        print(f"STAGE2 {sym} …", flush=True)
        s2 = stage2_simple_trade(sym, s1)
        stage2_rows.append(s2)
        print(f"  stage2={s2.get('status')} {s2.get('metrics') or s2.get('note')}", flush=True)

    print("MULTITASK …", flush=True)
    mt_rows = []
    for sym in SYMBOLS:
        mt = multitask_symbol(sym)
        mt_rows.append(mt)
        print(f"  {sym} {json.dumps(mt['models'], default=str)[:240]}", flush=True)

    # Diagnostic ablation (not a selection step): skill without fib_position*.
    print("ABLATION drop fib_position* on ETH …", flush=True)
    ablation = {"note": "diagnostic only; does not change selection", "ETHUSDT": {}}
    try:
        s1_eth = next(s for s in stage1_rows if s.get("symbol") == "ETHUSDT")
        # Re-score ridge on features excluding fib_position*
        ohlcv = load_ohlcv("ETHUSDT", TF)
        lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
        ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
        sparse = build_next_retrace_sparse_frame("ETHUSDT", TF)
        feats = build_space(ohlcv, SPACE, symbol="ETHUSDT", timeframe=TF)
        keep = [c for c in feats.columns if "fib_position" not in c]
        feat_ms = index_to_ms(feats.index)
        dec = sparse["decision_ts_ms"].to_numpy(dtype=np.int64)
        j = np.searchsorted(feat_ms, dec, side="right") - 1
        ok = j >= 0
        X = feats[keep].to_numpy(dtype=float)[j[ok]]
        y = sparse["next_retrace_pct"].to_numpy(dtype=float)[ok]
        known = sparse["known_ts_ms"].to_numpy(dtype=np.int64)[ok]
        ts = dec[ok]
        finite = np.all(np.isfinite(X), axis=1)
        X, y, known, ts = X[finite], y[finite], known[finite], ts[finite]
        ics = []
        for fold_i, tr, te in _outer_masks(ts):
            te_start = int(ts[te].min()) if te.any() else 0
            tr_use = tr & (known < te_start)
            if int(tr_use.sum()) < 40 or int(te.sum()) < 15:
                continue
            yp = _fit_predict("ridge", X[tr_use], y[tr_use], X[te])
            m = _metrics(y[te], yp)
            if np.isfinite(m["spearman_ic"]):
                ics.append(m["spearman_ic"])
        ablation["ETHUSDT"] = {
            "model": "ridge",
            "dropped": "fib_position*",
            "n_cols": len(keep),
            "mean_spearman_ic": float(np.mean(ics)) if ics else float("nan"),
            "n_folds": len(ics),
            "full_space_ic": (s1_eth.get("best_model") or {}).get("mean_spearman_ic"),
        }
        print(f"  ablation IC={ablation['ETHUSDT']['mean_spearman_ic']}", flush=True)
    except Exception as exc:  # noqa: BLE001
        ablation["ETHUSDT"] = {"error": str(exc)[:300]}

    # Freeze preregister after OOS viewed
    text = PREREG.read_text(encoding="utf-8")
    if "status: OPEN" in text:
        PREREG.write_text(
            text.replace("status: OPEN", "status: FROZEN_OOS_VIEWED", 1)
            + f"frozen_utc: \"{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\"\n"
            + "frozen_reason: outer-OOS of next_retrace_forecast_001 viewed.\n",
            encoding="utf-8",
        )

    def _strip(s1: dict) -> dict:
        return {k: v for k, v in s1.items() if k != "_best_blob"}

    report = {
        "generation_id": "structure_v1_next_retrace_forecast_001",
        "stamp": stamp,
        "preregister_sha256": sha,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "four_proof": {
            "ok": fp.get("ok"),
            "artifact_dir": fp.get("artifact_dir"),
            "artifact_hashes": fp.get("artifact_hashes"),
            "proofs_ok": fp.get("proofs_ok"),
        },
        "stage1_skill_hurdle": {
            "mean_spearman_ic": IC_MIN,
            "frac_folds_ic_positive": IC_POS_FRAC,
            "deep_shallow_acc": ACC_MIN,
        },
        "stage1": [_strip(s) for s in stage1_rows],
        "stage2_trade_rule": stage2_rows,
        "multitask_arm": mt_rows,
        "ablation_drop_fib_position": ablation,
        "readiness_max": "RESEARCH_ONLY",
        "stage1_hurdle_any_pass": any(
            bool((s.get("best_model") or {}).get("stage1_hurdle_pass")) for s in stage1_rows
        ),
        "stage2_trade_pf_any_ge_1": any(
            float((s.get("metrics") or {}).get("profit_factor") or 0) >= 1.0
            for s in stage2_rows
            if s.get("status") == "RAN"
        ),
        "note": (
            "Forecast skill and trade Profit Factor are separate gates. "
            "Stage-2 runs only when Stage-1 hurdle passes. "
            "Good R^2 / IC on next_retrace does not authorize live. "
            "No live deploy authorization."
        ),
    }
    out = ARTIFACTS / "reports" / f"structure_v1_next_retrace_forecast_001_{stamp}.json"
    latest = ARTIFACTS / "reports" / "structure_v1_next_retrace_forecast_001_latest.json"
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"WROTE {out}", flush=True)

    # Console summary
    print("\n=== STAGE-1 FORECAST SKILL ===", flush=True)
    for s in report["stage1"]:
        b = s.get("best_model") or {}
        print(
            f"{s['symbol']}: model={b.get('model')} IC={b.get('mean_spearman_ic')} "
            f"acc={b.get('mean_deep_shallow_acc')} hurdle={b.get('stage1_hurdle_pass')}",
            flush=True,
        )
    print("\n=== STAGE-2 TRADE RULE ===", flush=True)
    for s in stage2_rows:
        print(f"{s['symbol']}: {s.get('status')} {s.get('metrics') or s.get('note')}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
