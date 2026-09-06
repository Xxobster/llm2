"""Hunt 013 causal ideas: third invented formula pack (not a 009/011 retune).

Every signal is +1 / 0 / −1 from completed bars only. Thresholds are module
constants, not searched on profit factor.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.autonomy.public_formulas import wilder_atr
from llm2.ml_lab.causal_math import (
    WIN,
    Z_FIRE,
    bar_return,
    dfa_alpha,
    delay_divergence,
    fisher_rank,
    haar_energy_ratio,
    hjorth_mobility,
    inst_amplitude,
    inst_frequency,
    kinematic_accel,
    log_price,
    robust_end_slope,
    sign_nz,
    volterra_quad_resid,
    zscore,
)

DFA_TREND = 0.58
DFA_MR = 0.42
HJ_HIGH = 1.15
HJ_LOW = 0.85
IF_Q = 0.40
SLOPE_Z = 1.20
FISH_FIRE = 1.20
DIV_Z = 1.80

IDEA_IDS_J: tuple[str, ...] = (
    "hilbert_amp_fade",
    "inst_freq_follow",
    "hjorth_mobility_switch",
    "robust_slope_follow",
    "haar_energy_fade",
    "kalman_accel_follow",
    "fisher_rank_fade",
    "volterra_resid_fade",
    "dfa_alpha_switch",
    "delay_div_fade",
)


def _state(ohlcv: pd.DataFrame) -> dict[str, np.ndarray]:
    h = ohlcv["high"].to_numpy(dtype=float)
    l = ohlcv["low"].to_numpy(dtype=float)
    c = ohlcv["close"].to_numpy(dtype=float)
    r = bar_return(c)
    lp = log_price(c)
    atr = wilder_atr(h, l, c, 14)
    amp = inst_amplitude(lp)
    ifr = inst_frequency(lp)
    mob = hjorth_mobility(lp)
    slope = robust_end_slope(lp)
    haar = haar_energy_ratio(lp)
    acc = kinematic_accel(lp)
    fish = fisher_rank(lp)
    volt = volterra_quad_resid(r)
    dfa = dfa_alpha(r)
    div = delay_divergence(r)
    return {
        "close": c,
        "ret": r,
        "logp": lp,
        "atr": atr,
        "amp": amp,
        "amp_z": zscore(amp),
        "ifr": ifr,
        "mob": mob,
        "slope": slope,
        "slope_z": zscore(slope),
        "haar": haar,
        "haar_z": zscore(haar),
        "acc": acc,
        "acc_z": zscore(acc),
        "fish": fish,
        "volt": volt,
        "volt_z": zscore(volt),
        "dfa": dfa,
        "div": div,
        "div_z": zscore(div),
    }


def hilbert_amp_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade a 3-bar move when the causal Hilbert envelope is extreme."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["amp_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = np.isfinite(z) & (z >= Z_FIRE)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def inst_freq_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow 8-bar drift when instantaneous frequency is in the slow (low) quartile."""
    del timeframe
    st = st or _state(ohlcv)
    ifr = st["ifr"]
    q = pd.Series(np.abs(ifr)).rolling(WIN, min_periods=WIN).quantile(IF_Q).to_numpy(dtype=float)
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    slow = np.isfinite(ifr) & np.isfinite(q) & (np.abs(ifr) <= q)
    out = np.zeros(ifr.size, dtype=np.float64)
    out[slow] = sign_nz(r8)[slow]
    return out


def hjorth_mobility_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """High Hjorth mobility: follow drift. Low mobility: fade versus a 20-bar mean."""
    del timeframe
    st = st or _state(ohlcv)
    mob = st["mob"]
    med = pd.Series(mob).rolling(WIN, min_periods=WIN).median().to_numpy(dtype=float)
    c = st["close"]
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    mid = pd.Series(c).rolling(20, min_periods=20).mean().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    high = np.isfinite(mob) & np.isfinite(med) & (mob >= med * HJ_HIGH)
    low = np.isfinite(mob) & np.isfinite(med) & (mob <= med * HJ_LOW)
    out[high] = sign_nz(r8)[high]
    out[low] = -sign_nz(c - mid)[low]
    return out


def robust_slope_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow the causal Theil–Sen-style end-point slope when it is extreme."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["slope_z"]
    sl = st["slope"]
    fire = np.isfinite(z) & (np.abs(z) >= SLOPE_Z)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = sign_nz(sl)[fire]
    return out


def haar_energy_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade a 3-bar impulse when the Haar 1-bar / 8-bar energy ratio spikes."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["haar_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = np.isfinite(z) & (z >= Z_FIRE)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def kalman_accel_follow(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Follow the sign of a causal exponential kinematic acceleration when |z| is high."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["acc_z"]
    acc = st["acc"]
    fire = np.isfinite(z) & (np.abs(z) >= Z_FIRE)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = sign_nz(acc)[fire]
    return out


def fisher_rank_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade when the Fisher transform of the rolling log-price rank is extreme."""
    del timeframe
    st = st or _state(ohlcv)
    f = st["fish"]
    out = np.zeros(f.size, dtype=np.float64)
    out[np.isfinite(f) & (f >= FISH_FIRE)] = -1.0
    out[np.isfinite(f) & (f <= -FISH_FIRE)] = 1.0
    return out


def volterra_resid_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade a large residual versus a rolling quadratic Volterra one-step predictor."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["volt_z"]
    out = np.zeros(z.size, dtype=np.float64)
    out[z >= Z_FIRE] = -1.0
    out[z <= -Z_FIRE] = 1.0
    return out


def dfa_alpha_switch(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """High Detrended Fluctuation exponent: follow. Low: fade versus a 20-bar mean."""
    del timeframe
    st = st or _state(ohlcv)
    a = st["dfa"]
    c = st["close"]
    r8 = pd.Series(st["ret"]).rolling(8, min_periods=8).sum().to_numpy(dtype=float)
    mid = pd.Series(c).rolling(20, min_periods=20).mean().to_numpy(dtype=float)
    out = np.zeros(c.size, dtype=np.float64)
    trend = np.isfinite(a) & (a >= DFA_TREND)
    revert = np.isfinite(a) & (a <= DFA_MR)
    out[trend] = sign_nz(r8)[trend]
    out[revert] = -sign_nz(c - mid)[revert]
    return out


def delay_div_fade(ohlcv: pd.DataFrame, timeframe: str | None = None, st: dict | None = None) -> np.ndarray:
    """Fade a 3-bar move after a delay-embedding trajectory-divergence spike."""
    del timeframe
    st = st or _state(ohlcv)
    z = st["div_z"]
    r3 = pd.Series(st["ret"]).rolling(3, min_periods=3).sum().to_numpy(dtype=float)
    fire = np.isfinite(z) & (z >= DIV_Z)
    out = np.zeros(z.size, dtype=np.float64)
    out[fire] = -sign_nz(r3)[fire]
    return out


def signals_j(ohlcv: pd.DataFrame, timeframe: str) -> dict[str, np.ndarray]:
    st = _state(ohlcv)
    return {
        "hilbert_amp_fade": hilbert_amp_fade(ohlcv, timeframe, st=st),
        "inst_freq_follow": inst_freq_follow(ohlcv, timeframe, st=st),
        "hjorth_mobility_switch": hjorth_mobility_switch(ohlcv, timeframe, st=st),
        "robust_slope_follow": robust_slope_follow(ohlcv, timeframe, st=st),
        "haar_energy_fade": haar_energy_fade(ohlcv, timeframe, st=st),
        "kalman_accel_follow": kalman_accel_follow(ohlcv, timeframe, st=st),
        "fisher_rank_fade": fisher_rank_fade(ohlcv, timeframe, st=st),
        "volterra_resid_fade": volterra_resid_fade(ohlcv, timeframe, st=st),
        "dfa_alpha_switch": dfa_alpha_switch(ohlcv, timeframe, st=st),
        "delay_div_fade": delay_div_fade(ohlcv, timeframe, st=st),
    }


def build_features_for_guard(ohlcv: pd.DataFrame, **kwargs) -> pd.DataFrame:
    del kwargs
    st = _state(ohlcv)
    return pd.DataFrame(
        {
            "bar_return": st["ret"],
            "inst_amp": st["amp"],
            "inst_freq": st["ifr"],
            "hjorth_mobility": st["mob"],
            "robust_slope": st["slope"],
            "haar_ratio": st["haar"],
            "kalman_accel": st["acc"],
            "fisher_rank": st["fish"],
            "volterra_resid": st["volt"],
            "dfa_alpha": st["dfa"],
            "delay_div": st["div"],
        },
        index=ohlcv.index,
    )
