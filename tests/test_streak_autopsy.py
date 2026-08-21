"""Unit tests for streak autopsy helpers."""

from __future__ import annotations

import numpy as np
import pandas as pd

from llm2.evidence.streak_autopsy import (
    annotate_trades_with_preds,
    chronological_streaks,
    cross_pack_similarity,
    miscalibration_summary,
    offline_llm_proposals,
    pack_dossier,
    rank_packs_by_pain,
)


def test_chronological_loss_streak():
    rows = []
    # 1 win, then 5 losses, then 2 wins
    pnl = [1.0, -1, -1, -1, -1, -1, 1.0, 1.0]
    for i, p in enumerate(pnl):
        rows.append(
            {
                "entry_ts_ms": 1_000_000 + i * 1000,
                "exit_ts_ms": 2_000_000 + i * 1000,
                "pnl": p,
                "trade_id": i,
            }
        )
    s = chronological_streaks(rows, min_streak=3)
    assert s["max_loss_streak"] == 5
    assert s["max_win_streak"] == 2
    assert len(s["loss_streaks_ge_n"]) == 1
    assert s["loss_streaks_ge_n"][0]["length"] == 5


def test_annotate_and_miscal():
    trades = [
        {
            "entry_ts_ms": 10,
            "exit_ts_ms": 20,
            "pnl": -1.0,
            "side": 1,
            "exit_reason": "stop",
            "signed_fwd_1": -0.01,
        },
        {
            "entry_ts_ms": 30,
            "exit_ts_ms": 40,
            "pnl": 1.0,
            "side": 1,
            "exit_reason": "target",
            "signed_fwd_1": 0.01,
        },
    ]
    df = annotate_trades_with_preds(
        trades,
        pred_ts_ms=np.array([10, 30]),
        pred_mean=np.array([0.5, 0.2]),
        pred_side=np.array([1, 1]),
    )
    assert float(df.loc[0, "abs_mean"]) == 0.5
    df["strength_tercile"] = ["high", "low"]
    m = miscalibration_summary(df, min_edge=0.1)
    assert m["n"] == 2
    assert m["n_high_strength_losers"] == 1


def test_cross_pack_and_offline_proposals():
    d1 = pack_dossier(
        version_id="a",
        symbol="ETHUSDT",
        geometry={"mode": "single"},
        trades_df=pd.DataFrame(
            [
                {
                    "entry_ts_ms": 1,
                    "exit_ts_ms": 2,
                    "pnl": -1,
                    "side": 1,
                    "book_idx": 1,
                    "strength_tercile": "high",
                    "vol_tercile": "high",
                    "exit_reason": "stop",
                    "signed_fwd_1": -0.01,
                    "win": False,
                }
            ]
            * 4
            + [
                {
                    "entry_ts_ms": 10 + i,
                    "exit_ts_ms": 20 + i,
                    "pnl": 1,
                    "side": 1,
                    "book_idx": 1,
                    "strength_tercile": "low",
                    "vol_tercile": "low",
                    "exit_reason": "target",
                    "signed_fwd_1": 0.01,
                    "win": True,
                }
                for i in range(2)
            ]
        ),
        streaks=chronological_streaks(
            [
                {
                    "entry_ts_ms": i,
                    "exit_ts_ms": i + 1,
                    "pnl": -1 if i < 4 else 1,
                    "trade_id": i,
                }
                for i in range(6)
            ],
            min_streak=3,
        ),
        miscal={"frac_high_strength_and_loss": 0.2},
    )
    d2 = dict(d1)
    d2["version_id"] = "b"
    d2["elevated_loss_streak_buckets"] = d1["elevated_loss_streak_buckets"]
    shared = cross_pack_similarity([d1, d2], min_starts=1)
    assert isinstance(shared, list)
    pain = rank_packs_by_pain([d1, d2])
    assert pain[0]["version_id"] in {"a", "b"}
    prop = offline_llm_proposals({"pain_rank": pain, "cross_pack_loss_streak_buckets": shared})
    assert prop["promotion_blocked"] is True
    assert len(prop["proposals"]) <= 5
