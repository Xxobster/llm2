"""Causal time-series primitives (past-only, vectorized).

Rolling windows and finite impulse response filters only. No centered
windows, no full-history Fourier transform, no future bars.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

WIN = 64
FRAC_D = 0.40
FRAC_LAGS = 48
SG_M = 17
SPEC_W = 64
AR_WIN = 64
TEAGER_Z = 1.80
Z_FIRE = 1.50
HL_FAST = 12.0
HL_SLOW = 40.0
CENT_Q = 0.60
BICO_Z = 1.60
PRED_TH = 0.0008
PERM_DIM = 3
PERM_WIN = 64


def log_price(close: np.ndarray) -> np.ndarray:
    c = np.asarray(close, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.log(np.where(c > 0.0, c, np.nan))


def bar_return(close: np.ndarray) -> np.ndarray:
    c = np.asarray(close, dtype=np.float64)
    r = np.full(c.size, np.nan)
    with np.errstate(divide="ignore", invalid="ignore"):
        r[1:] = c[1:] / np.where(c[:-1] > 0.0, c[:-1], np.nan) - 1.0
    return r


def zscore(x: np.ndarray, win: int = WIN) -> np.ndarray:
    s = pd.Series(x)
    mu = s.rolling(win, min_periods=win).mean()
    sd = s.rolling(win, min_periods=win).std(ddof=0)
    return ((s - mu) / sd.replace(0.0, np.nan)).to_numpy(dtype=float)


def fracdiff(x: np.ndarray, d: float = FRAC_D, n_lags: int = FRAC_LAGS) -> np.ndarray:
    """Causal truncated binomial filter for (1-L)^d."""
    x = np.asarray(x, dtype=np.float64)
    n = x.size
    out = np.full(n, np.nan)
    w = np.empty(n_lags, dtype=np.float64)
    w[0] = 1.0
    for k in range(1, n_lags):
        w[k] = w[k - 1] * (k - 1 - d) / k
    if n < n_lags:
        return out
    windows = sliding_window_view(x, n_lags)
    out[n_lags - 1 :] = windows[:, ::-1] @ w
    return out


def causal_poly_weights(m: int, degree: int, deriv: int = 0) -> np.ndarray:
    """Weights so yhat[t] = w · x[t-m+1 : t+1] from a causal polynomial fit."""
    t = np.arange(m, dtype=np.float64)
    v = np.vander(t, N=degree + 1, increasing=True)
    gram = v.T @ v
    inv = np.linalg.inv(gram)
    coef = np.zeros(degree + 1, dtype=np.float64)
    t_last = t[-1]
    if deriv == 0:
        coef[:] = v[-1]
    elif deriv == 1:
        for k in range(1, degree + 1):
            coef[k] = k * (t_last ** (k - 1))
    else:
        raise ValueError("deriv must be 0 or 1")
    return coef @ inv @ v.T


_SG_VAL = causal_poly_weights(SG_M, 2, deriv=0)
_SG_SLOPE = causal_poly_weights(SG_M, 2, deriv=1)


def apply_causal_fir(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    w = np.asarray(w, dtype=np.float64)
    n = x.size
    m = int(w.size)
    out = np.full(n, np.nan)
    if n < m:
        return out
    out[m - 1 :] = sliding_window_view(x, m) @ w
    return out


def sgolay_value(x: np.ndarray) -> np.ndarray:
    return apply_causal_fir(x, _SG_VAL)


def sgolay_slope(x: np.ndarray) -> np.ndarray:
    return apply_causal_fir(x, _SG_SLOPE)


def teager_causal(r: np.ndarray) -> np.ndarray:
    """psi[t] = r[t-1]^2 - r[t-2] r[t] (no future bar)."""
    r = np.asarray(r, dtype=np.float64)
    psi = np.full(r.size, np.nan)
    if r.size >= 3:
        psi[2:] = r[1:-1] ** 2 - r[:-2] * r[2:]
    return psi


def spectral_centroid(r: np.ndarray, width: int = SPEC_W) -> np.ndarray:
    r = np.nan_to_num(np.asarray(r, dtype=np.float64), nan=0.0)
    n = r.size
    out = np.full(n, np.nan)
    if n < width:
        return out
    hann = np.hanning(width)
    spec = np.abs(np.fft.rfft(sliding_window_view(r, width) * hann, axis=1)) ** 2
    freqs = np.fft.rfftfreq(width)
    den = spec.sum(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        out[width - 1 :] = (spec @ freqs) / np.where(den > 1e-15, den, np.nan)
    return out


def spectral_log_slope(r: np.ndarray, width: int = SPEC_W) -> np.ndarray:
    """Causal log-log slope of the rolling real-FFT power spectrum (1/f proxy)."""
    r = np.nan_to_num(np.asarray(r, dtype=np.float64), nan=0.0)
    n = r.size
    out = np.full(n, np.nan)
    if n < width:
        return out
    hann = np.hanning(width)
    spec = np.abs(np.fft.rfft(sliding_window_view(r, width) * hann, axis=1)) ** 2
    freqs = np.fft.rfftfreq(width)
    mask = freqs > 0.0
    logf = np.log(freqs[mask])
    logf_c = logf - logf.mean()
    den = float(logf_c @ logf_c)
    if den <= 1e-18:
        return out
    logp = np.log(spec[:, mask] + 1e-18)
    out[width - 1 :] = (logp * logf_c).sum(axis=1) / den
    return out


def permutation_entropy(
    x: np.ndarray, dim: int = PERM_DIM, win: int = PERM_WIN
) -> np.ndarray:
    """Causal Bandt–Pompe permutation entropy of a rolling window."""
    x = np.asarray(x, dtype=np.float64)
    n = x.size
    out = np.full(n, np.nan)
    if n < dim or dim < 2:
        return out
    ranks = np.argsort(np.argsort(sliding_window_view(x, dim), axis=1), axis=1)
    base = dim ** np.arange(dim, dtype=np.int64)
    codes = (ranks * base).sum(axis=1)
    n_codes = int(dim**dim)
    oh = (codes[:, None] == np.arange(n_codes, dtype=np.int64)[None, :]).astype(np.float64)
    p = pd.DataFrame(oh).rolling(win, min_periods=win).mean().to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        ent = -np.where(p > 0.0, p * np.log(p), 0.0).sum(axis=1)
    out[dim - 1 :] = ent
    return out


def ar2_next_pred(r: np.ndarray, win: int = AR_WIN) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    r1 = np.roll(r, 1)
    r2 = np.roll(r, 2)
    r1[0] = np.nan
    r2[:2] = np.nan
    s = pd.Series(r)
    g0 = s.rolling(win, min_periods=win).var(ddof=0)
    g1 = s.rolling(win, min_periods=win).cov(pd.Series(r1))
    g2 = s.rolling(win, min_periods=win).cov(pd.Series(r2))
    det = g0 * g0 - g1 * g1
    with np.errstate(divide="ignore", invalid="ignore"):
        a1 = (g0 * g1 - g1 * g2) / det.replace(0.0, np.nan)
        a2 = (g0 * g2 - g1 * g1) / det.replace(0.0, np.nan)
        pred = a1.to_numpy(dtype=float) * r + a2.to_numpy(dtype=float) * r1
    return pred


def ou_half_life(logp: np.ndarray, win: int = WIN) -> tuple[np.ndarray, np.ndarray]:
    s = pd.Series(logp)
    mu = s.rolling(win, min_periods=win).mean()
    d = s - mu
    ar1 = d.rolling(win, min_periods=win).corr(d.shift(1)).to_numpy(dtype=float)
    z = (d / d.rolling(win, min_periods=win).std(ddof=0).replace(0.0, np.nan)).to_numpy(
        dtype=float
    )
    rho = np.clip(np.abs(ar1), 1e-6, 0.999)
    with np.errstate(divide="ignore", invalid="ignore"):
        hl = -np.log(2.0) / np.log(rho)
    return hl, z


def bicoherence_proxy(r: np.ndarray, lag: int = 4, win: int = WIN) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    a = np.roll(r, lag)
    b = np.roll(r, 2 * lag)
    a[:lag] = np.nan
    b[: 2 * lag] = np.nan
    prod = r * a * b
    num = pd.Series(prod).rolling(win, min_periods=win).mean()
    den = pd.Series(np.abs(r)).rolling(win, min_periods=win).mean() ** 3
    with np.errstate(divide="ignore", invalid="ignore"):
        return (num / den.replace(0.0, np.nan)).to_numpy(dtype=float)


def sign_nz(x: np.ndarray) -> np.ndarray:
    s = np.sign(np.asarray(x, dtype=float))
    return np.where(np.isfinite(s) & (s != 0.0), s, 0.0)


def hurst_rs(r: np.ndarray, width: int = WIN) -> np.ndarray:
    """Single-scale causal rescaled-range Hurst proxy on a rolling window."""
    r = np.nan_to_num(np.asarray(r, dtype=np.float64), nan=0.0)
    n = r.size
    out = np.full(n, np.nan)
    if n < width:
        return out
    w = sliding_window_view(r, width)
    d = w - w.mean(axis=1, keepdims=True)
    z = np.cumsum(d, axis=1)
    rng = z.max(axis=1) - z.min(axis=1)
    sd = w.std(axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        rs = rng / np.where(sd > 1e-15, sd, np.nan)
        out[width - 1 :] = np.log(np.where(rs > 0.0, rs, np.nan)) / np.log(float(width))
    return out


def realized_quarticity(r: np.ndarray, win: int = WIN) -> np.ndarray:
    x = np.asarray(r, dtype=np.float64) ** 4
    return pd.Series(x).rolling(win, min_periods=win).mean().to_numpy(dtype=float)


def amihud_illiquidity(r: np.ndarray, volume: np.ndarray, win: int = WIN) -> np.ndarray:
    r = np.asarray(r, dtype=np.float64)
    v = np.asarray(volume, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        illiq = np.abs(r) / np.where(v > 0.0, v, np.nan)
    return pd.Series(illiq).rolling(win, min_periods=win).mean().to_numpy(dtype=float)


def rolling_skew(x: np.ndarray, win: int = WIN) -> np.ndarray:
    return pd.Series(x).rolling(win, min_periods=win).skew().to_numpy(dtype=float)


def ewm_resid(logp: np.ndarray, span: int = 32) -> np.ndarray:
    s = pd.Series(np.asarray(logp, dtype=np.float64))
    return (s - s.ewm(span=span, min_periods=span, adjust=False).mean()).to_numpy(dtype=float)


HILB_M = 31
KALMAN_LVL = 32
KALMAN_VEL = 16
KALMAN_ACC = 8
HAAR_SHORT = 1
HAAR_LONG = 8
DFA_W = 64
FISH_WIN = 64


def hilbert_fir_weights(m: int = HILB_M) -> np.ndarray:
    """Odd-length windowed Type-III Hilbert FIR (applied causally, delay m//2)."""
    m = int(m)
    if m < 3 or m % 2 == 0:
        raise ValueError("Hilbert length must be odd and >= 3")
    n = np.arange(m, dtype=np.float64) - (m // 2)
    w = np.zeros(m, dtype=np.float64)
    odd = n % 2 != 0.0
    w[odd] = 2.0 / (np.pi * n[odd])
    w *= np.hanning(m)
    return w


_HILB_W = hilbert_fir_weights(HILB_M)


def analytic_pair(x: np.ndarray, m: int = HILB_M) -> tuple[np.ndarray, np.ndarray]:
    """Causal in-phase (delayed) and quadrature pair. Both use only x[t-m+1:t+1]."""
    x = np.asarray(x, dtype=np.float64)
    delay = int(m) // 2
    ip = np.full(x.size, np.nan)
    if x.size > delay:
        ip[delay:] = x[: x.size - delay]
    quad = apply_causal_fir(x, hilbert_fir_weights(m) if m != HILB_M else _HILB_W)
    return ip, quad


def inst_amplitude(x: np.ndarray, m: int = HILB_M) -> np.ndarray:
    ip, quad = analytic_pair(x, m=m)
    return np.sqrt(ip * ip + quad * quad)


def inst_frequency(x: np.ndarray, m: int = HILB_M) -> np.ndarray:
    """Causal one-bar phase increment of the delayed analytic signal (radians / bar)."""
    ip, quad = analytic_pair(x, m=m)
    ok = np.isfinite(ip) & np.isfinite(quad)
    phase = np.where(ok, np.arctan2(quad, ip), 0.0)
    unw = np.unwrap(phase)
    freq = np.full(x.size, np.nan)
    freq[1:] = np.diff(unw)
    freq = np.where(ok, freq, np.nan)
    return freq


def hjorth_mobility(x: np.ndarray, win: int = WIN) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    dx = np.full(x.size, np.nan)
    dx[1:] = np.diff(x)
    vx = pd.Series(x).rolling(win, min_periods=win).var(ddof=0)
    vd = pd.Series(dx).rolling(win, min_periods=win).var(ddof=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.sqrt((vd / vx.replace(0.0, np.nan)).to_numpy(dtype=float))


def hjorth_complexity(x: np.ndarray, win: int = WIN) -> np.ndarray:
    dx = np.full(np.asarray(x).size, np.nan)
    dx[1:] = np.diff(np.asarray(x, dtype=np.float64))
    m1 = hjorth_mobility(x, win=win)
    m2 = hjorth_mobility(dx, win=win)
    with np.errstate(divide="ignore", invalid="ignore"):
        return m2 / np.where(np.isfinite(m1) & (m1 > 0.0), m1, np.nan)


def robust_end_slope(x: np.ndarray, width: int = WIN) -> np.ndarray:
    """Causal Theil–Sen-style slope: median of (x[t]-x[t-k])/k for k=1..width/2."""
    x = np.asarray(x, dtype=np.float64)
    n = x.size
    out = np.full(n, np.nan)
    if n < width:
        return out
    w = sliding_window_view(x, width)
    ks = np.arange(1, width // 2 + 1, dtype=np.int64)
    slopes = (w[:, -1][:, None] - w[:, -1 - ks]) / ks.astype(np.float64)
    out[width - 1 :] = np.median(slopes, axis=1)
    return out


def haar_energy_ratio(
    x: np.ndarray, win: int = WIN, short: int = HAAR_SHORT, long: int = HAAR_LONG
) -> np.ndarray:
    """Causal Haar-like energy: 1-bar detail vs 8-bar detail, rolling mean of squares."""
    x = np.asarray(x, dtype=np.float64)
    d_s = np.full(x.size, np.nan)
    d_l = np.full(x.size, np.nan)
    d_s[short:] = x[short:] - x[:-short]
    d_l[long:] = x[long:] - x[:-long]
    e_s = pd.Series(d_s * d_s).rolling(win, min_periods=win).mean()
    e_l = pd.Series(d_l * d_l).rolling(win, min_periods=win).mean() / float(long)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (e_s / e_l.replace(0.0, np.nan)).to_numpy(dtype=float)


def kinematic_accel(logp: np.ndarray) -> np.ndarray:
    """Causal 3-span exponential kinematic filter: level → velocity → acceleration."""
    s = pd.Series(np.asarray(logp, dtype=np.float64))
    lvl = s.ewm(span=KALMAN_LVL, min_periods=KALMAN_LVL, adjust=False).mean()
    vel = lvl.diff().ewm(span=KALMAN_VEL, min_periods=KALMAN_VEL, adjust=False).mean()
    acc = vel.diff().ewm(span=KALMAN_ACC, min_periods=KALMAN_ACC, adjust=False).mean()
    return acc.to_numpy(dtype=float)


def fisher_rank(x: np.ndarray, win: int = FISH_WIN) -> np.ndarray:
    """Fisher transform of the causal rolling rank of x[t] inside the last `win` bars."""
    x = np.asarray(x, dtype=np.float64)
    n = x.size
    out = np.full(n, np.nan)
    if n < win:
        return out
    w = sliding_window_view(x, win)
    p = (w <= w[:, -1][:, None]).mean(axis=1)
    p = np.clip(p, 1e-4, 1.0 - 1e-4)
    z = 2.0 * p - 1.0
    out[win - 1 :] = 0.5 * np.log((1.0 + z) / (1.0 - z))
    return out


def volterra_quad_resid(r: np.ndarray, win: int = WIN) -> np.ndarray:
    """Residual of causal rolling r[t] ~ a r[t-1] + b r[t-1]^2 (quadratic Volterra)."""
    r = np.asarray(r, dtype=np.float64)
    x1 = np.roll(r, 1)
    x1[0] = np.nan
    x2 = x1 * x1
    y = r
    e11 = pd.Series(x1 * x1).rolling(win, min_periods=win).mean()
    e22 = pd.Series(x2 * x2).rolling(win, min_periods=win).mean()
    e12 = pd.Series(x1 * x2).rolling(win, min_periods=win).mean()
    e1y = pd.Series(x1 * y).rolling(win, min_periods=win).mean()
    e2y = pd.Series(x2 * y).rolling(win, min_periods=win).mean()
    det = e11 * e22 - e12 * e12
    with np.errstate(divide="ignore", invalid="ignore"):
        a = (e22 * e1y - e12 * e2y) / det.replace(0.0, np.nan)
        b = (e11 * e2y - e12 * e1y) / det.replace(0.0, np.nan)
        pred = a.to_numpy(dtype=float) * x1 + b.to_numpy(dtype=float) * x2
    return y - pred


def dfa_alpha(r: np.ndarray, width: int = DFA_W) -> np.ndarray:
    """Single-scale causal Detrended Fluctuation Analysis exponent on a rolling window."""
    r = np.nan_to_num(np.asarray(r, dtype=np.float64), nan=0.0)
    n = r.size
    out = np.full(n, np.nan)
    if n < width:
        return out
    w = sliding_window_view(r, width)
    d = w - w.mean(axis=1, keepdims=True)
    profile = np.cumsum(d, axis=1)
    t = np.arange(width, dtype=np.float64)
    tc = t - t.mean()
    den = float(tc @ tc)
    if den <= 1e-18:
        return out
    slope = (profile * tc).sum(axis=1) / den
    intercept = profile.mean(axis=1) - slope * t.mean()
    resid = profile - (slope[:, None] * t + intercept[:, None])
    fluc = np.sqrt((resid * resid).mean(axis=1))
    with np.errstate(divide="ignore", invalid="ignore"):
        out[width - 1 :] = np.log(np.where(fluc > 1e-15, fluc, np.nan)) / np.log(float(width))
    return out


def delay_divergence(r: np.ndarray, lag: int = 2) -> np.ndarray:
    """Euclidean step length in a 2-delay embedding (local trajectory divergence)."""
    r = np.asarray(r, dtype=np.float64)
    r1 = np.roll(r, 1)
    r2 = np.roll(r, lag)
    r3 = np.roll(r, lag + 1)
    r1[0] = np.nan
    r2[:lag] = np.nan
    r3[: lag + 1] = np.nan
    return np.sqrt((r - r1) ** 2 + (r2 - r3) ** 2)
