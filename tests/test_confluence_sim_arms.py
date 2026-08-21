"""Checkpoint helpers for the autonomous hunt."""

from __future__ import annotations

from llm2.confluence.sim_arms import arm_done, jsonable, open_checkpoint, save_arm, load_arms


def test_checkpoint_roundtrip(tmp_path):
    con = open_checkpoint(tmp_path / "hunt.sqlite")
    assert not arm_done(con, "a")
    save_arm(
        con,
        "a",
        {
            "symbol": "ETHUSDT",
            "timeframe": "15m",
            "horizon": 4,
            "event": "control",
            "mode": "control",
            "tp": 0.01,
            "sl": 0.01,
            "gate": "p75",
        },
        {"status": "RAN", "n_trades": 10, "profit_factor": 1.2},
    )
    assert arm_done(con, "a")
    rows = load_arms(con)
    assert len(rows) == 1
    assert rows[0]["profit_factor"] == 1.2
    con.close()


def test_jsonable_nan():
    assert jsonable(float("nan")) is None
    assert jsonable({"x": 1}) == {"x": 1}
