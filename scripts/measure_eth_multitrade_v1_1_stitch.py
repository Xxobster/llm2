"""Measure live ETH multitrade v1.1 geometry (K=7 fib) — fold V2 stitch, no retune.

Hard end exclusive: FORWARD_LOCKBOX_START. Evidence class MEASURE_LIVE_GEOMETRY.
"""

from __future__ import annotations

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
    Side,
    Signal,
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
from llm2.live.multitrade import (  # noqa: E402
    MEAN_LOOKBACK,
    book_tp_hold,
    mean_strength_ok,
    parse_multitrade_config,
)
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.research_policy import stamp_min_size_equity_caveat  # noqa: E402
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
K = 7
SL = 0.02
MIN_EDGE = DIRECTION_BAND
GEN = "structure_v1_eth_multitrade_v1_1_measure"
PACK = ARTIFACTS / "live_packs" / "structure_v1_ethusdt_multitrade_v1_1"


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


def _bootstrap_pos_exp(pnls: np.ndarray, n: int = 2000, seed: int = 42) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size < 10:
        return float("nan")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(a), size=(n, len(a)))
    return float(np.mean(a[idx].mean(axis=1) > 0))


def build_multitrade_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    *,
    cfg: dict[str, Any],
) -> tuple[list[Signal], dict[str, Any]]:
    """Recreate live multitrade gate (addon clarity, fib book tiers)."""
    cap = int(cfg["max_positions_per_side"])
    clarity = str(cfg.get("clarity", "none"))
    scope = str(cfg.get("clarity_scope", "addon"))
    lookback = int(cfg.get("mean_lookback", MEAN_LOOKBACK))
    bar_ms = int(cfg.get("bar_ms", 3_600_000))
    open_exit: dict[int, list[int]] = {1: [], -1: []}
    strength_hist: list[float] = []
    out: list[Signal] = []
    stats = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_primary": 0,
        "n_addon": 0,
    }
    for i in range(len(ts_ms)):
        s = int(side[i])
        m = float(mean[i])
        if s == 0 or not np.isfinite(m) or abs(m) < MIN_EDGE:
            continue
        ts = int(ts_ms[i])
        open_exit[s] = [e for e in open_exit[s] if int(e) > ts]
        n_open = len(open_exit[s])
        is_addon = n_open >= 1
        abs_m = abs(m)
        recent = strength_hist[-lookback:] if strength_hist else []
        apply_clarity = clarity == "mean_strength" and (
            scope == "all" or (scope == "addon" and is_addon)
        )
        if apply_clarity and not mean_strength_ok(abs_m, recent):
            stats["n_skipped_clarity"] += 1
            strength_hist.append(abs_m)
            continue
        if n_open >= cap:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs_m)
            continue
        book_idx = n_open + 1
        tp, hold = book_tp_hold(
            book_idx,
            fib_ext=float(cfg["fib_ext"]),
            hold_addon=int(cfg["hold_addon"]),
            base_tp=float(cfg["base_tp"]),
            base_hold=int(cfg["base_hold"]),
            uniform_books=bool(cfg.get("uniform_books", False)),
        )
        if book_idx == 1:
            stats["n_primary"] += 1
        else:
            stats["n_addon"] += 1
        out.append(
            Signal(
                ts_ms=ts,
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(cfg["base_sl"]),
                target_offset=float(tp),
                max_hold_bars=int(hold),
                tag=f"k{cap}_b{book_idx}",
                meta={"book_idx": book_idx, "tp_pct": tp, "hold": hold},
            )
        )
        open_exit[s].append(ts + int(hold) * bar_ms)
        strength_hist.append(abs_m)
        stats["n_emitted"] += 1
    return out, stats


def main() -> int:
    t0 = time.perf_counter()
    conf = run_conformance_check()
    if conf.get("passed") is False:
        raise RuntimeError("conformance failed")
    if "botsgeneral" not in str(__import__("tradesim").__file__).lower():
        raise RuntimeError("tradesim not botsgeneral")

    pack_strat = json.loads((PACK / "strategy.json").read_text(encoding="utf-8"))
    cfg = parse_multitrade_config(pack_strat)
    if not cfg:
        raise SystemExit("pack is not multitrade")
    # live v1.1: addon clarity default (parse sets addon)
    cfg["max_positions_per_side"] = K
    cfg["fib_ext"] = float((pack_strat.get("multitrade") or {}).get("fib_ext", 1.618))
    cfg["hold_addon"] = int((pack_strat.get("multitrade") or {}).get("hold_addon", 12))
    cfg["base_hold"] = int((pack_strat.get("multitrade") or {}).get("base_hold", 6))
    cfg["base_tp"] = 0.01
    cfg["base_sl"] = 0.02
    cfg["clarity"] = "mean_strength"
    cfg["clarity_scope"] = str(
        (pack_strat.get("multitrade") or {}).get("clarity_scope") or "addon"
    )
    cfg["uniform_books"] = False

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

    fold_rows = []
    all_pnls: list[float] = []
    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        sigs, stats = build_multitrade_signals(ts_ms[oos], side, mean, cfg=cfg)
        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, int(cfg["base_hold"]) * 4)
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
            strategy_id=f"mt-v11-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_hedge(
                max_hold_bars=int(cfg["hold_addon"]),
                decision_timeframe=TIMEFRAME,
                max_positions_per_side=K,
                max_positions_per_symbol=K * 2,
            ),
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": GEN, "k": K},
            plot=False,
            print_headline=False,
            store_path=None,
        )
        m = bundle.metrics
        pnls = [float(getattr(t, "realized_pnl", 0) or 0) for t in bundle.result.trades]
        all_pnls.extend(pnls)
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "n_trades": int(m.n_trades),
                "net_pnl": float(m.net_pnl),
                "profit_factor": float(m.profit_factor),
                "win_rate": float(getattr(m, "win_rate", float("nan"))),
                "n_signals": int(stats["n_emitted"]),
                "signal_stats": stats,
                "entry_bar_exits": int(getattr(m, "entry_bar_exits", 0) or 0),
                "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
                "total_fees": float(getattr(m, "total_fees", float("nan"))),
            }
        )
        print(
            f"fold {fold.fold_index}: n={m.n_trades} pf={m.profit_factor:.3f} "
            f"pnl={m.net_pnl:.2f} wr={getattr(m,'win_rate',float('nan')):.1%}",
            flush=True,
        )

    stitched = {
        "n_trades": len(all_pnls),
        "net_pnl": float(np.nansum(all_pnls)),
        "profit_factor": _pf(all_pnls),
        "bootstrap_pos_exp": _bootstrap_pos_exp(np.asarray(all_pnls)),
        "frac_folds_pf_gt_1": float(np.mean([r["profit_factor"] > 1 for r in fold_rows])),
        "n_liquidations": int(sum(r["n_liquidations"] for r in fold_rows)),
        "total_fees": float(np.nansum([r["total_fees"] for r in fold_rows])),
        "entry_bar_exits": int(sum(r["entry_bar_exits"] for r in fold_rows)),
    }
    report = stamp_min_size_equity_caveat(
        {
            "generation_id": GEN,
            "created_utc": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
            "evidence_class": "MEASURE_LIVE_GEOMETRY",
            "live_unit": "llm2-structure-eth-multitrade-v1_1",
            "live_account": "Xxobster8",
            "pack": str(PACK.relative_to(_ROOT)),
            "geometry": {
                "k": K,
                "clarity": cfg["clarity"],
                "clarity_scope": cfg["clarity_scope"],
                "fib_ext": cfg["fib_ext"],
                "base_hold": cfg["base_hold"],
                "hold_addon": cfg["hold_addon"],
                "base_tp": cfg["base_tp"],
                "base_sl": cfg["base_sl"],
            },
            "hard_end_exclusive": FORWARD_LOCKBOX_START,
            "lockbox_used": False,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "conformance": conf,
            "folds": fold_rows,
            "stitched": stitched,
            "leverage": lev,
            "elapsed_sec": round(time.perf_counter() - t0, 1),
            "max_readiness": "RESEARCH_ONLY",
            "note": "Measurement of live Xxobster8 pack geometry on clean outer folds.",
        }
    )
    out = ARTIFACTS / "reports" / f"{GEN}_latest.json"
    stamp = report["created_utc"]
    out.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    (ARTIFACTS / "reports" / f"{GEN}_{stamp}.json").write_text(out.read_text(), encoding="utf-8")
    print(json.dumps({"stitched": stitched, "geometry": report["geometry"]}, indent=2))
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
