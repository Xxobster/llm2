"""Thirty named causal ideas: power-trend, channel-surf, formula mixes.

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are frozen
module constants, not searched on profit factor.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import (
    bollinger,
    close_location_value,
    donchian_prior,
    ema,
    kaufman_efficiency_ratio,
    keltner_channel,
    opening_gap,
    percent_b,
    rate_of_change,
    realized_vol_frac,
    rolling_linreg_slope,
    sma,
    wilder_atr,
)
from llm2.ml_lab.kref import forward_return

ER_HI = 0.40
VOL_RATIO = 1.50
BB_WIDTH_MAX = 0.040
ATR_FRAC_COMPRESS = 0.012
Z_FIRE = 1.50
HURST_TREND = 0.55
HURST_MR = 0.45
AR1_TH = 0.05
DRIFT_TH = 0.0003
GAP_TH = 0.003
BLEND_TH = 0.30
SL_FLOOR = 0.004
SL_CAP = 0.030
TP_CAP = 0.090

PIVOT_BARS = {"5m": 288, "15m": 96, "1h": 24, "4h": 6, "1d": 5}
HORIZON_BARS = {"5m": 12, "15m": 8, "1h": 8, "4h": 6, "1d": 5}

POWER = (
    "power_donchian_er",
    "power_vol_expand",
    "power_atr_expand",
    "power_volume_z",
    "power_linreg_er",
    "power_ema_stack_long",
    "power_donchian_volume",
    "power_clv_range",
    "power_sma_pullback",
    "power_gap_continue",
)
SURF = (
    "surf_bb_band",
    "surf_keltner_band",
    "surf_donchian_band",
    "surf_linreg_channel",
    "surf_inside_mother",
    "surf_tp_vwap",
    "surf_daily_pivot",
    "surf_range_compress",
    "surf_bb_mid",
    "surf_keltner_mid",
)
MIX = (
    "mix_ar1_switch",
    "mix_holt_slope",
    "mix_hurst_switch",
    "mix_z_er_flip",
    "mix_roc_accel",
    "mix_fastslow_ewma",
    "mix_btc_residual",
    "mix_drift_theta",
    "mix_turtle_hurst",
    "mix_er_blend",
)
IDEA_IDS: tuple[str, ...] = POWER + SURF + MIX
CHANNEL_IDEAS = set(SURF) | {"mix_turtle_hurst"}


def _ret(close: np.ndarray) -> np.ndarray:
    c = np.asarray(close, dtype=np.float64)
    r = np.full(c.size, np.nan)
    with np.errstate(divide="ignore", invalid="ignore"):
        r[1:] = c[1:] / np.where(c[:-1] > 0, c[:-1], np.nan) - 1.0
    return r


def _sign_nz(x: np.ndarray) -> np.ndarray:
    s = np.sign(np.asarray(x, dtype=float))
    return np.where(np.isfinite(s) & (s != 0), s, 0.0)


def _zscore(x: np.ndarray, win: int) -> np.ndarray:
    s = pd.Series(x)
    mu = s.rolling(win, min_periods=win).mean()
    sd = s.rolling(win, min_periods=win).std(ddof=0)
    return ((s - mu) / sd.replace(0, np.nan)).to_numpy(dtype=float)


def _rolling_ar1(r: np.ndarray, win: int = 64) -> np.ndarray:
    a = pd.Series(r)
    return a.rolling(win, min_periods=win).corr(a.shift(1)).to_numpy(dtype=float)


def _hurst_proxy(r: np.ndarray, win: int = 64, k: int = 8) -> np.ndarray:
    """Causal variance-ratio Hurst proxy: 0.5 * log(VR) / log(k)."""
    s = pd.Series(r)
    ksum = s.rolling(k, min_periods=k).sum()
    v1 = s.rolling(win, min_periods=win).var(ddof=0)
    vk = ksum.rolling(win, min_periods=win).var(ddof=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        vr = vk / (float(k) * v1.replace(0, np.nan))
        h = 0.5 * np.log(vr.to_numpy(dtype=float)) / np.log(float(k))
    return h


def _band_fade(close: np.ndarray, lo: np.ndarray, hi: np.ndarray, ok: np.ndarray) -> np.ndarray:
    out = np.zeros(close.size, dtype=np.float64)
    out[ok & (close <= lo)] = 1.0
    out[ok & (close >= hi)] = -1.0
    return out


def _band_mid_fade(close: np.ndarray, mid: np.ndarray, ok: np.ndarray) -> np.ndarray:
    return np.where(ok, -_sign_nz(close - mid), 0.0)


def channel_offsets(
    close: np.ndarray,
    lo: np.ndarray,
    hi: np.ndarray,
    is_short: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    c = np.asarray(close, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        sl_long = (c - lo) / np.where(c > 0, c, np.nan)
        tp_long = (hi - c) / np.where(c > 0, c, np.nan)
        sl_short = (hi - c) / np.where(c > 0, c, np.nan)
        tp_short = (c - lo) / np.where(c > 0, c, np.nan)
    sl = np.where(is_short, sl_short, sl_long)
    tp = np.where(is_short, tp_short, tp_long)
    sl = np.clip(sl, SL_FLOOR, SL_CAP)
    tp = np.clip(tp, SL_FLOOR, TP_CAP)
    return sl.astype(float), tp.astype(float)


def event_metrics(sig: np.ndarray, y: np.ndarray, *, cost_floor: float = 0.0011) -> dict[str, Any]:
    s = np.asarray(sig, dtype=float)
    t = np.asarray(y, dtype=float)
    m = (s != 0) & np.isfinite(s) & np.isfinite(t)
    n = int(m.sum())
    if n < 40:
        return {
            "n_skill": n,
            "spearman_ic": float("nan"),
            "directional_acc": float("nan"),
            "mean_signed": float("nan"),
            "mean_signed_net": float("nan"),
        }
    pp = s[m]
    tt = t[m]
    if np.std(pp) < 1e-12 or np.std(tt) < 1e-12:
        ic = 0.0
    else:
        ic = float(np.corrcoef(pp.argsort().argsort(), tt.argsort().argsort())[0, 1])
    da = float(np.mean(np.sign(pp) == np.sign(tt)))
    mu = float(np.mean(pp * tt))
    return {
        "n_skill": n,
        "spearman_ic": ic,
        "directional_acc": da,
        "mean_signed": mu,
        "mean_signed_net": mu - float(cost_floor),
    }


def signals_from_ohlcv(
    ohlcv: pd.DataFrame,
    timeframe: str,
    *,
    other_close: np.ndarray | None = None,
) -> dict[str, np.ndarray]:
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    o = ohlcv["open"].to_numpy(dtype=float) if "open" in ohlcv.columns else c
    vol = ohlcv["volume"].to_numpy(dtype=float) if "volume" in ohlcv.columns else np.ones(c.size)
    n = c.size
    r = _ret(c)
    atr = wilder_atr(h, l, c, 14)
    atr_frac = atr / np.where(c > 0, c, np.nan)
    er = kaufman_efficiency_ratio(c, 10)
    sma96 = sma(c, 96)
    sma48 = sma(c, 48)
    slope = rolling_linreg_slope(c, 20)
    ll, hh = donchian_prior(h, l, 20)
    blo, bmid, bhi, bwid = bollinger(c, period=20, n_std=2.0)
    klo, kmid, khi = keltner_channel(h, l, c, period=20, atr_mult=2.0)
    pb = percent_b(c, blo, bhi)
    rv4 = realized_vol_frac(c, 4)
    rv96 = realized_vol_frac(c, 96)
    vol_z = _zscore(vol, 96)
    clv = close_location_value(h, l, c, 14)
    gap = opening_gap(o, c)
    rng = h - l
    ema12 = ema(c, 12)
    ema48 = ema(c, 48)
    ema192 = ema(c, 192)
    ar1 = _rolling_ar1(r, 64)
    hurst = _hurst_proxy(r, 64, 8)
    z_r = _zscore(r, 48)
    roc12 = rate_of_change(c, 12)
    roc_d = np.full(n, np.nan)
    roc_d[1:] = np.diff(roc12)
    tp = (h + l + c) / 3.0
    vwap = sma(tp, 96)
    vwap_sd = pd.Series(tp - vwap).rolling(96, min_periods=96).std(ddof=0).to_numpy()
    pivot_n = int(PIVOT_BARS.get(timeframe, 24))
    p_hi = pd.Series(h).rolling(pivot_n, min_periods=pivot_n).max().shift(1).to_numpy()
    p_lo = pd.Series(l).rolling(pivot_n, min_periods=pivot_n).min().shift(1).to_numpy()
    p_mid = 0.5 * (p_hi + p_lo)
    rng_ma = sma(rng, 20)
    mother_hi = np.roll(h, 1)
    mother_lo = np.roll(l, 1)
    mother_hi[0] = np.nan
    mother_lo[0] = np.nan
    inside = (h <= mother_hi) & (l >= mother_lo)
    resid_std = pd.Series(c - sma(c, 20)).rolling(20, min_periods=20).std(ddof=0).to_numpy()
    lin_mid = sma(c, 20)
    lin_hi = lin_mid + 2.0 * resid_std
    lin_lo = lin_mid - 2.0 * resid_std
    atr_med = pd.Series(atr_frac).rolling(96, min_periods=96).median().to_numpy()
    power = er >= ER_HI
    compress_bb = bwid <= BB_WIDTH_MAX
    compress_atr = atr_frac <= ATR_FRAC_COMPRESS
    expand_vol = rv4 >= (VOL_RATIO * rv96)
    expand_atr = atr_frac >= (1.25 * atr_med)
    vol_hot = vol_z >= 1.0
    break_up = c > hh
    break_dn = c < ll

    out: dict[str, np.ndarray] = {}
    out["power_donchian_er"] = np.where(power & break_up, 1.0, np.where(power & break_dn, -1.0, 0.0))
    out["power_vol_expand"] = np.where(expand_vol, _sign_nz(sma(r, 4)), 0.0)
    out["power_atr_expand"] = np.where(expand_atr, _sign_nz(c - sma48), 0.0)
    out["power_volume_z"] = np.where(vol_z >= 2.0, _sign_nz(r), 0.0)
    out["power_linreg_er"] = np.where(power, _sign_nz(slope), 0.0)
    stack = (ema12 > ema48) & (ema48 > ema192) & power
    out["power_ema_stack_long"] = np.where(stack, 1.0, 0.0)
    out["power_donchian_volume"] = np.where(vol_hot & break_up, 1.0, np.where(vol_hot & break_dn, -1.0, 0.0))
    rng_hot = rng >= (1.2 * atr)
    out["power_clv_range"] = np.where(rng_hot & (np.abs(clv) >= 0.4), _sign_nz(clv), 0.0)
    near_sma = np.abs(c - sma96) <= atr
    out["power_sma_pullback"] = np.where(
        (slope > 0) & near_sma & (c <= sma96),
        1.0,
        np.where((slope < 0) & near_sma & (c >= sma96), -1.0, 0.0),
    )
    out["power_gap_continue"] = np.where(np.abs(gap) >= GAP_TH, _sign_nz(gap), 0.0)

    out["surf_bb_band"] = _band_fade(c, blo, bhi, compress_bb)
    out["surf_keltner_band"] = _band_fade(c, klo, khi, compress_atr)
    out["surf_donchian_band"] = _band_fade(c, ll, hh, compress_atr)
    out["surf_linreg_channel"] = _band_fade(c, lin_lo, lin_hi, compress_bb)
    mid_m = 0.5 * (mother_hi + mother_lo)
    out["surf_inside_mother"] = np.where(inside, -_sign_nz(c - mid_m), 0.0)
    out["surf_tp_vwap"] = _band_fade(c, vwap - 2.0 * vwap_sd, vwap + 2.0 * vwap_sd, compress_bb)
    out["surf_daily_pivot"] = _band_fade(c, p_lo, p_hi, compress_atr)
    compress_run = rng <= (0.7 * rng_ma)
    box_lo = pd.Series(l).rolling(8, min_periods=8).min().to_numpy()
    box_hi = pd.Series(h).rolling(8, min_periods=8).max().to_numpy()
    out["surf_range_compress"] = _band_fade(c, box_lo, box_hi, compress_run)
    out["surf_bb_mid"] = _band_mid_fade(c, bmid, compress_bb)
    out["surf_keltner_mid"] = _band_mid_fade(c, kmid, compress_atr)

    fade_r = -_sign_nz(r)
    follow_r = _sign_nz(r)
    out["mix_ar1_switch"] = np.where(ar1 <= -AR1_TH, fade_r, np.where(ar1 >= AR1_TH, follow_r, 0.0))
    holt = ema(c, 16) - ema(c, 48)
    out["mix_holt_slope"] = _sign_nz(holt)
    sma_dir = _sign_nz(c - sma48)
    out["mix_hurst_switch"] = np.where(
        hurst >= HURST_TREND, sma_dir, np.where(hurst <= HURST_MR, -sma_dir, 0.0)
    )
    out["mix_z_er_flip"] = np.where(
        np.abs(z_r) >= Z_FIRE,
        np.where(power, _sign_nz(z_r), -_sign_nz(z_r)),
        0.0,
    )
    out["mix_roc_accel"] = np.where(_sign_nz(roc12) == _sign_nz(roc_d), _sign_nz(roc12), 0.0)
    fs = ema(c, 8) - ema(c, 32)
    out["mix_fastslow_ewma"] = np.where(np.abs(fs) >= (0.2 * atr), _sign_nz(fs), 0.0)
    resid = np.zeros(n)
    if other_close is not None and np.asarray(other_close).size == n:
        oth = _ret(np.asarray(other_close, dtype=float))
        oth_lag = np.roll(oth, 1)
        oth_lag[0] = np.nan
        beta = pd.Series(r).rolling(96, min_periods=96).cov(pd.Series(oth_lag)) / pd.Series(
            oth_lag
        ).rolling(96, min_periods=96).var(ddof=0).replace(0, np.nan)
        resid = r - beta.to_numpy(dtype=float) * oth_lag
    out["mix_btc_residual"] = np.where(
        expand_vol, _sign_nz(resid), np.where(compress_bb, -_sign_nz(resid), 0.0)
    )
    drift = sma(r, 24)
    out["mix_drift_theta"] = np.where(np.abs(drift) >= DRIFT_TH, _sign_nz(drift), 0.0)
    out["mix_turtle_hurst"] = np.where(
        hurst >= HURST_TREND,
        np.where(break_up, 1.0, np.where(break_dn, -1.0, 0.0)),
        np.where(hurst <= HURST_MR, _band_fade(c, ll, hh, np.ones(n, dtype=bool)), 0.0),
    )
    w = np.clip(np.nan_to_num(er, nan=0.0), 0.0, 1.0)
    raw = w * _sign_nz(slope) + (1.0 - w) * (-_sign_nz(c - sma48))
    out["mix_er_blend"] = np.where(np.abs(raw) >= BLEND_TH, _sign_nz(raw), 0.0)

    for k in IDEA_IDS:
        out[k] = np.nan_to_num(out[k], nan=0.0)
    return out


def channel_levels(
    ohlcv: pd.DataFrame, idea: str, *, timeframe: str = "1h"
) -> tuple[np.ndarray, np.ndarray] | None:
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    if idea in ("surf_bb_band", "surf_bb_mid", "surf_linreg_channel", "surf_tp_vwap"):
        blo, bmid, bhi, _ = bollinger(c)
        if idea == "surf_bb_mid":
            return bmid - (bhi - blo) * 0.25, bmid + (bhi - blo) * 0.25
        if idea == "surf_tp_vwap":
            tp = (h + l + c) / 3.0
            vwap = sma(tp, 96)
            sd = pd.Series(tp - vwap).rolling(96, min_periods=96).std(ddof=0).to_numpy()
            return vwap - 2.0 * sd, vwap + 2.0 * sd
        if idea == "surf_linreg_channel":
            mid = sma(c, 20)
            sd = pd.Series(c - mid).rolling(20, min_periods=20).std(ddof=0).to_numpy()
            return mid - 2.0 * sd, mid + 2.0 * sd
        return blo, bhi
    if idea in ("surf_keltner_band", "surf_keltner_mid"):
        klo, kmid, khi = keltner_channel(h, l, c)
        if idea == "surf_keltner_mid":
            return kmid - (khi - klo) * 0.25, kmid + (khi - klo) * 0.25
        return klo, khi
    if idea == "surf_daily_pivot":
        pn = int(PIVOT_BARS.get(timeframe, 24))
        return (
            pd.Series(l).rolling(pn, min_periods=pn).min().shift(1).to_numpy(),
            pd.Series(h).rolling(pn, min_periods=pn).max().shift(1).to_numpy(),
        )
    if idea in ("surf_donchian_band", "mix_turtle_hurst"):
        return donchian_prior(h, l, 20)
    if idea == "surf_inside_mother":
        return np.roll(l, 1), np.roll(h, 1)
    if idea == "surf_range_compress":
        return (
            pd.Series(l).rolling(8, min_periods=8).min().to_numpy(),
            pd.Series(h).rolling(8, min_periods=8).max().to_numpy(),
        )
    return None


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    _, _, _, bwid = bollinger(c)
    return pd.DataFrame(
        {
            "bar_return": _ret(c),
            "efficiency_ratio": kaufman_efficiency_ratio(c, 10),
            "bb_width": bwid,
            "atr_frac": wilder_atr(h, l, c, 14) / np.where(c > 0, c, np.nan),
        },
        index=ohlcv.index,
    )
