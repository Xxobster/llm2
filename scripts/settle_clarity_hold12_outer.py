"""Full V2.1 outer settle of frozen single-book arm mean_strength|hold12|tp1%.

Hard end exclusive: FORWARD_LOCKBOX_START. No lockbox. No re-search.
Live-matching targets: BTCUSDT fwd_return, ETHUSDT direction, SOLUSDT direction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
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
from llm2.gates.evidence import (  # noqa: E402
    leverage_from_stop,
    mdd_fraction_from_daily_returns,
    peak_margin_utilization,
    research_costs_baseline,
    research_costs_moderate_stress,
)
from llm2.gates.v21 import evaluate_v21_gates, format_gates_table  # noqa: E402
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
GEN_ID = "structure_v1_clarity_hold12_outer_settle_001"
PREREG = _ROOT / "configs" / "preregister" / f"{GEN_ID}.yaml"
REPORT_DIR = ARTIFACTS / "reports"
PACKS = ARTIFACTS / "live_packs"

# Live-matching product targets only for promotion settle.
COMBOS = (
    ("BTCUSDT", "fwd_return", "structure_v1_lgbm"),
    ("ETHUSDT", "direction", "structure_v1_ethusdt_direction"),
    ("SOLUSDT", "direction", "structure_v1_solusdt_direction"),
)
N_TRIALS_DSR = 12  # parent gen-1 candidate count


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
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


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


def _min_edge(target: str) -> float:
    return float(DIRECTION_BAND) if target_family(target) == "directional" else float(ROUND_TRIP_COST)


def _labels(ohlcv: pd.DataFrame, target: str) -> pd.Series:
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=LABEL_HORIZON)["fwd_return"]
    raise ValueError(target)


def _touch_for(symbol: str) -> tuple[pd.DataFrame | None, str | None]:
    try:
        tf = touch_timeframe(TIMEFRAME, symbol)
        return load_ohlcv(symbol, tf), tf
    except Exception:  # noqa: BLE001
        return None, None


def _window_for_oos(
    ohlcv: pd.DataFrame, aligned_index: pd.DatetimeIndex, oos: np.ndarray, hold: int
) -> pd.DataFrame:
    oos_start = aligned_index[oos[0]]
    oos_end = aligned_index[oos[-1]]
    pad = max(50, int(hold) * 4)
    pos = int(ohlcv.index.searchsorted(oos_start))
    pad_start = ohlcv.index[max(0, pos - pad)]
    return ohlcv.loc[pad_start:oos_end]


def _backtest(
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
    costs: Any,
) -> dict[str, Any]:
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
        costs=costs,
        margin=research_margin(leverage=lev),
        sizing=research_sizing(),
        sim=research_sim(max_hold_bars=int(hold), decision_timeframe=TIMEFRAME),
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
    daily_rets: list[float] = []
    de = getattr(bundle.result, "daily_equity", None)
    if de is not None:
        if isinstance(de, pd.DataFrame) and "equity" in de.columns:
            eq = de["equity"].to_numpy(dtype=float)
        else:
            eq = np.asarray(de, dtype=float).reshape(-1)
        if len(eq) > 1:
            daily_rets = (np.diff(eq) / np.maximum(eq[:-1], 1e-9)).tolist()
    margin_u = peak_margin_utilization(
        trades,
        equity=getattr(bundle.result, "equity", None),
        starting_equity=float(m.starting_equity),
    )
    return {
        "n_trades": int(m.n_trades),
        "net_pnl": float(m.net_pnl),
        "profit_factor": float(m.profit_factor),
        "win_rate": float(getattr(m, "win_rate", float("nan"))),
        "total_fees": float(getattr(m, "total_fees", float("nan"))),
        "trade_pnls": pnls,
        "daily_returns": daily_rets,
        "margin_util": float(margin_u),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
        "max_drawdown_pct": float(getattr(m, "max_drawdown_pct", float("nan"))),
        "starting_equity": float(m.starting_equity),
        "ending_equity": float(m.ending_equity),
    }


def walk_arm(
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
    costs: Any,
) -> dict[str, Any]:
    fold_rows: list[dict[str, Any]] = []
    all_pnls: list[float] = []
    all_daily: list[float] = []
    peak_margin = 0.0
    any_liq = False
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
        bt = _backtest(
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
            costs=costs,
        )
        all_pnls.extend(bt["trade_pnls"])
        all_daily.extend(bt["daily_returns"])
        peak_margin = max(peak_margin, float(bt["margin_util"]))
        if int(bt["n_liquidations"]) > 0:
            any_liq = True
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "oos_start": str(aligned_index[oos[0]]),
                "oos_end": str(aligned_index[oos[-1]]),
                "n_signals": int(stats["n_emitted"]),
                "metrics": {k: v for k, v in bt.items() if k not in {"trade_pnls", "daily_returns"}},
                "pf_from_trades": _pf(bt["trade_pnls"]),
            }
        )
        print(
            f"  [{symbol} {tag}] fold {fold.fold_index}: n={bt['n_trades']} "
            f"pf={bt['profit_factor']:.3f} pnl={bt['net_pnl']:.2f}",
            flush=True,
        )
    daily_arr = np.asarray(all_daily, dtype=float) if all_daily else None
    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "n_liquidations": int(sum(r["metrics"].get("n_liquidations", 0) for r in fold_rows)),
        "peak_margin_util": float(peak_margin),
        "any_liquidation": bool(any_liq),
        "daily_n": int(daily_arr.size) if daily_arr is not None else 0,
    }
    return {
        "arm": arm.key,
        "folds": fold_rows,
        "stitched": stitched,
        "all_trade_pnls": all_pnls,
        "daily_returns": all_daily,
        "peak_margin": float(peak_margin),
        "any_liquidation": bool(any_liq),
    }


def _gates_for(outer: dict[str, Any], stress: dict[str, Any]) -> dict[str, Any]:
    folds = outer["folds"]
    fold_pnls = [float(r["metrics"]["net_pnl"]) for r in folds]
    fold_pfs = [float(r["metrics"]["profit_factor"]) for r in folds]
    fold_trades = [int(r["metrics"]["n_trades"]) for r in folds]
    daily = np.asarray(outer["daily_returns"], dtype=float) if outer["daily_returns"] else None
    stress_pnls = stress["all_trade_pnls"]
    stress_fold_pnls = [float(r["metrics"]["net_pnl"]) for r in stress["folds"]]
    stress_daily = (
        np.asarray(stress["daily_returns"], dtype=float) if stress["daily_returns"] else None
    )
    return evaluate_v21_gates(
        fold_pnls=fold_pnls,
        fold_pfs=fold_pfs,
        fold_trades=fold_trades,
        daily_returns=daily,
        pooled_pf=float(outer["stitched"]["profit_factor"]),
        pooled_trades=int(outer["stitched"]["n_trades"]),
        metric_kind="profit_factor",
        n_trials=N_TRIALS_DSR,
        stress_pnl=float(np.nansum(stress_fold_pnls)),
        stress_pf=_pf(stress_pnls),
        baseline_mdd=mdd_fraction_from_daily_returns(daily) if daily is not None and daily.size else None,
        stress_mdd=mdd_fraction_from_daily_returns(stress_daily)
        if stress_daily is not None and stress_daily.size
        else None,
        margin_util=float(outer["peak_margin"]),
        candidate_matrix=None,  # single frozen arm — PBO UNAVAILABLE
        liquidation=bool(outer["any_liquidation"] or stress["any_liquidation"]),
    )


def settle_combo(symbol: str, target: str, parent_pack: str) -> dict[str, Any]:
    print(f"\n=== SETTLE {symbol} {target} ===", flush=True)
    ohlcv = load_ohlcv(symbol, TIMEFRAME)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()
    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = _labels(ohlcv, target)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON)
    if len(folds) < 5:
        raise RuntimeError(f"{symbol}: need >=5 outer folds, got {len(folds)}")

    touch, touch_tf = _touch_for(symbol)
    funding = load_funding(symbol)
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    try:
        instrument = research_instrument(symbol)
    except Exception:  # noqa: BLE001
        instrument = None
    family = target_family(target)
    min_edge = _min_edge(target)
    base_costs = research_costs_baseline()
    stress_costs = research_costs_moderate_stress()

    frozen_b = walk_arm(
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
        costs=base_costs,
    )
    frozen_s = walk_arm(
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
        tag="frozen-stress",
        costs=stress_costs,
    )
    control_b = walk_arm(
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
        costs=base_costs,
    )
    control_s = walk_arm(
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
        tag="control-stress",
        costs=stress_costs,
    )

    fg = _gates_for(frozen_b, frozen_s)
    cg = _gates_for(control_b, control_s)
    print(format_gates_table(fg), flush=True)
    fs, cs = frozen_b["stitched"], control_b["stitched"]
    delta_pf = (
        float(fs["profit_factor"]) - float(cs["profit_factor"])
        if np.isfinite(fs["profit_factor"]) and np.isfinite(cs["profit_factor"])
        else None
    )
    beats_control = bool(
        delta_pf is not None
        and delta_pf > 0
        and float(fs["profit_factor"]) >= 1.20
        and int(fs["n_liquidations"]) == 0
    )
    overall = str(fg.get("overall"))
    pack_eligible = overall == "PASS" and beats_control
    return {
        "symbol": symbol,
        "target": target,
        "parent_pack": parent_pack,
        "min_edge": min_edge,
        "leverage": lev,
        "n_folds": len(folds),
        "frozen_arm": FROZEN.key,
        "control_arm": CONTROL.key,
        "frozen_stitched": {k: v for k, v in fs.items()},
        "control_stitched": {k: v for k, v in cs.items()},
        "delta_pf": delta_pf,
        "beats_control": beats_control,
        "frozen_gates": fg,
        "control_gates": cg,
        "overall": overall,
        "pack_eligible": pack_eligible,
        "frozen_folds": frozen_b["folds"],
        "control_folds": control_b["folds"],
    }


def freeze_pack_if_eligible(row: dict[str, Any]) -> dict[str, Any] | None:
    if not row.get("pack_eligible"):
        return None
    parent = PACKS / str(row["parent_pack"])
    if not parent.is_dir():
        return {"error": f"missing parent pack {parent}"}
    sym = row["symbol"].lower()
    # new name, never overwrite control pack
    dst_name = f"structure_v1_{sym}_clarity_hold12_v1"
    dst = PACKS / dst_name
    if dst.exists():
        return {"skipped": True, "path": str(dst), "reason": "already_exists"}
    shutil.copytree(parent, dst)
    strat_path = dst / "strategy.json"
    strat = json.loads(strat_path.read_text(encoding="utf-8"))
    strat["version_id"] = f"{sym}_clarity_hold12_v1"
    strat["horizon_bars"] = 12
    strat["tp_pct"] = 0.01
    strat["sl_pct"] = 0.02
    strat["execution_mode"] = "single_book"
    strat["max_positions"] = 1
    strat["clarity"] = "mean_strength"
    strat["singlebook"] = {
        "clarity": "mean_strength",
        "clarity_scope": "primary",
        "horizon_bars": 12,
        "tp_pct": 0.01,
        "sl_pct": 0.02,
        "mean_lookback": 168,
        "settled_from": GEN_ID,
    }
    strat["what_it_does"] = (
        f"FROZEN settle arm mean_strength|hold12|tp1%|sl2% for {row['symbol']} "
        f"{row['target']}. OUTER_SETTLE {GEN_ID}. Not deployed until certificate."
    )
    strat["version_lineage"] = {
        "parent_pack": row["parent_pack"],
        "research_arm": FROZEN.key,
        "generation_id": GEN_ID,
        "evidence_class": "OUTER_SETTLE",
    }
    strat_path.write_text(json.dumps(strat, indent=2) + "\n", encoding="utf-8")
    (dst / "README.md").write_text(
        f"# {dst_name}\n\nFrozen from OUTER_SETTLE {GEN_ID}. "
        f"Not live until certificate + user auth.\n",
        encoding="utf-8",
    )
    from llm2.live.certificate import pack_fingerprint

    fp = pack_fingerprint(dst)
    if fp:
        (dst / "pack_hash.txt").write_text(fp + "\n", encoding="utf-8")
    return {"path": str(dst), "pack_hash": fp, "version_id": strat["version_id"]}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--skip-conformance", action="store_true")
    ap.add_argument("--no-freeze", action="store_true", help="skip pack freeze even if PASS")
    args = ap.parse_args()
    t0 = time.perf_counter()

    if not PREREG.is_file():
        raise SystemExit(f"missing preregister {PREREG}")
    prereg_sha = _sha256_file(PREREG)

    if args.skip_conformance:
        conf: dict[str, Any] = {"status": "skipped"}
    else:
        conf = run_conformance_check()
        print(f"conformance: {conf.get('status') or conf}", flush=True)
        if conf.get("passed") is False:
            raise RuntimeError("conformance failed — stop before settle")

    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not from botsgeneral")

    rows = []
    freezes = []
    for sym, tgt, parent in COMBOS:
        row = settle_combo(sym, tgt, parent)
        rows.append(row)
        if not args.no_freeze:
            fr = freeze_pack_if_eligible(row)
            if fr:
                freezes.append(fr)
                print(f"pack freeze: {fr}", flush=True)

    n_pass = sum(1 for r in rows if r.get("overall") == "PASS")
    n_eligible = sum(1 for r in rows if r.get("pack_eligible"))
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN_ID,
            "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
            "evidence_class": "OUTER_SETTLE",
            "max_readiness": "SHADOW_READY_CANDIDATE" if n_pass else "RESEARCH_ONLY",
            "lockbox_used": False,
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "preregister_path": str(PREREG.relative_to(_ROOT)),
            "preregister_sha256": prereg_sha,
            "frozen_arm": FROZEN.key,
            "control_arm": CONTROL.key,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "n_trials_dsr": N_TRIALS_DSR,
            "conformance": conf,
            "combos": rows,
            "pack_freezes": freezes,
            "summary": [
                {
                    "symbol": r["symbol"],
                    "target": r["target"],
                    "frozen_pf": r["frozen_stitched"]["profit_factor"],
                    "control_pf": r["control_stitched"]["profit_factor"],
                    "delta_pf": r["delta_pf"],
                    "frozen_n": r["frozen_stitched"]["n_trades"],
                    "overall": r["overall"],
                    "beats_control": r["beats_control"],
                    "pack_eligible": r["pack_eligible"],
                }
                for r in rows
            ],
            "verdict": {
                "n_pass_gates": n_pass,
                "n_pack_eligible": n_eligible,
                "principal_blocker": (
                    None
                    if n_eligible == len(COMBOS)
                    else "not_all_live_matching_combos_pack_eligible"
                ),
                "no_live_deploy": True,
                "note": (
                    "OUTER_SETTLE of frozen arm. Pack freeze does not authorize VPS. "
                    "Require certificate + explicit user auth to swap Xxobster7."
                ),
            },
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "tradesim_file": str(__import__("tradesim").__file__),
        }
    )
    # strip heavy fold details for latest if needed — keep folds for audit
    stamp = report["created_utc"]
    out = REPORT_DIR / f"{GEN_ID}_{stamp}.json"
    latest = REPORT_DIR / f"{GEN_ID}_latest.json"
    # fold arrays large — keep but drop nested gate value noise if any
    slim = json.loads(json.dumps(report, default=_json_default))
    text = json.dumps(slim, indent=2)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    latest.write_text(text, encoding="utf-8")

    # annotate preregister as viewed after run
    try:
        body = PREREG.read_text(encoding="utf-8")
        if "status: ACTIVE" in body:
            PREREG.write_text(
                body.replace("status: ACTIVE", "status: OOS_SETTLE_COMPLETE")
                .replace(
                    f"created_utc: \"2026-08-04T12:50:00Z\"",
                    f"created_utc: \"2026-08-04T12:50:00Z\"\n"
                    f"settled_utc: \"{stamp}\"\n"
                    f"preregister_sha256_at_run: {prereg_sha}",
                ),
                encoding="utf-8",
            )
    except Exception as exc:  # noqa: BLE001
        print(f"prereg annotate warn: {exc}", flush=True)

    print("\n=== OUTER SETTLE SUMMARY ===", flush=True)
    for s in report["summary"]:
        print(
            f"{s['symbol']:8} {s['target']:11} frozen_pf={s['frozen_pf']} "
            f"control_pf={s['control_pf']} overall={s['overall']} "
            f"beats={s['beats_control']} pack={s['pack_eligible']}",
            flush=True,
        )
    print(f"wrote {out}", flush=True)
    return 0 if n_pass else 2


if __name__ == "__main__":
    raise SystemExit(main())
