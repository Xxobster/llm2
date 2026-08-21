#!/usr/bin/env python3
"""ETH K5: size_mult ∝ |pred_mean| vs live time-double control.

Outer walk-forward stitch before lockbox. MEASURE_DIAGNOSTIC / RESEARCH_ONLY.
Does not authorize live pack changes.

Formula (candidate):
  strength_mult = clip(|pred_mean| / 0.5, 1.0, 2.0)
  size_mult = time_mult × strength_mult
  time_mult = 2 if same-side entry within 3h else 1  (when double enabled)

Run::

  python scripts/settle_eth_k5_size_scale_absmean_001.py
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import numpy as np
import pandas as pd

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

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
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import DIRECTION_BAND, proxy_side, target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.signals.cluster_concurrency import build_cluster_size_signals  # noqa: E402
from llm2.signals.singlebook_clarity import SingleBookArm  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
)

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
LABEL_HORIZON = 6
K = 5
SL = 0.02
MIN_EDGE = DIRECTION_BAND
GEN = "structure_v1_eth_k5_size_scale_absmean_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
ARM = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
STRENGTH_Q = 0.5  # live median clarity — isolate size effect


def _finite(x: Any) -> Any:
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    if isinstance(x, (np.floating,)):
        v = float(x)
        return None if not math.isfinite(v) else v
    if isinstance(x, (np.integer,)):
        return int(x)
    return x


def _metrics_from_bundle(bundle: Any) -> dict[str, Any]:
    m = bundle.metrics
    sh = getattr(m, "sharpe", None)
    return {
        "n_trades": int(m.n_trades),
        "net_pnl": _finite(float(m.net_pnl)),
        "profit_factor": _finite(float(m.profit_factor)),
        "win_rate": _finite(float(m.win_rate)),
        "expectancy": _finite(float(getattr(m, "expectancy", float("nan")))),
        "expectancy_return_units": _finite(
            float(getattr(m, "expectancy_return_units", float("nan")))
        ),
        "total_fees": _finite(float(getattr(m, "total_fees", float("nan")))),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "max_drawdown": _finite(float(getattr(m, "max_drawdown", float("nan")))),
        "sharpe_annualised": _finite(
            float(getattr(sh, "annualised", getattr(sh, "annualized", float("nan"))))
        )
        if sh is not None
        else None,
    }


def _pf(pnls: list[float]) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return float("nan")
    gp = float(a[a > 0].sum())
    gl = float((-a[a < 0]).sum())
    if gl <= 0:
        return float("inf") if gp > 0 else float("nan")
    return gp / gl


def stitch_arm(
    *,
    label: str,
    size_double_within_bars: int,
    size_scale_by_abs_mean: bool,
    size_scale_ref: float = 0.5,
    size_scale_factor_min: float = 1.0,
    size_scale_factor_max: float = 2.0,
) -> dict[str, Any]:
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    touch = load_ohlcv(SYMBOL, touch_timeframe(TIMEFRAME, SYMBOL))
    touch_tf = touch_timeframe(TIMEFRAME, SYMBOL)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(SYMBOL)
    family = target_family(TARGET)
    close_full = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)

    fold_rows: list[dict[str, Any]] = []
    all_pnls: list[float] = []
    all_fees = 0.0
    n_liq = 0
    total_stats: dict[str, float] = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_size_1x": 0,
        "n_size_2x": 0,
        "n_size_strength_scaled": 0,
        "mean_size_mult_sum": 0.0,
        "mean_size_mult_n": 0,
    }

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        close_oos = close_full[oos]
        sigs, stats = build_cluster_size_signals(
            oos_ts,
            side,
            mean,
            close_oos,
            arm=ARM,
            min_edge=MIN_EDGE,
            max_per_side=K,
            instrument=instrument,
            size_double_within_bars=int(size_double_within_bars),
            strength_quantile=STRENGTH_Q,
            size_scale_by_abs_mean=bool(size_scale_by_abs_mean),
            size_scale_ref=float(size_scale_ref),
            size_scale_factor_min=float(size_scale_factor_min),
            size_scale_factor_max=float(size_scale_factor_max),
        )
        for k in (
            "n_emitted",
            "n_skipped_clarity",
            "n_size_1x",
            "n_size_2x",
            "n_size_strength_scaled",
        ):
            total_stats[k] = float(total_stats[k]) + float(stats.get(k, 0) or 0)
        if stats.get("mean_size_mult") is not None and stats.get("n_emitted", 0):
            n_e = float(stats.get("n_emitted") or 0)
            total_stats["mean_size_mult_sum"] += float(stats["mean_size_mult"]) * n_e
            total_stats["mean_size_mult_n"] += n_e

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, int(ARM.horizon_bars) * 4)
        pos = int(ohlcv.index.searchsorted(oos0))
        window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
        end, start = window.index[-1], window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
        w_ts = index_to_ms(window.index)
        fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
        bundle = run_strategy_backtest(
            window,
            sigs,
            symbol=SYMBOL,
            timeframe=TIMEFRAME,
            strategy_id=f"{label}-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_hedge(
                max_hold_bars=int(ARM.horizon_bars),
                decision_timeframe=TIMEFRAME,
                max_positions_per_side=K,
                max_positions_per_symbol=K * 2,
            ),
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={
                "name": label,
                "generation_id": GEN,
                "size_double_within_bars": size_double_within_bars,
                "size_scale_by_abs_mean": size_scale_by_abs_mean,
            },
            plot=False,
            print_headline=False,
            store_path=None,
        )
        mdict = _metrics_from_bundle(bundle)
        pnls = [float(getattr(t, "realized_pnl", 0) or 0) for t in bundle.result.trades]
        all_pnls.extend(pnls)
        all_fees += float(mdict.get("total_fees") or 0.0)
        n_liq += int(mdict.get("n_liquidations") or 0)
        fold_rows.append({"fold_index": int(fold.fold_index), **mdict})
        print(
            f"  {label} fold {fold.fold_index}: n={mdict['n_trades']} "
            f"pnl={mdict['net_pnl']} pf={mdict['profit_factor']} "
            f"exp_ru={mdict['expectancy_return_units']}",
            flush=True,
        )

    wins = sum(1 for p in all_pnls if p > 0)
    exp_num = exp_den = exp_usdt = 0.0
    for fr in fold_rows:
        n = float(fr.get("n_trades") or 0)
        if n > 0 and fr.get("expectancy_return_units") is not None:
            exp_num += float(fr["expectancy_return_units"]) * n
            exp_den += n
        if n > 0 and fr.get("expectancy") is not None:
            exp_usdt += float(fr["expectancy"]) * n
    mean_sm = (
        total_stats["mean_size_mult_sum"] / total_stats["mean_size_mult_n"]
        if total_stats["mean_size_mult_n"] > 0
        else None
    )
    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "win_rate": float(wins / len(all_pnls)) if all_pnls else float("nan"),
        "expectancy": (exp_usdt / exp_den) if exp_den else float("nan"),
        "expectancy_return_units": (exp_num / exp_den) if exp_den else float("nan"),
        "total_fees": all_fees,
        "n_liquidations": int(n_liq),
        "mean_size_mult": _finite(mean_sm) if mean_sm is not None else None,
        "frac_folds_pf_gt_1": float(
            np.mean([float(r.get("profit_factor") or 0) > 1 for r in fold_rows])
        )
        if fold_rows
        else float("nan"),
    }
    return {
        "label": label,
        "cfg": {
            "k": K,
            "strength_quantile": STRENGTH_Q,
            "hold": 12,
            "tp": 0.01,
            "sl": SL,
            "size_double_within_bars": int(size_double_within_bars),
            "size_scale_by_abs_mean": bool(size_scale_by_abs_mean),
            "size_scale_ref": float(size_scale_ref),
            "size_scale_factor_min": float(size_scale_factor_min),
            "size_scale_factor_max": float(size_scale_factor_max),
            "size_formula": (
                "size_mult = time_mult × clip(|pred_mean|/0.5, 1, 2); "
                "time_mult = 2 if same-side within size_double_within_bars else 1"
            ),
        },
        "folds": fold_rows,
        "stitched": stitched,
        "signal_stats_total": {
            k: int(v) if k.startswith("n_") else v for k, v in total_stats.items()
            if k not in ("mean_size_mult_sum", "mean_size_mult_n")
        },
        "leverage": lev,
    }


def main() -> int:
    t0 = time.perf_counter()
    if not PREREG.is_file():
        print(f"MISSING prereg {PREREG}", file=sys.stderr)
        return 2
    conf = run_conformance_check()
    conf_ok = bool(getattr(conf, "passed", conf is True if conf is True else False))
    if isinstance(conf, dict):
        conf_ok = bool(conf.get("passed") or conf.get("ok"))
    print(f"conformance_ok={conf_ok}", flush=True)

    arms = [
        {
            "label": "control_time_double",
            "size_double_within_bars": 3,
            "size_scale_by_abs_mean": False,
        },
        {
            "label": "size_scale_on_time_double",
            "size_double_within_bars": 3,
            "size_scale_by_abs_mean": True,
        },
        {
            "label": "size_scale_only",
            "size_double_within_bars": 0,
            "size_scale_by_abs_mean": True,
        },
    ]
    results = []
    for arm in arms:
        print(f"=== {arm['label']} ===", flush=True)
        results.append(
            stitch_arm(
                label=arm["label"],
                size_double_within_bars=arm["size_double_within_bars"],
                size_scale_by_abs_mean=arm["size_scale_by_abs_mean"],
            )
        )

    control = results[0]["stitched"]
    compare_rows = []
    for r in results:
        s = r["stitched"]
        compare_rows.append(
            {
                "label": r["label"],
                "n_trades": s["n_trades"],
                "net_pnl": s["net_pnl"],
                "profit_factor": s["profit_factor"],
                "expectancy_return_units": s["expectancy_return_units"],
                "win_rate": s["win_rate"],
                "total_fees": s["total_fees"],
                "n_liquidations": s["n_liquidations"],
                "mean_size_mult": s.get("mean_size_mult"),
                "delta_net_pnl_vs_control": (
                    None
                    if r["label"] == "control_time_double"
                    else float(s["net_pnl"] or 0) - float(control["net_pnl"] or 0)
                ),
                "delta_exp_ru_vs_control": (
                    None
                    if r["label"] == "control_time_double"
                    or s.get("expectancy_return_units") is None
                    or control.get("expectancy_return_units") is None
                    else float(s["expectancy_return_units"])
                    - float(control["expectancy_return_units"])
                ),
            }
        )
        print(
            f"SUMMARY {r['label']}: n={s['n_trades']} pnl={s['net_pnl']:.4f} "
            f"PF={s['profit_factor']} E[r]={s['expectancy_return_units']} "
            f"mean_x={s.get('mean_size_mult')}",
            flush=True,
        )

    # Verdict: capital (net_pnl) and quality (E[r], PF) vs control
    cand = next(c for c in compare_rows if c["label"] == "size_scale_on_time_double")
    wins_capital = (
        cand["delta_net_pnl_vs_control"] is not None
        and cand["delta_net_pnl_vs_control"] > 0
        and int(cand["n_liquidations"] or 0) == 0
        and int(control.get("n_liquidations") or 0) == 0
    )
    out = {
        "generation_id": GEN,
        "gate_name": "ETH K5 size scale by |pred_mean|",
        "evidence_class": "MEASURE_DIAGNOSTIC",
        "maximum_earned_readiness": "RESEARCH_ONLY",
        "promotion_allowed": False,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "hard_end_exclusive": str(FORWARD_LOCKBOX_START),
        "lockbox_used": False,
        "conformance_ok": conf_ok,
        "prereg_sha256": hashlib.sha256(PREREG.read_bytes()).hexdigest(),
        "formula": {
            "strength_mult": "clip(|pred_mean|/0.5, 1.0, 2.0)",
            "size_mult": "time_mult × strength_mult",
            "time_mult": "2 if same-side entry within 3h else 1 (when enabled)",
            "note": (
                "MIN_EXCHANGE×size_mult sizes positions; E[r] often stable while "
                "net_pnl scales with notional. Not a readiness unlock."
            ),
        },
        "arms": results,
        "compare": compare_rows,
        "verdict": {
            "size_scale_on_time_double_raises_net_pnl": bool(wins_capital),
            "principal_blocker": None
            if wins_capital
            else "NO_NET_PNL_LIFT_OR_LIQ"
            if cand.get("delta_net_pnl_vs_control", 0) is not None
            and float(cand.get("delta_net_pnl_vs_control") or 0) <= 0
            else "SEE_COMPARE",
        },
        "elapsed_sec": time.perf_counter() - t0,
    }
    stamp_min_size_equity_caveat(out)
    reports = ARTIFACTS / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    stamp = out["created_utc"]
    path = reports / f"{GEN}_{stamp}.json"
    latest = reports / f"{GEN}_latest.json"
    blob = json.dumps(out, indent=2, default=str)
    path.write_text(blob, encoding="utf-8")
    latest.write_text(blob, encoding="utf-8")
    print(json.dumps({"compare": compare_rows, "verdict": out["verdict"]}, indent=2), flush=True)
    print(f"WROTE {latest}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
