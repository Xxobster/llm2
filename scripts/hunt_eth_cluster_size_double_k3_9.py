"""ETH: K=3..9 concurrency with optional 2× size when signal ≤3h after last entry.

Walk-forward fold V2 only (no future peek, lockbox excluded).
Preregister: configs/preregister/structure_v1_eth_cluster_size_double_k3_9_001.yaml
"""

from __future__ import annotations

import argparse
import hashlib
import json
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
from llm2.signals.cluster_concurrency import (  # noqa: E402
    build_cluster_concurrent_signals,
    build_cluster_size_signals,
)
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
SL = 0.02
MIN_EDGE = DIRECTION_BAND
BASE = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
K_VALUES = (3, 4, 5, 6, 7, 8, 9)
PREREG = _ROOT / "configs" / "preregister" / "structure_v1_eth_cluster_size_double_k3_9_001.yaml"
GEN_ID = "structure_v1_eth_cluster_size_double_k3_9_001"
REPORT_DIR = ARTIFACTS / "reports"


def _json_default(obj: object) -> object:
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        return None if not np.isfinite(v) else v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    raise TypeError(type(obj))


def _pf(pnls: list[float] | np.ndarray) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return float("nan")
    gp = float(a[a > 0].sum())
    gl = float((-a[a < 0]).sum())
    if gl <= 0:
        return float("inf") if gp > 0 else float("nan")
    return gp / gl


def _bootstrap_pos_exp(pnls: np.ndarray, n: int = 2000, seed: int = 42) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size < 10:
        return float("nan")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(a), size=(n, len(a)))
    return float(np.mean(a[idx].mean(axis=1) > 0))


def _touch_window(ohlcv: pd.DataFrame) -> tuple[pd.DataFrame | None, str | None]:
    try:
        tf = touch_timeframe(TIMEFRAME, SYMBOL)
        return load_ohlcv(SYMBOL, tf), tf
    except Exception:  # noqa: BLE001
        return None, None


def _bt(
    window: pd.DataFrame,
    signals: list,
    *,
    k: int,
    hold: int,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
    label: str,
) -> dict[str, Any]:
    sim = research_sim_hedge(
        max_hold_bars=int(hold),
        decision_timeframe=TIMEFRAME,
        max_positions_per_side=int(k),
        max_positions_per_symbol=int(k) * 2,
    )
    touch_win = None
    if touch is not None and len(window):
        end = window.index[-1]
        start = window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
    w_ts = index_to_ms(window.index)
    fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
    bundle = run_strategy_backtest(
        window,
        signals,
        symbol=SYMBOL,
        timeframe=TIMEFRAME,
        strategy_id=label,
        touch_ohlcv=touch_win,
        touch_timeframe=touch_tf,
        costs=research_costs_baseline(),
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=sim,
        instrument=instrument,
        funding_ts_ms=funding_ts[fmask],
        funding_rate=funding_rt[fmask],
        strategy_meta={"name": label, "batch": GEN_ID, "k": k},
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    pnls = [float(getattr(t, "realized_pnl", 0.0) or 0.0) for t in bundle.result.trades]
    return {
        "n_trades": int(m.n_trades),
        "net_pnl": float(m.net_pnl),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "trade_pnls": pnls,
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
    }


def _window_for_oos(
    ohlcv: pd.DataFrame, aligned_index: pd.DatetimeIndex, oos: np.ndarray, hold: int
) -> pd.DataFrame:
    oos_start = aligned_index[oos[0]]
    oos_end = aligned_index[oos[-1]]
    pad = max(50, int(hold) * 4)
    pos = int(ohlcv.index.searchsorted(oos_start))
    pad_start = ohlcv.index[max(0, pos - pad)]
    return ohlcv.loc[pad_start:oos_end]


def walk_arm(
    *,
    name: str,
    k: int,
    size_mode: str,
    X: np.ndarray,
    yv: np.ndarray,
    ts_ms: np.ndarray,
    close_all: np.ndarray,
    aligned_index: pd.DatetimeIndex,
    ohlcv: pd.DataFrame,
    folds: list,
    family: str,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
) -> dict[str, Any]:
    fold_rows = []
    all_pnls: list[float] = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        close_oos = close_all[oos]
        if size_mode == "flat_1x":
            signals, stats = build_cluster_concurrent_signals(
                ts_ms[oos],
                side,
                mean,
                arm=BASE,
                min_edge=MIN_EDGE,
                max_per_side=k,
                cluster_bars=None,
            )
        elif size_mode == "double_within_3h":
            signals, stats = build_cluster_size_signals(
                ts_ms[oos],
                side,
                mean,
                close_oos,
                arm=BASE,
                min_edge=MIN_EDGE,
                max_per_side=k,
                instrument=instrument,
                size_double_within_bars=3,
            )
        else:
            raise ValueError(size_mode)
        window = _window_for_oos(ohlcv, aligned_index, oos, BASE.horizon_bars)
        bt = _bt(
            window,
            signals,
            k=k,
            hold=BASE.horizon_bars,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"{name}-f{fold.fold_index}",
        )
        all_pnls.extend(bt["trade_pnls"])
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "n_signals": int(stats["n_emitted"]),
                "signal_stats": {
                    key: stats.get(key)
                    for key in (
                        "n_emitted",
                        "n_primary",
                        "n_addon",
                        "n_skipped_cap",
                        "n_size_1x",
                        "n_size_2x",
                    )
                    if key in stats
                },
                "metrics": {key: val for key, val in bt.items() if key != "trade_pnls"},
            }
        )
        print(
            f"  [{name}] fold {fold.fold_index}: n={bt['n_trades']} "
            f"pf={bt['profit_factor']:.3f} pnl={bt['net_pnl']:.2f} "
            f"2x={stats.get('n_size_2x', 0)}",
            flush=True,
        )
    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "bootstrap_pos_exp": _bootstrap_pos_exp(np.asarray(all_pnls)),
        "frac_folds_pf_gt_1": float(
            np.mean([r["metrics"]["profit_factor"] > 1.0 for r in fold_rows])
        ),
        "frac_folds_pnl_gt_0": float(np.mean([r["metrics"]["net_pnl"] > 0 for r in fold_rows])),
        "n_liquidations": int(sum(r["metrics"].get("n_liquidations", 0) for r in fold_rows)),
    }
    return {
        "name": name,
        "k": k,
        "size_mode": size_mode,
        "max_total_both_sides": int(k) * 2,
        "base_arm": BASE.key,
        "folds": fold_rows,
        "stitched": stitched,
    }


def run(*, skip_conformance: bool = False) -> dict[str, Any]:
    t0 = time.perf_counter()
    if skip_conformance:
        conf: dict[str, Any] = {"status": "skipped", "passed": None}
    else:
        conf = run_conformance_check()
        print(f"conformance: {conf.get('status')}", flush=True)
        if conf.get("passed") is False:
            raise RuntimeError("conformance failed")

    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    PREREG.with_suffix(".sha256").write_text(sha + "\n", encoding="utf-8")

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    # Allowed research window only — exclude lockbox (no future peek / no lockbox tune)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    # Close aligned to feature rows (causal bar close used only for min-qty estimate)
    close_all = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    touch, touch_tf = _touch_window(ohlcv)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(SYMBOL)
    family = target_family(TARGET)

    arms: list[tuple[str, int, str]] = []
    for k in K_VALUES:
        arms.append((f"k{k}_flat_1x", k, "flat_1x"))
        arms.append((f"k{k}_double3h", k, "double_within_3h"))

    results = []
    for name, k, mode in arms:
        print(f"\n=== {name} k={k} max_total={k*2} ===", flush=True)
        results.append(
            walk_arm(
                name=name,
                k=k,
                size_mode=mode,
                X=X,
                yv=yv,
                ts_ms=ts_ms,
                close_all=close_all,
                aligned_index=aligned.index,
                ohlcv=ohlcv,
                folds=folds,
                family=family,
                touch=touch,
                touch_tf=touch_tf,
                funding_ts=funding_ts,
                funding_rt=funding_rt,
                lev=lev,
                instrument=instrument,
            )
        )

    summary = []
    by_k: dict[int, dict[str, dict[str, Any]]] = {}
    for r in results:
        s = r["stitched"]
        row = {
            "name": r["name"],
            "k": r["k"],
            "size_mode": r["size_mode"],
            "max_total_both_sides": r["max_total_both_sides"],
            "profit_factor": s["profit_factor"],
            "net_pnl": s["net_pnl"],
            "n_trades": s["n_trades"],
            "bootstrap_pos_exp": s["bootstrap_pos_exp"],
            "n_liquidations": s["n_liquidations"],
        }
        summary.append(row)
        by_k.setdefault(int(r["k"]), {})[str(r["size_mode"])] = row

    comparisons = []
    for k in K_VALUES:
        flat = by_k[k]["flat_1x"]
        dbl = by_k[k]["double_within_3h"]
        comparisons.append(
            {
                "k": k,
                "flat_1x_pf": flat["profit_factor"],
                "double3h_pf": dbl["profit_factor"],
                "delta_pf": float(dbl["profit_factor"]) - float(flat["profit_factor"]),
                "flat_1x_pnl": flat["net_pnl"],
                "double3h_pnl": dbl["net_pnl"],
                "delta_pnl": float(dbl["net_pnl"]) - float(flat["net_pnl"]),
                "double_beats_flat_pf": float(dbl["profit_factor"]) > float(flat["profit_factor"]),
                "double_beats_flat_pnl": float(dbl["net_pnl"]) > float(flat["net_pnl"]),
            }
        )

    best_dbl = max(
        (s for s in summary if s["size_mode"] == "double_within_3h"),
        key=lambda s: (s["profit_factor"] if np.isfinite(s["profit_factor"]) else -1e9),
    )
    n_pf_wins = sum(1 for c in comparisons if c["double_beats_flat_pf"])
    n_pnl_wins = sum(1 for c in comparisons if c["double_beats_flat_pnl"])

    return {
        "generation_id": GEN_ID,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
        "preregister_sha256": sha,
        "evidence_class": "fold_V2_stitched_size_double_cluster_k3_9",
        "lockbox_used": False,
        "future_peek": False,
        "data_end_exclusive": FORWARD_LOCKBOX_START,
        "base_arm": BASE.key,
        "conformance": conf,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "symbol": SYMBOL,
        "target": TARGET,
        "rule": "qty=2*min_exchange if signal within 3h of last same-side entry else 1x",
        "arms": results,
        "summary": summary,
        "comparisons_by_k": comparisons,
        "verdict": {
            "best_double3h_pf_arm": best_dbl,
            "double_pf_wins_vs_flat": n_pf_wins,
            "double_pnl_wins_vs_flat": n_pnl_wins,
            "n_k_tested": len(K_VALUES),
            "max_readiness": "RESEARCH_ONLY",
            "caveat": "min-exchange / 2x stacked books; not scale or liquidation evidence",
            "no_live_deploy": True,
        },
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "tradesim_file": str(__import__("tradesim").__file__),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skip-conformance", action="store_true")
    args = ap.parse_args()
    report = run(skip_conformance=bool(args.skip_conformance))
    if "botsgeneral" not in str(report["tradesim_file"]).lower():
        raise RuntimeError("tradesim not from botsgeneral")
    stamp = report["created_utc"]
    out = REPORT_DIR / f"{GEN_ID}_{stamp}.json"
    latest = REPORT_DIR / f"{GEN_ID}_latest.json"
    text = json.dumps(report, indent=2, default=_json_default)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")
    print("\n=== COMPARISON flat_1x vs double_within_3h ===", flush=True)
    for c in report["comparisons_by_k"]:
        print(
            f"k={c['k']} flat_pf={c['flat_1x_pf']:.4f} dbl_pf={c['double3h_pf']:.4f} "
            f"dPF={c['delta_pf']:+.4f} flat_pnl={c['flat_1x_pnl']:.1f} "
            f"dbl_pnl={c['double3h_pnl']:.1f} dPnL={c['delta_pnl']:+.1f}",
            flush=True,
        )
    v = report["verdict"]
    print(
        f"double PF wins {v['double_pf_wins_vs_flat']}/{v['n_k_tested']} "
        f"PnL wins {v['double_pnl_wins_vs_flat']}/{v['n_k_tested']}",
        flush=True,
    )
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
