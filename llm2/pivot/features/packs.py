"""Causal feature packs for pivot forecasting (OHLCV-only, vectorized)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.pivot.labels.fractal import wilder_atr


def _safe_div(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    out = np.full_like(a, np.nan, dtype=float)
    m = np.isfinite(a) & np.isfinite(b) & (np.abs(b) > 1e-12)
    out[m] = a[m] / b[m]
    return out


def build_feature_frame(ohlcv: pd.DataFrame, *, pack: str = "price_vol") -> pd.DataFrame:
    """Build one of the registered feature packs at each bar (knowable at close)."""
    o = ohlcv["open"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    v = (
        ohlcv["volume"].to_numpy(dtype=float)
        if "volume" in ohlcv.columns
        else np.ones(len(c), dtype=float)
    )
    n = len(c)
    log_ret = np.full(n, np.nan)
    log_ret[1:] = np.log(_safe_div(c[1:], c[:-1]))
    tr_range = _safe_div(h - l, c)
    body = _safe_div(np.abs(c - o), np.maximum(h - l, 1e-12))
    upper_wick = _safe_div(h - np.maximum(o, c), np.maximum(h - l, 1e-12))
    lower_wick = _safe_div(np.minimum(o, c) - l, np.maximum(h - l, 1e-12))
    atr14 = wilder_atr(h, l, c, period=14)
    atr_n = _safe_div(atr14, c)
    # rolling vol
    ret_s = pd.Series(log_ret)
    rv_12 = ret_s.rolling(12, min_periods=6).std().to_numpy()
    rv_48 = ret_s.rolling(48, min_periods=12).std().to_numpy()
    # momentum
    mom_6 = ret_s.rolling(6, min_periods=3).sum().to_numpy()
    mom_24 = ret_s.rolling(24, min_periods=6).sum().to_numpy()
    # distance to rolling high/low
    rh_48 = pd.Series(h).rolling(48, min_periods=12).max().to_numpy()
    rl_48 = pd.Series(l).rolling(48, min_periods=12).min().to_numpy()
    dist_hi = _safe_div(rh_48 - c, atr14)
    dist_lo = _safe_div(c - rl_48, atr14)
    # volume z
    vol_z = (
        (pd.Series(v) - pd.Series(v).rolling(48, min_periods=12).mean())
        / pd.Series(v).rolling(48, min_periods=12).std().replace(0, np.nan)
    ).to_numpy()
    # compression: low RV + narrow range
    range_ma = pd.Series(tr_range).rolling(24, min_periods=8).mean().to_numpy()
    compression = _safe_div(tr_range, range_ma)
    # physics proxies
    velocity = log_ret
    accel = np.full(n, np.nan)
    accel[1:] = velocity[1:] - velocity[:-1]
    jerk = np.full(n, np.nan)
    jerk[1:] = accel[1:] - accel[:-1]
    kinetic = v * (log_ret**2)
    # slope of close (linear over 12 bars) via rolling corr with time — approx first diff mean
    slope_12 = ret_s.rolling(12, min_periods=6).mean().to_numpy()

    base = {
        "log_ret": log_ret,
        "range_n": tr_range,
        "body_ratio": body,
        "upper_wick": upper_wick,
        "lower_wick": lower_wick,
        "atr_n": atr_n,
        "rv_12": rv_12,
        "rv_48": rv_48,
        "vol_z": vol_z,
        "compression": compression,
    }
    mom = {
        "mom_6": mom_6,
        "mom_24": mom_24,
        "slope_12": slope_12,
        "dist_hi_atr": dist_hi,
        "dist_lo_atr": dist_lo,
    }
    physics = {
        "velocity": velocity,
        "accel": accel,
        "jerk": jerk,
        "kinetic": kinetic,
    }
    # lagged returns stack
    lags = {}
    for k in (1, 2, 3, 6, 12):
        lr = np.full(n, np.nan)
        if k < n:
            lr[k:] = log_ret[:-k] if k > 0 else log_ret
            # log_ret already shifted by 1 from close; lag k means look back further
            lr = pd.Series(log_ret).shift(k).to_numpy()
        lags[f"lag_ret_{k}"] = lr

    # Extra causal shape cues for *where* (level) — still OHLCV-only, close-known.
    wick_skew = upper_wick - lower_wick
    close_loc = _safe_div(c - l, np.maximum(h - l, 1e-12))  # 0=low, 1=high of bar
    atr_ch = _safe_div(atr14 - pd.Series(atr14).shift(6).to_numpy(), atr14)
    rh_12 = pd.Series(h).rolling(12, min_periods=6).max().to_numpy()
    rl_12 = pd.Series(l).rolling(12, min_periods=6).min().to_numpy()
    dist_hi_12 = _safe_div(rh_12 - c, atr14)
    dist_lo_12 = _safe_div(c - rl_12, atr14)
    # rolling high/low *return* targets proxies (past only)
    ret_to_hi_12 = _safe_div(rh_12 - c, c)
    ret_to_lo_12 = _safe_div(rl_12 - c, c)
    level_extra = {
        "wick_skew": wick_skew,
        "close_loc": close_loc,
        "atr_ch_6": atr_ch,
        "dist_hi_12_atr": dist_hi_12,
        "dist_lo_12_atr": dist_lo_12,
        "ret_to_hi_12": ret_to_hi_12,
        "ret_to_lo_12": ret_to_lo_12,
    }

    # Causal Volume Spread Analysis (VSA) *proxies* (OHLCV only; no discretionary labels).
    # Knowable at bar close: relative volume, spread vs average, close location, effort vs result.
    vol_ma = pd.Series(v).rolling(48, min_periods=12).mean().to_numpy()
    spread_ma = pd.Series(h - l).rolling(48, min_periods=12).mean().to_numpy()
    rel_vol = _safe_div(v, vol_ma)
    rel_spread = _safe_div(h - l, spread_ma)
    # Effort vs result: high volume + small net progress (possible absorption)
    effort_vs_result = _safe_div(rel_vol, np.maximum(np.abs(log_ret) * 100.0, 1e-6))
    # Wide spread upthrust / selling climax proxies (shape only)
    wide_spread = (rel_spread > 1.5).astype(float)
    high_vol = (rel_vol > 1.5).astype(float)
    close_off_high = _safe_div(h - c, np.maximum(h - l, 1e-12))
    close_off_low = _safe_div(c - l, np.maximum(h - l, 1e-12))
    # No-demand / no-supply-ish: narrow spread + low volume after a move
    narrow_low_vol = ((rel_spread < 0.7) & (rel_vol < 0.7)).astype(float)
    vsa_proxy = {
        "rel_vol_48": rel_vol,
        "rel_spread_48": rel_spread,
        "effort_vs_result": effort_vs_result,
        "wide_spread_flag": wide_spread,
        "high_vol_flag": high_vol,
        "close_off_high": close_off_high,
        "close_off_low": close_off_low,
        "narrow_low_vol_flag": narrow_low_vol,
        "vol_z": vol_z,
        "close_loc": close_loc,
        "wick_skew": wick_skew,
    }

    # Stronger multi-scale shape for level heads (still causal OHLCV).
    rh_6 = pd.Series(h).rolling(6, min_periods=3).max().to_numpy()
    rl_6 = pd.Series(l).rolling(6, min_periods=3).min().to_numpy()
    rh_24 = pd.Series(h).rolling(24, min_periods=8).max().to_numpy()
    rl_24 = pd.Series(l).rolling(24, min_periods=8).min().to_numpy()
    level_strong = {
        "ret_to_hi_6": _safe_div(rh_6 - c, c),
        "ret_to_lo_6": _safe_div(rl_6 - c, c),
        "ret_to_hi_24": _safe_div(rh_24 - c, c),
        "ret_to_lo_24": _safe_div(rl_24 - c, c),
        "range_6_n": _safe_div(rh_6 - rl_6, c),
        "range_24_n": _safe_div(rh_24 - rl_24, c),
        "pos_in_24": _safe_div(c - rl_24, np.maximum(rh_24 - rl_24, 1e-12)),
    }

    packs = {
        "price_vol": base,
        "price_vol_mom": {**base, **mom},
        "price_vol_mom_phys": {**base, **mom, **physics},
        "full": {**base, **mom, **physics, **lags},
        "level_focus": {**base, **mom, **physics, **lags, **level_extra},
        "vsa_proxy": {**base, **mom, **level_extra, **vsa_proxy},
        "level_vsa": {**base, **mom, **physics, **lags, **level_extra, **vsa_proxy},
        "level_strong": {
            **base,
            **mom,
            **physics,
            **lags,
            **level_extra,
            **vsa_proxy,
            **level_strong,
        },
    }
    if pack not in packs:
        raise ValueError(f"unknown feature pack {pack}; choose from {list(packs)}")
    frame = pd.DataFrame(packs[pack], index=ohlcv.index)
    return frame.replace([np.inf, -np.inf], np.nan)
