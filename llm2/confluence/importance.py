"""Oracle importance helpers: correlation prune, FDR, promote rule."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from llm2.confluence.events import EVENT_IDS, signed_forward_log_return
from llm2.diagnostics.stats import Effect, apply_fdr, newey_west_tstat, normal_two_sided_p

EBR_CAP = 0.35
PF_FLOOR_VS_CTRL = 0.85
DUP_ABS_CORR = 0.8


def event_correlation(labels: pd.DataFrame) -> pd.DataFrame:
    """Pearson correlation of oracle event bits (pairwise complete)."""
    cols = [c for c in EVENT_IDS if c in labels.columns]
    x = labels[cols].astype(float)
    return x.corr(method="pearson")


def prune_duplicates(
    corr: pd.DataFrame,
    intent_exp: dict[str, float],
    *,
    abs_thr: float = DUP_ABS_CORR,
) -> dict[str, Any]:
    """Drop the weaker of each pair with |rho| > threshold."""
    dropped: list[dict[str, Any]] = []
    keep = set(corr.columns)
    cols = list(corr.columns)
    for i, a in enumerate(cols):
        if a not in keep:
            continue
        for b in cols[i + 1 :]:
            if b not in keep:
                continue
            rho = corr.loc[a, b]
            if not np.isfinite(rho) or abs(float(rho)) <= abs_thr:
                continue
            ea = float(intent_exp.get(a, float("-inf")))
            eb = float(intent_exp.get(b, float("-inf")))
            loser = b if ea >= eb else a
            keep.discard(loser)
            dropped.append(
                {
                    "kept": a if loser == b else b,
                    "dropped": loser,
                    "abs_corr": float(abs(rho)),
                }
            )
    return {"keep": sorted(keep), "dropped": dropped}


def signed_return_effects(
    close: np.ndarray,
    side_frame: pd.DataFrame,
    *,
    horizon: int,
) -> list[Effect]:
    """HAC t-test: is mean signed H-bar log return after the oracle event != 0?"""
    effects: list[Effect] = []
    for eid in EVENT_IDS:
        if eid not in side_frame.columns:
            continue
        side = side_frame[eid].to_numpy(dtype=float)
        vals = signed_forward_log_return(close, side, horizon)
        finite = vals[np.isfinite(vals)]
        if finite.size < 30:
            effects.append(
                Effect(
                    name=eid,
                    statistic=float("nan"),
                    n=int(finite.size),
                    p_value=float("nan"),
                    detail={"mean_bps": float("nan")},
                )
            )
            continue
        mean, t_stat = newey_west_tstat(finite, lags=horizon)
        effects.append(
            Effect(
                name=eid,
                statistic=float(mean),
                n=int(finite.size),
                p_value=normal_two_sided_p(t_stat),
                detail={
                    "t_hac": float(t_stat) if np.isfinite(t_stat) else float("nan"),
                    "mean_bps": float(mean * 1e4) if np.isfinite(mean) else float("nan"),
                },
            )
        )
    return apply_fdr(effects)


def promote_rule(
    *,
    control: dict[str, Any],
    arm: dict[str, Any],
    q_value: float,
    duplicate: bool,
    ebr_cap: float = EBR_CAP,
) -> dict[str, Any]:
    exp_ok = float(arm.get("expectancy_intent_all") or -1e9) > float(
        control.get("expectancy_intent_all") or -1e9
    )
    ctrl_pf = float(control.get("profit_factor") or 1.0)
    pf_ok = float(arm.get("profit_factor") or 0.0) >= PF_FLOOR_VS_CTRL * ctrl_pf
    ebr = float(arm.get("entry_bar_exit_rate") or float("nan"))
    ebr_ok = bool(np.isfinite(ebr) and ebr <= ebr_cap)
    fdr_ok = bool(np.isfinite(q_value) and q_value <= 0.05)
    status = str(arm.get("status") or "")
    ran = status == "RAN"
    return {
        "intent_exp_improved": bool(exp_ok),
        "pf_not_collapsed": bool(pf_ok),
        "entry_bar_ok": bool(ebr_ok),
        "fdr_ok": bool(fdr_ok),
        "not_duplicate": not bool(duplicate),
        "ran": ran,
        "promote": bool(ran and exp_ok and pf_ok and ebr_ok and fdr_ok and not duplicate),
        "q_value": float(q_value) if np.isfinite(q_value) else float("nan"),
        "entry_bar_exit_rate": ebr,
    }
