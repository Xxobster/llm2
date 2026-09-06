"""Multi-timeframe swing structure primitives (wave-trading doctrine, made causal).

Ported from the concepts catalogued in ``C:\\projects\\wavetheory`` — a
knowledge-extraction project on a simplified Elliott-wave / cycle-structure
method. Its own rule proxy **failed** out of sample (profit factor 0.65-0.75 on
BTC/ETH/XRP, worse than buy-and-hold), and that backtest contained two defects
this module deliberately does not reproduce:

1. ``fractal_pivots`` + ``last_pivot_series`` exposed a pivot at the bar where it
   occurred, even though confirming it needs ``wing`` **later** bars — roughly a
   5-bar look-ahead on 1-hour data.
2. Higher-timeframe open/high/low/close was forward-filled onto lower-timeframe
   bars, injecting the **forming** higher-timeframe bar into every lower bar
   inside it.

So nothing numeric is inherited. What is inherited is the vocabulary, which is a
testable hypothesis about structure geometry:

- **bas** — a confirmed swing low; breaking it invalidates the bullish count
- **top** — a confirmed swing high; the natural take-profit
- **pullback** — a retrace of 25-78% of the impulse leg (bas to top)
- **higher-timeframe bias** — the higher timeframe sets direction, the lower
  timeframe times entry
- **invalidation** ("casser le bas") — first close below the active bas

Causality
---------
A pivot at bar ``i`` is knowable only at bar ``i + wing``, so every confirmed
extreme is shifted by ``wing`` before use. Higher-timeframe values are joined by
their **close** time with ``merge_asof(direction="backward")``, never
forward-filled from a forming bar.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.edge_lab.sessions import _wilder_atr

# Pullback band from the source doctrine: shallower is not a correction, deeper
# means the impulse leg is probably being retraced entirely.
PULLBACK_MIN = 0.25
PULLBACK_MAX = 0.78
# Fraction of the bar range the close must sit in to count as a confirming candle.
CLOSE_POS_CONFIRM = 0.55
# Buffer below the bas before a break counts as an invalidation.
BAS_BUFFER = 0.003

TF_MINUTES: dict[str, int] = {"5m": 5, "15m": 15, "1h": 60, "4h": 240, "1d": 1440}

STRUCTURE_EVENT_SIDE: dict[str, int] = {
    "wt_pullback_long": 1,
    "wt_pullback_short": -1,
    "wt_pullback_confirmed_long": 1,
    "wt_pullback_confirmed_short": -1,
    "wt_bas_break_short": -1,
    "wt_top_break_long": 1,
    "wt_htf_bias_pullback_long": 1,
    "wt_htf_bias_pullback_short": -1,
    "wt_hh_hl_continuation_long": 1,
    "wt_lh_ll_continuation_short": -1,
}


def confirmed_swings(
    high: pd.Series, low: pd.Series, *, wing: int
) -> tuple[pd.Series, pd.Series, pd.Series, pd.Series]:
    """Last and previous confirmed swing high / low, lagged by ``wing`` bars.

    A centered window finds the pivot, then ``shift(wing)`` delays publication
    until the right-hand bars have actually closed. This is the corrected
    version of the source project's backtest path.
    """
    win = 2 * int(wing) + 1
    is_high = high == high.rolling(win, center=True).max()
    is_low = low == low.rolling(win, center=True).min()

    pivot_high = high.where(is_high)
    pivot_low = low.where(is_low)

    last_high = pivot_high.ffill().shift(wing)
    last_low = pivot_low.ffill().shift(wing)
    # "Previous" = the confirmed pivot before the current one, same publication lag.
    prev_high = pivot_high.dropna().shift(1).reindex(high.index).ffill().shift(wing)
    prev_low = pivot_low.dropna().shift(1).reindex(low.index).ffill().shift(wing)
    return last_high, last_low, prev_high, prev_low


def structure_mtf_frame(
    ohlcv: pd.DataFrame,
    *,
    wing: int = 5,
    atr_period: int = 14,
    htf: str | None = None,
    htf_wing: int = 5,
) -> pd.DataFrame:
    """Causal swing-structure features, optionally with a higher-timeframe bias.

    ``htf`` is a pandas offset alias (``"4h"``, ``"1d"``). When given, the higher
    timeframe is resampled from the handed candles and joined on its close time,
    so a forming higher bar can never reach a lower bar.
    """
    high, low, close = ohlcv["high"], ohlcv["low"], ohlcv["close"]
    atr = pd.Series(
        _wilder_atr(high.to_numpy(), low.to_numpy(), close.to_numpy(), period=atr_period),
        index=ohlcv.index,
    )
    atr_safe = atr.replace(0.0, np.nan)

    top, bas, prev_top, prev_bas = confirmed_swings(high, low, wing=wing)

    out = pd.DataFrame(index=ohlcv.index)
    out["atr"] = atr
    out["atr_frac"] = atr / close.replace(0.0, np.nan)
    out["swing_top"] = top
    out["swing_bas"] = bas

    impulse = (top - bas).replace(0.0, np.nan)
    out["dist_to_top_atr"] = (top - close) / atr_safe
    out["dist_to_bas_atr"] = (close - bas) / atr_safe
    out["impulse_atr"] = impulse / atr_safe
    # 0 at the top, 1 back at the bas.
    depth = (top - close) / impulse
    out["pullback_depth"] = depth
    out["in_pullback_band"] = (
        (depth >= PULLBACK_MIN) & (depth <= PULLBACK_MAX)
    ).astype(float)
    # Mirror for shorts: depth measured up from the bas.
    depth_short = (close - bas) / impulse
    out["pullback_depth_short"] = depth_short
    out["in_pullback_band_short"] = (
        (depth_short >= PULLBACK_MIN) & (depth_short <= PULLBACK_MAX)
    ).astype(float)

    rng = (high - low).replace(0.0, np.nan)
    out["close_pos_in_bar"] = (close - low) / rng
    out["bas_intact"] = (close > bas * (1.0 + BAS_BUFFER)).astype(float)
    out["top_intact"] = (close < top * (1.0 - BAS_BUFFER)).astype(float)
    out["higher_high"] = (top > prev_top).astype(float)
    out["higher_low"] = (bas > prev_bas).astype(float)
    out["lower_high"] = (top < prev_top).astype(float)
    out["lower_low"] = (bas < prev_bas).astype(float)
    out["wt_bullish_structure"] = (out["higher_high"] * out["higher_low"]).astype(float)
    out["wt_bearish_structure"] = (out["lower_high"] * out["lower_low"]).astype(float)

    # First close through the confirmed level, not every bar beyond it.
    below = close < bas * (1.0 - BAS_BUFFER)
    above = close > top * (1.0 + BAS_BUFFER)
    out["bas_broken_first"] = (below & ~below.shift(1).fillna(False)).astype(float)
    out["top_broken_first"] = (above & ~above.shift(1).fillna(False)).astype(float)

    if htf:
        out = out.join(_htf_bias(ohlcv, htf=htf, wing=htf_wing))
    return out


def _resample_closed(ohlcv: pd.DataFrame, rule: str) -> pd.DataFrame:
    """Resample to ``rule`` keeping the bar **open** time as the index."""
    agg = ohlcv.resample(rule, label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last"}
    )
    return agg.dropna(subset=["close"])


def _htf_bias(ohlcv: pd.DataFrame, *, htf: str, wing: int) -> pd.DataFrame:
    """Higher-timeframe structure joined by close time (completed bars only)."""
    h = _resample_closed(ohlcv, htf)
    if len(h) < 2 * wing + 3:
        cols = [
            "htf_bas_intact",
            "htf_bullish_structure",
            "htf_bearish_structure",
            "htf_dist_to_bas_frac",
            "htf_dist_to_top_frac",
        ]
        return pd.DataFrame(np.nan, index=ohlcv.index, columns=cols)

    top, bas, prev_top, prev_bas = confirmed_swings(h["high"], h["low"], wing=wing)
    hc = h["close"]
    frame = pd.DataFrame(
        {
            "htf_bas_intact": (hc > bas * (1.0 + BAS_BUFFER)).astype(float),
            "htf_bullish_structure": ((top > prev_top) & (bas > prev_bas)).astype(float),
            "htf_bearish_structure": ((top < prev_top) & (bas < prev_bas)).astype(float),
            "htf_dist_to_bas_frac": (hc - bas) / hc.replace(0.0, np.nan),
            "htf_dist_to_top_frac": (top - hc) / hc.replace(0.0, np.nan),
        }
    )
    # A higher bar opening at T is only knowable once it closes at T + rule.
    frame = frame.copy()
    frame["_avail"] = h.index + pd.tseries.frequencies.to_offset(htf)

    joined = pd.merge_asof(
        pd.DataFrame(index=ohlcv.index).reset_index(names="_ts"),
        frame.reset_index(drop=True).sort_values("_avail"),
        left_on="_ts",
        right_on="_avail",
        direction="backward",
        allow_exact_matches=True,
    )
    joined.index = ohlcv.index
    return joined.drop(columns=["_ts", "_avail"])


def _first(mask: np.ndarray) -> np.ndarray:
    """Edge-trigger a state mask: fire only on the bar the state becomes true.

    ``in_pullback_band`` and the structure flags are *states* that stay true for
    as long as price sits in the zone. Firing on every such bar produced 320-3400
    "events" per month, which is not a trade decision. A trader acts when the
    condition is first met, so every state-based event is edge-triggered.
    """
    prev = np.empty_like(mask)
    prev[0] = False
    prev[1:] = mask[:-1]
    return mask & ~prev


def structure_mtf_events(frame: pd.DataFrame) -> dict[str, pd.Series]:
    """Named entry-event occurrence bits from the structure frame."""

    def b(col: str) -> np.ndarray:
        if col not in frame.columns:
            return np.zeros(len(frame), dtype=bool)
        return frame[col].fillna(0.0).to_numpy(dtype=float) > 0.5

    idx = frame.index
    band_l = b("in_pullback_band")
    band_s = b("in_pullback_band_short")
    bas_ok = b("bas_intact")
    top_ok = b("top_intact")
    close_pos = frame["close_pos_in_bar"].fillna(0.5).to_numpy(dtype=float)
    conf_l = close_pos >= CLOSE_POS_CONFIRM
    conf_s = close_pos <= (1.0 - CLOSE_POS_CONFIRM)
    bull = b("wt_bullish_structure")
    bear = b("wt_bearish_structure")
    htf_bull = b("htf_bullish_structure")
    htf_bear = b("htf_bearish_structure")

    # The pullback band itself is edge-triggered, then extra conditions are
    # required on that same trigger bar. This keeps "first entry into the zone"
    # semantics instead of re-firing once a later bar happens to confirm.
    enter_l = _first(band_l)
    enter_s = _first(band_s)

    ev = {
        "wt_pullback_long": enter_l & bas_ok,
        "wt_pullback_short": enter_s & top_ok,
        "wt_pullback_confirmed_long": enter_l & bas_ok & conf_l,
        "wt_pullback_confirmed_short": enter_s & top_ok & conf_s,
        "wt_bas_break_short": b("bas_broken_first"),
        "wt_top_break_long": b("top_broken_first"),
        "wt_htf_bias_pullback_long": enter_l & bas_ok & htf_bull,
        "wt_htf_bias_pullback_short": enter_s & top_ok & htf_bear,
        "wt_hh_hl_continuation_long": enter_l & bull & bas_ok,
        "wt_lh_ll_continuation_short": enter_s & bear & top_ok,
    }
    return {k: pd.Series(np.asarray(v, dtype=np.int8), index=idx) for k, v in ev.items()}


STRUCTURE_FEATURE_PREFIXES: tuple[str, ...] = (
    "atr_frac",
    "dist_to_top_atr",
    "dist_to_bas_atr",
    "impulse_atr",
    "pullback_depth",
    "in_pullback_band",
    "close_pos_in_bar",
    "bas_intact",
    "top_intact",
    "higher_high",
    "higher_low",
    "lower_high",
    "lower_low",
    "wt_bullish_structure",
    "wt_bearish_structure",
    "bas_broken_first",
    "top_broken_first",
    "htf_bas_intact",
    "htf_bullish_structure",
    "htf_bearish_structure",
    "htf_dist_to_bas_frac",
    "htf_dist_to_top_frac",
)


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    """Leakage-audit entry point for the multi-timeframe structure space."""
    frame = structure_mtf_frame(ohlcv, wing=5, htf="4h", htf_wing=5)
    keep = [
        c
        for c in frame.columns
        if any(c == p or c.startswith(p) for p in STRUCTURE_FEATURE_PREFIXES)
    ]
    return frame.reindex(columns=sorted(set(keep)))
