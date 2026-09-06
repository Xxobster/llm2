"""Causal known-now features + future-event labels for diagonal S/R hunt.

Labels may look ahead inside this module only. Features must be prefix-invariant.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from llm2.confluence.events import any_in_next
from llm2.diagonal_sr.geometry import TOUCH_ATR_MULT, build_geometry_frame
from llm2.diagonal_sr.mtf import attach_mtf_geometry

EVENT_IDS_A: tuple[str, ...] = (
    "bounce_upper",
    "bounce_lower",
    "break_upper",
    "break_lower",
    "retest_after_break_up",
    "retest_after_break_down",
    "channel_walk_long",
    "channel_walk_short",
)

EVENT_IDS_B: tuple[str, ...] = (
    "confluence_bounce_long",
    "confluence_bounce_short",
    "confluence_break_up",
    "confluence_break_down",
)

LONG_EVENTS = frozenset(
    {
        "bounce_lower",
        "break_upper",
        "retest_after_break_up",
        "channel_walk_long",
        "confluence_bounce_long",
        "confluence_break_up",
    }
)
SHORT_EVENTS = frozenset(
    {
        "bounce_upper",
        "break_lower",
        "retest_after_break_down",
        "channel_walk_short",
        "confluence_bounce_short",
        "confluence_break_down",
    }
)
MARKET_ENTRY_EVENTS = frozenset(
    {
        "break_upper",
        "break_lower",
        "confluence_break_up",
        "confluence_break_down",
    }
)

# Feature columns used for training (scale-free / slope / state only — no raw USD).
FEATURE_COLS_A: tuple[str, ...] = (
    "atr_frac",
    "dist_last2_upper_atr",
    "dist_last2_lower_atr",
    "dist_ols3_upper_atr",
    "dist_ols3_lower_atr",
    "dist_channel_upper_atr",
    "dist_channel_lower_atr",
    "dist_valid3_upper_atr",
    "dist_valid3_lower_atr",
    "last2_upper_slope",
    "last2_lower_slope",
    "ols3_upper_slope",
    "ols3_lower_slope",
    "channel_upper_slope",
    "channel_lower_slope",
    "valid3_upper_touches",
    "valid3_lower_touches",
    "near_upper",
    "near_lower",
    "broke_upper",
    "broke_lower",
    "wick_reject_upper",
    "wick_reject_lower",
    "inside_channel",
    "vol_z_48",
    "ret4",
    "close_pos_in_range20",
)

FEATURE_COLS_B: tuple[str, ...] = FEATURE_COLS_A + (
    "dist_horiz_resist_atr",
    "dist_horiz_support_atr",
    "confluence_upper",
    "confluence_lower",
    "dist_placebo_upper_atr",
    "dist_placebo_lower_atr",
    "dist_donchian20_upper_atr",
    "dist_donchian20_lower_atr",
)


@dataclass(frozen=True)
class EventPack:
    horizon: int
    generation: str
    features: pd.DataFrame
    labels: pd.DataFrame
    side: pd.DataFrame
    occurrence: pd.DataFrame


def _vol_z(volume: np.ndarray, window: int = 48) -> np.ndarray:
    s = pd.Series(volume)
    mu = s.rolling(window, min_periods=window).mean()
    sd = s.rolling(window, min_periods=window).std()
    return ((s - mu) / sd.replace(0, np.nan)).to_numpy(dtype=float)


def _range_pos(high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 20) -> np.ndarray:
    hh = pd.Series(high).rolling(n, min_periods=n).max().to_numpy()
    ll = pd.Series(low).rolling(n, min_periods=n).min().to_numpy()
    den = hh - ll
    return (close - ll) / np.where(np.abs(den) > 1e-15, den, np.nan)


def _ensure_dist_cols(geom: pd.DataFrame, close: pd.Series, atr: pd.Series) -> pd.DataFrame:
    out = geom.copy()
    for name in (
        "last2_upper",
        "last2_lower",
        "ols3_upper",
        "ols3_lower",
        "channel_upper",
        "channel_lower",
        "valid3_upper",
        "valid3_lower",
        "horiz_resist",
        "horiz_support",
        "donchian20_upper",
        "donchian20_lower",
        "placebo_upper",
        "placebo_lower",
    ):
        col = f"dist_{name}_atr"
        if col not in out.columns and name in out.columns:
            out[col] = (close - out[name]) / atr.replace(0, np.nan)
    return out


def build_known_now_features(
    ohlcv: pd.DataFrame,
    *,
    generation: str = "A",
    htf_ohlcv_by_tf: dict[str, pd.DataFrame] | None = None,
    decision_tf: str = "15m",
) -> pd.DataFrame:
    """Scale-free known-now features. Generation B adds horizontal confluence."""
    if htf_ohlcv_by_tf:
        geom = attach_mtf_geometry(ohlcv, htf_ohlcv_by_tf, decision_tf=decision_tf)
    else:
        geom = build_geometry_frame(ohlcv)
        close = ohlcv["close"]
        atr = geom["atr"]
        geom = _ensure_dist_cols(geom, close, atr)

    high = ohlcv["high"].to_numpy(dtype=float)
    low = ohlcv["low"].to_numpy(dtype=float)
    close_a = ohlcv["close"].to_numpy(dtype=float)
    atr = geom["atr"].to_numpy(dtype=float)
    band = TOUCH_ATR_MULT * atr

    upper = geom["last2_upper"].to_numpy(dtype=float)
    lower = geom["last2_lower"].to_numpy(dtype=float)
    ch_u = geom["channel_upper"].to_numpy(dtype=float)
    ch_l = geom["channel_lower"].to_numpy(dtype=float)

    near_upper = (high >= upper - band) & (high <= upper + band) & np.isfinite(upper)
    near_lower = (low <= lower + band) & (low >= lower - band) & np.isfinite(lower)
    broke_upper = (close_a > upper) & np.isfinite(upper)
    broke_lower = (close_a < lower) & np.isfinite(lower)
    # Wick through then close back (reject).
    wick_reject_upper = (high > upper) & (close_a < upper) & np.isfinite(upper)
    wick_reject_lower = (low < lower) & (close_a > lower) & np.isfinite(lower)
    inside_channel = (
        np.isfinite(ch_u)
        & np.isfinite(ch_l)
        & (close_a <= ch_u)
        & (close_a >= ch_l)
    )

    feat = pd.DataFrame(index=ohlcv.index)
    feat["atr_frac"] = geom["atr_frac"]
    for col in (
        "dist_last2_upper_atr",
        "dist_last2_lower_atr",
        "dist_ols3_upper_atr",
        "dist_ols3_lower_atr",
        "dist_channel_upper_atr",
        "dist_channel_lower_atr",
        "dist_valid3_upper_atr",
        "dist_valid3_lower_atr",
        "last2_upper_slope",
        "last2_lower_slope",
        "ols3_upper_slope",
        "ols3_lower_slope",
        "channel_upper_slope",
        "channel_lower_slope",
        "valid3_upper_touches",
        "valid3_lower_touches",
    ):
        feat[col] = geom[col] if col in geom.columns else np.nan

    feat["near_upper"] = near_upper.astype(float)
    feat["near_lower"] = near_lower.astype(float)
    feat["broke_upper"] = broke_upper.astype(float)
    feat["broke_lower"] = broke_lower.astype(float)
    feat["wick_reject_upper"] = wick_reject_upper.astype(float)
    feat["wick_reject_lower"] = wick_reject_lower.astype(float)
    feat["inside_channel"] = inside_channel.astype(float)
    feat["vol_z_48"] = _vol_z(ohlcv["volume"].to_numpy(dtype=float))
    ret = np.empty_like(close_a)
    ret[:4] = np.nan
    ret[4:] = close_a[4:] / close_a[:-4] - 1.0
    feat["ret4"] = ret
    feat["close_pos_in_range20"] = _range_pos(high, low, close_a)

    # Carry raw geometry bits needed for labels (not used as model features).
    feat["_upper"] = upper
    feat["_lower"] = lower
    feat["_ch_u"] = ch_u
    feat["_ch_l"] = ch_l
    feat["_atr"] = atr
    feat["_close"] = close_a
    feat["_high"] = high
    feat["_low"] = low

    if generation.upper() == "B":
        for col in (
            "dist_horiz_resist_atr",
            "dist_horiz_support_atr",
            "dist_placebo_upper_atr",
            "dist_placebo_lower_atr",
            "dist_donchian20_upper_atr",
            "dist_donchian20_lower_atr",
        ):
            feat[col] = geom[col] if col in geom.columns else np.nan
        # Confluence: diagonal within k*ATR of horizontal.
        du = geom["dist_last2_upper_atr"].to_numpy(dtype=float) if "dist_last2_upper_atr" in geom else np.full(len(feat), np.nan)
        hu = geom["dist_horiz_resist_atr"].to_numpy(dtype=float) if "dist_horiz_resist_atr" in geom else np.full(len(feat), np.nan)
        dl = geom["dist_last2_lower_atr"].to_numpy(dtype=float) if "dist_last2_lower_atr" in geom else np.full(len(feat), np.nan)
        hl = geom["dist_horiz_support_atr"].to_numpy(dtype=float) if "dist_horiz_support_atr" in geom else np.full(len(feat), np.nan)
        feat["confluence_upper"] = (
            np.isfinite(du) & np.isfinite(hu) & (np.abs(du - hu) <= 0.5)
        ).astype(float)
        feat["confluence_lower"] = (
            np.isfinite(dl) & np.isfinite(hl) & (np.abs(dl - hl) <= 0.5)
        ).astype(float)

    # Append any HTF columns already present in geom (prefixed).
    for col in geom.columns:
        if col.startswith("htf_") and col not in feat.columns:
            # Only keep scale-free / slope / dist columns.
            if any(x in col for x in ("_slope", "dist_", "touches", "atr_frac")):
                feat[col] = geom[col]

    return feat


def occurrence_bits(feat: pd.DataFrame, *, generation: str) -> pd.DataFrame:
    """Causal occurrence bits on this bar (used to build future-event labels)."""
    close = feat["_close"].to_numpy(dtype=float)
    high = feat["_high"].to_numpy(dtype=float)
    low = feat["_low"].to_numpy(dtype=float)
    upper = feat["_upper"].to_numpy(dtype=float)
    lower = feat["_lower"].to_numpy(dtype=float)
    atr = feat["_atr"].to_numpy(dtype=float)
    band = TOUCH_ATR_MULT * atr
    ch_u = feat["_ch_u"].to_numpy(dtype=float)
    ch_l = feat["_ch_l"].to_numpy(dtype=float)

    near_u = (high >= upper - band) & (high <= upper + band) & np.isfinite(upper)
    near_l = (low <= lower + band) & (low >= lower - band) & np.isfinite(lower)
    reject_u = (high > upper) & (close < upper) & np.isfinite(upper)
    reject_l = (low < lower) & (close > lower) & np.isfinite(lower)
    break_u = (close > upper) & np.isfinite(upper)
    break_l = (close < lower) & np.isfinite(lower)
    inside = np.isfinite(ch_u) & np.isfinite(ch_l) & (close <= ch_u) & (close >= ch_l)

    # Break state latch without a Python bar loop: +1 on break_up, -1 on break_down.
    # State is the sign of the cumulative last non-zero event (causal forward-fill).
    event = np.zeros(len(feat), dtype=np.int8)
    event[break_u] = 1
    event[break_l] = -1
    # Prefer simultaneous lower break if both fire (rare).
    both = break_u & break_l
    event[both] = -1
    filled = pd.Series(event).replace(0, np.nan).ffill().fillna(0).to_numpy(dtype=np.int8)
    broke_up_state = filled > 0
    broke_dn_state = filled < 0

    # Retest: after a break, price returns into band from the other side.
    prev_bu = np.roll(broke_up_state, 1)
    prev_bu[0] = False
    prev_bd = np.roll(broke_dn_state, 1)
    prev_bd[0] = False
    retest_up = prev_bu & near_u & (close > upper - band) & ~break_u
    retest_dn = prev_bd & near_l & (close < lower + band) & ~break_l

    bounce_u = near_u & reject_u & ~break_u
    bounce_l = near_l & reject_l & ~break_l
    walk_long = inside & near_l & (close > low)
    walk_short = inside & near_u & (close < high)

    occ = pd.DataFrame(index=feat.index)
    occ["bounce_upper"] = bounce_u.astype(np.int8)
    occ["bounce_lower"] = bounce_l.astype(np.int8)
    occ["break_upper"] = break_u.astype(np.int8)
    occ["break_lower"] = break_l.astype(np.int8)
    occ["retest_after_break_up"] = retest_up.astype(np.int8)
    occ["retest_after_break_down"] = retest_dn.astype(np.int8)
    occ["channel_walk_long"] = walk_long.astype(np.int8)
    occ["channel_walk_short"] = walk_short.astype(np.int8)

    if generation.upper() == "B":
        conf_u = feat["confluence_upper"].to_numpy(dtype=float) > 0.5
        conf_l = feat["confluence_lower"].to_numpy(dtype=float) > 0.5
        occ["confluence_bounce_long"] = (conf_l & bounce_l).astype(np.int8)
        occ["confluence_bounce_short"] = (conf_u & bounce_u).astype(np.int8)
        occ["confluence_break_up"] = (conf_u & break_u).astype(np.int8)
        occ["confluence_break_down"] = (conf_l & break_l).astype(np.int8)

    return occ


def build_event_pack(
    ohlcv: pd.DataFrame,
    *,
    horizon: int,
    generation: str = "A",
    htf_ohlcv_by_tf: dict[str, pd.DataFrame] | None = None,
    decision_tf: str = "15m",
) -> EventPack:
    gen = generation.upper()
    feat_raw = build_known_now_features(
        ohlcv, generation=gen, htf_ohlcv_by_tf=htf_ohlcv_by_tf, decision_tf=decision_tf
    )
    occ = occurrence_bits(feat_raw, generation=gen)
    event_ids = EVENT_IDS_A if gen == "A" else EVENT_IDS_A + EVENT_IDS_B

    labels = pd.DataFrame(index=ohlcv.index)
    side = pd.DataFrame(index=ohlcv.index)
    for eid in event_ids:
        bit = occ[eid].to_numpy(dtype=np.int8) if eid in occ.columns else np.zeros(len(ohlcv), dtype=np.int8)
        fut = any_in_next(bit, horizon).astype(float)
        fut[-horizon:] = np.nan
        labels[eid] = fut
        if eid in LONG_EVENTS:
            side[eid] = np.where(np.isfinite(fut), 1.0, np.nan)
        elif eid in SHORT_EVENTS:
            side[eid] = np.where(np.isfinite(fut), -1.0, np.nan)
        else:
            side[eid] = 0.0

    feature_cols = list(FEATURE_COLS_A if gen == "A" else FEATURE_COLS_B)
    # Include available HTF columns deterministically (sorted) for leakage stability.
    htf_cols = sorted(c for c in feat_raw.columns if c.startswith("htf_"))
    for c in htf_cols:
        if c not in feature_cols:
            feature_cols.append(c)
    features = feat_raw.reindex(columns=feature_cols)

    return EventPack(
        horizon=int(horizon),
        generation=gen,
        features=features,
        labels=labels,
        side=side,
        occurrence=occ,
    )


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    """Leakage-audit entry: generation A known-now features only (no labels)."""
    feat = build_known_now_features(ohlcv, generation="A")
    cols = [c for c in FEATURE_COLS_A if c in feat.columns]
    return feat[cols].copy()


def feature_cols_for(generation: str) -> tuple[str, ...]:
    return FEATURE_COLS_A if generation.upper() == "A" else FEATURE_COLS_B
