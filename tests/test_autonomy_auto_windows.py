"""Auto-extend unused public windows so the hunt queue never idles."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.autonomy.auto_windows import (
    WindowSpec,
    emit_auto_windows_for_ids,
    events_for,
    next_in_band,
    plan_batch,
    remaining_count,
    used_periods_from_text,
)


def _ohlcv(n: int = 2200, seed: int = 11) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    close = 100.0 + np.cumsum(rng.normal(0.02, 0.35, size=n))
    idx = pd.date_range("2023-01-01", periods=n, freq="15min", tz="UTC")
    return pd.DataFrame(
        {
            "open": close,
            "high": close + 0.2,
            "low": close - 0.2,
            "close": close,
            "volume": 20.0,
        },
        index=idx,
    )


def test_events_for_kinds():
    assert events_for("sma", 678)[0] == "sma678_above_at_h"
    assert events_for("xh", 540) == (
        "xh540_at_h",
        "xl540_at_h",
        "xh540_cross_up",
        "xl540_cross_down",
    )


def test_next_in_band_skips_used():
    used = {672, 678}
    assert next_in_band(used, step=6, lo=600, hi=900) == 684


def test_next_in_band_overflow_fills_gap():
    used = set(range(900, 1600, 10))
    assert 910 in used
    assert next_in_band(used, step=10, lo=900, hi=1600) == 901


def test_plan_batch_eight_unused_slots():
    packs = (
        '"1002": GEN_1002_EVENTS\n'
        "sma672_above_at_h ema1005_below_at_h ret197_neg_at_h wma530_cross_up "
        "xh535_at_h sma2100_above_at_h ema2060_below_at_h ret856_pos_at_h"
    )
    planned = plan_batch(n=8, packs_text=packs, existing=[])
    assert [p.id for p in planned] == [str(x) for x in range(1003, 1011)]
    assert [p.kind for p in planned] == ["sma", "ema", "ret", "wma", "xh", "sma", "ema", "ret"]
    assert [p.period for p in planned] == [678, 1015, 199, 535, 540, 2120, 2080, 864]
    used = used_periods_from_text(packs)
    for spec in planned:
        assert spec.period not in used.get(spec.kind, set())


def test_emit_auto_window_finite():
    df = _ohlcv()
    spec = WindowSpec(
        id="1003",
        kind="sma",
        period=678,
        title="SMA678_distance",
        events=events_for("sma", 678),
        hypothesis="test",
    )
    n = len(df)
    occ: dict = {}
    bits: dict = {}
    sides: dict = {}
    emit_auto_windows_for_ids(
        close=df["close"].to_numpy(dtype=float),
        high=df["high"].to_numpy(dtype=float),
        low=df["low"].to_numpy(dtype=float),
        n=n,
        horizon=4,
        occ=occ,
        bits=bits,
        sides=sides,
        ids=spec.events,
        windows=[spec],
    )
    for eid in spec.events:
        assert eid in bits
        assert np.isfinite(bits[eid].astype(float)).sum() >= 20


def test_ensure_queue_writes_prereg(tmp_path: Path):
    from llm2.autonomy.auto_windows import ensure_queue_depth

    packs = tmp_path / "llm2" / "autonomy"
    packs.mkdir(parents=True)
    (packs / "packs.py").write_text(
        '"1002": GEN_1002_EVENTS\n'
        "sma672_above_at_h ema1005_below_at_h ret197_neg_at_h wma530_cross_up "
        "xh535_at_h sma2100_above_at_h ema2060_below_at_h ret856_pos_at_h\n",
        encoding="utf-8",
    )
    cfg = tmp_path / "configs" / "autonomy"
    cfg.mkdir(parents=True)
    (cfg / "research_loop_v1.yaml").write_text('generations:\n  - id: "1002"\n', encoding="utf-8")
    (cfg / "auto_public_windows.json").write_text('{"windows": []}\n', encoding="utf-8")
    (tmp_path / "configs" / "preregister").mkdir(parents=True)
    auto = tmp_path / "artifacts" / "autonomy"
    auto.mkdir(parents=True)
    (auto / "loop_state.json").write_text(json.dumps({"completed": ["1002"]}), encoding="utf-8")
    added = ensure_queue_depth(min_remaining=12, batch=8, root=tmp_path)
    assert added == [str(x) for x in range(1003, 1019)]
    assert remaining_count(
        queue_path=cfg / "research_loop_v1.yaml",
        prereg_dir=tmp_path / "configs" / "preregister",
        state_path=auto / "loop_state.json",
    ) >= 12
    assert (tmp_path / "configs" / "preregister" / "autonomy_gen_1003_public_indicators.yaml").is_file()
