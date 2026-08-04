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

from llm2.live.multitrade import MEAN_LOOKBACK, mean_strength_ok  # noqa: E402
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
            if not mean_strength_ok(abs_m, recent):
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
) -> tuple[list[Signal], dict[str, Any]]:
    """Concurrent books up to K; qty = 2× min-exchange if signal ≤ N bars after last entry.

    Always allows add-ons under the cap (no cluster *skip* gate). Size doubling is
    causal: uses only the previous emitted same-side entry timestamp.
    """
    k = max(1, int(max_per_side))
    strength_hist: list[float] = []
    open_exit: dict[int, list[int]] = {1: [], -1: []}
    last_entry_ts: dict[int, int | None] = {1: None, -1: None}
    stats: dict[str, Any] = {
        "n_candidates": 0,
        "n_emitted": 0,
        "n_skipped_clarity": 0,
        "n_skipped_edge": 0,
        "n_skipped_cap": 0,
        "n_primary": 0,
        "n_addon": 0,
        "n_size_1x": 0,
        "n_size_2x": 0,
        "max_per_side": k,
        "size_double_within_bars": int(size_double_within_bars),
    }
    out: list[Signal] = []
    side_a = np.asarray(side, dtype=int)
    mean_a = np.asarray(mean, dtype=float)
    close_a = np.asarray(close, dtype=float)
    hold_ms = int(arm.horizon_bars) * int(bar_ms)
    double_ms = int(size_double_within_bars) * int(bar_ms)

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
        px = float(close_a[i])
        if not np.isfinite(px) or px <= 0:
            stats["n_skipped_edge"] += 1
            continue

        open_exit[s] = [e for e in open_exit[s] if int(e) > ts]
        n_open = len(open_exit[s])

        if arm.clarity == "mean_strength":
            recent = strength_hist[-int(lookback) :] if strength_hist else []
            if not mean_strength_ok(abs_m, recent):
                stats["n_skipped_clarity"] += 1
                strength_hist.append(abs_m)
                continue

        if n_open >= k:
            stats["n_skipped_cap"] += 1
            strength_hist.append(abs_m)
            continue

        prev = last_entry_ts[s]
        in_cluster = prev is not None and (ts - int(prev)) <= int(double_ms)
        size_mult = 2 if in_cluster else 1
        min_q = float(minimum_executable_qty(instrument, px))
        qty = float(size_mult) * min_q

        book_idx = n_open + 1
        if book_idx == 1:
            stats["n_primary"] += 1
        else:
            stats["n_addon"] += 1
        if size_mult == 2:
            stats["n_size_2x"] += 1
        else:
            stats["n_size_1x"] += 1

        out.append(
            Signal(
                ts_ms=ts,
                side=Side.LONG if s > 0 else Side.SHORT,
                stop_offset=float(arm.sl_pct),
                target_offset=float(arm.tp_pct),
                max_hold_bars=int(arm.horizon_bars),
                qty=qty,
                tag=f"k{k}_b{book_idx}_x{size_mult}",
                meta={
                    "book_idx": book_idx,
                    "max_per_side": k,
                    "size_mult": size_mult,
                    "size_double_within_bars": int(size_double_within_bars),
                    "min_qty": min_q,
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
