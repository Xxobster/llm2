"""Gen-1 single-book ETH direction: clarity × hold × TP grid (SL fixed 2%).

Preregister: configs/preregister/structure_v1_eth_singlebook_clarity_hold_tp_001.yaml

Protocol:
  1) Conformance gate
  2) Inner-select ONE arm on outer-fold-0 train (3 inner folds) — never on OOS/lockbox
  3) Freeze arm; walk-forward all V2 outer folds; stitch OOS trades
  4) Always report control (none|hold6|tp1%) on the same outer stitch

mean_strength gates PRIMARY entries (single-book). Not multitrade add-on logic.
Lockbox (May-2026→) is not opened for selection or ranking.
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
    Signal,
    research_instrument,
    research_margin,
    research_sizing,
    research_sim,
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
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    TF_MS,
    touch_timeframe,
)
from llm2.signals.singlebook_clarity import (  # noqa: E402
    SingleBookArm,
    arm_grid,
    build_singlebook_signals,
)
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
    make_inner_folds,
)

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
LABEL_HORIZON = 6
SL = 0.02
MIN_EDGE = DIRECTION_BAND
CLARITY = ("none", "mean_strength")
HOLDS = (6, 12)
TPS = (0.01, 0.015, 0.02618)
CONTROL = {"clarity": "none", "horizon_bars": 6, "tp_pct": 0.01, "sl_pct": SL}
PREREG = (
    _ROOT
    / "configs"
    / "preregister"
    / "structure_v1_eth_singlebook_clarity_hold_tp_001.yaml"
)
REPORT_DIR = ARTIFACTS / "reports"
GEN_ID = "structure_v1_eth_singlebook_clarity_hold_tp_001"


def all_arms() -> list[SingleBookArm]:
    return arm_grid(clarity=CLARITY, holds=HOLDS, tps=TPS, sl_pct=SL)  # type: ignore[arg-type]


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


def prereg_sha256() -> str:
    raw = PREREG.read_bytes()
    return hashlib.sha256(raw).hexdigest()


def _touch_window(ohlcv: pd.DataFrame, symbol: str, timeframe: str) -> tuple[pd.DataFrame | None, str | None]:
    try:
        tf = touch_timeframe(timeframe, symbol)
        return load_ohlcv(symbol, tf), tf
    except Exception:  # noqa: BLE001
        return None, None


def _bt(
    window: pd.DataFrame,
    signals: list[Signal],
    *,
    hold: int,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
    label: str,
) -> dict[str, Any]:
    sim = research_sim(max_hold_bars=int(hold), decision_timeframe=TIMEFRAME)
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
        strategy_meta={"name": label, "batch": GEN_ID},
        plot=False,
        print_headline=False,
        store_path=None,
    )
    m = bundle.metrics
    trades = list(bundle.result.trades)
    pnls = [float(getattr(t, "realized_pnl", 0.0) or 0.0) for t in trades]
    return {
        "n_trades": int(m.n_trades),
        "net_pnl": float(m.net_pnl),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "trade_pnls": pnls,
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
    }


def _window_for_oos(
    ohlcv: pd.DataFrame,
    aligned_index: pd.DatetimeIndex,
    oos: np.ndarray,
    hold: int,
) -> pd.DataFrame:
    oos_start = aligned_index[oos[0]]
    oos_end = aligned_index[oos[-1]]
    pad = max(50, int(hold) * 4)
    pos = int(ohlcv.index.searchsorted(oos_start))
    pad_start = ohlcv.index[max(0, pos - pad)]
    return ohlcv.loc[pad_start:oos_end]


def _score_arm_inner(
    *,
    X: np.ndarray,
    yv: np.ndarray,
    ts_ms: np.ndarray,
    aligned_index: pd.DatetimeIndex,
    ohlcv: pd.DataFrame,
    train_indices: np.ndarray,
    arm: SingleBookArm,
    family: str,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
) -> dict[str, Any]:
    """Score one arm on inner folds of outer-fold-0 train only."""
    inners = make_inner_folds(
        train_indices,
        n_folds=3,
        purge_bars=LABEL_HORIZON,
        embargo_bars=LABEL_HORIZON,
    )
    pfs: list[float] = []
    n_trades: list[int] = []
    for fi, inner in enumerate(inners):
        # FoldSpec offsets are into the train window length (see llm2.hunt.runner)
        tr_rel = np.arange(0, int(inner.train_end), dtype=np.int64)
        va_rel = np.arange(int(inner.val_start), int(inner.val_end), dtype=np.int64)
        tr = train_indices[tr_rel]
        va = train_indices[va_rel]
        if tr.size < 200 or va.size < 50:
            continue
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[va])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        signals, stats = build_singlebook_signals(
            ts_ms[va], side, mean, arm=arm, min_edge=MIN_EDGE
        )
        window = _window_for_oos(ohlcv, aligned_index, va, arm.horizon_bars)
        bt = _bt(
            window,
            signals,
            hold=arm.horizon_bars,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"inner-f0-{fi}-{arm.key}",
        )
        pfs.append(float(bt["profit_factor"]))
        n_trades.append(int(bt["n_trades"]))
    mean_pf = float(np.nanmean(pfs)) if pfs else float("nan")
    mean_n = float(np.nanmean(n_trades)) if n_trades else 0.0
    return {
        "arm": arm.key,
        "clarity": arm.clarity,
        "horizon_bars": arm.horizon_bars,
        "tp_pct": arm.tp_pct,
        "n_inner_scored": len(pfs),
        "mean_inner_pf": mean_pf,
        "mean_inner_n_trades": mean_n,
        "inner_pfs": pfs,
        "inner_n_trades": n_trades,
    }


def _select_arm(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Tie-break: higher PF, then more trades, then lower tp, shorter hold, clarity=none."""

    def sort_key(r: dict[str, Any]) -> tuple:
        pf = r["mean_inner_pf"]
        pf_s = -1e9 if not np.isfinite(pf) else float(pf)
        return (
            pf_s,
            float(r["mean_inner_n_trades"]),
            -float(r["tp_pct"]),
            -int(r["horizon_bars"]),
            0 if r["clarity"] == "none" else -1,
        )

    ranked = sorted(rows, key=sort_key, reverse=True)
    winner = ranked[0]
    return {"selected": winner, "ranked": ranked}


def walk_outer(
    *,
    X: np.ndarray,
    yv: np.ndarray,
    ts_ms: np.ndarray,
    aligned_index: pd.DatetimeIndex,
    ohlcv: pd.DataFrame,
    folds: list,
    arm: SingleBookArm,
    family: str,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
    tag: str,
) -> dict[str, Any]:
    fold_rows: list[dict[str, Any]] = []
    all_pnls: list[float] = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        signals, stats = build_singlebook_signals(
            ts_ms[oos], side, mean, arm=arm, min_edge=MIN_EDGE
        )
        window = _window_for_oos(ohlcv, aligned_index, oos, arm.horizon_bars)
        bt = _bt(
            window,
            signals,
            hold=arm.horizon_bars,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"{tag}-f{fold.fold_index}",
        )
        all_pnls.extend(bt["trade_pnls"])
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "oos_start": str(aligned_index[oos[0]]),
                "oos_end": str(aligned_index[oos[-1]]),
                "n_signals": int(stats["n_emitted"]),
                "signal_stats": stats,
                "metrics": {k: v for k, v in bt.items() if k != "trade_pnls"},
                "pf_from_trades": _pf(bt["trade_pnls"]),
            }
        )
        print(
            f"  [{tag}] fold {fold.fold_index}: n={bt['n_trades']} "
            f"pf={bt['profit_factor']:.3f} pnl={bt['net_pnl']:.2f}",
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
        "frac_folds_pnl_gt_0": float(np.mean([r["metrics"]["net_pnl"] > 0 for r in fold_rows]))
        if fold_rows
        else float("nan"),
        "n_liquidations": int(sum(r["metrics"].get("n_liquidations", 0) for r in fold_rows)),
    }
    return {"arm": arm.key, "folds": fold_rows, "stitched": stitched, "trade_pnls": all_pnls}


def run() -> dict[str, Any]:
    t0 = time.perf_counter()
    conf = run_conformance_check()
    conf_state = conf.get("state") or conf.get("status") or conf
    print(f"conformance: {conf_state}", flush=True)

    sha = prereg_sha256()
    (PREREG.with_suffix(".sha256")).write_text(sha + "\n", encoding="utf-8")

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    if not folds:
        raise RuntimeError("no outer folds")

    touch, touch_tf = _touch_window(ohlcv, SYMBOL, TIMEFRAME)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    if funding.empty:
        raise RuntimeError("no funding pre-lockbox")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    try:
        instrument = research_instrument(SYMBOL)
    except Exception:  # noqa: BLE001
        instrument = None

    family = target_family(TARGET)
    arms = all_arms()
    assert len(arms) == 12

    # --- Inner selection on outer fold 0 train only ---
    f0 = folds[0]
    print(f"inner selection on outer fold {f0.fold_index} train ({len(f0.train_indices)} rows)", flush=True)
    inner_rows: list[dict[str, Any]] = []
    for arm in arms:
        row = _score_arm_inner(
            X=X,
            yv=yv,
            ts_ms=ts_ms,
            aligned_index=aligned.index,
            ohlcv=ohlcv,
            train_indices=f0.train_indices,
            arm=arm,
            family=family,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
        )
        inner_rows.append(row)
        print(
            f"  inner {arm.key}: mean_pf={row['mean_inner_pf']:.3f} "
            f"mean_n={row['mean_inner_n_trades']:.1f}",
            flush=True,
        )

    selection = _select_arm(inner_rows)
    sel = selection["selected"]
    selected_arm = SingleBookArm(
        clarity=sel["clarity"],  # type: ignore[arg-type]
        horizon_bars=int(sel["horizon_bars"]),
        tp_pct=float(sel["tp_pct"]),
        sl_pct=SL,
    )
    control_arm = SingleBookArm(
        clarity=CONTROL["clarity"],  # type: ignore[arg-type]
        horizon_bars=int(CONTROL["horizon_bars"]),
        tp_pct=float(CONTROL["tp_pct"]),
        sl_pct=SL,
    )
    print(f"FROZEN selected arm: {selected_arm.key}", flush=True)

    # --- Outer stitch (selected + control) ---
    print("outer walk-forward: selected", flush=True)
    selected_outer = walk_outer(
        X=X,
        yv=yv,
        ts_ms=ts_ms,
        aligned_index=aligned.index,
        ohlcv=ohlcv,
        folds=folds,
        arm=selected_arm,
        family=family,
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        lev=lev,
        instrument=instrument,
        tag="selected",
    )
    print("outer walk-forward: control", flush=True)
    control_outer = walk_outer(
        X=X,
        yv=yv,
        ts_ms=ts_ms,
        aligned_index=aligned.index,
        ohlcv=ohlcv,
        folds=folds,
        arm=control_arm,
        family=family,
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        lev=lev,
        instrument=instrument,
        tag="control",
    )

    sel_s = selected_outer["stitched"]
    ctl_s = control_outer["stitched"]
    beats_control = (
        np.isfinite(sel_s["profit_factor"])
        and np.isfinite(ctl_s["profit_factor"])
        and float(sel_s["profit_factor"]) > float(ctl_s["profit_factor"])
    )
    pf_gate = bool(np.isfinite(sel_s["profit_factor"]) and float(sel_s["profit_factor"]) >= 1.20)
    boot_ok = bool(
        (sel_s["n_trades"] < 50)
        or (
            np.isfinite(sel_s["bootstrap_pos_exp"])
            and float(sel_s["bootstrap_pos_exp"]) >= 0.90
        )
    )
    no_liq = int(sel_s["n_liquidations"]) == 0
    success = bool(beats_control and pf_gate and boot_ok and no_liq)

    # Drop bulky trade lists from nested payload; keep stitched summaries
    selected_outer_out = {k: v for k, v in selected_outer.items() if k != "trade_pnls"}
    control_outer_out = {k: v for k, v in control_outer.items() if k != "trade_pnls"}

    report = {
        "generation_id": GEN_ID,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "preregister_path": str(PREREG.relative_to(_ROOT)).replace("\\", "/"),
        "preregister_sha256": sha,
        "evidence_class": "fold_V2_stitched_outer_OOS_execution_grid",
        "lockbox_used": False,
        "conformance": conf,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "symbol": SYMBOL,
        "timeframe": TIMEFRAME,
        "target": TARGET,
        "sl_pct": SL,
        "leverage": lev,
        "candidate_space": {
            "clarity": list(CLARITY),
            "horizon_bars": list(HOLDS),
            "tp_pct": list(TPS),
            "n_arms": len(arms),
        },
        "inner_selection": {
            "on": "outer_fold_0_train",
            "rows": inner_rows,
            "selected_arm": selected_arm.key,
            "selected_detail": sel,
        },
        "control_arm": control_arm.key,
        "selected_outer": selected_outer_out,
        "control_outer": control_outer_out,
        "verdict": {
            "success": success,
            "beats_control_pf": beats_control,
            "selected_pf_ge_1_20": pf_gate,
            "bootstrap_ok": boot_ok,
            "no_liquidation": no_liq,
            "selected_stitched_pf": sel_s["profit_factor"],
            "control_stitched_pf": ctl_s["profit_factor"],
            "delta_pf": (
                float(sel_s["profit_factor"]) - float(ctl_s["profit_factor"])
                if np.isfinite(sel_s["profit_factor"]) and np.isfinite(ctl_s["profit_factor"])
                else None
            ),
            "max_readiness": "RESEARCH_ONLY",
            "principal_blocker": (
                None
                if success
                else (
                    "selected_arm_did_not_beat_control_and_gates"
                    if not beats_control
                    else "gates_failed_after_beating_control"
                )
            ),
            "caveat": "min-exchange equity / MDD is not scale evidence",
        },
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "tradesim_file": str(__import__("tradesim").__file__),
    }
    if "botsgeneral" not in str(report["tradesim_file"]).lower():
        raise RuntimeError(f"tradesim not from botsgeneral: {report['tradesim_file']}")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Report JSON path (default: artifacts/reports/..._TIMESTAMP.json)",
    )
    args = parser.parse_args()
    report = run()
    stamp = report["created_utc"]
    out = args.out or (REPORT_DIR / f"{GEN_ID}_{stamp}.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2, default=_json_default)
    out.write_text(text, encoding="utf-8")
    latest = REPORT_DIR / f"{GEN_ID}_latest.json"
    latest.write_text(text, encoding="utf-8")

    v = report["verdict"]
    print("\n=== VERDICT ===", flush=True)
    print(f"selected: {report['inner_selection']['selected_arm']}", flush=True)
    print(
        f"selected PF={v['selected_stitched_pf']:.4f}  control PF={v['control_stitched_pf']:.4f}  "
        f"delta={v['delta_pf']}",
        flush=True,
    )
    print(f"success={v['success']}  readiness={v['max_readiness']}  blocker={v['principal_blocker']}", flush=True)
    print(f"wrote {out}", flush=True)
    print(f"wrote {latest}", flush=True)
    return 0 if v["success"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
