"""Diagnostics for confirmed-swing market structure and Fibonacci geometry.

Four claims are tested, each of which is widely asserted and rarely measured:

1. The structure label predicts direction — a higher high means continuation up.
2. Fibonacci retracement levels are support and resistance.
3. Confirmed prior swing levels are support and resistance.
4. Impulse legs continue and corrective legs revert.

Claim 2 gets a placebo arm, and that arm is the point of this module. Testing "price near
the 0.618 line tends to bounce" in isolation cannot distinguish the Fibonacci ratio from the
mere fact of sitting inside a recent range near a round fraction of it. So each real ratio is
paired with arbitrary non-Fibonacci ratios drawn from the same anchors, on the same bars,
with the same proximity band. If 0.618 does not outperform 0.55, the ratio is decoration and
only the range is doing any work.

Everything here is conditional-mean measurement with overlap-aware standard errors and
false-discovery-rate control across the family. Nothing here selects a strategy.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.data.indicators import STRUCTURE_LABELS, load_bar_features, structure_frame
from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p
from llm2.diagnostics.structure import forward_log_return

MIN_BUCKET = 300

# Genuine Fibonacci retracements, and deliberately unremarkable ratios to test them against.
# The placebos avoid the Fibonacci values and the halfway point, and are spread across the
# same interval so that any "somewhere in the middle of the range" effect hits both arms.
FIB_RATIOS = (0.236, 0.382, 0.500, 0.618, 0.786)
PLACEBO_RATIOS = (0.150, 0.310, 0.440, 0.550, 0.690, 0.870)

# Proximity band in units of trailing volatility. A fixed percentage band would select
# quiet periods in a quiet regime and nothing at all in a violent one.
PROXIMITY_SIGMA = 0.5
VOL_WINDOW = 168


def _trailing_vol(close: pd.Series, window: int = VOL_WINDOW) -> pd.Series:
    c = pd.to_numeric(close, errors="coerce")
    return np.log(c.where(c > 0)).diff().rolling(window, min_periods=window // 4).std()


def _bucket_effect(name: str, fwd: np.ndarray, baseline: float, nw_lags: int, **detail) -> Effect | None:
    """Mean excess forward return for one conditioning bucket.

    ``nw_lags`` is the Newey-West lag count and is set to the forecast horizon, because
    overlapping forward returns are mechanically correlated out to exactly that many bars
    and an uncorrected standard error would overstate significance several-fold.
    """
    if fwd.size < MIN_BUCKET:
        return None
    excess = fwd - baseline
    mean_excess, t_stat = newey_west_tstat(excess, lags=nw_lags)
    return Effect(
        name=name,
        statistic=float(mean_excess),
        n=int(fwd.size),
        p_value=normal_two_sided_p(t_stat),
        detail={
            "t_hac": float(t_stat),
            "excess_bps": float(mean_excess * 1e4),
            "raw_mean_bps": float(np.nanmean(fwd) * 1e4),
            "uncond_mean_bps": float(baseline * 1e4),
            **detail,
        },
    )


def structure_label_effect(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    *,
    horizons: tuple[int, ...] = (6, 24, 96),
) -> list[Effect]:
    """Forward return conditioned on the prevailing higher-high / lower-low label.

    Tested against the unconditional mean rather than zero. Crypto's drift over this sample
    is large and positive, so "the mean after a higher high is positive" is true of almost
    any subset of bars and answers nothing.
    """
    frame = structure_frame(symbol, timeframe)
    raw = load_bar_features(symbol, timeframe)
    labels = raw["last_structure_label"].astype(str).reindex(frame.index)
    close = pd.to_numeric(ohlcv["close"], errors="coerce")

    effects: list[Effect] = []
    for h in horizons:
        fwd = forward_log_return(close, h).reindex(labels.index)
        baseline = float(np.nanmean(fwd.to_numpy()))
        for label in STRUCTURE_LABELS:
            sel = fwd[(labels == label)].dropna().to_numpy()
            eff = _bucket_effect(
                f"struct_label|{label}|fwd{h}", sel, baseline, h, horizon=float(h)
            )
            if eff is not None:
                effects.append(eff)

        # Impulse versus correction, the second half of the structural claim.
        for kind in ("impulse", "correction"):
            mask = raw["last_leg_kind"].astype(str).reindex(labels.index) == kind
            for direction, dmask in (
                ("up", raw["last_leg_dir"].astype(str).reindex(labels.index) == "up"),
                ("down", raw["last_leg_dir"].astype(str).reindex(labels.index) == "down"),
            ):
                sel = fwd[mask & dmask].dropna().to_numpy()
                eff = _bucket_effect(
                    f"leg|{kind}_{direction}|fwd{h}", sel, baseline, h, horizon=float(h)
                )
                if eff is not None:
                    effects.append(eff)
    return apply_fdr(effects)


def fibonacci_placebo_test(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    *,
    horizons: tuple[int, ...] = (6, 24),
    proximity_sigma: float = PROXIMITY_SIGMA,
) -> list[Effect]:
    """Do real Fibonacci ratios beat arbitrary ratios drawn from the same anchors?

    For each ratio the level is reconstructed from the confirmed swing anchors already in
    the warehouse, bars within ``proximity_sigma`` trailing standard deviations of it are
    selected, and the mean forward return of that bucket is measured. Real and placebo
    ratios go through identical code on identical bars.

    The comparison that matters is not whether an individual ratio is significant — with
    eleven ratios and several horizons something usually will be — but whether the real
    ratios as a group separate from the placebo group. That summary is attached to every
    effect as ``real_minus_placebo_bps``.
    """
    from llm2.research_policy import LevelClaim, require_placebo_arm

    require_placebo_arm(
        LevelClaim(
            name=f"fibonacci|{symbol}|{timeframe}",
            real_ratios=FIB_RATIOS,
            placebo_ratios=PLACEBO_RATIOS,
            anchors="confirmed swing high/low from indicators.sqlite",
            proximity_band=f"{proximity_sigma} trailing vol",
        )
    )

    raw = load_bar_features(symbol, timeframe)
    close = pd.to_numeric(ohlcv["close"], errors="coerce")
    close = close[~close.index.duplicated(keep="last")].reindex(raw.index)
    vol = _trailing_vol(close)

    anchor_lo = raw["fib_0000"]
    span = raw["fib_1000"] - raw["fib_0000"]

    effects: list[Effect] = []
    for h in horizons:
        fwd = forward_log_return(close, h)
        baseline = float(np.nanmean(fwd.to_numpy()))
        means: dict[str, list[float]] = {"fib": [], "placebo": []}

        for arm, ratios in (("fib", FIB_RATIOS), ("placebo", PLACEBO_RATIOS)):
            for r in ratios:
                level = anchor_lo + r * span
                # Distance in trailing-volatility units, so the band means the same thing
                # in a quiet market and a violent one.
                dist = (close - level).abs() / close.abs().replace(0, np.nan)
                near = dist <= (proximity_sigma * vol)
                sel = fwd[near.fillna(False)].dropna().to_numpy()
                eff = _bucket_effect(
                    f"{arm}_zone|{r:.3f}|fwd{h}",
                    sel,
                    baseline,
                    h,
                    horizon=float(h),
                    ratio=float(r),
                    is_placebo=float(arm == "placebo"),
                    coverage_frac=float(near.mean()),
                )
                if eff is not None:
                    effects.append(eff)
                    means[arm].append(eff.statistic)

        # The decisive summary: does the Fibonacci arm separate from the placebo arm?
        if means["fib"] and means["placebo"]:
            sep = (np.mean(np.abs(means["fib"])) - np.mean(np.abs(means["placebo"]))) * 1e4
            for eff in effects:
                if eff.detail.get("horizon") == float(h):
                    eff.detail["real_minus_placebo_bps"] = float(sep)
    return apply_fdr(effects)


def support_resistance_effect(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    *,
    horizons: tuple[int, ...] = (6, 24),
    proximity_sigma: float = PROXIMITY_SIGMA,
) -> list[Effect]:
    """Forward return when price sits close to a confirmed prior swing level.

    A level that genuinely acts as support should produce a positive mean forward return
    when approached from above, and a resistance level a negative one when approached from
    below. Both signs are reported so a bounce and a break are distinguishable.
    """
    frame = structure_frame(symbol, timeframe)
    close = pd.to_numeric(ohlcv["close"], errors="coerce")
    close = close[~close.index.duplicated(keep="last")].reindex(frame.index)
    vol = _trailing_vol(close)

    effects: list[Effect] = []
    for h in horizons:
        fwd = forward_log_return(close, h)
        baseline = float(np.nanmean(fwd.to_numpy()))
        for kind in ("support", "resistance"):
            col = f"dist_{kind}_pct"
            if col not in frame.columns:
                continue
            near = frame[col].abs() <= (proximity_sigma * vol)
            sel = fwd[near.fillna(False)].dropna().to_numpy()
            eff = _bucket_effect(
                f"near_{kind}|fwd{h}",
                sel,
                baseline,
                h,
                horizon=float(h),
                coverage_frac=float(near.mean()),
            )
            if eff is not None:
                effects.append(eff)

        # Room-to-run asymmetry: is the ratio of headroom to downside informative?
        if "sr_asymmetry" in frame.columns:
            asym = frame["sr_asymmetry"]
            for lo, hi, tag in ((0.0, 0.33, "resistance_close"), (0.67, 1.0, "support_close")):
                sel = fwd[(asym >= lo) & (asym <= hi)].dropna().to_numpy()
                eff = _bucket_effect(
                    f"sr_asym|{tag}|fwd{h}", sel, baseline, h, horizon=float(h)
                )
                if eff is not None:
                    effects.append(eff)
    return apply_fdr(effects)


def structure_confluence(
    ohlcv: pd.DataFrame,
    symbol: str,
    timeframe: str,
    peers: tuple[str, ...],
    *,
    horizon: int = 24,
    min_samples: int = MIN_BUCKET,
) -> list[Effect]:
    """Joint structural bias across assets, the literal form of the confluence question.

    Where the earlier confluence scan reduced each external series to a moving-average
    slope, this uses its confirmed swing structure: is the dollar index making lower highs
    while gold makes higher lows and bitcoin makes higher highs?

    The state is the Dow reading of the label — higher high or higher low is up, lower high
    or lower low is down — rather than the warehouse's ``structure_bias`` column. That
    column is near-constant (positive on 99.2% of XAUUSD 1h bars), so a table built on it
    puts almost every observation in one cell and cannot answer the question at all. The
    label split is within a point of even on every series checked.
    """
    from llm2.data.indicators import align_multi_timeframe

    close = pd.to_numeric(ohlcv["close"], errors="coerce")
    fwd = forward_log_return(close, horizon)
    idx = pd.DatetimeIndex(pd.to_datetime(ohlcv.index, utc=True))
    idx = idx[~idx.duplicated(keep="last")]

    # The traded symbol's own structure is part of the state, not excluded from it: the
    # question is "the dollar is making lower highs *while bitcoin makes higher highs*",
    # which is unanswerable if bitcoin's own leg is not one of the dimensions.
    members = tuple(dict.fromkeys((symbol, *peers)))

    cols: dict[str, pd.Series] = {}
    for peer in members:
        try:
            pf = structure_frame(peer, timeframe)
        except (ValueError, FileNotFoundError, KeyError):
            continue
        if "struct_dir" not in pf.columns:
            continue
        # Peers trade on their own calendars; foreign exchange and metals stop at the
        # weekend while crypto does not, so this is an as-of join on completion, never a
        # reindex that would silently carry a stale Friday reading as if it were fresh.
        aligned = align_multi_timeframe(pf[["struct_dir"]], idx, timeframe)
        cols[peer] = aligned["struct_dir"]
    if not cols:
        return []

    states = pd.DataFrame(cols, index=idx)
    fwd_u = fwd[~fwd.index.duplicated(keep="last")].reindex(idx)
    frame = states.copy()
    frame["fwd"] = fwd_u
    frame = frame.dropna()
    if frame.empty:
        return []

    usable = list(cols)
    bits = (frame[usable].to_numpy() > 0).astype(np.int64)
    weights = (1 << np.arange(len(usable), dtype=np.int64))[::-1]
    frame["state_id"] = bits @ weights
    baseline = float(np.nanmean(frame["fwd"].to_numpy()))

    effects: list[Effect] = []
    for state_id, grp in frame.groupby("state_id", observed=True):
        if len(grp) < min_samples:
            continue
        label = "|".join(f"{s}{'+' if grp[s].iloc[0] > 0 else '-'}" for s in usable)
        eff = _bucket_effect(
            f"struct_state[{label}]",
            grp["fwd"].to_numpy(),
            baseline,
            horizon,
            state_id=float(state_id),
            coverage_frac=float(len(grp) / len(frame)),
            states_possible=float(2 ** len(usable)),
        )
        if eff is not None:
            effects.append(eff)
    return apply_fdr(effects)
