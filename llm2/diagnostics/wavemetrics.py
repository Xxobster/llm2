"""Causal metrics of the market-strength wave: amplitude, phase and their derivatives.

Every column here is built from :func:`llm2.diagnostics.wave.causal_wave` alone. That
function's warmup blanking (roughly three periods) is inherited rather than re-derived —
the mask is read straight off the wave it returns and re-applied to every metric computed
from it, so a metric can never be non-NaN where the underlying wave itself was still an
untrustworthy filter transient. Nothing here backfills: a metric that needs a longer window
than the wave's own warmup (the trailing percentile ranks, in particular) simply starts NaN
for longer, and stays NaN rather than being seeded with a stand-in value.

The two families are the amplitude/phase state of the wave itself (amp, phase, their slopes
and curvature, instantaneous period, bars since the last zero-crossing or peak) and the
energy/coherence family that asks how much of *this* is genuine cyclical structure rather
than broadband noise passing through the filter (energy, its trailing percentile rank,
coherence of the phase rotation, and how well a pure sinusoid at the fitted period explains
the recent path).

``detect_triggers`` turns a subset of these into boolean entry conditions: a phase-velocity
turning point (the wave "peaked" one bar ago, which is the earliest a peak can be known),
an ascending threshold grid on the phase itself, and a capitulation flag that requires the
energy and volume to both be in their top decile *and* a peak turn to have just occurred,
signed by which way the wave had been moving into that turn.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.diagnostics.wave import causal_wave
from llm2.diagnostics.wave_mining_guard import forbid_analytic_import

forbid_analytic_import(globals())

# Slope horizons, in bars. Three scales rather than one because a 2-bar slope answers "is
# this turning right now" while an 8-bar slope answers "has the broader push held up".
SLOPE_KS: tuple[int, ...] = (2, 4, 8)
DEFAULT_SLOPE_K = 4

RANK_WINDOW = 500
REALISED_VOL_WINDOW = 168
PHASE_VELOCITY_EPS = 1e-6


def _bars_since_event(event: np.ndarray, index: pd.Index) -> pd.Series:
    """Bars elapsed since the most recent ``True`` in ``event``, NaN before the first one.

    Vectorized via a forward-fill of each event's own position: legitimate causal use of
    ``ffill`` because what is being carried forward is "when did this last happen", which is
    knowable at every subsequent bar, not a future value being smuggled backward.
    """
    n = event.size
    positions = np.arange(n, dtype=float)
    last_event_pos = np.where(event, positions, np.nan)
    last_event_pos = pd.Series(last_event_pos, index=index).ffill().to_numpy()
    return pd.Series(positions - last_event_pos, index=index)


def build_causal_metrics(close: pd.Series, volume: pd.Series | None, period: float) -> pd.DataFrame:
    """Causal amplitude/phase metric panel for one series at one fitted period.

    ``close`` and ``volume`` share an index; ``volume`` may be omitted, in which case
    ``volume_pct_rank_500`` and the capitulation trigger's volume leg are unavailable.
    """
    close = pd.to_numeric(close, errors="coerce")
    log_c = np.log(close.where(close > 0)).interpolate(limit_direction="both")
    wave, amp, phase = causal_wave(log_c, period)
    idx = close.index
    warmup = wave.isna()

    out = pd.DataFrame(index=idx)
    out["wave"] = wave
    out["amp"] = amp
    out["phase"] = phase

    for k in SLOPE_KS:
        out[f"amp_slope_{k}"] = (amp - amp.shift(k)) / k
        out[f"wave_slope_{k}"] = (wave - wave.shift(k)) / k

    # Discrete second derivative at a 4-bar step: cheap and avoids amplifying single-bar
    # filter jitter the way a step-1 second difference would.
    out["amp_accel"] = (amp - 2.0 * amp.shift(4) + amp.shift(8)) / 16.0
    out["wave_curvature"] = (wave - 2.0 * wave.shift(4) + wave.shift(8)) / 16.0

    out["amp_pct_rank_500"] = (
        amp.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).rank(pct=True) * 100.0
    )

    realised_vol = log_c.diff().rolling(
        REALISED_VOL_WINDOW, min_periods=REALISED_VOL_WINDOW // 4
    ).std()
    out["amp_over_realised_vol"] = amp / realised_vol.replace(0, np.nan)

    base_mean = wave.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).mean()
    base_std = wave.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).std()
    out["wave_level_z"] = (wave - base_mean) / base_std.replace(0, np.nan)

    sign = np.sign(wave.to_numpy())
    sign_prev = np.concatenate([[np.nan], sign[:-1]])
    zero_cross = np.nan_to_num(sign * sign_prev, nan=1.0) < 0
    out["bars_since_zero_cross"] = _bars_since_event(zero_cross, idx)

    dphi = phase.diff()
    phase_velocity = (dphi + np.pi) % (2.0 * np.pi) - np.pi  # wrap to (-pi, pi]
    out["phase_velocity"] = phase_velocity

    pv = phase_velocity.to_numpy()
    with np.errstate(divide="ignore", invalid="ignore"):
        inst_period = np.where(np.abs(pv) > PHASE_VELOCITY_EPS, 2.0 * np.pi / np.abs(pv), np.nan)
    out["inst_period"] = pd.Series(inst_period, index=idx)
    drift_k = max(1, int(round(period)))
    out["period_drift"] = out["inst_period"].diff(drift_k)

    # A peak in the rotation is known the bar the velocity, having been rising, turns
    # non-positive — one bar after the true turning point, which is the earliest that turn
    # can be known without looking ahead.
    prev_pv = phase_velocity.shift(1)
    prev_prev_pv = phase_velocity.shift(2)
    peak_turn = (prev_pv > 0) & (prev_pv > prev_prev_pv) & (phase_velocity <= 0)
    out["bars_since_last_peak"] = _bars_since_event(peak_turn.fillna(False).to_numpy(), idx)

    energy = amp**2
    out["energy"] = energy
    out["energy_slope"] = (energy - energy.shift(DEFAULT_SLOPE_K)) / DEFAULT_SLOPE_K
    out["power"] = energy * phase_velocity.abs()
    out["energy_pct_rank_500"] = (
        energy.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).rank(pct=True) * 100.0
    )

    # Coherence: how steady the phase rotation is, relative to its own trailing magnitude. A
    # clean cycle rotates at a near-constant rate; broadband noise passing through the same
    # filter jitters, including sign flips. 1 means metronomic, 0 means the rotation rate is
    # as noisy as it is fast.
    pv_win = max(8, int(round(period * 3)))
    pv_std = phase_velocity.rolling(pv_win, min_periods=pv_win // 2).std()
    pv_abs_mean = phase_velocity.abs().rolling(pv_win, min_periods=pv_win // 2).mean()
    out["coherence"] = (1.0 - pv_std / pv_abs_mean.replace(0, np.nan)).clip(lower=0.0, upper=1.0)

    # How much of the recent bar-to-bar return is explained by the wave's own bar-to-bar
    # change: a rolling R^2 of one against the other, using only the trailing window.
    r2_win = max(16, int(round(period * 5)))
    ret = log_c.diff()
    roll_corr = ret.rolling(r2_win, min_periods=r2_win // 2).corr(wave.diff())
    out["sinusoid_r2"] = roll_corr**2

    out["amp_x_slope"] = out["amp"] * out[f"amp_slope_{DEFAULT_SLOPE_K}"]
    out["energy_x_coherence"] = out["energy"] * out["coherence"]

    # Every wave-derived column is blanked for exactly as long as causal_wave's own warmup,
    # and never backfilled: a metric with a longer intrinsic window (the percentile ranks,
    # coherence, sinusoid_r2) simply stays NaN past that point until its own window fills.
    wave_cols = [c for c in out.columns]
    out.loc[warmup, wave_cols] = np.nan

    if volume is not None:
        vol = pd.to_numeric(volume, errors="coerce").reindex(idx)
        out["volume_pct_rank_500"] = (
            vol.rolling(RANK_WINDOW, min_periods=RANK_WINDOW // 2).rank(pct=True) * 100.0
        )

    return out


def detect_triggers(
    metrics: pd.DataFrame,
    *,
    period: float,
    phase_thresholds: tuple[float, ...] = (1.8, 2.1, 2.4, 2.7),
    energy_rank_floor: float = 90.0,
    volume_rank_floor: float = 90.0,
) -> dict[str, pd.Series]:
    """Boolean trigger conditions derived from :func:`build_causal_metrics` output.

    ``peak_detect``
        The phase-velocity turning point described in :func:`build_causal_metrics`, exposed
        directly as a trigger rather than only as ``bars_since_last_peak == 0``.

    ``threshold_up_{x}``
        Phase crosses upward through ``x`` radians, for each of ``phase_thresholds``. All
        thresholds are comfortably inside ``(-pi, pi]`` so no unwrap is needed.

    ``capitulation`` / ``capitulation_up`` / ``capitulation_down``
        Energy and volume both in their trailing top decile *and* a peak turn on the same
        bar. Direction comes from the sign of the wave's own change over the preceding
        half-period — the leg that was running into the turn — not from the peak turn itself,
        which by construction says only that momentum stalled, not which way it had been
        going.
    """
    phase = metrics["phase"]
    phase_velocity = metrics["phase_velocity"]

    prev_pv = phase_velocity.shift(1)
    prev_prev_pv = phase_velocity.shift(2)
    peak_detect = ((prev_pv > 0) & (prev_pv > prev_prev_pv) & (phase_velocity <= 0)).fillna(False)

    out: dict[str, pd.Series] = {"peak_detect": peak_detect}

    prev_phase = phase.shift(1)
    for thr in phase_thresholds:
        key = f"threshold_up_{thr}".replace(".", "p")
        out[key] = ((prev_phase < thr) & (phase >= thr)).fillna(False)

    half_period = max(1, int(round(period / 2.0)))
    wave_change = metrics["wave"] - metrics["wave"].shift(half_period)

    energy_hi = metrics["energy_pct_rank_500"] >= energy_rank_floor
    if "volume_pct_rank_500" in metrics.columns:
        volume_hi = metrics["volume_pct_rank_500"] >= volume_rank_floor
    else:
        volume_hi = pd.Series(False, index=metrics.index)

    capitulation = (energy_hi & peak_detect & volume_hi).fillna(False)
    out["capitulation"] = capitulation
    out["capitulation_up"] = (capitulation & (wave_change > 0)).fillna(False)
    out["capitulation_down"] = (capitulation & (wave_change < 0)).fillna(False)
    return out
