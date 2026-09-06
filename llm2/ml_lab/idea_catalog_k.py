"""Hunt 014 causal ideas: higher-timeframe Fair Value Gap plus new formulas.

Higher-timeframe Fair Value Gap uses only *completed* coarser bars (15-minute →
1-hour, 1-hour → 4-hour, 4-hour → 1-day). The event is stamped on the first
finer bar of the new coarse bucket — the moment the coarse candle is known.

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import wilder_atr
from llm2.ml_lab.causal_math import bar_return, sign_nz, zscore
from llm2.ml_lab.idea_catalog_i import FVG_ATR_MIN, _fvg_arrays, _gap_size
from llm2.paths import TF_MS
from llm2.validation.folds import index_to_ms

DISP_ATR = 1.20
STACK_WIN = 30
STACK_MIN = 2.0
PARK_WIN = 24
PARK_Z = 1.50
MIDNIGHT_ATR = 0.30
HTF_FACTOR = {"15m": 4, "1h": 4, "4h": 6}

IDEA_IDS_K: tuple[str, ...] = (
    "htf_fvg_follow",
    "htf_fvg_confluence",
    "htf_fvg_inside",
    "fvg_fill_continue",
    "displace_fvg_follow",
    "fvg_stack_long",
    "parkinson_expand_follow",
    "utc_midnight_fade",
)


def _parkinson_close_ratio(high: np.ndarray, low: np.ndarray, close: np.ndarray) -> np.ndarray:
    with np.errstate(divide="ignore", invalid="ignore"):
        hl = np.log(np.where((high > 0) & (low > 0), high / low, np.nan))
        park = (hl * hl) / (4.0 * np.log(2.0))
    cc = bar_return(close) ** 2
    p_m = pd.Series(park).rolling(PARK_WIN, min_periods=PARK_WIN).mean()
    c_m = pd.Series(cc).rolling(PARK_WIN, min_periods=PARK_WIN).mean()
    with np.errstate(divide="ignore", invalid="ignore"):
        return (p_m / c_m.replace(0.0, np.nan)).to_numpy(dtype=float)


def _htf_just_closed(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    """Map completed coarser Fair Value Gaps onto the first finer bar of the new bucket."""
    n = len(ohlcv)
    z = np.zeros(n, dtype=np.float64)
    nan = np.full(n, np.nan)
    factor = HTF_FACTOR.get(str(timeframe))
    if factor is None:
        return {"sign": z, "bull_bot": nan, "bull_top": nan, "just_closed": np.zeros(n, dtype=bool)}
    ts = index_to_ms(ohlcv.index).astype(np.int64)
    htf_ms = int(TF_MS[str(timeframe)]) * int(factor)
    bucket = ts // htf_ms
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    g = pd.DataFrame({"b": bucket, "o": o, "h": h, "l": l, "c": c})
    htf = g.groupby("b", sort=True).agg(o=("o", "first"), h=("h", "max"), l=("l", "min"), c=("c", "last"))
    hh = htf["h"].to_numpy(dtype=float)
    ll = htf["l"].to_numpy(dtype=float)
    cc = htf["c"].to_numpy(dtype=float)
    bt, bb, et, eb = _fvg_arrays(hh, ll)
    atr_h = wilder_atr(hh, ll, cc, 14)
    bull_gap = _gap_size(bt, bb)
    bear_gap = _gap_size(et, eb)
    htf_sign = np.zeros(hh.size, dtype=np.float64)
    htf_sign[np.isfinite(bb) & (bull_gap >= FVG_ATR_MIN * atr_h)] = 1.0
    htf_sign[np.isfinite(eb) & (bear_gap >= FVG_ATR_MIN * atr_h)] = -1.0
    just_closed = np.zeros(n, dtype=bool)
    just_closed[1:] = bucket[1:] != bucket[:-1]
    completed = bucket - 1
    idx = htf.index.to_numpy()
    sign_s = pd.Series(htf_sign, index=idx)
    bb_s = pd.Series(bb, index=idx)
    bt_s = pd.Series(bt, index=idx)
    mapped = sign_s.reindex(completed).to_numpy(dtype=float)
    bull_bot = bb_s.reindex(completed).to_numpy(dtype=float)
    bull_top = bt_s.reindex(completed).to_numpy(dtype=float)
    mapped = np.where(just_closed & np.isfinite(mapped), mapped, 0.0)
    return {
        "sign": mapped,
        "bull_bot": np.where(just_closed, bull_bot, np.nan),
        "bull_top": np.where(just_closed, bull_top, np.nan),
        "just_closed": just_closed,
    }


def htf_fvg_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow the Fair Value Gap of the higher timeframe that just closed."""
    return _htf_just_closed(ohlcv, str(timeframe or "1h"))["sign"]


def htf_fvg_confluence(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Bullish higher-timeframe gap just closed and the finer 20-bar low is intact."""
    htf = _htf_just_closed(ohlcv, str(timeframe or "1h"))
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    prior_low = pd.Series(l).shift(1).rolling(20, min_periods=20).min().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    fire = (htf["sign"] >= 0.5) & np.isfinite(prior_low) & (c > prior_low)
    out[fire] = 1.0
    return out


def htf_fvg_inside(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Just-closed bullish higher-timeframe gap and finer close sits inside that gap."""
    htf = _htf_just_closed(ohlcv, str(timeframe or "1h"))
    c = ohlcv["close"].to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    inside = (
        (htf["sign"] >= 0.5)
        & np.isfinite(htf["bull_bot"])
        & np.isfinite(htf["bull_top"])
        & (c >= htf["bull_bot"])
        & (c <= htf["bull_top"])
    )
    out[inside] = 1.0
    return out


def fvg_fill_continue(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """After price trades through a native gap, follow the original gap direction."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bt, bb, et, eb = _fvg_arrays(h, l)
    bull_ok = np.isfinite(bb) & (_gap_size(bt, bb) >= FVG_ATR_MIN * atr)
    bear_ok = np.isfinite(eb) & (_gap_size(et, eb) >= FVG_ATR_MIN * atr)
    n = c.size
    idx = np.arange(n)
    last_bull = np.maximum.accumulate(np.where(bull_ok, idx, -1))
    last_bear = np.maximum.accumulate(np.where(bear_ok, idx, -1))
    bull_bot = np.where(last_bull >= 0, bb[np.clip(last_bull, 0, n - 1)], np.nan)
    bull_top = np.where(last_bull >= 0, bt[np.clip(last_bull, 0, n - 1)], np.nan)
    bear_bot = np.where(last_bear >= 0, eb[np.clip(last_bear, 0, n - 1)], np.nan)
    bear_top = np.where(last_bear >= 0, et[np.clip(last_bear, 0, n - 1)], np.nan)
    out = np.zeros(n, dtype=np.float64)
    bull_fill = (last_bull >= 0) & (last_bull < idx) & np.isfinite(bull_bot) & (l <= bull_bot) & (c >= bull_top)
    bear_fill = (last_bear >= 0) & (last_bear < idx) & np.isfinite(bear_top) & (h >= bear_top) & (c <= bear_bot)
    out[bull_fill] = 1.0
    out[bear_fill] = -1.0
    return out


def displace_fvg_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fresh native Fair Value Gap plus a same-direction body larger than 1.2 Average True Range."""
    del timeframe
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    body = np.abs(c - o)
    disp = np.isfinite(atr) & (atr > 0) & (body >= DISP_ATR * atr)
    bt, bb, et, eb = _fvg_arrays(h, l)
    out = np.zeros(c.size, dtype=np.float64)
    bull = disp & (c > o) & np.isfinite(bb) & (_gap_size(bt, bb) >= FVG_ATR_MIN * atr)
    bear = disp & (c < o) & np.isfinite(eb) & (_gap_size(et, eb) >= FVG_ATR_MIN * atr)
    out[bull] = 1.0
    out[bear] = -1.0
    return out


def fvg_stack_long(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """A new bullish Fair Value Gap while at least two such gaps printed in the last 30 bars."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    bt, bb, _, _ = _fvg_arrays(h, l)
    bull = (np.isfinite(bb) & (_gap_size(bt, bb) >= FVG_ATR_MIN * atr)).astype(np.float64)
    stack = pd.Series(bull).rolling(STACK_WIN, min_periods=STACK_WIN).sum().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    out[(bull >= 0.5) & (stack >= STACK_MIN)] = 1.0
    return out


def parkinson_expand_follow(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Follow the bar return when Parkinson range-vol is high versus close-to-close vol."""
    del timeframe
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    ratio = _parkinson_close_ratio(h, l, c)
    z = zscore(ratio)
    r = bar_return(c)
    out = np.zeros(c.size, dtype=np.float64)
    fire = np.isfinite(z) & (z >= PARK_Z)
    out[fire] = sign_nz(r)[fire]
    return out


def utc_midnight_fade(ohlcv: pd.DataFrame, timeframe: str | None = None) -> np.ndarray:
    """Fade a large UTC 00:00 open gap (crypto daily open)."""
    del timeframe
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    idx = ohlcv.index
    if idx.tz is None:
        utc = idx.tz_localize("UTC")
    else:
        utc = idx.tz_convert("UTC")
    is_open = (utc.hour == 0) & (utc.minute == 0)
    prev = np.roll(c, 1)
    prev[0] = np.nan
    with np.errstate(divide="ignore", invalid="ignore"):
        gap = o / np.where(prev > 0, prev, np.nan) - 1.0
        atr_frac = atr / np.where(c > 0, c, np.nan)
    out = np.zeros(c.size, dtype=np.float64)
    wide = np.isfinite(gap) & np.isfinite(atr_frac) & (np.abs(gap) >= MIDNIGHT_ATR * atr_frac)
    fire = np.asarray(is_open) & wide
    out[fire] = -sign_nz(gap)[fire]
    return out


def signals_k(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    return {
        "htf_fvg_follow": htf_fvg_follow(ohlcv, timeframe),
        "htf_fvg_confluence": htf_fvg_confluence(ohlcv, timeframe),
        "htf_fvg_inside": htf_fvg_inside(ohlcv, timeframe),
        "fvg_fill_continue": fvg_fill_continue(ohlcv, timeframe),
        "displace_fvg_follow": displace_fvg_follow(ohlcv, timeframe),
        "fvg_stack_long": fvg_stack_long(ohlcv, timeframe),
        "parkinson_expand_follow": parkinson_expand_follow(ohlcv, timeframe),
        "utc_midnight_fade": utc_midnight_fade(ohlcv, timeframe),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state for leakage (not the sparse ±1 fires)."""
    tf = str(kwargs.get("timeframe") or "1h")
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    o = ohlcv["open"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    htf = _htf_just_closed(ohlcv, tf)
    park = _parkinson_close_ratio(h, l, c)
    with np.errstate(divide="ignore", invalid="ignore"):
        body_atr = np.abs(c - o) / np.where(atr > 0, atr, np.nan)
        atr_frac = atr / np.where(c > 0, c, np.nan)
    return pd.DataFrame(
        {
            "bar_return": bar_return(c),
            "atr_frac": atr_frac,
            "body_atr": body_atr,
            "htf_fvg_sign": htf["sign"],
            "parkinson_ratio": park,
            "high_low_atr": (h - l) / np.where(atr > 0, atr, np.nan),
        },
        index=ohlcv.index,
    )
