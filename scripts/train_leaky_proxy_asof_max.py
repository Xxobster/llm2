"""Push CAUSAL prediction of oracle_leaky (orange last_retrace_pct) to the ceiling.

Key idea: between two leg completions the leaky series holds the *final* retrace of
the previous leg (look-ahead). A causal proxy can track the *running* retrace depth
of the active opposite move (price known at bar T). That is legitimate and is the
information that will become the label once the next swing confirms.

Also: dense pivot history, multi-model LGBM + HistGradientBoosting + residual,
heavy hyper hunt, top-k blend. Trade retest oracle_leaky vs best pred_leaky.

No cyan/causal target. Lockbox unused. RESEARCH_ONLY / promotion FORBIDDEN.
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
from sklearn.ensemble import ExtraTreesRegressor, HistGradientBoostingRegressor  # noqa: E402
from sklearn.linear_model import Ridge  # noqa: E402

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
N_RANDOM = 80  # LGBM random trials

OUT_DIR = ARTIFACTS / "reports" / "leaky_proxy_asof_max_001"
MODEL_DIR = ARTIFACTS / "models" / "leaky_proxy_asof_max_001"
STORE = Path(r"D:\projectsdata\backtests\tradesim_runs.sqlite")
RETRACE_PREFIX = "last_retrace"
RNG = np.random.default_rng(42)


@dataclass
class ReconScores:
    n: int
    mae: float
    rmse: float
    r2: float
    corr: float
    max_abs: float
    pct_within_010: float
    pct_within_005: float


def _log(msg: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(msg, flush=True)
    with (OUT_DIR / "run.log").open("a", encoding="utf-8") as fh:
        fh.write(msg + "\n")


def recon_scores(y_true: np.ndarray, y_hat: np.ndarray) -> ReconScores:
    m = np.isfinite(y_true) & np.isfinite(y_hat)
    if int(m.sum()) < 10:
        return ReconScores(
            0, float("nan"), float("nan"), float("nan"), float("nan"), float("nan"),
            float("nan"), float("nan"),
        )
    yt, yp = y_true[m], y_hat[m]
    err = yp - yt
    ae = np.abs(err)
    mae = float(np.mean(ae))
    rmse = float(np.sqrt(np.mean(err ** 2)))
    ss_res = float(np.sum(err ** 2))
    ss_tot = float(np.sum((yt - yt.mean()) ** 2))
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-18 else float("nan")
    if float(yt.std()) < 1e-12 or float(yp.std()) < 1e-12:
        corr = float("nan")
    else:
        corr = float(np.corrcoef(yt, yp)[0, 1])
    return ReconScores(
        int(m.sum()),
        mae,
        rmse,
        r2,
        corr,
        float(np.max(ae)),
        float(np.mean(ae <= 0.10)),
        float(np.mean(ae <= 0.05)),
    )


def _ohlcv_raw(ohlcv: pd.DataFrame) -> pd.DataFrame:
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


def oracle_leaky_and_asof_features(ohlcv: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """Build oracle_leaky + as-of running-retrace and pivot-history features (vectorized)."""
    raw = _ohlcv_raw(ohlcv)
    bundle = compute_structure(
        raw, source="binance", symbol=SYMBOL, timeframe=TIMEFRAME
    )
    ts = raw["ts_ms"].to_numpy(dtype=np.int64)
    close = raw["close"].to_numpy(dtype=float)
    high = raw["high"].to_numpy(dtype=float)
    low = raw["low"].to_numpy(dtype=float)
    n = len(ts)
    idx = pd.to_datetime(ts, unit="ms", utc=True)

    legs = bundle.legs
    swings = bundle.swings
    swing_confirm = {s.swing_id: s.confirm_ts_ms for s in swings}

    leaky = np.full(n, np.nan)
    if not legs:
        return pd.Series(leaky, index=idx, name="oracle_leaky"), pd.DataFrame(index=idx)

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
    dirs = np.asarray([1.0 if lg.direction == "up" else -1.0 for lg in legs_o], dtype=float)
    end_px = np.asarray([lg.end_price for lg in legs_o], dtype=float)
    start_px = np.asarray([lg.start_price for lg in legs_o], dtype=float)
    length_abs = np.asarray([lg.length_abs for lg in legs_o], dtype=float)
    length_pct = np.asarray([lg.length_pct for lg in legs_o], dtype=float)
    end_ts = np.asarray([lg.end_ts_ms for lg in legs_o], dtype=np.int64)
    kind_imp = np.asarray([1.0 if lg.kind == "impulse" else 0.0 for lg in legs_o])

    # leaky target
    li = np.searchsorted(known_ts, ts, side="right") - 1
    ok = li >= 0
    leaky[ok] = retr[li[ok]]

    # last completed leg as-of T
    li_safe = np.clip(li, 0, len(legs_o) - 1)
    ep = np.where(ok, end_px[li_safe], np.nan)
    sp = np.where(ok, start_px[li_safe], np.nan)
    la = np.where(ok, length_abs[li_safe], np.nan)
    lp = np.where(ok, length_pct[li_safe], np.nan)
    d = np.where(ok, dirs[li_safe], np.nan)
    kt = np.where(ok, known_ts[li_safe].astype(float), np.nan)
    et = np.where(ok, end_ts[li_safe].astype(float), np.nan)
    imp = np.where(ok, kind_imp[li_safe], np.nan)

    # running retrace of the last completed leg using current price (causal)
    # if last leg was up, opposite (down) retrace depth = (end - close)/length_abs when close < end
    # if last leg was down, opposite (up) = (close - end)/length_abs when close > end
    move_against = np.where(d > 0, ep - close, close - ep)
    run_retrace = np.where(ok & (la > 1e-12), np.maximum(0.0, move_against) / la, np.nan)
    # excursion with high/low extremes of current bar for same-bar adverse
    against_hi = np.where(d > 0, ep - low, high - ep)  # max against during bar
    run_retrace_ext = np.where(ok & (la > 1e-12), np.maximum(0.0, against_hi) / la, np.nan)

    # bars since last leg known
    bars_since_leg = np.where(ok, (ts.astype(float) - kt) / float(TF_MS[TIMEFRAME]), np.nan)
    bars_since_end = np.where(ok, (ts.astype(float) - et) / float(TF_MS[TIMEFRAME]), np.nan)

    # previous completed leg stats (leg i-1)
    prev_ok = li >= 1
    li_p = np.clip(li - 1, 0, len(legs_o) - 1)
    prev_retr_label_final = np.where(prev_ok, retr[li_p], np.nan)  # FUTURE for previous - STOP
    # Do NOT use prev final retr for older legs when predicting current... actually for
    # older legs (i-1), by the time leg i is known, retr[i-1] is knowable (needs leg i).
    # So when li points to last leg, retr of li-1 IS causal (next opposite = current last
    # leg already completed). Good feature.
    prev_retr_causal = np.where(prev_ok, retr[li_p], np.nan)
    prev_len = np.where(prev_ok, length_pct[li_p], np.nan)
    prev_dir = np.where(prev_ok, dirs[li_p], np.nan)
    # final retr of CURRENT last leg is NOT causal - that's the target y. Don't include retr[li].

    # swing extremes as-of
    sw_ts = np.asarray([s.confirm_ts_ms for s in swings], dtype=np.int64)
    sw_px = np.asarray([s.price for s in swings], dtype=float)
    sw_k = np.asarray([1.0 if s.kind == "high" else -1.0 for s in swings], dtype=float)
    if len(swings):
        order_s = np.argsort(sw_ts, kind="mergesort")
        sw_ts = sw_ts[order_s]
        sw_px = sw_px[order_s]
        sw_k = sw_k[order_s]
        si = np.searchsorted(sw_ts, ts, side="right") - 1
        sok = si >= 0
        last_sw_px = np.where(sok, sw_px[np.clip(si, 0, len(sw_px) - 1)], np.nan)
        last_sw_k = np.where(sok, sw_k[np.clip(si, 0, len(sw_k) - 1)], np.nan)
        # last high / last low separately via two pass
        high_mask = sw_k > 0
        low_mask = sw_k < 0
        h_ts, h_px = sw_ts[high_mask], sw_px[high_mask]
        l_ts, l_px = sw_ts[low_mask], sw_px[low_mask]
        if len(h_ts):
            hi = np.searchsorted(h_ts, ts, side="right") - 1
            last_sh = np.where(hi >= 0, h_px[np.clip(hi, 0, len(h_px) - 1)], np.nan)
        else:
            last_sh = np.full(n, np.nan)
        if len(l_ts):
            li2 = np.searchsorted(l_ts, ts, side="right") - 1
            last_sl = np.where(li2 >= 0, l_px[np.clip(li2, 0, len(l_px) - 1)], np.nan)
        else:
            last_sl = np.full(n, np.nan)
        dist_sh = (close - last_sh) / close
        dist_sl = (close - last_sl) / close
        # swing count lookbacks (completed confirms in last N hours)
        sw_counts = np.zeros(n)
        for look in (24, 72, 168):
            # approximate count with searchsorted for each bar - O(n log m) ok
            t0 = ts - look * int(TF_MS[TIMEFRAME])
            left = np.searchsorted(sw_ts, t0, side="left")
            right = np.searchsorted(sw_ts, ts, side="right")
            cnt = (right - left).astype(float)
            sw_counts = cnt  # overwritten below with named
            if look == 24:
                n_sw_24 = cnt
            elif look == 72:
                n_sw_72 = cnt
            else:
                n_sw_168 = cnt
    else:
        last_sw_px = last_sw_k = last_sh = last_sl = dist_sh = dist_sl = np.full(n, np.nan)
        n_sw_24 = n_sw_72 = n_sw_168 = np.zeros(n)

    # rolling max of running retrace over active window since leg known (causal expansion)
    # compute with group loops is slow; use forward fill segments + expanding max vectorized via pandas
    asof = pd.DataFrame(
        {
            "run_retrace": run_retrace,
            "run_retrace_ext": run_retrace_ext,
            "asof_leg_id": np.where(ok, li.astype(float), np.nan),
            "asof_last_leg_len_pct": lp,
            "asof_last_leg_len_abs": la,
            "asof_last_leg_dir": d,
            "asof_last_leg_impulse": imp,
            "bars_since_leg_known": bars_since_leg,
            "bars_since_leg_end": bars_since_end,
            "dist_to_leg_end_pct": np.where(ok & (close != 0), (close - ep) / close, np.nan),
            "prev_leg_retrace_causal": prev_retr_causal,
            "prev_leg_len_pct": prev_len,
            "prev_leg_dir": prev_dir,
            "dist_last_sh_asof": dist_sh,
            "dist_last_sl_asof": dist_sl,
            "last_sw_kind": last_sw_k,
            "dist_last_sw_pct": np.where(
                np.isfinite(last_sw_px), (close - last_sw_px) / close, np.nan
            ),
            "n_sw_24": n_sw_24,
            "n_sw_72": n_sw_72,
            "n_sw_168": n_sw_168,
            # proxy: clip running depth as naive estimator of eventual retrace
            "naive_run_as_label": run_retrace_ext,
        },
        index=idx,
    )
    # expanding max of run_retrace within each leg segment
    leg_id_s = pd.Series(np.where(ok, li, -1), index=idx)
    run_s = pd.Series(run_retrace_ext, index=idx)
    asof["run_retrace_expand_max"] = run_s.groupby(leg_id_s).cummax()
    asof["run_minus_prev_retr"] = asof["run_retrace_expand_max"] - asof["prev_leg_retrace_causal"]
    # velocity of running retrace
    asof["run_retrace_diff1"] = asof["run_retrace"].diff(1)
    asof["run_retrace_diff3"] = asof["run_retrace"].diff(3)
    asof["run_retrace_mean6"] = asof["run_retrace"].rolling(6, min_periods=2).mean()

    y = pd.Series(leaky, index=idx, name="oracle_leaky")
    return y, asof


def engineer_base(ohlcv: pd.DataFrame, struct: pd.DataFrame) -> pd.DataFrame:
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
    x["hl_range_ma24"] = x["hl_range"].rolling(24, min_periods=8).mean()
    x["close_z_48"] = (close - close.rolling(48, min_periods=24).mean()) / (
        close.rolling(48, min_periods=24).std() + 1e-12
    )
    x["vol_z_24"] = (vol - vol.rolling(24, min_periods=12).mean()) / (
        vol.rolling(24, min_periods=12).std() + 1e-12
    )
    for c in (
        "dist_last_sh_pct",
        "dist_last_sl_pct",
        "last_leg_len_pct",
        "fib_position",
        "sr_asymmetry",
        "structure_bias",
    ):
        if c not in x.columns:
            continue
        s = x[c]
        for L in (1, 3, 6, 12, 24):
            x[f"{c}_lag{L}"] = s.shift(L)
        x[f"{c}_rmean12"] = s.rolling(12, min_periods=4).mean()
        x[f"{c}_rstd12"] = s.rolling(12, min_periods=4).std()
    return x


def fit_lgbm(X_tr, y_tr, X_val, y_val, params: dict) -> lgb.LGBMRegressor:
    p = {
        "verbosity": -1,
        "n_estimators": int(params.get("n_estimators", 400)),
        "learning_rate": float(params.get("learning_rate", 0.03)),
        "num_leaves": int(params.get("num_leaves", 31)),
        "min_child_samples": int(params.get("min_child_samples", 40)),
        "subsample": float(params.get("subsample", 0.85)),
        "colsample_bytree": float(params.get("colsample_bytree", 0.85)),
        "reg_lambda": float(params.get("reg_lambda", 1.0)),
        "reg_alpha": float(params.get("reg_alpha", 0.1)),
        "min_split_gain": float(params.get("min_split_gain", 0.0)),
        "subsample_freq": 1,
        "max_depth": int(params.get("max_depth", -1)),
    }
    m = lgb.LGBMRegressor(**p)
    m.fit(
        X_tr,
        y_tr,
        eval_set=[(X_val, y_val)],
        eval_metric="l1",
        callbacks=[lgb.early_stopping(100, verbose=False), lgb.log_evaluation(0)],
    )
    return m


def pred_lgbm(m: lgb.LGBMRegressor, X: np.ndarray) -> np.ndarray:
    bi = getattr(m, "best_iteration_", None)
    if bi is not None and bi > 0:
        return np.asarray(m.predict(X, num_iteration=bi), dtype=float).reshape(-1)
    return np.asarray(m.predict(X), dtype=float).reshape(-1)


def sample_lgbm_params() -> dict[str, Any]:
    return {
        "n_estimators": int(RNG.choice([200, 400, 600, 800, 1000])),
        "learning_rate": float(RNG.choice([0.005, 0.01, 0.015, 0.02, 0.03, 0.05, 0.07])),
        "num_leaves": int(RNG.choice([15, 23, 31, 47, 63, 95, 127])),
        "min_child_samples": int(RNG.choice([20, 30, 40, 60, 80, 100, 150, 200])),
        "subsample": float(RNG.choice([0.6, 0.7, 0.8, 0.9, 1.0])),
        "colsample_bytree": float(RNG.choice([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])),
        "reg_lambda": float(RNG.choice([0.0, 0.5, 1.0, 2.0, 5.0])),
        "reg_alpha": float(RNG.choice([0.0, 0.05, 0.1, 0.5, 1.0])),
        "min_split_gain": float(RNG.choice([0.0, 0.0, 0.01, 0.05])),
        "max_depth": int(RNG.choice([-1, -1, 6, 8, 10, 12])),
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


def run_trade(
    ohlcv: pd.DataFrame,
    feats: pd.DataFrame,
    *,
    arm: str,
    outer0: pd.Timestamp,
    outer1: pd.Timestamp,
    lock: pd.Timestamp,
) -> dict[str, Any]:
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    ts_ms = index_to_ms(aligned.index)
    o0 = int(outer0.value // 1_000_000)
    o1 = int(outer1.value // 1_000_000)
    purge = LABEL_HORIZON * int(TF_MS[TIMEFRAME])
    tr = np.where(ts_ms < o0 - purge)[0]
    oos = np.where((ts_ms >= o0) & (ts_ms < o1))[0]
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    model = LGBMRegressorPredictor(n_estimators=120, learning_rate=0.05)
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
    touch_end = end + pd.Timedelta(milliseconds=int(TF_MS[TIMEFRAME])) - pd.Timedelta(
        milliseconds=1
    )
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    fts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    fr = funding.to_numpy(dtype=float)
    wts = index_to_ms(window.index)
    fm = (fts >= int(wts[0])) & (fts <= int(wts[-1]))
    lev = float(leverage_from_stop(SL))
    bundle = run_strategy_backtest(
        window,
        sigs,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=f"eth_1h_leaky_asof_{arm}",
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
        funding_ts_ms=fts[fm],
        funding_rate=fr[fm],
        strategy_meta={
            "arm": arm,
            "evidence_class": "LEAKY_PROXY_ASOF_MAX",
            "promotion": "FORBIDDEN",
        },
        plot=False,
        print_headline=False,
        store_path=str(STORE),
    )
    m = bundle.metrics
    return {
        "arm": arm,
        "n_trades": int(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "expectancy_return_units": float(
            getattr(m, "expectancy_return_units", float("nan"))
        ),
        "net_pnl": float(m.net_pnl),
        "run_id": getattr(bundle, "run_id", None),
        "signal_stats": stats,
    }


def fill_retrace(feats: pd.DataFrame, s: pd.Series) -> pd.DataFrame:
    out = feats.copy()
    v = s.reindex(out.index).astype(float).to_numpy()
    for c in out.columns:
        if RETRACE_PREFIX in c:
            out[c] = v
    return out


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "run.log").write_text("", encoding="utf-8")
    t0 = time.perf_counter()
    _log(f"LEAKY_PROXY_ASOF_MAX n_random={N_RANDOM} start")

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

    _log("oracle + as-of pivot/running-retrace features …")
    y_s, asof = oracle_leaky_and_asof_features(ohlcv)
    _log("structure_v1 + base engineers …")
    struct = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    base = engineer_base(ohlcv, struct)
    X_df = base.join(asof, how="inner").join(y_s, how="inner")

    # naive running-retrace alone as baseline
    naive = X_df["naive_run_as_label"].to_numpy(dtype=float)
    y_all = X_df["oracle_leaky"].to_numpy(dtype=float)
    ts_ms = index_to_ms(X_df.index)
    outer = (ts_ms >= outer0_ms) & (ts_ms < outer1_ms)
    oi = np.where(outer)[0]
    naive_sc = recon_scores(y_all[oi], naive[oi])
    _log(f"baseline naive_run_retrace_ext outer MAE={naive_sc.mae:.5f} r2={naive_sc.r2:.4f} corr={naive_sc.corr:.4f}")

    xcols = [c for c in X_df.columns if c != "oracle_leaky"]
    X_raw = X_df[xcols].to_numpy(dtype=float)
    # drop low-coverage cols
    cov = np.mean(np.isfinite(X_raw), axis=0)
    keep = cov >= 0.85
    xcols = [c for c, k in zip(xcols, keep) if k]
    X_raw = X_df[xcols].to_numpy(dtype=float)
    y = X_df["oracle_leaky"].to_numpy(dtype=float)
    row_ok = np.isfinite(y) & (np.mean(np.isfinite(X_raw), axis=1) >= 0.90)
    X_df = X_df.loc[row_ok].copy()
    y = X_df["oracle_leaky"].to_numpy(dtype=float)
    X_raw = X_df[xcols].to_numpy(dtype=float)
    ts_ms = index_to_ms(X_df.index)
    pre = ts_ms < hunt_end_ms
    med = np.nanmedian(X_raw[pre], axis=0)
    med = np.where(np.isfinite(med), med, 0.0)
    bad = ~np.isfinite(X_raw)
    X_raw[bad] = np.take(med, np.where(bad)[1])
    X = X_raw
    _log(f"matrix n={len(X_df)} feats={len(xcols)}")

    pre_idx = np.where(pre)[0]
    n_val = max(500, int(len(pre_idx) * VAL_FRAC))
    val_i = pre_idx[-n_val:]
    tr_i = pre_idx[:-n_val]
    tr_i = tr_i[np.isfinite(y[tr_i])]
    val_i = val_i[np.isfinite(y[val_i])]
    _log(f"train={tr_i.size} val={val_i.size}")

    # also val score of naive
    nv = recon_scores(y[val_i], X_df["naive_run_as_label"].to_numpy()[val_i])
    _log(f"naive val MAE={nv.mae:.5f} r2={nv.r2:.4f} corr={nv.corr:.4f}")

    trials: list[dict[str, Any]] = []
    models: dict[str, Any] = {}

    # --- LGBM random hunt ---
    _log(f"=== LGBM random hunt n={N_RANDOM} ===")
    for i in range(N_RANDOM):
        params = sample_lgbm_params()
        t1 = time.perf_counter()
        m = fit_lgbm(X[tr_i], y[tr_i], X[val_i], y[val_i], params)
        hat = pred_lgbm(m, X[val_i])
        sc = recon_scores(y[val_i], hat)
        trials.append(
            {
                "model": "lgbm",
                "trial": i,
                "params": {
                    **params,
                    "best_iteration_": int(getattr(m, "best_iteration_", 0) or 0),
                },
                "val": asdict(sc),
                "elapsed_sec": round(time.perf_counter() - t1, 2),
            }
        )
        if i % 10 == 0 or sc.mae < 0.35:
            _log(f"  lgbm {i:02d} mae={sc.mae:.5f} r2={sc.r2:.4f} corr={sc.corr:.4f}")
        models[f"lgbm_{i}"] = m

    lgbm_ranked = sorted(
        [t for t in trials if t["model"] == "lgbm"], key=lambda r: r["val"]["mae"]
    )
    top_lgbm = lgbm_ranked[:5]
    _log(f"best lgbm val mae={top_lgbm[0]['val']['mae']:.5f}")

    # --- HistGradientBoosting ---
    _log("=== HistGradientBoosting ===")
    hgb_grid = [
        {"max_depth": 6, "learning_rate": 0.05, "max_iter": 300, "min_samples_leaf": 40, "l2_regularization": 0.1},
        {"max_depth": 8, "learning_rate": 0.03, "max_iter": 400, "min_samples_leaf": 30, "l2_regularization": 0.5},
        {"max_depth": 10, "learning_rate": 0.02, "max_iter": 500, "min_samples_leaf": 50, "l2_regularization": 1.0},
        {"max_depth": 12, "learning_rate": 0.015, "max_iter": 600, "min_samples_leaf": 25, "l2_regularization": 0.0},
        {"max_depth": 8, "learning_rate": 0.04, "max_iter": 350, "min_samples_leaf": 80, "l2_regularization": 2.0},
    ]
    for i, p in enumerate(hgb_grid):
        t1 = time.perf_counter()
        m = HistGradientBoostingRegressor(loss="absolute_error", random_state=42, **p)
        m.fit(X[tr_i], y[tr_i])
        hat = m.predict(X[val_i])
        sc = recon_scores(y[val_i], hat)
        trials.append(
            {
                "model": "hgb",
                "trial": i,
                "params": p,
                "val": asdict(sc),
                "elapsed_sec": round(time.perf_counter() - t1, 2),
            }
        )
        models[f"hgb_{i}"] = m
        _log(f"  hgb {i} mae={sc.mae:.5f} r2={sc.r2:.4f}")

    # --- ExtraTrees (sample for speed) ---
    _log("=== ExtraTrees ===")
    et = ExtraTreesRegressor(
        n_estimators=200,
        max_depth=20,
        min_samples_leaf=20,
        n_jobs=-1,
        random_state=42,
    )
    t1 = time.perf_counter()
    et.fit(X[tr_i], y[tr_i])
    hat = et.predict(X[val_i])
    sc = recon_scores(y[val_i], hat)
    trials.append(
        {
            "model": "extratrees",
            "trial": 0,
            "params": {"n_estimators": 200, "max_depth": 20},
            "val": asdict(sc),
            "elapsed_sec": round(time.perf_counter() - t1, 2),
        }
    )
    models["extratrees_0"] = et
    _log(f"  et mae={sc.mae:.5f} r2={sc.r2:.4f}")

    # --- blend top LGBMs + best HGB + naive ---
    preds_val = []
    names = []
    for t in top_lgbm:
        key = f"lgbm_{t['trial']}"
        preds_val.append(pred_lgbm(models[key], X[val_i]))
        names.append(key)
    best_hgb = min([t for t in trials if t["model"] == "hgb"], key=lambda r: r["val"]["mae"])
    preds_val.append(models[f"hgb_{best_hgb['trial']}"].predict(X[val_i]))
    names.append(f"hgb_{best_hgb['trial']}")
    preds_val.append(X_df["naive_run_as_label"].to_numpy()[val_i])
    names.append("naive")
    P = np.column_stack(preds_val)
    # ridge blend on val
    ridge = Ridge(alpha=1.0, fit_intercept=True)
    ridge.fit(P, y[val_i])
    blend_val = ridge.predict(P)
    # also plain mean of top3 lgbm
    mean3 = np.mean(np.column_stack(preds_val[:3]), axis=1)
    sc_ridge = recon_scores(y[val_i], blend_val)
    sc_mean = recon_scores(y[val_i], mean3)
    sc_naive = recon_scores(y[val_i], preds_val[-1])
    _log(f"blend ridge val mae={sc_ridge.mae:.5f} mean3={sc_mean.mae:.5f} naive={sc_naive.mae:.5f}")

    # residual model on best single
    best_key = f"lgbm_{top_lgbm[0]['trial']}"
    base_hat_tr = pred_lgbm(models[best_key], X[tr_i])
    base_hat_va = pred_lgbm(models[best_key], X[val_i])
    resid_tr = y[tr_i] - base_hat_tr
    resid_m = fit_lgbm(
        X[tr_i],
        resid_tr,
        X[val_i],
        y[val_i] - base_hat_va,
        {
            "n_estimators": 300,
            "learning_rate": 0.02,
            "num_leaves": 31,
            "min_child_samples": 60,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "reg_lambda": 2.0,
            "reg_alpha": 0.2,
        },
    )
    resid_hat_va = pred_lgbm(resid_m, X[val_i])
    two_stage_va = base_hat_va + resid_hat_va
    sc_2s = recon_scores(y[val_i], two_stage_va)
    _log(f"two_stage val mae={sc_2s.mae:.5f} r2={sc_2s.r2:.4f}")

    candidates = {
        "best_lgbm": base_hat_va,
        "ridge_blend": blend_val,
        "mean_top3_lgbm": mean3,
        "naive_run": preds_val[-1],
        "two_stage": two_stage_va,
        "hgb_best": models[f"hgb_{best_hgb['trial']}"].predict(X[val_i]),
    }
    # pick best val
    pick_name, pick_val = min(
        ((n, recon_scores(y[val_i], h)) for n, h in candidates.items()),
        key=lambda kv: kv[1].mae,
    )
    _log(f"VAL PICK {pick_name} mae={pick_val.mae:.5f} r2={pick_val.r2:.4f} corr={pick_val.corr:.4f}")

    # full-series predictions for delivery
    full_preds = {}
    for t in top_lgbm:
        full_preds[f"lgbm_{t['trial']}"] = pred_lgbm(models[f"lgbm_{t['trial']}"], X)
    full_preds[f"hgb_{best_hgb['trial']}"] = models[f"hgb_{best_hgb['trial']}"].predict(X)
    full_preds["naive"] = X_df["naive_run_as_label"].to_numpy(dtype=float)
    cols_p = []
    for n in names:
        if n == "naive":
            cols_p.append(full_preds["naive"])
        else:
            cols_p.append(full_preds[n])
    P_full = np.column_stack(cols_p)
    full_ridge = ridge.predict(P_full)
    full_best = full_preds[best_key]
    full_2s = full_best + pred_lgbm(resid_m, X)
    full_mean3 = np.mean(
        np.column_stack([full_preds[f"lgbm_{t['trial']}"] for t in top_lgbm[:3]]),
        axis=1,
    )

    delivery_map = {
        "best_lgbm": full_best,
        "ridge_blend": full_ridge,
        "mean_top3_lgbm": full_mean3,
        "naive_run": full_preds["naive"],
        "two_stage": full_2s,
        "hgb_best": full_preds[f"hgb_{best_hgb['trial']}"],
    }
    hat = delivery_map[pick_name]

    oi = np.where((ts_ms >= outer0_ms) & (ts_ms < outer1_ms))[0]
    outer_sc = recon_scores(y[oi], hat[oi])
    outer_by = {n: asdict(recon_scores(y[oi], delivery_map[n][oi])) for n in delivery_map}
    _log(f"OUTER delivery={pick_name} mae={outer_sc.mae:.5f} r2={outer_sc.r2:.4f} corr={outer_sc.corr:.4f} "
         f"within05={outer_sc.pct_within_005:.3f} within10={outer_sc.pct_within_010:.3f}")
    for n, scd in sorted(outer_by.items(), key=lambda kv: kv[1]["mae"]):
        _log(f"  outer {n}: mae={scd['mae']:.5f} r2={scd['r2']:.4f} corr={scd['corr']:.4f}")

    # importance from best lgbm
    bi = models[best_key].feature_importances_
    top_imp = sorted(zip(xcols, bi), key=lambda z: -z[1])[:25]
    _log("top features: " + ", ".join(f"{a}:{b}" for a, b in top_imp[:12]))

    series = pd.DataFrame(
        {
            "oracle_leaky": y,
            "pred_leaky": hat,
            "naive_run": full_preds["naive"],
            "best_lgbm": full_best,
            "two_stage": full_2s,
            "ridge_blend": full_ridge,
        },
        index=X_df.index,
    )
    series.to_parquet(OUT_DIR / "leaky_asof_series.parquet")
    joblib.dump(
        {
            "pick": pick_name,
            "feature_columns": xcols,
            "medians": med.tolist(),
            "ridge_coef": ridge.coef_.tolist(),
            "ridge_intercept": float(ridge.intercept_),
            "top_lgbm_trials": [t["trial"] for t in top_lgbm],
            "best_hgb_trial": best_hgb["trial"],
            "models": {k: models[k] for k in list(models) if k.startswith("lgbm_") and int(k.split("_")[1]) in {t["trial"] for t in top_lgbm}}
            | {f"hgb_{best_hgb['trial']}": models[f"hgb_{best_hgb['trial']}"], "resid": resid_m, "ridge": ridge},
            "top_importances": top_imp,
            "target": "oracle_leaky",
            "note": "CAUSAL running-retrace features; still predicting look-ahead label",
        },
        MODEL_DIR / "proxy_leaky_asof_max.joblib",
    )

    # trade retest
    pred_s = series["pred_leaky"]
    oracle_s = series["oracle_leaky"]
    trade_results = []
    for arm, fill in (
        ("oracle_leaky", oracle_s),
        ("pred_leaky", pred_s),
        ("naive_run_as_retrace", series["naive_run"]),
    ):
        _log(f"=== trade {arm} ===")
        fmat = fill_retrace(struct, fill.reindex(struct.index))
        tr = run_trade(ohlcv, fmat, arm=arm, outer0=outer0, outer1=outer1, lock=lock)
        trade_results.append(tr)
        _log(
            f"  {arm}: n={tr.get('n_trades')} pf={tr.get('profit_factor')} "
            f"E[r]={tr.get('expectancy_return_units')}"
        )

    report = {
        "evidence_class": "LEAKY_PROXY_ASOF_MAX",
        "maximum_earned_readiness": "LIVE_STOP / RESEARCH_ONLY",
        "promotion_allowed": False,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "target": "oracle_leaky_only",
        "causal_features_only": True,
        "n_features": len(xcols),
        "n_lgbm_trials": N_RANDOM,
        "val_pick": pick_name,
        "val_scores": asdict(pick_val),
        "outer_delivery": asdict(outer_sc),
        "outer_all_candidates": outer_by,
        "naive_outer": asdict(naive_sc),
        "top_importances": top_imp,
        "top5_lgbm_val": [t["val"] for t in top_lgbm],
        "trade_arms": trade_results,
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "ceiling_note": (
            "Even perfect causal running-retrace cannot fully match oracle_leaky "
            "because the label is frozen only at the NEXT opposite swing confirm. "
            "If outer MAE still >> 0 or trade fails, residual is future structure."
        ),
        "artifacts": {
            "series": str(OUT_DIR / "leaky_asof_series.parquet"),
            "model": str(MODEL_DIR / "proxy_leaky_asof_max.joblib"),
        },
    }
    latest = OUT_DIR / "leaky_proxy_asof_max_001_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    _log(f"wrote {latest}")
    _log(
        "SUMMARY "
        + json.dumps(
            {
                "pick": pick_name,
                "outer": asdict(outer_sc),
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
        context="train_leaky_proxy_asof_max.py (oracle_leaky MAE hunt + trade retest)"
    )
    raise SystemExit(main())
