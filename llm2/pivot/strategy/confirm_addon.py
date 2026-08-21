"""Causal pivot-shape confirmation: delay entry or add a second trade."""

from __future__ import annotations

from typing import Sequence

import numpy as np
import pandas as pd

from tradesim import Side, Signal
from tradesim.contracts import EntryOrder

from llm2.pivot.strategy.working_limit import LimitIntent
from llm2.validation.folds import index_to_ms


def pivot_shape_confirmed(
    *,
    is_short: bool,
    i_dec: int,
    k: int,
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
) -> bool:
    """True if the next ``k`` closed bars look like a confirmed pivot.

    ``k == 1``: close simply moved in the predicted direction.
    ``k >= 2``: extreme in the window is not the last bar, and last close reversed.
    """
    n = len(close)
    kk = int(k)
    if kk < 1 or i_dec < 0 or i_dec + kk >= n:
        return False
    i_conf = i_dec + kk
    if kk == 1:
        if is_short:
            return bool(close[i_conf] < close[i_dec])
        return bool(close[i_conf] > close[i_dec])
    i0 = i_dec + 1
    if is_short:
        wh = high[i0 : i_conf + 1]
        if wh.size < 2 or not np.isfinite(wh).any():
            return False
        j = int(np.nanargmax(wh))
        return bool(j < (wh.size - 1) and close[i_conf] < wh[j])
    wl = low[i0 : i_conf + 1]
    if wl.size < 2 or not np.isfinite(wl).any():
        return False
    j = int(np.nanargmin(wl))
    return bool(j < (wl.size - 1) and close[i_conf] > wl[j])


def delay_intents_until_confirm(
    ohlcv: pd.DataFrame,
    intents: Sequence[LimitIntent],
    *,
    confirm_k: int,
) -> tuple[list[LimitIntent], dict]:
    """Move the decision timestamp to the confirm bar when the shape rule passes."""
    bar_ts = index_to_ms(ohlcv.index)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    out: list[LimitIntent] = []
    n_drop = 0
    n_bad = 0
    for it in intents:
        i_dec = pos.get(int(it.decision_ts_ms))
        if i_dec is None:
            n_bad += 1
            continue
        ok = pivot_shape_confirmed(
            is_short=it.side == Side.SHORT,
            i_dec=i_dec,
            k=int(confirm_k),
            high=high,
            low=low,
            close=close,
        )
        if not ok:
            n_drop += 1
            continue
        i_conf = i_dec + int(confirm_k)
        meta = dict(it.meta or {})
        meta["confirm_k"] = int(confirm_k)
        meta["orig_decision_ts_ms"] = int(it.decision_ts_ms)
        out.append(
            LimitIntent(
                decision_ts_ms=int(bar_ts[i_conf]),
                side=it.side,
                limit_price=float(it.limit_price),
                stop_offset=float(it.stop_offset),
                target_offset=float(it.target_offset),
                max_hold_bars=int(it.max_hold_bars),
                work_bars=it.work_bars,
                meta=meta,
            )
        )
    stats = {
        "n_intent_in": len(intents),
        "n_confirmed": len(out),
        "n_dropped": n_drop,
        "n_bad": n_bad,
        "confirm_rate": float(len(out) / len(intents)) if intents else float("nan"),
        "confirm_k": int(confirm_k),
    }
    return out, stats


def addon_signals_after_fill(
    ohlcv: pd.DataFrame,
    filled: Sequence[Signal],
    *,
    confirm_k: int,
) -> tuple[list[Signal], dict]:
    """After a LIMIT fill, if K bars confirm, emit a same-side market add-on.

    Confirmation: last close is in-profit versus the fill limit, and the stop
    price was not touched in those K bars.
    """
    bar_ts = index_to_ms(ohlcv.index)
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    pos = {int(t): i for i, t in enumerate(bar_ts.tolist())}
    n = len(bar_ts)
    kk = int(confirm_k)
    out: list[Signal] = []
    n_drop = 0
    n_stop = 0
    n_bad = 0
    for sig in filled:
        # Signal is stamped on the bar before the touch/fill bar.
        i_sig = pos.get(int(sig.ts_ms))
        if i_sig is None:
            n_bad += 1
            continue
        i_fill = i_sig + 1
        i_conf = i_fill + kk
        if i_conf >= n or i_fill >= n:
            n_drop += 1
            continue
        lim = float(sig.limit_price) if sig.limit_price is not None else float(close[i_fill])
        sl = float(sig.stop_offset or 0.01)
        is_short = sig.side == Side.SHORT
        sl_px = lim * (1.0 + sl) if is_short else lim * (1.0 - sl)
        w0, w1 = i_fill + 1, i_conf + 1
        if w0 >= w1:
            n_drop += 1
            continue
        if is_short:
            stopped = bool(np.nanmax(high[w0:w1]) >= sl_px)
            in_profit = bool(close[i_conf] < lim)
        else:
            stopped = bool(np.nanmin(low[w0:w1]) <= sl_px)
            in_profit = bool(close[i_conf] > lim)
        if stopped:
            n_stop += 1
            continue
        if not in_profit:
            n_drop += 1
            continue
        meta = dict(sig.meta or {})
        size_mult = float(
            meta.get("addon_size_mult", meta.get("size_mult", 1.0)) or 1.0
        )
        meta["addon"] = True
        meta["confirm_k"] = kk
        meta["parent_ts_ms"] = int(sig.ts_ms)
        meta["size_mult"] = size_mult
        out.append(
            Signal(
                ts_ms=int(bar_ts[i_conf]),
                side=sig.side,
                stop_offset=float(sig.stop_offset or sl),
                target_offset=float(sig.target_offset or 0.01),
                max_hold_bars=int(sig.max_hold_bars or 6),
                entry_order=EntryOrder.MARKET,
                tag="pivot_confirm_addon",
                meta=meta,
            )
        )
    stats = {
        "n_parent_fills": len(filled),
        "n_addon": len(out),
        "n_stopped": n_stop,
        "n_dropped": n_drop,
        "n_bad": n_bad,
        "addon_rate": float(len(out) / len(filled)) if filled else float("nan"),
        "confirm_k": kk,
    }
    return out, stats
