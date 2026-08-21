"""Train proxies for leaky/causal last_retrace_pct; swap into ETHUSDT trade arms.

Phase 1 — reconstruct targets
  y_leaky  = pre-CAUS-STRUCT-001 publish (orange / look-ahead label)
  y_causal = fixed publish (cyan)
  X        = structure_v1 EXCEPT any last_retrace* column (no circular use of the target)

Chronological hyperparameter search on pre-lockbox data; outer recon slice
[2026-01-01, 2026-05-01). Selection uses only validation MAE prior to the outer slice.

Phase 2 — ETHUSDT trade arms (display / RESEARCH_ONLY)
  Replace last_retrace_pct (+ HTF last_retrace_* if present) with proxy fills and run
  the same wall_clock multitrade geometry as the leak diagnostic.

Evidence class: RESEARCH_ONLY / RETRACE_PROXY_EXPERIMENT
Promotion: FORBIDDEN (proxy of contaminated or post-fix features ≠ live pack).
"""

from __future__ import annotations

import itertools
import json
import os
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

os.environ.setdefault("TRADESIM_NO_PLOT", "1")

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

import joblib  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tradesim import (  # noqa: E402
    research_instrument,
    research_margin,
    research_sizing,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.experiments.eth_multitrade_nested import build_multitrade_signals  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import index_to_ms  # noqa: E402

sys.path.insert(0, r"C:\projects\botsgeneral\packages\indicators\src")
from indicators.compute import compute_structure  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
SL = 0.02
BASE_HOLD = 12
HOLD_ADDON = 24
MEAN_LOOKBACK = 168
LABEL_HORIZON = 6
STRENGTH_Q = 0.75
K = 7
FIB = 1.618

# Pre-lockbox chronology (no lockbox used for selection or trade eval).
HUNT_END = "2025-10-01"  # last train+val end exclusive for proxy selection
OUTER_START = "2026-01-01"  # recon + trade outer display
OUTER_END = FORWARD_LOCKBOX_START  # 2026-05-01
VAL_FRAC = 0.20  # trailing 20% of pre-HUNT_END used for param selection

OUT_DIR = ARTIFACTS / "reports" / "last_retrace_proxy_trade_001"
MODEL_DIR = ARTIFACTS / "models" / "last_retrace_proxy_001"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")

RETRACE_PREFIX = "last_retrace"

# Compact LightGBM grid (chronological val MAE selects best).
PARAM_GRID: list[dict[str, Any]] = [
    {"n_estimators": 60, "learning_rate": 0.05, "num_leaves": 15, "min_child_samples": 50, "subsample": 0.8, "colsample_bytree": 0.8},
    {"n_estimators": 100, "learning_rate": 0.05, "num_leaves": 31, "min_child_samples": 40, "subsample": 0.9, "colsample_bytree": 0.9},
    {"n_estimators": 150, "learning_rate": 0.03, "num_leaves": 31, "min_child_samples": 30, "subsample": 0.85, "colsample_bytree": 0.85},
    {"n_estimators": 200, "learning_rate": 0.03, "num_leaves": 63, "min_child_samples": 40, "subsample": 0.8, "colsample_bytree": 0.8},
    {"n_estimators": 120, "learning_rate": 0.07, "num_leaves": 47, "min_child_samples": 25, "subsample": 0.9, "colsample_bytree": 0.7},
    {"n_estimators": 250, "learning_rate": 0.02, "num_leaves": 31, "min_child_samples": 60, "subsample": 0.75, "colsample_bytree": 0.9},
    {"n_estimators": 180, "learning_rate": 0.04, "num_leaves": 23, "min_child_samples": 35, "reg_lambda": 1.0, "subsample": 0.85, "colsample_bytree": 0.85},
    {"n_estimators": 100, "learning_rate": 0.05, "num_leaves": 31, "min_child_samples": 20, "reg_alpha": 0.1, "reg_lambda": 0.5, "subsample": 1.0, "colsample_bytree": 1.0},
]


@dataclass
class ReconScores:
    n: int
    mae: float
    rmse: float
    r2: float
    corr: float
    max_abs: float


def _log(msg: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(msg, flush=True)
    with (OUT_DIR / "run.log").open("a", encoding="utf-8") as fh:
        fh.write(msg + "\n")


def _ohlcv_to_struct_input(ohlcv: pd.DataFrame) -> pd.DataFrame:
    ts = index_to_ms(ohlcv.index)
    return pd.DataFrame(
        {
            "ts_ms": ts,
            "open": ohlcv["open"].to_numpy(dtype=float),
            "high": ohlcv["high"].to_numpy(dtype=float),
            "low": ohlcv["low"].to_numpy(dtype=float),
            "close": ohlcv["close"].to_numpy(dtype=float),
            "volume": ohlcv["volume"].to_numpy(dtype=float)
            if "volume" in ohlcv.columns
            else np.zeros(len(ohlcv)),
        }
    )


def last_retrace_leaky_and_causal(
    ohlcv: pd.DataFrame, *, timeframe: str = TIMEFRAME
) -> pd.DataFrame:
    raw = _ohlcv_to_struct_input(ohlcv)
    bundle = compute_structure(
        raw, source="binance", symbol=SYMBOL, timeframe=timeframe
    )
    ts_ms = raw["ts_ms"].to_numpy(dtype=np.int64)
    n = len(ts_ms)
    legs = bundle.legs
    swings = bundle.swings
    swing_confirm = {s.swing_id: s.confirm_ts_ms for s in swings}
    leaky = np.full(n, np.nan)
    causal = np.full(n, np.nan)
    if legs:
        known_ts = np.asarray(
            [
                max(
                    swing_confirm.get(lg.start_swing_id, lg.end_ts_ms),
                    swing_confirm.get(lg.end_swing_id, lg.end_ts_ms),
                )
                for lg in legs
            ],
            dtype=np.int64,
        )
        order = np.argsort(known_ts, kind="mergesort")
        known_ts = known_ts[order]
        legs_o = [legs[i] for i in order.tolist()]
        retr = np.asarray([lg.retrace_pct for lg in legs_o], dtype=float)
        idx = np.searchsorted(known_ts, ts_ms, side="right") - 1
        ok = idx >= 0
        leaky[ok] = retr[idx[ok]]
        if len(legs_o) >= 2:
            retr_known = known_ts[1:]
            retr_vals = retr[:-1]
            idx_r = np.searchsorted(retr_known, ts_ms, side="right") - 1
            ok_r = idx_r >= 0
            causal[ok_r] = retr_vals[idx_r[ok_r]]
    idx = pd.to_datetime(ts_ms, unit="ms", utc=True)
    return pd.DataFrame({"leaky": leaky, "causal": causal}, index=idx)


def recon_scores(y_true: np.ndarray, y_hat: np.ndarray) -> ReconScores:
    m = np.isfinite(y_true) & np.isfinite(y_hat)
    if m.sum() < 10:
        return ReconScores(0, float("nan"), float("nan"), float("nan"), float("nan"), float("nan"))
    yt, yp = y_true[m], y_hat[m]
    err = yp - yt
    mae = float(np.mean(np.abs(err)))
    rmse = float(np.sqrt(np.mean(err ** 2)))
    ss_res = float(np.sum(err ** 2))
    ss_tot = float(np.sum((yt - yt.mean()) ** 2))
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-18 else float("nan")
    if yt.std() < 1e-12 or yp.std() < 1e-12:
        corr = float("nan")
    else:
        corr = float(np.corrcoef(yt, yp)[0, 1])
    return ReconScores(
        n=int(m.sum()),
        mae=mae,
        rmse=rmse,
        r2=r2,
        corr=corr,
        max_abs=float(np.max(np.abs(err))),
    )


def feature_cols_without_retrace(cols: list[str]) -> list[str]:
    return [c for c in cols if RETRACE_PREFIX not in c]


def retrace_cols(cols: list[str]) -> list[str]:
    return [c for c in cols if RETRACE_PREFIX in c]


def fit_lgbm(X: np.ndarray, y: np.ndarray, params: dict[str, Any]) -> LGBMRegressorPredictor:
    model = LGBMRegressorPredictor(**params)
    model.fit(X, y)
    return model


def predict_arr(model: LGBMRegressorPredictor, X: np.ndarray) -> np.ndarray:
    return np.asarray(model.predict(X).mean, dtype=float).reshape(-1)


def hunt_proxy(
    X: np.ndarray,
    y: np.ndarray,
    ts_ms: np.ndarray,
    *,
    hunt_end_ms: int,
    label: str,
) -> dict[str, Any]:
    """Chronological train/val grid search; refit best on all pre-hunt_end rows."""
    pre = ts_ms < hunt_end_ms
    if pre.sum() < 2000:
        raise RuntimeError(f"{label}: insufficient pre-hunt rows {pre.sum()}")
    pre_idx = np.where(pre)[0]
    n_val = max(200, int(len(pre_idx) * VAL_FRAC))
    val_i = pre_idx[-n_val:]
    tr_i = pre_idx[:-n_val]
    # drop nan y
    def _clean(ix: np.ndarray) -> np.ndarray:
        return ix[np.isfinite(y[ix]) & np.all(np.isfinite(X[ix]), axis=1)]

    tr_i, val_i = _clean(tr_i), _clean(val_i)
    if tr_i.size < 500 or val_i.size < 100:
        raise RuntimeError(f"{label}: clean train/val too small {tr_i.size}/{val_i.size}")

    trials = []
    best = None
    for pi, params in enumerate(PARAM_GRID):
        t0 = time.perf_counter()
        model = fit_lgbm(X[tr_i], y[tr_i], params)
        hat = predict_arr(model, X[val_i])
        sc = recon_scores(y[val_i], hat)
        row = {
            "trial": pi,
            "params": params,
            "val": asdict(sc),
            "elapsed_sec": round(time.perf_counter() - t0, 2),
        }
        trials.append(row)
        _log(
            f"  {label} trial={pi} mae={sc.mae:.5f} r2={sc.r2:.4f} "
            f"corr={sc.corr:.4f} n={sc.n} p={params}"
        )
        if sc.n > 0 and (best is None or sc.mae < best["val"]["mae"]):
            best = row

    assert best is not None
    # Refit on all pre-hunt clean rows
    all_pre = _clean(pre_idx)
    final = fit_lgbm(X[all_pre], y[all_pre], best["params"])
    return {
        "label": label,
        "best": best,
        "trials": trials,
        "model": final,
        "n_train_final": int(all_pre.size),
        "params": best["params"],
    }


def _mt_cfg() -> dict:
    return {
        "max_positions_per_side": K,
        "clarity": "mean_strength",
        "clarity_scope": "all",
        "fib_ext": FIB,
        "hold_addon": HOLD_ADDON,
        "base_hold": BASE_HOLD,
        "base_tp": 0.01,
        "base_sl": SL,
        "mean_lookback": MEAN_LOOKBACK,
        "uniform_books": False,
        "bar_ms": int(TF_MS[TIMEFRAME]),
        "strength_quantile": STRENGTH_Q,
        "geometry": "wall_clock",
    }


def run_trade_arm(
    ohlcv: pd.DataFrame,
    feats: pd.DataFrame,
    *,
    arm_name: str,
    outer0: pd.Timestamp,
    outer1: pd.Timestamp,
    lock: pd.Timestamp,
) -> dict[str, Any]:
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    ts_ms = index_to_ms(aligned.index)
    o0 = int(outer0.value // 1_000_000)
    o1 = int(outer1.value // 1_000_000)
    purge_ms = LABEL_HORIZON * int(TF_MS[TIMEFRAME])
    train_end = o0 - purge_ms
    tr = np.where(ts_ms < train_end)[0]
    oos = np.where((ts_ms >= o0) & (ts_ms < o1))[0]
    if tr.size < 400 or oos.size < 40:
        return {"arm": arm_name, "error": f"insufficient bars tr={tr.size} oos={oos.size}"}

    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    model.fit(X[tr], yv[tr])
    pred = model.predict(X[oos])
    mean = np.asarray(pred.mean, dtype=float).reshape(-1)
    side = proxy_side(mean, target_family(TARGET))
    close_oos = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)[oos]
    sigs, stats = build_multitrade_signals(
        ts_ms[oos], side, mean, cfg=_mt_cfg(), close=close_oos
    )
    oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
    pad = max(50, HOLD_ADDON * 4)
    pos = int(ohlcv.index.searchsorted(oos0))
    window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    touch = load_ohlcv(SYMBOL, touch_tf)
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TIMEFRAME])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    lev = float(leverage_from_stop(SL))

    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=f"eth_1h_retrace_proxy_{arm_name}",
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim_hedge(
            max_hold_bars=HOLD_ADDON,
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=K,
            max_positions_per_symbol=K * 2,
        ),
        instrument=research_instrument(SYMBOL),
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={
            "name": f"eth_1h_retrace_proxy_{arm_name}",
            "evidence_class": "RETRACE_PROXY_EXPERIMENT",
            "arm": arm_name,
            "window": [str(outer0.date()), str(outer1.date())],
            "promotion": "FORBIDDEN",
        },
        plot=False,
        print_headline=False,
        store_path=str(STORE),
    )
    m = bundle.metrics
    return {
        "arm": arm_name,
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy_return_units": float(
            getattr(m, "expectancy_return_units", float("nan"))
        ),
        "net_pnl": float(m.net_pnl),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "signal_stats": stats,
        "run_id": getattr(bundle, "run_id", None),
        "train_n": int(tr.size),
        "oos_n": int(oos.size),
    }


def apply_retrace_fill(
    feats: pd.DataFrame,
    *,
    fill_1h: pd.Series,
    fill_mode: str,
) -> pd.DataFrame:
    """Overwrite last_retrace* columns with proxy series (HTF: ffill of 1h fill)."""
    out = feats.copy()
    cols = retrace_cols(list(out.columns))
    s = fill_1h.reindex(out.index)
    for c in cols:
        # Primary decision column and HTF variants get same fill (aligned as-of).
        # Using predicted 1h causal/leaky is the controlled substitution.
        out[c] = s.to_numpy(dtype=float)
    _log(f"  fill mode={fill_mode} cols={cols} n_finite={int(np.isfinite(s).sum())}")
    return out


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "run.log").write_text("", encoding="utf-8")
    t0 = time.perf_counter()
    _log(
        "RETRACE_PROXY_EXPERIMENT start "
        f"grid={len(PARAM_GRID)} hunt_end={HUNT_END} outer=[{OUTER_START},{OUTER_END})"
    )
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    hunt_end = pd.Timestamp(HUNT_END, tz="UTC")
    outer0 = pd.Timestamp(OUTER_START, tz="UTC")
    outer1 = pd.Timestamp(OUTER_END, tz="UTC")
    hunt_end_ms = int(hunt_end.value // 1_000_000)
    outer0_ms = int(outer0.value // 1_000_000)
    outer1_ms = int(outer1.value // 1_000_000)

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    _log(f"ohlcv n={len(ohlcv)} tip={ohlcv.index.max()}")

    _log("targets leaky/causal …")
    tg = last_retrace_leaky_and_causal(ohlcv)
    _log("structure features …")
    feats_full = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    rcols = retrace_cols(list(feats_full.columns))
    xcols = feature_cols_without_retrace(list(feats_full.columns))
    _log(f"feature X cols={len(xcols)} dropped_retrace={rcols}")

    # Join numeric feature matrix + targets
    data = feats_full[xcols].apply(pd.to_numeric, errors="coerce")
    data = data.join(tg[["leaky", "causal"]], how="inner")
    # Keep finite X rows; y may still be nan for one target
    x_ok = np.all(np.isfinite(data[xcols].to_numpy(dtype=float)), axis=1)
    data = data.loc[x_ok].copy()
    ts_ms = index_to_ms(data.index)
    X = data[xcols].to_numpy(dtype=float)
    y_leaky = data["leaky"].to_numpy(dtype=float)
    y_causal = data["causal"].to_numpy(dtype=float)
    _log(f"aligned n={len(data)} leaky_finite={int(np.isfinite(y_leaky).sum())} "
         f"causal_finite={int(np.isfinite(y_causal).sum())}")

    # ---- Phase 1 hunt ----
    _log("=== hunt LEAKY target (contaminated labels) ===")
    hunt_l = hunt_proxy(X, y_leaky, ts_ms, hunt_end_ms=hunt_end_ms, label="leaky")
    _log("=== hunt CAUSAL target (correct labels) ===")
    hunt_c = hunt_proxy(X, y_causal, ts_ms, hunt_end_ms=hunt_end_ms, label="causal")

    # Outer recon evaluation (frozen params + models trained before hunt_end only)
    outer = (ts_ms >= outer0_ms) & (ts_ms < outer1_ms)
    outer_i = np.where(outer)[0]
    hat_l = predict_arr(hunt_l["model"], X)
    hat_c = predict_arr(hunt_c["model"], X)
    recon_outer = {
        "leaky_proxy_vs_leaky_truth": asdict(recon_scores(y_leaky[outer_i], hat_l[outer_i])),
        "causal_proxy_vs_causal_truth": asdict(recon_scores(y_causal[outer_i], hat_c[outer_i])),
        "leaky_proxy_vs_causal_truth": asdict(recon_scores(y_causal[outer_i], hat_l[outer_i])),
        "causal_proxy_vs_leaky_truth": asdict(recon_scores(y_leaky[outer_i], hat_c[outer_i])),
    }
    _log("outer recon: " + json.dumps(recon_outer, indent=2))

    # Persist models + full-series series
    series = data[["leaky", "causal"]].copy()
    series["pred_leaky"] = hat_l
    series["pred_causal"] = hat_c
    series_path = OUT_DIR / "retrace_proxy_series.parquet"
    series.to_parquet(series_path)
    joblib.dump(
        {
            "model": hunt_l["model"]._model,
            "feature_columns": xcols,
            "params": hunt_l["params"],
            "target": "leaky",
        },
        MODEL_DIR / "proxy_leaky.joblib",
    )
    joblib.dump(
        {
            "model": hunt_c["model"]._model,
            "feature_columns": xcols,
            "params": hunt_c["params"],
            "target": "causal",
        },
        MODEL_DIR / "proxy_causal.joblib",
    )
    _log(f"wrote models -> {MODEL_DIR}")

    # ---- Phase 2 trade arms ----
    pred_leaky_s = series["pred_leaky"]
    pred_causal_s = series["pred_causal"]
    true_causal_s = series["causal"]
    true_leaky_s = series["leaky"]

    arms: dict[str, pd.DataFrame] = {
        "oracle_causal_warehouse": apply_retrace_fill(
            feats_full, fill_1h=true_causal_s.reindex(feats_full.index), fill_mode="oracle_causal"
        ),
        "oracle_leaky": apply_retrace_fill(
            feats_full, fill_1h=true_leaky_s.reindex(feats_full.index), fill_mode="oracle_leaky"
        ),
        "pred_causal": apply_retrace_fill(
            feats_full, fill_1h=pred_causal_s.reindex(feats_full.index), fill_mode="pred_causal"
        ),
        "pred_leaky": apply_retrace_fill(
            feats_full, fill_1h=pred_leaky_s.reindex(feats_full.index), fill_mode="pred_leaky"
        ),
        "drop_retrace_zero": apply_retrace_fill(
            feats_full,
            fill_1h=pd.Series(0.0, index=feats_full.index),
            fill_mode="drop_zero",
        ),
    }

    trade_results = []
    for name, fmat in arms.items():
        _log(f"=== trade arm {name} ===")
        # After fill, drop rows with remaining nans from non-retrace features
        tr = run_trade_arm(
            ohlcv, fmat, arm_name=name, outer0=outer0, outer1=outer1, lock=lock
        )
        trade_results.append(tr)
        _log(
            f"  {name}: n={tr.get('n_trades')} pf={tr.get('profit_factor')} "
            f"E[r]={tr.get('expectancy_return_units')} wr={tr.get('win_rate')}"
        )

    # Rank arms by expectancy then PF (diagnostic only)
    ranked = sorted(
        [t for t in trade_results if "error" not in t],
        key=lambda r: (
            float(r.get("expectancy_return_units") or -1e9),
            float(r.get("profit_factor") or 0.0),
        ),
        reverse=True,
    )

    report = {
        "evidence_class": "RETRACE_PROXY_EXPERIMENT",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "promotion_allowed": False,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "calendar": {
            "hunt_end_exclusive": HUNT_END,
            "outer": [OUTER_START, OUTER_END],
            "lockbox_start": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
        },
        "feature_space": {
            "base": SPACE,
            "x_without_retrace_n": len(xcols),
            "retrace_cols_overwritten": rcols,
        },
        "proxy_hunt": {
            "leaky": {
                "best": hunt_l["best"],
                "n_train_final": hunt_l["n_train_final"],
                "n_trials": len(hunt_l["trials"]),
            },
            "causal": {
                "best": hunt_c["best"],
                "n_train_final": hunt_c["n_train_final"],
                "n_trials": len(hunt_c["trials"]),
            },
        },
        "outer_reconstruction": recon_outer,
        "trade_arms": trade_results,
        "trade_rank_by_expectancy": [r["arm"] for r in ranked],
        "best_trade_arm": ranked[0] if ranked else None,
        "best_proxy_by_val_mae": {
            "leaky": hunt_l["best"],
            "causal": hunt_c["best"],
        },
        "artifacts": {
            "series": str(series_path),
            "model_leaky": str(MODEL_DIR / "proxy_leaky.joblib"),
            "model_causal": str(MODEL_DIR / "proxy_causal.joblib"),
        },
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "note": (
            "Orange/leaky targets are still look-ahead labels — modelling them is "
            "diagnostic. Prefer cyan/causal proxy for any post-fix feature swap. "
            "Trade metrics on MIN_EXCHANGE dust are not scale-edge. Not a live pack."
        ),
    }
    latest = OUT_DIR / "last_retrace_proxy_trade_001_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (OUT_DIR / f"last_retrace_proxy_trade_001_{stamp}.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    _log(f"wrote {latest}")
    _log("BEST PROXY (val MAE): " + json.dumps({
        "leaky": hunt_l["best"]["val"],
        "causal": hunt_c["best"]["val"],
        "params_leaky": hunt_l["params"],
        "params_causal": hunt_c["params"],
    }, indent=2))
    _log("BEST TRADE ARM: " + json.dumps(ranked[0] if ranked else {}, indent=2, default=str))
    _log("OUTER RECON: " + json.dumps(recon_outer, indent=2))
    return 0


if __name__ == "__main__":
    from llm2.research.orange_track_seal import refuse_orange_pnl_optimization

    refuse_orange_pnl_optimization(
        context="train_last_retrace_proxy_and_trade.py (dual leaky/causal proxy trade hunt)"
    )
    raise SystemExit(main())
