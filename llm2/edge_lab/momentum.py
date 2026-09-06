"""Momentum / breakout continuation primitives (Kristjan Kullamagi style, causal).

Kullamagi's published process is a sequence of filters rather than one indicator:

1. **A large prior move** — only trade names that have already run hard.
2. **A tight consolidation** — the range contracts and the moving averages
   converge while the prior move digests (his "3-4 week base", flag or wedge).
3. **A breakout of the consolidation high** with an expansion in volume.
4. **A stop at the consolidation low** or the prior bar's low, and a trailing
   exit on a short moving average, taking part of the position into strength.
5. **Average Daily Range percent** as a volatility screen, so the target is
   reachable relative to normal movement.

Ported here for a single perpetual on an intraday timeframe: the cross-sectional
relative-strength ranking is replaced by a **causal self-referential quantile**
(rolling window, shifted one bar), because a hunt over three symbols cannot rank
cross-sectionally without leaking.

Every threshold is a rolling quantile of the **past** only. No full-history
quantile, no centred window, no negative shift.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagonal_sr.geometry import _wilder_atr

PRIOR_MOVE_BARS: tuple[int, ...] = (30, 60, 90)
CONSOLIDATION_BARS: tuple[int, ...] = (10, 20, 40)
QUANTILE_WINDOW = 500


def _causal_quantile(series: pd.Series, *, window: int, q: float) -> pd.Series:
    """Rolling quantile of past bars only (shifted so bar t is excluded)."""
    return series.rolling(window, min_periods=window // 2).quantile(q).shift(1)


def momentum_frame(
    ohlcv: pd.DataFrame,
    *,
    atr_period: int = 14,
    quantile_window: int = QUANTILE_WINDOW,
) -> pd.DataFrame:
    """Prior-move, consolidation-tightness, moving-average and breakout state."""
    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close_a = ohlcv["close"].to_numpy(dtype=float)
    close = pd.Series(close_a, index=ohlcv.index)
    volume = pd.Series(ohlcv["volume"].to_numpy(dtype=float), index=ohlcv.index)

    atr = _wilder_atr(high, low, close_a, period=atr_period)
    atr_long = _wilder_atr(high, low, close_a, period=50)
    atr_safe = pd.Series(
        np.where(np.isfinite(atr) & (atr > 0), atr, np.nan), index=ohlcv.index
    )

    out = pd.DataFrame(index=ohlcv.index)
    out["atr"] = atr
    out["atr_frac"] = atr / np.where(close_a > 0, close_a, np.nan)
    # Average Daily Range percent, intraday analogue: mean bar range over 20 bars.
    bar_range_pct = pd.Series(
        (high - low) / np.where(close_a > 0, close_a, np.nan), index=ohlcv.index
    )
    out["adr_pct_20"] = bar_range_pct.rolling(20, min_periods=20).mean()
    out["atr_compression"] = atr / np.where(
        np.isfinite(atr_long) & (atr_long > 0), atr_long, np.nan
    )

    for n in PRIOR_MOVE_BARS:
        mv = close / close.shift(n) - 1.0
        out[f"prior_move_{n}"] = mv
        out[f"prior_move_{n}_q70"] = _causal_quantile(mv, window=quantile_window, q=0.70)
        out[f"prior_move_{n}_q30"] = _causal_quantile(mv, window=quantile_window, q=0.30)

    hi_s = pd.Series(high, index=ohlcv.index)
    lo_s = pd.Series(low, index=ohlcv.index)
    for w in CONSOLIDATION_BARS:
        roll_hi = hi_s.rolling(w, min_periods=w).max().shift(1)
        roll_lo = lo_s.rolling(w, min_periods=w).min().shift(1)
        tight = (roll_hi - roll_lo) / close.replace(0.0, np.nan)
        out[f"box_high_{w}"] = roll_hi
        out[f"box_low_{w}"] = roll_lo
        out[f"tightness_{w}"] = tight
        out[f"tightness_{w}_q30"] = _causal_quantile(
            tight, window=quantile_window, q=0.30
        )
        out[f"dist_box_high_{w}_atr"] = (close - roll_hi) / atr_safe
        out[f"dist_box_low_{w}_atr"] = (close - roll_lo) / atr_safe
        out[f"breakout_up_{w}"] = (close > roll_hi).astype(float)
        out[f"breakout_down_{w}"] = (close < roll_lo).astype(float)

    for span in (10, 20, 50):
        ema = close.ewm(span=span, adjust=False, min_periods=span).mean()
        out[f"ema{span}"] = ema
        out[f"dist_ema{span}_atr"] = (close - ema) / atr_safe
    out["ma_stack_up"] = (
        (out["ema10"] > out["ema20"]) & (out["ema20"] > out["ema50"])
    ).astype(float)
    out["ma_stack_down"] = (
        (out["ema10"] < out["ema20"]) & (out["ema20"] < out["ema50"])
    ).astype(float)
    ema_spread = (out["ema10"] - out["ema50"]).abs() / atr_safe
    out["ma_convergence_atr"] = ema_spread
    out["ma_convergence_q30"] = _causal_quantile(
        ema_spread, window=quantile_window, q=0.30
    )

    vol_mean = volume.rolling(20, min_periods=20).mean().shift(1)
    vol_std = volume.rolling(20, min_periods=20).std().shift(1)
    out["vol_expansion"] = volume / vol_mean.replace(0.0, np.nan)
    out["vol_z_20"] = (volume - vol_mean) / vol_std.replace(0.0, np.nan)

    body = close_a - ohlcv["open"].to_numpy(dtype=float)
    rng = np.where((high - low) > 0, high - low, np.nan)
    out["close_pos_in_bar"] = (close_a - low) / rng
    out["body_frac_of_range"] = np.abs(body) / rng
    out["bar_range_atr"] = (high - low) / atr_safe
    return out


def momentum_events(mom: pd.DataFrame) -> pd.DataFrame:
    """Named breakout / ignition events."""
    ev = pd.DataFrame(index=mom.index)

    def _f(col: str) -> np.ndarray:
        return mom[col].to_numpy(dtype=float)

    strong_up = _f("prior_move_60") > _f("prior_move_60_q70")
    strong_down = _f("prior_move_60") < _f("prior_move_60_q30")
    tight20 = _f("tightness_20") < _f("tightness_20_q30")
    tight40 = _f("tightness_40") < _f("tightness_40_q30")
    converged = _f("ma_convergence_atr") < _f("ma_convergence_q30")
    vol_exp = _f("vol_expansion") > 1.5
    bo_up20 = _f("breakout_up_20") > 0.5
    bo_dn20 = _f("breakout_down_20") > 0.5
    bo_up40 = _f("breakout_up_40") > 0.5
    bo_dn40 = _f("breakout_down_40") > 0.5
    stack_up = _f("ma_stack_up") > 0.5
    stack_dn = _f("ma_stack_down") > 0.5

    # Ignition ("episodic pivot" analogue): an outsized, well-closed, high-volume bar.
    ignite_up = (
        (_f("bar_range_atr") > 2.5)
        & (_f("close_pos_in_bar") > 0.75)
        & (_f("vol_z_20") > 2.0)
    )
    ignite_down = (
        (_f("bar_range_atr") > 2.5)
        & (_f("close_pos_in_bar") < 0.25)
        & (_f("vol_z_20") > 2.0)
    )

    ev["momo_breakout_long"] = (strong_up & tight20 & bo_up20 & vol_exp & stack_up).astype(np.int8)
    ev["momo_breakout_short"] = (strong_down & tight20 & bo_dn20 & vol_exp & stack_dn).astype(np.int8)
    ev["flag_breakout_long"] = (tight20 & bo_up20 & vol_exp).astype(np.int8)
    ev["flag_breakout_short"] = (tight20 & bo_dn20 & vol_exp).astype(np.int8)
    ev["base_breakout_long"] = (tight40 & converged & bo_up40).astype(np.int8)
    ev["base_breakout_short"] = (tight40 & converged & bo_dn40).astype(np.int8)
    ev["ignition_long"] = ignite_up.astype(np.int8)
    ev["ignition_short"] = ignite_down.astype(np.int8)
    ev["ignition_with_trend_long"] = (ignite_up & stack_up).astype(np.int8)
    ev["ignition_with_trend_short"] = (ignite_down & stack_dn).astype(np.int8)
    return ev


MOMENTUM_EVENT_SIDE: dict[str, int] = {
    "momo_breakout_long": 1,
    "momo_breakout_short": -1,
    "flag_breakout_long": 1,
    "flag_breakout_short": -1,
    "base_breakout_long": 1,
    "base_breakout_short": -1,
    "ignition_long": 1,
    "ignition_short": -1,
    "ignition_with_trend_long": 1,
    "ignition_with_trend_short": -1,
}
