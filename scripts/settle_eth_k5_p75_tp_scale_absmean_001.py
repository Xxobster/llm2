"""Nested settle: ETH K5 p75 + TP scale by |pred_mean| vs p75 fixed TP.

Control = shipped p75 (q=0.75, TP 1%). Candidate adds frozen proportional TP.
Outer folds only; lockbox unused. Evidence OUTER_TRANSFER_COMPARE.
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
from llm2.evidence.pack_registry import (  # noqa: E402
    ensure_registry_schema,
    register_compare_report,
)
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
STRENGTH_Q = 0.75
GEN = "structure_v1_eth_k5_p75_tp_scale_absmean_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN}.yaml"
CONTROL_PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_k5_double3h_p75_v1"
ARM = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "payoff_ratio": _finite(float(getattr(m, "payoff_ratio", float("nan")))),
        "avg_win": _finite(float(getattr(m, "avg_win", float("nan")))),
        "avg_loss": _finite(float(getattr(m, "avg_loss", float("nan")))),
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


def stitch_arm(*, tp_scale: bool, label: str) -> dict[str, Any]:
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
    tp_vals: list[float] = []
    total_stats: dict[str, int] = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_size_1x": 0,
        "n_size_2x": 0,
    }
    run_ids: list[str] = []

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
            size_double_within_bars=3,
            strength_quantile=STRENGTH_Q,
            tp_scale_by_abs_mean=bool(tp_scale),
            tp_scale_ref=0.5,
            tp_scale_factor_min=1.0,
            tp_scale_factor_max=2.0,
        )
        for k in total_stats:
            total_stats[k] += int(stats.get(k, 0) or 0)
        for s in sigs:
            tp_vals.append(float(s.target_offset))

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
                "strength_quantile": STRENGTH_Q,
                "tp_scale_by_abs_mean": bool(tp_scale),
                "k": K,
            },
            plot=False,
            print_headline=False,
            store_path=r"D:\projectsdata\backtests\tradesim_runs.sqlite",
        )
        mdict = _metrics_from_bundle(bundle)
        pnls = [
            float(getattr(t, "realized_pnl", 0) or 0) for t in bundle.result.trades
        ]
        all_pnls.extend(pnls)
        all_fees += float(mdict.get("total_fees") or 0.0)
        n_liq += int(mdict.get("n_liquidations") or 0)
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                **mdict,
                "signal_stats": {k: int(stats.get(k, 0) or 0) for k in total_stats},
            }
        )
        rid = getattr(bundle, "run_id", None)
        if rid is None:
            rid = getattr(getattr(bundle, "result", None), "run_id", None)
        meta_obj = getattr(bundle, "meta", None)
        if rid is None and isinstance(meta_obj, dict):
            rid = meta_obj.get("run_id")
        if rid:
            run_ids.append(str(rid))
        print(
            f"  {label} fold {fold.fold_index}: n={mdict['n_trades']} "
            f"pf={mdict['profit_factor']} exp_ru={mdict['expectancy_return_units']}",
            flush=True,
        )

    stitched_pf = _pf(all_pnls)
    wins = sum(1 for p in all_pnls if p > 0)
    exp_num = 0.0
    exp_den = 0.0
    exp_usdt_num = 0.0
    for fr in fold_rows:
        n = float(fr.get("n_trades") or 0)
        eru = fr.get("expectancy_return_units")
        eu = fr.get("expectancy")
        if n > 0 and eru is not None:
            exp_num += float(eru) * n
            exp_den += n
        if n > 0 and eu is not None:
            exp_usdt_num += float(eu) * n
    tp_a = np.asarray(tp_vals, dtype=float)
    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": stitched_pf,
        "win_rate": float(wins / len(all_pnls)) if all_pnls else float("nan"),
        "expectancy": (exp_usdt_num / exp_den) if exp_den else float("nan"),
        "expectancy_return_units": (exp_num / exp_den) if exp_den else float("nan"),
        "total_fees": all_fees,
        "n_liquidations": int(n_liq),
        "mean_tp_pct": float(np.nanmean(tp_a)) if tp_a.size else float("nan"),
        "median_tp_pct": float(np.nanmedian(tp_a)) if tp_a.size else float("nan"),
        "frac_folds_pf_gt_1": float(
            np.mean([float(r["profit_factor"] or 0) > 1 for r in fold_rows])
        )
        if fold_rows
        else float("nan"),
    }
    return {
        "label": label,
        "strength_quantile": STRENGTH_Q,
        "tp_scale_by_abs_mean": bool(tp_scale),
        "cfg": {
            "k": K,
            "clarity": "mean_strength",
            "clarity_scope": "all",
            "strength_quantile": STRENGTH_Q,
            "hold": 12,
            "tp_base": 0.01,
            "tp_scale_by_abs_mean": bool(tp_scale),
            "tp_scale_formula": "0.01*min(2,max(1,abs(mean)/0.5))" if tp_scale else "0.01",
            "sl": SL,
            "size_double_within_bars": 3,
        },
        "folds": fold_rows,
        "stitched": stitched,
        "signal_stats_total": total_stats,
        "tradesim_run_ids": run_ids,
        "leverage": lev,
    }


def main() -> int:
    t0 = time.perf_counter()
    if not PREREG.is_file():
        raise SystemExit(f"missing preregister {PREREG}")
    prereg_sha = _sha(PREREG)
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")
    ensure_registry_schema()

    print(f"[{GEN}] control (p75 fixed TP) stitch …", flush=True)
    control = stitch_arm(tp_scale=False, label=f"{GEN}_control")
    print(
        f"  control PF={control['stitched']['profit_factor']:.4f} "
        f"exp_ru={control['stitched']['expectancy_return_units']} "
        f"n={control['stitched']['n_trades']}",
        flush=True,
    )
    print(f"[{GEN}] candidate (p75 + TP∝|mean|) stitch …", flush=True)
    candidate = stitch_arm(tp_scale=True, label=f"{GEN}_candidate")
    print(
        f"  candidate PF={candidate['stitched']['profit_factor']:.4f} "
        f"exp_ru={candidate['stitched']['expectancy_return_units']} "
        f"mean_tp={candidate['stitched']['mean_tp_pct']} "
        f"n={candidate['stitched']['n_trades']}",
        flush=True,
    )

    c_exp = control["stitched"]["expectancy_return_units"]
    k_exp = candidate["stitched"]["expectancy_return_units"]
    c_pf = control["stitched"]["profit_factor"]
    k_pf = candidate["stitched"]["profit_factor"]
    beat_exp = (
        c_exp is not None
        and k_exp is not None
        and math.isfinite(float(c_exp))
        and math.isfinite(float(k_exp))
        and float(k_exp) > float(c_exp)
    )
    pf_ok = k_pf is not None and math.isfinite(float(k_pf)) and float(k_pf) >= 1.20
    no_liq = int(candidate["stitched"]["n_liquidations"]) == 0
    passed = bool(beat_exp and pf_ok and no_liq)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
            "preregister_sha256": prereg_sha,
            "evidence_class": "OUTER_TRANSFER_COMPARE",
            "max_readiness": "RESEARCH_ONLY",
            "promotion_allowed": False,
            "live_deploy": "FORBIDDEN",
            "primary_metric": "expectancy_return_units",
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "conformance_passed": bool(conf.get("passed")),
            "control_pack": str(CONTROL_PACK.relative_to(_ROOT)).replace("\\", "/"),
            "control": control,
            "candidate": candidate,
            "compare": {
                "control_expectancy_return_units": c_exp,
                "candidate_expectancy_return_units": k_exp,
                "exp_ru_delta": (
                    float(k_exp) - float(c_exp)
                    if c_exp is not None
                    and k_exp is not None
                    and math.isfinite(float(c_exp))
                    and math.isfinite(float(k_exp))
                    else None
                ),
                "control_pf": c_pf,
                "candidate_pf": k_pf,
                "candidate_mean_tp_pct": candidate["stitched"].get("mean_tp_pct"),
                "candidate_beats_control_exp_ru": beat_exp,
                "candidate_pf_ge_1_20": pf_ok,
                "candidate_no_liquidation": no_liq,
                "passed_success_criteria": passed,
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "note": (
                "Nested on p75 control only. Formula TP=1%*min(2,max(1,|mean|/0.5)). "
                "No clarity×hold×TP reopen. MIN_EXCHANGE dust caveat."
            ),
        }
    )
    out_dir = ARTIFACTS / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    latest = out_dir / f"{GEN}_latest.json"
    latest.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (out_dir / f"{GEN}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )

    text = PREREG.read_text(encoding="utf-8")
    if "status: FROZEN" in text:
        text = text.replace(
            "status: FROZEN",
            f"status: OOS_COMPARE_COMPLETE\nsettled_utc: \"{stamp}\"\n"
            f"preregister_sha256_at_run: {prereg_sha}",
            1,
        )
        PREREG.write_text(text, encoding="utf-8")

    run_ids = list(control.get("tradesim_run_ids") or []) + list(
        candidate.get("tradesim_run_ids") or []
    )
    register_compare_report(
        GEN,
        report_path=latest,
        control_metrics=control["stitched"],
        candidate_metrics=candidate["stitched"],
        tradesim_run_ids=run_ids,
        control_version_id="eth_k5_double3h_p75_v1",
    )

    print(json.dumps(report["compare"], indent=2))
    print(f"wrote {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
