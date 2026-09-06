"""Hunt 009 causal ideas: invented time-series formulas (not a 004–008 retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import ema, kaufman_efficiency_ratio, sma, wilder_atr
from llm2.ml_lab.causal_math import (
    BICO_Z,
    CENT_Q,
    FRAC_D,
    FRAC_LAGS,
    HL_FAST,
    HL_SLOW,
    PRED_TH,
    SPEC_W,
    TEAGER_Z,
    WIN,
    Z_FIRE,
    ar2_next_pred,
    bar_return,
    bicoherence_proxy,
    fracdiff,
    log_price,
    ou_half_life,
    permutation_entropy,
    sgolay_slope,
    sgolay_value,
    sign_nz,
    spectral_centroid,
    spectral_log_slope,
    teager_causal,
    zscore,
)

IDEA_IDS_F: tuple[str, ...] = (
    "fracdiff_fade",
    "quad_resid_fade",
    "quad_slope_follow",
    "spec_centroid_switch",
    "teager_exhaust_fade",
    "ar2_pred_follow",
    "ou_halflife_switch",
    "bicoherence_fade",
    "perm_entropy_switch",
    "spec_log_slope_switch",
    "lag_beta_residual",
    "value_pullback_er",
)


def _state(ohlcv: pd.DataFrame) -> dict[str, np.ndarray]:
    c = ohlcv["close"].to_numpy(dtype=float)
    r = bar_return(c)
    lp = log_price(c)
    fd = fracdiff(lp, d=FRAC_D, n_lags=FRAC_LAGS)
    sg = sgolay_value(lp)
    slope = sgolay_slope(lp)
    cent = spectral_centroid(r, width=SPEC_W)
    slope_spec = spectral_log_slope(r, width=SPEC_W)
    perm = permutation_entropy(r)
    psi = teager_causal(r)
    pred = ar2_next_pred(r)
    hl, z_ou = ou_half_life(lp)
    bico = bicoherence_proxy(r)
    return {
        "close": c,
        "ret": r,
        "logp": lp,
        "fracdiff": fd,
        "frac_z": zscore(fd),
        "sg_val": sg,
        "sg_resid": lp - sg,
        "sg_slope": slope,
        "centroid": cent,
        "spec_slope": slope_spec,
        "perm_ent": perm,
        "teager": psi,
        "teager_z": zscore(psi),
        "ar2_pred": pred,
        "ou_hl": hl,
        "ou_z": z_ou,
        "bico": bico,
        "bico_z": zscore(bico),
    }


def fracdiff_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade extremes of a causal fractional difference of log-price (memory residual)."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["frac_z"]
    out = np.zeros(z.size, dtype=np.float64)
    out[z >= Z_FIRE] = -1.0
    out[z <= -Z_FIRE] = 1.0
    return out


def quad_resid_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade when log-price sits far from a causal quadratic Savitzky–Golay fit."""
    del timeframe
    st = st or _state(ohlcv)
    z = zscore(st["sg_resid"])
    out = np.zeros(z.size, dtype=np.float64)
    out[z >= Z_FIRE] = -1.0
    out[z <= -Z_FIRE] = 1.0
    return out


def quad_slope_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow the last-point slope of the same causal quadratic fit."""
    del timeframe
    st = st or _state(ohlcv)
    z = zscore(st["sg_slope"])
    out = np.zeros(z.size, dtype=np.float64)
    out[z >= Z_FIRE] = 1.0
    out[z <= -Z_FIRE] = -1.0
    return out


def spec_centroid_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """High rolling-FFT centroid: fade. Low centroid: follow the 8-bar return."""
    del timeframe
    st = st or _state(ohlcv)
    c = st["close"]
    cent = st["centroid"]
    med = pd.Series(cent).rolling(WIN, min_periods=WIN).quantile(CENT_Q).to_numpy(dtype=float)
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    sma = pd.Series(c).rolling(20, min_periods=20).mean().to_numpy(dtype=float)
    noisy = np.isfinite(cent) & np.isfinite(med) & (cent >= med)
    quiet = np.isfinite(cent) & np.isfinite(med) & (cent < med)
    out = np.zeros(c.size, dtype=np.float64)
    out[noisy] = -sign_nz(c - sma)[noisy]
    out[quiet] = sign_nz(r8)[quiet]
    return out


def teager_exhaust_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade after a causal Teager energy spike collapses."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["teager_z"]
    z2 = np.roll(z, 2)
    z2[:2] = np.nan
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = (z2 >= TEAGER_Z) & np.isfinite(z) & (z <= 0.50)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def ar2_pred_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow a causal two-lag Yule–Walker one-step return forecast."""
    del timeframe
    st = st or _state(ohlcv)
    p = st["ar2_pred"]
    out = np.zeros(p.size, dtype=np.float64)
    out[p >= PRED_TH] = 1.0
    out[p <= -PRED_TH] = -1.0
    return out


def ou_halflife_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fast Ornstein–Uhlenbeck half-life: fade z-score. Slow: follow 8-bar drift."""
    del timeframe
    st = st or _state(ohlcv)
    hl, z = st["ou_hl"], st["ou_z"]
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    out = np.zeros(z.size, dtype=np.float64)
    fade = np.isfinite(hl) & (hl <= HL_FAST) & np.isfinite(z) & (np.abs(z) >= Z_FIRE)
    follow = np.isfinite(hl) & (hl >= HL_SLOW)
    out[fade] = -sign_nz(z)[fade]
    out[follow] = sign_nz(r8)[follow]
    return out


def bicoherence_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade when a causal three-lag product (bicoherence proxy) is extreme."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["bico_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    out = np.zeros(z.size, dtype=np.float64)
    fire = np.isfinite(z) & (np.abs(z) >= BICO_Z)
    out[fire] = -sign_nz(r3)[fire]
    return out


def perm_entropy_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """High Bandt–Pompe entropy: fade versus a 20-bar mean. Low entropy: follow 8-bar drift."""
    del timeframe
    st = st or _state(ohlcv)
    c = st["close"]
    ent = st["perm_ent"]
    z = zscore(ent)
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    mid = pd.Series(c).rolling(20, min_periods=20).mean().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    noisy = np.isfinite(z) & (z >= Z_FIRE)
    quiet = np.isfinite(z) & (z <= -Z_FIRE)
    out[noisy] = -sign_nz(c - mid)[noisy]
    out[quiet] = sign_nz(r8)[quiet]
    return out


def spec_log_slope_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Redder rolling spectrum (more negative log-log slope): follow. Whiter: fade."""
    del timeframe
    st = st or _state(ohlcv)
    c = st["close"]
    z = zscore(st["spec_slope"])
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    mid = pd.Series(c).rolling(20, min_periods=20).mean().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    red = np.isfinite(z) & (z <= -Z_FIRE)
    white = np.isfinite(z) & (z >= Z_FIRE)
    out[red] = sign_nz(r8)[red]
    out[white] = -sign_nz(c - mid)[white]
    return out


def lag_beta_residual(ohlcv: pd.DataFrame, other_close: np.ndarray | None = None) -> np.ndarray:
    """Answer A: residual vs one-bar-lagged Bitcoin/Ether, z-fired."""
    r = bar_return(ohlcv["close"].to_numpy(dtype=float))
    n = r.size
    out = np.zeros(n, dtype=np.float64)
    if other_close is None or np.asarray(other_close).size != n:
        return out
    oth = bar_return(np.asarray(other_close, dtype=float))
    oth_lag = np.roll(oth, 1)
    oth_lag[0] = np.nan
    beta = pd.Series(r).rolling(96, min_periods=96).cov(pd.Series(oth_lag)) / pd.Series(
        oth_lag
    ).rolling(96, min_periods=96).var(ddof=0).replace(0, np.nan)
    resid = r - beta.to_numpy(dtype=float) * oth_lag
    z = zscore(resid)
    fire = np.isfinite(z) & (np.abs(z) >= Z_FIRE)
    out[fire] = -sign_nz(resid)[fire]
    return out


def value_pullback_er(ohlcv: pd.DataFrame) -> np.ndarray:
    """Answer A: maker pullback to SMA(48) only while Kaufman efficiency is high."""
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    mid = sma(c, 48)
    er = kaufman_efficiency_ratio(c, 10)
    slope = ema(c, 12) - ema(c, 48)
    dist = (c - mid) / np.where(atr > 0, atr, np.nan)
    long_ok = (er >= 0.40) & (slope > 0) & (dist <= 0.35) & (dist >= -0.50)
    short_ok = (er >= 0.40) & (slope < 0) & (dist >= -0.35) & (dist <= 0.50)
    out = np.zeros(c.size, dtype=np.float64)
    out[long_ok] = 1.0
    out[short_ok] = -1.0
    return out


def signals_f(
    ohlcv: pd.DataFrame, timeframe: str, other_close: np.ndarray | None = None
) -> dict[str, np.ndarray]:
    st = _state(ohlcv)
    return {
        "fracdiff_fade": fracdiff_fade(ohlcv, timeframe, st=st),
        "quad_resid_fade": quad_resid_fade(ohlcv, timeframe, st=st),
        "quad_slope_follow": quad_slope_follow(ohlcv, timeframe, st=st),
        "spec_centroid_switch": spec_centroid_switch(ohlcv, timeframe, st=st),
        "teager_exhaust_fade": teager_exhaust_fade(ohlcv, timeframe, st=st),
        "ar2_pred_follow": ar2_pred_follow(ohlcv, timeframe, st=st),
        "ou_halflife_switch": ou_halflife_switch(ohlcv, timeframe, st=st),
        "bicoherence_fade": bicoherence_fade(ohlcv, timeframe, st=st),
        "perm_entropy_switch": perm_entropy_switch(ohlcv, timeframe, st=st),
        "spec_log_slope_switch": spec_log_slope_switch(ohlcv, timeframe, st=st),
        "lag_beta_residual": lag_beta_residual(ohlcv, other_close),
        "value_pullback_er": value_pullback_er(ohlcv),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    """Dense causal state (sparse ±1 fires would miss a tip-shape shock)."""
    del kwargs
    st = _state(ohlcv)
    c = ohlcv["close"].to_numpy(dtype=float)
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    atr = wilder_atr(h, l, c, 14)
    mid = sma(c, 48)
    with np.errstate(divide="ignore", invalid="ignore"):
        sma_dist = (c - mid) / np.where(atr > 0, atr, np.nan)
    return pd.DataFrame(
        {
            "bar_return": st["ret"],
            "fracdiff": st["fracdiff"],
            "sg_resid": st["sg_resid"],
            "sg_slope": st["sg_slope"],
            "centroid": st["centroid"],
            "spec_slope": st["spec_slope"],
            "perm_ent": st["perm_ent"],
            "teager": st["teager"],
            "ar2_pred": st["ar2_pred"],
            "ou_hl": st["ou_hl"],
            "bico": st["bico"],
            "er_10": kaufman_efficiency_ratio(c, 10),
            "sma48_atr_dist": sma_dist,
        },
        index=ohlcv.index,
    )
