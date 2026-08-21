"""Boundary-break study on confirmed swing structure: does a break continue or reverse?

Four boundary constructions, all evaluated with the same confirmation rules so results are
comparable across them:

``swing``
    The single last confirmed swing high (resistance) / swing low (support), read straight
    from ``bar_features.last_sh_price`` / ``last_sl_price`` — already confirmation-time safe
    by construction (see ``llm2.data.indicators`` module docstring).
``channel``
    A line through the **last two** confirmed swings of one kind, projected forward in bar
    units. Two confirmed points are needed for a slope, which ``bar_features`` alone does not
    carry (it stores only the single most recent swing); the ``swings`` table does, and the
    join below is a backward as-of merge on ``confirm_ts_ms``, so the second point is exactly
    as confirmation-time-safe as the first.
``donchianN`` (N in 20, 50) — **benchmark**
    The rolling N-bar high/low, shifted one bar so the current bar's own extreme cannot
    define its own boundary. Deliberately the simplest possible construction: if a swing or
    channel break does no better than this, the confirmed-swing machinery has added nothing.
``placebo``
    40%/60% of the trailing range — an arbitrary level with no structural claim attached,
    required by :func:`llm2.research_policy.require_placebo_arm` before anything here is
    trusted as evidence that *structure*, rather than *proximity to any level near the edge
    of a recent range*, is doing the work.

Three confirmation rules per boundary (``close_beyond``, ``close_beyond_atr``, ``retest``),
each in both directions, each scored for **continuation** and **reversal/false-breakout**
rather than continuation alone — a boundary that "works" by reliably faking out is exactly
as tradeable as one that works by continuing, just with the sign flipped, and reporting only
one side would hide that.

**The coil filter is deliberately fenced off from lookahead.** "The market coiled before it
broke" is a claim that can only be evaluated using the amplitude reading *before* the break,
never at or after it — reading amplitude at the break bar would let the break itself (which
is exactly the kind of high-energy event the wave amplitude responds to) contaminate the
"was it quiet beforehand" question. :func:`coil_filter` takes an explicit ``lookback_bars``
and raises :class:`CoilLookaheadError` rather than silently clamping if it is asked to read
at bar 0 lookback or later.
"""

from __future__ import annotations

import sqlite3

import numpy as np
import pandas as pd

from llm2.data.indicators import INDICATORS_DB, SWING_LEFT, SWING_RIGHT, align_multi_timeframe, load_bar_features
from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p
from llm2.diagnostics.wave_mining_guard import forbid_analytic_import
from llm2.diagnostics.wavemetrics import build_causal_metrics
from llm2.research_policy import EventStudySpec, LevelClaim, require_matched_control, require_placebo_arm

forbid_analytic_import(globals())


class CoilLookaheadError(RuntimeError):
    """The coil filter was asked to read wave amplitude at or after the break bar."""


DONCHIAN_NS: tuple[int, ...] = (20, 50)
BREAK_ATR_MULT = 0.25
RETEST_ATR_MULT = 0.25
RETEST_MAX_WAIT = 20
COIL_LOOKBACK_BARS = 1
COIL_TERCILE = 100.0 / 3.0
DEFAULT_MAX_HOLD = 96
MIN_BREAK_EVENTS = 15

PLACEBO_LOWER_FRAC = 0.40
PLACEBO_UPPER_FRAC = 0.60
PLACEBO_RANGE_WINDOW = 50

BOUNDARY_LEVEL_CLAIM = LevelClaim(
    name="structure_break_boundary",
    real_ratios=(0.0, 1.0),  # swing/channel/donchian sit at the extremes of the range
    placebo_ratios=(PLACEBO_LOWER_FRAC, PLACEBO_UPPER_FRAC),
    anchors="trailing Donchian range (rolling high/low, shifted one bar) over the same window",
    proximity_band="exact boundary crossing, not a proximity band",
)

BREAK_EVENT_STUDY_SPEC = EventStudySpec(
    name="structure_break",
    event_definition="close beyond a swing/channel/donchian boundary, plain/ATR-margin/retest",
    treatment_arm="swing / channel boundary break",
    control_arm="donchian benchmark break + placebo-boundary break (40%/60% of trailing range)",
    matching="volatility-matched: the same trailing-range construction and ATR confirmation "
    "margin are applied to every boundary, real and placebo alike",
)


def _atr(ohlcv: pd.DataFrame, window: int = 14) -> pd.Series:
    high, low, close = ohlcv["high"], ohlcv["low"], ohlcv["close"]
    prev = close.shift(1)
    tr = pd.concat([high - low, (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    return tr.rolling(window, min_periods=max(2, window // 2)).mean()


# --------------------------------------------------------------------------------------
# Boundaries
# --------------------------------------------------------------------------------------


def _load_swings(symbol: str, timeframe: str, *, source: str, kind: str) -> pd.DataFrame:
    """Confirmed swing pivots of one kind ('high' or 'low'), ordered by confirmation time.

    ``pivot_i`` is the swing's own positional row index in the same ``(symbol, timeframe,
    source, swing_left, swing_right)`` bar ordering used by ``bar_features`` (verified
    directly against the warehouse), which lets the channel line below be projected in bar
    units instead of calendar time.
    """
    if not INDICATORS_DB.is_file():
        raise FileNotFoundError(f"Indicator warehouse missing: {INDICATORS_DB}")
    conn = sqlite3.connect(f"file:{INDICATORS_DB}?mode=ro", uri=True, timeout=120.0)
    try:
        conn.execute("PRAGMA busy_timeout=120000")
        df = pd.read_sql(
            "SELECT pivot_i, pivot_ts_ms, confirm_ts_ms, price FROM swings "
            "WHERE symbol = ? AND timeframe = ? AND source = ? AND swing_left = ? "
            "AND swing_right = ? AND kind = ? ORDER BY confirm_ts_ms",
            conn,
            params=(symbol.upper(), timeframe, source, SWING_LEFT, SWING_RIGHT, kind),
        )
    finally:
        conn.close()
    return df


def channel_line(
    swings: pd.DataFrame, decision_index: pd.DatetimeIndex, decision_pos: np.ndarray
) -> pd.Series:
    """Line through the last two confirmed swings of one kind, projected onto each bar.

    ``swings`` must carry ``pivot_i``, ``confirm_ts_ms`` and ``price``. The second-most-recent
    swing is attached to the most recent one via a plain ``shift(1)`` *before* the as-of join,
    so a decision bar can never see a swing confirmed after it: the join only ever looks
    backward from ``decision_at`` to ``confirm_ts_ms``, and both swings it finds were already
    confirmed at or before that instant.
    """
    if swings.empty:
        return pd.Series(np.nan, index=decision_index)

    s = swings.sort_values("confirm_ts_ms").reset_index(drop=True)
    s["prev_price"] = s["price"].shift(1)
    s["prev_pivot_i"] = s["pivot_i"].shift(1)

    # merge_asof requires identical datetime unit/tz dtypes (us vs ms fails hard).
    left = pd.DataFrame(
        {
            "decision_at": pd.DatetimeIndex(decision_index)
            .tz_convert("UTC")
            .astype("datetime64[ns, UTC]"),
            "pos": decision_pos,
        }
    ).sort_values("decision_at")
    right = s.rename(columns={"confirm_ts_ms": "confirm_at"}).copy()
    right["confirm_at"] = pd.to_datetime(
        right["confirm_at"].to_numpy(), unit="ms", utc=True
    ).astype("datetime64[ns, UTC]")
    right = right.sort_values("confirm_at")

    merged = pd.merge_asof(left, right, left_on="decision_at", right_on="confirm_at", direction="backward")
    merged = merged.sort_values("pos")

    denom = (merged["pivot_i"] - merged["prev_pivot_i"]).replace(0, np.nan)
    slope = (merged["price"] - merged["prev_price"]) / denom
    value = merged["price"].to_numpy() + slope.to_numpy() * (
        merged["pos"].to_numpy() - merged["pivot_i"].to_numpy()
    )
    return pd.Series(value, index=decision_index)


def donchian_boundaries(
    ohlcv: pd.DataFrame, *, windows: tuple[int, ...] = DONCHIAN_NS
) -> pd.DataFrame:
    """Rolling N-bar high/low, shifted one bar so a bar cannot define its own boundary."""
    high, low = ohlcv["high"], ohlcv["low"]
    out = pd.DataFrame(index=ohlcv.index)
    for n in windows:
        out[f"donchian{n}_upper"] = high.rolling(n, min_periods=n).max().shift(1)
        out[f"donchian{n}_lower"] = low.rolling(n, min_periods=n).min().shift(1)
    return out


def placebo_boundaries(
    ohlcv: pd.DataFrame,
    *,
    window: int = PLACEBO_RANGE_WINDOW,
    lower_frac: float = PLACEBO_LOWER_FRAC,
    upper_frac: float = PLACEBO_UPPER_FRAC,
) -> pd.DataFrame:
    """Arbitrary levels inside the trailing range: no structural claim, deliberately."""
    require_placebo_arm(BOUNDARY_LEVEL_CLAIM)
    high, low = ohlcv["high"], ohlcv["low"]
    range_high = high.rolling(window, min_periods=window).max().shift(1)
    range_low = low.rolling(window, min_periods=window).min().shift(1)
    span = range_high - range_low
    out = pd.DataFrame(index=ohlcv.index)
    out["placebo_upper"] = range_low + upper_frac * span
    out["placebo_lower"] = range_low + lower_frac * span
    return out


def build_boundaries(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    *,
    source: str = "binance",
    donchian_windows: tuple[int, ...] = DONCHIAN_NS,
) -> pd.DataFrame:
    """All boundary families for one series, aligned on the bar-feature index."""
    raw = load_bar_features(symbol, timeframe, source=source)
    idx = raw.index
    pos = np.arange(len(idx))

    out = pd.DataFrame(index=idx)
    out["swing_upper"] = pd.to_numeric(raw["last_sh_price"], errors="coerce")
    out["swing_lower"] = pd.to_numeric(raw["last_sl_price"], errors="coerce")

    # The warehouse's own swing kind labels are 'high'/'low' (verified against
    # indicators.sqlite directly; NOT the 'SH'/'SL' shorthand used for bar_features'
    # last_sh_price/last_sl_price column names).
    sh = _load_swings(symbol, timeframe, source=source, kind="high")
    sl = _load_swings(symbol, timeframe, source=source, kind="low")
    out["channel_upper"] = channel_line(sh, idx, pos)
    out["channel_lower"] = channel_line(sl, idx, pos)

    aligned_ohlcv = ohlcv.reindex(idx)
    out = out.join(donchian_boundaries(aligned_ohlcv, windows=donchian_windows))
    out = out.join(placebo_boundaries(aligned_ohlcv))
    return out


BOUNDARY_PAIRS: dict[str, tuple[str, str]] = {
    "swing": ("swing_upper", "swing_lower"),
    "channel": ("channel_upper", "channel_lower"),
    "donchian20": ("donchian20_upper", "donchian20_lower"),
    "donchian50": ("donchian50_upper", "donchian50_lower"),
    "placebo": ("placebo_upper", "placebo_lower"),
}


# --------------------------------------------------------------------------------------
# Confirmations
# --------------------------------------------------------------------------------------


def _first_true(condition: pd.Series) -> pd.Series:
    """Rising edge of a boolean condition: True only on the bar it first becomes true."""
    cond = condition.fillna(False).astype(bool)
    return cond & ~cond.shift(1, fill_value=False)


def _retest_confirm(
    events: np.ndarray,
    close: np.ndarray,
    boundary: np.ndarray,
    atr: np.ndarray,
    *,
    direction: int,
    max_wait: int,
    atr_mult: float,
) -> np.ndarray:
    """First bar, within ``max_wait`` of a break, where price returns near the boundary.

    Bounded by the number of break events (typically tens to low hundreds), not by the
    length of the series, so the inner loop over the wait window is a small, fixed-size
    scan rather than a bar-by-bar pass over the whole history.
    """
    n = close.size
    out = np.zeros(n, dtype=bool)
    for t0 in np.flatnonzero(events):
        end = min(n, t0 + 1 + max_wait)
        for t in range(t0 + 1, end):
            c, b, a = close[t], boundary[t], atr[t]
            if not (np.isfinite(c) and np.isfinite(b) and np.isfinite(a)):
                continue
            dist = (c - b) * direction
            if dist < -atr_mult * a:
                break  # decisively broke back through; the retest window is over
            if abs(c - b) <= atr_mult * a:
                out[t] = True
                break
    return out


def detect_breaks(
    ohlcv: pd.DataFrame,
    upper: pd.Series,
    lower: pd.Series,
    *,
    atr: pd.Series,
    atr_mult: float = BREAK_ATR_MULT,
    retest_max_wait: int = RETEST_MAX_WAIT,
    retest_atr_mult: float = RETEST_ATR_MULT,
) -> dict[str, pd.Series]:
    """Break confirmations in both directions: plain close, ATR-margin close, and retest."""
    idx = upper.index
    close = ohlcv["close"].reindex(idx)
    atr = atr.reindex(idx)

    close_beyond_up = _first_true(close > upper)
    close_beyond_down = _first_true(close < lower)
    close_beyond_atr_up = _first_true((close - upper) >= atr_mult * atr)
    close_beyond_atr_down = _first_true((lower - close) >= atr_mult * atr)

    retest_up = pd.Series(
        _retest_confirm(
            close_beyond_up.to_numpy(),
            close.to_numpy(),
            upper.to_numpy(),
            atr.to_numpy(),
            direction=1,
            max_wait=retest_max_wait,
            atr_mult=retest_atr_mult,
        ),
        index=idx,
    )
    retest_down = pd.Series(
        _retest_confirm(
            close_beyond_down.to_numpy(),
            close.to_numpy(),
            lower.to_numpy(),
            atr.to_numpy(),
            direction=-1,
            max_wait=retest_max_wait,
            atr_mult=retest_atr_mult,
        ),
        index=idx,
    )

    return {
        "close_beyond_up": close_beyond_up,
        "close_beyond_down": close_beyond_down,
        "close_beyond_atr_up": close_beyond_atr_up,
        "close_beyond_atr_down": close_beyond_atr_down,
        "retest_up": retest_up,
        "retest_down": retest_down,
    }


CONFIRMATION_DIRECTIONS: tuple[tuple[str, int], ...] = (
    ("close_beyond_up", 1),
    ("close_beyond_atr_up", 1),
    ("retest_up", 1),
    ("close_beyond_down", -1),
    ("close_beyond_atr_down", -1),
    ("retest_down", -1),
)


# --------------------------------------------------------------------------------------
# Coil filter (causality-fenced)
# --------------------------------------------------------------------------------------


def coil_filter(
    amp_pct_rank: pd.Series,
    break_bars: np.ndarray,
    *,
    lookback_bars: int = COIL_LOOKBACK_BARS,
    tercile: float = COIL_TERCILE,
) -> np.ndarray:
    """True where wave amplitude, read strictly before the break, sat in the bottom tercile.

    ``amp_pct_rank`` is already a 0-100 trailing percentile rank, so "bottom tercile" is
    simply a threshold at ``100/3`` on it. ``lookback_bars`` must be at least 1: a value of 0
    would read amplitude at the break bar itself, which is exactly the bar the break's own
    volatility could inflate, and a negative value would read after it. Both raise rather
    than silently clamping to something causal.
    """
    if lookback_bars < 1:
        raise CoilLookaheadError(
            f"coil_filter called with lookback_bars={lookback_bars}; the coil condition must "
            "be read strictly BEFORE the break bar (lookback_bars >= 1)."
        )
    shifted = amp_pct_rank.shift(lookback_bars).to_numpy()
    values = shifted[break_bars]
    finite = np.isfinite(values)
    out = np.zeros(break_bars.shape, dtype=bool)
    out[finite] = values[finite] <= tercile
    return out


# --------------------------------------------------------------------------------------
# Outcomes
# --------------------------------------------------------------------------------------


def break_outcome(
    ohlcv: pd.DataFrame,
    break_bars: np.ndarray,
    *,
    direction: int,
    horizons: tuple[int, ...] = (6, 24, 96),
    min_events: int = MIN_BREAK_EVENTS,
) -> list[Effect]:
    """Continuation vs reversal/false-breakout rate and mean forward return, by horizon."""
    close = ohlcv["close"]
    log_c = np.log(close.replace(0, np.nan))
    effects: list[Effect] = []
    n = len(close)
    valid_bars = break_bars[break_bars < n]

    for h in horizons:
        fwd = (log_c.shift(-h) - log_c).to_numpy()
        vals = fwd[valid_bars]
        finite = np.isfinite(vals)
        vals = vals[finite]
        if vals.size < min_events:
            continue
        signed = vals * direction
        continuation_rate = float(np.mean(signed > 0))
        mean, t_stat = newey_west_tstat(signed, lags=h)
        effects.append(
            Effect(
                name=f"break|fwd{h}",
                statistic=float(mean),
                n=int(vals.size),
                p_value=normal_two_sided_p(t_stat),
                detail={
                    "t_hac": float(t_stat),
                    "mean_bps": float(mean * 1e4),
                    "continuation_rate": continuation_rate,
                    "reversal_rate": float(1.0 - continuation_rate),
                    "horizon": float(h),
                    "direction": float(direction),
                    "n_events": float(vals.size),
                },
            )
        )
    return effects


def structural_bracket_outcome(
    ohlcv: pd.DataFrame,
    break_bars: np.ndarray,
    *,
    direction: int,
    stop_level: np.ndarray,
    target_level: np.ndarray,
    max_hold: int = DEFAULT_MAX_HOLD,
) -> pd.DataFrame:
    """Which comes first after a break: the opposite-boundary stop or the prior-swing target.

    Same-bar ambiguity (both stop and target touched within one bar) resolves to the stop —
    the adverse feasible sequence, per the execution-parity convention used across this
    codebase — rather than assuming the more favourable order.
    """
    high = ohlcv["high"].to_numpy()
    low = ohlcv["low"].to_numpy()
    n = high.size

    rows = []
    for t0 in break_bars:
        if t0 >= n:
            continue
        stop, target = stop_level[t0], target_level[t0]
        if not (np.isfinite(stop) and np.isfinite(target)):
            continue
        end = min(n, t0 + 1 + max_hold)
        outcome, exit_bar = "no_touch", end - 1
        for t in range(t0 + 1, end):
            hit_target = (high[t] >= target) if direction > 0 else (low[t] <= target)
            hit_stop = (low[t] <= stop) if direction > 0 else (high[t] >= stop)
            if hit_stop:
                outcome, exit_bar = "stop", t
                break
            if hit_target:
                outcome, exit_bar = "target", t
                break
        rows.append({"entry_bar": int(t0), "exit_bar": int(exit_bar), "outcome": outcome})
    return pd.DataFrame(rows, columns=["entry_bar", "exit_bar", "outcome"])


# --------------------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------------------


def run_structure_break_study(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    *,
    period: float,
    mtf_timeframe: str | None = None,
    horizons: tuple[int, ...] = (6, 24, 96),
    source: str = "binance",
    apply_coil_filter: bool = True,
) -> list[Effect]:
    """Full boundary-break scan: swing, channel, donchian benchmark and placebo, one family.

    Adds an mtf arm (boundaries built on ``mtf_timeframe``, causally aligned onto this
    timeframe's decision index via :func:`llm2.data.indicators.align_multi_timeframe`) when
    ``mtf_timeframe`` is given.
    """
    require_placebo_arm(BOUNDARY_LEVEL_CLAIM)
    require_matched_control(BREAK_EVENT_STUDY_SPEC)

    boundaries = build_boundaries(ohlcv, symbol, timeframe, source=source)
    atr = _atr(ohlcv).reindex(boundaries.index)
    metrics = build_causal_metrics(ohlcv["close"], ohlcv.get("volume"), period).reindex(boundaries.index)
    amp_rank = metrics["amp_pct_rank_500"]

    effects: list[Effect] = []
    arms: list[tuple[str, pd.DataFrame]] = [("single_tf", boundaries)]

    if mtf_timeframe is not None:
        from llm2.data.loader import load_ohlcv

        higher_ohlcv = load_ohlcv(symbol, mtf_timeframe, source=source)
        higher_boundaries = build_boundaries(higher_ohlcv, symbol, mtf_timeframe, source=source)
        aligned = align_multi_timeframe(higher_boundaries, boundaries.index, mtf_timeframe)
        arms.append((f"mtf_{mtf_timeframe}", aligned))

    for arm_name, arm_boundaries in arms:
        ohlcv_arm = ohlcv.reindex(arm_boundaries.index)
        for boundary_name, (up_col, lo_col) in BOUNDARY_PAIRS.items():
            if up_col not in arm_boundaries.columns or lo_col not in arm_boundaries.columns:
                continue
            confirmations = detect_breaks(
                ohlcv_arm, arm_boundaries[up_col], arm_boundaries[lo_col], atr=atr.reindex(arm_boundaries.index)
            )
            for conf_name, direction in CONFIRMATION_DIRECTIONS:
                ev = confirmations.get(conf_name)
                if ev is None:
                    continue
                bars = np.flatnonzero(ev.to_numpy())
                if bars.size < MIN_BREAK_EVENTS:
                    continue

                for eff in break_outcome(ohlcv_arm, bars, direction=direction, horizons=horizons):
                    eff.name = f"{arm_name}|{boundary_name}|{conf_name}|{eff.name}"
                    eff.detail.update({"arm": arm_name, "boundary": boundary_name, "confirmation": conf_name})
                    effects.append(eff)

                if apply_coil_filter:
                    coil_mask = coil_filter(amp_rank.reindex(arm_boundaries.index), bars)
                    coil_bars = bars[coil_mask]
                    if coil_bars.size >= MIN_BREAK_EVENTS:
                        for eff in break_outcome(ohlcv_arm, coil_bars, direction=direction, horizons=horizons):
                            eff.name = f"{arm_name}|{boundary_name}|{conf_name}|coil|{eff.name}"
                            eff.detail.update(
                                {"arm": arm_name, "boundary": boundary_name, "confirmation": conf_name, "coil_filtered": 1.0}
                            )
                            effects.append(eff)

    return apply_fdr(effects)
