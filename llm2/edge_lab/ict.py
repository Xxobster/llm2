"""Inner Circle Trader / Smart Money Concepts primitives (causal).

Implements the computable core of the concepts Michael J. Huddleston popularised,
plus the exact three-bar Fair Value Gap definition used by the TradingView
indicator *FVG (Nephew_Sam_)*:

* **Fair Value Gap (FVG)** — a three-candle imbalance. Bullish when
  ``low[i] > high[i-2]``: price moved up so fast that the range between
  ``high[i-2]`` and ``low[i]`` was skipped. Bearish is the mirror,
  ``high[i] < low[i-2]``. Known at the close of bar ``i``.
* **Consequent encroachment (CE)** — the midpoint of the gap, the level ICT
  treats as the gap's fair value.
* **Mitigation / fill** — the Nephew Sam indicator offers two modes: a wick
  touching the far edge, or a candle *closing* through it. Both are provided.
* **Inverse Fair Value Gap (iFVG)** — once price closes through a gap, the zone
  flips polarity: a spent bullish gap becomes resistance.
* **Market structure** — break of structure and change of character from
  right-confirmed fractal swings.
* **Order block** — the last opposite-colour candle before the displacement that
  broke structure.
* **Premium / discount** — position of price inside the current dealing range.

Causality
---------
Swings come from ``indicators.swings.find_swings``, which confirms a pivot only
after its right-hand bars have closed, and every level is joined as-of the
confirmation instant. Gap zones are written forward from the bar that created
them. Nothing looks ahead.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagonal_sr.geometry import _wilder_atr, swings_from_ohlcv

DEFAULT_MIN_GAP_ATR = 0.10
DEFAULT_MAX_AGE_BARS = 400
CE_TOUCH_ATR = 0.25


def _first_true_after(flags: np.ndarray, start: int, stop: int) -> int:
    """Index of the first True in ``flags[start:stop]``, else ``stop``."""
    if start >= stop:
        return stop
    window = flags[start:stop]
    hit = int(np.argmax(window))
    return start + hit if bool(window[hit]) else stop


def _gap_zones(
    *,
    created: np.ndarray,
    top: np.ndarray,
    bottom: np.ndarray,
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    bullish: bool,
    fill_mode: str,
    max_age_bars: int,
) -> dict[str, np.ndarray]:
    """Forward-project each gap until it is mitigated; keep the most recent one.

    Returns per-bar arrays for the newest still-active zone of this polarity,
    plus the inverted (iFVG) zone left behind when a gap is closed through.
    """
    n = len(close)
    z_top = np.full(n, np.nan)
    z_bot = np.full(n, np.nan)
    z_age = np.full(n, np.nan)
    z_created = np.full(n, np.nan)
    inv_top = np.full(n, np.nan)
    inv_bot = np.full(n, np.nan)
    inv_age = np.full(n, np.nan)

    idxs = np.flatnonzero(created)
    for c in idxs:
        t = float(top[c])
        b = float(bottom[c])
        if not (np.isfinite(t) and np.isfinite(b)):
            continue
        limit = min(n, c + 1 + int(max_age_bars))
        # A gap is *filled* at its far edge, not on first contact. A bullish gap
        # sits below price, so its far edge is the bottom; a bearish gap sits
        # above price, so its far edge is the top. Entering the gap only starts
        # the test — that is what makes a consequent-encroachment entry possible.
        if bullish:
            touched = low <= b if fill_mode == "wick" else close < b
            through = close < b
        else:
            touched = high >= t if fill_mode == "wick" else close > t
            through = close > t
        end = _first_true_after(touched, c + 1, limit)
        if end > c + 1:
            rng = np.arange(c + 1, end)
            z_top[rng] = t
            z_bot[rng] = b
            z_created[rng] = c
            z_age[rng] = rng - c
        # Inversion: after a close through the far edge the zone flips polarity.
        thr = _first_true_after(through, c + 1, limit)
        if thr < limit:
            inv_end = min(n, thr + 1 + int(max_age_bars))
            rng2 = np.arange(thr + 1, inv_end)
            if rng2.size:
                inv_top[rng2] = t
                inv_bot[rng2] = b
                inv_age[rng2] = rng2 - thr
    return {
        "top": z_top,
        "bottom": z_bot,
        "age": z_age,
        "created_at": z_created,
        "inv_top": inv_top,
        "inv_bottom": inv_bot,
        "inv_age": inv_age,
    }


def fvg_frame(
    ohlcv: pd.DataFrame,
    *,
    min_gap_atr: float = DEFAULT_MIN_GAP_ATR,
    fill_mode: str = "wick",
    max_age_bars: int = DEFAULT_MAX_AGE_BARS,
    atr_period: int = 14,
) -> pd.DataFrame:
    """Fair Value Gap / inverse Fair Value Gap state per bar."""
    if fill_mode not in {"wick", "close"}:
        raise ValueError("fill_mode must be 'wick' or 'close'")
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    atr = _wilder_atr(high, low, close, period=atr_period)
    atr_safe = np.where(np.isfinite(atr) & (atr > 0), atr, np.nan)
    n = len(close)

    h2 = np.full(n, np.nan)
    l2 = np.full(n, np.nan)
    h2[2:] = high[:-2]
    l2[2:] = low[:-2]

    bull_raw = low > h2
    bear_raw = high < l2
    bull_size = np.where(bull_raw, low - h2, np.nan)
    bear_size = np.where(bear_raw, l2 - high, np.nan)
    big = float(min_gap_atr)
    bull_new = bull_raw & (bull_size >= big * atr_safe)
    bear_new = bear_raw & (bear_size >= big * atr_safe)

    bull = _gap_zones(
        created=bull_new,
        top=low,
        bottom=h2,
        high=high,
        low=low,
        close=close,
        bullish=True,
        fill_mode=fill_mode,
        max_age_bars=max_age_bars,
    )
    bear = _gap_zones(
        created=bear_new,
        top=l2,
        bottom=high,
        high=high,
        low=low,
        close=close,
        bullish=False,
        fill_mode=fill_mode,
        max_age_bars=max_age_bars,
    )

    out = pd.DataFrame(index=ohlcv.index)
    out["fvg_bull_new"] = bull_new.astype(float)
    out["fvg_bear_new"] = bear_new.astype(float)
    out["fvg_bull_new_size_atr"] = np.where(bull_new, bull_size / atr_safe, np.nan)
    out["fvg_bear_new_size_atr"] = np.where(bear_new, bear_size / atr_safe, np.nan)

    for label, zone in (("bull", bull), ("bear", bear)):
        top = zone["top"]
        bot = zone["bottom"]
        ce = (top + bot) / 2.0
        out[f"fvg_{label}_top"] = top
        out[f"fvg_{label}_bottom"] = bot
        out[f"fvg_{label}_ce"] = ce
        out[f"fvg_{label}_age"] = zone["age"]
        out[f"fvg_{label}_size_atr"] = (top - bot) / atr_safe
        out[f"fvg_{label}_active"] = np.isfinite(top).astype(float)
        out[f"dist_fvg_{label}_top_atr"] = (close - top) / atr_safe
        out[f"dist_fvg_{label}_bottom_atr"] = (close - bot) / atr_safe
        out[f"dist_fvg_{label}_ce_atr"] = (close - ce) / atr_safe
        out[f"in_fvg_{label}"] = (
            np.isfinite(top) & (close <= top) & (close >= bot)
        ).astype(float)
        out[f"touch_fvg_{label}"] = (
            np.isfinite(top) & (low <= top) & (high >= bot)
        ).astype(float)
        out[f"at_fvg_{label}_ce"] = (
            np.isfinite(ce) & (np.abs(close - ce) <= CE_TOUCH_ATR * atr_safe)
        ).astype(float)

        # Inverted zone: a spent bullish gap acts bearish, and vice versa.
        inv_top = zone["inv_top"]
        inv_bot = zone["inv_bottom"]
        inv_label = "bear" if label == "bull" else "bull"
        out[f"ifvg_{inv_label}_top"] = inv_top
        out[f"ifvg_{inv_label}_bottom"] = inv_bot
        out[f"ifvg_{inv_label}_age"] = zone["inv_age"]
        out[f"ifvg_{inv_label}_active"] = np.isfinite(inv_top).astype(float)
        out[f"dist_ifvg_{inv_label}_top_atr"] = (close - inv_top) / atr_safe
        out[f"dist_ifvg_{inv_label}_bottom_atr"] = (close - inv_bot) / atr_safe
        out[f"in_ifvg_{inv_label}"] = (
            np.isfinite(inv_top) & (close <= inv_top) & (close >= inv_bot)
        ).astype(float)
    return out


def _asof_last_two(
    swings: pd.DataFrame, index: pd.DatetimeIndex, kind: str
) -> tuple[np.ndarray, np.ndarray]:
    """Price of the last and previous confirmed swing of ``kind``, as-of each bar."""
    n = len(index)
    if swings.empty:
        return np.full(n, np.nan), np.full(n, np.nan)
    s = swings[swings["kind"] == kind].sort_values("confirm_ts_ms").reset_index(drop=True)
    if s.empty:
        return np.full(n, np.nan), np.full(n, np.nan)
    s["prev_price"] = s["price"].shift(1)
    left = pd.DataFrame(
        {
            "decision_at": pd.DatetimeIndex(index).tz_convert("UTC").as_unit("ns"),
            "ord": np.arange(n),
        }
    ).sort_values("decision_at")
    right = s.rename(columns={"confirm_ts_ms": "confirm_at"}).copy()
    right["confirm_at"] = pd.to_datetime(
        right["confirm_at"].to_numpy(dtype=np.int64), unit="ms", utc=True
    ).as_unit("ns")
    right = right.sort_values("confirm_at")
    merged = pd.merge_asof(
        left, right, left_on="decision_at", right_on="confirm_at", direction="backward"
    ).sort_values("ord")
    return (
        merged["price"].to_numpy(dtype=float),
        merged["prev_price"].to_numpy(dtype=float),
    )


def structure_frame(
    ohlcv: pd.DataFrame,
    *,
    left: int = 2,
    right: int = 2,
    atr_period: int = 14,
) -> pd.DataFrame:
    """Break of structure, change of character, dealing range and order blocks."""
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close = ohlcv["close"].to_numpy(dtype=float)
    open_ = ohlcv["open"].to_numpy(dtype=float)
    atr = _wilder_atr(high, low, close, period=atr_period)
    atr_safe = np.where(np.isfinite(atr) & (atr > 0), atr, np.nan)
    idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True)).as_unit("ns")
    n = len(close)

    sw = swings_from_ohlcv(ohlcv, left=left, right=right)
    sh, sh_prev = _asof_last_two(sw, idx, "high")
    sl, sl_prev = _asof_last_two(sw, idx, "low")

    bos_up = np.isfinite(sh) & (close > sh)
    bos_down = np.isfinite(sl) & (close < sl)
    higher_high = np.isfinite(sh_prev) & (sh > sh_prev)
    higher_low = np.isfinite(sl_prev) & (sl > sl_prev)
    lower_high = np.isfinite(sh_prev) & (sh < sh_prev)
    lower_low = np.isfinite(sl_prev) & (sl < sl_prev)
    bullish_structure = higher_high & higher_low
    bearish_structure = lower_high & lower_low

    # Only the first close beyond the level is the break (avoid a latched run).
    prev_bos_up = np.roll(bos_up, 1)
    prev_bos_up[0] = False
    prev_bos_down = np.roll(bos_down, 1)
    prev_bos_down[0] = False
    bos_up_first = bos_up & ~prev_bos_up
    bos_down_first = bos_down & ~prev_bos_down

    choch_up = bos_up_first & bearish_structure
    choch_down = bos_down_first & bullish_structure

    span = sh - sl
    span_safe = np.where(np.isfinite(span) & (np.abs(span) > 1e-12), span, np.nan)
    range_pos = (close - sl) / span_safe

    # Order block: most recent opposite-colour candle strictly before this bar.
    pos = np.arange(n)
    bear_candle = close < open_
    bull_candle = close > open_
    last_bear = np.maximum.accumulate(np.where(bear_candle, pos, -1))
    last_bull = np.maximum.accumulate(np.where(bull_candle, pos, -1))
    prev_last_bear = np.roll(last_bear, 1)
    prev_last_bear[0] = -1
    prev_last_bull = np.roll(last_bull, 1)
    prev_last_bull[0] = -1

    ob_bull_top = np.full(n, np.nan)
    ob_bull_bot = np.full(n, np.nan)
    ob_bear_top = np.full(n, np.nan)
    ob_bear_bot = np.full(n, np.nan)
    take_bull = bos_up_first & (prev_last_bear >= 0)
    take_bear = bos_down_first & (prev_last_bull >= 0)
    kb = prev_last_bear[take_bull]
    ob_bull_top[take_bull] = high[kb]
    ob_bull_bot[take_bull] = low[kb]
    kl = prev_last_bull[take_bear]
    ob_bear_top[take_bear] = high[kl]
    ob_bear_bot[take_bear] = low[kl]
    ob_bull_top = pd.Series(ob_bull_top).ffill().to_numpy()
    ob_bull_bot = pd.Series(ob_bull_bot).ffill().to_numpy()
    ob_bear_top = pd.Series(ob_bear_top).ffill().to_numpy()
    ob_bear_bot = pd.Series(ob_bear_bot).ffill().to_numpy()

    out = pd.DataFrame(index=ohlcv.index)
    out["atr"] = atr
    out["atr_frac"] = atr / np.where(close > 0, close, np.nan)
    out["swing_high"] = sh
    out["swing_low"] = sl
    out["dist_swing_high_atr"] = (close - sh) / atr_safe
    out["dist_swing_low_atr"] = (close - sl) / atr_safe
    out["bos_up"] = bos_up_first.astype(float)
    out["bos_down"] = bos_down_first.astype(float)
    out["choch_up"] = choch_up.astype(float)
    out["choch_down"] = choch_down.astype(float)
    out["bullish_structure"] = bullish_structure.astype(float)
    out["bearish_structure"] = bearish_structure.astype(float)
    out["range_pos"] = range_pos
    out["dealing_range_atr"] = span / atr_safe
    out["in_premium"] = (range_pos > 0.5).astype(float)
    out["in_discount"] = (range_pos < 0.5).astype(float)
    out["ob_bull_top"] = ob_bull_top
    out["ob_bull_bottom"] = ob_bull_bot
    out["ob_bear_top"] = ob_bear_top
    out["ob_bear_bottom"] = ob_bear_bot
    out["dist_ob_bull_top_atr"] = (close - ob_bull_top) / atr_safe
    out["dist_ob_bear_bottom_atr"] = (close - ob_bear_bot) / atr_safe
    out["in_ob_bull"] = (
        np.isfinite(ob_bull_top) & (low <= ob_bull_top) & (high >= ob_bull_bot)
    ).astype(float)
    out["in_ob_bear"] = (
        np.isfinite(ob_bear_top) & (high >= ob_bear_bot) & (low <= ob_bear_top)
    ).astype(float)
    return out


def ict_events(fvg: pd.DataFrame, structure: pd.DataFrame) -> pd.DataFrame:
    """Named entry events built from the gap and structure state."""
    close_above_ce = (fvg["at_fvg_bull_ce"].to_numpy() > 0.5) & (
        fvg["dist_fvg_bull_ce_atr"].to_numpy() >= 0.0
    )
    close_below_ce = (fvg["at_fvg_bear_ce"].to_numpy() > 0.5) & (
        fvg["dist_fvg_bear_ce_atr"].to_numpy() <= 0.0
    )
    touch_bull = fvg["touch_fvg_bull"].to_numpy() > 0.5
    touch_bear = fvg["touch_fvg_bear"].to_numpy() > 0.5
    in_ifvg_bull = fvg["in_ifvg_bull"].to_numpy() > 0.5
    in_ifvg_bear = fvg["in_ifvg_bear"].to_numpy() > 0.5

    discount = structure["in_discount"].to_numpy() > 0.5
    premium = structure["in_premium"].to_numpy() > 0.5
    bull_struct = structure["bullish_structure"].to_numpy() > 0.5
    bear_struct = structure["bearish_structure"].to_numpy() > 0.5
    ob_bull = structure["in_ob_bull"].to_numpy() > 0.5
    ob_bear = structure["in_ob_bear"].to_numpy() > 0.5
    choch_up = structure["choch_up"].to_numpy() > 0.5
    choch_down = structure["choch_down"].to_numpy() > 0.5

    ev = pd.DataFrame(index=fvg.index)
    ev["fvg_bull_ce_tag"] = (close_above_ce & touch_bull).astype(np.int8)
    ev["fvg_bear_ce_tag"] = (close_below_ce & touch_bear).astype(np.int8)
    ev["fvg_bull_ce_discount"] = (close_above_ce & touch_bull & discount).astype(np.int8)
    ev["fvg_bear_ce_premium"] = (close_below_ce & touch_bear & premium).astype(np.int8)
    ev["fvg_bull_with_structure"] = (close_above_ce & touch_bull & bull_struct).astype(np.int8)
    ev["fvg_bear_with_structure"] = (close_below_ce & touch_bear & bear_struct).astype(np.int8)
    ev["ifvg_bull_reclaim"] = (in_ifvg_bull & bull_struct).astype(np.int8)
    ev["ifvg_bear_reject"] = (in_ifvg_bear & bear_struct).astype(np.int8)
    ev["ob_bull_tap"] = (ob_bull & discount).astype(np.int8)
    ev["ob_bear_tap"] = (ob_bear & premium).astype(np.int8)
    ev["choch_up_fvg"] = (choch_up & (fvg["fvg_bull_new"].to_numpy() > 0.5)).astype(np.int8)
    ev["choch_down_fvg"] = (choch_down & (fvg["fvg_bear_new"].to_numpy() > 0.5)).astype(np.int8)
    return ev


ICT_EVENT_SIDE: dict[str, int] = {
    "fvg_bull_ce_tag": 1,
    "fvg_bear_ce_tag": -1,
    "fvg_bull_ce_discount": 1,
    "fvg_bear_ce_premium": -1,
    "fvg_bull_with_structure": 1,
    "fvg_bear_with_structure": -1,
    "ifvg_bull_reclaim": 1,
    "ifvg_bear_reject": -1,
    "ob_bull_tap": 1,
    "ob_bear_tap": -1,
    "choch_up_fvg": 1,
    "choch_down_fvg": -1,
}
