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
    scale_tp_by_abs_mean,
    slot_release_ts_ms,
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
    close: np.ndarray | None = None,
    seed_strength_hist: list[float] | None = None,
    occupancy_bars: dict[str, np.ndarray] | None = None,
) -> tuple[list[Signal], dict[str, Any]]:
    """Concurrent-book gate. Shares ``decide_entry_gate`` semantics with the live bot.

    ``occupancy_bars`` (keys ``ts_ms``/``open``/``high``/``low``) makes a book release
    its slot when the take-profit or stop is touched, which is what live does. Without
    it a slot is held to max-hold and the backtest skips entries live took.
    """
    cap = int(cfg["max_positions_per_side"])
    clarity = str(cfg.get("clarity", "none"))
    scope = str(cfg.get("clarity_scope", "addon"))
    lookback = int(cfg.get("mean_lookback", MEAN_LOOKBACK))
    bar_ms = int(cfg.get("bar_ms", 3_600_000))
    strength_q = float(cfg.get("strength_quantile", 0.5) or 0.5)
    cooloff_n = max(0, int(cfg.get("cooloff_after_consecutive_losses", 0) or 0))
    pause_bars = int(cfg.get("cooloff_pause_bars") or cfg.get("base_hold") or 6)
    # Causal autopsy filter: skip SHORT book1 unless |mean| is in high tercile.
    skip_weak_short_book1 = bool(cfg.get("skip_weak_short_book1", False))
    # High tercile floor: quantile 2/3 of strength history (top third).
    weak_short_q = float(cfg.get("weak_short_book1_strength_quantile", 2.0 / 3.0) or (2.0 / 3.0))
    open_exit: dict[int, list[int]] = {1: [], -1: []}
    # Optional pre-window |mean| history so lockbox opens with a warm quantile floor
    # (books stay empty — only strength gate memory is seeded).
    strength_hist: list[float] = (
        [float(x) for x in seed_strength_hist] if seed_strength_hist else []
    )
    open_books: list[tuple[int, int, float]] = []
    consecutive_losses = 0
    cooloff_until_ts = -1
    close_a = None if close is None else np.asarray(close, dtype=float)
    occ = occupancy_bars or None
    double_bars = int(cfg.get("size_double_within_bars", 0) or 0)
    double_mult = float(cfg.get("size_double_mult", 2.0) or 2.0)
    last_entry_ts: dict[int, int | None] = {1: None, -1: None}
    out: list[Signal] = []
    stats = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_skipped_loss_cooloff": 0,
        "n_skipped_weak_short_book1": 0,
        "n_primary": 0,
        "n_addon": 0,
    }
    pause_ms = int(pause_bars) * int(bar_ms)
    for i in range(len(ts_ms)):
        s = int(side[i])
        m = float(mean[i])
        ts = int(ts_ms[i])
        px = float(close_a[i]) if close_a is not None and np.isfinite(close_a[i]) else float("nan")

        if cooloff_n > 0 and close_a is not None and np.isfinite(px) and px > 0:
            still: list[tuple[int, int, float]] = []
            for exit_ts, bs, entry_px in open_books:
                if int(exit_ts) > ts:
                    still.append((exit_ts, bs, entry_px))
                    continue
                signed = float(bs) * (float(px) / float(entry_px) - 1.0)
                if signed < 0:
                    consecutive_losses += 1
                    if consecutive_losses >= cooloff_n:
                        cooloff_until_ts = max(cooloff_until_ts, ts + pause_ms)
                elif signed > 0:
                    consecutive_losses = 0
            open_books = still

        edge = float(cfg.get("min_edge", MIN_EDGE) or MIN_EDGE)
        if s == 0 or not np.isfinite(m) or abs(m) < edge:
            continue
        open_exit[s] = [e for e in open_exit[s] if int(e) > ts]
        n_open = len(open_exit[s])
        is_addon = n_open >= 1
        abs_m = abs(m)
        recent = strength_hist[-lookback:] if strength_hist else []
        apply_clarity = clarity == "mean_strength" and (
            scope == "all" or (scope == "addon" and is_addon)
        )
        if apply_clarity and not mean_strength_ok(
            abs_m, recent, strength_quantile=strength_q
        ):
            stats["n_skipped_clarity"] += 1
            strength_hist.append(abs_m)
            continue
        if cooloff_n > 0 and close_a is not None and ts < int(cooloff_until_ts):
            stats["n_skipped_loss_cooloff"] += 1
            strength_hist.append(abs_m)
            continue
        if n_open >= cap:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs_m)
            continue
        book_idx = n_open + 1
        # Decision-time only: side + book_idx + strength history (no exits).
        if (
            skip_weak_short_book1
            and book_idx == 1
            and s < 0
            and strength_hist
        ):
            thr = float(np.quantile(np.asarray(strength_hist[-lookback:], dtype=float), weak_short_q))
            if abs_m < thr:
                stats["n_skipped_weak_short_book1"] += 1
                strength_hist.append(abs_m)
                continue
        tp, hold = book_tp_hold(
            book_idx,
            fib_ext=float(cfg["fib_ext"]),
            hold_addon=int(cfg["hold_addon"]),
            base_tp=float(cfg["base_tp"]),
            base_hold=int(cfg["base_hold"]),
            uniform_books=bool(cfg.get("uniform_books", False)),
        )
        if bool(cfg.get("tp_scale_by_abs_mean", False)):
            tp = scale_tp_by_abs_mean(
                float(tp),
                abs_m,
                ref=float(cfg.get("tp_scale_ref", 0.5) or 0.5),
                factor_min=float(cfg.get("tp_scale_factor_min", 1.0) or 1.0),
                factor_max=float(cfg.get("tp_scale_factor_max", 2.0) or 2.0),
            )
        if book_idx == 1:
            stats["n_primary"] += 1
        else:
            stats["n_addon"] += 1
        # Same size rule as live: a same-side re-entry inside the doubling window
        # trades a multiple of the venue minimum.
        size_mult = 1.0
        prev_ts = last_entry_ts[s]
        if double_bars > 0 and prev_ts is not None:
            gap = ts - int(prev_ts)
            if 0 <= gap <= double_bars * bar_ms:
                size_mult = double_mult
        out.append(
            Signal(
                ts_ms=ts,
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(cfg["base_sl"]),
                target_offset=float(tp),
                max_hold_bars=int(hold),
                tag=f"k{cap}_b{book_idx}",
                meta={
                    "pred_mean": float(m),
                    "abs_mean": float(abs_m),
                    "book_idx": book_idx,
                    "tp_pct": tp,
                    "hold": hold,
                    "size_mult": float(size_mult),
                },
            )
        )
        last_entry_ts[s] = ts
        if occ is not None:
            release = slot_release_ts_ms(
                ts,
                s,
                tp_pct=float(tp),
                sl_pct=float(cfg["base_sl"]),
                max_hold_bars=int(hold),
                bar_ts_ms=occ["ts_ms"],
                bar_open=occ["open"],
                bar_high=occ["high"],
                bar_low=occ["low"],
                tf_ms=bar_ms,
            )
        else:
            release = ts + int(hold) * bar_ms
        open_exit[s].append(release)
        if cooloff_n > 0 and close_a is not None and np.isfinite(px) and px > 0:
            open_books.append((ts + int(hold) * bar_ms, s, px))
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
    timeframe: str | None = None,
    symbol: str | None = None,
    label_horizon: int | None = None,
) -> dict[str, Any]:
    """Walk-forward outer stitch for one multitrade config on ETHUSDT direction.

    ``timeframe`` / ``label_horizon`` override module defaults so 15m transfers can
    reuse this stitch without a second simulator path. Touch TF follows
    ``touch_timeframe`` (15m→1m for ETH).
    """
    tf = str(timeframe or TIMEFRAME)
    sym = str(symbol or SYMBOL)
    label_h = int(label_horizon if label_horizon is not None else LABEL_HORIZON)
    if "bar_ms" not in cfg:
        cfg = {**cfg, "bar_ms": int(TF_MS[tf])}
    ohlcv = load_ohlcv(sym, tf)
    lock = pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < int(lock.value // 1_000_000)].copy()
    feats = build_space(ohlcv, SPACE, symbol=sym, timeframe=tf)
    y = build_direction_labels(ohlcv, horizon=label_h)["direction"]
    aligned = feats.join(y.rename("y"), how="inner").dropna()
    cols = [c for c in aligned.columns if c != "y"]
    X = aligned[cols].to_numpy(dtype=float)
    yv = aligned["y"].to_numpy(dtype=float)
    ts_ms = index_to_ms(aligned.index)
    folds = build_outer_folds(ts_ms, purge_bars=label_h, embargo_bars=label_h)
    touch = load_ohlcv(sym, touch_timeframe(tf, sym))
    touch_tf = touch_timeframe(tf, sym)
    funding = load_funding(sym)
    funding = funding[funding.index < lock]
    funding_ts = (funding.index.asi8 // 1_000_000).astype(np.int64)
    funding_rt = funding.to_numpy(dtype=float)
    lev = float(leverage_from_stop(SL))
    instrument = research_instrument(sym)
    family = target_family(TARGET)
    full_close = ohlcv["close"].to_numpy(dtype=float)
    full_ts = index_to_ms(ohlcv.index)
    ts_to_i = {int(t): i for i, t in enumerate(full_ts)}

    fold_rows: list[dict[str, Any]] = []
    all_pnls: list[float] = []
    all_trades: list[Any] = []
    all_tp: list[float] = []
    sig_book: dict[int, int] = {}
    exit_counts: dict[str, int] = {}
    total_stats = {
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_cap": 0,
        "n_skipped_loss_cooloff": 0,
        "n_skipped_weak_short_book1": 0,
        "n_primary": 0,
        "n_addon": 0,
    }
    n_liq = 0
    sharpe_vals: list[float] = []

    for fold in folds:
        tr, oos = fold.train_indices, fold.oos_indices
        model = LGBMRegressorPredictor(n_estimators=80, learning_rate=0.05)
        model.fit(X[tr], yv[tr])
        pred = model.predict(X[oos])
        mean = np.asarray(pred.mean, dtype=float).reshape(-1)
        side = proxy_side(mean, family)
        oos_ts = ts_ms[oos]
        close_oos = ohlcv["close"].reindex(aligned.index).to_numpy(dtype=float)[oos]
        sigs, stats = build_multitrade_signals(
            oos_ts, side, mean, cfg=cfg, close=close_oos
        )
        for s in sigs:
            sig_book[int(s.ts_ms)] = int((s.meta or {}).get("book_idx", 0) or 0)
            all_tp.append(float(s.target_offset))
        for k in total_stats:
            total_stats[k] += int(stats.get(k, 0))

        oos0, oos1 = aligned.index[oos[0]], aligned.index[oos[-1]]
        pad = max(50, int(cfg["hold_addon"]) * 4)
        pos = int(ohlcv.index.searchsorted(oos0))
        window = ohlcv.loc[ohlcv.index[max(0, pos - pad)] : oos1]
        end, start = window.index[-1], window.index[0]
        dec_ms = int(TF_MS[tf])
        touch_end = end + pd.Timedelta(milliseconds=dec_ms) - pd.Timedelta(milliseconds=1)
        touch_win = touch.loc[(touch.index >= start) & (touch.index <= touch_end)]
        w_ts = index_to_ms(window.index)
        fmask = (funding_ts >= int(w_ts[0])) & (funding_ts <= int(w_ts[-1]))
        bundle = run_strategy_backtest(
            window,
            sigs,
            symbol=sym,
            timeframe=tf,
            strategy_id=f"{label}-f{fold.fold_index}",
            touch_ohlcv=touch_win,
            touch_timeframe=touch_tf,
            costs=research_costs_baseline(),
            margin=research_margin(leverage=lev),
            sizing=research_sizing(),
            sim=research_sim_hedge(
                max_hold_bars=int(cfg["hold_addon"]),
                decision_timeframe=tf,
                max_positions_per_side=int(cfg["max_positions_per_side"]),
                max_positions_per_symbol=int(cfg["max_positions_per_side"]) * 2,
            ),
            instrument=instrument,
            funding_ts_ms=funding_ts[fmask],
            funding_rate=funding_rt[fmask],
            strategy_meta={"name": label, "timeframe": tf, "label_horizon": label_h},
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
        sh = getattr(m, "sharpe", None)
        if sh is not None:
            try:
                sharpe_vals.append(
                    float(getattr(sh, "annualised", getattr(sh, "annualized", float("nan"))))
                )
            except Exception:  # noqa: BLE001
                pass
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
                "expectancy_return_units": float(
                    getattr(m, "expectancy_return_units", float("nan"))
                ),
                "signal_stats": stats,
                "n_liquidations": int(getattr(m, "n_liquidations", 0) or 0),
            }
        )

    wins = sum(1 for p in all_pnls if p > 0)
    exp_num = 0.0
    exp_den = 0.0
    for fr in fold_rows:
        n = float(fr.get("n_trades") or 0)
        eru = fr.get("expectancy_return_units")
        if n > 0 and eru is not None and np.isfinite(float(eru)):
            exp_num += float(eru) * n
            exp_den += n
    trade_eru = (
        float(
            np.nanmean(
                [float(getattr(t, "return_units", float("nan"))) for t in all_trades]
            )
        )
        if all_trades
        else float("nan")
    )
    return {
        "label": label,
        "timeframe": tf,
        "symbol": sym,
        "label_horizon": label_h,
        "touch_timeframe": touch_tf,
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
                "mean_lookback",
                "bar_ms",
            )
            if k in cfg
        }
        | {
            "cooloff_after_consecutive_losses": int(
                cfg.get("cooloff_after_consecutive_losses", 0) or 0
            ),
            "strength_quantile": float(cfg.get("strength_quantile", 0.5) or 0.5),
            "skip_weak_short_book1": bool(cfg.get("skip_weak_short_book1", False)),
            "geometry": str(cfg.get("geometry") or ""),
            "tp_scale_by_abs_mean": bool(cfg.get("tp_scale_by_abs_mean", False)),
            "tp_scale_ref": float(cfg.get("tp_scale_ref", 0.5) or 0.5),
            "tp_scale_factor_min": float(cfg.get("tp_scale_factor_min", 1.0) or 1.0),
            "tp_scale_factor_max": float(cfg.get("tp_scale_factor_max", 2.0) or 2.0),
        },
        "folds": fold_rows,
        "stitched": {
            "n_trades": len(all_pnls),
            "net_pnl": float(np.nansum(all_pnls)),
            "profit_factor": pf(all_pnls),
            "win_rate": float(wins / len(all_pnls)) if all_pnls else float("nan"),
            "expectancy_return_units": (
                (exp_num / exp_den) if exp_den else trade_eru
            ),
            "expectancy_return_units_trade_mean": trade_eru,
            "sharpe_annualised_fold_mean": (
                float(np.nanmean(sharpe_vals)) if sharpe_vals else float("nan")
            ),
            "n_liquidations": int(n_liq),
            "mean_tp_pct": float(np.nanmean(all_tp)) if all_tp else float("nan"),
            "median_tp_pct": float(np.nanmedian(all_tp)) if all_tp else float("nan"),
            "frac_folds_pf_gt_1": float(
                np.mean([r["profit_factor"] > 1 for r in fold_rows])
            )
            if fold_rows
            else float("nan"),
        },
        "signal_stats_total": total_stats,
        "exit_reasons": exit_counts,
        "book1_wrong_way_next_bar": book1_wrong_way_1h(
            all_trades, sig_book=sig_book, close=full_close, ts_to_i=ts_to_i
        ),
        "leverage": lev,
    }
