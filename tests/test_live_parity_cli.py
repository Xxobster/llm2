from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load_cli():
    spec = importlib.util.spec_from_file_location("live_parity_cli_mod", ROOT / "scripts" / "live_parity.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_live_parity_dry_run_lists_steps() -> None:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "live_parity.py"),
            "--i-accept-lockbox-contamination",
            "--dry-run",
            "--host",
            "both",
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "would: pull_ln1" in proc.stdout
    assert "would: audit_ln2" in proc.stdout


def test_arm_closeness_maps_rates_and_fills() -> None:
    mod = _load_cli()
    arm = {
        "candles": {"match_rate": 1.0},
        "replay": {"action_match_rate": 1.0, "p_any_match_rate": 0.997},
        "fills": {
            "pairs": [
                {"same_side": True, "entry_slip_ok": True, "entry_slip_frac": 0.00013},
                {"same_side": True, "entry_slip_ok": True, "entry_slip_frac": 0.0002},
            ]
        },
    }
    c = mod.arm_closeness(arm)
    assert c["candles_pct"] == 100.0
    assert c["signals_pct"] == 100.0
    assert abs(c["calculations_pct"] - 99.7) < 1e-9
    assert c["entries_exits_pct"] == 100.0
    assert c["fill_price_pct"] > 99.9
    table = mod._format_glimpse([{"label": "Xxobster7 unit-a", **c}], title="CLOSENESS")
    assert "candles" in table
    assert "100%" in table
    assert mod._fmt_pct(None) == "n/a"


def test_classify_missed_counts_bt_enter_without_live() -> None:
    spec = importlib.util.spec_from_file_location(
        "audit_pivot_mod", ROOT / "scripts" / "audit_llm2_pivot_live_vs_bt.py"
    )
    assert spec and spec.loader
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    import numpy as np

    ts = np.array([1000, 2000, 3000], dtype=np.int64)
    act = np.array(["FLAT", "ENTER_LIMIT", "ENTER_LIMIT"])
    live_by = {
        1000: {"action": "FLAT"},
        2000: {"action": "FLAT"},
    }
    replay = {
        "flips": [
            {
                "utc": "t2",
                "live_action": "FLAT",
                "bt_action": "ENTER_LIMIT",
            }
        ]
    }
    out = audit.classify_missed(
        ts_ms=ts,
        bt_action=act,
        live_by_ts=live_by,
        replay=replay,
        live_counts={"ENTER_LIMIT": 2, "filled": 0, "cancelled_data_unsafe": 2},
        fills={"n_extra_bt": 1, "extra_bt_trades": [{}]},
        since_ms=1000,
        last_live_ms=3000,
    )
    assert out["n_replay_bt_enter_live_not"] == 1
    assert out["n_bt_enter_no_live_row"] == 1
    assert out["n_missed_signals"] == 2
    assert out["n_live_enter_unfilled"] == 2
    assert out["n_extra_bt_trades"] == 1
    assert out["n_missed_trades"] == 3
