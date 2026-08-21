"""Causal known-now features + future-event labels for the confluence pack.

Labels may look ahead inside this module only. Features must be prefix-invariant.
Do not use unconfirmed fractal pivots as features (confirmed_at bar index <= t).
"""

from __future__ import annotations

from dataclasses import dataclass
from warnings import catch_warnings, simplefilter

import numpy as np
import pandas as pd

from llm2.diagnostics.events import detect_pulses
from llm2.pivot.labels.config import PivotLabelConfig
from llm2.pivot.labels.fractal import label_fractal_pivots

EVENT_IDS: tuple[str, ...] = (
    "rsi_cross_up_30",
    "rsi_cross_down_70",
    "macd_hist_flip_up",
    "macd_hist_flip_down",
    "adx_fade",
    "vsa_dryup_expand",
    "failed_swing_ll",
    "failed_swing_hh",
    "stoch_cross_up_20",
    "stoch_cross_down_80",
    "pulse_extend",
    "structure_break_hold",
)

# Generation 002 extras. Keep off the 001 column list unless include_002=True.
EVENT_IDS_002: tuple[str, ...] = (
    "range_hold",
    "range_break_up",
    "range_break_down",
    "atr_squeeze_expand",
)

REVERSAL_EVENTS = frozenset(EVENT_IDS[:10])
CONTINUATION_EVENTS = frozenset(EVENT_IDS[10:]) | frozenset(
    {"range_break_up", "range_break_down", "atr_squeeze_expand"}
)
RANGE_EVENTS = frozenset({"range_hold"})
MARKET_ENTRY_EVENTS = frozenset(
    {"pulse_extend", "range_break_up", "range_break_down", "atr_squeeze_expand"}
)
LONG_EVENTS = frozenset(
    {
        "rsi_cross_up_30",
        "macd_hist_flip_up",
        "stoch_cross_up_20",
        "failed_swing_ll",
        "range_break_up",
    }
)
SHORT_EVENTS = frozenset(
    {
        "rsi_cross_down_70",
        "macd_hist_flip_down",
        "stoch_cross_down_80",
        "failed_swing_hh",
        "range_break_down",
    }
)


@dataclass(frozen=True)
class EventPack:
    """Aligned to ``ohlcv`` rows. Labels are NaN on the last ``horizon`` bars."""

    horizon: int
    features: pd.DataFrame
    labels: pd.DataFrame  # 0/1, last H rows NaN
    side: pd.DataFrame  # -1 short, +1 long, 0 none (oracle trade side)
    occurrence: pd.DataFrame  # event bit on this bar (causal if occurrence-style)


def _ema(x: np.ndarray, span: int) -> np.ndarray:
    return pd.Series(x).ewm(span=span, adjust=False, min_periods=span).mean().to_numpy()


def _rma(x: np.ndarray, period: int) -> np.ndarray:
    return pd.Series(x).ewm(alpha=1.0 / period, adjust=False, min_periods=period).mean().to_numpy()


def _rsi(close: np.ndarray, period: int = 14) -> np.ndarray:
    delta = np.diff(close, prepend=close[0])
    gain = np.clip(delta, 0.0, None)
    loss = np.clip(-delta, 0.0, None)
    avg_g = _rma(gain, period)
    avg_l = _rma(loss, period)
    rs = avg_g / np.where(avg_l > 0, avg_l, np.nan)
    return 100.0 - (100.0 / (1.0 + rs))


def _macd_hist(close: np.ndarray) -> np.ndarray:
    macd = _ema(close, 12) - _ema(close, 26)
    signal = pd.Series(macd).ewm(span=9, adjust=False, min_periods=9).mean().to_numpy()
    return macd - signal


def _stoch(high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 14, d: int = 3):
    hh = pd.Series(high).rolling(n, min_periods=n).max().to_numpy()
    ll = pd.Series(low).rolling(n, min_periods=n).min().to_numpy()
    den = hh - ll
    k = 100.0 * (close - ll) / np.where(np.abs(den) > 1e-15, den, np.nan)
    d_line = pd.Series(k).rolling(d, min_periods=d).mean().to_numpy()
    return k, d_line


def _adx(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14):
    prev_c = np.empty_like(close)
    prev_c[0] = close[0]
    prev_c[1:] = close[:-1]
    prev_h = np.empty_like(high)
    prev_h[0] = high[0]
    prev_h[1:] = high[:-1]
    prev_l = np.empty_like(low)
    prev_l[0] = low[0]
    prev_l[1:] = low[:-1]
    tr = np.maximum(high - low, np.maximum(np.abs(high - prev_c), np.abs(low - prev_c)))
    up = high - prev_h
    dn = prev_l - low
    plus_dm = np.where((up > dn) & (up > 0.0), up, 0.0)
    minus_dm = np.where((dn > up) & (dn > 0.0), dn, 0.0)
    atr = _rma(tr, period)
    pdi = 100.0 * _rma(plus_dm, period) / np.where(atr > 0, atr, np.nan)
    mdi = 100.0 * _rma(minus_dm, period) / np.where(atr > 0, atr, np.nan)
    dx = 100.0 * np.abs(pdi - mdi) / np.where((pdi + mdi) > 0, pdi + mdi, np.nan)
    adx = _rma(dx, period)
    return adx, pdi, mdi


def _wilder_atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
    prev_c = np.empty_like(close)
    prev_c[0] = close[0]
    prev_c[1:] = close[:-1]
    tr = np.maximum(high - low, np.maximum(np.abs(high - prev_c), np.abs(low - prev_c)))
    return _rma(tr, period)


def any_in_next(bit: np.ndarray, horizon: int) -> np.ndarray:
    """True at t if ``bit`` is true on any of bars t+1 .. t+horizon.

    Last ``horizon`` rows are False (incomplete); callers should NaN labels there.
    """
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


def _window_from(arr: np.ndarray, horizon: int, offset: int = 1) -> np.ndarray:
    """Return shape (n, horizon) with ``out[t, k] = arr[t + offset + k]`` (NaN past end)."""
    x = np.asarray(arr, dtype=float).reshape(-1)
    n = x.size
    pad = np.empty(n + horizon + offset, dtype=float)
    pad[:n] = x
    pad[n:] = np.nan
    t = np.arange(n, dtype=np.int64)[:, None]
    k = np.arange(horizon, dtype=np.int64)[None, :]
    return pad[t + offset + k]


def _cross_up(series: np.ndarray, level: float) -> np.ndarray:
    s = np.asarray(series, dtype=float)
    prev = np.empty_like(s)
    prev[0] = np.nan
    prev[1:] = s[:-1]
    return (prev < level) & (s >= level)


def _cross_down(series: np.ndarray, level: float) -> np.ndarray:
    s = np.asarray(series, dtype=float)
    prev = np.empty_like(s)
    prev[0] = np.nan
    prev[1:] = s[:-1]
    return (prev > level) & (s <= level)


def _sign_flip_up(series: np.ndarray) -> np.ndarray:
    s = np.asarray(series, dtype=float)
    prev = np.empty_like(s)
    prev[0] = np.nan
    prev[1:] = s[:-1]
    return (prev <= 0.0) & (s > 0.0)


def _sign_flip_down(series: np.ndarray) -> np.ndarray:
    s = np.asarray(series, dtype=float)
    prev = np.empty_like(s)
    prev[0] = np.nan
    prev[1:] = s[:-1]
    return (prev >= 0.0) & (s < 0.0)


def _confirmed_swing_levels(ohlcv: pd.DataFrame, cfg: PivotLabelConfig) -> tuple[np.ndarray, np.ndarray]:
    """Last confirmed swing high/low price at each bar (NaN until first confirm)."""
    n = len(ohlcv)
    last_high = np.full(n, np.nan)
    last_low = np.full(n, np.nan)
    events = label_fractal_pivots(ohlcv, cfg)
    if events is None or len(events) == 0:
        return last_high, last_low
    upd_h = np.full(n, np.nan)
    upd_l = np.full(n, np.nan)
    conf = events["confirm_bar_index"].to_numpy(dtype=np.int64)
    side = events["pivot_side"].to_numpy()
    px = events["pivot_price"].to_numpy(dtype=float)
    ok = (conf >= 0) & (conf < n)
    is_h = ok & (side == "high")
    is_l = ok & (side == "low")
    # Last write wins on the same confirm bar.
    upd_h[conf[is_h]] = px[is_h]
    upd_l[conf[is_l]] = px[is_l]
    last_high = pd.Series(upd_h).ffill().to_numpy()
    last_low = pd.Series(upd_l).ffill().to_numpy()
    return last_high, last_low


def _pulse_dir(ohlcv: pd.DataFrame) -> np.ndarray:
    n = len(ohlcv)
    out = np.zeros(n, dtype=np.int8)
    pulses = detect_pulses(ohlcv)
    if pulses is None or len(pulses) == 0:
        return out
    bars = pulses["bar"].to_numpy(dtype=np.int64)
    d = pulses["direction"].to_numpy(dtype=np.int8)
    ok = (bars >= 0) & (bars < n)
    out[bars[ok]] = d[ok]
    return out


def build_known_now_features(ohlcv: pd.DataFrame) -> pd.DataFrame:
    """Strictly causal columns (no future). Prefix-invariant."""
    df = ohlcv.sort_index()
    high = df["high"].to_numpy(dtype=float)
    low = df["low"].to_numpy(dtype=float)
    close = df["close"].to_numpy(dtype=float)
    vol = df["volume"].to_numpy(dtype=float) if "volume" in df.columns else np.ones(len(df))
    rsi = _rsi(close, 14)
    hist = _macd_hist(close)
    adx, pdi, mdi = _adx(high, low, close, 14)
    k, d_line = _stoch(high, low, close)
    atr = _wilder_atr(high, low, close, 14)
    ema21 = _ema(close, 21)
    vol_z = (
        (vol - pd.Series(vol).rolling(48, min_periods=12).mean().to_numpy())
        / pd.Series(vol).rolling(48, min_periods=12).std().to_numpy()
    )
    adx_slope = adx - np.concatenate([[np.nan], adx[:-1]])
    cfg = PivotLabelConfig(
        timeframe="15m",
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        min_left_prominence_atr=0.5,
        min_right_reversal_atr=0.5,
        min_reversal_pct=0.0015,
    )
    last_high, last_low = _confirmed_swing_levels(df, cfg)
    pulse = _pulse_dir(df)
    with np.errstate(divide="ignore", invalid="ignore"):
        dist_high = (close - last_high) / np.where(close > 0, close, np.nan)
        dist_low = (close - last_low) / np.where(close > 0, close, np.nan)
        atr_frac = atr / np.where(close > 0, close, np.nan)
        ema_dist = (close - ema21) / np.where(close > 0, close, np.nan)
    broke_high = np.isfinite(last_high) & (close > last_high)
    broke_low = np.isfinite(last_low) & (close < last_low)
    prev_bh = np.empty_like(broke_high)
    prev_bh[0] = False
    prev_bh[1:] = broke_high[:-1]
    prev_bl = np.empty_like(broke_low)
    prev_bl[0] = False
    prev_bl[1:] = broke_low[:-1]
    hh20 = pd.Series(high).rolling(20, min_periods=10).max().to_numpy()
    ll20 = pd.Series(low).rolling(20, min_periods=10).min().to_numpy()
    rng = hh20 - ll20
    close_pos = (close - ll20) / np.where(np.abs(rng) > 1e-15, rng, np.nan)
    range_w = rng / np.where(close > 0, close, np.nan)
    atr_min = pd.Series(atr).rolling(100, min_periods=40).min().to_numpy()
    atr_max = pd.Series(atr).rolling(100, min_periods=40).max().to_numpy()
    atr_span = atr_max - atr_min
    atr_pos = (atr - atr_min) / np.where(np.abs(atr_span) > 1e-15, atr_span, np.nan)
    ret4 = np.full_like(close, np.nan)
    ret4[4:] = close[4:] / np.where(close[:-4] > 0, close[:-4], np.nan) - 1.0
    out = pd.DataFrame(
        {
            "rsi_14": rsi,
            "rsi_below_30": (rsi < 30).astype(float),
            "rsi_above_70": (rsi > 70).astype(float),
            "macd_hist": hist,
            "macd_hist_sign": np.sign(hist),
            "adx_14": adx,
            "plus_di": pdi,
            "minus_di": mdi,
            "adx_slope": adx_slope,
            "adx_stretched": (adx > 25.0).astype(float),
            "stoch_k": k,
            "stoch_d": d_line,
            "vol_z_48": vol_z,
            "atr_frac": atr_frac,
            "ema21_dist": ema_dist,
            "dist_confirmed_high": dist_high,
            "dist_confirmed_low": dist_low,
            "broke_confirmed_high": broke_high.astype(float),
            "broke_confirmed_low": broke_low.astype(float),
            "fresh_break_high": (broke_high & ~prev_bh).astype(float),
            "fresh_break_low": (broke_low & ~prev_bl).astype(float),
            "pulse_dir": pulse.astype(float),
            "pulse_flag": (pulse != 0).astype(float),
            "range20_width": range_w,
            "close_pos_in_range20": close_pos,
            "atr_pos_100": atr_pos,
            "ret4": ret4,
        },
        index=df.index,
    )
    return out.replace([np.inf, -np.inf], np.nan)


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    """Leakage-CLI adapter: known-now features only."""
    return build_known_now_features(ohlcv)


def build_event_pack(
    ohlcv: pd.DataFrame, *, horizon: int = 4, include_002: bool = False
) -> EventPack:
    """Build features + oracle labels for one horizon."""
    if horizon < 1:
        raise ValueError("horizon must be >= 1")
    df = ohlcv.sort_index()
    n = len(df)
    high = df["high"].to_numpy(dtype=float)
    low = df["low"].to_numpy(dtype=float)
    close = df["close"].to_numpy(dtype=float)
    feat = build_known_now_features(df)
    rsi = feat["rsi_14"].to_numpy(dtype=float)
    hist = feat["macd_hist"].to_numpy(dtype=float)
    adx = feat["adx_14"].to_numpy(dtype=float)
    pdi = feat["plus_di"].to_numpy(dtype=float)
    mdi = feat["minus_di"].to_numpy(dtype=float)
    k = feat["stoch_k"].to_numpy(dtype=float)
    vol_z = feat["vol_z_48"].to_numpy(dtype=float)
    pulse = feat["pulse_dir"].to_numpy(dtype=float)
    cfg = PivotLabelConfig(
        timeframe="15m",
        left_bars=3,
        right_bars=3,
        confirm_bars=3,
        min_left_prominence_atr=0.5,
        min_right_reversal_atr=0.5,
        min_reversal_pct=0.0015,
    )
    last_high, last_low = _confirmed_swing_levels(df, cfg)

    occ: dict[str, np.ndarray] = {}
    bits: dict[str, np.ndarray] = {}
    sides: dict[str, np.ndarray] = {}

    occ["rsi_cross_up_30"] = _cross_up(rsi, 30.0)
    occ["rsi_cross_down_70"] = _cross_down(rsi, 70.0)
    bits["rsi_cross_up_30"] = any_in_next(occ["rsi_cross_up_30"], horizon)
    bits["rsi_cross_down_70"] = any_in_next(occ["rsi_cross_down_70"], horizon)
    sides["rsi_cross_up_30"] = np.where(bits["rsi_cross_up_30"], 1.0, 0.0)
    sides["rsi_cross_down_70"] = np.where(bits["rsi_cross_down_70"], -1.0, 0.0)

    occ["macd_hist_flip_up"] = _sign_flip_up(hist)
    occ["macd_hist_flip_down"] = _sign_flip_down(hist)
    bits["macd_hist_flip_up"] = any_in_next(occ["macd_hist_flip_up"], horizon)
    bits["macd_hist_flip_down"] = any_in_next(occ["macd_hist_flip_down"], horizon)
    sides["macd_hist_flip_up"] = np.where(bits["macd_hist_flip_up"], 1.0, 0.0)
    sides["macd_hist_flip_down"] = np.where(bits["macd_hist_flip_down"], -1.0, 0.0)

    occ["stoch_cross_up_20"] = _cross_up(k, 20.0)
    occ["stoch_cross_down_80"] = _cross_down(k, 80.0)
    bits["stoch_cross_up_20"] = any_in_next(occ["stoch_cross_up_20"], horizon)
    bits["stoch_cross_down_80"] = any_in_next(occ["stoch_cross_down_80"], horizon)
    sides["stoch_cross_up_20"] = np.where(bits["stoch_cross_up_20"], 1.0, 0.0)
    sides["stoch_cross_down_80"] = np.where(bits["stoch_cross_down_80"], -1.0, 0.0)

    # ADX fade over the horizon after a stretch (loss of trend strength).
    fut_adx = _window_from(adx, horizon, offset=1)
    adx_end = fut_adx[:, -1]
    stretched_now = adx > 25.0
    fade = stretched_now & np.isfinite(adx_end) & (adx_end < (adx - 2.0))
    occ["adx_fade"] = (adx > 25.0) & (feat["adx_slope"].to_numpy(dtype=float) < 0.0)
    bits["adx_fade"] = fade
    # Fade after uptrend → short reversal; after downtrend → long.
    up_trend = pdi > mdi
    sides["adx_fade"] = np.where(fade, np.where(up_trend, -1.0, 1.0), 0.0)

    # Volume dry-up then expansion inside the horizon.
    fut_z = _window_from(vol_z, horizon, offset=1)
    half = max(1, horizon // 2)
    with catch_warnings():
        simplefilter("ignore", RuntimeWarning)
        dry = np.nanmin(fut_z[:, :half], axis=1) < -0.5
        expn = np.nanmax(fut_z[:, half:], axis=1) > 0.5
    vsa = dry & expn
    occ["vsa_dryup_expand"] = feat["vol_z_48"].to_numpy(dtype=float) < -0.5
    bits["vsa_dryup_expand"] = vsa
    ema_dist = feat["ema21_dist"].to_numpy(dtype=float)
    sides["vsa_dryup_expand"] = np.where(vsa, np.where(ema_dist < 0.0, 1.0, -1.0), 0.0)

    # Failed swing: wick through last confirmed swing then close back (reversal).
    w_low = _window_from(low, horizon, offset=1)
    w_high = _window_from(high, horizon, offset=1)
    w_close = _window_from(close, horizon, offset=1)
    L = last_low[:, None]
    H = last_high[:, None]
    pierce_low = w_low < L
    reclaim_low = w_close > L
    first_pl = np.argmax(pierce_low, axis=1)
    ks = np.arange(horizon)[None, :]
    failed_ll = pierce_low.any(axis=1) & ((ks >= first_pl[:, None]) & reclaim_low).any(axis=1)
    failed_ll[~np.isfinite(last_low)] = False
    pierce_high = w_high > H
    reclaim_high = w_close < H
    first_ph = np.argmax(pierce_high, axis=1)
    failed_hh = pierce_high.any(axis=1) & ((ks >= first_ph[:, None]) & reclaim_high).any(axis=1)
    failed_hh[~np.isfinite(last_high)] = False
    occ["failed_swing_ll"] = feat["broke_confirmed_low"].to_numpy(dtype=bool)
    occ["failed_swing_hh"] = feat["broke_confirmed_high"].to_numpy(dtype=bool)
    bits["failed_swing_ll"] = failed_ll
    bits["failed_swing_hh"] = failed_hh
    sides["failed_swing_ll"] = np.where(failed_ll, 1.0, 0.0)
    sides["failed_swing_hh"] = np.where(failed_hh, -1.0, 0.0)

    # Pulse already flagged at t; next H bars extend the pulse (continuation).
    close_h = np.empty_like(close)
    close_h[:] = np.nan
    if n > horizon:
        close_h[: n - horizon] = close[horizon:]
    pulse_i = np.sign(pulse)
    extend = (pulse_i != 0) & np.isfinite(close_h) & (np.sign(close_h - close) == pulse_i)
    occ["pulse_extend"] = pulse_i != 0
    bits["pulse_extend"] = extend
    sides["pulse_extend"] = np.where(extend, pulse_i, 0.0)

    # Fresh break of last confirmed swing, then hold beyond it (continuation).
    fresh_h = feat["fresh_break_high"].to_numpy(dtype=bool)
    fresh_l = feat["fresh_break_low"].to_numpy(dtype=bool)
    with catch_warnings():
        simplefilter("ignore", RuntimeWarning)
        min_low = np.nanmin(w_low, axis=1)
        max_high = np.nanmax(w_high, axis=1)
    hold_up = fresh_h & np.isfinite(last_high) & np.isfinite(min_low) & (min_low > last_high)
    hold_dn = fresh_l & np.isfinite(last_low) & np.isfinite(max_high) & (max_high < last_low)
    occ["structure_break_hold"] = fresh_h | fresh_l
    bits["structure_break_hold"] = hold_up | hold_dn
    sides["structure_break_hold"] = np.where(hold_up, 1.0, np.where(hold_dn, -1.0, 0.0))

    ids = EVENT_IDS
    if include_002:
        hh20 = pd.Series(high).rolling(20, min_periods=10).max().to_numpy()
        ll20 = pd.Series(low).rolling(20, min_periods=10).min().to_numpy()
        with catch_warnings():
            simplefilter("ignore", RuntimeWarning)
            fut_max_h = np.nanmax(w_high, axis=1)
            fut_min_l = np.nanmin(w_low, axis=1)
        hold = (
            np.isfinite(hh20)
            & np.isfinite(ll20)
            & np.isfinite(fut_max_h)
            & np.isfinite(fut_min_l)
            & (fut_max_h <= hh20)
            & (fut_min_l >= ll20)
        )
        occ["range_hold"] = np.isfinite(feat["range20_width"].to_numpy(dtype=float))
        bits["range_hold"] = hold
        pos = feat["close_pos_in_range20"].to_numpy(dtype=float)
        # Mean-revert inside the channel: high in range → short, low → long.
        sides["range_hold"] = np.where(hold, np.where(pos >= 0.66, -1.0, np.where(pos <= 0.34, 1.0, 0.0)), 0.0)

        last_c = w_close[:, -1]
        br_up = np.isfinite(hh20) & np.isfinite(last_c) & (last_c > hh20) & (w_close > hh20[:, None]).any(axis=1)
        br_dn = np.isfinite(ll20) & np.isfinite(last_c) & (last_c < ll20) & (w_close < ll20[:, None]).any(axis=1)
        occ["range_break_up"] = feat["close_pos_in_range20"].to_numpy(dtype=float) > 0.8
        occ["range_break_down"] = feat["close_pos_in_range20"].to_numpy(dtype=float) < 0.2
        bits["range_break_up"] = br_up
        bits["range_break_down"] = br_dn
        sides["range_break_up"] = np.where(br_up, 1.0, 0.0)
        sides["range_break_down"] = np.where(br_dn, -1.0, 0.0)

        atr_now = feat["atr_frac"].to_numpy(dtype=float) * close
        fut_atr = _window_from(atr_now, horizon, offset=1)
        atr_end = fut_atr[:, -1]
        squeezed = feat["atr_pos_100"].to_numpy(dtype=float) < 0.25
        expand = squeezed & np.isfinite(atr_end) & np.isfinite(atr_now) & (atr_end > (atr_now * 1.25))
        occ["atr_squeeze_expand"] = squeezed
        bits["atr_squeeze_expand"] = expand
        ret4 = feat["ret4"].to_numpy(dtype=float)
        sides["atr_squeeze_expand"] = np.where(expand, np.sign(ret4), 0.0)
        ids = EVENT_IDS + EVENT_IDS_002

    valid = np.arange(n) + horizon < n
    labels = pd.DataFrame(index=df.index)
    side_df = pd.DataFrame(index=df.index)
    occ_df = pd.DataFrame(index=df.index)
    for eid in ids:
        lab = bits[eid].astype(float)
        lab[~valid] = np.nan
        labels[eid] = lab
        sd = sides[eid].astype(float)
        sd[~valid] = np.nan
        sd[lab != 1.0] = 0.0
        side_df[eid] = sd
        occ_df[eid] = occ[eid].astype(float)
    return EventPack(
        horizon=int(horizon),
        features=feat,
        labels=labels,
        side=side_df,
        occurrence=occ_df,
    )


def event_ids(*, family: str | None = None, include_002: bool = False) -> tuple[str, ...]:
    ids = EVENT_IDS + EVENT_IDS_002 if include_002 else EVENT_IDS
    if family is None:
        return ids
    if family == "reversal":
        return tuple(e for e in ids if e in REVERSAL_EVENTS)
    if family == "continuation":
        return tuple(e for e in ids if e in CONTINUATION_EVENTS)
    if family == "range":
        return tuple(e for e in ids if e in RANGE_EVENTS)
    raise ValueError(f"unknown family {family!r}")


def signed_forward_log_return(close: np.ndarray, side: np.ndarray, horizon: int) -> np.ndarray:
    """Oracle diagnostic: side[t] * log(close[t+H]/close[t])."""
    c = np.asarray(close, dtype=float)
    s = np.asarray(side, dtype=float)
    n = c.size
    fut = np.full(n, np.nan)
    if n > horizon:
        fut[: n - horizon] = c[horizon:]
    with np.errstate(divide="ignore", invalid="ignore"):
        ret = np.log(fut / np.where(c > 0, c, np.nan))
    out = s * ret
    out[s == 0] = np.nan
    return out
