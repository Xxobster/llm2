"""Shared statistics for the diagnostics layer.

Financial return series are autocorrelated and volatility-clustered, so the textbook
standard error of a correlation is far too small and the textbook p-value is far too
optimistic. Every significance statement produced here therefore comes from either a
stationary block bootstrap or an explicit heteroskedasticity-and-autocorrelation-consistent
adjustment, and every family of tests is corrected for multiplicity.

Scanning roughly 40 external series across 20 lags and 4 horizons is 3,200 tests. At a
nominal five percent level that yields about 160 "discoveries" from pure noise, which is
why `benjamini_hochberg` is applied to every scan rather than offered as an option.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class Effect:
    """One measured relationship, with the uncertainty needed to judge it."""

    name: str
    statistic: float
    n: int
    p_value: float = float("nan")
    ci_low: float = float("nan")
    ci_high: float = float("nan")
    q_value: float = float("nan")  # Benjamini-Hochberg adjusted
    detail: dict[str, float] = field(default_factory=dict)

    @property
    def significant(self) -> bool:
        return bool(np.isfinite(self.q_value) and self.q_value <= 0.05)


def effects_to_frame(effects: list[Effect]) -> pd.DataFrame:
    if not effects:
        return pd.DataFrame(
            columns=["name", "statistic", "n", "p_value", "q_value", "ci_low", "ci_high", "significant"]
        )
    rows = [
        {
            "name": e.name,
            "statistic": e.statistic,
            "n": e.n,
            "p_value": e.p_value,
            "q_value": e.q_value,
            "ci_low": e.ci_low,
            "ci_high": e.ci_high,
            "significant": e.significant,
            **e.detail,
        }
        for e in effects
    ]
    return pd.DataFrame(rows)


def benjamini_hochberg(p_values: np.ndarray) -> np.ndarray:
    """False-discovery-rate adjusted q-values, order preserved.

    Controls the expected share of false positives among rejections, which is the right
    error rate for a screen whose output is a shortlist of hypotheses rather than a single
    accept/reject decision.
    """
    p = np.asarray(p_values, dtype=float)
    out = np.full(p.shape, np.nan)
    finite = np.isfinite(p)
    if not finite.any():
        return out

    vals = p[finite]
    n = vals.size
    order = np.argsort(vals)
    ranked = vals[order]
    # Step-up: q_(i) = min over j>=i of (n/j) * p_(j), enforced by a reverse cumulative min.
    scaled = ranked * n / np.arange(1, n + 1)
    q_sorted = np.minimum.accumulate(scaled[::-1])[::-1]
    q = np.empty(n)
    q[order] = np.clip(q_sorted, 0.0, 1.0)
    out[finite] = q
    return out


def apply_fdr(effects: list[Effect]) -> list[Effect]:
    """Attach q-values across a family of tests. Call once per scan, not per test."""
    q = benjamini_hochberg(np.array([e.p_value for e in effects], dtype=float))
    for effect, qv in zip(effects, q, strict=True):
        effect.q_value = float(qv)
    return effects


def _paired_finite(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    mask = np.isfinite(x) & np.isfinite(y)
    return x[mask], y[mask]


def safe_corr(x: np.ndarray, y: np.ndarray, *, method: str = "pearson") -> float:
    """Correlation on the finite intersection, NaN when undefined rather than 0."""
    xv, yv = _paired_finite(x, y)
    if xv.size < 30:
        return float("nan")
    if method == "spearman":
        xv = _rankdata(xv)
        yv = _rankdata(yv)
    sx, sy = xv.std(), yv.std()
    if sx <= 1e-18 or sy <= 1e-18:
        return float("nan")
    return float(np.mean((xv - xv.mean()) * (yv - yv.mean())) / (sx * sy))


def _rankdata(a: np.ndarray) -> np.ndarray:
    """Average-rank transform, vectorized (equivalent to scipy.stats.rankdata)."""
    order = np.argsort(a, kind="mergesort")
    ranks = np.empty(a.size, dtype=float)
    ranks[order] = np.arange(1, a.size + 1, dtype=float)
    # Average ties so that a heavily tied series does not fabricate structure.
    sorted_a = a[order]
    ties_start = 0
    for i in range(1, a.size + 1):
        if i == a.size or sorted_a[i] != sorted_a[ties_start]:
            if i - ties_start > 1:
                ranks[order[ties_start:i]] = np.mean(np.arange(ties_start + 1, i + 1, dtype=float))
            ties_start = i
    return ranks


def optimal_block_length(x: np.ndarray) -> int:
    """Politis-White style block length from the first-order autocorrelation.

    A block bootstrap only preserves dependence if the block outlives it. Hourly crypto
    returns have weak but non-zero persistence and strong volatility clustering, so blocks
    an order of magnitude longer than the return autocorrelation are appropriate.
    """
    xv = x[np.isfinite(x)]
    n = xv.size
    if n < 50:
        return max(2, n // 10)
    centred = xv - xv.mean()
    denom = float(np.sum(centred**2))
    if denom <= 1e-18:
        return max(2, int(n ** (1 / 3)))
    rho = float(np.sum(centred[1:] * centred[:-1]) / denom)
    rho = float(np.clip(abs(rho), 1e-3, 0.95))
    block = int(np.ceil((2.0 * rho / (1.0 - rho**2)) ** (2 / 3) * n ** (1 / 3)))
    return int(np.clip(block, 2, max(2, n // 10)))


def stationary_bootstrap_indices(
    n: int, block_len: int, rng: np.random.Generator, *, n_boot: int
) -> np.ndarray:
    """Index matrix (n_boot, n) for a stationary bootstrap with geometric block lengths.

    Fully vectorized: a new block starts wherever a Bernoulli(1/block_len) draw fires,
    otherwise the index advances by one, wrapping circularly.
    """
    p = 1.0 / max(1, block_len)
    starts = rng.integers(0, n, size=(n_boot, n))
    new_block = rng.random((n_boot, n)) < p
    new_block[:, 0] = True

    # Position within the current block: reset to 0 at each new block, else increment.
    steps = np.arange(n)
    # Index of the most recent block start for every column.
    anchor_pos = np.maximum.accumulate(np.where(new_block, steps, -1), axis=1)
    offset = steps[None, :] - anchor_pos
    anchor_val = np.take_along_axis(starts, np.clip(anchor_pos, 0, n - 1), axis=1)
    return (anchor_val + offset) % n


def bootstrap_statistic(
    values: np.ndarray,
    statistic,
    *,
    n_boot: int = 1000,
    seed: int = 0,
    block_len: int | None = None,
) -> tuple[float, float, float]:
    """Percentile confidence interval for a statistic of a dependent series.

    ``values`` may be 1-D or (n, k); resampling is applied along the first axis so paired
    series keep their alignment.
    """
    arr = np.asarray(values, dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    n = arr.shape[0]
    if n < 50:
        return float("nan"), float("nan"), float("nan")

    rng = np.random.default_rng(seed)
    bl = block_len or optimal_block_length(arr[:, 0])
    idx = stationary_bootstrap_indices(n, bl, rng, n_boot=n_boot)

    draws = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        draws[b] = statistic(arr[idx[b]])

    finite = draws[np.isfinite(draws)]
    if finite.size < 10:
        return float("nan"), float("nan"), float("nan")
    return float(np.mean(finite)), float(np.quantile(finite, 0.025)), float(np.quantile(finite, 0.975))


def bootstrap_corr_test(
    x: np.ndarray,
    y: np.ndarray,
    *,
    n_boot: int = 1000,
    seed: int = 0,
    method: str = "pearson",
) -> Effect:
    """Correlation with a dependence-aware interval and a circular-shift null p-value.

    The null shifts one series circularly, which destroys the cross-series alignment while
    preserving each series' own autocorrelation and volatility clustering. A plain
    permutation would destroy both and understate the null spread badly.
    """
    xv, yv = _paired_finite(x, y)
    n = xv.size
    if n < 100:
        return Effect(name="corr", statistic=float("nan"), n=int(n))

    stat = safe_corr(xv, yv, method=method)
    paired = np.column_stack([xv, yv])
    _, lo, hi = bootstrap_statistic(
        paired,
        lambda a: safe_corr(a[:, 0], a[:, 1], method=method),
        n_boot=n_boot,
        seed=seed,
    )

    rng = np.random.default_rng(seed + 1)
    shifts = rng.integers(n // 20, n - n // 20, size=n_boot)
    null = np.empty(n_boot, dtype=float)
    for i, s in enumerate(shifts):
        null[i] = safe_corr(xv, np.roll(yv, int(s)), method=method)
    null = null[np.isfinite(null)]

    if null.size < 10 or not np.isfinite(stat):
        p = float("nan")
    else:
        p = float((1.0 + np.sum(np.abs(null) >= abs(stat))) / (1.0 + null.size))

    return Effect(
        name="corr",
        statistic=float(stat),
        n=int(n),
        p_value=p,
        ci_low=lo,
        ci_high=hi,
        detail={"null_sd": float(np.std(null)) if null.size else float("nan")},
    )


UNIT_ROOT_ACF1 = 0.995
ADF_SAMPLE = 5000


def looks_integrated(x: np.ndarray, *, alpha: float = 0.01) -> bool:
    """True when a series carries a unit root, i.e. it is a level rather than a return.

    High autocorrelation alone is not integration, and the distinction matters: a 96-bar
    overlapping return has a lag-1 autocorrelation around 0.99 yet is a moving average of
    stationary increments and is perfectly valid input. A cheap autocorrelation screen
    admits the obvious cases, and anything borderline goes to an augmented Dickey-Fuller
    test on a contiguous slice (contiguous, not strided, because striding would destroy the
    very dynamics being tested).
    """
    xv = np.asarray(x, dtype=float)
    xv = xv[np.isfinite(xv)]
    if xv.size < 200:
        return False
    centred = xv - xv.mean()
    denom = float(np.dot(centred, centred))
    if denom <= 0:
        return False
    if float(np.dot(centred[1:], centred[:-1]) / denom) <= UNIT_ROOT_ACF1:
        return False

    try:
        from statsmodels.tsa.stattools import adfuller

        sample = xv[-ADF_SAMPLE:] if xv.size > ADF_SAMPLE else xv
        p_value = float(adfuller(sample, maxlag=10, autolag=None, regression="c")[1])
    except Exception:  # noqa: BLE001 - fall back to the screen if the test cannot run
        return True
    # Failing to reject the unit root means we must treat it as integrated.
    return p_value > alpha


def circular_shift_max_lag_null(
    x: np.ndarray,
    y: np.ndarray,
    *,
    max_lag: int,
    n_null: int = 400,
    seed: int = 0,
    guard_frac: float = 0.05,
    require_stationary: bool = True,
) -> Effect:
    """Max-|correlation| over lags 1..max_lag, against a max-statistic circular-shift null.

    Selecting the winning lag by maximising absolute correlation and then testing that
    winner against a single-lag null makes every p-value optimistic by roughly the
    selection factor. The null here takes, for each circular shift of ``y``, the same
    maximum over the same lag range, so the search is paid for. Same pattern as
    ``dominant_period`` taking the global maximum across frequency bins.
    """
    xv, yv = _paired_finite(x, y)
    n = xv.size
    if n < 500 or max_lag < 1:
        return Effect(name="max_lag_lead", statistic=float("nan"), n=int(n))

    if require_stationary:
        offenders = [nm for nm, arr in (("x", xv), ("y", yv)) if looks_integrated(arr)]
        if offenders:
            raise ValueError(
                f"circular_shift_max_lag_null received near-unit-root input "
                f"({', '.join(offenders)}). Difference to returns first."
            )

    def _best_linear_lag(a: np.ndarray, b: np.ndarray) -> tuple[float, int]:
        """Max |corr(a[L:], b[:-L])| over L=1..max_lag — same definition as the lead scan."""
        best_corr, best_lag = 0.0, 0
        for lag in range(1, max_lag + 1):
            aa = a[lag:] - a[lag:].mean()
            bb = b[:-lag] - b[:-lag].mean()
            sa = float(np.sqrt(np.dot(aa, aa)))
            sb = float(np.sqrt(np.dot(bb, bb)))
            if sa <= 1e-18 or sb <= 1e-18:
                continue
            corr = float(np.dot(aa, bb) / (sa * sb))
            if abs(corr) > abs(best_corr):
                best_corr, best_lag = corr, lag
        return best_corr, best_lag

    # Observed statistic: linear slices (matches phase_lead_scan / panel).
    obs_corr, obs_lag = _best_linear_lag(xv, yv)
    corr0 = safe_corr(xv, yv)

    # Null: circular shifts of y, max |corr| over the same lag set. For lag << n the
    # circular cross-correlation at lag L equals the linear one up to O(L/n), so one FFT
    # plus index rotation gives the full null without  n_null × max_lag slice loops.
    xs = (xv - xv.mean()) / (xv.std() or np.nan)
    ys = (yv - yv.mean()) / (yv.std() or np.nan)
    if not np.isfinite(xs).all() or not np.isfinite(ys).all():
        return Effect(name="max_lag_lead", statistic=float(obs_corr), n=int(n))
    cross = np.fft.irfft(np.fft.rfft(xs) * np.conj(np.fft.rfft(ys)), n=n) / n
    # corr(x[L:], y[:-L]) ≈ cross[n-L] under circular convention (y leads x by L).
    lag_idx = (n - np.arange(1, max_lag + 1)) % n

    rng = np.random.default_rng(seed)
    lo = max(1, int(n * guard_frac))
    hi = max(lo + 1, n - lo)
    shifts = rng.integers(lo, hi, size=n_null)
    # roll(y, s) rotates the cross-correlation: new_cross[k] = cross[(k - s) mod n].
    null_max = np.max(np.abs(cross[(lag_idx[None, :] - shifts[:, None]) % n]), axis=1)

    finite = null_max[np.isfinite(null_max)]
    if finite.size < 20 or not np.isfinite(obs_corr):
        p = float("nan")
    else:
        p = float((1.0 + np.sum(finite >= abs(obs_corr))) / (1.0 + finite.size))

    return Effect(
        name="max_lag_lead",
        statistic=float(obs_corr),
        n=int(n),
        p_value=p,
        detail={
            "lag_bars": float(obs_lag),
            "corr_lag0": float(corr0) if np.isfinite(corr0) else float("nan"),
            "leads_beyond_contemporaneous": float(
                abs(obs_corr) > abs(corr0) if np.isfinite(corr0) else False
            ),
            "null_mean_max": float(np.mean(finite)) if finite.size else float("nan"),
            "max_lag_searched": float(max_lag),
        },
    )


def circular_shift_null_corr(
    x: np.ndarray,
    y: np.ndarray,
    *,
    guard_frac: float = 0.05,
    require_stationary: bool = True,
) -> Effect:
    """Correlation of ``x`` and ``y`` against the null of every circular shift of ``y``.

    Every one of the ``n`` circular shifts is evaluated exactly, in one pass, via the
    Fourier transform: the circular cross-correlation of two standardised series is the
    inverse transform of the product of their spectra. That makes a full null distribution
    cost one fast Fourier transform instead of thousands of resampled correlations, which is
    what makes a several-hundred-pair scan tractable.

    Circular shifting preserves each series' own autocorrelation and volatility clustering
    while destroying the alignment between them, so the null answers the right question:
    "how large a correlation do two series this persistent produce when unrelated?"

    Shifts within ``guard_frac`` of zero are excluded, because a shift shorter than the
    series' own memory is not really an independent draw.

    The null assumes approximate stationarity. On integrated series (price *levels* rather
    than returns) the wrap-around discontinuity makes it anti-conservative: measured
    rejection on independent random walks is about 17 percent rather than 5. Correlating
    levels is a methodological error in its own right, so integrated input is rejected
    rather than silently mis-tested.
    """
    xv, yv = _paired_finite(x, y)
    n = xv.size
    if n < 500:
        return Effect(name="lead_lag", statistic=float("nan"), n=int(n))

    if require_stationary:
        offenders = [nm for nm, arr in (("x", xv), ("y", yv)) if looks_integrated(arr)]
        if offenders:
            raise ValueError(
                f"circular_shift_null_corr received near-unit-root input ({', '.join(offenders)}). "
                "Difference to returns first: the circular null is anti-conservative on levels "
                "and correlating price levels is a spurious-regression error regardless."
            )

    xs = (xv - xv.mean()) / (xv.std() or np.nan)
    ys = (yv - yv.mean()) / (yv.std() or np.nan)
    if not np.isfinite(xs).all() or not np.isfinite(ys).all():
        return Effect(name="lead_lag", statistic=float("nan"), n=int(n))

    spectrum = np.fft.rfft(xs) * np.conj(np.fft.rfft(ys))
    cross = np.fft.irfft(spectrum, n=n) / n  # cross[s] = corr(x, roll(y, -s))

    observed = float(cross[0])
    guard = max(1, int(n * guard_frac))
    null = np.concatenate([cross[guard : n - guard]])
    if null.size < 50:
        return Effect(name="lead_lag", statistic=observed, n=int(n))

    p = float((1.0 + np.sum(np.abs(null) >= abs(observed))) / (1.0 + null.size))
    sd = float(np.std(null))
    return Effect(
        name="lead_lag",
        statistic=observed,
        n=int(n),
        p_value=p,
        ci_low=observed - 1.96 * sd,
        ci_high=observed + 1.96 * sd,
        detail={"null_sd": sd, "z_vs_null": float(observed / sd) if sd > 0 else float("nan")},
    )


def newey_west_tstat(x: np.ndarray, lags: int | None = None) -> tuple[float, float]:
    """Mean and heteroskedasticity/autocorrelation-consistent t-statistic of a series.

    Used for "is this conditional mean different from zero" questions, where overlapping
    forward returns make the naive t-statistic roughly sqrt(horizon) too large.
    """
    xv = np.asarray(x, dtype=float)
    xv = xv[np.isfinite(xv)]
    n = xv.size
    if n < 30:
        return float("nan"), float("nan")

    mean = float(xv.mean())
    e = xv - mean
    L = lags if lags is not None else int(np.floor(4 * (n / 100.0) ** (2 / 9)))
    L = int(np.clip(L, 0, max(0, n - 2)))

    gamma0 = float(np.dot(e, e) / n)
    var = gamma0
    for lag in range(1, L + 1):
        cov = float(np.dot(e[lag:], e[:-lag]) / n)
        var += 2.0 * (1.0 - lag / (L + 1.0)) * cov
    if var <= 0:
        return mean, float("nan")
    se = float(np.sqrt(var / n))
    return mean, (mean / se if se > 0 else float("nan"))


def normal_two_sided_p(t_stat: float) -> float:
    """Two-sided p-value from a t-statistic using the normal approximation."""
    if not np.isfinite(t_stat):
        return float("nan")
    from scipy.stats import norm

    return float(2.0 * norm.sf(abs(t_stat)))
