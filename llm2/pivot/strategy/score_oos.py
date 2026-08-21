"""Walk-forward score outer folds: calibrated any, high|event, level, time."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import lightgbm as lgb
import numpy as np
import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.paths import FORWARD_LOCKBOX_START
from llm2.pivot.labels.config import PivotLabelConfig
from llm2.pivot.train.calibration import apply_calibrator, fit_binary_calibrator
from llm2.pivot.train.multihead import (
    _fit_predict_binary,
    _fit_predict_reg,
    expected_calibration_error,
)
from llm2.pivot.train.samples import build_samples
from llm2.pivot.train.walk_forward import ModelSpec
from llm2.validation.folds import build_outer_folds, index_to_ms


@dataclass
class ScoredOOS:
    symbol: str
    timeframe: str
    ohlcv: pd.DataFrame
    ts_ms: np.ndarray
    close: np.ndarray
    atr_frac: np.ndarray
    p_any: np.ndarray
    p_high: np.ndarray
    level_ret: np.ndarray
    time_bars: np.ndarray
    y_any: np.ndarray
    y_high: np.ndarray
    y_level: np.ndarray
    y_time: np.ndarray
    thr_any: np.ndarray  # per-row fold threshold (cal p75)
    level_mae_train: np.ndarray  # train-fold MAE at decision row for asym SL
    level_p90_train: np.ndarray
    ece_folds: list[dict]
    frac_any: float
    n_rows: int
    level_mode: str = "ret"  # ret | atr | q50
    horizon_bars: int = 4
    confirm_bars: int = 3
    next_level_ret: np.ndarray | None = None
    next_time_bars: np.ndarray | None = None
    y_next_level: np.ndarray | None = None
    y_next_time: np.ndarray | None = None
    next_level_p90_train: np.ndarray | None = None
    frac_next: float = float("nan")


def _lgbm_cls() -> ModelSpec:
    return ModelSpec(
        "lgbm_m",
        lambda: lgb.LGBMClassifier(
            n_estimators=200,
            num_leaves=31,
            learning_rate=0.05,
            class_weight="balanced",
            verbosity=-1,
            random_state=20260810,
        ),
    )


def _atr_frac(ohlcv: pd.DataFrame, period: int = 14) -> np.ndarray:
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    prev_c = np.roll(c, 1)
    prev_c[0] = c[0]
    tr = np.maximum(h - l, np.maximum(np.abs(h - prev_c), np.abs(l - prev_c)))
    atr = pd.Series(tr).ewm(alpha=1.0 / period, adjust=False).mean().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        out = atr / np.where(c > 0, c, np.nan)
    return out.astype(float)


def default_label_cfg(
    *, timeframe: str = "15m", atr_min: float = 2.0, confirm_bars: int = 3
) -> PivotLabelConfig:
    right = 3
    confirm = max(int(confirm_bars), right)
    return PivotLabelConfig(
        timeframe=timeframe,
        left_bars=3,
        right_bars=right,
        confirm_bars=confirm,
        min_left_prominence_atr=atr_min,
        min_right_reversal_atr=atr_min,
        min_reversal_pct=0.0015,
        atr_period=14,
        label_family="fractal_stack",
        suppress_neighbor_bars=3,
    )


def score_symbol_oos(
    symbol: str,
    *,
    timeframe: str = "15m",
    horizon_bars: int = 4,
    atr_min: float = 2.0,
    feature_pack: str = "price_vol_mom",
    max_rows: int = 120_000,
    level_mode: str = "ret",
    confirm_bars: int = 3,
    predict_next: bool = True,
) -> ScoredOOS:
    cfg = default_label_cfg(
        timeframe=timeframe, atr_min=atr_min, confirm_bars=confirm_bars
    )
    ms = _lgbm_cls()
    samp = build_samples(
        symbol=symbol,
        timeframe=timeframe,
        feature_pack=feature_pack,
        label_cfg=cfg,
        horizon_bars=horizon_bars,
        max_rows=max_rows,
    )
    X, ts = samp["X"], samp["ts_ms"]
    y_any, y_high = samp["y_any"], samp["y_high_given"]
    y_level, y_time = samp["y_level_ret"], samp["y_time_bars"]
    y_next_level = np.asarray(samp.get("y_next_level_ret"), dtype=float)
    y_next_time = np.asarray(samp.get("y_next_time_bars"), dtype=float)
    if y_next_level.shape != y_level.shape:
        y_next_level = np.full(len(y_level), np.nan)
        y_next_time = np.full(len(y_level), np.nan)

    ohlcv = load_ohlcv(symbol, timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    if max_rows and len(ohlcv) > max_rows:
        ohlcv = ohlcv.iloc[-max_rows:].copy()
    ohlcv_ts = index_to_ms(ohlcv.index)
    close_map = dict(zip(ohlcv_ts.tolist(), ohlcv["close"].to_numpy(dtype=float).tolist()))
    atr_map = dict(zip(ohlcv_ts.tolist(), _atr_frac(ohlcv).tolist()))
    closes = np.array([close_map.get(int(t), np.nan) for t in ts], dtype=float)
    atrs = np.array([atr_map.get(int(t), np.nan) for t in ts], dtype=float)

    purge = max(horizon_bars + 6, int(samp.get("next_horizon_bars", horizon_bars)) + 2, 24)
    folds = build_outer_folds(ts, purge_bars=purge, embargo_bars=purge)

    p_any = np.full(len(ts), np.nan)
    p_high = np.full(len(ts), np.nan)
    level = np.full(len(ts), np.nan)
    time_p = np.full(len(ts), np.nan)
    next_lv = np.full(len(ts), np.nan)
    next_tm = np.full(len(ts), np.nan)
    next_p90 = np.full(len(ts), np.nan)
    thr = np.full(len(ts), np.nan)
    tr_mae = np.full(len(ts), np.nan)
    tr_p90 = np.full(len(ts), np.nan)
    ece_folds: list[dict] = []

    for fold in folds:
        tr, te = fold.train_indices, fold.oos_indices
        if tr.size < 800 or te.size < 100:
            continue
        cut = int(tr.size * 0.8)
        tr_fit, tr_cal = tr[:cut], tr[cut:]
        if tr_cal.size < 100:
            tr_fit, tr_cal = tr, tr[-max(100, tr.size // 10) :]

        p_cal_raw = _fit_predict_binary(
            X[tr_fit], y_any[tr_fit], X[tr_cal], model_spec=ms, is_baserate=False
        )
        # Calibration-first: pick isotonic vs Platt by lower inner-cal ECE (hold ECE).
        cal_iso = fit_binary_calibrator(y_any[tr_cal], p_cal_raw, method="isotonic")
        cal_platt = fit_binary_calibrator(y_any[tr_cal], p_cal_raw, method="platt")
        p_iso = apply_calibrator(cal_iso, p_cal_raw)
        p_platt = apply_calibrator(cal_platt, p_cal_raw)
        ece_iso = expected_calibration_error(y_any[tr_cal], p_iso)
        ece_platt = expected_calibration_error(y_any[tr_cal], p_platt)
        if np.isfinite(ece_platt) and (not np.isfinite(ece_iso) or ece_platt < ece_iso):
            cal_any, cal_method, p_cal_cal, ece_inner = cal_platt, "platt", p_platt, ece_platt
        else:
            cal_any, cal_method, p_cal_cal, ece_inner = cal_iso, "isotonic", p_iso, ece_iso
        p_te_raw = _fit_predict_binary(
            X[tr], y_any[tr], X[te], model_spec=ms, is_baserate=False
        )
        p_te = apply_calibrator(cal_any, p_te_raw)
        p_any[te] = p_te
        thr_v = max(float(np.nanpercentile(p_cal_cal, 75)), 0.35)
        thr[te] = thr_v
        ece_folds.append(
            {
                "fold": fold.fold_index,
                "cal_method": cal_method,
                "ece_inner_raw": expected_calibration_error(y_any[tr_cal], p_cal_raw),
                "ece_inner_cal": float(ece_inner) if np.isfinite(ece_inner) else float("nan"),
                "ece_outer_cal": expected_calibration_error(y_any[te], p_te),
            }
        )

        tr_ev = tr[y_high[tr] >= 0]
        p_high_te = np.full(te.size, 0.5)
        if tr_ev.size >= 80:
            p_high_all = _fit_predict_binary(
                X[tr_ev], y_high[tr_ev], X[te], model_spec=ms, is_baserate=False
            )
            tr_cal_ev = tr_cal[y_high[tr_cal] >= 0]
            if tr_cal_ev.size >= 40:
                p_hg_cal_raw = _fit_predict_binary(
                    X[tr_ev], y_high[tr_ev], X[tr_cal_ev], model_spec=ms, is_baserate=False
                )
                cal_hg = fit_binary_calibrator(
                    y_high[tr_cal_ev], p_hg_cal_raw, method="isotonic"
                )
                p_high_te = apply_calibrator(cal_hg, p_high_all)
            else:
                p_high_te = p_high_all
        p_high[te] = p_high_te

        # Level head: ret | ATR-normalized (convert back to ret) | quantile 0.5 ret
        q_alpha = 0.5 if level_mode == "q50" else None
        y_lv_tr = y_level.copy()
        atr_te = atrs[te]
        if level_mode == "atr":
            with np.errstate(divide="ignore", invalid="ignore"):
                y_lv_tr = np.where(
                    np.isfinite(atrs) & (atrs > 1e-8),
                    y_level / atrs,
                    np.nan,
                )

        tr_lv = tr[np.isfinite(y_lv_tr[tr])]
        level_te = np.zeros(te.size)
        mae_v, p90_v = float("nan"), float("nan")
        if tr_lv.size >= 50:
            tr_fit_lv = tr_fit[np.isfinite(y_lv_tr[tr_fit])]
            tr_cal_lv = tr_cal[np.isfinite(y_lv_tr[tr_cal])]
            if tr_fit_lv.size >= 40 and tr_cal_lv.size >= 20:
                pred_cal = _fit_predict_reg(
                    X[tr_fit_lv],
                    y_lv_tr[tr_fit_lv],
                    X[tr_cal_lv],
                    model_name="lgbm",
                    is_baserate=False,
                    quantile_alpha=q_alpha,
                )
                # MAE always in return space for comparability
                if level_mode == "atr":
                    pred_cal_ret = pred_cal * atrs[tr_cal_lv]
                    y_cal_ret = y_level[tr_cal_lv]
                else:
                    pred_cal_ret = pred_cal
                    y_cal_ret = y_level[tr_cal_lv]
                res = np.abs(pred_cal_ret - y_cal_ret)
                res = res[np.isfinite(res)]
                if res.size:
                    mae_v = float(res.mean())
                    p90_v = float(np.percentile(res, 90))
            level_raw = _fit_predict_reg(
                X[tr_lv],
                y_lv_tr[tr_lv],
                X[te],
                model_name="lgbm",
                is_baserate=False,
                quantile_alpha=q_alpha,
            )
            if level_mode == "atr":
                level_te = level_raw * atr_te
            else:
                level_te = level_raw
        level[te] = level_te
        tr_mae[te] = mae_v
        tr_p90[te] = p90_v

        tr_tm = tr[np.isfinite(y_time[tr])]
        if tr_tm.size >= 50:
            time_p[te] = _fit_predict_reg(
                X[tr_tm],
                y_time[tr_tm],
                X[te],
                model_name="lgbm",
                is_baserate=False,
            )
        else:
            time_p[te] = float(horizon_bars) / 2.0

        if predict_next:
            tr_nl = tr[np.isfinite(y_next_level[tr])]
            p90_n = float("nan")
            if tr_nl.size >= 50:
                tr_cal_nl = tr_cal[np.isfinite(y_next_level[tr_cal])]
                if tr_cal_nl.size >= 20:
                    pred_cal_n = _fit_predict_reg(
                        X[tr_nl],
                        y_next_level[tr_nl],
                        X[tr_cal_nl],
                        model_name="lgbm",
                        is_baserate=False,
                    )
                    res_n = np.abs(pred_cal_n - y_next_level[tr_cal_nl])
                    res_n = res_n[np.isfinite(res_n)]
                    if res_n.size:
                        p90_n = float(np.percentile(res_n, 90))
                next_lv[te] = _fit_predict_reg(
                    X[tr_nl],
                    y_next_level[tr_nl],
                    X[te],
                    model_name="lgbm",
                    is_baserate=False,
                )
            next_p90[te] = p90_n
            tr_nt = tr[np.isfinite(y_next_time[tr])]
            if tr_nt.size >= 50:
                next_tm[te] = _fit_predict_reg(
                    X[tr_nt],
                    y_next_time[tr_nt],
                    X[te],
                    model_name="lgbm",
                    is_baserate=False,
                )

    mask = np.isfinite(p_any)
    nxt_ok = predict_next and np.isfinite(next_lv).any()
    return ScoredOOS(
        symbol=symbol,
        timeframe=timeframe,
        ohlcv=ohlcv,
        ts_ms=ts[mask],
        close=closes[mask],
        atr_frac=atrs[mask],
        p_any=p_any[mask],
        p_high=p_high[mask],
        level_ret=level[mask],
        time_bars=time_p[mask],
        y_any=y_any[mask],
        y_high=y_high[mask],
        y_level=y_level[mask],
        y_time=y_time[mask],
        thr_any=thr[mask],
        level_mae_train=tr_mae[mask],
        level_p90_train=tr_p90[mask],
        ece_folds=ece_folds,
        frac_any=float(samp["frac_any"]),
        n_rows=int(mask.sum()),
        level_mode=str(level_mode),
        horizon_bars=int(horizon_bars),
        confirm_bars=int(cfg.confirm_bars),
        next_level_ret=next_lv[mask] if nxt_ok else None,
        next_time_bars=next_tm[mask] if nxt_ok else None,
        y_next_level=y_next_level[mask],
        y_next_time=y_next_time[mask],
        next_level_p90_train=next_p90[mask] if nxt_ok else None,
        frac_next=float(samp.get("frac_next", float("nan"))),
    )


def gate_mask(
    scored: ScoredOOS,
    *,
    mode: str,
    tp: float,
    sl: float,
    pi_star: float | None = None,
    level_band_atr: float = 2.0,
    max_abs_level: float = 0.03,
    min_abs_level: float = 0.0015,
) -> np.ndarray:
    """Boolean gate on scored rows. Modes are preregistered composition rules."""
    base = scored.p_any >= scored.thr_any
    if mode == "p75":
        return base
    if mode == "pi_star":
        thr = float(pi_star if pi_star is not None else 0.55)
        return base & (scored.p_any >= thr)
    if mode == "pi_star_level":
        thr = float(pi_star if pi_star is not None else 0.55)
        abs_lr = np.abs(scored.level_ret)
        band = (abs_lr >= min_abs_level) & (abs_lr <= max_abs_level)
        # Distance band + pi* only. Do NOT hard-fail on train MAE vs ATR here:
        # while MAE is still ~1% that filter empties the book (seen in stack runs).
        _ = level_band_atr  # reserved for a future soft penalty, not a hard gate
        return base & (scored.p_any >= thr) & band
    raise ValueError(f"unknown gate mode {mode!r}")


def limit_price_side(scored: ScoredOOS, mask: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return (ts, side_is_short, limit_px) for gated rows."""
    idx = np.flatnonzero(mask)
    ts = scored.ts_ms[idx]
    p_high = scored.p_high[idx]
    c = scored.close[idx]
    lr = scored.level_ret[idx]
    is_short = p_high >= 0.5
    lim = np.empty(len(idx), dtype=float)
    for j in range(len(idx)):
        if is_short[j]:
            move = float(np.clip(lr[j] if np.isfinite(lr[j]) else 0.005, 0.0015, 0.03))
            lim[j] = float(c[j]) * (1.0 + move)
        else:
            move = float(np.clip(lr[j] if np.isfinite(lr[j]) else -0.005, -0.03, -0.0015))
            lim[j] = float(c[j]) * (1.0 + move)
    return ts, is_short, lim
