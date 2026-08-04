"""Is ETH concurrent lockbox (hedge×3 PF~2.4) luck or reproducible?

Diagnostic only. Compares screenshots' lockbox numbers to:
  1) Mechanical re-run identity (same inputs → same metrics)
  2) Frozen settle outer-OOS single-book baseline (already official: PF ~1.77)
  3) Walk-forward V2 outer folds, fold-trained LGBM, single vs hedge×3 concurrent
  4) Bootstrap fraction of positive expectancy on stitched concurrent OOS trades
  5) Lockbox PF vs OOS PF gap (contamination / optimism)

Does not authorize live concurrency.
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
_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

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
from llm2.models.base import Prediction  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import (  # noqa: E402
    ARTIFACTS,
    FORWARD_LOCKBOX_START,
    ROUND_TRIP_COST,
    TF_MS,
    touch_timeframe,
)
from llm2.signals.translate import predictions_to_signals  # noqa: E402
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
HORIZON = 6
TP = 0.01
SL = 0.02
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_direction"
OUT = ARTIFACTS / "reports" / "structure_v1_eth_concurrent_reproducibility.json"
SETTLE = ARTIFACTS / "reports" / "structure_v1_eth_sol_settle_20260803T161346Z.json"
LOCKBOX_REF = ARTIFACTS / "reports" / "structure_v1_eth_concurrent_lockbox.json"


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
    means = a[idx].mean(axis=1)
    return float(np.mean(means > 0))


def _touch_window(ohlcv: pd.DataFrame, symbol: str, timeframe: str) -> tuple[pd.DataFrame | None, str | None]:
    try:
        tf = touch_timeframe(timeframe, symbol)
        touch = load_ohlcv(symbol, tf)
        return touch, tf
    except Exception:  # noqa: BLE001
        return None, None


def _bt(
    window: pd.DataFrame,
    signals: list,
    *,
    max_per_side: int,
    touch: pd.DataFrame | None,
    touch_tf: str | None,
    funding_ts: np.ndarray,
    funding_rt: np.ndarray,
    lev: float,
    instrument: Any,
    label: str,
) -> dict[str, Any]:
    if max_per_side <= 1:
        sim = research_sim(max_hold_bars=HORIZON, decision_timeframe=TIMEFRAME)
    else:
        sim = research_sim_hedge(
            max_hold_bars=HORIZON,
            decision_timeframe=TIMEFRAME,
            max_positions_per_side=int(max_per_side),
            max_positions_per_symbol=int(max_per_side) * 2,
        )
    # Align touch to window
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
        strategy_meta={"name": label, "batch": "eth_conc_repro"},
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
    }


def walk_forward() -> dict[str, Any]:
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    feats = build_space(ohlcv, SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    y = build_direction_labels(ohlcv, horizon=HORIZON)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    feature_cols = [c for c in aligned.columns if c != "y"]
    X = aligned[feature_cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=HORIZON, embargo_bars=HORIZON)

    touch, touch_tf = _touch_window(ohlcv, SYMBOL, TIMEFRAME)
    funding = load_funding(SYMBOL)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    if funding.empty:
        raise RuntimeError("no funding pre-lockbox")
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = leverage_from_stop(SL)
    try:
        instrument = research_instrument(SYMBOL)
    except Exception:  # noqa: BLE001
        instrument = None

    family = target_family(TARGET)
    min_edge = DIRECTION_BAND

    fold_rows: list[dict[str, Any]] = []
    single_pnls: list[float] = []
    hedge_pnls: list[float] = []

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        signals = predictions_to_signals(
            oos_ts,
            Prediction(side=side, mean=mean),
            tp_pct=TP,
            sl_pct=SL,
            min_edge=min_edge,
        )
        oos_end = aligned.index[oos[-1]]
        oos_start = aligned.index[oos[0]]
        # pad for holds
        pad_start = ohlcv.index[max(0, ohlcv.index.searchsorted(oos_start) - 50)]
        window = ohlcv.loc[pad_start:oos_end]

        s1 = _bt(
            window,
            signals,
            max_per_side=1,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"eth-dir-single-f{fold.fold_index}",
        )
        s3 = _bt(
            window,
            signals,
            max_per_side=3,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"eth-dir-hedge3-f{fold.fold_index}",
        )
        # Only trades entering in OOS window count for stitch
        # (engine may include pad; filter by entry_ts using bundle already window-local —
        # use engine metrics for fold headline; for stitch use all trade_pnls from OOS-only
        # signals dominated window — conservative: use returned trades all)
        single_pnls.extend(s1["trade_pnls"])
        hedge_pnls.extend(s3["trade_pnls"])
        row = {
            "fold_index": int(fold.fold_index),
            "oos_start": str(oos_start),
            "oos_end": str(oos_end),
            "n_signals": len(signals),
            "single": {k: v for k, v in s1.items() if k != "trade_pnls"},
            "hedge3": {k: v for k, v in s3.items() if k != "trade_pnls"},
            "single_pf_from_trades": _pf(s1["trade_pnls"]),
            "hedge3_pf_from_trades": _pf(s3["trade_pnls"]),
        }
        fold_rows.append(row)
        print(
            f"fold {fold.fold_index}: single n={s1['n_trades']} pf={s1['profit_factor']:.3f} "
            f"hedge3 n={s3['n_trades']} pf={s3['profit_factor']:.3f}",
            flush=True,
        )

    stitched = {
        "single": {
            "n_trades": len(single_pnls),
            "net_pnl": float(np.nansum(single_pnls)),
            "profit_factor": _pf(single_pnls),
            "bootstrap_pos_exp": _bootstrap_pos_exp(np.asarray(single_pnls)),
            "frac_folds_pf_gt_1": float(
                np.mean([r["single"]["profit_factor"] > 1.0 for r in fold_rows])
            ),
            "frac_folds_pnl_gt_0": float(
                np.mean([r["single"]["net_pnl"] > 0 for r in fold_rows])
            ),
        },
        "hedge3": {
            "n_trades": len(hedge_pnls),
            "net_pnl": float(np.nansum(hedge_pnls)),
            "profit_factor": _pf(hedge_pnls),
            "bootstrap_pos_exp": _bootstrap_pos_exp(np.asarray(hedge_pnls)),
            "frac_folds_pf_gt_1": float(
                np.mean([r["hedge3"]["profit_factor"] > 1.0 for r in fold_rows])
            ),
            "frac_folds_pnl_gt_0": float(
                np.mean([r["hedge3"]["net_pnl"] > 0 for r in fold_rows])
            ),
        },
    }
    return {
        "fold_geometry": FOLD_GEOMETRY_VERSION,
        "outer_fold_ranges": OUTER_FOLD_RANGES,
        "model": "lgbm_regressor n_estimators=80",
        "target": TARGET,
        "folds": fold_rows,
        "stitched": stitched,
    }


def lockbox_mechanical_double() -> dict[str, Any]:
    """Re-sim lockbox hedge×3 twice; compare PF/n/PnL (engine determinism)."""
    import joblib

    if not (PACK / "model.joblib").is_file():
        return {"ok": False, "error": "missing pack"}

    strategy = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    blob = joblib.load(PACK / "model.joblib")
    model = blob["model"]
    cols = list(blob["feature_columns"])
    min_edge = float(strategy.get("min_edge") or DIRECTION_BAND)

    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    start_ts = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    if ohlcv.index.tz is None:
        ohlcv.index = ohlcv.index.tz_localize("UTC")
    feats = build_space(ohlcv.copy(), SPACE, symbol=SYMBOL, timeframe=TIMEFRAME)
    feats = feats.reindex(columns=cols)
    if "last_retrace_pct" in feats.columns:
        feats["last_retrace_pct"] = feats["last_retrace_pct"].fillna(0.0)
    aligned = feats.dropna()
    lock_mask = aligned.index >= start_ts
    X = aligned.loc[lock_mask].to_numpy(dtype=float)
    ts_idx = aligned.index[lock_mask]
    mean = np.asarray(model.predict(X).mean, dtype=float).reshape(-1)
    side = proxy_side(mean, "directional")
    signals = predictions_to_signals(
        index_to_ms(ts_idx),
        Prediction(side=side, mean=mean),
        tp_pct=TP,
        sl_pct=SL,
        min_edge=min_edge,
    )
    end_ts = ts_idx[-1]
    window = ohlcv.loc[(ohlcv.index >= start_ts - pd.Timedelta(days=14)) & (ohlcv.index <= end_ts)]
    touch, touch_tf = _touch_window(ohlcv, SYMBOL, TIMEFRAME)
    funding = load_funding(SYMBOL)
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = leverage_from_stop(SL)
    try:
        instrument = research_instrument(SYMBOL)
    except Exception:  # noqa: BLE001
        instrument = None

    def once(tag: str) -> dict[str, Any]:
        return _bt(
            window,
            signals,
            max_per_side=3,
            touch=touch,
            touch_tf=touch_tf,
            funding_ts=funding_ts,
            funding_rt=funding_rt,
            lev=lev,
            instrument=instrument,
            label=f"lockbox-hedge3-{tag}",
        )

    a = once("a")
    b = once("b")
    match = (
        abs(a["net_pnl"] - b["net_pnl"]) < 1e-9
        and abs(a["profit_factor"] - b["profit_factor"]) < 1e-12
        and a["n_trades"] == b["n_trades"]
    )
    pnls = np.asarray(a["trade_pnls"], dtype=float)
    return {
        "ok": True,
        "mechanical_identical": match,
        "run_a": {k: v for k, v in a.items() if k != "trade_pnls"},
        "run_b": {k: v for k, v in b.items() if k != "trade_pnls"},
        "lockbox_bootstrap_pos_exp": _bootstrap_pos_exp(pnls),
        "lockbox_n_trades": int(a["n_trades"]),
        "lockbox_pf": float(a["profit_factor"]),
        "lockbox_net_pnl": float(a["net_pnl"]),
        "mdd_wallet_note": (
            "Reported max drawdown ~0.02% of 10k wallet is min-exchange sizing artifact, "
            "not deployment risk capacity."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-walkforward", action="store_true")
    ap.add_argument("--skip-lockbox", action="store_true")
    args = ap.parse_args()

    stamp = run_conformance_check(quiet=True)
    if not stamp.get("passed"):
        print("conformance not green")
        return 1

    t0 = time.time()
    settle_eth_dir = None
    if SETTLE.is_file():
        s = json.loads(SETTLE.read_text(encoding="utf-8"))
        for row in s.get("combos") or []:
            if row.get("symbol") == "ETHUSDT" and row.get("target") == "direction":
                settle_eth_dir = row
                break

    lockbox_prior = None
    if LOCKBOX_REF.is_file():
        lockbox_prior = json.loads(LOCKBOX_REF.read_text(encoding="utf-8"))

    mech = None if args.skip_lockbox else lockbox_mechanical_double()
    wf = None if args.skip_walkforward else walk_forward()

    # Interpret
    oos_pf = float((wf or {}).get("stitched", {}).get("hedge3", {}).get("profit_factor") or float("nan"))
    lock_pf = float((mech or {}).get("lockbox_pf") or float("nan"))
    settle_pf = float((settle_eth_dir or {}).get("pooled_pf") or float("nan"))
    oos_single = float((wf or {}).get("stitched", {}).get("single", {}).get("profit_factor") or float("nan"))
    boot_oos = float((wf or {}).get("stitched", {}).get("hedge3", {}).get("bootstrap_pos_exp") or float("nan"))
    folds_pos = float((wf or {}).get("stitched", {}).get("hedge3", {}).get("frac_folds_pnl_gt_0") or float("nan"))

    if mech and mech.get("mechanical_identical") and np.isfinite(oos_pf) and oos_pf >= 1.2 and (
        not np.isfinite(boot_oos) or boot_oos >= 0.90
    ) and folds_pos >= 0.8:
        verdict = "MECHANICALLY_REPRODUCIBLE_AND_POSITIVE_ON_OUTER_OOS"
        luck = "unlikely_pure_luck_on_nested_oos_but_lockbox_still_contaminated"
    elif mech and mech.get("mechanical_identical") and np.isfinite(oos_pf) and oos_pf > 1.0:
        verdict = "MECHANICALLY_REPRODUCIBLE_WEAK_OOS"
        luck = "partial — engine deterministic; edge weaker/fragile out of lockbox"
    elif mech and mech.get("mechanical_identical"):
        verdict = "MECHANICALLY_REPRODUCIBLE_OOS_NOT_SUPPORTIVE"
        luck = "lockbox chart numbers are optimistic relative to outer OOS — treat as luck/selection"
    else:
        verdict = "INCONCLUSIVE"
        luck = "insufficient evidence"

    lockbox_gap = None
    if np.isfinite(lock_pf) and np.isfinite(oos_pf):
        lockbox_gap = float(lock_pf - oos_pf)

    payload = {
        "stamped_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_class": "DIAGNOSTIC_REPRO_AUDIT",
        "readiness": "RESEARCH_ONLY",
        "screenshots_claim": {
            "label": "structure_v1 direction LOCKBOX concurrent hedge x 3",
            "reported_pf": 2.44,
            "reported_n": 1155,
            "reported_pnl": 64.73,
            "prior_json": (
                {
                    "concurrent_net_pnl": (lockbox_prior or {}).get("concurrent", {}).get("net_pnl"),
                    "concurrent_pf": (lockbox_prior or {}).get("concurrent", {}).get("profit_factor"),
                    "n_trades": (lockbox_prior or {}).get("concurrent", {}).get("n_trades"),
                }
                if lockbox_prior
                else None
            ),
        },
        "official_settle_single_book": {
            "source": str(SETTLE.name) if SETTLE.is_file() else None,
            "ETH_direction_pooled_pf": settle_pf,
            "pooled_trades": (settle_eth_dir or {}).get("pooled_trades"),
            "overall": (settle_eth_dir or {}).get("overall"),
            "note": "This is the quotable promotion proxy for single-book ETH direction — not lockbox concurrent.",
        },
        "mechanical_lockbox": mech,
        "walk_forward_pre_lockbox": wf,
        "comparison": {
            "lockbox_pf": lock_pf,
            "stitched_oos_hedge3_pf": oos_pf,
            "stitched_oos_single_pf": oos_single,
            "settle_single_pf": settle_pf,
            "lockbox_minus_oos_hedge3_pf": lockbox_gap,
            "bootstrap_pos_exp_oos_hedge3": boot_oos,
            "frac_oos_folds_pnl_positive_hedge3": folds_pos,
        },
        "verdict": verdict,
        "luck_assessment": luck,
        "caveats": [
            "Lockbox May→Aug was opened (D-035): LOCKBOX_OPENED_CONTAMINATED — cannot be first-look gate.",
            "Min-exchange size + 10k wallet makes wallet MDD appear ~0; not scale risk evidence.",
            "Screenshot PF ~2.4 is a single forward path after model freeze peek — not multi-fold validation of concurrency.",
            "Concurrent OOS here is execution-mode stress on fold-trained LGBM; live still max-1 book per symbol.",
            "If lockbox PF >> stitched OOS concurrent PF, treat screenshot edge as optimistic.",
        ],
        "elapsed_sec": time.time() - t0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, default=_json_default) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": verdict, "luck": luck, "comparison": payload["comparison"]}, indent=2), flush=True)
    print(f"wrote {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
