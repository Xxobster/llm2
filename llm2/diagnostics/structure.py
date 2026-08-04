"""Single-series structure: does this instrument contain any of the classical regularities?

Answers, with numbers rather than model performance: autocorrelation, mean reversion,
momentum, seasonality, regime dependence, volatility clustering, cyclicality and nonlinear
lag structure. The lab previously asked only "can model M predict target T", which conflates
"no structure exists" with "this model did not find it".

Every conditional mean is reported with a Newey-West t-statistic because forward returns
over h bars measured every bar overlap h-fold, which inflates a naive t by roughly sqrt(h).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.stats import (
    Effect,
    apply_fdr,
    bootstrap_corr_test,
    newey_west_tstat,
    normal_two_sided_p,
    safe_corr,
)

# UTC session windows. These are fixed-UTC approximations: the underlying venues shift by an
# hour under daylight saving, so a genuine effect should survive a one-hour perturbation.
SESSIONS = {
    "tokyo": (0, 9),
    "london": (7, 16),
    "newyork": (12, 21),
    "london_ny_overlap": (12, 16),
    "asia_quiet": (21, 24),
}


def forward_log_return(close: pd.Series, horizon: int) -> pd.Series:
    """Return over the next ``horizon`` bars, aligned to the decision bar."""
    log_c = np.log(close.replace(0, np.nan))
    return log_c.shift(-horizon) - log_c


def _bucket_effects(
    forward: pd.Series,
    bucket: pd.Series,
    *,
    prefix: str,
    horizon: int,
    min_count: int = 200,
) -> list[Effect]:
    """Conditional mean forward return per bucket, with overlap-aware significance."""
    effects: list[Effect] = []
    frame = pd.DataFrame({"fwd": forward, "bucket": bucket}).dropna()
    for key, grp in frame.groupby("bucket", observed=True):
        vals = grp["fwd"].to_numpy()
        if vals.size < min_count:
            continue
        mean, t_stat = newey_west_tstat(vals, lags=horizon)
        effects.append(
            Effect(
                name=f"{prefix}[{key}]",
                statistic=float(mean),
                n=int(vals.size),
                p_value=normal_two_sided_p(t_stat),
                detail={"t_hac": float(t_stat), "mean_bps": float(mean * 1e4)},
            )
        )
    return effects


def autocorrelation(close: pd.Series, *, max_lag: int = 48, horizon: int = 6) -> list[Effect]:
    """Linear memory in returns: autocorrelation function, variance ratio, Hurst exponent."""
    ret = np.log(close.replace(0, np.nan)).diff().dropna()
    arr = ret.to_numpy()
    n = arr.size
    effects: list[Effect] = []

    centred = arr - arr.mean()
    denom = float(np.dot(centred, centred))
    for lag in range(1, max_lag + 1):
        if denom <= 0 or n - lag < 100:
            continue
        rho = float(np.dot(centred[lag:], centred[:-lag]) / denom)
        # Bartlett standard error under the null of white noise.
        se = 1.0 / np.sqrt(n)
        effects.append(
            Effect(
                name=f"acf_lag_{lag}",
                statistic=rho,
                n=int(n - lag),
                p_value=normal_two_sided_p(rho / se),
                ci_low=rho - 1.96 * se,
                ci_high=rho + 1.96 * se,
                detail={"lag": float(lag)},
            )
        )

    # Ljung-Box: is the whole first block of autocorrelations jointly zero?
    try:
        from statsmodels.stats.diagnostic import acorr_ljungbox

        lb = acorr_ljungbox(arr, lags=[min(max_lag, 24)], return_df=True)
        effects.append(
            Effect(
                name=f"ljung_box_{min(max_lag, 24)}",
                statistic=float(lb["lb_stat"].iloc[0]),
                n=int(n),
                p_value=float(lb["lb_pvalue"].iloc[0]),
            )
        )
    except Exception:  # noqa: BLE001
        pass

    # Variance ratio: >1 means trending (variance grows faster than linearly), <1 mean
    # reverting. Under a random walk it is 1 at every aggregation.
    for q in (2, 4, 8, 24):
        if n < q * 100:
            continue
        vr, z = _variance_ratio(arr, q)
        effects.append(
            Effect(
                name=f"variance_ratio_{q}",
                statistic=vr,
                n=int(n),
                p_value=normal_two_sided_p(z),
                detail={"z": z, "q": float(q)},
            )
        )

    effects.append(
        Effect(name="hurst_rs", statistic=_hurst(arr), n=int(n), detail={"note_half_is_random_walk": 0.5})
    )
    _ = horizon
    return apply_fdr(effects)


def _variance_ratio(ret: np.ndarray, q: int) -> tuple[float, float]:
    """Lo-MacKinlay variance ratio with the heteroskedasticity-robust test statistic."""
    n = ret.size
    mu = ret.mean()
    var_1 = float(np.sum((ret - mu) ** 2) / (n - 1))
    agg = np.convolve(ret, np.ones(q), mode="valid")
    m = float(q * (n - q + 1) * (1 - q / n))
    var_q = float(np.sum((agg - q * mu) ** 2) / m) if m > 0 else np.nan
    if not np.isfinite(var_1) or var_1 <= 0 or not np.isfinite(var_q):
        return float("nan"), float("nan")
    vr = var_q / var_1

    # Heteroskedasticity-consistent variance of the ratio.
    e2 = (ret - mu) ** 2
    denom = float(np.sum(e2)) ** 2
    theta = 0.0
    for j in range(1, q):
        num = float(np.sum(e2[j:] * e2[:-j])) * n
        delta = num / denom if denom > 0 else 0.0
        theta += ((2.0 * (q - j) / q) ** 2) * delta
    z = (vr - 1.0) / np.sqrt(theta) if theta > 0 else float("nan")
    return float(vr), float(z)


def _hurst(ret: np.ndarray, min_chunk: int = 32) -> float:
    """Rescaled-range Hurst exponent. 0.5 is a random walk, >0.5 persistent."""
    arr = ret[np.isfinite(ret)]
    n = arr.size
    if n < min_chunk * 4:
        return float("nan")
    sizes, rs_vals = [], []
    size = min_chunk
    while size <= n // 2:
        n_chunks = n // size
        chunks = arr[: n_chunks * size].reshape(n_chunks, size)
        dev = chunks - chunks.mean(axis=1, keepdims=True)
        cumdev = np.cumsum(dev, axis=1)
        r = cumdev.max(axis=1) - cumdev.min(axis=1)
        s = chunks.std(axis=1, ddof=1)
        valid = s > 1e-18
        if valid.any():
            sizes.append(size)
            rs_vals.append(float(np.mean(r[valid] / s[valid])))
        size *= 2
    if len(sizes) < 3:
        return float("nan")
    slope = np.polyfit(np.log(sizes), np.log(rs_vals), 1)[0]
    return float(slope)


def mean_reversion(
    ohlcv: pd.DataFrame, *, horizon: int = 6, ema_spans: tuple[int, ...] = (24, 96, 200)
) -> list[Effect]:
    """Does stretch away from a moving average predict a move back toward it?"""
    close = ohlcv["close"]
    fwd = forward_log_return(close, horizon)
    effects: list[Effect] = []

    for span in ema_spans:
        ema = close.ewm(span=span, adjust=False, min_periods=span).mean()
        atr = _atr(ohlcv, 14)
        stretch = (close - ema) / atr.replace(0, np.nan)

        # If stretch predicts reversion the correlation with the forward return is negative.
        eff = bootstrap_corr_test(stretch.to_numpy(), fwd.to_numpy(), n_boot=300, seed=span)
        eff.name = f"stretch_ema{span}_vs_fwd{horizon}"
        effects.append(eff)

        decile = _safe_qcut(stretch, 10, labels=[f"d{i}" for i in range(10)])
        effects.extend(
            _bucket_effects(fwd, decile, prefix=f"fwd{horizon}|stretch_ema{span}", horizon=horizon)
        )

    half_life = _ou_half_life(close)
    effects.append(
        Effect(
            name="ou_half_life_bars",
            statistic=half_life,
            n=int(close.notna().sum()),
            detail={"note_negative_means_trending": -1.0},
        )
    )
    return apply_fdr(effects)


def _ou_half_life(close: pd.Series) -> float:
    """Half-life of an Ornstein-Uhlenbeck fit to log price: -ln(2)/ln(1+beta)."""
    log_c = np.log(close.replace(0, np.nan)).dropna()
    if log_c.size < 500:
        return float("nan")
    y = log_c.diff().dropna()
    x = log_c.shift(1).dropna().loc[y.index]
    xv, yv = x.to_numpy(), y.to_numpy()
    xc = xv - xv.mean()
    denom = float(np.dot(xc, xc))
    if denom <= 0:
        return float("nan")
    beta = float(np.dot(xc, yv - yv.mean()) / denom)
    if beta >= 0 or beta <= -1:
        return float("nan")  # not mean reverting
    return float(-np.log(2.0) / np.log(1.0 + beta))


def momentum(ohlcv: pd.DataFrame, *, horizon: int = 6, lookbacks: tuple[int, ...] = (6, 24, 96)) -> list[Effect]:
    """Does a trailing move predict a continuation?"""
    close = ohlcv["close"]
    fwd = forward_log_return(close, horizon)
    effects: list[Effect] = []

    for lb in lookbacks:
        trail = np.log(close.replace(0, np.nan)).diff(lb)
        eff = bootstrap_corr_test(trail.to_numpy(), fwd.to_numpy(), n_boot=300, seed=lb)
        eff.name = f"trail{lb}_vs_fwd{horizon}"
        effects.append(eff)

        decile = _safe_qcut(trail, 10, labels=[f"d{i}" for i in range(10)])
        effects.extend(_bucket_effects(fwd, decile, prefix=f"fwd{horizon}|trail{lb}", horizon=horizon))

    return apply_fdr(effects)


def seasonality(ohlcv: pd.DataFrame, *, horizon: int = 6) -> list[Effect]:
    """Hour, weekday, trading session, funding window and turn-of-month effects.

    The existing feature pack encodes only cyclical hour and weekday; no session structure
    was ever tested, which is what makes the London and New York question open.
    """
    close = ohlcv["close"]
    fwd = forward_log_return(close, horizon)
    idx = pd.DatetimeIndex(ohlcv.index)
    effects: list[Effect] = []

    hour = pd.Series(idx.hour, index=ohlcv.index).astype("category")
    effects.extend(_bucket_effects(fwd, hour, prefix=f"fwd{horizon}|hour_utc", horizon=horizon))

    dow = pd.Series(idx.dayofweek, index=ohlcv.index).astype("category")
    effects.extend(_bucket_effects(fwd, dow, prefix=f"fwd{horizon}|dayofweek", horizon=horizon))

    for name, (start, end) in SESSIONS.items():
        inside = (idx.hour >= start) & (idx.hour < end)
        flag = pd.Series(np.where(inside, name, f"not_{name}"), index=ohlcv.index).astype("category")
        effects.extend(_bucket_effects(fwd, flag, prefix=f"fwd{horizon}|session", horizon=horizon))

    # Binance settles funding at 00:00, 08:00 and 16:00 UTC; crowding unwinds around those.
    near_funding = pd.Series(
        np.where(np.isin(idx.hour, [0, 8, 16]), "funding_hour", "other"), index=ohlcv.index
    ).astype("category")
    effects.extend(_bucket_effects(fwd, near_funding, prefix=f"fwd{horizon}|funding_hour", horizon=horizon))

    tom = pd.Series(
        np.where((idx.day <= 3) | (idx.day >= 28), "turn_of_month", "mid_month"), index=ohlcv.index
    ).astype("category")
    effects.extend(_bucket_effects(fwd, tom, prefix=f"fwd{horizon}|turn_of_month", horizon=horizon))

    return apply_fdr(effects)


def volatility_clustering(ohlcv: pd.DataFrame, *, horizon: int = 24) -> list[Effect]:
    """Volatility persistence: the one regularity that is reliably present in this asset class."""
    close = ohlcv["close"]
    ret = np.log(close.replace(0, np.nan)).diff().dropna()
    arr = ret.to_numpy()
    abs_ret = np.abs(arr)
    effects: list[Effect] = []

    centred = abs_ret - abs_ret.mean()
    denom = float(np.dot(centred, centred))
    for lag in (1, 6, 24, 96, 240):
        if denom <= 0 or abs_ret.size - lag < 100:
            continue
        rho = float(np.dot(centred[lag:], centred[:-lag]) / denom)
        se = 1.0 / np.sqrt(abs_ret.size)
        effects.append(
            Effect(
                name=f"abs_ret_acf_lag_{lag}",
                statistic=rho,
                n=int(abs_ret.size - lag),
                p_value=normal_two_sided_p(rho / se),
                detail={"lag": float(lag)},
            )
        )

    try:
        from statsmodels.stats.diagnostic import het_arch

        stat, p, _, _ = het_arch(arr, nlags=12)
        effects.append(Effect(name="arch_lm_12", statistic=float(stat), n=int(arr.size), p_value=float(p)))
    except Exception:  # noqa: BLE001
        pass

    # Persistence alpha+beta near 1 means shocks to volatility decay slowly, which is what
    # makes volatility forecastable even when direction is not.
    try:
        from arch import arch_model

        scaled = arr * 100.0  # arch warns and conditions poorly on raw returns
        res = arch_model(scaled, vol="GARCH", p=1, q=1, mean="Zero").fit(disp="off", show_warning=False)
        alpha = float(res.params.get("alpha[1]", np.nan))
        beta = float(res.params.get("beta[1]", np.nan))
        effects.append(
            Effect(
                name="garch11_persistence",
                statistic=alpha + beta,
                n=int(arr.size),
                detail={"alpha": alpha, "beta": beta},
            )
        )
    except Exception:  # noqa: BLE001
        pass

    # Vol-of-vol: is the volatility level itself unstable enough to be worth forecasting?
    realized = pd.Series(abs_ret).rolling(horizon, min_periods=horizon // 2).mean()
    effects.append(
        Effect(
            name="vol_of_vol",
            statistic=float(realized.std() / realized.mean()) if realized.mean() else float("nan"),
            n=int(realized.notna().sum()),
        )
    )
    return apply_fdr(effects)


def regime_conditional(ohlcv: pd.DataFrame, *, horizon: int = 6, lookback: int = 24) -> list[Effect]:
    """Do momentum and mean reversion flip sign across volatility and trend regimes?

    A relationship that is positive in one regime and negative in another averages to zero
    over the full sample, which is one way genuine structure hides from an unconditional
    scan.
    """
    close = ohlcv["close"]
    fwd = forward_log_return(close, horizon)
    ret = np.log(close.replace(0, np.nan)).diff()

    vol = ret.rolling(lookback, min_periods=lookback // 2).std()
    vol_regime = _safe_qcut(vol, 3, labels=["vol_low", "vol_mid", "vol_high"])

    ema_fast = close.ewm(span=24, adjust=False, min_periods=24).mean()
    ema_slow = close.ewm(span=96, adjust=False, min_periods=96).mean()
    trend_regime = pd.Series(
        np.where(ema_fast > ema_slow, "trend_up", "trend_down"), index=close.index
    ).astype("category")

    effects: list[Effect] = []
    trail = np.log(close.replace(0, np.nan)).diff(lookback)

    for label, regime in (("vol", vol_regime), ("trend", trend_regime)):
        frame = pd.DataFrame({"trail": trail, "fwd": fwd, "regime": regime}).dropna()
        for key, grp in frame.groupby("regime", observed=True):
            if len(grp) < 500:
                continue
            eff = bootstrap_corr_test(
                grp["trail"].to_numpy(), grp["fwd"].to_numpy(), n_boot=200, seed=hash(str(key)) % 10_000
            )
            eff.name = f"trail{lookback}_vs_fwd{horizon}|{label}={key}"
            effects.append(eff)
        effects.extend(_bucket_effects(fwd, regime, prefix=f"fwd{horizon}|{label}_regime", horizon=horizon))

    return apply_fdr(effects)


def cycles(close: pd.Series, *, n_surrogates: int = 200, seed: int = 0, top_k: int = 5) -> list[Effect]:
    """Is there a genuine periodic component, or is the spectrum indistinguishable from noise?

    This is the honest form of the "represent market strength as a wave" question. A wave
    representation is only meaningful if some frequency carries more power than an
    autocorrelation-matched null produces by chance.

    The test is a **global maximum** statistic: the largest normalised peak in the observed
    spectrum against the distribution of largest peaks under the null. Testing each of the
    ~512 frequency bins separately cannot work — with a permutation p floored at
    1/(1+draws), no bin can ever clear a false-discovery threshold across that many tests,
    which is the same structural inability to reject that produced D-013. Individual peaks
    are reported descriptively, without p-values, so they cannot enter a multiplicity
    correction and manufacture discoveries.
    """
    from scipy.signal import lfilter, welch

    ret = np.log(close.replace(0, np.nan)).diff().dropna().to_numpy()
    if ret.size < 2048:
        return []

    nperseg = min(1024, ret.size // 8)
    freqs, power = welch(ret, nperseg=nperseg)

    # Null: AR(1) surrogates matched to the observed lag-1 autocorrelation, which is the
    # weakest null that still reproduces the series' own linear memory.
    centred = ret - ret.mean()
    rho = float(np.dot(centred[1:], centred[:-1]) / np.dot(centred, centred))
    rng = np.random.default_rng(seed)
    sigma = float(ret.std() * np.sqrt(max(1e-9, 1 - rho**2)))

    null_power = np.empty((n_surrogates, power.size))
    for i in range(n_surrogates):
        innov = rng.normal(0.0, sigma, size=ret.size)
        # AR(1) as a recursive filter rather than a Python loop over ~57k bars.
        surrogate = lfilter([1.0], [1.0, -rho], innov)
        _, null_power[i] = welch(surrogate, nperseg=nperseg)

    # Normalise each bin by its own null level so peaks are comparable across frequencies,
    # then take the maximum over bins in both arms.
    baseline = np.median(null_power, axis=0)
    baseline[baseline <= 0] = np.nan
    obs_ratio = power / baseline
    null_ratio = null_power / baseline[None, :]

    band = slice(1, power.size)  # drop the zero-frequency bin
    obs_max = float(np.nanmax(obs_ratio[band]))
    null_max = np.nanmax(null_ratio[:, band], axis=1)
    p_global = float((1.0 + np.sum(null_max >= obs_max)) / (1.0 + n_surrogates))

    peak_bin = int(np.nanargmax(obs_ratio[band])) + 1
    peak_period = float(1.0 / freqs[peak_bin]) if freqs[peak_bin] > 0 else float("inf")

    effects = [
        Effect(
            name="spectral_peak_global",
            statistic=obs_max,
            n=int(ret.size),
            p_value=p_global,
            detail={
                "peak_period_bars": peak_period,
                "null_max_median": float(np.median(null_max)),
                "ar1_rho": rho,
            },
        )
    ]

    # Descriptive only: no p-value, so apply_fdr leaves them out of the correction.
    order = np.argsort(obs_ratio[band])[::-1][:top_k]
    for rank, j in enumerate(order):
        bin_idx = int(j) + 1
        period = float(1.0 / freqs[bin_idx]) if freqs[bin_idx] > 0 else float("inf")
        effects.append(
            Effect(
                name=f"spectral_peak_rank{rank + 1}_period_{period:.1f}_bars",
                statistic=float(obs_ratio[bin_idx]),
                n=int(ret.size),
                detail={"period_bars": period, "power": float(power[bin_idx])},
            )
        )
    return apply_fdr(effects)


def nonlinear_lag(ohlcv: pd.DataFrame, *, horizon: int = 6, max_lag: int = 24) -> list[Effect]:
    """Mutual information between lagged returns and the forward return.

    Reported alongside the linear correlation so that a large information score with a near
    zero correlation is visible as genuine nonlinearity rather than being missed entirely.
    """
    from sklearn.feature_selection import mutual_info_regression

    close = ohlcv["close"]
    fwd = forward_log_return(close, horizon)
    ret = np.log(close.replace(0, np.nan)).diff()

    lags = [1, 2, 3, 6, 12, 24]
    lags = [lag for lag in lags if lag <= max_lag]
    frame = pd.DataFrame({f"lag_{lag}": ret.shift(lag) for lag in lags})
    frame["fwd"] = fwd
    frame = frame.dropna()
    if len(frame) < 1000:
        return []

    # Subsample: mutual information estimation is O(n log n) per feature with a k-nearest
    # neighbour estimator and adds nothing beyond ~30k rows.
    if len(frame) > 30_000:
        frame = frame.iloc[:: len(frame) // 30_000 + 1]

    X = frame[[f"lag_{lag}" for lag in lags]].to_numpy()
    y = frame["fwd"].to_numpy()
    mi = mutual_info_regression(X, y, random_state=0)

    effects: list[Effect] = []
    for lag, score in zip(lags, mi, strict=True):
        linear = safe_corr(frame[f"lag_{lag}"].to_numpy(), y)
        effects.append(
            Effect(
                name=f"mutual_info_lag_{lag}",
                statistic=float(score),
                n=int(len(frame)),
                detail={"linear_corr": float(linear), "lag": float(lag)},
            )
        )
    return effects


def _atr(ohlcv: pd.DataFrame, window: int) -> pd.Series:
    high, low, close = ohlcv["high"], ohlcv["low"], ohlcv["close"]
    prev = close.shift(1)
    tr = pd.concat([high - low, (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(window, min_periods=max(2, window // 2)).mean()


def _safe_qcut(series: pd.Series, q: int, labels: list[str]) -> pd.Series:
    """Quantile buckets that tolerate ties and missing data."""
    try:
        return pd.qcut(series, q, labels=labels, duplicates="drop")
    except (ValueError, IndexError):
        return pd.Series(pd.Categorical([np.nan] * len(series)), index=series.index)
