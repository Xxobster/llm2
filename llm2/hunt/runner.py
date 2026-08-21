"""Autonomous nested walk-forward hunt runner with alert tiers."""

from __future__ import annotations

import hashlib
import json
import traceback
from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from llm2.audit.cost_hurdle import CostHurdle
from llm2.audit.predictability import audit_predictability, required_surrogates_per_family
from llm2.audit.release_gates import require_constant_predictor_invariant
from llm2.audit.surrogates import apply_surrogate, list_surrogates
from llm2.backtest.run import run_strategy_backtest
from llm2.data.loader import load_ohlcv
from llm2.data.splits import split_and_materialize
from llm2.features.guard import run_audit_for_space
from llm2.features.ohlcv_v1 import build_ohlcv_v1
from llm2.features.registry import build_space
from llm2.gates.evidence import (
    build_fold_return_matrix,
    leverage_from_stop,
    mdd_fraction_from_daily_returns,
    peak_margin_utilization,
    pooled_profit_factor,
    research_costs_baseline,
    research_costs_moderate_stress,
)
from llm2.gates.v21 import evaluate_v21_gates, format_gates_table
from llm2.labels.direction import build_direction_labels
from llm2.labels.fwd_return import build_fwd_return_labels
from llm2.labels.quantiles import build_quantile_labels
from llm2.labels.volatility import build_volatility_labels
from llm2.labels.xs_rank import build_xs_rank_labels
from llm2.models.base import Prediction
from llm2.models.baselines import HistoricalMeanBaseline, LastValueBaseline, SeasonalNaiveBaseline
from llm2.models.boosting import LGBMClassifierPredictor, LGBMRegressorPredictor
from llm2.models.classical import RidgePredictor
from llm2.paths import FORWARD_LOCKBOX_START, ROUND_TRIP_COST, ensure_artifact_dirs, touch_timeframe
from llm2.hunt.targets import DEFAULT_HORIZON, proxy_side, target_family
from llm2.registry.db import ResearchDB
from llm2.registry.ledger import append_ledger
from llm2.signals.translate import predictions_to_signals
from llm2.validation.folds import build_outer_folds, index_to_ms, make_inner_folds

# Re-exports for callers / tests that imported these from the runner.
_proxy_side = proxy_side

MAX_TRIALS_PER_GEN = 200

# Stage-B permutation test configuration. The draw count is derived from alpha rather than
# hardcoded, so lowering alpha cannot silently produce a test that is unable to reject.
PREDICTABILITY_ALPHA = 0.05
PREDICTABILITY_DRAWS = required_surrogates_per_family(PREDICTABILITY_ALPHA, len(list_surrogates()))


@dataclass
class HuntConfig:
    generation_id: str
    symbol: str = "BTCUSDT"
    timeframe: str = "1h"
    target: str = "fwd_return"
    feature_space: str = "ohlcv_v1"
    horizon: int = 6
    max_trials: int = 20
    seed: int = 42
    run_surrogate_challenge: bool = True
    run_backtest: bool = True
    tp_pct: float = 0.01
    sl_pct: float = 0.02
    models: list[str] = field(
        default_factory=lambda: [
            "hist_mean",
            "last_value",
            "seasonal_naive",
            "ridge",
            "lgbm_regressor",
            "lgbm_classifier",
            "torch_mlp",
        ]
    )


def _make_model(name: str):
    if name == "hist_mean":
        return HistoricalMeanBaseline()
    if name == "last_value":
        return LastValueBaseline()
    if name == "seasonal_naive":
        return SeasonalNaiveBaseline(season=24)
    if name == "ridge":
        return RidgePredictor()
    if name == "lgbm_regressor":
        return LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
    if name == "lgbm_classifier":
        return LGBMClassifierPredictor(n_estimators=80, learning_rate=0.05)
    if name in ("torch_mlp", "patchtst_lite"):
        from llm2.models.deep import PatchTSTLitePredictor, TorchMLPPredictor

        return TorchMLPPredictor() if name == "torch_mlp" else PatchTSTLitePredictor()
    raise ValueError(f"unknown model: {name}")


def _labels_for_target(ohlcv: pd.DataFrame, target: str, horizon: int, symbol: str) -> pd.Series:
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=horizon)["fwd_return"]
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=horizon)["direction"]
    if target == "volatility":
        return build_volatility_labels(ohlcv, horizon=horizon).iloc[:, 0]
    if target == "quantile":
        return build_quantile_labels(ohlcv, horizon=horizon)["quantile_target"]
    if target == "xs_rank":
        return build_xs_rank_labels(ohlcv, symbol=symbol, horizon=horizon)["xs_rank"]
    if target == "vol_ratio":
        # Forward realized range against the trailing range: a regime *shift*, which is
        # forward-looking, unlike the regime label itself which is a function of the past.
        fwd = build_volatility_labels(ohlcv, horizon=horizon)["volatility"]
        c = ohlcv["close"].astype(float)
        past = ((ohlcv["high"].astype(float).rolling(horizon, min_periods=max(2, horizon // 4)).max()
                 - ohlcv["low"].astype(float).rolling(horizon, min_periods=max(2, horizon // 4)).min())
                / c.replace(0, np.nan))
        return (fwd / past.replace(0, np.nan)).rename("vol_ratio")
    raise ValueError(f"unknown target: {target}")


def _feature_matrix(
    ohlcv: pd.DataFrame,
    space: str,
    symbol: str,
    timeframe: str = "1h",
) -> pd.DataFrame:
    if space == "ohlcv_v1":
        return build_ohlcv_v1(ohlcv)
    return build_space(ohlcv, space, symbol=symbol, timeframe=timeframe)


def _tier_from_gates(
    gates: dict[str, Any],
    screen_pass: bool,
    *,
    require_full_gates: bool = False,
) -> int:
    # A result the surrogate challenge could not distinguish from randomised data is not
    # promotable no matter how the profit gates read, so the screen bounds the tier.
    if not screen_pass:
        return 0
    overall = gates.get("overall", "UNKNOWN")
    if require_full_gates:
        # Tradesim path: no Tier ≥ 2 while stress/MDD/margin are unbound, and no Tier ≥ 2
        # on an overall FAIL (honest negative after full gates).
        for key in (
            "stress_pnl",
            "stress_pf",
            "baseline_mdd",
            "stress_mdd",
            "margin_utilization",
        ):
            if gates.get(key) == "UNKNOWN":
                return 1
        if overall == "PASS" and gates.get("dsr") == "PASS":
            return 3
        if overall == "PASS":
            return 2
        return 1 if gates.get("pooled_pf") == "PASS" else 0
    if overall == "PASS" and gates.get("dsr") == "PASS":
        return 3
    if overall == "PASS" or (
        gates.get("pooled_pf") == "PASS"
        and gates.get("positive_fold_frac") in ("PASS", "UNKNOWN")
        and gates.get("pooled_trades") == "PASS"
    ):
        return 2
    return 1


def run_nested_hunt(config: HuntConfig, *, db: ResearchDB | None = None) -> dict[str, Any]:
    """Full nested walk-forward hunt for one (symbol, timeframe, target, space)."""
    ensure_artifact_dirs()
    # Fail closed before any trial work if scoring units are unsafe.
    require_constant_predictor_invariant()
    db = db or ResearchDB()
    config_hash = hashlib.sha256(
        json.dumps(config.__dict__, sort_keys=True, default=str).encode()
    ).hexdigest()[:16]
    db.create_generation(
        config.generation_id,
        max_trials=min(config.max_trials, MAX_TRIALS_PER_GEN),
        hypothesis=f"{config.target}/{config.feature_space}/{config.symbol}/{config.timeframe}",
        config_hash=config_hash,
    )
    append_ledger(
        f"START gen={config.generation_id} {config.symbol} {config.timeframe} "
        f"target={config.target} space={config.feature_space}",
        tier=0,
    )

    # --- leakage gate ---
    ohlcv = load_ohlcv(config.symbol, config.timeframe)
    # Drop forward lockbox from research
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ts_all = index_to_ms(ohlcv.index)
    ohlcv = ohlcv.loc[ts_all < lock_ms].copy()

    audit = run_audit_for_space(
        ohlcv.tail(8000),
        interval=config.timeframe,
        space=config.feature_space,
        symbol=config.symbol,
        cuts=3,
    )
    if not audit["passed"]:
        append_ledger(f"LEAKAGE FAIL space={config.feature_space}: {audit.get('report_text', '')[:500]}", tier=0)
        return {"generation_id": config.generation_id, "status": "LEAKAGE_FAIL", "audit": audit["report_text"]}

    # Warehouse-backed spaces: shared leakage PASS alone is illegal (D-014/D-016/D-055).
    from llm2.evidence.four_proof import (
        refuse_warehouse_leakage_pass_alone,
        require_four_proof_ok,
        run_four_proof_gate,
    )
    from llm2.research_policy import WAREHOUSE_BACKED_SPACES

    four_proof_summary = None
    if config.feature_space in WAREHOUSE_BACKED_SPACES:
        # Structure Layer-A requires the *same* candle universe as the warehouse tip.
        # Truncating to 4k bars recomputes a different swing path and false-fails identity.
        four_proof_summary = run_four_proof_gate(
            space=config.feature_space,
            symbol=config.symbol,
            timeframe=config.timeframe,
            ohlcv=ohlcv,
        )
        if not bool(four_proof_summary.get("ok")):
            append_ledger(
                f"FOUR_PROOF FAIL space={config.feature_space}: "
                f"{four_proof_summary.get('proofs_ok')}",
                tier=0,
            )
            return {
                "generation_id": config.generation_id,
                "status": "FOUR_PROOF_FAIL",
                "four_proof": four_proof_summary,
                "audit": audit.get("report_text"),
            }
        refuse_warehouse_leakage_pass_alone(
            space=config.feature_space,
            leakage_passed=bool(audit["passed"]),
            four_proof_ok=True,
        )
        try:
            require_four_proof_ok(four_proof_summary)
        except Exception as exc:  # noqa: BLE001 — PolicyError or RuntimeError
            append_ledger(
                f"FOUR_PROOF FAIL space={config.feature_space}: {exc}",
                tier=0,
            )
            return {
                "generation_id": config.generation_id,
                "status": "FOUR_PROOF_FAIL",
                "four_proof": four_proof_summary,
                "audit": audit.get("report_text"),
            }

    feats = _feature_matrix(
        ohlcv, config.feature_space, config.symbol, config.timeframe
    )
    family = target_family(config.target)
    y_ser = _labels_for_target(
        ohlcv, config.target, config.horizon, config.symbol
    ).reindex(feats.index)
    # Realized forward return over the same horizon: the only series a proxy P&L may be
    # denominated in, whatever the model was trained to predict.
    realized_ret = build_fwd_return_labels(ohlcv, horizon=config.horizon)["fwd_return"]
    aligned = feats.join(y_ser.rename("y"), how="inner")
    aligned = aligned.replace([np.inf, -np.inf], np.nan).dropna()
    if len(aligned) < 2000:
        return {"generation_id": config.generation_id, "status": "INSUFFICIENT_DATA", "n": len(aligned)}

    X_all = aligned.drop(columns=["y"]).to_numpy(dtype=float)
    y_all = aligned["y"].to_numpy(dtype=float)
    pnl_all = realized_ret.reindex(aligned.index).to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    feature_cols = list(aligned.drop(columns=["y"]).columns)

    # cost hurdle filter for return-like targets
    hurdle = CostHurdle(round_trip_cost=ROUND_TRIP_COST)
    if config.target in ("fwd_return", "direction"):
        abs_mean = float(np.nanmean(np.abs(y_all)))
        if abs_mean < ROUND_TRIP_COST * 0.5:
            append_ledger(
                f"COST_HURDLE kill: mean|y|={abs_mean:.6f} < 0.5*hurdle={ROUND_TRIP_COST}",
                tier=0,
            )
            # still continue for diagnostics but mark killed

    # Stage B predictability on a held-out chronological slice (last 20% of pre-lockbox).
    # Draws per surrogate family must let the add-one p-value express alpha; anything less
    # cannot reject regardless of the data (D-013).
    cut = int(len(X_all) * 0.8)
    pred_report = audit_predictability(
        X_all[:cut],
        y_all[:cut],
        target=config.target,
        n_surrogates=PREDICTABILITY_DRAWS,
        alpha=PREDICTABILITY_ALPHA,
    )
    append_ledger(f"PREDICTABILITY {pred_report.summary()}", tier=0)

    folds = build_outer_folds(ts_ms, purge_bars=config.horizon, embargo_bars=config.horizon)
    if len(folds) < 3:
        return {"generation_id": config.generation_id, "status": "INSUFFICIENT_FOLDS", "n_folds": len(folds)}

    # materialize physical train/test for fold 0 as geometry evidence
    f0 = folds[0]
    train_mask = pd.Series(False, index=aligned.index)
    test_mask = pd.Series(False, index=aligned.index)
    train_mask.iloc[f0.train_indices] = True
    test_mask.iloc[f0.oos_indices] = True
    split_and_materialize(
        ohlcv.reindex(aligned.index),
        train_mask,
        test_mask,
        symbol=config.symbol,
        timeframe=config.timeframe,
        fold_index=f0.fold_index,
        build_features=lambda df: _feature_matrix(
            df, config.feature_space, config.symbol, config.timeframe
        ),
        build_labels=lambda df: _labels_for_target(
            df, config.target, config.horizon, config.symbol
        ).to_frame("y"),
    )

    rng = np.random.default_rng(config.seed)
    model_names = config.models[: min(config.max_trials, MAX_TRIALS_PER_GEN)]
    trial_results: list[dict[str, Any]] = []
    best_tier = 0
    best_summary: dict[str, Any] | None = None

    touch_tf = touch_timeframe(config.timeframe, config.symbol)
    try:
        touch_ohlcv = load_ohlcv(config.symbol, touch_tf)
        touch_ohlcv = touch_ohlcv.loc[index_to_ms(touch_ohlcv.index) < lock_ms]
    except Exception:  # noqa: BLE001
        touch_ohlcv = None

    # Research factories for tradesim path (honest costs / venue sizing / leverage / funding).
    bt_costs = None
    bt_stress_costs = None
    bt_margin = None
    bt_sizing = None
    bt_instrument = None
    funding_ts = np.array([], dtype=np.int64)
    funding_rt = np.array([], dtype=float)
    if config.run_backtest:
        from tradesim import research_margin, research_sizing, research_instrument

        from llm2.data.macro import load_funding

        bt_costs = research_costs_baseline()
        bt_stress_costs = research_costs_moderate_stress(slip_mult=2.0)
        lev = leverage_from_stop(config.sl_pct)
        bt_margin = research_margin(leverage=lev)
        bt_sizing = research_sizing()
        try:
            bt_instrument = research_instrument(config.symbol)
        except Exception as exc:  # noqa: BLE001
            append_ledger(
                f"HUNT {config.generation_id}: instrument unavailable ({exc})",
                tier=0,
            )
        try:
            funding = load_funding(config.symbol)
            funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
            if funding.empty:
                raise RuntimeError("empty funding series")
            funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
            funding_rt = funding.to_numpy(dtype=float)
        except Exception as exc:  # noqa: BLE001
            append_ledger(
                f"HUNT {config.generation_id}: funding unavailable ({exc}); "
                "refusing to treat settle numbers as live-parity",
                tier=0,
            )
            raise RuntimeError(
                f"funding history required for tradesim hunt path ({config.symbol}): {exc}"
            ) from exc

    model_fold_pnls: dict[str, list[float]] = {}

    for trial_i, model_name in enumerate(model_names):
        try:
            # inner selection on fold 0 train only (honest)
            inner_folds = make_inner_folds(
                f0.train_indices, n_folds=3, purge_bars=config.horizon, embargo_bars=config.horizon
            )
            inner_scores: list[float] = []
            for inn in inner_folds:
                # FoldSpec uses offsets into the train window length
                tr_rel = np.arange(0, inn.train_end, dtype=np.int64)
                va_rel = np.arange(inn.val_start, inn.val_end, dtype=np.int64)
                tr = f0.train_indices[tr_rel]
                va = f0.train_indices[va_rel]
                if len(tr) < 200 or len(va) < 50:
                    continue
                m = _make_model(model_name)
                y_tr = y_all[tr]
                if model_name == "lgbm_classifier":
                    y_tr = np.sign(y_tr)
                m.fit(X_all[tr], y_tr)
                pred = m.predict(X_all[va])
                if pred.mean is not None:
                    err = y_all[va] - pred.mean
                    score = float(-np.nanmean(err**2))
                else:
                    score = 0.0
                inner_scores.append(score)
            inner_score = float(np.nanmean(inner_scores)) if inner_scores else float("-inf")

            # outer OOS evaluation once per fold
            fold_pnls: list[float] = []
            fold_pfs: list[float] = []  # Profit Factor only; never a skill ratio
            fold_skills: list[float] = []
            fold_trades: list[int] = []
            all_daily: list[float] = []
            all_trade_pnls: list[float] = []
            stress_trade_pnls: list[float] = []
            stress_fold_pnls: list[float] = []
            stress_daily: list[float] = []
            peak_margin = 0.0
            any_liquidation = False
            last_pred_mean: np.ndarray | None = None

            for fold in folds:
                m = _make_model(model_name)
                y_tr = y_all[fold.train_indices]
                if model_name == "lgbm_classifier":
                    y_tr = np.sign(y_tr)
                m.fit(X_all[fold.train_indices], y_tr)
                pred = m.predict(X_all[fold.oos_indices])
                if fold is folds[-1] and pred.mean is not None:
                    last_pred_mean = np.asarray(pred.mean, dtype=float)

                if family == "magnitude":
                    # Magnitude targets have no side. Graded on forecast skill only;
                    # skill never enters the Profit Factor field.
                    mean = pred.mean if pred.mean is not None else np.full(len(fold.oos_indices), np.nan)
                    y_oos = y_all[fold.oos_indices]
                    mae = float(np.nanmean(np.abs(y_oos - mean)))
                    mae_base = float(np.nanmean(np.abs(y_oos - np.nanmean(y_all[fold.train_indices]))))
                    skill = float(mae_base / mae) if mae > 1e-12 else 0.0
                    fold_pnls.append(float(mae_base - mae))
                    fold_skills.append(skill)
                    fold_trades.append(int(np.sum(np.isfinite(mean))))
                    continue

                mean = pred.mean if pred.mean is not None else np.zeros(len(fold.oos_indices))
                side = proxy_side(np.asarray(mean, dtype=float), family)

                if not config.run_backtest:
                    # Proxy P&L is the realized forward return earned by that side, never
                    # the target itself.
                    ret = pnl_all[fold.oos_indices] * side - ROUND_TRIP_COST * (side != 0)
                    fold_pnls.append(float(np.nansum(ret)))
                    wins = float(np.nansum(ret[ret > 0]))
                    losses = float(-np.nansum(ret[ret < 0]))
                    if losses > 0:
                        fold_pfs.append(wins / losses)
                    elif wins > 0:
                        fold_pfs.append(2.0)  # finite cap; never inf for gates
                    else:
                        fold_pfs.append(0.0)
                    fold_trades.append(int(np.sum(side != 0)))
                    continue

                signals = predictions_to_signals(
                    ts_ms[fold.oos_indices],
                    Prediction(side=side),
                    tp_pct=config.tp_pct,
                    sl_pct=config.sl_pct,
                    min_edge=ROUND_TRIP_COST,
                )
                if not signals:
                    fold_pnls.append(0.0)
                    fold_pfs.append(0.0)
                    fold_trades.append(0)
                    stress_fold_pnls.append(0.0)
                    continue

                oos_end = aligned.index[fold.oos_indices[-1]]
                window = ohlcv.loc[:oos_end].tail(max(len(fold.oos_indices) + 500, 1000))
                touch_win = None
                if touch_ohlcv is not None:
                    # Cover through the end of the last decision bar (not its open).
                    from llm2.paths import TF_MS as _TF_MS

                    _touch_end = oos_end + pd.Timedelta(milliseconds=int(_TF_MS[config.timeframe])) - pd.Timedelta(
                        milliseconds=1
                    )
                    # 1h→1m needs ~60 touch bars/decision bar; keep ample pad.
                    touch_win = touch_ohlcv.loc[:_touch_end].tail(max(len(window) * 60, 20_000))

                meta = {
                    "name": model_name,
                    "batch": config.generation_id,
                    "tp_pct": config.tp_pct,
                    "sl_pct": config.sl_pct,
                    "target": config.target,
                    "feature_space": config.feature_space,
                    "feature_cols": len(feature_cols),
                }
                w_ts = index_to_ms(window.index)
                w0, w1 = int(w_ts[0]), int(w_ts[-1])
                fmask = (funding_ts >= w0) & (funding_ts <= w1)
                bundle = run_strategy_backtest(
                    window,
                    signals,
                    symbol=config.symbol,
                    timeframe=config.timeframe,
                    strategy_id=f"llm2-{config.generation_id}-{model_name}-f{fold.fold_index}",
                    touch_ohlcv=touch_win,
                    touch_timeframe=touch_tf if touch_win is not None else None,
                    strategy_meta=meta,
                    costs=bt_costs,
                    margin=bt_margin,
                    sizing=bt_sizing,
                    instrument=bt_instrument,
                    funding_ts_ms=funding_ts[fmask],
                    funding_rate=funding_rt[fmask],
                    plot=False,
                    print_headline=False,
                    store_path=None,
                )
                metrics = bundle.metrics
                fold_pnls.append(float(metrics.net_pnl))
                fold_trades.append(int(metrics.n_trades))
                trades = bundle.result.trades
                all_trade_pnls.extend(float(t.realized_pnl) for t in trades)
                if int(getattr(metrics, "n_liquidations", 0) or 0) > 0:
                    any_liquidation = True
                peak_margin = max(
                    peak_margin,
                    peak_margin_utilization(
                        trades,
                        equity=getattr(bundle.result, "equity", None),
                        starting_equity=float(metrics.starting_equity),
                    ),
                )
                de = getattr(bundle.result, "daily_equity", None)
                if de is not None:
                    if isinstance(de, pd.DataFrame) and "equity" in de.columns:
                        eq = de["equity"].to_numpy(dtype=float)
                    else:
                        eq = np.asarray(de, dtype=float).reshape(-1)
                    if len(eq) > 1:
                        rets = np.diff(eq) / np.maximum(eq[:-1], 1e-9)
                        all_daily.extend(rets.tolist())

                # Moderate stress: same signals, 2× slippage.
                stress_bundle = run_strategy_backtest(
                    window,
                    signals,
                    symbol=config.symbol,
                    timeframe=config.timeframe,
                    strategy_id=(
                        f"llm2-{config.generation_id}-{model_name}-f{fold.fold_index}-stress"
                    ),
                    touch_ohlcv=touch_win,
                    touch_timeframe=touch_tf if touch_win is not None else None,
                    strategy_meta={**meta, "stress": "2x_slip"},
                    costs=bt_stress_costs,
                    margin=bt_margin,
                    sizing=bt_sizing,
                    instrument=bt_instrument,
                    funding_ts_ms=funding_ts[fmask],
                    funding_rate=funding_rt[fmask],
                    plot=False,
                    print_headline=False,
                    store_path=None,
                )
                stress_fold_pnls.append(float(stress_bundle.metrics.net_pnl))
                stress_trade_pnls.extend(
                    float(t.realized_pnl) for t in stress_bundle.result.trades
                )
                if int(getattr(stress_bundle.metrics, "n_liquidations", 0) or 0) > 0:
                    any_liquidation = True
                sde = getattr(stress_bundle.result, "daily_equity", None)
                if sde is not None:
                    if isinstance(sde, pd.DataFrame) and "equity" in sde.columns:
                        seq = sde["equity"].to_numpy(dtype=float)
                    else:
                        seq = np.asarray(sde, dtype=float).reshape(-1)
                    if len(seq) > 1:
                        stress_daily.extend(
                            (np.diff(seq) / np.maximum(seq[:-1], 1e-9)).tolist()
                        )

                # Fold PF from this fold's trades (diagnostic); pooled PF uses all trades.
                fold_pnls_arr = np.array(
                    [float(t.realized_pnl) for t in trades], dtype=float
                )
                fold_pfs.append(pooled_profit_factor(fold_pnls_arr))

            pooled_trades = int(sum(fold_trades))
            weights = np.array(fold_trades, dtype=float)
            if family == "magnitude":
                pooled_skill = (
                    float(np.nansum(np.array(fold_skills) * weights) / np.nansum(weights))
                    if pooled_trades > 0 and fold_skills and weights.sum()
                    else 0.0
                )
                pooled_pf = float("nan")  # never a Profit Factor
                metric_kind = "forecast_skill"
                gate_fold_pfs = fold_skills  # fold-level skill for positive_fold_frac
            else:
                pooled_skill = float("nan")
                if config.run_backtest and all_trade_pnls:
                    pooled_pf = pooled_profit_factor(all_trade_pnls)
                else:
                    pooled_pf = (
                        float(np.nansum(np.array(fold_pfs) * weights) / np.nansum(weights))
                        if pooled_trades > 0 and fold_pfs and weights.sum()
                        else 0.0
                    )
                metric_kind = "profit_factor"
                gate_fold_pfs = fold_pfs

            daily_arr = np.asarray(all_daily, dtype=float) if all_daily else None
            model_fold_pnls[model_name] = list(fold_pnls)
            # Fold-aligned matrix only — never truncate independent daily stitches (spurious PBO).
            cand_matrix = build_fold_return_matrix(model_fold_pnls)

            stress_pnl = float(np.nansum(stress_fold_pnls)) if stress_fold_pnls else None
            stress_pf = (
                pooled_profit_factor(stress_trade_pnls) if stress_trade_pnls else None
            )
            baseline_mdd = (
                mdd_fraction_from_daily_returns(daily_arr)
                if daily_arr is not None and daily_arr.size
                else None
            )
            stress_mdd = (
                mdd_fraction_from_daily_returns(np.asarray(stress_daily, dtype=float))
                if stress_daily
                else None
            )
            margin_util = peak_margin if config.run_backtest else None

            gates = evaluate_v21_gates(
                fold_pnls=fold_pnls,
                fold_pfs=gate_fold_pfs,
                fold_trades=fold_trades,
                daily_returns=daily_arr,
                pooled_pf=None if metric_kind == "forecast_skill" else pooled_pf,
                pooled_skill=pooled_skill if metric_kind == "forecast_skill" else None,
                pooled_trades=pooled_trades,
                metric_kind=metric_kind,  # type: ignore[arg-type]
                n_trials=len(model_names),
                stress_pnl=stress_pnl,
                stress_pf=stress_pf,
                baseline_mdd=baseline_mdd,
                stress_mdd=stress_mdd,
                margin_util=margin_util,
                candidate_matrix=cand_matrix,
                liquidation=any_liquidation,
            )

            # Surrogate challenge on the last fold. Skill is measured against the
            # train-mean baseline so it is unit-free and works for targets that are not
            # centred on zero; a real fit has to beat a fit on randomised labels.
            screen_pass = bool(pred_report.passed)
            if config.run_surrogate_challenge and folds and last_pred_mean is not None:
                fold = folds[-1]
                y_s = apply_surrogate(y_all[fold.train_indices], "row_shuffle", rng=rng)
                m_s = _make_model(model_name if model_name != "lgbm_classifier" else "lgbm_regressor")
                try:
                    m_s.fit(X_all[fold.train_indices], y_s if "classifier" not in model_name else np.sign(y_s))
                    pred_s = m_s.predict(X_all[fold.oos_indices])
                    y_oos = y_all[fold.oos_indices]
                    baseline = float(np.nanmean(y_all[fold.train_indices]))
                    mae_base = float(np.nanmean(np.abs(y_oos - baseline)))
                    if mae_base > 1e-12:
                        mean_s = pred_s.mean
                        mae_s = (
                            float(np.nanmean(np.abs(y_oos - mean_s)))
                            if mean_s is not None
                            else mae_base
                        )
                        mae_r = float(np.nanmean(np.abs(y_oos - last_pred_mean)))
                        skill_real = 1.0 - mae_r / mae_base
                        skill_surr = 1.0 - mae_s / mae_base
                        if skill_real <= max(skill_surr, 0.0):
                            screen_pass = False
                            append_ledger(
                                f"SURROGATE FAIL model={model_name} "
                                f"skill_real={skill_real:+.5f} skill_surrogate={skill_surr:+.5f}",
                                tier=0,
                            )
                except Exception:  # noqa: BLE001
                    pass

            tier = _tier_from_gates(
                gates, screen_pass, require_full_gates=bool(config.run_backtest)
            )
            if family == "magnitude":
                # A volatility forecast is an input to sizing or regime filtering, never a
                # standalone strategy, so it cannot reach the human-review tier on its own.
                tier = min(tier, 1)
            headline = pooled_skill if family == "magnitude" else pooled_pf
            trial_id = db.register_trial(
                config.generation_id,
                tier=tier,
                seed=int(rng.integers(0, 2**31 - 1)),
                symbol=config.symbol,
                timeframe=config.timeframe,
                target=config.target,
                feature_space=config.feature_space,
                model=model_name,
                inner_score=inner_score,
                # DB column is historically named outer_pf; for magnitude it stores skill.
                outer_pf=float(headline) if np.isfinite(headline) else None,
                outer_trades=pooled_trades,
                status="completed",
                notes=json.dumps(
                    {
                        "metric_kind": metric_kind,
                        "pooled_pf": pooled_pf if np.isfinite(pooled_pf) else None,
                        "pooled_skill": pooled_skill if np.isfinite(pooled_skill) else None,
                        "gates": {k: v for k, v in gates.items() if isinstance(v, str)},
                    }
                ),
            )
            metric_name = "skill" if family == "magnitude" else "pf"
            entry = (
                f"trial `{trial_id}` model={model_name} tier={tier} target={config.target} "
                f"{metric_name}={float(headline):.3f} n={pooled_trades} gates={gates.get('overall')}"
            )
            append_ledger(entry, tier=tier)
            if tier >= 2:
                print(f"ALERT tier={tier} {entry}")
                print(format_gates_table(gates))
            trade_arr = np.asarray(all_trade_pnls, dtype=float) if all_trade_pnls else np.array([])
            pooled_pnl = float(np.nansum(trade_arr)) if trade_arr.size else 0.0
            wins = trade_arr[trade_arr > 0] if trade_arr.size else np.array([])
            losses = trade_arr[trade_arr < 0] if trade_arr.size else np.array([])
            win_rate = float(wins.size / trade_arr.size) if trade_arr.size else None
            expectancy = float(np.nanmean(trade_arr)) if trade_arr.size else None
            payoff = (
                float(np.nanmean(wins) / abs(np.nanmean(losses)))
                if wins.size and losses.size and abs(float(np.nanmean(losses))) > 1e-12
                else None
            )
            trial_results.append(
                {
                    "trial_id": trial_id,
                    "model": model_name,
                    "tier": tier,
                    "metric_kind": metric_kind,
                    "pooled_pf": pooled_pf if np.isfinite(pooled_pf) else None,
                    "pooled_skill": pooled_skill if np.isfinite(pooled_skill) else None,
                    "pooled_trades": pooled_trades,
                    "pooled_pnl": pooled_pnl,
                    "win_rate": win_rate,
                    "expectancy": expectancy,
                    "payoff": payoff,
                    "inner_score": inner_score,
                    "gates": gates,
                }
            )
            if tier > best_tier or (
                tier == best_tier
                and (
                    best_summary is None
                    or float(headline) > float(
                        best_summary.get("pooled_skill")
                        or best_summary.get("pooled_pf")
                        or -1
                    )
                )
            ):
                best_tier = tier
                best_summary = trial_results[-1]
        except Exception as exc:  # noqa: BLE001
            append_ledger(f"TRIAL ERROR model={model_name}: {exc}\n{traceback.format_exc()[:800]}", tier=0)
            db.register_trial(
                config.generation_id,
                tier=0,
                symbol=config.symbol,
                timeframe=config.timeframe,
                target=config.target,
                feature_space=config.feature_space,
                model=model_name,
                status="error",
                notes=str(exc)[:500],
            )

    summary = {
        "generation_id": config.generation_id,
        "status": "COMPLETE",
        "n_trials": len(trial_results),
        "best_tier": best_tier,
        "best": best_summary,
        "predictability_passed": pred_report.passed,
        "n_folds": len(folds),
        "cost_hurdle": ROUND_TRIP_COST,
        "break_even_p": hurdle.break_even_probability(),
    }
    append_ledger(f"Hunt complete: {json.dumps({k: v for k, v in summary.items() if k != 'best'}, default=str)}", tier=0)
    return summary


# Backward-compatible thin wrapper used by early CLI
def run_hunt(
    config: HuntConfig,
    X: np.ndarray | None = None,
    y: np.ndarray | None = None,
    *,
    db: ResearchDB | None = None,
) -> dict[str, Any]:
    """Prefer nested hunt; fall back to simple in-memory loop if X/y provided without warehouse."""
    if X is None or y is None:
        return run_nested_hunt(config, db=db)
    # legacy smoke path
    db = db or ResearchDB()
    db.create_generation(config.generation_id, max_trials=config.max_trials)
    results = []
    for i, name in enumerate(config.models[: config.max_trials]):
        try:
            m = _make_model(name)
            yy = np.sign(y) if "classifier" in name else y
            m.fit(X, yy)
            pred = m.predict(X)
            score = float(np.nanmean(pred.mean)) if pred.mean is not None else 0.0
        except Exception as exc:  # noqa: BLE001
            score = float("nan")
            name = f"{name}:error:{exc}"
        tid = db.register_trial(
            config.generation_id,
            tier=0,
            model=name,
            inner_score=score,
            status="completed",
            symbol=config.symbol,
            timeframe=config.timeframe,
            target=config.target,
            feature_space=config.feature_space,
        )
        results.append({"trial_id": tid, "score": score, "model": name})
    return {"generation_id": config.generation_id, "n_trials": len(results), "status": "LEGACY_SMOKE"}
