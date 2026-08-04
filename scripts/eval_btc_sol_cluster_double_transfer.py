"""Transfer frozen ETH K=1 clarity + K=5 double3h to BTCUSDT / SOLUSDT (no re-rank).

Hard end: FORWARD_LOCKBOX_START. RESEARCH_ONLY.
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
    research_sim,
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
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.signals.cluster_concurrency import (  # noqa: E402
    build_cluster_concurrent_signals,
    build_cluster_size_signals,
)
from llm2.signals.singlebook_clarity import SingleBookArm, build_singlebook_signals  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
)

TIMEFRAME = "1h"
SPACE = "structure_v1"
LABEL_HORIZON = 6
SL = 0.02
CLARITY = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
CONTROL = SingleBookArm(clarity="none", horizon_bars=6, tp_pct=0.01, sl_pct=SL)
GEN_ID = "structure_v1_btc_sol_cluster_double_transfer_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN_ID}.yaml"
REPORT_DIR = ARTIFACTS / "reports"
COMBOS = (
    ("BTCUSDT", "fwd_return"),
    ("SOLUSDT", "direction"),
)
ARMS = (
    {"id": "control_live", "k": 1, "arm": CONTROL, "double_bars": 0, "mode": "single"},
    {"id": "k1_clarity", "k": 1, "arm": CLARITY, "double_bars": 0, "mode": "single"},
    {"id": "k5_double3h", "k": 5, "arm": CLARITY, "double_bars": 3, "mode": "double"},
)


def _json_default(obj: object) -> object:
    if isinstance(obj, float) and (np.isnan(obj) or np.isinf(obj)):
        return None
    if isinstance(obj, (np.floating,)):
        v = float(obj)
        return None if not np.isfinite(v) else v
    if isinstance(obj, (np.integer,)):
        return int(obj)
    raise TypeError(type(obj))


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def _min_edge(target: str) -> float:
    return float(DIRECTION_BAND) if target_family(target) == "directional" else float(ROUND_TRIP_COST)


def _labels(ohlcv: pd.DataFrame, target: str) -> pd.Series:
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=LABEL_HORIZON)["fwd_return"]
    raise ValueError(target)


def _window_for_oos(
    ohlcv: pd.DataFrame, aligned_index: pd.DatetimeIndex, oos: np.ndarray, hold: int
) -> pd.DataFrame:
    oos_start = aligned_index[oos[0]]
    oos_end = aligned_index[oos[-1]]
    pad = max(50, int(hold) * 4)
    pos = int(ohlcv.index.searchsorted(oos_start))
    pad_start = ohlcv.index[max(0, pos - pad)]
    return ohlcv.loc[pad_start:oos_end]


def _bt(
    window: pd.DataFrame,
    signals: list,
    *,
    symbol: str,
    hold: int,
    k: int,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
    label: str,
) -> dict[str, Any]:
    if k <= 1:
        sim = research_sim(max_hold_bars=int(hold), decision_timeframe=TIMEFRAME)
    else:
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
        symbol=symbol,
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
        strategy_meta={"name": label, "batch": GEN_ID},
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
        "trade_pnls": pnls,
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
    }


def eval_arm_on_symbol(
    *,
    symbol: str,
    target: str,
    arm_spec: dict[str, Any],
    X: np.ndarray,
    yv: np.ndarray,
    close_all: np.ndarray,
    ts_ms: np.ndarray,
    aligned_index: pd.DatetimeIndex,
    ohlcv: pd.DataFrame,
    folds: list,
    family: str,
    min_edge: float,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
) -> dict[str, Any]:
    arm: SingleBookArm = arm_spec["arm"]
    k = int(arm_spec["k"])
    mode = str(arm_spec["mode"])
    fold_rows = []
    all_pnls: list[float] = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        if mode == "double":
            sigs, stats = build_cluster_size_signals(
                ts_ms[oos],
                side,
                mean,
                close_all[oos],
                arm=arm,
                min_edge=min_edge,
                max_per_side=k,
                instrument=instrument,
                size_double_within_bars=int(arm_spec["double_bars"]),
            )
        elif k > 1:
            sigs, stats = build_cluster_concurrent_signals(
                ts_ms[oos],
                side,
                mean,
                arm=arm,
                min_edge=min_edge,
                max_per_side=k,
                cluster_bars=None,
            )
        else:
            sigs, stats = build_singlebook_signals(
                ts_ms[oos], side, mean, arm=arm, min_edge=min_edge
            )
        window = _window_for_oos(ohlcv, aligned_index, oos, arm.horizon_bars)
        bt = _bt(
            window,
            sigs,
            symbol=symbol,
            hold=arm.horizon_bars,
            k=k,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"{symbol[:3]}-{arm_spec['id']}-f{fold.fold_index}",
        )
        all_pnls.extend(bt["trade_pnls"])
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "metrics": {kk: vv for kk, vv in bt.items() if kk != "trade_pnls"},
                "n_signals": int(stats.get("n_emitted", 0)),
                "signal_stats": stats,
            }
        )
        print(
            f"  [{symbol} {arm_spec['id']}] fold {fold.fold_index}: "
            f"n={bt['n_trades']} pf={bt['profit_factor']:.3f} pnl={bt['net_pnl']:.2f}",
            flush=True,
        )
    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "bootstrap_pos_exp": _bootstrap_pos_exp(np.asarray(all_pnls)),
        "frac_folds_pf_gt_1": float(
            np.mean([r["metrics"]["profit_factor"] > 1.0 for r in fold_rows])
        )
        if fold_rows
        else float("nan"),
        "n_liquidations": int(sum(r["metrics"].get("n_liquidations", 0) for r in fold_rows)),
    }
    return {
        "arm_id": arm_spec["id"],
        "k": k,
        "arm_key": arm.key,
        "double_bars": arm_spec["double_bars"],
        "folds": fold_rows,
        "stitched": stitched,
    }


def eval_symbol(symbol: str, target: str) -> dict[str, Any]:
    print(f"\n=== TRANSFER {symbol} {target} ===", flush=True)
    ohlcv = load_ohlcv(symbol, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = _labels(ohlcv, target)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    close_all = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    try:
        touch_tf = touch_timeframe(TIMEFRAME, symbol)
        touch = load_ohlcv(symbol, touch_tf)
    except Exception:  # noqa: BLE001
        touch, touch_tf = None, None
    funding = load_funding(symbol)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(symbol)
    family = target_family(target)
    min_edge = _min_edge(target)
    arms_out = {}
    for spec in ARMS:
        arms_out[spec["id"]] = eval_arm_on_symbol(
            symbol=symbol,
            target=target,
            arm_spec=spec,
            X=X,
            yv=yv,
            close_all=close_all,
            ts_ms=ts_ms,
            aligned_index=aligned.index,
            ohlcv=ohlcv,
            folds=folds,
            family=family,
            min_edge=min_edge,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
        )
    ctrl = arms_out["control_live"]["stitched"]
    wins = {}
    for aid, a in arms_out.items():
        if aid == "control_live":
            continue
        s = a["stitched"]
        delta = (
            float(s["profit_factor"]) - float(ctrl["profit_factor"])
            if np.isfinite(s["profit_factor"]) and np.isfinite(ctrl["profit_factor"])
            else None
        )
        wins[aid] = bool(
            delta is not None
            and delta > 0
            and float(s["profit_factor"]) >= 1.20
            and int(s["n_liquidations"]) == 0
            and (not np.isfinite(s["bootstrap_pos_exp"]) or s["bootstrap_pos_exp"] >= 0.90 or s["n_trades"] < 50)
        )
        # bootstrap hard when n>=50
        if s["n_trades"] >= 50 and np.isfinite(s["bootstrap_pos_exp"]) and s["bootstrap_pos_exp"] < 0.90:
            wins[aid] = False
    return {
        "symbol": symbol,
        "target": target,
        "leverage": lev,
        "n_folds": len(folds),
        "arms": {k: {kk: vv for kk, vv in v.items() if kk != "folds"} for k, v in arms_out.items()},
        "arms_full": arms_out,
        "beats_control": wins,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skip-conformance", action="store_true")
    args = ap.parse_args()
    t0 = time.perf_counter()
    if not PREREG.is_file():
        raise SystemExit(f"missing {PREREG}")
    prereg_sha = _sha256_file(PREREG)

    conf = (
        {"status": "skipped"}
        if args.skip_conformance
        else run_conformance_check()
    )
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not from botsgeneral")

    rows = [eval_symbol(s, t) for s, t in COMBOS]
    # drop arms_full from report body for size — keep summary fold-free
    slim_rows = []
    for r in rows:
        slim_rows.append(
            {
                "symbol": r["symbol"],
                "target": r["target"],
                "leverage": r["leverage"],
                "n_folds": r["n_folds"],
                "arms": r["arms"],
                "beats_control": r["beats_control"],
            }
        )

    n_k5_win = sum(1 for r in rows if r["beats_control"].get("k5_double3h"))
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN_ID,
            "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
            "evidence_class": "frozen_geometry_symbol_transfer_fold_V2",
            "max_readiness": "RESEARCH_ONLY",
            "lockbox_used": False,
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "preregister_sha256": prereg_sha,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "conformance": conf,
            "combos": slim_rows,
            "verdict": {
                "k5_double3h_beats_on_n_symbols": n_k5_win,
                "n_symbols": len(COMBOS),
                "principal_blocker": (
                    None if n_k5_win else "k5_double3h_did_not_beat_control_on_btc_or_sol"
                ),
                "settle_candidates": [
                    f"{r['symbol']}:{r['target']}"
                    for r in rows
                    if r["beats_control"].get("k5_double3h")
                ],
                "note": "RESEARCH_ONLY. Winners need separate OUTER_SETTLE before pack freeze.",
                "no_live_deploy": True,
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "tradesim_file": str(__import__("tradesim").__file__),
        }
    )
    stamp = report["created_utc"]
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2, default=_json_default)
    (REPORT_DIR / f"{GEN_ID}_{stamp}.json").write_text(text, encoding="utf-8")
    (REPORT_DIR / f"{GEN_ID}_latest.json").write_text(text, encoding="utf-8")

    print("\n=== TRANSFER SUMMARY ===", flush=True)
    for r in slim_rows:
        for aid, a in r["arms"].items():
            s = a["stitched"]
            print(
                f"{r['symbol']:8} {aid:14} pf={s['profit_factor']} n={s['n_trades']} "
                f"boot={s.get('bootstrap_pos_exp')} beats={r['beats_control'].get(aid)}",
                flush=True,
            )
    print(f"wrote {REPORT_DIR / f'{GEN_ID}_latest.json'}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
