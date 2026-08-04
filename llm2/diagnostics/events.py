"""Event study around price pulses: what moves before, during and after a large move?

Two design constraints decide whether this is research or self-deception.

**The pulse must be knowable when it is flagged.** A pulse defined as "the bar where a big
move happened" is flagged using the move itself, so the during-window is guaranteed to look
dramatic and the after-window is guaranteed to look like whatever follows big moves. Only
the *before* window can contain tradeable information, and only if the flag depends on
nothing after it. Every pulse here is detected from a trailing move measured against a
trailing volatility estimate, so its timestamp is the first instant it could have been
known.

**Everything moves around a big move.** Cross-asset volatility is synchronised, so a naive
event study shows every series displaced around every pulse. The null therefore relocates
pseudo-events to bars matched on volatility: the question is not "does the panel move
around pulses" but "does it move *differently* around real pulses than around equally
volatile non-pulses".
"""

from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

from llm2.diagnostics.stats import Effect, apply_fdr


def detect_pulses(
    ohlcv: pd.DataFrame,
    *,
    lookback: int = 6,
    vol_window: int = 168,
    threshold_sigma: float = 3.0,
    min_gap: int = 24,
) -> pd.DataFrame:
    """Bars where a trailing move exceeded ``threshold_sigma`` trailing standard deviations.

    Normalising by trailing volatility rather than a fixed percentage matters: a fixed
    threshold would select almost entirely from 2021 and almost never from quiet years, so
    the "event study" would really be a study of one regime.
    """
    close = ohlcv["close"]
    log_c = np.log(close.replace(0, np.nan))
    move = log_c.diff(lookback)
    # Volatility of the same lookback-length move, estimated strictly from the past.
    sigma = move.rolling(vol_window, min_periods=vol_window // 2).std().shift(1)
    z = move / sigma.replace(0, np.nan)

    is_pulse = z.abs() >= threshold_sigma
    idx = np.flatnonzero(is_pulse.to_numpy())

    # Enforce a minimum gap so one long move is not counted as dozens of overlapping events.
    kept: list[int] = []
    last = -(10**9)
    for i in idx:
        if i - last >= min_gap:
            kept.append(int(i))
            last = int(i)

    return pd.DataFrame(
        {
            "bar": kept,
            "timestamp": ohlcv.index[kept],
            "z": z.to_numpy()[kept],
            "direction": np.sign(z.to_numpy()[kept]).astype(int),
            "vol": sigma.to_numpy()[kept],
        }
    )


def _standardize(frame: pd.DataFrame, window: int = 720) -> pd.DataFrame:
    """Causal z-score per column, so paths across series are on a comparable scale."""
    mean = frame.rolling(window, min_periods=window // 4).mean()
    std = frame.rolling(window, min_periods=window // 4).std()
    return (frame - mean) / std.replace(0, np.nan)


def event_paths(
    features: pd.DataFrame,
    pulses: pd.DataFrame,
    *,
    before: int = 24,
    after: int = 24,
    direction: int | None = None,
) -> pd.DataFrame:
    """Mean standardised feature path over the window around each pulse.

    Returns a frame indexed by relative bar offset (negative is before the pulse) with one
    column per feature. Extraction is vectorized: one gather over an offsets matrix rather
    than a loop over events.
    """
    if pulses.empty:
        return pd.DataFrame()

    sel = pulses if direction is None else pulses[pulses["direction"] == direction]
    if sel.empty:
        return pd.DataFrame()

    z = _standardize(features)
    arr = z.to_numpy()
    n = arr.shape[0]

    offsets = np.arange(-before, after + 1)
    bars = sel["bar"].to_numpy()[:, None] + offsets[None, :]
    valid = (bars >= 0) & (bars < n)
    bars_clipped = np.clip(bars, 0, n - 1)

    # (n_events, n_offsets, n_features)
    gathered = arr[bars_clipped]
    gathered[~valid] = np.nan

    mean_path = np.nanmean(gathered, axis=0)
    return pd.DataFrame(mean_path, index=pd.Index(offsets, name="offset"), columns=z.columns)


def pre_event_displacement(
    features: pd.DataFrame,
    ohlcv: pd.DataFrame,
    pulses: pd.DataFrame,
    *,
    before: int = 12,
    n_pseudo: int = 200,
    seed: int = 0,
    direction: int | None = None,
) -> list[Effect]:
    """Which features are displaced *before* a pulse, beyond volatility-matched controls.

    This is the only part of the event study that can become a strategy. The statistic is
    the mean standardised feature level over the ``before`` bars leading into the pulse,
    compared against the same statistic at pseudo-events drawn from bars with comparable
    trailing volatility.
    """
    if pulses.empty:
        return []

    sel = pulses if direction is None else pulses[pulses["direction"] == direction]
    if len(sel) < 20:
        return []

    z = _standardize(features)
    arr = z.to_numpy()
    n = arr.shape[0]
    offsets = np.arange(-before, 0)

    def window_mean(bars: np.ndarray) -> np.ndarray:
        pos = bars[:, None] + offsets[None, :]
        valid = (pos >= 0) & (pos < n)
        gathered = arr[np.clip(pos, 0, n - 1)]
        gathered[~valid] = np.nan
        # Events before the standardisation window fills give all-NaN slices; NaN is the
        # correct answer for those, so the expected warning is suppressed rather than
        # worked around.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            return np.nanmean(np.nanmean(gathered, axis=1), axis=0)

    observed = window_mean(sel["bar"].to_numpy())

    # Volatility-matched controls: sample pseudo-events from bars in the same trailing
    # volatility decile as the real pulses, so "big move days are different" cannot pass.
    vol = np.log(ohlcv["close"].replace(0, np.nan)).diff().rolling(168, min_periods=42).std()
    vol_rank = vol.rank(pct=True).to_numpy()
    pulse_ranks = vol_rank[sel["bar"].to_numpy()]
    lo, hi = np.nanpercentile(pulse_ranks, [10, 90])

    eligible = np.flatnonzero(np.isfinite(vol_rank) & (vol_rank >= lo) & (vol_rank <= hi))
    eligible = eligible[(eligible > before) & (eligible < n - 1)]
    if eligible.size < len(sel) * 2:
        return []

    rng = np.random.default_rng(seed)
    null = np.empty((n_pseudo, arr.shape[1]))
    for i in range(n_pseudo):
        pseudo = rng.choice(eligible, size=len(sel), replace=False)
        null[i] = window_mean(pseudo)

    effects: list[Effect] = []
    for j, col in enumerate(z.columns):
        obs = observed[j]
        col_null = null[:, j]
        col_null = col_null[np.isfinite(col_null)]
        if not np.isfinite(obs) or col_null.size < 20:
            continue
        p = float((1.0 + np.sum(np.abs(col_null - np.mean(col_null)) >= abs(obs - np.mean(col_null)))) / (1.0 + col_null.size))
        sd = float(np.std(col_null))
        effects.append(
            Effect(
                name=f"pre_event[{col}]",
                statistic=float(obs),
                n=int(len(sel)),
                p_value=p,
                ci_low=float(obs - 1.96 * sd),
                ci_high=float(obs + 1.96 * sd),
                detail={
                    "null_mean": float(np.mean(col_null)),
                    "null_sd": sd,
                    "z_vs_null": float((obs - np.mean(col_null)) / sd) if sd > 0 else float("nan"),
                    "n_events": float(len(sel)),
                },
            )
        )
    return apply_fdr(effects)


def pulse_forward_outcome(
    ohlcv: pd.DataFrame, pulses: pd.DataFrame, *, horizons: tuple[int, ...] = (6, 24, 96)
) -> list[Effect]:
    """What happens after a pulse: continuation or reversal, by direction.

    Descriptive counterpart to the pre-event analysis. Conditioning on the pulse itself is
    legitimate here because the pulse is knowable at its own timestamp.
    """
    from llm2.diagnostics.stats import newey_west_tstat, normal_two_sided_p

    if pulses.empty:
        return []

    close = ohlcv["close"]
    log_c = np.log(close.replace(0, np.nan))
    effects: list[Effect] = []

    for h in horizons:
        fwd = (log_c.shift(-h) - log_c).to_numpy()
        for d, label in ((1, "up"), (-1, "down")):
            bars = pulses.loc[pulses["direction"] == d, "bar"].to_numpy()
            if bars.size < 20:
                continue
            vals = fwd[bars]
            vals = vals[np.isfinite(vals)]
            if vals.size < 20:
                continue
            mean, t_stat = newey_west_tstat(vals, lags=h)
            effects.append(
                Effect(
                    name=f"after_{label}_pulse|fwd{h}",
                    statistic=float(mean),
                    n=int(vals.size),
                    p_value=normal_two_sided_p(t_stat),
                    detail={
                        "t_hac": float(t_stat),
                        "mean_bps": float(mean * 1e4),
                        # Sign relative to the pulse: positive means continuation.
                        "continuation_bps": float(mean * d * 1e4),
                    },
                )
            )
    return apply_fdr(effects)
