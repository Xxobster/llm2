"""Nest forecast filters on a frozen tp1/sl2/hold6 direction baseline.

Preregister: ``configs/preregister/structure_v1_forecast_filter_on_direction_001.yaml``.

- Baseline sides come from a causal OOS direction model (pack geometry only).
- ``next_retrace`` / ``next_vol`` forecasts may only skip; they never set side.
- Forecast-model choice uses inner-fold Spearman IC only.
- Trading Profit Factor is reported separately from forecast skill.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import (  # noqa: E402
    Side,
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
)

from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.runner import _make_model  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND  # noqa: E402
from llm2.signals.rules import direction_gate  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.labels.next_retrace import build_next_retrace_sparse_frame  # noqa: E402
from llm2.labels.next_vol import build_next_vol_labels  # noqa: E402
from llm2.paths import FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    build_outer_folds,
    index_to_ms,
    make_inner_folds,
)

TP = 0.01
SL = 0.02
HOLD = 6
MIN_EDGE = 0.1
HORIZON = 6
VOL_HORIZON = 24
DEEP_THRESH = 0.5
SCORE_MIN = 0.05
SPACE = "structure_v1"
TF = "1h"
SEED = 20260806


@dataclass(frozen=True)
class ArmFoldMetrics:
    arm: str
    fold: int
    n_signals: int
    n_trades: int
    profit_factor: float
    net_pnl: float
    win_rate: float


def _lock_cut(ohlcv: pd.DataFrame) -> pd.DataFrame:
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    return ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()


def _pred_mean(model: Any, X: np.ndarray) -> np.ndarray:
    pred = model.predict(X)
    return np.asarray(pred.mean if hasattr(pred, "mean") else pred, dtype=float).reshape(-1)


def _spearman_ic(y: np.ndarray, p: np.ndarray) -> float:
    from scipy import stats

    m = np.isfinite(y) & np.isfinite(p)
    if int(m.sum()) < 10:
        return float("nan")
    yt, yp = y[m], p[m]
    if float(np.std(yp)) < 1e-12 or float(np.std(yt)) < 1e-12:
        return float("nan")
    return float(stats.spearmanr(yt, yp).statistic)


def select_model_inner_ic(
    *,
    model_names: Sequence[str],
    X: np.ndarray,
    y: np.ndarray,
    train_indices: np.ndarray,
    horizon: int,
) -> tuple[str, float]:
    """Pick forecast model by mean inner-fold Spearman IC (never trading PF)."""
    best_name = str(model_names[0])
    best_ic = float("-inf")
    inner = make_inner_folds(
        train_indices, n_folds=3, purge_bars=horizon, embargo_bars=horizon
    )
    for name in model_names:
        try:
            _make_model(name)
        except Exception:  # noqa: BLE001
            continue
        ics: list[float] = []
        for inn in inner:
            tr_rel = np.arange(0, inn.train_end, dtype=np.int64)
            va_rel = np.arange(inn.val_start, inn.val_end, dtype=np.int64)
            if tr_rel.size < 80 or va_rel.size < 20:
                continue
            tr = train_indices[tr_rel]
            va = train_indices[va_rel]
            model = _make_model(name)
            model.fit(X[tr], y[tr])
            ic = _spearman_ic(y[va], _pred_mean(model, X[va]))
            if np.isfinite(ic):
                ics.append(ic)
        mean_ic = float(np.mean(ics)) if ics else float("-inf")
        if mean_ic > best_ic:
            best_ic = mean_ic
            best_name = str(name)
    return best_name, best_ic


def asof_sparse_to_bars(
    bar_ms: np.ndarray,
    decision_ms: np.ndarray,
    values: np.ndarray,
) -> np.ndarray:
    """Forward-fill sparse decision values onto bars (causal as-of)."""
    out = np.full(len(bar_ms), np.nan, dtype=float)
    if len(decision_ms) == 0:
        return out
    order = np.argsort(decision_ms)
    d = decision_ms[order]
    v = values[order]
    j = np.searchsorted(d, bar_ms, side="right") - 1
    ok = j >= 0
    out[ok] = v[j[ok]]
    return out


def retrace_agree_mask(
    *,
    side: np.ndarray,
    pred_retrace: np.ndarray,
    leg_dir: np.ndarray,
) -> np.ndarray:
    """Keep baseline side only when forecast score agrees (skip otherwise)."""
    score = leg_dir * (DEEP_THRESH - pred_retrace)
    agree = (
        np.isfinite(score)
        & np.isfinite(pred_retrace)
        & (np.abs(score) >= SCORE_MIN)
        & (np.sign(side) == np.sign(score))
        & (side != 0)
    )
    return agree


def vol_skip_mask(pred_vol: np.ndarray, *, threshold: float) -> np.ndarray:
    """True = keep. Skip when predicted vol exceeds train-fold threshold."""
    return np.isfinite(pred_vol) & (pred_vol <= float(threshold))


def sides_to_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    *,
    pred_mean: np.ndarray | None = None,
    tag: str = "",
) -> list[Signal]:
    signals: list[Signal] = []
    for i in range(len(ts_ms)):
        s = int(side[i])
        if s == 0:
            continue
        meta: dict[str, Any] = {"arm": tag}
        if pred_mean is not None and np.isfinite(pred_mean[i]):
            meta["pred_mean"] = float(pred_mean[i])
        signals.append(
            Signal(
                ts_ms=int(ts_ms[i]),
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=SL,
                target_offset=TP,
                max_hold_bars=HOLD,
                tag=tag,
                meta=meta,
            )
        )
    return signals


def _bt_metrics(
    ohlcv: pd.DataFrame,
    signals: list[Signal],
    *,
    symbol: str,
    fold_index: int,
    arm: str,
) -> dict[str, float]:
    if not signals:
        return {
            "n_signals": 0.0,
            "n_trades": 0.0,
            "profit_factor": 0.0,
            "net_pnl": 0.0,
            "win_rate": float("nan"),
        }
    touch_tf = touch_timeframe(TF, symbol)
    touch = load_ohlcv(symbol, touch_tf)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    touch = touch.loc[touch.index < lock]
    funding = load_funding(symbol)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)

    sig_ts = np.asarray([s.ts_ms for s in signals], dtype=np.int64)
    bar_ms = index_to_ms(ohlcv.index)
    i0 = int(np.searchsorted(bar_ms, int(sig_ts.min()), side="left"))
    i1 = int(np.searchsorted(bar_ms, int(sig_ts.max()), side="right"))
    pad = max(50, HOLD * 4)
    lo = max(0, i0 - pad)
    hi = min(len(ohlcv), i1 + pad)
    window = ohlcv.iloc[lo:hi]
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    end, start = window.index[-1], window.index[0]
    dec_ms = int(TF_MS[TF])
    touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
    touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]

    lev = float(leverage_from_stop(SL))
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=symbol,
        timeframe=TF,
        strategy_id=f"ffod_{symbol.lower()}_{arm}_f{fold_index}",
        touch_ohlcv=touch_win if len(touch_win) else None,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim(max_hold_bars=HOLD, decision_timeframe=TF),
        instrument=research_instrument(symbol),
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    return {
        "n_signals": float(len(signals)),
        "n_trades": float(m.n_trades),
        "profit_factor": float(m.profit_factor),
        "net_pnl": float(m.net_pnl),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
    }


def run_symbol(symbol: str) -> dict[str, Any]:
    """Causal baseline + preregistered filter arms on outer folds."""
    ohlcv = _lock_cut(load_ohlcv(symbol, TF))
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TF)
    y_dir = build_direction_labels(ohlcv, horizon=HORIZON)["direction"]
    y_vol = build_next_vol_labels(ohlcv, horizon=VOL_HORIZON)
    y_fwd = build_fwd_return_labels(ohlcv, horizon=HORIZON)["fwd_return"]
    sparse = build_next_retrace_sparse_frame(symbol, TF)

    aligned = feats.join(y_dir.rename("direction"), how="inner")
    aligned = aligned.join(y_vol.rename("next_vol"), how="left")
    aligned = aligned.join(y_fwd.rename("fwd_return"), how="left")
    aligned = aligned.replace([np.inf, -np.inf], np.nan).dropna(
        subset=list(feats.columns) + ["direction"]
    )
    X_cols = list(feats.columns)
    X = aligned[X_cols].to_numpy(dtype=float)
    y_d = aligned["direction"].to_numpy(dtype=float)
    y_v = aligned["next_vol"].to_numpy(dtype=float)
    y_f = aligned["fwd_return"].to_numpy(dtype=float)
    ts = index_to_ms(aligned.index)
    folds = build_outer_folds(ts, purge_bars=HORIZON, embargo_bars=HORIZON)

    # Sparse retrace matrix aligned via as-of from features at decision.
    feat_ms_full = index_to_ms(feats.index)
    dec = sparse["decision_ts_ms"].to_numpy(dtype=np.int64)
    j = np.searchsorted(feat_ms_full, dec, side="right") - 1
    ok = j >= 0
    X_sp_all = feats.to_numpy(dtype=float)[j[ok]]
    finite = np.all(np.isfinite(X_sp_all), axis=1)
    idx = np.flatnonzero(ok)[finite]
    X_sp = X_sp_all[finite]
    y_sp = sparse["next_retrace_pct"].to_numpy(dtype=float)[idx]
    known_sp = sparse["known_ts_ms"].to_numpy(dtype=np.int64)[idx]
    ts_sp = dec[idx]
    leg_sp = sparse["leg_dir"].to_numpy(dtype=float)[idx]

    retrace_models = ("ridge", "lgbm_regressor")
    vol_models = ("ridge", "lgbm_regressor", "torch_mlp")
    try:
        _make_model("torch_mlp")
    except Exception:  # noqa: BLE001
        vol_models = ("ridge", "lgbm_regressor")

    arm_names = ("control", "next_retrace_agree_skip", "next_vol_skip_p75")
    fold_rows: list[dict[str, Any]] = []
    skill_rows: list[dict[str, Any]] = []
    model_picks: list[dict[str, Any]] = []

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        # --- direction baseline (geometry frozen; model causal per fold) ---
        dir_model = _make_model("lgbm_regressor")
        dir_model.fit(X[tr], y_d[tr])
        dir_pred = _pred_mean(dir_model, X[oos])
        # Frozen pack min_edge=0.1 matches DIRECTION_BAND for direction target.
        _ = MIN_EDGE  # preregistered; assert equality with direction gate
        assert abs(float(MIN_EDGE) - float(DIRECTION_BAND)) < 1e-12
        base_side = direction_gate(dir_pred, threshold=MIN_EDGE).astype(np.int8)

        # --- next_retrace forecast: inner pick + outer pred ---
        oos_start = int(ts[oos].min()) if oos.size else 0
        sp_tr = np.flatnonzero((ts_sp < oos_start) & (known_sp < oos_start))
        sp_te = np.flatnonzero((ts_sp >= int(fold.oos_start_ms)) & (ts_sp < int(fold.oos_end_ms)))
        retr_name, retr_inner_ic = ("ridge", float("nan"))
        retr_oos = np.full(len(ts_sp), np.nan)
        if sp_tr.size >= 80:
            retr_name, retr_inner_ic = select_model_inner_ic(
                model_names=retrace_models,
                X=X_sp,
                y=y_sp,
                train_indices=sp_tr,
                horizon=HORIZON,
            )
            rm = _make_model(retr_name)
            rm.fit(X_sp[sp_tr], y_sp[sp_tr])
            if sp_te.size:
                retr_oos[sp_te] = _pred_mean(rm, X_sp[sp_te])
            # skill on outer sparse
            if sp_te.size:
                skill_rows.append(
                    {
                        "fold": fold.fold_index,
                        "target": "next_retrace_pct",
                        "model": retr_name,
                        "inner_ic": retr_inner_ic,
                        "outer_ic": _spearman_ic(y_sp[sp_te], retr_oos[sp_te]),
                        "n_oos": int(sp_te.size),
                    }
                )

        pred_retr_bars = asof_sparse_to_bars(ts[oos], ts_sp, retr_oos)
        leg_bars = asof_sparse_to_bars(ts[oos], ts_sp, leg_sp)

        # --- next_vol forecast: inner pick + outer pred ---
        vol_tr = tr[np.isfinite(y_v[tr])]
        vol_name, vol_inner_ic = ("ridge", float("nan"))
        vol_pred = np.full(len(oos), np.nan)
        vol_thr = float("inf")
        if vol_tr.size >= 200:
            vol_name, vol_inner_ic = select_model_inner_ic(
                model_names=vol_models,
                X=X,
                y=y_v,
                train_indices=vol_tr,
                horizon=VOL_HORIZON,
            )
            vm = _make_model(vol_name)
            vm.fit(X[vol_tr], y_v[vol_tr])
            # threshold from train predictions only
            vol_tr_pred = _pred_mean(vm, X[vol_tr])
            vol_thr = float(np.nanpercentile(vol_tr_pred, 75))
            vol_pred = _pred_mean(vm, X[oos])
            skill_rows.append(
                {
                    "fold": fold.fold_index,
                    "target": "next_vol",
                    "model": vol_name,
                    "inner_ic": vol_inner_ic,
                    "outer_ic": _spearman_ic(y_v[oos], vol_pred),
                    "n_oos": int(oos.size),
                    "train_p75": vol_thr,
                }
            )
            # fwd_return skill (reporting only — never used as a filter head here)
            fwd_tr = tr[np.isfinite(y_f[tr])]
            if fwd_tr.size >= 200:
                fm = _make_model("lgbm_regressor")
                fm.fit(X[fwd_tr], y_f[fwd_tr])
                skill_rows.append(
                    {
                        "fold": fold.fold_index,
                        "target": "fwd_return",
                        "model": "lgbm_regressor",
                        "inner_ic": float("nan"),
                        "outer_ic": _spearman_ic(y_f[oos], _pred_mean(fm, X[oos])),
                        "n_oos": int(np.isfinite(y_f[oos]).sum()),
                        "note": "reporting_only_not_used_for_filter",
                    }
                )

        model_picks.append(
            {
                "fold": fold.fold_index,
                "next_retrace_model": retr_name,
                "next_retrace_inner_ic": retr_inner_ic,
                "next_vol_model": vol_name,
                "next_vol_inner_ic": vol_inner_ic,
                "vol_train_p75": vol_thr,
            }
        )

        # --- arms ---
        keep_retrace = retrace_agree_mask(
            side=base_side, pred_retrace=pred_retr_bars, leg_dir=leg_bars
        )
        keep_vol = vol_skip_mask(vol_pred, threshold=vol_thr)

        arm_sides = {
            "control": base_side,
            "next_retrace_agree_skip": np.where(keep_retrace, base_side, 0).astype(np.int8),
            "next_vol_skip_p75": np.where(keep_vol, base_side, 0).astype(np.int8),
        }
        oos_ts = ts[oos]
        for arm in arm_names:
            sigs = sides_to_signals(
                oos_ts, arm_sides[arm], pred_mean=dir_pred, tag=arm
            )
            metrics = _bt_metrics(
                ohlcv, sigs, symbol=symbol, fold_index=fold.fold_index, arm=arm
            )
            fold_rows.append(
                {
                    "arm": arm,
                    "fold": fold.fold_index,
                    **metrics,
                }
            )

    # Pool per arm
    pooled: dict[str, Any] = {}
    for arm in arm_names:
        rows = [r for r in fold_rows if r["arm"] == arm]
        pnls = [float(r["net_pnl"]) for r in rows]
        # Recompute pooled PF from fold trades is approximate; use PnL-weighted proxy:
        # report mean fold PF and sum pnl; full pooled PF would need trade lists.
        pfs = [float(r["profit_factor"]) for r in rows if np.isfinite(r["profit_factor"])]
        n_sig = int(sum(r["n_signals"] for r in rows))
        n_tr = int(sum(r["n_trades"] for r in rows))
        pooled[arm] = {
            "n_folds": len(rows),
            "n_signals": n_sig,
            "n_trades": n_tr,
            "sum_net_pnl": float(np.sum(pnls)) if pnls else 0.0,
            "mean_fold_pf": float(np.mean(pfs)) if pfs else float("nan"),
            "frac_folds_pf_gt_1": float(np.mean(np.asarray(pfs) > 1.0)) if pfs else 0.0,
            "folds": rows,
        }

    control = pooled["control"]
    comparisons = {}
    for arm in arm_names:
        if arm == "control":
            continue
        a = pooled[arm]
        comparisons[arm] = {
            "pf_vs_control_mean_fold": (
                float(a["mean_fold_pf"] - control["mean_fold_pf"])
                if np.isfinite(a["mean_fold_pf"]) and np.isfinite(control["mean_fold_pf"])
                else float("nan")
            ),
            "pnl_vs_control": float(a["sum_net_pnl"] - control["sum_net_pnl"]),
            "signals_vs_control": int(a["n_signals"] - control["n_signals"]),
            "beats_control_pf": bool(
                np.isfinite(a["mean_fold_pf"])
                and np.isfinite(control["mean_fold_pf"])
                and a["mean_fold_pf"] > control["mean_fold_pf"]
            ),
            "beats_control_pnl": bool(a["sum_net_pnl"] > control["sum_net_pnl"]),
            "skip_more": bool(a["n_signals"] <= control["n_signals"]),
            "methodology_win": bool(
                a["mean_fold_pf"] > control["mean_fold_pf"]
                and a["sum_net_pnl"] > control["sum_net_pnl"]
                and a["n_signals"] <= control["n_signals"]
            ),
        }

    # Aggregate outer skill
    skill_summary: dict[str, Any] = {}
    for tgt in ("next_retrace_pct", "next_vol", "fwd_return"):
        rows = [r for r in skill_rows if r["target"] == tgt]
        ics = [r["outer_ic"] for r in rows if np.isfinite(r.get("outer_ic", float("nan")))]
        skill_summary[tgt] = {
            "mean_outer_spearman_ic": float(np.mean(ics)) if ics else float("nan"),
            "frac_folds_ic_positive": float(np.mean(np.asarray(ics) > 0)) if ics else 0.0,
            "n_folds": len(ics),
            "folds": rows,
        }

    return {
        "symbol": symbol,
        "n_bars": int(len(aligned)),
        "n_sparse_legs": int(len(y_sp)),
        "model_picks": model_picks,
        "forecast_skill": skill_summary,
        "arms": pooled,
        "vs_control": comparisons,
        "readiness_max": "RESEARCH_ONLY",
        "note": (
            "Forecast skill and trading Profit Factor are separate. "
            "Methodology win ≠ SHADOW_READY. No live authorization."
        ),
    }
