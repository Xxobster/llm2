"""Transfer-test ETH-frozen single-book arm on BTCUSDT + SOLUSDT (no re-search).

Frozen arm (from structure_v1_eth_singlebook_clarity_hold_tp_001):
  mean_strength | hold 12 | tp 1% | sl 2%

Control (live baseline geometry):
  none | hold 6 | tp 1% | sl 2%

Protocol: fold V2 outer stitch only; arm already selected on ETH — do not re-rank.
Lockbox not opened. RESEARCH_ONLY.
"""

from __future__ import annotations

import argparse
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
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
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
FROZEN = SingleBookArm(clarity="mean_strength", horizon_bars=12, tp_pct=0.01, sl_pct=SL)
CONTROL = SingleBookArm(clarity="none", horizon_bars=6, tp_pct=0.01, sl_pct=SL)
# Live-matching targets + direction parity with ETH gen-1
COMBOS = (
    ("BTCUSDT", "direction"),
    ("BTCUSDT", "fwd_return"),
    ("SOLUSDT", "direction"),
    ("SOLUSDT", "fwd_return"),
)
ETH_REF = ARTIFACTS / "reports" / "structure_v1_eth_singlebook_clarity_hold_tp_001_latest.json"
GEN_ID = "structure_v1_frozen_arm_btc_sol_transfer_001"
REPORT_DIR = ARTIFACTS / "reports"
PREREG_SHA = "eedcafe3fdd0b0ff545c4f252f0deae3cf93cbed5e3b06299fe3aa354bb5eafa"


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


def _min_edge(target: str) -> float:
    fam = target_family(target)
    if fam == "directional":
        return float(DIRECTION_BAND)
    return float(ROUND_TRIP_COST)


def _labels(ohlcv: pd.DataFrame, target: str) -> pd.Series:
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=LABEL_HORIZON)["fwd_return"]
    raise ValueError(target)


def _touch_window(ohlcv: pd.DataFrame, symbol: str) -> tuple[pd.DataFrame | None, str | None]:
    try:
        tf = touch_timeframe(TIMEFRAME, symbol)
        return load_ohlcv(symbol, tf), tf
    except Exception:  # noqa: BLE001
        return None, None


def _bt(
    window: pd.DataFrame,
    signals: list[Signal],
    *,
    symbol: str,
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


def walk_outer(
    *,
    symbol: str,
    X: np.ndarray,
    yv: np.ndarray,
    ts_ms: np.ndarray,
    aligned_index: pd.DatetimeIndex,
    ohlcv: pd.DataFrame,
    folds: list,
    arm: SingleBookArm,
    family: str,
    min_edge: float,
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
            ts_ms[oos], side, mean, arm=arm, min_edge=min_edge
        )
        window = _window_for_oos(ohlcv, aligned_index, oos, arm.horizon_bars)
        bt = _bt(
            window,
            signals,
            symbol=symbol,
            hold=arm.horizon_bars,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"{symbol[:3]}-{tag}-f{fold.fold_index}",
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
            f"  [{symbol} {tag}] fold {fold.fold_index}: n={bt['n_trades']} "
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
    return {"arm": arm.key, "folds": fold_rows, "stitched": stitched}


def eval_combo(symbol: str, target: str) -> dict[str, Any]:
    print(f"\n=== {symbol} {target} ===", flush=True)
    ohlcv = load_ohlcv(symbol, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = _labels(ohlcv, target)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    if not folds:
        raise RuntimeError(f"no outer folds for {symbol}")

    touch, touch_tf = _touch_window(ohlcv, symbol)
    funding = load_funding(symbol)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    if funding.empty:
        raise RuntimeError(f"no funding pre-lockbox for {symbol}")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    try:
        instrument = research_instrument(symbol)
    except Exception:  # noqa: BLE001
        instrument = None

    family = target_family(target)
    min_edge = _min_edge(target)

    frozen_outer = walk_outer(
        symbol=symbol,
        X=X,
        yv=yv,
        ts_ms=ts_ms,
        aligned_index=aligned.index,
        ohlcv=ohlcv,
        folds=folds,
        arm=FROZEN,
        family=family,
        min_edge=min_edge,
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        lev=lev,
        instrument=instrument,
        tag="frozen",
    )
    control_outer = walk_outer(
        symbol=symbol,
        X=X,
        yv=yv,
        ts_ms=ts_ms,
        aligned_index=aligned.index,
        ohlcv=ohlcv,
        folds=folds,
        arm=CONTROL,
        family=family,
        min_edge=min_edge,
        touch=touch,
        touch_tf=touch_tf,
        funding_ts=funding_ts,
        funding_rt=funding_rt,
        lev=lev,
        instrument=instrument,
        tag="control",
    )
    fs = frozen_outer["stitched"]
    cs = control_outer["stitched"]
    delta = (
        float(fs["profit_factor"]) - float(cs["profit_factor"])
        if np.isfinite(fs["profit_factor"]) and np.isfinite(cs["profit_factor"])
        else None
    )
    beats = bool(
        delta is not None and delta > 0 and float(fs["profit_factor"]) >= 1.20 and int(fs["n_liquidations"]) == 0
    )
    return {
        "symbol": symbol,
        "target": target,
        "min_edge": min_edge,
        "leverage": lev,
        "frozen_arm": FROZEN.key,
        "control_arm": CONTROL.key,
        "frozen": frozen_outer,
        "control": control_outer,
        "delta_pf": delta,
        "beats_control_and_pf_gate": beats,
        "n_folds": len(folds),
    }


def _eth_ref_row() -> dict[str, Any] | None:
    if not ETH_REF.is_file():
        return None
    r = json.loads(ETH_REF.read_text(encoding="utf-8"))
    v = r.get("verdict") or {}
    return {
        "symbol": "ETHUSDT",
        "target": "direction",
        "source": str(ETH_REF.name),
        "frozen_arm": r.get("inner_selection", {}).get("selected_arm"),
        "control_arm": r.get("control_arm"),
        "frozen_stitched_pf": v.get("selected_stitched_pf"),
        "control_stitched_pf": v.get("control_stitched_pf"),
        "delta_pf": v.get("delta_pf"),
        "frozen_n_trades": (r.get("selected_outer") or {}).get("stitched", {}).get("n_trades"),
        "control_n_trades": (r.get("control_outer") or {}).get("stitched", {}).get("n_trades"),
        "note": "ETH gen-1 selection source; not re-run here",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-conformance", action="store_true")
    args = parser.parse_args()
    t0 = time.perf_counter()

    if args.skip_conformance:
        conf: dict[str, Any] = {"status": "skipped", "passed": None}
    else:
        conf = run_conformance_check()
        print(f"conformance: {conf.get('status') or conf}", flush=True)
        if conf.get("passed") is False:
            raise RuntimeError("conformance failed")

    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not from botsgeneral")

    rows = []
    for sym, tgt in COMBOS:
        rows.append(eval_combo(sym, tgt))

    eth = _eth_ref_row()
    summary = []
    if eth:
        summary.append(
            {
                "symbol": "ETHUSDT",
                "target": "direction",
                "frozen_pf": eth["frozen_stitched_pf"],
                "control_pf": eth["control_stitched_pf"],
                "delta_pf": eth["delta_pf"],
                "frozen_n": eth["frozen_n_trades"],
                "control_n": eth["control_n_trades"],
                "beats": True,
                "source": "eth_gen1_ref",
            }
        )
    for row in rows:
        fs = row["frozen"]["stitched"]
        cs = row["control"]["stitched"]
        summary.append(
            {
                "symbol": row["symbol"],
                "target": row["target"],
                "frozen_pf": fs["profit_factor"],
                "control_pf": cs["profit_factor"],
                "delta_pf": row["delta_pf"],
                "frozen_n": fs["n_trades"],
                "control_n": cs["n_trades"],
                "beats": row["beats_control_and_pf_gate"],
                "bootstrap_pos_exp": fs["bootstrap_pos_exp"],
                "frac_folds_pf_gt_1": fs["frac_folds_pf_gt_1"],
                "n_liquidations": fs["n_liquidations"],
                "source": "transfer_eval",
            }
        )

    n_liveish = sum(
        1
        for s in summary
        if s["source"] == "transfer_eval"
        and (
            (s["symbol"] == "BTCUSDT" and s["target"] == "fwd_return")
            or (s["symbol"] == "SOLUSDT" and s["target"] == "direction")
        )
        and s["beats"]
    )
    report = {
        "generation_id": GEN_ID,
        "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "evidence_class": "frozen_arm_symbol_transfer_fold_V2_stitch",
        "lockbox_used": False,
        "selection": "FROZEN_from_ETH_gen1_no_rerank",
        "frozen_arm": FROZEN.key,
        "control_arm": CONTROL.key,
        "eth_preregister_sha256_at_run": PREREG_SHA,
        "conformance": conf,
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "eth_reference": eth,
        "combos": rows,
        "summary": summary,
        "verdict": {
            "max_readiness": "RESEARCH_ONLY",
            "live_matching_beats": n_liveish,
            "live_matching_note": (
                "BTC live pack target=fwd_return; SOL live pack target=direction. "
                "Count of those two that beat control with PF>=1.20 and no liq."
            ),
            "principal_blocker": (
                None
                if n_liveish == 2
                else "frozen_arm_does_not_transfer_to_all_live_matching_symbols"
            ),
            "caveat": "min-exchange equity / MDD is not scale evidence; not a V2.1 full-gate settle",
            "no_live_deploy": True,
        },
        "elapsed_sec": round(time.perf_counter() - t0, 1),
        "tradesim_file": str(__import__("tradesim").__file__),
    }

    stamp = report["created_utc"]
    out = REPORT_DIR / f"{GEN_ID}_{stamp}.json"
    latest = REPORT_DIR / f"{GEN_ID}_latest.json"
    text = json.dumps(report, indent=2, default=_json_default)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    print("\n=== SUMMARY ===", flush=True)
    for s in summary:
        print(
            f"{s['symbol']:8} {s['target']:11} frozen_pf={s['frozen_pf']} "
            f"control_pf={s['control_pf']} delta={s['delta_pf']} beats={s['beats']}",
            flush=True,
        )
    print(f"wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
