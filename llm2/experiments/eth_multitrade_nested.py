"""Shared outer-fold stitch for eth_multitrade nested arm compares."""

from __future__ import annotations

from typing import Any

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
)
from llm2.models.boosting import LGBMRegressorPredictor  # noqa: E402
from llm2.paths import FORWARD_LOCKBOX_START, TF_MS, touch_timeframe  # noqa: E402
from llm2.validation.folds import build_outer_folds, index_to_ms  # noqa: E402

SYMBOL = "ETHUSDT"
TIMEFRAME = "1h"
SPACE = "structure_v1"
TARGET = "direction"
LABEL_HORIZON = 6
SL = 0.02
MIN_EDGE = DIRECTION_BAND
K = 7


def build_multitrade_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    *,
    cfg: dict[str, Any],
) -> tuple[list[Signal], dict[str, Any]]:
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


def pf(pnls: list[float] | np.ndarray) -> float:
    a = np.asarray(pnls, dtype=float)
    a = a[np.isfinite(a)]
    if a.size == 0:
        return float("nan")
    gp = float(a[a > 0].sum())
    gl = float((-a[a < 0]).sum())
    if gl <= 0:
        return float("inf") if gp > 0 else float("nan")
    return gp / gl


def live_control_cfg() -> dict[str, Any]:
    return {
        "max_positions_per_side": K,
        "clarity": "mean_strength",
        "clarity_scope": "addon",
        "fib_ext": 1.618,
        "hold_addon": 12,
        "base_hold": 6,
        "base_tp": 0.01,
        "base_sl": 0.02,
        "mean_lookback": MEAN_LOOKBACK,
        "uniform_books": False,
        "bar_ms": 3_600_000,
    }


def _book_from_trade(t: Any, sig_book: dict[int, int]) -> int:
    """Prefer signal tag ``k*_bN``; entry_ts often differs from signal_ts after fill lag."""
    tag = str(getattr(t, "tag", "") or "")
    if "_b" in tag:
        try:
            return int(tag.rsplit("_b", 1)[-1])
        except ValueError:
            pass
    return int(sig_book.get(int(t.entry_ts_ms), 0))


def book1_wrong_way_1h(
    trades: list[Any],
    *,
    sig_book: dict[int, int],
    close: np.ndarray,
    ts_to_i: dict[int, int],
) -> float:
    flags: list[bool] = []
    for t in trades:
        if _book_from_trade(t, sig_book) != 1:
            continue
        ets = int(t.entry_ts_ms)
        s = int(getattr(t.side, "value", t.side))
        i = ts_to_i.get(ets)
        if i is None or i + 1 >= len(close):
            continue
        px0 = float(close[i])
        px1 = float(close[i + 1])
        if px0 <= 0 or not np.isfinite(px0) or not np.isfinite(px1):
            continue
        signed = float(s) * (px1 / px0 - 1.0)
        flags.append(signed < 0)
    return float(np.mean(flags)) if flags else float("nan")


def stitch_arm(
    cfg: dict[str, Any],
    *,
    label: str,
) -> dict[str, Any]:
    """Walk-forward outer stitch for one multitrade config on ETHUSDT direction."""
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
    full_close = ohlcv["close"].to_numpy(dtype=float)
    full_ts = index_to_ms(ohlcv.index)
    ts_to_i = {int(t): i for i, t in enumerate(full_ts)}

    fold_rows: list[dict[str, Any]] = []
    all_pnls: list[float] = []
    all_trades: list[Any] = []
    sig_book: dict[int, int] = {}
    exit_counts: dict[str, int] = {}
    total_stats = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_primary": 0,
        "n_addon": 0,
    }
    n_liq = 0

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        sigs, stats = build_multitrade_signals(oos_ts, side, mean, cfg=cfg)
        for s in sigs:
            sig_book[int(s.ts_ms)] = int((s.meta or {}).get("book_idx", 0) or 0)
        for k in total_stats:
            total_stats[k] += int(stats.get(k, 0))

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, int(cfg["hold_addon"]) * 4)
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
                max_hold_bars=int(cfg["hold_addon"]),
                decision_timeframe=TIMEFRAME,
                max_positions_per_side=int(cfg["max_positions_per_side"]),
                max_positions_per_symbol=int(cfg["max_positions_per_side"]) * 2,
            ),
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": label},
            plot=False,
            print_headline=False,
            store_path=None,
        )
        m = bundle.metrics
        trades = list(bundle.result.trades)
        pnls = [float(getattr(t, "realized_pnl", 0) or 0) for t in trades]
        all_pnls.extend(pnls)
        all_trades.extend(trades)
        n_liq += int(getattr(m, "n_liquidations", 0) or 0)
        for t in trades:
            reason = str(getattr(t, "exit_reason", "") or "unknown")
            exit_counts[reason] = exit_counts.get(reason, 0) + 1
        fold_rows.append(
            {
                "fold_index": int(fold.fold_index),
                "n_trades": int(m.n_trades),
                "net_pnl": float(m.net_pnl),
                "profit_factor": float(m.profit_factor),
                "win_rate": float(getattr(m, "win_rate", float("nan"))),
                "signal_stats": stats,
                "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
            }
        )

    wins = sum(1 for p in all_pnls if p > 0)
    return {
        "label": label,
        "cfg": {
            k: cfg[k]
            for k in (
                "clarity",
                "clarity_scope",
                "max_positions_per_side",
                "fib_ext",
                "hold_addon",
                "base_hold",
                "base_tp",
                "base_sl",
            )
        },
        "folds": fold_rows,
        "stitched": {
            "n_trades": len(all_pnls),
            "net_pnl": float(np.nansum(all_pnls)),
            "profit_factor": pf(all_pnls),
            "win_rate": float(wins / len(all_pnls)) if all_pnls else float("nan"),
            "n_liquidations": int(n_liq),
            "frac_folds_pf_gt_1": float(
                np.mean([r["profit_factor"] > 1 for r in fold_rows])
            )
            if fold_rows
            else float("nan"),
        },
        "signal_stats_total": total_stats,
        "exit_reasons": exit_counts,
        "book1_wrong_way_1h": book1_wrong_way_1h(
            all_trades, sig_book=sig_book, close=full_close, ts_to_i=ts_to_i
        ),
        "leverage": lev,
    }
