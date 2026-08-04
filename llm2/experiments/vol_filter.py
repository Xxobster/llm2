"""Vol-as-filter experiment: magnitude forecast gates entries; never sets side.

Preregistration: ``configs/preregister/volfilter_001.yaml``.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from llm2.audit.release_gates import require_constant_predictor_invariant
from llm2.backtest.run import run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.features.ohlcv_v1 import build_ohlcv_v1
from llm2.features.registry import build_space
from llm2.labels.volatility import build_volatility_labels
from llm2.models.base import Prediction
from llm2.models.classical import RidgePredictor
from llm2.paths import (
    FORWARD_LOCKBOX_START,
    ROOT,
    ROUND_TRIP_COST,
    ensure_artifact_dirs,
    touch_timeframe,
)
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger
from llm2.signals.translate import predictions_to_signals
from llm2.validation.folds import build_outer_folds, index_to_ms

PREREG_PATH = ROOT / "configs" / "preregister" / "volfilter_001.yaml"
PREREG_DIR = ROOT / "configs" / "preregister"

# Standing policy: the vol skip percentile is frozen at 75 after volfilter_001 OOS.
# New experiments may change the *entry rule* only, not hunt other percentiles.
FROZEN_VOL_FILTER_PERCENTILE = 75
FROZEN_FILTER_NAME = "skip_top_quartile_predicted_vol"


@dataclass(frozen=True)
class ArmResult:
    name: str
    pooled_pf: float
    pooled_pnl: float
    n_signals: int
    fold_pfs: list[float]
    fold_pnls: list[float]
    fold_signals: list[int]


def load_prereg(path: Path = PREREG_PATH) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    cfg = yaml.safe_load(text)
    cfg["_sha256"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    cfg["_path"] = str(path)
    validate_vol_filter_prereg(cfg)
    return cfg


def validate_vol_filter_prereg(cfg: dict[str, Any]) -> None:
    """Refuse percentile hunting and high-vol leverage after OOS on volfilter_001."""
    fr = cfg.get("filter_rule") or {}
    pct = int(fr.get("percentile", -1))
    if pct != FROZEN_VOL_FILTER_PERCENTILE:
        raise RuntimeError(
            f"vol-filter percentile must stay frozen at {FROZEN_VOL_FILTER_PERCENTILE}; "
            f"got {pct}. Change the entry rule, not the filter grid."
        )
    if fr.get("name") != FROZEN_FILTER_NAME:
        raise RuntimeError(
            f"vol-filter name must remain {FROZEN_FILTER_NAME!r}; got {fr.get('name')!r}"
        )
    forbidden = set(fr.get("action_forbidden") or [])
    for req in ("increase_leverage", "emit_long_or_short_from_vol_forecast"):
        if req not in forbidden:
            raise RuntimeError(f"prereg must forbid {req}")
    if cfg.get("vol_model", {}).get("role") != "filter_input_only":
        raise RuntimeError("vol_model.role must be filter_input_only")


def momentum_side(close: pd.Series, *, lookback: int, cost: float) -> np.ndarray:
    """Cost-gated momentum. Vectorized."""
    ret = close.pct_change(lookback).to_numpy(dtype=float)
    return np.where(ret > cost, 1, np.where(ret < -cost, -1, 0)).astype(np.int8)


def meanrev_side(close: pd.Series, *, lookback: int, cost: float) -> np.ndarray:
    """Cost-gated mean-reversion (fade the past move). Vectorized."""
    ret = close.pct_change(lookback).to_numpy(dtype=float)
    return np.where(ret < -cost, 1, np.where(ret > cost, -1, 0)).astype(np.int8)


def entry_side(close: pd.Series, entry_rule: dict[str, Any], *, cost: float) -> np.ndarray:
    name = entry_rule["name"]
    lookback = int(entry_rule["lookback_bars"])
    if name == "momentum_24_cost_gate":
        return momentum_side(close, lookback=lookback, cost=cost)
    if name == "meanrev_24_cost_gate":
        return meanrev_side(close, lookback=lookback, cost=cost)
    raise ValueError(f"unknown entry_rule.name: {name}")


def _feature_matrix(ohlcv: pd.DataFrame, space: str, symbol: str) -> pd.DataFrame:
    if space == "ohlcv_v1":
        return build_ohlcv_v1(ohlcv)
    return build_space(ohlcv, space, symbol=symbol)


def _proxy_stats(side: np.ndarray, realized: np.ndarray, cost: float) -> tuple[float, float, int]:
    active = side != 0
    n = int(active.sum())
    if n == 0:
        return 0.0, 0.0, 0
    ret = realized * side - cost * active
    pnl = float(np.nansum(ret))
    wins = float(np.nansum(ret[ret > 0]))
    losses = float(-np.nansum(ret[ret < 0]))
    if losses > 0:
        pf = wins / losses
    elif wins > 0:
        pf = 2.0
    else:
        pf = 0.0
    return pf, pnl, n


def run_vol_filter_experiment(
    *,
    prereg_path: Path = PREREG_PATH,
    db: ResearchDB | None = None,
) -> dict[str, Any]:
    """Single frozen comparison: filtered entry rule vs always-on control."""
    require_constant_predictor_invariant()
    ensure_artifact_dirs()
    cfg = load_prereg(prereg_path)
    db = db or ResearchDB()

    symbol = cfg["universe"]["symbol"]
    timeframe = cfg["universe"]["timeframe"]
    lookback = int(cfg["entry_rule"]["lookback_bars"])
    vol_horizon = int(cfg["vol_model"]["horizon"])
    space = cfg["vol_model"]["feature_space"]
    percentile = int(cfg["filter_rule"]["percentile"])
    gid = cfg["generation_id"]

    append_ledger(
        f"PREREG {gid} status={cfg.get('status')} entry={cfg['entry_rule']['name']} "
        f"sha256={cfg['_sha256'][:16]} — vol filter_input_only; never emits side; "
        f"percentile frozen at {percentile}",
        tier=0,
    )
    db.create_generation(
        gid,
        max_trials=2,
        hypothesis=str(cfg["hypothesis"])[:500],
        config_hash=cfg["_sha256"][:16],
    )

    ohlcv = load_ohlcv(symbol, timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = _feature_matrix(ohlcv, space, symbol)
    vol_y = build_volatility_labels(ohlcv, horizon=vol_horizon)["volatility"].reindex(feats.index)
    # Realized forward return over the entry lookback horizon for proxy P&L.
    fwd = ohlcv["close"].pct_change(lookback).shift(-lookback).reindex(feats.index)

    side_all = entry_side(
        ohlcv["close"].reindex(feats.index), cfg["entry_rule"], cost=ROUND_TRIP_COST
    )

    aligned = pd.DataFrame(
        {
            "vol_y": vol_y,
            "fwd": fwd,
            "side": side_all,
        },
        index=feats.index,
    ).join(feats)
    aligned = aligned.replace([np.inf, -np.inf], np.nan).dropna()
    if len(aligned) < 2000:
        return {"status": "INSUFFICIENT_DATA", "n": len(aligned)}

    feature_cols = [c for c in aligned.columns if c not in ("vol_y", "fwd", "side")]
    X = aligned[feature_cols].to_numpy(dtype=float)
    vol_target = aligned["vol_y"].to_numpy(dtype=float)
    fwd_ret = aligned["fwd"].to_numpy(dtype=float)
    base_side = aligned["side"].to_numpy(dtype=np.int8)
    ts_ms = index_to_ms(aligned.index)

    folds = build_outer_folds(ts_ms, purge_bars=vol_horizon, embargo_bars=vol_horizon)
    if len(folds) < 3:
        return {"status": "INSUFFICIENT_FOLDS", "n_folds": len(folds)}

    ctrl_pfs: list[float] = []
    ctrl_pnls: list[float] = []
    ctrl_ns: list[int] = []
    filt_pfs: list[float] = []
    filt_pnls: list[float] = []
    filt_ns: list[int] = []
    # Sanity: vol predictions must not correlate into a synthetic side.
    vol_side_violations = 0

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = RidgePredictor()
        model.fit(X[tr], vol_target[tr])
        pred_tr = model.predict(X[tr])
        pred_oos = model.predict(X[oos])
        assert pred_tr.mean is not None and pred_oos.mean is not None
        # Magnitude path: no side from vol.
        if pred_oos.side is not None:
            vol_side_violations += 1
        thr = float(np.nanpercentile(pred_tr.mean, percentile))
        pred_v = np.asarray(pred_oos.mean, dtype=float)

        side_ctrl = base_side[oos].copy()
        side_filt = side_ctrl.copy()
        side_filt[pred_v > thr] = 0  # skip-more policy

        pf_c, pnl_c, n_c = _proxy_stats(side_ctrl, fwd_ret[oos], ROUND_TRIP_COST)
        pf_f, pnl_f, n_f = _proxy_stats(side_filt, fwd_ret[oos], ROUND_TRIP_COST)
        ctrl_pfs.append(pf_c)
        ctrl_pnls.append(pnl_c)
        ctrl_ns.append(n_c)
        filt_pfs.append(pf_f)
        filt_pnls.append(pnl_f)
        filt_ns.append(n_f)

    def _pool(pfs: list[float], pnls: list[float], ns: list[int], name: str) -> ArmResult:
        w = np.array(ns, dtype=float)
        pooled_pf = (
            float(np.nansum(np.array(pfs) * w) / np.nansum(w)) if w.sum() > 0 else 0.0
        )
        return ArmResult(
            name=name,
            pooled_pf=pooled_pf,
            pooled_pnl=float(np.nansum(pnls)),
            n_signals=int(np.sum(ns)),
            fold_pfs=pfs,
            fold_pnls=pnls,
            fold_signals=ns,
        )

    control = _pool(ctrl_pfs, ctrl_pnls, ctrl_ns, "always_on")
    filtered = _pool(filt_pfs, filt_pnls, filt_ns, "skip_top_quartile_predicted_vol")

    beats_pf = filtered.pooled_pf > control.pooled_pf
    beats_pnl = filtered.pooled_pnl > control.pooled_pnl
    skip_more = filtered.n_signals <= control.n_signals
    no_vol_side = vol_side_violations == 0
    success = bool(beats_pf and beats_pnl and skip_more and no_vol_side)

    for arm, label in ((control, "control"), (filtered, "filtered")):
        db.register_trial(
            gid,
            tier=1 if success and label == "filtered" else 0,
            symbol=symbol,
            timeframe=timeframe,
            target="vol_filter",
            feature_space=space,
            model=f"ridge_vol+{arm.name}",
            outer_pf=arm.pooled_pf,
            outer_trades=arm.n_signals,
            status="completed",
            notes=str(
                {
                    "arm": label,
                    "pooled_pnl": arm.pooled_pnl,
                    "fold_pfs": arm.fold_pfs,
                    "prereg_sha256": cfg["_sha256"][:16],
                }
            )[:500],
        )

    verdict = "FILTER_BEATS_CONTROL" if success else "FILTER_FAILS_vs_CONTROL"
    append_ledger(
        f"{verdict} {gid}: filtered_pf={filtered.pooled_pf:.4f} ctrl_pf={control.pooled_pf:.4f} "
        f"filtered_pnl={filtered.pooled_pnl:.6f} ctrl_pnl={control.pooled_pnl:.6f} "
        f"n_filt={filtered.n_signals} n_ctrl={control.n_signals} "
        f"skip_more={skip_more} no_vol_side={no_vol_side}",
        tier=1 if success else 0,
    )

    return {
        "status": "COMPLETE",
        "verdict": verdict,
        "success": success,
        "generation_id": gid,
        "prereg_sha256": cfg["_sha256"],
        "control": control.__dict__,
        "filtered": filtered.__dict__,
        "criteria": {
            "beats_pf": beats_pf,
            "beats_pnl": beats_pnl,
            "skip_more": skip_more,
            "no_vol_side": no_vol_side,
        },
        "n_folds": len(folds),
        "entry_rule": cfg["entry_rule"]["name"],
        "filter_percentile": percentile,
        "prereg_status": cfg.get("status"),
        "note": (
            "Proxy screen only. Volatility forecast never set side. "
            "No leverage increase. Beating control while PF<1 is a methodology win, "
            "not a strategy candidate. No Finplot/live from this alone. "
            "Tradesim only if success."
        ),
    }


def _sides_to_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    *,
    tp_pct: float,
    sl_pct: float,
) -> list:
    """Entry sides come from the frozen entry rule — never from the vol forecast."""
    return predictions_to_signals(
        ts_ms,
        Prediction(side=np.asarray(side, dtype=int)),
        tp_pct=tp_pct,
        sl_pct=sl_pct,
        min_edge=0.0,  # side already cost-gated in the entry rule
        target_family="directional",
    )


def run_vol_filter_tradesim(
    *,
    prereg_path: Path = PREREG_PATH,
    max_signals_per_fold: int = 800,
) -> dict[str, Any]:
    """Tradesim-backed comparison after a proxy FILTER_BEATS_CONTROL.

    Caps signals per fold (strongest |momentum| keep) so the run is feasible; the cap
    is applied identically to control and filtered after the vol skip, so the
    skip-more relationship is preserved before the cap.
    """
    require_constant_predictor_invariant()
    cfg = load_prereg(prereg_path)
    symbol = cfg["universe"]["symbol"]
    timeframe = cfg["universe"]["timeframe"]
    lookback = int(cfg["entry_rule"]["lookback_bars"])
    vol_horizon = int(cfg["vol_model"]["horizon"])
    space = cfg["vol_model"]["feature_space"]
    percentile = int(cfg["filter_rule"]["percentile"])
    tp = float(cfg["entry_rule"]["tp_pct"])
    sl = float(cfg["entry_rule"]["sl_pct"])
    gid = cfg["generation_id"] + "_ts"

    ohlcv = load_ohlcv(symbol, timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    touch_tf = touch_timeframe(timeframe, symbol)
    try:
        touch = load_ohlcv(symbol, touch_tf)
        touch = touch.loc[index_to_ms(touch.index) < lock_ms]
    except Exception:  # noqa: BLE001
        touch = None

    feats = _feature_matrix(ohlcv, space, symbol)
    vol_y = build_volatility_labels(ohlcv, horizon=vol_horizon)["volatility"].reindex(feats.index)
    side_all = entry_side(
        ohlcv["close"].reindex(feats.index), cfg["entry_rule"], cost=ROUND_TRIP_COST
    )
    mom = ohlcv["close"].pct_change(lookback).reindex(feats.index).to_numpy(dtype=float)

    aligned = pd.DataFrame({"vol_y": vol_y, "side": side_all, "mom": mom}, index=feats.index).join(
        feats
    )
    aligned = aligned.replace([np.inf, -np.inf], np.nan).dropna()
    feature_cols = [c for c in aligned.columns if c not in ("vol_y", "side", "mom")]
    X = aligned[feature_cols].to_numpy(dtype=float)
    vol_target = aligned["vol_y"].to_numpy(dtype=float)
    base_side = aligned["side"].to_numpy(dtype=np.int8)
    mom_arr = aligned["mom"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=vol_horizon, embargo_bars=vol_horizon)

    def _cap(side: np.ndarray, strength: np.ndarray) -> np.ndarray:
        out = side.copy()
        idx = np.flatnonzero(out != 0)
        if len(idx) <= max_signals_per_fold:
            return out
        keep = idx[np.argsort(np.abs(strength[idx]))[-max_signals_per_fold:]]
        mask = np.zeros(len(out), dtype=bool)
        mask[keep] = True
        out = np.where(mask, out, 0)
        return out

    arms = {"control": [], "filtered": []}
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = RidgePredictor()
        model.fit(X[tr], vol_target[tr])
        pred_tr = model.predict(X[tr])
        pred_oos = model.predict(X[oos])
        thr = float(np.nanpercentile(pred_tr.mean, percentile))
        pred_v = np.asarray(pred_oos.mean, dtype=float)

        side_c = _cap(base_side[oos].copy(), mom_arr[oos])
        side_f = base_side[oos].copy()
        side_f[pred_v > thr] = 0
        side_f = _cap(side_f, mom_arr[oos])

        oos_end = aligned.index[oos[-1]]
        window = ohlcv.loc[:oos_end].tail(max(len(oos) + 500, 1000))
        touch_win = None
        if touch is not None:
            from llm2.paths import TF_MS as _TF_MS

            _touch_end = oos_end + pd.Timedelta(milliseconds=int(_TF_MS[timeframe])) - pd.Timedelta(
                milliseconds=1
            )
            touch_win = touch.loc[:_touch_end].tail(max(len(window) * 60, 20_000))

        for name, side in (("control", side_c), ("filtered", side_f)):
            signals = _sides_to_signals(ts_ms[oos], side, tp_pct=tp, sl_pct=sl)
            if not signals:
                arms[name].append({"pf": 0.0, "pnl": 0.0, "n": 0})
                continue
            bundle = run_strategy_backtest(
                window,
                signals,
                symbol=symbol,
                timeframe=timeframe,
                strategy_id=f"llm2-{gid}-{name}-f{fold.fold_index}",
                touch_ohlcv=touch_win,
                touch_timeframe=touch_tf if touch_win is not None else None,
                strategy_meta={
                    "name": name,
                    "batch": gid,
                    "tp_pct": tp,
                    "sl_pct": sl,
                    "target": "vol_filter",
                },
                plot=False,
                print_headline=False,
                store_path=None,
            )
            m = bundle.metrics
            arms[name].append(
                {
                    "pf": float(m.profit_factor) if np.isfinite(m.profit_factor) else 0.0,
                    "pnl": float(m.net_pnl),
                    "n": int(m.n_trades),
                }
            )

    def _summ(rows: list[dict[str, Any]]) -> dict[str, Any]:
        ns = np.array([r["n"] for r in rows], dtype=float)
        pfs = np.array([r["pf"] for r in rows], dtype=float)
        pooled_pf = float(np.nansum(pfs * ns) / np.nansum(ns)) if ns.sum() else 0.0
        return {
            "pooled_pf": pooled_pf,
            "pooled_pnl": float(sum(r["pnl"] for r in rows)),
            "n_trades": int(ns.sum()),
            "folds": rows,
        }

    control = _summ(arms["control"])
    filtered = _summ(arms["filtered"])
    success = (
        filtered["pooled_pf"] > control["pooled_pf"]
        and filtered["pooled_pnl"] > control["pooled_pnl"]
        and filtered["n_trades"] <= control["n_trades"]
    )
    verdict = "TRADESIM_FILTER_BEATS_CONTROL" if success else "TRADESIM_FILTER_FAILS_vs_CONTROL"
    append_ledger(
        f"{verdict} {gid}: filt_pf={filtered['pooled_pf']:.4f} ctrl_pf={control['pooled_pf']:.4f} "
        f"filt_pnl={filtered['pooled_pnl']:.4f} ctrl_pnl={control['pooled_pnl']:.4f} "
        f"n_filt={filtered['n_trades']} n_ctrl={control['n_trades']} "
        f"(max_signals_per_fold={max_signals_per_fold})",
        tier=1 if success else 0,
    )
    return {
        "status": "COMPLETE",
        "verdict": verdict,
        "success": success,
        "generation_id": gid,
        "control": control,
        "filtered": filtered,
        "max_signals_per_fold": max_signals_per_fold,
    }
