"""Emit concurrent Signals when direction signals cluster in a short window.

Used for research only: approximate open-book lifecycle with max-hold so the
signal gate stays causal and conservative (TP/SL early exits free slots sooner
in the real sim than this gate assumes).
"""

from __future__ import annotations

from typing import Any

import numpy as np

from tradesim.ensure_source import prefer_botsgeneral_tradesim

prefer_botsgeneral_tradesim()

from tradesim import Side, Signal  # noqa: E402
from tradesim.contracts import InstrumentSpec  # noqa: E402
from tradesim.sizing import minimum_executable_qty  # noqa: E402

from llm2.live.multitrade import (  # noqa: E402
    MEAN_LOOKBACK,
    mean_strength_ok,
    scale_size_mult_by_abs_mean,
    scale_tp_by_abs_mean,
)
from llm2.signals.singlebook_clarity import SingleBookArm  # noqa: E402

BAR_MS_1H = 3_600_000


def build_cluster_concurrent_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    *,
    arm: SingleBookArm,
    min_edge: float,
    max_per_side: int,
    cluster_bars: int | None,
    lookback: int = MEAN_LOOKBACK,
    bar_ms: int = BAR_MS_1H,
    strength_quantile: float = 0.5,
) -> tuple[list[Signal], dict[str, Any]]:
    """Primary mean_strength (if configured) + up to K same-side concurrent books.

    ``cluster_bars``: when not None, book 2+ requires the new signal to fall within
    ``cluster_bars`` bars of the previous *emitted* same-side entry. ``None`` means
    always allow add-ons while under the cap.
    """
    k = max(1, int(max_per_side))
    strength_hist: list[float] = []
    # per-side open books as exit_ts_ms (max-hold approx)
    open_exit: dict[int, list[int]] = {1: [], -1: []}
    last_entry_ts: dict[int, int | None] = {1: None, -1: None}
    stats: dict[str, Any] = {
        "n_candidates": 0,
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_edge": 0,
        "n_skipped_cap": 0,
        "n_skipped_cluster": 0,
        "n_primary": 0,
        "n_addon": 0,
        "max_per_side": k,
        "cluster_bars": cluster_bars,
    }
    out: list[Signal] = []
    side_a = np.asarray(side, dtype=int)
    mean_a = np.asarray(mean, dtype=float)
    hold_ms = int(arm.horizon_bars) * int(bar_ms)
    cluster_ms = None if cluster_bars is None else int(cluster_bars) * int(bar_ms)

    for i in range(len(ts_ms)):
        s = int(side_a[i])
        m = float(mean_a[i])
        if s == 0:
            continue
        if not np.isfinite(m) or abs(m) < float(min_edge):
            stats["n_skipped_edge"] += 1
            continue
        stats["n_candidates"] += 1
        abs_m = abs(m)
        ts = int(ts_ms[i])

        # prune finished books (max-hold approx)
        open_exit[s] = [e for e in open_exit[s] if int(e) > ts]
        n_open = len(open_exit[s])

        if arm.clarity == "mean_strength":
            recent = strength_hist[-int(lookback) :] if strength_hist else []
            if not mean_strength_ok(abs_m, recent, strength_quantile=strength_quantile):
                stats["n_skipped_clarity"] += 1
                strength_hist.append(abs_m)
                continue

        if n_open >= k:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs_m)
            continue

        if n_open >= 1 and cluster_ms is not None:
            prev = last_entry_ts[s]
            if prev is None or (ts - int(prev)) > int(cluster_ms):
                stats["n_skipped_cluster"] += 1
                strength_hist.append(abs_m)
                continue

        book_idx = n_open + 1
        if book_idx == 1:
            stats["n_primary"] += 1
        else:
            stats["n_addon"] += 1

        out.append(
            Signal(
                ts_ms=ts,
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(arm.sl_pct),
                target_offset=float(arm.tp_pct),
                max_hold_bars=int(arm.horizon_bars),
                tag=f"k{k}_b{book_idx}_c{cluster_bars}",
                meta={
                    "pred_mean": float(m),
                    "abs_mean": float(abs_m),
                    "book_idx": book_idx,
                    "max_per_side": k,
                    "cluster_bars": cluster_bars,
                    "clarity": arm.clarity,
                    "tp_pct": arm.tp_pct,
                    "sl_pct": arm.sl_pct,
                    "horizon_bars": arm.horizon_bars,
                },
            )
        )
        open_exit[s].append(ts + hold_ms)
        last_entry_ts[s] = ts
        strength_hist.append(abs_m)
        stats["n_emitted"] += 1

    return out, stats


def build_cluster_size_signals(
    ts_ms: np.ndarray,
    side: np.ndarray,
    mean: np.ndarray,
    close: np.ndarray,
    *,
    arm: SingleBookArm,
    min_edge: float,
    max_per_side: int,
    instrument: InstrumentSpec,
    size_double_within_bars: int = 3,
    lookback: int = MEAN_LOOKBACK,
    bar_ms: int = BAR_MS_1H,
    strength_quantile: float = 0.5,
    cooloff_after_consecutive_losses: int = 0,
    cooloff_pause_bars: int | None = None,
    tp_scale_by_abs_mean: bool = False,
    tp_scale_ref: float = 0.5,
    tp_scale_factor_min: float = 1.0,
    tp_scale_factor_max: float = 2.0,
    size_scale_by_abs_mean: bool = False,
    size_scale_ref: float = 0.5,
    size_scale_factor_min: float = 1.0,
    size_scale_factor_max: float = 2.0,
) -> tuple[list[Signal], dict[str, Any]]:
    """Concurrent books up to K; optional time double + strength size scale.

    Always allows add-ons under the cap (no cluster *skip* gate). Size doubling is
    causal: uses only the previous emitted same-side entry timestamp.

    ``cooloff_after_consecutive_losses``: when >0, skip new entries for
    ``cooloff_pause_bars`` (default = arm.horizon_bars) after a causal max-hold
    proxy marks ≥N consecutive closed losses.

    ``tp_scale_by_abs_mean``: when True, TP = base × clip(|mean|/ref, min, max).
    ``size_scale_by_abs_mean``: when True, multiply size_mult by
    clip(|mean|/size_scale_ref, min, max) (on top of time-based 1×/2× if enabled).
    """
    k = max(1, int(max_per_side))
    strength_hist: list[float] = []
    open_exit: dict[int, list[int]] = {1: [], -1: []}
    last_entry_ts: dict[int, int | None] = {1: None, -1: None}
    # open approx books: (exit_ts, side, entry_px)
    open_books: list[tuple[int, int, float]] = []
    consecutive_losses = 0
    cooloff_n = max(0, int(cooloff_after_consecutive_losses))
    pause_bars = int(
        cooloff_pause_bars if cooloff_pause_bars is not None else arm.horizon_bars
    )
    cooloff_until_ts = -1
    stats: dict[str, Any] = {
        "n_candidates": 0,
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_edge": 0,
        "n_skipped_cap": 0,
        "n_skipped_loss_cooloff": 0,
        "n_primary": 0,
        "n_addon": 0,
        "n_size_1x": 0,
        "n_size_2x": 0,
        "n_size_strength_scaled": 0,
        "mean_size_mult": 0.0,
        "max_per_side": k,
        "size_double_within_bars": int(size_double_within_bars),
        "strength_quantile": float(strength_quantile),
        "cooloff_after_consecutive_losses": cooloff_n,
        "cooloff_pause_bars": pause_bars,
        "tp_scale_by_abs_mean": bool(tp_scale_by_abs_mean),
        "size_scale_by_abs_mean": bool(size_scale_by_abs_mean),
        "size_scale_ref": float(size_scale_ref),
        "size_scale_factor_min": float(size_scale_factor_min),
        "size_scale_factor_max": float(size_scale_factor_max),
    }
    out: list[Signal] = []
    size_mult_sum = 0.0
    size_mult_n = 0
    side_a = np.asarray(side, dtype=int)
    mean_a = np.asarray(mean, dtype=float)
    close_a = np.asarray(close, dtype=float)
    hold_ms = int(arm.horizon_bars) * int(bar_ms)
    double_ms = int(size_double_within_bars) * int(bar_ms)
    pause_ms = int(pause_bars) * int(bar_ms)

    for i in range(len(ts_ms)):
        s = int(side_a[i])
        m = float(mean_a[i])
        ts = int(ts_ms[i])
        px = float(close_a[i]) if np.isfinite(close_a[i]) else float("nan")

        # settle matured max-hold proxies with current (and only then) bar time
        if cooloff_n > 0 and np.isfinite(px) and px > 0:
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

        if s == 0:
            continue
        if not np.isfinite(m) or abs(m) < float(min_edge):
            stats["n_skipped_edge"] += 1
            continue
        stats["n_candidates"] += 1
        abs_m = abs(m)
        if not np.isfinite(px) or px <= 0:
            stats["n_skipped_edge"] += 1
            continue

        open_exit[s] = [e for e in open_exit[s] if int(e) > ts]
        n_open = len(open_exit[s])

        if arm.clarity == "mean_strength":
            recent = strength_hist[-int(lookback) :] if strength_hist else []
            if not mean_strength_ok(abs_m, recent, strength_quantile=strength_quantile):
                stats["n_skipped_clarity"] += 1
                strength_hist.append(abs_m)
                continue

        if cooloff_n > 0 and ts < int(cooloff_until_ts):
            stats["n_skipped_loss_cooloff"] += 1
            strength_hist.append(abs_m)
            continue

        if n_open >= k:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs_m)
            continue

        prev = last_entry_ts[s]
        in_cluster = prev is not None and (ts - int(prev)) <= int(double_ms)
        time_mult = 2.0 if (int(size_double_within_bars) > 0 and in_cluster) else 1.0
        strength_mult = 1.0
        if size_scale_by_abs_mean:
            strength_mult = scale_size_mult_by_abs_mean(
                abs_m,
                ref=float(size_scale_ref),
                factor_min=float(size_scale_factor_min),
                factor_max=float(size_scale_factor_max),
            )
            stats["n_size_strength_scaled"] += 1
        size_mult = float(time_mult) * float(strength_mult)
        min_q = float(minimum_executable_qty(instrument, px))

        book_idx = n_open + 1
        if book_idx == 1:
            stats["n_primary"] += 1
        else:
            stats["n_addon"] += 1
        if abs(size_mult - 2.0) < 1e-12 and not size_scale_by_abs_mean:
            stats["n_size_2x"] += 1
        elif abs(size_mult - 1.0) < 1e-12 and not size_scale_by_abs_mean:
            stats["n_size_1x"] += 1
        elif size_mult >= 2.0 - 1e-12:
            stats["n_size_2x"] += 1
        else:
            stats["n_size_1x"] += 1
        size_mult_sum += size_mult
        size_mult_n += 1

        tp_use = float(arm.tp_pct)
        if tp_scale_by_abs_mean:
            tp_use = scale_tp_by_abs_mean(
                tp_use,
                abs_m,
                ref=float(tp_scale_ref),
                factor_min=float(tp_scale_factor_min),
                factor_max=float(tp_scale_factor_max),
            )

        out.append(
            Signal(
                ts_ms=ts,
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(arm.sl_pct),
                target_offset=float(tp_use),
                max_hold_bars=int(arm.horizon_bars),
                # qty left unset so SizingConfig (MIN_EXCHANGE or equity×leverage) owns size;
                # size_mult scales the engine qty (time double × strength scale).
                tag=f"k{k}_b{book_idx}_x{size_mult:.3f}",
                meta={
                    "pred_mean": float(m),
                    "abs_mean": float(abs_m),
                    "book_idx": book_idx,
                    "max_per_side": k,
                    "size_mult": float(size_mult),
                    "time_size_mult": float(time_mult),
                    "strength_size_mult": float(strength_mult),
                    "size_double_within_bars": int(size_double_within_bars),
                    "size_scale_by_abs_mean": bool(size_scale_by_abs_mean),
                    "min_qty_ref": min_q,
                    "clarity": arm.clarity,
                    "tp_pct": float(tp_use),
                    "tp_base": float(arm.tp_pct),
                    "sl_pct": arm.sl_pct,
                    "horizon_bars": arm.horizon_bars,
                    "cooloff_after_consecutive_losses": cooloff_n,
                },
            )
        )
        open_exit[s].append(ts + hold_ms)
        last_entry_ts[s] = ts
        if cooloff_n > 0:
            open_books.append((ts + hold_ms, s, px))
        strength_hist.append(abs_m)
        stats["n_emitted"] += 1

    if size_mult_n > 0:
        stats["mean_size_mult"] = float(size_mult_sum / size_mult_n)
    return out, stats
