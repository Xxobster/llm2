"""Market strength as a wave: amplitude, phase and cross-asset phase lead.

The diagnostics pass found a 15.3-bar spectral peak on BTCUSDT 1h that beats an AR(1)
null at q = 0.005, but only at 1.7 times the null level. This module turns that number
into something you can look at and compare across assets, and — more importantly — draws a
hard line through the middle of the idea.

**The two-wave problem.** The textbook way to extract a cycle is to band-pass filter the
series and take the Hilbert transform of the result. Both operations are *non-causal*. A
zero-phase filter runs forwards and backwards, and the analytic signal at bar ``t`` is
built from a transform over the entire series including everything after ``t``. The
resulting wave is beautiful, it turns at the exact top of every swing, and it is completely
untradeable. Plotting one of those over a candle chart and reading the turns as signals is
one of the most effective ways to fool yourself that exists in technical analysis.

So two waves are produced and they are never mixed:

``analytic_wave``
    Zero-phase, whole-series, non-causal. For **display and description only**. Every
    function that returns it marks it ``causal=False`` and the chart labels it in the
    legend. It answers "was there a rhythm in this history", which is a real question.

``causal_wave``
    One-sided. The band-pass is a forward-only biquad and the phase comes from a
    quadrature pair built only from past samples. It lags — that is not a defect to be
    tuned away, it is the price of not seeing the future — and it is the only version that
    may ever become a feature or a signal.

The gap between them is reported as ``phase_lag_bars`` and ``corr_causal_vs_analytic``. On
a genuine strong cycle the two agree closely; on a weak one the causal version is mostly
noise, which is the honest reading of a 1.7x peak.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt, hilbert, lfilter, welch

from llm2.diagnostics.stats import Effect, apply_fdr, circular_shift_max_lag_null

# Band around the dominant period, as a multiplicative half-width. A cycle detected at 15
# bars is never exactly 15 bars, so the band has to be wide enough to hold a drifting
# period and narrow enough not to simply pass the whole series through.
BAND_HALF_WIDTH = 0.5
MIN_SAMPLES = 2048


@dataclass
class WaveFit:
    """Dominant cycle of one series, in both the honest and the flattering form."""

    symbol: str
    timeframe: str
    period_bars: float
    peak_ratio: float
    p_value: float
    n: int
    index: pd.DatetimeIndex = field(repr=False, default_factory=lambda: pd.DatetimeIndex([]))
    analytic_wave: pd.Series = field(repr=False, default_factory=lambda: pd.Series(dtype=float))
    analytic_amplitude: pd.Series = field(repr=False, default_factory=lambda: pd.Series(dtype=float))
    analytic_phase: pd.Series = field(repr=False, default_factory=lambda: pd.Series(dtype=float))
    causal_wave: pd.Series = field(repr=False, default_factory=lambda: pd.Series(dtype=float))
    causal_amplitude: pd.Series = field(repr=False, default_factory=lambda: pd.Series(dtype=float))
    causal_phase: pd.Series = field(repr=False, default_factory=lambda: pd.Series(dtype=float))
    phase_lag_bars: float = float("nan")
    corr_causal_vs_analytic: float = float("nan")

    @property
    def is_meaningful(self) -> bool:
        """A peak this shallow is a rhythm you can describe, not one you can trade."""
        return self.peak_ratio >= 2.0 and self.p_value <= 0.05

    def summary(self) -> str:
        verdict = "tradeable-strength" if self.is_meaningful else "descriptive only"
        return (
            f"{self.symbol} {self.timeframe}: period {self.period_bars:.1f} bars, "
            f"peak {self.peak_ratio:.2f}x null, p={self.p_value:.4f}, "
            f"causal-vs-analytic corr {self.corr_causal_vs_analytic:.2f}, "
            f"lag {self.phase_lag_bars:.1f} bars [{verdict}]"
        )


def dominant_period(
    returns: np.ndarray, *, n_surrogates: int = 200, seed: int = 0
) -> tuple[float, float, float]:
    """Dominant spectral period, its height above an AR(1) null, and a global p-value.

    Identical machinery to :func:`llm2.diagnostics.structure.cycles`, kept here so a wave
    can be fitted standalone. The null is AR(1) rather than white noise because financial
    returns are mildly autocorrelated and a white-noise null would call that autocorrelation
    a cycle. The p-value uses the *global maximum* across all frequency bins, so it answers
    "is any peak real" as a single hypothesis instead of testing hundreds of bins and
    drowning in the multiplicity correction.
    """
    ret = np.asarray(returns, dtype=float)
    ret = ret[np.isfinite(ret)]
    if ret.size < MIN_SAMPLES:
        return float("nan"), float("nan"), float("nan")

    nperseg = min(1024, ret.size // 8)
    freqs, power = welch(ret, nperseg=nperseg)

    centred = ret - ret.mean()
    rho = float(np.dot(centred[1:], centred[:-1]) / np.dot(centred, centred))
    sigma = float(ret.std() * np.sqrt(max(1e-9, 1 - rho**2)))

    rng = np.random.default_rng(seed)
    null_power = np.empty((n_surrogates, power.size))
    for i in range(n_surrogates):
        innov = rng.normal(0.0, sigma, size=ret.size)
        null_power[i] = welch(lfilter([1.0], [1.0, -rho], innov), nperseg=nperseg)[1]

    baseline = np.median(null_power, axis=0)
    baseline[baseline <= 0] = np.nan
    obs_ratio = power / baseline
    null_ratio = null_power / baseline[None, :]

    band = slice(1, power.size)
    obs_max = float(np.nanmax(obs_ratio[band]))
    null_max = np.nanmax(null_ratio[:, band], axis=1)
    p_global = float((1.0 + np.sum(null_max >= obs_max)) / (1.0 + n_surrogates))

    peak_bin = int(np.nanargmax(obs_ratio[band])) + 1
    period = float(1.0 / freqs[peak_bin]) if freqs[peak_bin] > 0 else float("inf")
    return period, obs_max, p_global


def _bandpass_coeffs(period: float, *, half_width: float = BAND_HALF_WIDTH, order: int = 2):
    """Butterworth band edges around a period, in normalised frequency."""
    f0 = 1.0 / period
    lo = max(1e-4, f0 * (1.0 - half_width))
    hi = min(0.49, f0 * (1.0 + half_width))
    if hi <= lo:
        lo, hi = max(1e-4, f0 * 0.5), min(0.49, f0 * 1.5)
    return butter(order, [lo * 2, hi * 2], btype="band")


class NonCausalWaveError(RuntimeError):
    """Raised when display-only ``analytic_wave`` is reached from a mining module."""


_MINING_MODULE_MARKERS = (
    "llm2.diagnostics.wavemetrics",
    "llm2.diagnostics.wavemotif",
    "llm2.diagnostics.waveevent",
    "llm2.diagnostics.wavepanel",
    "llm2.diagnostics.structurebreak",
)


def _refuse_analytic_from_mining() -> None:
    """Hard block: mining code must never see the non-causal wave."""
    import inspect

    for frame in inspect.stack()[2:]:
        mod = frame.frame.f_globals.get("__name__", "")
        if any(mod == m or mod.startswith(m + ".") for m in _MINING_MODULE_MARKERS):
            raise NonCausalWaveError(
                f"{mod} must not call analytic_wave; use causal_wave only. "
                "The non-causal wave is display-only (filtfilt + Hilbert over the full series)."
            )


def fit_period_in_window(
    returns: np.ndarray, *, n_surrogates: int = 200, seed: int = 0
) -> tuple[float, float, float]:
    """Fit the dominant period on a training window only.

    Applying a full-history period to early bars is look-ahead as soon as the period feeds
    a tradeable claim. Call this inside each training fold and apply the returned period
    unchanged out of sample.
    """
    return dominant_period(returns, n_surrogates=n_surrogates, seed=seed)


def analytic_wave(series: pd.Series, period: float) -> tuple[pd.Series, pd.Series, pd.Series]:
    """Zero-phase band-pass plus Hilbert transform. **Non-causal — display only.**

    ``filtfilt`` runs the filter forwards then backwards to cancel phase distortion, which
    means every output sample depends on the whole series. The Hilbert transform is a
    global operation for the same reason. This is the wave that looks uncanny on a chart.
    """
    _refuse_analytic_from_mining()
    x = pd.to_numeric(series, errors="coerce").astype(float)
    filled = x.interpolate(limit_direction="both").to_numpy()
    b, a = _bandpass_coeffs(period)
    wave = filtfilt(b, a, filled)
    z = hilbert(wave)
    idx = series.index
    return (
        pd.Series(wave, index=idx),
        pd.Series(np.abs(z), index=idx),
        pd.Series(np.angle(z), index=idx),
    )


def causal_wave(series: pd.Series, period: float) -> tuple[pd.Series, pd.Series, pd.Series]:
    """Forward-only band-pass with a quadrature pair. Lags, and is therefore usable.

    Phase and amplitude come from pairing the filtered signal with a quarter-cycle-delayed
    copy of itself. A delay is the crudest possible Hilbert approximation, and that is
    deliberate: it uses only past samples, so the value at bar ``t`` would have been
    available at bar ``t``. Anything cleverer here tends to smuggle in future data.
    """
    x = pd.to_numeric(series, errors="coerce").astype(float)
    filled = x.interpolate(limit_direction="both").to_numpy()
    b, a = _bandpass_coeffs(period)
    wave = lfilter(b, a, filled)

    quarter = max(1, int(round(period / 4.0)))
    inphase = wave
    quadrature = np.concatenate([np.full(quarter, np.nan), wave[:-quarter]])

    amplitude = np.sqrt(inphase**2 + quadrature**2)
    phase = np.arctan2(quadrature, inphase)

    idx = series.index
    # The filter needs a few periods to settle; before that the output is transient, not
    # signal. Blanking it stops a startup artefact being read as an early cycle.
    warmup = int(round(period * 3))
    out_w = pd.Series(wave, index=idx)
    out_a = pd.Series(amplitude, index=idx)
    out_p = pd.Series(phase, index=idx)
    out_w.iloc[:warmup] = np.nan
    out_a.iloc[:warmup] = np.nan
    out_p.iloc[:warmup] = np.nan
    return out_w, out_a, out_p


def fit_wave(
    close: pd.Series,
    *,
    symbol: str = "",
    timeframe: str = "",
    period: float | None = None,
    n_surrogates: int = 200,
    seed: int = 0,
) -> WaveFit:
    """Full wave decomposition of one series, causal and non-causal side by side."""
    c = pd.to_numeric(close, errors="coerce")
    log_c = np.log(c.where(c > 0))
    ret = log_c.diff().dropna()

    if period is None:
        period, ratio, p_val = dominant_period(
            ret.to_numpy(), n_surrogates=n_surrogates, seed=seed
        )
    else:
        _, ratio, p_val = dominant_period(ret.to_numpy(), n_surrogates=n_surrogates, seed=seed)

    fit = WaveFit(
        symbol=symbol,
        timeframe=timeframe,
        period_bars=float(period),
        peak_ratio=float(ratio),
        p_value=float(p_val),
        n=int(ret.size),
        index=pd.DatetimeIndex(c.index),
    )
    if not np.isfinite(period) or period <= 2:
        return fit

    # The wave is fitted on log price, not on returns: a cycle in price is what a chart
    # shows and what a trader means. Detrending is handled by the band-pass, which rejects
    # the zero-frequency component along with everything else outside the band.
    detrended = log_c.interpolate(limit_direction="both")
    fit.analytic_wave, fit.analytic_amplitude, fit.analytic_phase = analytic_wave(detrended, period)
    fit.causal_wave, fit.causal_amplitude, fit.causal_phase = causal_wave(detrended, period)

    both = pd.DataFrame({"a": fit.analytic_wave, "c": fit.causal_wave}).dropna()
    if len(both) > 100:
        fit.corr_causal_vs_analytic = float(both["a"].corr(both["c"]))
        fit.phase_lag_bars = _lag_of_max_correlation(
            both["a"].to_numpy(), both["c"].to_numpy(), max_lag=int(round(period))
        )
    return fit


def _lag_of_max_correlation(a: np.ndarray, b: np.ndarray, *, max_lag: int) -> float:
    """How far ``b`` must be pulled forward to line up with ``a``."""
    a = (a - a.mean()) / (a.std() or 1.0)
    b = (b - b.mean()) / (b.std() or 1.0)
    best_lag, best = 0, -np.inf
    for lag in range(0, max_lag + 1):
        if lag == 0:
            corr = float(np.mean(a * b))
        else:
            corr = float(np.mean(a[lag:] * b[:-lag]))
        if corr > best:
            best, best_lag = corr, lag
    return float(best_lag)


# --------------------------------------------------------------------------------------
# Cross-asset comparison
# --------------------------------------------------------------------------------------


def phase_lead_scan(
    fits: dict[str, WaveFit],
    reference: str,
    *,
    max_lag_bars: int = 48,
    use_causal: bool = True,
    common_period: float | None = None,
    closes: dict[str, pd.Series] | None = None,
) -> list[Effect]:
    """Does any asset's wave lead the reference asset's wave?

    **Both waves must come from the same filter.** This is not a refinement, it is the
    difference between a result and an artefact. A forward-only band-pass has a group delay
    set by its centre frequency: the filter for a 7-bar cycle delays its input by 3 bars and
    the one for a 15-bar cycle by 7. Comparing an asset fitted at 7 bars against one fitted
    at 15 therefore shows a 4-bar "lead" that is entirely the 4-bar difference in delay.

    Measured directly, that is exactly what happened here. Correlating BTCUSDT filtered at
    15.3 bars against **the same BTCUSDT series** filtered at 7.1 reported a lead of 4 bars
    at correlation 0.57 — and a series cannot lead itself. The first version of this scan
    reported "ETHUSDT leads BTCUSDT by 4 bars, r = 0.48" and 24 of 24 pairs surviving
    false-discovery control, all of it manufactured by the filter. On raw returns the same
    pair shows a 1-to-12-bar lead correlation between -0.013 and +0.008, against a
    contemporaneous correlation of +0.84: the two move together, and none of it is ahead.

    So ``common_period`` is applied to every series, defaulting to the reference asset's
    period, and ``closes`` supplies the price series to refilter. Passing pre-fitted waves
    without ``closes`` falls back to the per-asset fits and is flagged as untrustworthy.

    ``use_causal`` defaults to True and should stay that way for anything you intend to act
    on. A lead between two non-causal waves is close to meaningless: both were built with
    knowledge of the future.

    **Null:** p-values use :func:`circular_shift_max_lag_null` so the lag search is paid
    for. Any lead p-value computed under the old single-lag-after-selection null is
    ``INVALIDATED`` and must be recomputed before quoting.
    """
    if reference not in fits:
        return []
    ref_fit = fits[reference]
    period = float(common_period if common_period is not None else ref_fit.period_bars)

    def wave_for(sym: str, fit: WaveFit) -> tuple[pd.Series, bool]:
        """Refilter at the common period where the price series is available."""
        if closes is not None and sym in closes:
            c = pd.to_numeric(closes[sym], errors="coerce")
            log_c = np.log(c.where(c > 0)).interpolate(limit_direction="both")
            fn = causal_wave if use_causal else analytic_wave
            return fn(log_c, period)[0].dropna(), True
        return (fit.causal_wave if use_causal else fit.analytic_wave).dropna(), False

    ref, ref_common = wave_for(reference, ref_fit)
    if ref.empty:
        return []

    effects: list[Effect] = []
    for sym, fit in fits.items():
        if sym == reference:
            continue
        other, oth_common = wave_for(sym, fit)
        if other.empty:
            continue
        matched = bool(ref_common and oth_common)
        joined = pd.DataFrame({"ref": ref, "oth": other}).dropna()
        if len(joined) < 1000:
            continue

        r = joined["ref"].to_numpy()
        o = joined["oth"].to_numpy()

        # Lag 0 is included in the search even though it cannot be traded. If the strongest
        # alignment is contemporaneous, then there is no lead, and reporting the best
        # *positive* lag while hiding a larger lag-0 value would dress a co-movement up as
        # a forecast. That comparison is carried on the effect as ``corr_lag0``.
        # Max-statistic null: the lag search is paid for. A single-lag null after
        # selecting the winner made every earlier lead p-value optimistic (INVALIDATED).
        try:
            eff = circular_shift_max_lag_null(
                r, o, max_lag=max_lag_bars, n_null=400, seed=hash(sym) % (2**31)
            )
            p_val = eff.p_value
            best_corr = float(eff.statistic)
            best_lag = int(eff.detail.get("lag_bars", 0))
            corr_lag0 = float(eff.detail.get("corr_lag0", float("nan")))
            leads_genuinely = bool(eff.detail.get("leads_beyond_contemporaneous", 0.0))
        except ValueError as exc:
            effects.append(
                Effect(
                    name=f"wave_lead|{sym}->{reference}",
                    statistic=float("nan"),
                    n=int(len(joined)),
                    detail={"untested_reason": str(exc), "filters_matched": float(matched)},
                )
            )
            continue

        effects.append(
            Effect(
                name=f"wave_lead|{sym}->{reference}",
                statistic=float(best_corr),
                n=int(len(joined)),
                p_value=p_val,
                detail={
                    "lag_bars": float(best_lag),
                    "corr_lag0": corr_lag0,
                    "leads_beyond_contemporaneous": float(leads_genuinely),
                    "common_period_bars": period,
                    "filters_matched": float(matched),
                    "peak_ratio_other": fit.peak_ratio,
                    "causal": float(use_causal),
                    "null": "max_over_lags",
                    "prior_single_lag_null": "INVALIDATED",
                },
            )
        )
    return apply_fdr(effects)


def period_table(fits: dict[str, WaveFit]) -> pd.DataFrame:
    """One row per asset: period, peak height, significance, causal fidelity."""
    rows = [
        {
            "symbol": f.symbol or sym,
            "timeframe": f.timeframe,
            "period_bars": f.period_bars,
            "peak_ratio": f.peak_ratio,
            "p_value": f.p_value,
            "n": f.n,
            "causal_corr": f.corr_causal_vs_analytic,
            "causal_lag_bars": f.phase_lag_bars,
            "meaningful": f.is_meaningful,
        }
        for sym, f in fits.items()
    ]
    df = pd.DataFrame(rows)
    return df.sort_values("peak_ratio", ascending=False).reset_index(drop=True) if len(df) else df
