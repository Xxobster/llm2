"""Seal: structure_v1 direction nest-filter trading branch is closed (D-060).

Thresholds below are FROZEN after outer OOS view. Re-running with modified
filter grids, arms, percentiles, or score cutoffs is FORBIDDEN without a new
preregistered generation and an explicit forensics override.
"""

from __future__ import annotations

import os
import sys
from typing import Mapping

# Frozen after structure_v1_forecast_filter_on_direction_001 OOS (do not retune).
FROZEN_NEST_THRESHOLDS: dict[str, float | str | int] = {
    "generation_id": "structure_v1_forecast_filter_on_direction_001",
    "status": "CLOSED_TRADING_FAIL",
    "tp_pct": 0.01,
    "sl_pct": 0.02,
    "max_hold_bars": 6,
    "min_edge": 0.1,
    "deep_retrace_thresh": 0.5,
    "retrace_score_min": 0.05,
    "vol_skip_percentile": 75,
    "vol_filter_name": "skip_top_quartile_predicted_vol",
    "stage1_ic_min": 0.05,
    "stage1_ic_pos_frac": 0.66,
    "stage1_deep_shallow_acc_min": 0.55,
}

# Related gens closed for trading claims (forecast skill may still be reported).
CLOSED_TRADING_GENERATIONS = frozenset(
    {
        "structure_v1_caus_retrain_001",
        "structure_v1_causal_drop_retrace_001",
        "structure_v1_next_retrace_forecast_001",  # Stage-2 trade FAIL; Stage-1 skill ok forensically
        "structure_v1_forecast_filter_on_direction_001",
    }
)


def refuse_nest_filter_retune(
    *,
    argv: list[str] | None = None,
    context: str,
    proposed: Mapping[str, object] | None = None,
) -> None:
    """Abort retuning of nest-filter thresholds after D-060 close.

    Diagnostics with the exact frozen constants may re-run only when:
      LLM2_ALLOW_CLOSED_NEST_FILTER_RERUN=1
      AND --i-accept-closed-trading-fail-rerun
    Never for pack freeze or live.
    """
    args = list(sys.argv[1:] if argv is None else argv)
    allow_env = os.environ.get("LLM2_ALLOW_CLOSED_NEST_FILTER_RERUN", "").strip() in {
        "1",
        "true",
        "TRUE",
        "yes",
    }
    allow_flag = "--i-accept-closed-trading-fail-rerun" in args
    if proposed:
        for key, frozen in FROZEN_NEST_THRESHOLDS.items():
            if key in proposed and proposed[key] != frozen:
                print(
                    "REFUSED: nest-filter threshold retune after outer OOS (D-060).\n"
                    f"  key={key!r} frozen={frozen!r} proposed={proposed[key]!r}\n"
                    f"  context: {context}\n"
                    "  Open a NEW preregistered generation; do not retune this one.\n",
                    file=sys.stderr,
                    flush=True,
                )
                raise SystemExit(3)
    if allow_env and allow_flag:
        print(
            f"[CLOSED_NEST_FILTER_RERUN] diagnostics only with FROZEN thresholds — {context}. "
            "Promotion and pack freeze remain FORBIDDEN.",
            flush=True,
        )
        return
    print(
        "REFUSED: structure_v1 direction nest-filter trading branch is CLOSED (D-060).\n"
        f"  context: {context}\n"
        "  Trading FAIL: outer mean_fold Profit Factor < 1 on control and filter arms.\n"
        "  Do not retune agree threshold, vol percentile, TP/SL/hold, or arm list on OOS.\n"
        "  Forecast skill of next_retrace is NOT a trading authorization.\n"
        "  Exact frozen re-run (report only) requires BOTH:\n"
        "    LLM2_ALLOW_CLOSED_NEST_FILTER_RERUN=1\n"
        "    --i-accept-closed-trading-fail-rerun\n",
        file=sys.stderr,
        flush=True,
    )
    raise SystemExit(3)
