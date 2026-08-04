"""Amplitude-event study: does a surge or collapse in wave amplitude forecast anything?

Four kinds of amplitude-derived event, each a trailing-percentile-rank crossing so the
threshold means the same thing in a quiet regime and a violent one:

- ``amp_surge_{85,95}`` — amplitude crosses up through its own trailing 85th/95th percentile.
- ``amp_collapse_{15,5}`` — amplitude crosses down through its trailing 15th/5th percentile.
- ``amp_slope_burst`` — the amplitude's own slope crosses up through its trailing 90th
  percentile: not "amplitude is high" but "amplitude is rising unusually fast".

Every event is signed by the sign of the wave's own change over the preceding half-period —
the leg that was running into the event — and every target is scored twice, never once:
**direction** (the signed forward return, does the event predict which way price goes) and
**magnitude** (the absolute forward return, does the event predict how much price moves,
regardless of sign). These answer different questions and a strategy needs both kept apart:
an event that reliably precedes a big move with no directional bias is a volatility
forecast, not a trade.

**The benchmark problem.** A band-pass filter has a group delay: its output at bar ``t``
depends on a window of input ending some bars before ``t`` (see
``llm2.diagnostics.wave.causal_wave`` and ``tests/test_wave.py`` for the mechanism that makes
this a real hazard, not a theoretical one). An amplitude event is therefore never a response
to "what just happened" in the strict sense — it is a response to what happened up to
``group_delay`` bars ago. If a plain trailing-move control measured over the *same* lag would
show the same forward relationship, the wave has added nothing: it has just picked out big
trailing moves through a more complicated route. ``trailing_move_control_events`` measures
that control at the filter's own delay plus a small margin, and the honest reading of an
amplitude-event result requires beating it, not merely beating zero.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.signal import lfilter

from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p
from llm2.diagnostics.wave import _bandpass_coeffs
from llm2.diagnostics.wave_mining_guard import forbid_analytic_import
from llm2.diagnostics.wavemetrics import DEFAULT_SLOPE_K, RANK_WINDOW, build_causal_metrics
from llm2.research_policy import EventStudySpec, require_matched_control

forbid_analytic_import(globals())

AMP_SURGE_PCTS: tuple[float, ...] = (85.0, 95.0)
AMP_COLLAPSE_PCTS: tuple[float, ...] = (15.0, 5.0)
SLOPE_BURST_PCT = 90.0
MIN_EVENTS = 20
CONTROL_MARGIN_BARS = 2  # the "+k" in "group_delay + k"

AMPLITUDE_EVENT_STUDY_SPEC = EventStudySpec(
    name="wave_amplitude_event",
    event_definition="trailing-percentile-rank crossing of causal wave amplitude/slope",
    treatment_arm="amp_surge / amp_collapse / amp_slope_burst",
    control_arm="trailing_move_control at filter group_delay + margin",
    matching="volatility-matched: control window equals the filter's own group delay so "
    "both arms are exposed to comparably-sized trailing moves",
)


def group_delay_bars(period: float) -> int:
    """Bars of delay the forward-only bandpass introduces at this period.

    Measured directly from the filter's impulse response rather than assumed from a formula:
    the biquad's delay is not exactly linear in period
    (``tests/test_wave.py::test_filter_group_delay_grows_with_period``).
    """
    b, a = _bandpass_coeffs(period)
    n = max(64, int(round(period * 20)))
    impulse = np.zeros(n)
    impulse[0] = 1.0
    response = lfilter(b, a, impulse)
    return int(np.argmax(np.abs(response)))


def _pct_rank_crossing(rank: pd.Series, threshold: float, *, up: bool) -> pd.Series:
    prev = rank.shift(1)
    if up:
        return ((prev < threshold) & (rank >= threshold)).fillna(False)
    return ((prev > threshold) & (rank <= threshold)).fillna(False)


def _sign_events(events: dict[str, pd.Series], wave_change: pd.Series) -> dict[str, pd.Series]:
    signed: dict[str, pd.Series] = {}
    for name, ev in events.items():
        signed[f"{name}_up"] = (ev & (wave_change > 0)).fillna(False)
        signed[f"{name}_down"] = (ev & (wave_change < 0)).fillna(False)
    return signed


def detect_amplitude_events(
    metrics: pd.DataFrame,
    *,
    period: float,
    surge_pcts: tuple[float, ...] = AMP_SURGE_PCTS,
    collapse_pcts: tuple[float, ...] = AMP_COLLAPSE_PCTS,
    slope_burst_pct: float = SLOPE_BURST_PCT,
) -> dict[str, pd.Series]:
    """Amplitude-derived events, unsigned and signed by the preceding half-period leg."""
    out: dict[str, pd.Series] = {}
    amp_rank = metrics["amp_pct_rank_500"]
    for p in surge_pcts:
        out[f"amp_surge_{int(p)}"] = _pct_rank_crossing(amp_rank, p, up=True)
    for p in collapse_pcts:
        out[f"amp_collapse_{int(p)}"] = _pct_rank_crossing(amp_rank, p, up=False)

    slope_col = f"amp_slope_{DEFAULT_SLOPE_K}"
    slope_rank = (
        metrics[slope_col].rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).rank(pct=True) * 100.0
    )
    out["amp_slope_burst"] = _pct_rank_crossing(slope_rank, slope_burst_pct, up=True)

    half_period = max(1, int(round(period / 2.0)))
    wave_change = metrics["wave"] - metrics["wave"].shift(half_period)
    out.update(_sign_events(out, wave_change))
    return out


def realised_vol_percentile_events(
    close: pd.Series, *, window: int = 168, pcts: tuple[float, ...] = AMP_SURGE_PCTS
) -> dict[str, pd.Series]:
    """Benchmark: trailing realised-volatility percentile crossings, no wave involved."""
    ret = np.log(close.replace(0, np.nan)).diff()
    vol = ret.rolling(window, min_periods=window // 4).std()
    rank = vol.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).rank(pct=True) * 100.0
    return {f"vol_surge_{int(p)}": _pct_rank_crossing(rank, p, up=True) for p in pcts}


def atr_percentile_events(
    ohlcv: pd.DataFrame, *, window: int = 14, pcts: tuple[float, ...] = AMP_SURGE_PCTS
) -> dict[str, pd.Series]:
    """Benchmark: trailing Average True Range percentile crossings, no wave involved."""
    high, low, close = ohlcv["high"], ohlcv["low"], ohlcv["close"]
    prev = close.shift(1)
    tr = pd.concat([high - low, (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    atr = tr.rolling(window, min_periods=max(2, window // 2)).mean()
    rank = atr.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).rank(pct=True) * 100.0
    return {f"atr_surge_{int(p)}": _pct_rank_crossing(rank, p, up=True) for p in pcts}


def trailing_move_control_events(
    close: pd.Series,
    *,
    group_delay: int,
    margin_bars: int = CONTROL_MARGIN_BARS,
    threshold_sigma: float = 2.0,
    vol_window: int = 168,
) -> pd.Series:
    """The decisive control: a plain trailing move measured over the filter's own delay.

    If amplitude events do no better than this, the wave has added nothing beyond re-finding
    a big trailing move through a more roundabout, delayed route.
    """
    window = max(1, group_delay + margin_bars)
    log_c = np.log(close.replace(0, np.nan))
    move = log_c.diff(window)
    sigma = move.rolling(vol_window, min_periods=vol_window // 2).std().shift(1)
    z = move / sigma.replace(0, np.nan)
    return (z.abs() >= threshold_sigma).fillna(False)


def score_events(
    close: pd.Series,
    events: dict[str, pd.Series],
    *,
    horizons: tuple[int, ...],
    min_events: int = MIN_EVENTS,
) -> list[Effect]:
    """Direction and magnitude of the forward return at each event, scored separately.

    Both are measured as an excess over the unconditional mean of the same statistic on the
    same horizon: crypto's drift makes an unconditional-zero comparison for direction, and an
    unconditional-zero comparison for |return|, equally misleading.
    """
    log_c = np.log(close.replace(0, np.nan))
    effects: list[Effect] = []
    for h in horizons:
        fwd = (log_c.shift(-h) - log_c).to_numpy()
        base_dir = float(np.nanmean(fwd))
        base_mag = float(np.nanmean(np.abs(fwd)))
        for name, ev in events.items():
            bars = np.flatnonzero(ev.to_numpy())
            bars = bars[bars < fwd.size]
            if bars.size < min_events:
                continue
            vals = fwd[bars]
            finite = np.isfinite(vals)
            vals = vals[finite]
            if vals.size < min_events:
                continue

            mean_d, t_d = newey_west_tstat(vals - base_dir, lags=h)
            effects.append(
                Effect(
                    name=f"{name}|direction|fwd{h}",
                    statistic=float(mean_d),
                    n=int(vals.size),
                    p_value=normal_two_sided_p(t_d),
                    detail={
                        "t_hac": float(t_d),
                        "excess_bps": float(mean_d * 1e4),
                        "horizon": float(h),
                        "n_events": float(vals.size),
                    },
                )
            )

            mag = np.abs(vals) - base_mag
            mean_m, t_m = newey_west_tstat(mag, lags=h)
            effects.append(
                Effect(
                    name=f"{name}|magnitude|fwd{h}",
                    statistic=float(mean_m),
                    n=int(mag.size),
                    p_value=normal_two_sided_p(t_m),
                    detail={
                        "t_hac": float(t_m),
                        "excess_abs_bps": float(mean_m * 1e4),
                        "horizon": float(h),
                        "n_events": float(mag.size),
                    },
                )
            )
    return effects


def run_amplitude_event_study(
    ohlcv: pd.DataFrame,
    period: float,
    horizons: tuple[int, ...] = (6, 24, 96),
    *,
    volume: pd.Series | None = None,
) -> list[Effect]:
    """Full amplitude-event scan: treatment, benchmarks and control, one FDR family.

    Every effect name carries its arm (``amp_surge_95_up|direction|fwd24``,
    ``trailing_move_control|magnitude|fwd24``, ...) so the treatment can be read against its
    benchmarks after the fact without re-running anything.
    """
    require_matched_control(AMPLITUDE_EVENT_STUDY_SPEC)

    close = ohlcv["close"]
    vol_series = volume if volume is not None else ohlcv.get("volume")
    metrics = build_causal_metrics(close, vol_series, period)

    events = dict(detect_amplitude_events(metrics, period=period))
    events.update(realised_vol_percentile_events(close))
    events.update(atr_percentile_events(ohlcv))

    delay = group_delay_bars(period)
    events["trailing_move_control"] = trailing_move_control_events(close, group_delay=delay)

    effects = score_events(close, events, horizons=horizons)
    for eff in effects:
        eff.detail["group_delay_bars"] = float(delay)
    return apply_fdr(effects)
