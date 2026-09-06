"""Hunt 016 causal ideas: oscillators + classic floor pivots (not a 015 retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import ema, sma, wilder_atr
from llm2.ml_lab.causal_math import bar_return, sign_nz
from llm2.validation.folds import index_to_ms

RSI_N = 14
RSI_HI = 70.0
RSI_LO = 30.0
STOCH_N = 14
STOCH_HI = 0.80
STOCH_LO = 0.20
CCI_N = 20
CCI_TH = 100.0
ADX_N = 14
ADX_TH = 25.0
DAY_MS = 86_400_000

IDEA_IDS_M: tuple[str, ...] = (
    "rsi_extreme_fade",
    "macd_hist_flip",
    "stoch_extreme_fade",
    "cci_revert",
    "adx_trend_follow",
    "classic_pivot_fade",
    "inside_then_break",
    "bar_gap_fade",
)


def _wilder_smooth(x: np.ndarray, n: int) -> np.ndarray:
    return pd.Series(x).ewm(alpha=1.0 / float(n), min_periods=n, adjust=False).mean().to_numpy(dtype=float)


def rsi_extreme_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Wilder Relative Strength Index extremes (70 / 30)."""
    del timeframe
    r = bar_return(ohlcv["close"].to_numpy(dtype=float))
    gain = np.where(np.isfinite(r) & (r > 0), r, 0.0)
    loss = np.where(np.isfinite(r) & (r < 0), -r, 0.0)
    ag = _wilder_smooth(gain, RSI_N)
    al = _wilder_smooth(loss, RSI_N)
    with np.errstate(divide="ignore", invalid="ignore"):
        rs = ag / np.where(al > 0, al, np.nan)
        rsi = 100.0 - 100.0 / (1.0 + rs)
    out = np.zeros(r.size, dtype=np.float64)
    out[np.isfinite(rsi) & (rsi >= RSI_HI)] = -1.0
    out[np.isfinite(rsi) & (rsi <= RSI_LO)] = 1.0
    return out


def macd_hist_flip(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow the new sign when the Moving Average Convergence Divergence histogram flips."""
    del timeframe
    c = ohlcv["close"].to_numpy(dtype=float)
    hist = ema(c, 12) - ema(c, 26)
    hist = hist - ema(hist, 9)
    prev = np.roll(hist, 1)
    prev[0] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    flip = np.isfinite(hist) & np.isfinite(prev) & (np.sign(hist) != np.sign(prev)) & (hist != 0)
    out[flip] = sign_nz(hist)[flip]
    return out


def stoch_extreme_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a 14-bar stochastic percent-K at 80 / 20."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    hh = pd.Series(h).rolling(STOCH_N, min_periods=STOCH_N).max().to_numpy(dtype=float)
    ll = pd.Series(l).rolling(STOCH_N, min_periods=STOCH_N).min().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        k = (c - ll) / np.where(hh > ll, hh - ll, np.nan)
    out = np.zeros(c.size, dtype=np.float64)
    out[np.isfinite(k) & (k >= STOCH_HI)] = -1.0
    out[np.isfinite(k) & (k <= STOCH_LO)] = 1.0
    return out


def cci_revert(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade Commodity Channel Index beyond ±100 (typical price vs its mean)."""
    del timeframe
    tp = (ohlcv["high"].to_numpy(dtype=float) + ohlcv["low"].to_numpy(dtype=float) + ohlcv["close"].to_numpy(dtype=float)) / 3.0
    mid = sma(tp, CCI_N)
    mad = pd.Series(np.abs(tp - mid)).rolling(CCI_N, min_periods=CCI_N).mean().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        cci = (tp - mid) / (0.015 * np.where(mad > 0, mad, np.nan))
    out = np.zeros(tp.size, dtype=np.float64)
    out[np.isfinite(cci) & (cci >= CCI_TH)] = -1.0
    out[np.isfinite(cci) & (cci <= -CCI_TH)] = 1.0
    return out


def adx_trend_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow +DI / −DI when Average Directional Index is elevated."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    up = h - np.roll(h, 1)
    dn = np.roll(l, 1) - l
    up[0] = np.nan
    dn[0] = np.nan
    plus_dm = np.where(np.isfinite(up) & (up > dn) & (up > 0), up, 0.0)
    minus_dm = np.where(np.isfinite(dn) & (dn > up) & (dn > 0), dn, 0.0)
    atr = wilder_atr(h, l, c, ADX_N)
    plus_di = 100.0 * _wilder_smooth(plus_dm, ADX_N) / np.where(atr > 0, atr, np.nan)
    minus_di = 100.0 * _wilder_smooth(minus_dm, ADX_N) / np.where(atr > 0, atr, np.nan)
    with np.errstate(divide="ignore", invalid="ignore"):
        dx = 100.0 * np.abs(plus_di - minus_di) / np.where((plus_di + minus_di) > 0, plus_di + minus_di, np.nan)
    adx = _wilder_smooth(np.nan_to_num(dx, nan=0.0), ADX_N)
    adx = np.where(np.isfinite(dx), adx, np.nan)
    out = np.zeros(c.size, dtype=np.float64)
    trend = np.isfinite(adx) & (adx >= ADX_TH) & np.isfinite(plus_di) & np.isfinite(minus_di)
    out[trend & (plus_di > minus_di)] = 1.0
    out[trend & (minus_di > plus_di)] = -1.0
    return out


def classic_pivot_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a touch of the previous UTC day's R1 / S1 floor-trader pivots."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    day = index_to_ms(ohlcv.index).astype(np.int64) // DAY_MS
    g = pd.DataFrame({"d": day, "h": h, "l": l, "c": c})
    daily = g.groupby("d", sort=True).agg(hh=("h", "max"), ll=("l", "min"), cc=("c", "last"))
    p = (daily["hh"] + daily["ll"] + daily["cc"]) / 3.0
    r1 = (2.0 * p - daily["ll"]).shift(1)
    s1 = (2.0 * p - daily["hh"]).shift(1)
    rr = r1.reindex(day).to_numpy(dtype=float)
    ss = s1.reindex(day).to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    out[np.isfinite(rr) & (h >= rr)] = -1.0
    out[np.isfinite(ss) & (l <= ss)] = 1.0
    both = np.isfinite(rr) & np.isfinite(ss) & (h >= rr) & (l <= ss)
    out[both] = 0.0
    return out


def inside_then_break(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow a close beyond the mother bar after a completed inside bar."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    inside = np.zeros(c.size, dtype=bool)
    inside[1:] = (h[1:] <= h[:-1]) & (l[1:] >= l[:-1])
    was = np.roll(inside, 1)
    was[0] = False
    mother_h = np.roll(h, 2)
    mother_l = np.roll(l, 2)
    mother_h[:2] = np.nan
    mother_l[:2] = np.nan
    out = np.zeros(c.size, dtype=np.float64)
    up = was & np.isfinite(mother_h) & (c > mother_h)
    dn = was & np.isfinite(mother_l) & (c < mother_l)
    out[up] = 1.0
    out[dn] = -1.0
    return out


def bar_gap_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a gap between this open and the prior close (not a three-bar Fair Value Gap)."""
    del timeframe
    o = ohlcv["open"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    prev = np.roll(c, 1)
    prev[0] = np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        gap = o - prev
        wide = np.abs(gap) >= 0.25 * atr
    out = np.zeros(c.size, dtype=np.float64)
    out[wide & np.isfinite(gap)] = -sign_nz(gap)[wide & np.isfinite(gap)]
    return out


def signals_m(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "rsi_extreme_fade": rsi_extreme_fade(ohlcv, timeframe),
        "macd_hist_flip": macd_hist_flip(ohlcv, timeframe),
        "stoch_extreme_fade": stoch_extreme_fade(ohlcv, timeframe),
        "cci_revert": cci_revert(ohlcv, timeframe),
        "adx_trend_follow": adx_trend_follow(ohlcv, timeframe),
        "classic_pivot_fade": classic_pivot_fade(ohlcv, timeframe),
        "inside_then_break": inside_then_break(ohlcv, timeframe),
        "bar_gap_fade": bar_gap_fade(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state for leakage (not the sparse ±1 fires)."""
    del kwargs
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    r = bar_return(c)
    tp = (h + l + c) / 3.0
    hist = ema(c, 12) - ema(c, 26)
    hist = hist - ema(hist, 9)
    return pd.DataFrame(
        {
            "bar_return": r,
            "macd_hist": hist,
            "stoch_k": (c - pd.Series(l).rolling(STOCH_N, min_periods=STOCH_N).min().to_numpy(dtype=float))
            / np.where(
                (
                    pd.Series(h).rolling(STOCH_N, min_periods=STOCH_N).max()
                    - pd.Series(l).rolling(STOCH_N, min_periods=STOCH_N).min()
                ).to_numpy(dtype=float)
                > 0,
                (
                    pd.Series(h).rolling(STOCH_N, min_periods=STOCH_N).max()
                    - pd.Series(l).rolling(STOCH_N, min_periods=STOCH_N).min()
                ).to_numpy(dtype=float),
                np.nan,
            ),
            "typical": tp,
            "atr_frac": wilder_atr(h, l, c, 14) / np.where(c > 0, c, np.nan),
        },
        index=ohlcv.index,
    )
