"""Public-domain / textbook indicator formulas (vectorized where possible).

Not TradingView Pine. No third-party script paste. Formulas follow common
published definitions (Wilder, Lambert, Williams, Keltner / StockCharts).
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view


def ema(x: np.ndarray, span: int) -> np.ndarray:
    return pd.Series(x).ewm(span=span, adjust=False, min_periods=span).mean().to_numpy()


def rma(x: np.ndarray, period: int) -> np.ndarray:
    return pd.Series(x).ewm(alpha=1.0 / period, adjust=False, min_periods=period).mean().to_numpy()


def wilder_atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
    prev_c = np.empty_like(close)
    prev_c[0] = close[0]
    prev_c[1:] = close[:-1]
    tr = np.maximum(high - low, np.maximum(np.abs(high - prev_c), np.abs(low - prev_c)))
    return rma(tr, period)


def williams_r(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
    """Larry Williams %R on [-100, 0]."""
    hh = pd.Series(high).rolling(period, min_periods=period).max().to_numpy()
    ll = pd.Series(low).rolling(period, min_periods=period).min().to_numpy()
    den = hh - ll
    with np.errstate(divide="ignore", invalid="ignore"):
        return -100.0 * (hh - close) / np.where(np.abs(den) > 1e-15, den, np.nan)


def keltner_channel(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    *,
    period: int = 20,
    atr_mult: float = 2.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """EMA(typical price) ± atr_mult * Wilder ATR."""
    tp = (high + low + close) / 3.0
    mid = ema(tp, period)
    atr = wilder_atr(high, low, close, period)
    upper = mid + float(atr_mult) * atr
    lower = mid - float(atr_mult) * atr
    return lower, mid, upper


def bollinger(
    close: np.ndarray, *, period: int = 20, n_std: float = 2.0
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    s = pd.Series(close)
    mid = s.rolling(period, min_periods=period).mean().to_numpy()
    std = s.rolling(period, min_periods=period).std(ddof=0).to_numpy()
    upper = mid + float(n_std) * std
    lower = mid - float(n_std) * std
    width = (upper - lower) / np.where(np.abs(mid) > 1e-15, mid, np.nan)
    return lower, mid, upper, width


def percent_b(close: np.ndarray, lower: np.ndarray, upper: np.ndarray) -> np.ndarray:
    den = upper - lower
    with np.errstate(divide="ignore", invalid="ignore"):
        return (close - lower) / np.where(np.abs(den) > 1e-15, den, np.nan)


def aroon(high: np.ndarray, low: np.ndarray, period: int = 25) -> tuple[np.ndarray, np.ndarray]:
    """Aroon up / down in [0, 100]."""
    n = high.size
    up = np.full(n, np.nan)
    dn = np.full(n, np.nan)
    if n < period:
        return up, dn
    wh = sliding_window_view(high, period)
    wl = sliding_window_view(low, period)
    # argmax/argmin of last `period` bars; Aroon uses bars since extreme.
    hi_i = np.argmax(wh, axis=1)
    lo_i = np.argmin(wl, axis=1)
    # window index 0 = oldest, period-1 = newest
    up[period - 1 :] = 100.0 * (hi_i / float(period - 1)) if period > 1 else 100.0
    dn[period - 1 :] = 100.0 * (lo_i / float(period - 1)) if period > 1 else 100.0
    # Standard Aroon: ((period - bars_since_extreme) / period) * 100
    bars_since_hi = (period - 1) - hi_i
    bars_since_lo = (period - 1) - lo_i
    up[period - 1 :] = 100.0 * (period - bars_since_hi) / float(period)
    dn[period - 1 :] = 100.0 * (period - bars_since_lo) / float(period)
    return up, dn


def parabolic_sar(
    high: np.ndarray,
    low: np.ndarray,
    *,
    step: float = 0.02,
    max_af: float = 0.2,
) -> tuple[np.ndarray, np.ndarray]:
    """Wilder Parabolic SAR. Returns (sar, direction) with direction +1/-1.

    Path-dependent; sequential pass only on the recursive state.
    """
    n = high.size
    sar = np.full(n, np.nan)
    direction = np.full(n, np.nan)
    if n < 2:
        return sar, direction
    bull = True
    af = float(step)
    ep = high[0]
    sar[0] = low[0]
    direction[0] = 1.0
    for i in range(1, n):
        prev = sar[i - 1]
        if bull:
            cand = prev + af * (ep - prev)
            cand = min(cand, low[i - 1], low[i - 2] if i >= 2 else low[i - 1])
            if low[i] < cand:
                bull = False
                sar[i] = ep
                ep = low[i]
                af = float(step)
                direction[i] = -1.0
            else:
                sar[i] = cand
                direction[i] = 1.0
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + float(step), float(max_af))
        else:
            cand = prev + af * (ep - prev)
            cand = max(cand, high[i - 1], high[i - 2] if i >= 2 else high[i - 1])
            if high[i] > cand:
                bull = True
                sar[i] = ep
                ep = high[i]
                af = float(step)
                direction[i] = 1.0
            else:
                sar[i] = cand
                direction[i] = -1.0
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + float(step), float(max_af))
    return sar, direction


def stochastic_kd(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    *,
    period: int = 14,
    smooth: int = 3,
) -> tuple[np.ndarray, np.ndarray]:
    """George Lane Stochastic %K / %D on [0, 100]."""
    hh = pd.Series(high).rolling(period, min_periods=period).max().to_numpy()
    ll = pd.Series(low).rolling(period, min_periods=period).min().to_numpy()
    den = hh - ll
    with np.errstate(divide="ignore", invalid="ignore"):
        k = 100.0 * (close - ll) / np.where(np.abs(den) > 1e-15, den, np.nan)
    d = pd.Series(k).rolling(smooth, min_periods=smooth).mean().to_numpy()
    return k, d


def macd_line_signal(
    close: np.ndarray, *, fast: int = 12, slow: int = 26, signal: int = 9
) -> tuple[np.ndarray, np.ndarray]:
    """Gerald Appel MACD line and signal line."""
    line = ema(close, fast) - ema(close, slow)
    sig = ema(line, signal)
    return line, sig


def wilder_dmi(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Welles Wilder +DI, -DI, Average Directional Index (ADX)."""
    n = high.size
    plus_di = np.full(n, np.nan)
    minus_di = np.full(n, np.nan)
    adx = np.full(n, np.nan)
    if n < 2:
        return plus_di, minus_di, adx
    up = np.empty(n)
    dn = np.empty(n)
    up[0] = np.nan
    dn[0] = np.nan
    up[1:] = high[1:] - high[:-1]
    dn[1:] = low[:-1] - low[1:]
    plus_dm = np.where((up > dn) & (up > 0.0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0.0), dn, 0.0)
    plus_dm[0] = np.nan
    minus_dm[0] = np.nan
    atr = wilder_atr(high, low, close, period)
    plus_sm = rma(plus_dm, period)
    minus_sm = rma(minus_dm, period)
    with np.errstate(divide="ignore", invalid="ignore"):
        plus_di = 100.0 * plus_sm / np.where(atr > 1e-15, atr, np.nan)
        minus_di = 100.0 * minus_sm / np.where(atr > 1e-15, atr, np.nan)
        dx = 100.0 * np.abs(plus_di - minus_di) / np.where(
            (plus_di + minus_di) > 1e-15, plus_di + minus_di, np.nan
        )
    adx = rma(dx, period)
    return plus_di, minus_di, adx


def donchian_prior(
    high: np.ndarray, low: np.ndarray, period: int = 20
) -> tuple[np.ndarray, np.ndarray]:
    """Prior-bar Donchian channel (exclude current bar)."""
    hh = pd.Series(high).rolling(period, min_periods=period).max().shift(1).to_numpy()
    ll = pd.Series(low).rolling(period, min_periods=period).min().shift(1).to_numpy()
    return ll, hh


def rate_of_change(close: np.ndarray, period: int = 12) -> np.ndarray:
    """Percent rate of change vs the close `period` bars ago."""
    prev = pd.Series(close).shift(int(period)).to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        return 100.0 * (close / np.where(np.abs(prev) > 1e-15, prev, np.nan) - 1.0)


def money_flow_index(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    volume: np.ndarray,
    period: int = 14,
) -> np.ndarray:
    """Welles Wilder / Quong-Soudack Money Flow Index on [0, 100]."""
    tp = (high + low + close) / 3.0
    prev = np.empty_like(tp)
    prev[0] = np.nan
    prev[1:] = tp[:-1]
    raw = tp * np.asarray(volume, dtype=float)
    pos = np.where(tp > prev, raw, 0.0)
    neg = np.where(tp < prev, raw, 0.0)
    pos[0] = np.nan
    neg[0] = np.nan
    pm = pd.Series(pos).rolling(period, min_periods=period).sum().to_numpy()
    nm = pd.Series(neg).rolling(period, min_periods=period).sum().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = pm / np.where(nm > 1e-15, nm, np.nan)
        return 100.0 - 100.0 / (1.0 + ratio)


def elder_ray(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 13) -> tuple[np.ndarray, np.ndarray]:
    """Alexander Elder bull power and bear power vs EMA(close)."""
    mid = ema(close, period)
    return high - mid, low - mid


def wma(x: np.ndarray, period: int) -> np.ndarray:
    """Linear weighted moving average (oldest weight 1 … newest weight n)."""
    w = np.arange(1, period + 1, dtype=float)
    s = sliding_window_view(np.asarray(x, dtype=float), period)
    out = np.full(x.size, np.nan, dtype=float)
    out[period - 1 :] = (s * w).sum(axis=1) / w.sum()
    return out


def sma(x: np.ndarray, period: int) -> np.ndarray:
    return pd.Series(x).rolling(period, min_periods=period).mean().to_numpy()


def on_balance_volume(close: np.ndarray, volume: np.ndarray) -> np.ndarray:
    prev = np.empty_like(close)
    prev[0] = np.nan
    prev[1:] = close[:-1]
    direction = np.sign(close - prev)
    direction[0] = 0.0
    raw = direction * np.asarray(volume, dtype=float)
    raw[0] = 0.0
    return np.cumsum(raw)


def trix_line(close: np.ndarray, period: int = 15) -> np.ndarray:
    """Triple-smoothed EMA rate of change (TRIX)."""
    e1 = ema(close, period)
    e2 = ema(e1, period)
    e3 = ema(e2, period)
    prev = np.empty_like(e3)
    prev[0] = np.nan
    prev[1:] = e3[:-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        return 100.0 * (e3 / np.where(np.abs(prev) > 1e-15, prev, np.nan) - 1.0)


def force_index(close: np.ndarray, volume: np.ndarray, period: int = 13) -> np.ndarray:
    """Alexander Elder Force Index, EMA-smoothed."""
    prev = np.empty_like(close)
    prev[0] = np.nan
    prev[1:] = close[:-1]
    raw = (close - prev) * np.asarray(volume, dtype=float)
    return ema(raw, period)


def true_range(high: np.ndarray, low: np.ndarray, close: np.ndarray) -> np.ndarray:
    prev = np.empty_like(close)
    prev[0] = close[0]
    prev[1:] = close[:-1]
    return np.maximum(high - low, np.maximum(np.abs(high - prev), np.abs(low - prev)))


def ultimate_oscillator(
    high: np.ndarray, low: np.ndarray, close: np.ndarray
) -> np.ndarray:
    """Larry Williams Ultimate Oscillator (7/14/28)."""
    prev = np.empty_like(close)
    prev[0] = np.nan
    prev[1:] = close[:-1]
    bp = close - np.minimum(low, prev)
    tr = np.maximum(high, prev) - np.minimum(low, prev)
    bp[0] = np.nan
    tr[0] = np.nan
    out = np.full(close.size, np.nan)
    with np.errstate(divide="ignore", invalid="ignore"):
        parts = []
        for n in (7, 14, 28):
            num = pd.Series(bp).rolling(n, min_periods=n).sum().to_numpy()
            den = pd.Series(tr).rolling(n, min_periods=n).sum().to_numpy()
            parts.append(num / np.where(den > 1e-15, den, np.nan))
        out[:] = 100.0 * (4.0 * parts[0] + 2.0 * parts[1] + parts[2]) / 7.0
    return out


def chaikin_ad_osc(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, volume: np.ndarray
) -> np.ndarray:
    """Chaikin Accumulation/Distribution oscillator (EMA3 − EMA10 of A/D)."""
    den = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        mfm = ((close - low) - (high - close)) / np.where(np.abs(den) > 1e-15, den, np.nan)
    ad = np.nancumsum(mfm * np.asarray(volume, dtype=float))
    return ema(ad, 3) - ema(ad, 10)


def vortex_indicator(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> tuple[np.ndarray, np.ndarray]:
    """+VI and −VI (Botes / Siepman)."""
    prev_h = np.empty_like(high)
    prev_l = np.empty_like(low)
    prev_h[0] = np.nan
    prev_l[0] = np.nan
    prev_h[1:] = high[:-1]
    prev_l[1:] = low[:-1]
    vm_p = np.abs(high - prev_l)
    vm_m = np.abs(low - prev_h)
    tr = true_range(high, low, close)
    sp = pd.Series(vm_p).rolling(period, min_periods=period).sum().to_numpy()
    sm = pd.Series(vm_m).rolling(period, min_periods=period).sum().to_numpy()
    st = pd.Series(tr).rolling(period, min_periods=period).sum().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        plus_vi = sp / np.where(st > 1e-15, st, np.nan)
        minus_vi = sm / np.where(st > 1e-15, st, np.nan)
    return plus_vi, minus_vi


def mass_index(high: np.ndarray, low: np.ndarray, ema_n: int = 9, sum_n: int = 25) -> np.ndarray:
    """Donald Dorsey Mass Index."""
    hl = high - low
    e1 = ema(hl, ema_n)
    e2 = ema(e1, ema_n)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = e1 / np.where(e2 > 1e-15, e2, np.nan)
    return pd.Series(ratio).rolling(sum_n, min_periods=sum_n).sum().to_numpy()


def percent_price_oscillator(close: np.ndarray, *, fast: int = 12, slow: int = 26) -> np.ndarray:
    """Appel-style Percentage Price Oscillator: 100 * (EMA_fast − EMA_slow) / EMA_slow."""
    f = ema(close, fast)
    s = ema(close, slow)
    with np.errstate(divide="ignore", invalid="ignore"):
        return 100.0 * (f - s) / np.where(np.abs(s) > 1e-15, s, np.nan)


def ease_of_movement(high: np.ndarray, low: np.ndarray, volume: np.ndarray, period: int = 14) -> np.ndarray:
    """Richard Arms Ease of Movement, then SMA."""
    mid = (high + low) / 2.0
    prev = np.empty_like(mid)
    prev[0] = np.nan
    prev[1:] = mid[:-1]
    box = high - low
    vol = np.asarray(volume, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = (mid - prev) * box / np.where(np.abs(vol) > 1e-15, vol, np.nan)
    return sma(raw, period)


def chande_momentum(close: np.ndarray, period: int = 14) -> np.ndarray:
    """Tushar Chande Momentum Oscillator on [-100, 100]."""
    prev = np.empty_like(close)
    prev[0] = np.nan
    prev[1:] = close[:-1]
    delta = close - prev
    up = np.where(delta > 0.0, delta, 0.0)
    dn = np.where(delta < 0.0, -delta, 0.0)
    up[0] = np.nan
    dn[0] = np.nan
    su = pd.Series(up).rolling(period, min_periods=period).sum().to_numpy()
    sd = pd.Series(dn).rolling(period, min_periods=period).sum().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        return 100.0 * (su - sd) / np.where((su + sd) > 1e-15, su + sd, np.nan)


def demarker(high: np.ndarray, low: np.ndarray, period: int = 14) -> np.ndarray:
    """Tom DeMark DeMarker on [0, 1]."""
    prev_h = np.empty_like(high)
    prev_l = np.empty_like(low)
    prev_h[0] = np.nan
    prev_l[0] = np.nan
    prev_h[1:] = high[:-1]
    prev_l[1:] = low[:-1]
    demax = np.where(high > prev_h, high - prev_h, 0.0)
    demin = np.where(low < prev_l, prev_l - low, 0.0)
    demax[0] = np.nan
    demin[0] = np.nan
    sma_x = sma(demax, period)
    sma_n = sma(demin, period)
    with np.errstate(divide="ignore", invalid="ignore"):
        return sma_x / np.where((sma_x + sma_n) > 1e-15, sma_x + sma_n, np.nan)


def qstick(open_: np.ndarray, close: np.ndarray, period: int = 8) -> np.ndarray:
    """Tushar Chande Qstick: SMA(close − open)."""
    return sma(close - open_, period)


def awesome_oscillator(high: np.ndarray, low: np.ndarray) -> np.ndarray:
    """Bill Williams Awesome Oscillator: SMA5 − SMA34 of midpoint."""
    mid = (high + low) / 2.0
    return sma(mid, 5) - sma(mid, 34)


def accelerator_oscillator(high: np.ndarray, low: np.ndarray) -> np.ndarray:
    """Bill Williams Accelerator: AO − SMA(AO, 5)."""
    ao = awesome_oscillator(high, low)
    return ao - sma(ao, 5)


def wilder_rsi(close: np.ndarray, period: int = 14) -> np.ndarray:
    prev = np.empty_like(close)
    prev[0] = np.nan
    prev[1:] = close[:-1]
    delta = close - prev
    gain = np.where(delta > 0.0, delta, 0.0)
    loss = np.where(delta < 0.0, -delta, 0.0)
    gain[0] = np.nan
    loss[0] = np.nan
    avg_g = rma(gain, period)
    avg_l = rma(loss, period)
    with np.errstate(divide="ignore", invalid="ignore"):
        rs = avg_g / np.where(avg_l > 1e-15, avg_l, np.nan)
        return 100.0 - 100.0 / (1.0 + rs)


def stochastic_rsi(close: np.ndarray, period: int = 14) -> np.ndarray:
    """Stochastic of Wilder RSI on [0, 100]."""
    rsi = wilder_rsi(close, period)
    hh = pd.Series(rsi).rolling(period, min_periods=period).max().to_numpy()
    ll = pd.Series(rsi).rolling(period, min_periods=period).min().to_numpy()
    den = hh - ll
    with np.errstate(divide="ignore", invalid="ignore"):
        return 100.0 * (rsi - ll) / np.where(np.abs(den) > 1e-15, den, np.nan)


def chaikin_money_flow(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, volume: np.ndarray, period: int = 20
) -> np.ndarray:
    """Chaikin Money Flow: rolling money-flow volume / rolling volume."""
    hl = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        mfm = ((close - low) - (high - close)) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    mfv = mfm * volume
    num = pd.Series(mfv).rolling(period, min_periods=period).sum().to_numpy()
    den = pd.Series(volume).rolling(period, min_periods=period).sum().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        return num / np.where(np.abs(den) > 1e-15, den, np.nan)


def relative_vigor_index(
    open_: np.ndarray, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 10
) -> np.ndarray:
    """John Ehlers Relative Vigor Index: SMA(close − open) / SMA(high − low)."""
    num = sma(close - open_, period)
    den = sma(high - low, period)
    with np.errstate(divide="ignore", invalid="ignore"):
        return num / np.where(np.abs(den) > 1e-15, den, np.nan)


def balance_of_power(
    open_: np.ndarray, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    """Iggy Cho Balance of Power, then SMA."""
    hl = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = (close - open_) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    return sma(raw, period)


def choppiness_index(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    """Choppiness Index: 100 * log10(sum(TR) / (HH − LL)) / log10(n)."""
    tr = true_range(high, low, close)
    tr_sum = pd.Series(tr).rolling(period, min_periods=period).sum().to_numpy()
    hh = pd.Series(high).rolling(period, min_periods=period).max().to_numpy()
    ll = pd.Series(low).rolling(period, min_periods=period).min().to_numpy()
    span = hh - ll
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = tr_sum / np.where(np.abs(span) > 1e-15, span, np.nan)
        return 100.0 * np.log10(np.where(ratio > 0.0, ratio, np.nan)) / np.log10(float(period))


def know_sure_thing(close: np.ndarray) -> np.ndarray:
    """Martin Pring Know Sure Thing: weighted ROC sum, then SMA 10."""
    kst = (
        rate_of_change(close, 10)
        + 2.0 * rate_of_change(close, 15)
        + 3.0 * rate_of_change(close, 20)
        + 4.0 * rate_of_change(close, 30)
    )
    return sma(kst, 10)


def ehlers_fisher(high: np.ndarray, low: np.ndarray, period: int = 10) -> np.ndarray:
    """John Ehlers Fisher Transform of the median price, causal (no center)."""
    mid = (high + low) / 2.0
    hh = pd.Series(mid).rolling(period, min_periods=period).max().to_numpy()
    ll = pd.Series(mid).rolling(period, min_periods=period).min().to_numpy()
    span = hh - ll
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = 2.0 * (mid - ll) / np.where(np.abs(span) > 1e-15, span, np.nan) - 1.0
    raw = np.clip(raw, -0.999, 0.999)
    sm = pd.Series(raw).ewm(alpha=0.33, adjust=False, min_periods=period).mean().to_numpy()
    sm = np.clip(sm, -0.999, 0.999)
    with np.errstate(divide="ignore", invalid="ignore"):
        return 0.5 * np.log((1.0 + sm) / (1.0 - sm))


def dpo_uncentered(close: np.ndarray, period: int = 20) -> np.ndarray:
    """Detrended price oscillator without a centered window (causal)."""
    return close - sma(close, period)


def vwma(close: np.ndarray, volume: np.ndarray, period: int = 20) -> np.ndarray:
    """Volume-weighted moving average."""
    pv = pd.Series(close * volume).rolling(period, min_periods=period).sum().to_numpy()
    vv = pd.Series(volume).rolling(period, min_periods=period).sum().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        return pv / np.where(np.abs(vv) > 1e-15, vv, np.nan)


def ad_line_osc(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, volume: np.ndarray, period: int = 20
) -> np.ndarray:
    """Accumulation/Distribution line minus its SMA (oscillator)."""
    hl = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        mfm = ((close - low) - (high - close)) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    adl = np.cumsum(np.where(np.isfinite(mfm), mfm * volume, 0.0))
    adl = np.where(np.isfinite(mfm), adl, np.nan)
    return adl - sma(adl, period)


def hull_moving_average(close: np.ndarray, period: int = 16) -> np.ndarray:
    """Alan Hull moving average: WMA of 2*WMA(n/2) − WMA(n)."""
    half = max(2, period // 2)
    root = max(2, int(round(np.sqrt(period))))
    raw = 2.0 * wma(close, half) - wma(close, period)
    return wma(raw, root)


def volume_oscillator(volume: np.ndarray, fast: int = 5, slow: int = 10) -> np.ndarray:
    """Short SMA of volume minus long SMA of volume."""
    return sma(volume, fast) - sma(volume, slow)


def intradaily_intensity(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, volume: np.ndarray, period: int = 14
) -> np.ndarray:
    """Intraday Intensity: SMA of (2close − high − low) / (high − low) * volume."""
    hl = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = ((2.0 * close - high - low) / np.where(np.abs(hl) > 1e-15, hl, np.nan)) * volume
    return sma(raw, period)


def rolling_linreg_slope(close: np.ndarray, period: int = 20) -> np.ndarray:
    """Causal rolling ordinary-least-squares slope of close versus bar index."""
    x = np.asarray(close, dtype=float)
    n = int(period)
    if x.size < n:
        return np.full(x.size, np.nan, dtype=float)
    win = sliding_window_view(x, n)
    t = np.arange(n, dtype=float)
    sum_t = t.sum()
    sum_t2 = (t * t).sum()
    sum_x = win.sum(axis=1)
    sum_tx = win @ t
    den = n * sum_t2 - sum_t * sum_t
    with np.errstate(divide="ignore", invalid="ignore"):
        slope = (n * sum_tx - sum_t * sum_x) / np.where(np.abs(den) > 1e-15, den, np.nan)
    out = np.full(x.size, np.nan, dtype=float)
    out[n - 1 :] = slope
    return out


def midpoint_roc(high: np.ndarray, low: np.ndarray, period: int = 12) -> np.ndarray:
    """Rate of change of the median price (high + low) / 2."""
    return rate_of_change((high + low) / 2.0, period)


def close_location_value(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    """SMA of Close Location Value: ((close − low) − (high − close)) / (high − low)."""
    hl = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        clv = ((close - low) - (high - close)) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    return sma(clv, period)


def kaufman_efficiency_ratio(close: np.ndarray, period: int = 10) -> np.ndarray:
    """Kaufman Efficiency Ratio: |net change| / sum of absolute changes."""
    x = np.asarray(close, dtype=float)
    if x.size <= period:
        return np.full(x.size, np.nan, dtype=float)
    net = np.abs(x[period:] - x[:-period])
    dlt = np.abs(np.diff(x))
    vol = pd.Series(dlt).rolling(period, min_periods=period).sum().to_numpy()
    out = np.full(x.size, np.nan, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out[period:] = net / np.where(vol[period - 1 :] > 1e-15, vol[period - 1 :], np.nan)
    return out


def smma_median(high: np.ndarray, low: np.ndarray, period: int) -> np.ndarray:
    """Wilder smoothed moving average of the median price."""
    return rma((high + low) / 2.0, period)


def typical_price_dist(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 20) -> np.ndarray:
    """Typical price minus its SMA, as a fraction of close."""
    tp = (high + low + close) / 3.0
    mid = sma(tp, period)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (tp - mid) / np.where(close > 0, close, np.nan)


def true_range_relative(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 20
) -> np.ndarray:
    """True range divided by its trailing SMA (not Wilder ATR / ATR-average)."""
    tr = true_range(high, low, close)
    mid = sma(tr, period)
    with np.errstate(divide="ignore", invalid="ignore"):
        return tr / np.where(mid > 1e-15, mid, np.nan)


def body_fraction(
    open_: np.ndarray, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    """SMA of |close − open| / (high − low)."""
    hl = high - low
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = np.abs(close - open_) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    return sma(raw, period)


def upper_wick_fraction(
    open_: np.ndarray, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    """SMA of upper wick / (high − low)."""
    hl = high - low
    body_top = np.maximum(open_, close)
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = (high - body_top) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    return sma(raw, period)


def realized_vol_frac(close: np.ndarray, period: int = 20) -> np.ndarray:
    """Rolling standard deviation of close, divided by close."""
    sd = pd.Series(close).rolling(period, min_periods=period).std(ddof=0).to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        return sd / np.where(close > 0, close, np.nan)


def lower_wick_fraction(
    open_: np.ndarray, high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14
) -> np.ndarray:
    """SMA of lower wick / (high − low)."""
    hl = high - low
    body_bot = np.minimum(open_, close)
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = (body_bot - low) / np.where(np.abs(hl) > 1e-15, hl, np.nan)
    return sma(raw, period)


def close_open_bias(open_: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
    """SMA of (close − open) / close."""
    with np.errstate(divide="ignore", invalid="ignore"):
        raw = (close - open_) / np.where(close > 0, close, np.nan)
    return sma(raw, period)


def opening_gap(open_: np.ndarray, close: np.ndarray) -> np.ndarray:
    """(open − prior close) / prior close."""
    prev = np.empty_like(close)
    prev[0] = np.nan
    prev[1:] = close[:-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        return (open_ - prev) / np.where(prev > 0, prev, np.nan)


def roc_acceleration(close: np.ndarray, period: int = 12) -> np.ndarray:
    """One-bar change of the rate of change (causal)."""
    r = rate_of_change(close, period)
    out = np.empty_like(r)
    out[0] = np.nan
    out[1:] = r[1:] - r[:-1]
    return out


def price_volume_corr(close: np.ndarray, volume: np.ndarray, period: int = 20) -> np.ndarray:
    """Rolling correlation of close and volume."""
    return pd.Series(close).rolling(period, min_periods=period).corr(pd.Series(volume)).to_numpy()


def atr_relative(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, *, atr_n: int = 14, avg_n: int = 50
) -> np.ndarray:
    """Wilder ATR divided by its trailing average."""
    atr = wilder_atr(high, low, close, atr_n)
    mid = pd.Series(atr).rolling(avg_n, min_periods=max(10, avg_n // 2)).mean().to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        return atr / np.where(mid > 1e-15, mid, np.nan)


def cross_up(series: np.ndarray, level: float) -> np.ndarray:
    s = np.asarray(series, dtype=float)
    prev = np.empty_like(s)
    prev[0] = np.nan
    prev[1:] = s[:-1]
    return (prev < level) & (s >= level)


def cross_down(series: np.ndarray, level: float) -> np.ndarray:
    s = np.asarray(series, dtype=float)
    prev = np.empty_like(s)
    prev[0] = np.nan
    prev[1:] = s[:-1]
    return (prev > level) & (s <= level)


def any_in_next(bit: np.ndarray, horizon: int) -> np.ndarray:
    b = np.asarray(bit, dtype=np.int8).reshape(-1)
    n = b.size
    out = np.zeros(n, dtype=bool)
    if horizon <= 0 or n == 0:
        return out
    csum = np.empty(n + 1, dtype=np.int64)
    csum[0] = 0
    np.cumsum(b, out=csum[1:])
    idx = np.arange(n, dtype=np.int64)
    start = np.minimum(idx + 1, n)
    end = np.minimum(idx + 1 + horizon, n)
    out[:] = (csum[end] - csum[start]) > 0
    out[idx + horizon >= n] = False
    return out


def window_last(arr: np.ndarray, horizon: int, offset: int = 1) -> np.ndarray:
    x = np.asarray(arr, dtype=float).reshape(-1)
    n = x.size
    pad = np.empty(n + horizon + offset, dtype=float)
    pad[:n] = x
    pad[n:] = np.nan
    t = np.arange(n, dtype=np.int64)
    return pad[t + offset + horizon - 1]
