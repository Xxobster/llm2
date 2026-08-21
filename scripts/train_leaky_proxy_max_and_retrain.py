"""Maximize oracle_leaky (true orange last_retrace_pct) proxy; retrain ETHUSDT on pred.

No cyan / causal target and no causal trade arms.

Phase A — push reconstruction of LEAKY last_retrace_pct only
  X: structure_v1 without last_retrace* + OHLCV / lag engineering
  Large LightGBM grid + early stopping + fine grid around winner + top-3 blend
  Selection: chronological validation MAE before HUNT_END (never lockbox)

Phase B — retrain trade model with last_retrace* overwritten by best leaky proxy
  Arms: oracle_leaky (upper bound) vs pred_leaky (this experiment)

Evidence: RESEARCH_ONLY / LEAKY_PROXY_MAX_EXPERIMENT
Promotion FORBIDDEN — oracle_leaky is CAUS-STRUCT look-ahead; proxies of it stay contaminated.
"""

from __future__ import annotations

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
import lightgbm as lgb  # noqa: E402
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

HUNT_END = "2025-10-01"
OUTER_START = "2026-01-01"
OUTER_END = FORWARD_LOCKBOX_START
VAL_FRAC = 0.20

OUT_DIR = ARTIFACTS / "reports" / "leaky_proxy_max_001"
MODEL_DIR = ARTIFACTS / "models" / "leaky_proxy_max_001"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
RETRACE_PREFIX = "last_retrace"

# Broad stage-1 grid
STAGE1_GRID: list[dict[str, Any]] = []
for n_est, lr, leaves, mcs, sub, col in [
    (80, 0.05, 15, 50, 0.8, 0.8),
    (120, 0.05, 31, 40, 0.9, 0.9),
    (200, 0.03, 31, 40, 0.85, 0.85),
    (300, 0.02, 47, 50, 0.8, 0.8),
    (400, 0.015, 63, 60, 0.75, 0.85),
    (150, 0.07, 23, 30, 0.9, 0.7),
    (250, 0.025, 31, 35, 0.85, 0.9),
    (350, 0.02, 95, 40, 0.7, 0.7),
    (180, 0.04, 47, 25, 0.8, 0.85),
    (500, 0.01, 31, 80, 0.75, 0.8),
    (220, 0.035, 63, 45, 0.85, 0.75),
    (100, 0.06, 15, 100, 0.9, 0.9),
]:
    STAGE1_GRID.append(
        {
            "n_estimators": n_est,
            "learning_rate": lr,
            "num_leaves": leaves,
            "min_child_samples": mcs,
            "subsample": sub,
            "colsample_bytree": col,
            "reg_lambda": 0.0,
            "reg_alpha": 0.0,
            "min_split_gain": 0.0,
        }
    )
# regularized variants
STAGE1_GRID.extend(
    [
        {"n_estimators": 300, "learning_rate": 0.02, "num_leaves": 31, "min_child_samples": 50,
         "subsample": 0.8, "colsample_bytree": 0.8, "reg_lambda": 1.0, "reg_alpha": 0.1, "min_split_gain": 0.0},
        {"n_estimators": 400, "learning_rate": 0.015, "num_leaves": 47, "min_child_samples": 40,
         "subsample": 0.75, "colsample_bytree": 0.85, "reg_lambda": 2.0, "reg_alpha": 0.2, "min_split_gain": 0.01},
        {"n_estimators": 250, "learning_rate": 0.03, "num_leaves": 63, "min_child_samples": 30,
         "subsample": 0.85, "colsample_bytree": 0.7, "reg_lambda": 0.5, "reg_alpha": 0.05, "min_split_gain": 0.0},
        {"n_estimators": 600, "learning_rate": 0.01, "num_leaves": 23, "min_child_samples": 100,
         "subsample": 0.7, "colsample_bytree": 0.9, "reg_lambda": 3.0, "reg_alpha": 0.5, "min_split_gain": 0.0},
    ]
)

LAG_BASE = (
    "dist_last_sh_pct",
    "dist_last_sl_pct",
    "last_leg_len_pct",
    "fib_position",
    "sr_asymmetry",
    "structure_bias",
    "dist_support_pct",
    "dist_resistance_pct",
    "dist_fib_0500_pct",
    "dist_fib_0618_pct",
)
LAGS = (1, 3, 6, 12, 24)


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


def recon_scores(y_true: np.ndarray, y_hat: np.ndarray) -> ReconScores:
    m = np.isfinite(y_true) & np.isfinite(y_hat)
    if int(m.sum()) < 10:
        return ReconScores(0, float("nan"), float("nan"), float("nan"), float("nan"), float("nan"))
    yt, yp = y_true[m], y_hat[m]
    err = yp - yt
    mae = float(np.mean(np.abs(err)))
    rmse = float(np.sqrt(np.mean(err ** 2)))
    ss_res = float(np.sum(err ** 2))
    ss_tot = float(np.sum((yt - yt.mean()) ** 2))
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-18 else float("nan")
    if float(yt.std()) < 1e-12 or float(yp.std()) < 1e-12:
        corr = float("nan")
    else:
        corr = float(np.corrcoef(yt, yp)[0, 1])
    return ReconScores(int(m.sum()), mae, rmse, r2, corr, float(np.max(np.abs(err))))


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


def oracle_leaky_last_retrace(ohlcv: pd.DataFrame) -> pd.Series:
    """Pre-CAUS-STRUCT-001 last_retrace_pct (own-leg confirm publish = look-ahead)."""
    raw = _ohlcv_to_struct_input(ohlcv)
    bundle = compute_structure(
        raw, source="binance", symbol=SYMBOL, timeframe=TIMEFRAME
    )
    ts_ms = raw["ts_ms"].to_numpy(dtype=np.int64)
    n = len(ts_ms)
    leaky = np.full(n, np.nan)
    legs = bundle.legs
    swings = bundle.swings
    if legs:
        swing_confirm = {s.swing_id: s.confirm_ts_ms for s in swings}
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
    return pd.Series(
        leaky, index=pd.to_datetime(ts_ms, unit="ms", utc=True), name="oracle_leaky"
    )


def engineer_features(ohlcv: pd.DataFrame, struct: pd.DataFrame) -> pd.DataFrame:
    """Structure sans retrace + vectorized OHLC/lag features (all causal at bar T)."""
    cols = [c for c in struct.columns if RETRACE_PREFIX not in c]
    x = struct[cols].apply(pd.to_numeric, errors="coerce")
    close = ohlcv["close"].reindex(x.index).astype(float)
    high = ohlcv["high"].reindex(x.index).astype(float)
    low = ohlcv["low"].reindex(x.index).astype(float)
    vol = (
        ohlcv["volume"].reindex(x.index).astype(float)
        if "volume" in ohlcv.columns
        else pd.Series(0.0, index=x.index)
    )
    log_c = np.log(close.replace(0, np.nan))
    x["ret_1"] = log_c.diff(1)
    x["ret_3"] = log_c.diff(3)
    x["ret_6"] = log_c.diff(6)
    x["ret_12"] = log_c.diff(12)
    x["ret_24"] = log_c.diff(24)
    x["vol_24"] = x["ret_1"].rolling(24, min_periods=12).std()
    x["vol_72"] = x["ret_1"].rolling(72, min_periods=24).std()
    x["hl_range"] = (high - low) / close
    x["hl_range_24"] = x["hl_range"].rolling(24, min_periods=12).mean()
    x["vol_z_24"] = (vol - vol.rolling(24, min_periods=12).mean()) / (
        vol.rolling(24, min_periods=12).std() + 1e-12
    )
    for c in LAG_BASE:
        if c not in x.columns:
            continue
        s = x[c]
        for L in LAGS:
            x[f"{c}_lag{L}"] = s.shift(L)
        x[f"{c}_roll_mean_12"] = s.rolling(12, min_periods=6).mean()
        x[f"{c}_roll_std_12"] = s.rolling(12, min_periods=6).std()
    return x


def fit_early(
    X_tr: np.ndarray,
    y_tr: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    params: dict[str, Any],
) -> tuple[lgb.LGBMRegressor, dict[str, Any]]:
    p = {
        "verbosity": -1,
        "n_estimators": int(params.get("n_estimators", 200)),
        "learning_rate": float(params.get("learning_rate", 0.05)),
        "num_leaves": int(params.get("num_leaves", 31)),
        "min_child_samples": int(params.get("min_child_samples", 40)),
        "subsample": float(params.get("subsample", 0.9)),
        "colsample_bytree": float(params.get("colsample_bytree", 0.9)),
        "reg_lambda": float(params.get("reg_lambda", 0.0)),
        "reg_alpha": float(params.get("reg_alpha", 0.0)),
        "min_split_gain": float(params.get("min_split_gain", 0.0)),
        "subsample_freq": 1,
    }
    model = lgb.LGBMRegressor(**p)
    model.fit(
        X_tr,
        y_tr,
        eval_set=[(X_val, y_val)],
        eval_metric="l1",
        callbacks=[lgb.early_stopping(80, verbose=False), lgb.log_evaluation(0)],
    )
    used = dict(p)
    used["best_iteration_"] = int(getattr(model, "best_iteration_", p["n_estimators"]) or p["n_estimators"])
    return model, used


def predict_m(model: lgb.LGBMRegressor, X: np.ndarray) -> np.ndarray:
    bi = getattr(model, "best_iteration_", None)
    if bi is not None and bi > 0:
        return np.asarray(model.predict(X, num_iteration=bi), dtype=float).reshape(-1)
    return np.asarray(model.predict(X), dtype=float).reshape(-1)


def stage1_hunt(
    X: np.ndarray, y: np.ndarray, tr_i: np.ndarray, val_i: np.ndarray
) -> list[dict[str, Any]]:
    trials = []
    for pi, params in enumerate(STAGE1_GRID):
        t0 = time.perf_counter()
        model, used = fit_early(X[tr_i], y[tr_i], X[val_i], y[val_i], params)
        hat = predict_m(model, X[val_i])
        sc = recon_scores(y[val_i], hat)
        row = {
            "stage": 1,
            "trial": pi,
            "params": used,
            "val": asdict(sc),
            "elapsed_sec": round(time.perf_counter() - t0, 2),
            "model": model,
        }
        trials.append(row)
        _log(
            f"  s1 t={pi:02d} mae={sc.mae:.5f} r2={sc.r2:.4f} corr={sc.corr:.4f} "
            f"bi={used.get('best_iteration_')} n={sc.n}"
        )
    return trials


def fine_grid(best_params: dict[str, Any]) -> list[dict[str, Any]]:
    """Neighborhood fine-tune around stage-1 winner."""
    base = dict(best_params)
    for k in ("best_iteration_",):
        base.pop(k, None)
    candidates = [base]
    lr0 = float(base.get("learning_rate", 0.03))
    leaves0 = int(base.get("num_leaves", 31))
    mcs0 = int(base.get("min_child_samples", 40))
    nest0 = max(int(base.get("n_estimators", 200)), 200)
    for lr in sorted({max(0.005, lr0 * f) for f in (0.5, 0.75, 1.0, 1.25, 1.5)}):
        for leaves in sorted({max(8, int(leaves0 * f)) for f in (0.5, 0.75, 1.0, 1.25, 1.5, 2.0)}):
            for mcs in sorted({max(10, int(mcs0 * f)) for f in (0.5, 0.75, 1.0, 1.25, 1.5)}):
                for reg_l in (0.0, 0.5, 1.0, 2.0):
                    p = dict(base)
                    p.update(
                        {
                            "n_estimators": min(800, nest0 * 2),
                            "learning_rate": lr,
                            "num_leaves": leaves,
                            "min_child_samples": mcs,
                            "reg_lambda": reg_l,
                        }
                    )
                    candidates.append(p)
    # unique by frozenset of items
    uniq: dict[str, dict[str, Any]] = {}
    for p in candidates:
        key = json.dumps(p, sort_keys=True)
        uniq[key] = p
    out = list(uniq.values())
    # cap fine budget
    if len(out) > 48:
        # keep first + random-ish every k
        step = max(1, len(out) // 48)
        out = out[::step][:48]
    return out


def stage2_fine(
    X: np.ndarray,
    y: np.ndarray,
    tr_i: np.ndarray,
    val_i: np.ndarray,
    best_s1: dict[str, Any],
) -> list[dict[str, Any]]:
    grid = fine_grid(best_s1["params"])
    _log(f"stage-2 fine grid size={len(grid)}")
    trials = []
    for pi, params in enumerate(grid):
        t0 = time.perf_counter()
        model, used = fit_early(X[tr_i], y[tr_i], X[val_i], y[val_i], params)
        hat = predict_m(model, X[val_i])
        sc = recon_scores(y[val_i], hat)
        row = {
            "stage": 2,
            "trial": pi,
            "params": used,
            "val": asdict(sc),
            "elapsed_sec": round(time.perf_counter() - t0, 2),
            "model": model,
        }
        trials.append(row)
        if pi % 5 == 0 or sc.mae <= best_s1["val"]["mae"]:
            _log(
                f"  s2 t={pi:02d} mae={sc.mae:.5f} r2={sc.r2:.4f} corr={sc.corr:.4f} "
                f"bi={used.get('best_iteration_')}"
            )
    return trials


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
    model = LGBMRegressorPredictor(n_estimators=120, learning_rate=0.05, num_leaves=31)
    model.fit(X[tr], yv[tr])
    mean = np.asarray(model.predict(X[oos]).mean, dtype=float).reshape(-1)
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
        strategy_id=f"eth_1h_leaky_proxy_max_{arm_name}",
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
            "name": f"eth_1h_leaky_proxy_max_{arm_name}",
            "evidence_class": "LEAKY_PROXY_MAX_EXPERIMENT",
            "arm": arm_name,
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


def apply_leaky_fill(feats: pd.DataFrame, fill: pd.Series) -> pd.DataFrame:
    out = feats.copy()
    rcols = [c for c in out.columns if RETRACE_PREFIX in c]
    s = fill.reindex(out.index).astype(float)
    for c in rcols:
        out[c] = s.to_numpy(dtype=float)
    _log(f"  overwrite retrace cols={rcols} finite={int(np.isfinite(s).sum())}")
    return out


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "run.log").write_text("", encoding="utf-8")
    t0 = time.perf_counter()
    _log(
        f"LEAKY_PROXY_MAX start stage1={len(STAGE1_GRID)} "
        f"hunt_end={HUNT_END} outer=[{OUTER_START},{OUTER_END})"
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
    _log(f"ohlcv n={len(ohlcv)}")

    _log("oracle_leaky target …")
    y_s = oracle_leaky_last_retrace(ohlcv)
    _log("structure_v1 …")
    struct = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    _log("feature engineering …")
    X_df = engineer_features(ohlcv, struct)
    data = X_df.join(y_s, how="inner")
    # drop rows with all-nan X fringe
    xcols = [c for c in data.columns if c != "oracle_leaky"]
    X_raw = data[xcols].to_numpy(dtype=float)
    y = data["oracle_leaky"].to_numpy(dtype=float)
    # Require finite y + mostly finite X: drop cols with too many nan, then rows
    col_ok = np.mean(np.isfinite(X_raw), axis=0) >= 0.90
    xcols = [c for c, ok in zip(xcols, col_ok) if ok]
    X_raw = data[xcols].to_numpy(dtype=float)
    row_ok = np.isfinite(y) & (np.mean(np.isfinite(X_raw), axis=1) >= 0.95)
    # impute remaining nan with train-only later — for now fill col median pre-hunt
    data = data.loc[row_ok].copy()
    X_raw = data[xcols].to_numpy(dtype=float)
    y = data["oracle_leaky"].to_numpy(dtype=float)
    ts_ms = index_to_ms(data.index)
    # median impute using pre-hunt only
    pre_mask = ts_ms < hunt_end_ms
    med = np.nanmedian(X_raw[pre_mask], axis=0)
    med = np.where(np.isfinite(med), med, 0.0)
    inds = np.where(~np.isfinite(X_raw))
    X_raw[inds] = np.take(med, inds[1])
    X = X_raw
    _log(f"matrix n={len(data)} xcols={len(xcols)} y_finite={int(np.isfinite(y).sum())}")

    pre_idx = np.where(pre_mask)[0]
    n_val = max(400, int(len(pre_idx) * VAL_FRAC))
    val_i = pre_idx[-n_val:]
    tr_i = pre_idx[:-n_val]
    tr_i = tr_i[np.isfinite(y[tr_i])]
    val_i = val_i[np.isfinite(y[val_i])]
    _log(f"train={tr_i.size} val={val_i.size}")

    _log("=== stage-1 grid ===")
    s1 = stage1_hunt(X, y, tr_i, val_i)
    s1_sorted = sorted(s1, key=lambda r: r["val"]["mae"])
    best_s1 = s1_sorted[0]
    _log(f"stage-1 best mae={best_s1['val']['mae']:.5f} params={best_s1['params']}")

    _log("=== stage-2 fine ===")
    s2 = stage2_fine(X, y, tr_i, val_i, best_s1)
    all_trials = s1 + s2
    ranked = sorted(all_trials, key=lambda r: r["val"]["mae"])
    top3 = ranked[:3]
    for i, t in enumerate(top3):
        _log(f"top{i+1} mae={t['val']['mae']:.5f} stage={t['stage']} trial={t['trial']}")

    # Refit top models on all pre-hunt rows with last val slice for early stopping
    all_pre = pre_idx[np.isfinite(y[pre_idx])]
    n_es = max(300, int(len(all_pre) * 0.10))
    fit_tr, fit_es = all_pre[:-n_es], all_pre[-n_es:]
    refit_models = []
    for t in top3:
        m, used = fit_early(X[fit_tr], y[fit_tr], X[fit_es], y[fit_es], t["params"])
        refit_models.append({"params": used, "model": m, "val_mae_select": t["val"]["mae"]})

    # Predictions: best single + blend top3
    hat_best = predict_m(refit_models[0]["model"], X)
    hats = np.column_stack([predict_m(rm["model"], X) for rm in refit_models])
    hat_blend = np.mean(hats, axis=1)

    outer = (ts_ms >= outer0_ms) & (ts_ms < outer1_ms)
    oi = np.where(outer)[0]
    recon = {
        "best_single_outer": asdict(recon_scores(y[oi], hat_best[oi])),
        "blend_top3_outer": asdict(recon_scores(y[oi], hat_blend[oi])),
        "best_single_val": ranked[0]["val"],
        "blend_vs_best": {
            "outer_mae_best": recon_scores(y[oi], hat_best[oi]).mae,
            "outer_mae_blend": recon_scores(y[oi], hat_blend[oi]).mae,
        },
    }
    use_blend = recon["blend_vs_best"]["outer_mae_blend"] <= recon["blend_vs_best"]["outer_mae_best"]
    # outer MAE used only for *reporting choice of delivery series*, not for model selection.
    # Selection was val-only. Delivery picks blend if outer also better (diagnostic honesty:
    # prefer val_mae blend if average of top3 val is best).
    # Safer: use blend only if val MAE of blend would be better — recompute blend on val.
    blend_val = recon_scores(y[val_i], np.mean(hats[val_i], axis=1))
    best_val_mae = float(ranked[0]["val"]["mae"])
    use_blend = blend_val.mae <= best_val_mae
    hat_final = hat_blend if use_blend else hat_best
    delivery = "blend_top3" if use_blend else "best_single"
    recon["delivery"] = delivery
    recon["delivery_outer"] = asdict(recon_scores(y[oi], hat_final[oi]))
    recon["blend_val"] = asdict(blend_val)
    _log(
        f"delivery={delivery} outer_mae={recon['delivery_outer']['mae']:.5f} "
        f"outer_r2={recon['delivery_outer']['r2']:.4f} outer_corr={recon['delivery_outer']['corr']:.4f}"
    )

    series = pd.DataFrame(
        {
            "oracle_leaky": y,
            "pred_leaky_best": hat_best,
            "pred_leaky_blend": hat_blend,
            "pred_leaky": hat_final,
        },
        index=data.index,
    )
    series_path = OUT_DIR / "leaky_proxy_series.parquet"
    series.to_parquet(series_path)

    joblib.dump(
        {
            "feature_columns": xcols,
            "col_medians_prehunt": med.tolist() if isinstance(med, np.ndarray) else list(med),
            "delivery": delivery,
            "models": [
                {"params": rm["params"], "booster": rm["model"]} for rm in refit_models
            ],
            "target": "oracle_leaky",
            "note": "CAUS-STRUCT look-ahead target; research only",
        },
        MODEL_DIR / "proxy_oracle_leaky_max.joblib",
    )
    _log(f"wrote {MODEL_DIR / 'proxy_oracle_leaky_max.joblib'}")

    # Trade retrain
    pred_s = series["pred_leaky"]
    oracle_s = series["oracle_leaky"]
    arms = {
        "oracle_leaky": apply_leaky_fill(struct, oracle_s.reindex(struct.index)),
        "pred_leaky": apply_leaky_fill(struct, pred_s.reindex(struct.index)),
    }
    trade_results = []
    for name, fmat in arms.items():
        _log(f"=== trade arm {name} ===")
        tr = run_trade_arm(
            ohlcv, fmat, arm_name=name, outer0=outer0, outer1=outer1, lock=lock
        )
        trade_results.append(tr)
        _log(
            f"  {name}: n={tr.get('n_trades')} pf={tr.get('profit_factor')} "
            f"E[r]={tr.get('expectancy_return_units')} wr={tr.get('win_rate')}"
        )

    report = {
        "evidence_class": "LEAKY_PROXY_MAX_EXPERIMENT",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "promotion_allowed": False,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "target": "oracle_leaky_only",
        "causal_used": False,
        "calendar": {
            "hunt_end_exclusive": HUNT_END,
            "outer": [OUTER_START, OUTER_END],
            "lockbox_used": False,
        },
        "n_features": len(xcols),
        "n_stage1": len(s1),
        "n_stage2": len(s2),
        "best_val": ranked[0]["val"],
        "best_params": ranked[0]["params"],
        "top3_val_mae": [t["val"]["mae"] for t in top3],
        "reconstruction": recon,
        "trade_arms": trade_results,
        "artifacts": {
            "series": str(series_path),
            "model": str(MODEL_DIR / "proxy_oracle_leaky_max.joblib"),
        },
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "note": (
            "oracle_leaky is look-ahead by construction. Best trade numbers that rely "
            "on true orange remain contamination. Pred-leaky retrain is a proxy of "
            "contamination, not live readiness."
        ),
    }
    # strip models from trial dump
    trial_dump = [
        {
            "stage": t["stage"],
            "trial": t["trial"],
            "params": t["params"],
            "val": t["val"],
            "elapsed_sec": t["elapsed_sec"],
        }
        for t in ranked[:20]
    ]
    report["top20_trials"] = trial_dump

    latest = OUT_DIR / "leaky_proxy_max_001_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (OUT_DIR / f"leaky_proxy_max_001_{stamp}.json").write_text(
        json.dumps(report, indent=2, default=str), encoding="utf-8"
    )
    _log(f"wrote {latest}")
    _log(
        "SUMMARY "
        + json.dumps(
            {
                "delivery": delivery,
                "outer_recon": recon["delivery_outer"],
                "best_val_mae": ranked[0]["val"]["mae"],
                "trades": trade_results,
            },
            indent=2,
            default=str,
        )
    )
    return 0


if __name__ == "__main__":
    from llm2.research.orange_track_seal import refuse_orange_pnl_optimization

    refuse_orange_pnl_optimization(
        context="train_leaky_proxy_max_and_retrain.py (oracle_leaky grid + pred_leaky trade)"
    )
    raise SystemExit(main())
