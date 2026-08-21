"""Sweep |pred_mean| edge (0.10 baseline + 0.2…0.9) over all live_packs geometries.

MEASURE_DIAGNOSTIC / RESEARCH_ONLY — multi-edge outer stitch for comparison charts.
Does NOT promote any edge. Lockbox closed. One model fit per fold per pack;
edge only re-filters side + signal gates.

Includes 0.10 for live-pack default direction band comparison.
Return-target packs use the same absolute |pred_mean| thresholds (user request);
note return-space means often ≪ 0.2 so high edges sparsify harshly.
"""

from __future__ import annotations

import argparse
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
    research_sim,
    research_sim_hedge,
)

from llm2.backtest.conformance import run_conformance_check  # noqa: E402
from llm2.backtest.run import run_strategy_backtest  # noqa: E402
from llm2.data.loader import load_ohlcv  # noqa: E402
from llm2.data.macro import load_funding  # noqa: E402
from llm2.features.registry import build_space  # noqa: E402
from llm2.gates.evidence import leverage_from_stop, research_costs_baseline  # noqa: E402
from llm2.hunt.targets import target_family  # noqa: E402
from llm2.labels.direction import build_direction_labels  # noqa: E402
from llm2.labels.fwd_return import build_fwd_return_labels  # noqa: E402
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
from llm2.validation.folds import (  # noqa: E402
    FOLD_GEOMETRY_VERSION,
    OUTER_FOLD_RANGES,
    build_outer_folds,
    index_to_ms,
)

import importlib.util

_autopsy_path = _ROOT / "scripts" / "analyze_fleet_streak_autopsy.py"
_spec = importlib.util.spec_from_file_location("fleet_autopsy_edge", _autopsy_path)
_autopsy = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_autopsy)
_build_signals = _autopsy._build_signals
_load_strategy = _autopsy._load_strategy
discover_packs = _autopsy.discover_packs
geometry_from_strategy = _autopsy.geometry_from_strategy

GEN = "structure_v1_pred_mean_edge_sweep_001"
TIMEFRAME = "1h"
SPACE = "structure_v1"
LABEL_HORIZON = 6
# User grid + live default 0.10 for directional packs
EDGES = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]

# Live-active units (VERSIONS.md + CURRENT_STATE micro fleet)
LIVE_ACTIVE: dict[str, dict[str, str]] = {
    "btc_k5_double3h_v1": {
        "account": "Xxobster10",
        "service": "llm2-structure-btc-k5-double3h-v1",
    },
    "eth_k5_double3h_v1": {
        "account": "Xxobster6",
        "service": "llm2-structure-eth-k5-double3h-v1",
    },
    "sol_k5_double3h_v1": {
        "account": "Xxobster10",
        "service": "llm2-structure-sol-k5-double3h-v1",
    },
    "eth_multitrade_v1_2": {
        "account": "Xxobster8",
        "service": "llm2-structure-eth-multitrade-v1_2",
    },
    # Single-book Xxobster7 fleet (pack dirs lack version_id sometimes)
    "structure_v1_lgbm": {
        "account": "Xxobster7",
        "service": "llm2-structure-btc",
        "version_id_aliases": ["lgbm", "structure_v1_lgbm"],
    },
    "ethusdt_direction": {
        "account": "Xxobster7",
        "service": "llm2-structure-eth",
        "version_id_aliases": ["ethusdt_direction", "structure_v1_ethusdt_direction"],
    },
    "solusdt_direction": {
        "account": "Xxobster7",
        "service": "llm2-structure-sol",
        "version_id_aliases": ["solusdt_direction", "structure_v1_solusdt_direction"],
    },
}


def _is_live(version_id: str, pack_name: str) -> dict[str, Any]:
    keys = {version_id.lower(), pack_name.lower(), pack_name.replace("structure_v1_", "").lower()}
    for vid, meta in LIVE_ACTIVE.items():
        aliases = {vid.lower()}
        aliases.update(a.lower() for a in meta.get("version_id_aliases", []))
        if keys & aliases or version_id.lower() == vid.lower() or pack_name.lower().endswith(vid.lower()):
            return {
                "live_active": True,
                "account": meta["account"],
                "service": meta["service"],
            }
    # also match pack dir style structure_v1_{vid}
    for vid, meta in LIVE_ACTIVE.items():
        if f"structure_v1_{vid}" == pack_name.lower() or pack_name.lower() == vid.lower():
            return {
                "live_active": True,
                "account": meta["account"],
                "service": meta["service"],
            }
    # eth/sol/btc singles
    if pack_name in (
        "structure_v1_ethusdt_direction",
        "structure_v1_solusdt_direction",
        "structure_v1_lgbm",
    ):
        m = {
            "structure_v1_lgbm": LIVE_ACTIVE["structure_v1_lgbm"],
            "structure_v1_ethusdt_direction": LIVE_ACTIVE["ethusdt_direction"],
            "structure_v1_solusdt_direction": LIVE_ACTIVE["solusdt_direction"],
        }[pack_name]
        return {"live_active": True, "account": m["account"], "service": m["service"]}
    return {"live_active": False, "account": None, "service": None}


def _labels(ohlcv: pd.DataFrame, target: str) -> pd.Series:
    if target == "direction":
        return build_direction_labels(ohlcv, horizon=LABEL_HORIZON)["direction"]
    if target == "fwd_return":
        return build_fwd_return_labels(ohlcv, horizon=LABEL_HORIZON)["fwd_return"]
    raise ValueError(target)


def side_from_abs_edge(mean: np.ndarray, *, edge: float) -> np.ndarray:
    """Long if mean > edge, short if mean < -edge (any target family)."""
    m = np.asarray(mean, dtype=float)
    e = float(edge)
    return np.where(m > e, 1, np.where(m < -e, -1, 0)).astype(int)


def _finite(x: Any) -> Any:
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    if isinstance(x, (np.floating,)):
        v = float(x)
        return None if not math.isfinite(v) else v
    return x


def _metrics_bundle(bundle: Any) -> dict[str, Any]:
    m = bundle.metrics
    trades = list(bundle.result.trades)
    pnls = np.asarray(
        [float(getattr(t, "realized_pnl", 0) or 0) for t in trades], dtype=float
    )
    rus = np.asarray(
        [float(getattr(t, "return_units", float("nan"))) for t in trades], dtype=float
    )
    a = pnls[np.isfinite(pnls)]
    ru = rus[np.isfinite(rus)]
    gp = float(a[a > 0].sum()) if a.size else 0.0
    gl = float((-a[a < 0]).sum()) if a.size else 0.0
    pf = (gp / gl) if gl > 0 else (float("inf") if gp > 0 else float("nan"))

    def _scalar(obj: Any, *attrs: str) -> Any:
        v = obj
        for a_ in attrs:
            if v is None:
                return None
            v = getattr(v, a_, None)
        if v is None:
            return None
        if isinstance(v, (int, float, np.floating)):
            return _finite(float(v))
        # e.g. SharpeReport.annualized / .raw
        for key in ("annualized", "value", "sharpe", "ratio", "max_drawdown"):
            if hasattr(v, key):
                try:
                    return _finite(float(getattr(v, key)))
                except (TypeError, ValueError):
                    continue
        try:
            return _finite(float(v))
        except (TypeError, ValueError):
            return None

    return {
        "n_trades": int(a.size),
        "net_pnl": _finite(float(np.nansum(a)) if a.size else 0.0),
        "profit_factor": _finite(float(pf)),
        "win_rate": _finite(float(np.mean(a > 0)) if a.size else float("nan")),
        "expectancy": _finite(float(np.mean(a)) if a.size else float("nan")),
        "expectancy_return_units": _scalar(m, "expectancy_return_units")
        if _scalar(m, "expectancy_return_units") is not None
        else _finite(float(np.mean(ru)) if ru.size else float("nan")),
        "total_fees": _scalar(m, "total_fees"),
        "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
        "max_drawdown": _scalar(m, "max_drawdown")
        or _scalar(m, "max_drawdown", "value"),
        "sharpe": _scalar(m, "sharpe") or _scalar(m, "sharpe", "annualized"),
    }


def stitch_edge_for_pack(
    pack_dir: Path,
    edges: list[float],
) -> dict[str, Any]:
    strategy = _load_strategy(pack_dir)
    geom0 = geometry_from_strategy(strategy)
    symbol = geom0["symbol"]
    target = geom0["target"]
    version_id = geom0["version_id"]
    live = _is_live(version_id, pack_dir.name)
    pack_min_edge = float(geom0["min_edge"])
    family = target_family(target)

    out: dict[str, Any] = {
        "pack": pack_dir.name,
        "version_id": version_id,
        "symbol": symbol,
        "target": target,
        "target_family": family,
        "mode": geom0["mode"],
        "pack_min_edge": pack_min_edge,
        "live": live,
        "edges": {},
        "error": None,
    }
    if not symbol:
        out["error"] = "missing_symbol"
        return out

    print(
        f"SWEEP {pack_dir.name} vid={version_id} target={target} live={live['live_active']}",
        flush=True,
    )
    try:
        ohlcv = load_ohlcv(symbol, TIMEFRAME)
    except Exception as exc:  # noqa: BLE001
        out["error"] = f"load_ohlcv: {exc}"
        return out

    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    if len(ohlcv) < 500:
        out["error"] = "insufficient_bars"
        return out

    feats = build_space(ohlcv, SPACE, symbol=symbol, timeframe=TIMEFRAME)
    y = _labels(ohlcv, target)
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(
        ts_ms, purge_bars=LABEL_HORIZON, embargo_bars=LABEL_HORIZON
    )
    touch = load_ohlcv(symbol, touch_timeframe(TIMEFRAME, symbol))
    touch_tf = touch_timeframe(TIMEFRAME, symbol)
    funding = load_funding(symbol)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(float(geom0["sl"])))
    instrument = research_instrument(symbol)
    close_aligned = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)

    # Accumulate per edge
    acc: dict[float, dict[str, Any]] = {
        e: {
            "fold_metrics": [],
            "all_pnls": [],
            "all_ru": [],
            "n_liq": 0,
            "mean_abs_tradeable": [],
        }
        for e in edges
    }

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        oos_ts = ts_ms[oos]
        close_oos = close_aligned[oos]

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        hold = max(int(geom0["hold"]), int(geom0.get("hold_addon") or geom0["hold"]))
        pad = max(50, hold * 4)
        pos = int(ohlcv.index.searchsorted(oos0))
        window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
        end, start = window.index[-1], window.index[0]
        dec_ms = int(TF_MS[TIMEFRAME])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
        w_ts = index_to_ms(window.index)
        fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))

        for edge in edges:
            side = side_from_abs_edge(mean, edge=edge)
            geom = dict(geom0)
            geom["min_edge"] = float(edge)
            sigs, stats, sim = _build_signals(
                geom, oos_ts, side, mean, close_oos, instrument
            )
            bundle = run_strategy_backtest(
                window,
                sigs,
                symbol=symbol,
                timeframe=TIMEFRAME,
                strategy_id=f"{version_id}-e{edge}-f{fold.fold_index}",
                touch_ohlcv=touch_win,
                touch_timeframe=touch_tf,
                costs=research_costs_baseline(),
                margin=research_margin(leverage=lev),
                sizing=research_sizing(),
                sim=sim,
                instrument=instrument,
                funding_ts_ms=funding_ts[fmask],
                funding_rate=funding_rt[fmask],
                strategy_meta={
                    "name": version_id,
                    "generation_id": GEN,
                    "pred_mean_edge": edge,
                },
                plot=False,
                print_headline=False,
                store_path=None,
            )
            mdict = _metrics_bundle(bundle)
            mdict["fold_index"] = int(fold.fold_index)
            mdict["n_signals"] = int(stats.get("n_emitted") or len(sigs))
            acc[edge]["fold_metrics"].append(mdict)
            trades = list(bundle.result.trades)
            acc[edge]["all_pnls"].extend(
                float(getattr(t, "realized_pnl", 0) or 0) for t in trades
            )
            acc[edge]["all_ru"].extend(
                float(getattr(t, "return_units", float("nan"))) for t in trades
            )
            acc[edge]["n_liq"] += int(mdict.get("n_liquidations") or 0)
            mask = side != 0
            if np.any(mask):
                acc[edge]["mean_abs_tradeable"].append(
                    float(np.mean(np.abs(mean[mask])))
                )

        print(
            f"  fold {fold.fold_index}: mean|pred| p50={np.nanpercentile(np.abs(mean), 50):.4f} "
            f"p90={np.nanpercentile(np.abs(mean), 90):.4f}",
            flush=True,
        )

    for edge in edges:
        a = np.asarray(acc[edge]["all_pnls"], dtype=float)
        a = a[np.isfinite(a)]
        gp = float(a[a > 0].sum()) if a.size else 0.0
        gl = float((-a[a < 0]).sum()) if a.size else 0.0
        if gl > 0:
            stitched_pf = gp / gl
        elif gp > 0:
            stitched_pf = float("inf")
        else:
            stitched_pf = float("nan")
        ru = np.asarray(acc[edge]["all_ru"], dtype=float)
        ru = ru[np.isfinite(ru)]
        # trade-weighted E[r] from folds if available
        exp_num = exp_den = 0.0
        for fr in acc[edge]["fold_metrics"]:
            n = float(fr.get("n_trades") or 0)
            eru = fr.get("expectancy_return_units")
            if n > 0 and eru is not None and math.isfinite(float(eru)):
                exp_num += float(eru) * n
                exp_den += n
        stitched = {
            "pred_mean_edge": edge,
            "n_trades": int(a.size),
            "net_pnl": _finite(float(np.nansum(a)) if a.size else 0.0),
            "profit_factor": _finite(float(stitched_pf)),
            "win_rate": _finite(float(np.mean(a > 0)) if a.size else float("nan")),
            "expectancy": _finite(float(np.mean(a)) if a.size else float("nan")),
            "expectancy_return_units": _finite(
                (exp_num / exp_den)
                if exp_den
                else (float(np.mean(ru)) if ru.size else float("nan"))
            ),
            "n_liquidations": int(acc[edge]["n_liq"]),
            "is_pack_default_edge": abs(edge - pack_min_edge) < 1e-9
            or (
                family == "directional"
                and abs(edge - 0.10) < 1e-9
                and abs(pack_min_edge - 0.10) < 1e-9
            ),
            "mean_abs_when_tradeable": _finite(
                float(np.mean(acc[edge]["mean_abs_tradeable"]))
                if acc[edge]["mean_abs_tradeable"]
                else float("nan")
            ),
            "folds": acc[edge]["fold_metrics"],
        }
        out["edges"][f"{edge:.2f}"] = stitched
        print(
            f"  edge={edge:.2f}: n={stitched['n_trades']} pf={stitched['profit_factor']} "
            f"eru={stitched['expectancy_return_units']}",
            flush=True,
        )
    return out


def _rank_best(rows: list[dict[str, Any]]) -> dict[str, Any]:
    flat: list[dict[str, Any]] = []
    for r in rows:
        if r.get("error") or not r.get("edges"):
            continue
        for ek, m in r["edges"].items():
            if not m.get("n_trades"):
                continue
            flat.append(
                {
                    "version_id": r["version_id"],
                    "pack": r["pack"],
                    "symbol": r["symbol"],
                    "target": r["target"],
                    "mode": r["mode"],
                    "live_active": bool((r.get("live") or {}).get("live_active")),
                    "live_account": (r.get("live") or {}).get("account"),
                    "pred_mean_edge": m["pred_mean_edge"],
                    "n_trades": m["n_trades"],
                    "profit_factor": m["profit_factor"],
                    "expectancy_return_units": m["expectancy_return_units"],
                    "win_rate": m["win_rate"],
                    "net_pnl": m["net_pnl"],
                    "n_liquidations": m["n_liquidations"],
                    "is_pack_default_edge": m.get("is_pack_default_edge"),
                }
            )

    def key_eru(x: dict[str, Any]) -> float:
        v = x.get("expectancy_return_units")
        return float(v) if v is not None and math.isfinite(float(v)) else -1e18

    def key_pf(x: dict[str, Any]) -> float:
        v = x.get("profit_factor")
        if v is None:
            return -1e18
        fv = float(v)
        return fv if math.isfinite(fv) else 1e18  # inf PF last unless we want top — put high

    by_eru = sorted(flat, key=key_eru, reverse=True)[:15]
    by_pf = sorted(
        [x for x in flat if x.get("n_trades", 0) >= 50],
        key=lambda x: (
            float(x["profit_factor"])
            if x.get("profit_factor") is not None and math.isfinite(float(x["profit_factor"]))
            else -1.0
        ),
        reverse=True,
    )[:15]
    # best edge per pack by E[r]
    best_per_pack: list[dict[str, Any]] = []
    by_pack: dict[str, list[dict[str, Any]]] = {}
    for x in flat:
        by_pack.setdefault(x["version_id"], []).append(x)
    for vid, items in by_pack.items():
        best = max(items, key=key_eru)
        best_per_pack.append(best)
    best_per_pack.sort(key=key_eru, reverse=True)
    return {
        "top_by_expectancy_return_units": by_eru,
        "top_by_profit_factor_min50_trades": by_pf,
        "best_edge_per_pack_by_eru": best_per_pack,
        "n_cells_with_trades": len(flat),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument(
        "--edges",
        type=str,
        default=",".join(str(e) for e in EDGES),
        help="comma-separated pred_mean abs thresholds",
    )
    args = ap.parse_args()
    edges = [float(x.strip()) for x in args.edges.split(",") if x.strip()]

    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    packs = discover_packs(only=args.only)
    if not packs:
        raise SystemExit("no packs found")

    t0 = time.perf_counter()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_dir = ARTIFACTS / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    checkpoint = report_dir / f"{GEN}_checkpoint.json"
    rows: list[dict[str, Any]] = []

    for pack in packs:
        try:
            r = stitch_edge_for_pack(pack, edges)
        except Exception as exc:  # noqa: BLE001
            r = {
                "pack": pack.name,
                "error": f"{type(exc).__name__}: {exc}",
                "edges": {},
            }
            print(f"  ERROR {pack.name}: {exc}", flush=True)
        rows.append(r)
        checkpoint.write_text(
            json.dumps(
                {"generation_id": GEN, "rows": rows, "progress": len(rows)},
                indent=2,
                default=str,
            ),
            encoding="utf-8",
        )

    rankings = _rank_best(rows)
    payload = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": stamp,
            "evidence_class": "MEASURE_DIAGNOSTIC",
            "max_readiness": "RESEARCH_ONLY",
            "promotion_allowed": False,
            "note": (
                "Multi-edge outer-stitch comparison for charts only. Ranking is "
                "exploratory — do not promote edges selected on outer OOS without "
                "a new frozen single-arm prereg and settle."
            ),
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "pred_mean_edges": edges,
            "conformance_passed": bool(conf.get("passed")),
            "n_packs": len(rows),
            "packs": rows,
            "rankings": rankings,
            "live_active_map": LIVE_ACTIVE,
            "elapsed_sec": round(time.perf_counter() - t0, 1),
        }
    )
    latest = report_dir / f"{GEN}_latest.json"
    latest.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    (report_dir / f"{GEN}_{stamp}.json").write_text(
        latest.read_text(encoding="utf-8"), encoding="utf-8"
    )
    # Compact CSV of all cells
    flat_rows = rankings.get("top_by_expectancy_return_units")  # noqa — rebuild full
    csv_path = report_dir / f"{GEN}_all_cells.csv"
    flat_all: list[dict[str, Any]] = []
    for r in rows:
        if not r.get("edges"):
            continue
        for ek, m in r["edges"].items():
            flat_all.append(
                {
                    "version_id": r.get("version_id"),
                    "pack": r.get("pack"),
                    "symbol": r.get("symbol"),
                    "target": r.get("target"),
                    "mode": r.get("mode"),
                    "live_active": bool((r.get("live") or {}).get("live_active")),
                    "live_account": (r.get("live") or {}).get("account"),
                    "pred_mean_edge": m.get("pred_mean_edge"),
                    "n_trades": m.get("n_trades"),
                    "profit_factor": m.get("profit_factor"),
                    "expectancy_return_units": m.get("expectancy_return_units"),
                    "win_rate": m.get("win_rate"),
                    "net_pnl": m.get("net_pnl"),
                    "expectancy": m.get("expectancy"),
                    "n_liquidations": m.get("n_liquidations"),
                    "is_pack_default_edge": m.get("is_pack_default_edge"),
                }
            )
    if flat_all:
        pd.DataFrame(flat_all).to_csv(csv_path, index=False)
    print(json.dumps({"n_packs": len(rows), "rankings_head": rankings["top_by_expectancy_return_units"][:5]}, indent=2, default=str))
    print(f"wrote {latest}")
    print(f"csv {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
