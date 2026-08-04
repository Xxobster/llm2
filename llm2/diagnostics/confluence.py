"""Confluence: does a joint configuration of external trends predict the crypto move?

This is the formal version of "EMA200 on EURUSD is down and DXY is down while BTC is up".
Each external series is reduced to a causal trend sign, the signs form a joint state, and
the forward return is averaged within each state.

The combinatorics are the whole difficulty. Ten binary signs give 1024 states; on seven
years of hourly data most of them hold too few observations to estimate anything, and the
handful that happen to look extreme are the ones a naive reading would seize on. Three
defences are applied: a hard minimum-sample floor, overlap-aware standard errors, and
false-discovery-rate correction across the whole table. A marginal-contribution column
shows whether a state earns its result from the external series at all or merely from the
crypto trend embedded in it.
"""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd

from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p

MIN_STATE_SAMPLES = 500


def trend_sign(level: pd.Series, span: int, *, slope_bars: int = 1) -> pd.Series:
    """Causal trend direction: is the exponential moving average rising or falling?

    The sign is taken from the moving average's own slope rather than price-versus-average,
    because "EMA200 is down" in the user's sense means the average is declining, not that
    price sits beneath it. Both are available; this one is the literal reading.
    """
    ema = level.ewm(span=span, adjust=False, min_periods=span).mean()
    return np.sign(ema.diff(slope_bars))


def price_vs_trend_sign(level: pd.Series, span: int) -> pd.Series:
    """Alternative reading: is the level above or below its own moving average?"""
    ema = level.ewm(span=span, adjust=False, min_periods=span).mean()
    return np.sign(level - ema)


def build_state_frame(
    panel: pd.DataFrame,
    symbols: list[str],
    *,
    span: int = 200,
    mode: str = "slope",
) -> pd.DataFrame:
    """Per-series trend signs on the decision index, as +1 / -1 columns."""
    fn = trend_sign if mode == "slope" else price_vs_trend_sign
    out = {}
    for sym in symbols:
        if sym not in panel.columns:
            continue
        sign = fn(panel[sym], span)
        # A flat average is uninformative and would create a third state that dilutes the
        # table; fold it into the previous direction rather than inventing a category.
        out[sym] = sign.replace(0, np.nan).ffill()
    return pd.DataFrame(out, index=panel.index)


def _state_label(row: pd.Series, symbols: list[str]) -> str:
    return "|".join(f"{s}{'+' if row[s] > 0 else '-'}" for s in symbols)


def confluence_table(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    symbols: list[str],
    *,
    horizon: int = 24,
    span: int = 200,
    mode: str = "slope",
    min_samples: int = MIN_STATE_SAMPLES,
) -> list[Effect]:
    """Mean forward return for every sufficiently populated joint trend state."""
    from llm2.diagnostics.structure import forward_log_return

    states = build_state_frame(panel, symbols, span=span, mode=mode)
    usable = [s for s in symbols if s in states.columns]
    if not usable:
        return []

    fwd = forward_log_return(ohlcv["close"], horizon)
    frame = states[usable].copy()
    frame["fwd"] = fwd
    frame = frame.dropna()
    if frame.empty:
        return []

    # Vectorized state key: pack the signs into an integer, then label only the survivors.
    bits = (frame[usable].to_numpy() > 0).astype(np.int64)
    weights = (1 << np.arange(len(usable), dtype=np.int64))[::-1]
    frame["state_id"] = bits @ weights

    effects: list[Effect] = []
    baseline_mean = float(np.nanmean(frame["fwd"].to_numpy()))

    # Test each state against the unconditional mean, not against zero. Crypto carries a
    # large positive drift over this sample, so "is this bucket's mean non-zero" is
    # significant for almost every bucket and answers the wrong question. The question is
    # whether the state differs from simply being in the market.
    frame["excess"] = frame["fwd"] - baseline_mean

    for state_id, grp in frame.groupby("state_id", observed=True):
        if len(grp) < min_samples:
            continue
        excess = grp["excess"].to_numpy()
        mean_excess, t_stat = newey_west_tstat(excess, lags=horizon)
        mean_raw = float(np.nanmean(grp["fwd"].to_numpy()))
        label = _state_label(grp[usable].iloc[0], usable)
        effects.append(
            Effect(
                name=f"state[{label}]",
                statistic=float(mean_excess),
                n=int(len(grp)),
                p_value=normal_two_sided_p(t_stat),
                detail={
                    "t_hac": float(t_stat),
                    "excess_bps": float(mean_excess * 1e4),
                    "raw_mean_bps": float(mean_raw * 1e4),
                    "uncond_mean_bps": float(baseline_mean * 1e4),
                    "state_id": float(state_id),
                    "coverage_frac": float(len(grp) / len(frame)),
                },
            )
        )

    n_possible = 2 ** len(usable)
    for eff in effects:
        eff.detail["states_possible"] = float(n_possible)
        eff.detail["states_evaluated"] = float(len(effects))
    return apply_fdr(effects)


def marginal_contribution(
    ohlcv: pd.DataFrame,
    panel: pd.DataFrame,
    symbols: list[str],
    *,
    horizon: int = 24,
    span: int = 200,
    mode: str = "slope",
) -> list[Effect]:
    """Per-series up-minus-down spread, to show which series carry the joint result.

    If every joint state that looks good contains the same one series in the same direction,
    the confluence is that series and the rest is decoration.

    The statistic is the *difference* between the two states rather than each state's mean.
    Testing a single state against zero would mostly measure crypto's unconditional drift,
    which is present in every subset of bars and would make almost every series look
    informative.
    """
    from llm2.diagnostics.structure import forward_log_return

    states = build_state_frame(panel, symbols, span=span, mode=mode)
    fwd = forward_log_return(ohlcv["close"], horizon)
    effects: list[Effect] = []

    for sym in symbols:
        if sym not in states.columns:
            continue
        frame = pd.DataFrame({"sign": states[sym], "fwd": fwd}).dropna()
        up = frame.loc[frame["sign"] > 0, "fwd"].to_numpy()
        down = frame.loc[frame["sign"] < 0, "fwd"].to_numpy()
        if up.size < MIN_STATE_SAMPLES or down.size < MIN_STATE_SAMPLES:
            continue

        # Two-sample difference with overlap-aware standard errors on each arm.
        mean_up, t_up = newey_west_tstat(up, lags=horizon)
        mean_down, t_down = newey_west_tstat(down, lags=horizon)
        se_up = abs(mean_up / t_up) if t_up not in (0.0,) and np.isfinite(t_up) else np.nan
        se_down = abs(mean_down / t_down) if t_down not in (0.0,) and np.isfinite(t_down) else np.nan
        diff = mean_up - mean_down
        se_diff = float(np.sqrt(se_up**2 + se_down**2)) if np.isfinite(se_up) and np.isfinite(se_down) else np.nan
        t_diff = diff / se_diff if np.isfinite(se_diff) and se_diff > 0 else float("nan")

        effects.append(
            Effect(
                name=f"marginal[{sym}_up_minus_down]",
                statistic=float(diff),
                n=int(up.size + down.size),
                p_value=normal_two_sided_p(t_diff),
                detail={
                    "t_hac": float(t_diff),
                    "spread_bps": float(diff * 1e4),
                    "up_mean_bps": float(mean_up * 1e4),
                    "down_mean_bps": float(mean_down * 1e4),
                    "n_up": float(up.size),
                    "n_down": float(down.size),
                },
            )
        )
    return apply_fdr(effects)


def state_space_report(symbols: list[str], n_rows: int, *, min_samples: int = MIN_STATE_SAMPLES) -> dict:
    """How much of the joint state space this much data can even support.

    Included in every report so a table with three populated states out of 1024 is read as
    "the data cannot answer this", not as "only three configurations matter".
    """
    n_states = 2 ** len(symbols)
    return {
        "n_symbols": len(symbols),
        "states_possible": n_states,
        "rows": n_rows,
        "rows_per_state_if_uniform": n_rows / n_states if n_states else float("nan"),
        "max_states_supportable": int(n_rows // min_samples) if min_samples else 0,
        "min_samples_per_state": min_samples,
    }


def suggest_symbol_subsets(symbols: list[str], n_rows: int, *, max_size: int = 4) -> list[tuple[str, ...]]:
    """Subsets small enough that each state can be estimated on this much data.

    Preferring several small joint tables over one enormous one is not a stylistic choice:
    a 10-series table cannot be estimated at all, so scanning it produces only noise.
    """
    out: list[tuple[str, ...]] = []
    for size in range(2, max_size + 1):
        if n_rows / (2**size) < MIN_STATE_SAMPLES:
            break
        out.extend(itertools.combinations(symbols, size))
    return out
