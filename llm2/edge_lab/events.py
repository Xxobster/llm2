"""Edge-lab event catalogue: session x Smart Money Concepts x momentum.

One entry point builds every causal feature and every named entry event, so a
hunt, a leakage audit and a live runner all read the same code.

Event naming
------------
``<family>_<setup>_<direction>``. The side of every event is frozen in
``EVENT_SIDE``; a hunt may not flip it after seeing results.

Session filters are applied *on top* of a base event rather than baked into it,
so the same setup can be scored with and without a time-of-day restriction and
the difference is attributable.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.edge_lab.ict import ICT_EVENT_SIDE, fvg_frame, ict_events, structure_frame
from llm2.edge_lab.momentum import MOMENTUM_EVENT_SIDE, momentum_events, momentum_frame
from llm2.edge_lab.sessions import SWEEP_LEVELS, session_frame, sweep_event_side

# Session restrictions a hunt may apply to any base event.
SESSION_FILTERS: tuple[str, ...] = (
    "all",
    "no_weekend",
    "ny_am_kz",
    "ny_am_kz_no_weekend",
    "silver_bullet",
    "london_kz",
    "cash_open",
    "macro_release",
    "asia_kz",
    "weekday_ny",
)

# Sweep events that get their own catalogue entry (liquidity-run reversals).
SWEEP_EVENT_LEVELS: tuple[str, ...] = SWEEP_LEVELS

CONFLUENCE_EVENTS: tuple[str, ...] = (
    "sweep_pdh_fvg_bear_short",
    "sweep_pdl_fvg_bull_long",
    "sweep_asia_high_bear_struct_short",
    "sweep_asia_low_bull_struct_long",
    "sweep_pdh_choch_down_short",
    "sweep_pdl_choch_up_long",
    "fvg_bull_ob_bull_long",
    "fvg_bear_ob_bear_short",
    "momo_breakout_fvg_bull_long",
    "momo_breakout_fvg_bear_short",
    "ignition_fvg_bull_long",
    "ignition_fvg_bear_short",
)

CONFLUENCE_SIDE: dict[str, int] = {
    "sweep_pdh_fvg_bear_short": -1,
    "sweep_pdl_fvg_bull_long": 1,
    "sweep_asia_high_bear_struct_short": -1,
    "sweep_asia_low_bull_struct_long": 1,
    "sweep_pdh_choch_down_short": -1,
    "sweep_pdl_choch_up_long": 1,
    "fvg_bull_ob_bull_long": 1,
    "fvg_bear_ob_bear_short": -1,
    "momo_breakout_fvg_bull_long": 1,
    "momo_breakout_fvg_bear_short": -1,
    "ignition_fvg_bull_long": 1,
    "ignition_fvg_bear_short": -1,
}

EVENT_SIDE: dict[str, int] = {
    **{f"sweep_{lvl}": sweep_event_side(lvl) for lvl in SWEEP_EVENT_LEVELS},
    **ICT_EVENT_SIDE,
    **MOMENTUM_EVENT_SIDE,
    **CONFLUENCE_SIDE,
}
EVENT_IDS: tuple[str, ...] = tuple(EVENT_SIDE)

# Scale-free feature columns exposed to models and to the leakage audit.
# Raw price levels are deliberately excluded (only ATR-normalised distances).
FEATURE_PREFIXES: tuple[str, ...] = (
    "atr_frac",
    "dist_",
    "in_",
    "at_",
    "touch_",
    "sweep_",
    "pierce_",
    "range_pos",
    "prev_day_range_pos",
    "prev_day_range_atr",
    "dealing_range_atr",
    "bos_",
    "choch_",
    "bullish_structure",
    "bearish_structure",
    "fvg_bull_new",
    "fvg_bear_new",
    "fvg_bull_age",
    "fvg_bear_age",
    "fvg_bull_size_atr",
    "fvg_bear_size_atr",
    "fvg_bull_active",
    "fvg_bear_active",
    "ifvg_bull_active",
    "ifvg_bear_active",
    "adr_pct_20",
    "atr_compression",
    "prior_move_",
    "tightness_",
    "breakout_",
    "ma_stack_",
    "ma_convergence_atr",
    "vol_expansion",
    "vol_z_20",
    "close_pos_in_bar",
    "body_frac_of_range",
    "bar_range_atr",
    "hour_utc",
    "dow",
    "is_weekend",
    "is_monday",
    "is_friday",
    "hours_since_ny_open",
)
# Never expose an unnormalised price level as a feature.
FEATURE_EXCLUDE_PREFIXES: tuple[str, ...] = (
    "lvl_",
    "box_high_",
    "box_low_",
    "ema",
    "fvg_bull_top",
    "fvg_bull_bottom",
    "fvg_bull_ce",
    "fvg_bear_top",
    "fvg_bear_bottom",
    "fvg_bear_ce",
    "ifvg_bull_top",
    "ifvg_bull_bottom",
    "ifvg_bear_top",
    "ifvg_bear_bottom",
    "ob_bull_top",
    "ob_bull_bottom",
    "ob_bear_top",
    "ob_bear_bottom",
    "swing_high",
    "swing_low",
    "atr",
)


class EdgePack:
    """Causal features, event occurrence bits and the session frame."""

    __slots__ = ("features", "occurrence", "session", "raw")

    def __init__(
        self,
        features: pd.DataFrame,
        occurrence: pd.DataFrame,
        session: pd.DataFrame,
        raw: pd.DataFrame,
    ) -> None:
        self.features = features
        self.occurrence = occurrence
        self.session = session
        self.raw = raw


def _select_features(raw: pd.DataFrame) -> pd.DataFrame:
    keep: list[str] = []
    for col in raw.columns:
        if any(col.startswith(p) for p in FEATURE_EXCLUDE_PREFIXES):
            if col != "atr_frac":
                continue
        if any(col == p or col.startswith(p) for p in FEATURE_PREFIXES):
            keep.append(col)
    # Deterministic order so leakage reports and model packs are comparable.
    return raw.reindex(columns=sorted(set(keep)))


def build_edge_pack(
    ohlcv: pd.DataFrame,
    *,
    min_gap_atr: float = 0.10,
    fvg_fill_mode: str = "wick",
    swing_left: int = 2,
    swing_right: int = 2,
) -> EdgePack:
    """Build every causal feature and every event bit from the handed candles."""
    sess = session_frame(ohlcv)
    fvg = fvg_frame(ohlcv, min_gap_atr=min_gap_atr, fill_mode=fvg_fill_mode)
    struct = structure_frame(ohlcv, left=swing_left, right=swing_right)
    mom = momentum_frame(ohlcv)

    raw = pd.concat(
        [
            sess,
            fvg,
            struct.drop(columns=[c for c in ("atr", "atr_frac") if c in struct.columns]),
            mom.drop(columns=[c for c in ("atr", "atr_frac") if c in mom.columns]),
        ],
        axis=1,
    )
    raw = raw.loc[:, ~raw.columns.duplicated()]

    occ = pd.DataFrame(index=ohlcv.index)
    for lvl in SWEEP_EVENT_LEVELS:
        occ[f"sweep_{lvl}"] = (sess[f"sweep_{lvl}"].to_numpy(dtype=float) > 0.5).astype(np.int8)
    for col, bits in ict_events(fvg, struct).items():
        occ[col] = bits.to_numpy(dtype=np.int8)
    for col, bits in momentum_events(mom).items():
        occ[col] = bits.to_numpy(dtype=np.int8)

    def _b(frame: pd.DataFrame, col: str) -> np.ndarray:
        return frame[col].to_numpy(dtype=float) > 0.5

    sweep_pdh = _b(sess, "sweep_prev_day_high")
    sweep_pdl = _b(sess, "sweep_prev_day_low")
    sweep_ah = _b(sess, "sweep_asia_high")
    sweep_al = _b(sess, "sweep_asia_low")
    fvg_bear_active = _b(fvg, "fvg_bear_active")
    fvg_bull_active = _b(fvg, "fvg_bull_active")
    bear_struct = _b(struct, "bearish_structure")
    bull_struct = _b(struct, "bullish_structure")
    choch_dn = _b(struct, "choch_down")
    choch_up = _b(struct, "choch_up")
    ob_bull = _b(struct, "in_ob_bull")
    ob_bear = _b(struct, "in_ob_bear")
    touch_bull = _b(fvg, "touch_fvg_bull")
    touch_bear = _b(fvg, "touch_fvg_bear")
    momo_long = occ["momo_breakout_long"].to_numpy() > 0
    momo_short = occ["momo_breakout_short"].to_numpy() > 0
    ign_long = occ["ignition_long"].to_numpy() > 0
    ign_short = occ["ignition_short"].to_numpy() > 0

    occ["sweep_pdh_fvg_bear_short"] = (sweep_pdh & fvg_bear_active).astype(np.int8)
    occ["sweep_pdl_fvg_bull_long"] = (sweep_pdl & fvg_bull_active).astype(np.int8)
    occ["sweep_asia_high_bear_struct_short"] = (sweep_ah & bear_struct).astype(np.int8)
    occ["sweep_asia_low_bull_struct_long"] = (sweep_al & bull_struct).astype(np.int8)
    occ["sweep_pdh_choch_down_short"] = (sweep_pdh & choch_dn).astype(np.int8)
    occ["sweep_pdl_choch_up_long"] = (sweep_pdl & choch_up).astype(np.int8)
    occ["fvg_bull_ob_bull_long"] = (touch_bull & ob_bull).astype(np.int8)
    occ["fvg_bear_ob_bear_short"] = (touch_bear & ob_bear).astype(np.int8)
    occ["momo_breakout_fvg_bull_long"] = (momo_long & fvg_bull_active).astype(np.int8)
    occ["momo_breakout_fvg_bear_short"] = (momo_short & fvg_bear_active).astype(np.int8)
    occ["ignition_fvg_bull_long"] = (ign_long & fvg_bull_active).astype(np.int8)
    occ["ignition_fvg_bear_short"] = (ign_short & fvg_bear_active).astype(np.int8)

    missing = [e for e in EVENT_IDS if e not in occ.columns]
    if missing:
        raise RuntimeError(f"event catalogue incomplete: {missing}")
    return EdgePack(_select_features(raw), occ.reindex(columns=list(EVENT_IDS)), sess, raw)


def session_mask(session: pd.DataFrame, filter_name: str) -> np.ndarray:
    """Boolean bar mask for a named session restriction."""
    n = len(session)
    weekend = session["is_weekend_window"].to_numpy(dtype=float) > 0.5
    if filter_name == "all":
        return np.ones(n, dtype=bool)
    if filter_name == "no_weekend":
        return ~weekend
    if filter_name == "weekday_ny":
        return (session["in_ny"].to_numpy(dtype=float) > 0.5) & ~weekend
    if filter_name == "ny_am_kz_no_weekend":
        return (session["in_ny_am_kz"].to_numpy(dtype=float) > 0.5) & ~weekend
    col = f"in_{filter_name}"
    if col not in session.columns:
        raise ValueError(f"unknown session filter {filter_name!r}")
    return session[col].to_numpy(dtype=float) > 0.5


def build_features_for_guard(ohlcv: pd.DataFrame, **_kwargs) -> pd.DataFrame:
    """Leakage-audit entry point: causal features only, no labels, no events."""
    return build_edge_pack(ohlcv).features
