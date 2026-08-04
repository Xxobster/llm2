"""Sample-size design for the WAVE001 candidate space: count events, not performance.

Mirrors ``scripts/design_pulse_folds.py``. This script computes **no** effect size,
correlation, or p-value for any wave hypothesis — only how many triggers, amplitude events,
and structure breaks would have fired inside each existing outer fold
(``llm2.validation.folds.OUTER_FOLD_RANGES``), so the ten-events-per-fold and fifty-pooled
floors in ``docs/project_memory/FROZEN_DEFAULT_GATES_V2_1.md`` can be checked before
``scripts/run_wave_scan.py`` computes anything.
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.diagnostics.structurebreak import BOUNDARY_PAIRS, _atr, build_boundaries, detect_breaks
from llm2.diagnostics.wave import fit_wave
from llm2.diagnostics.waveevent import detect_amplitude_events
from llm2.diagnostics.wavemetrics import build_causal_metrics, detect_triggers
from llm2.paths import ARTIFACTS

SYMBOL, TIMEFRAME = "BTCUSDT", "1h"
TRAIN_END = "2026-05-01"
MIN_EVENTS_PER_FOLD = 10
MIN_POOLED_EVENTS = 50


def _fold_counts(timestamps: pd.DatetimeIndex, event_bars: np.ndarray) -> list[int]:
    from llm2.validation.folds import OUTER_FOLD_RANGES

    event_ts = timestamps[event_bars]
    counts = []
    for start, end in OUTER_FOLD_RANGES:
        a, b = pd.Timestamp(start, tz="UTC"), pd.Timestamp(end, tz="UTC")
        counts.append(int(((event_ts >= a) & (event_ts < b)).sum()))
    return counts


def _report(name: str, timestamps: pd.DatetimeIndex, event_bars: np.ndarray) -> dict:
    counts = _fold_counts(timestamps, event_bars)
    under = sum(1 for c in counts if c < MIN_EVENTS_PER_FOLD)
    pooled = sum(counts)
    ok = under == 0 and pooled >= MIN_POOLED_EVENTS
    flag = "CLEARS FLOOR" if ok else "UNDER FLOOR"
    print(f"  {name:48s} per-fold={counts} pooled={pooled:4d} under={under} {flag}")
    return {
        "name": name,
        "per_fold": counts,
        "pooled": pooled,
        "folds_under_floor": under,
        "clears_floor": ok,
    }


def main() -> int:
    ohlcv = load_ohlcv(SYMBOL, TIMEFRAME)
    ohlcv = ohlcv[ohlcv.index < pd.Timestamp(TRAIN_END, tz="UTC")]
    idx = ohlcv.index

    fit = fit_wave(ohlcv["close"], symbol=SYMBOL, timeframe=TIMEFRAME)
    period = fit.period_bars
    print(
        f"{SYMBOL} {TIMEFRAME}: {len(ohlcv):,} bars to {TRAIN_END}, fitted period "
        f"{period:.1f} bars (peak {fit.peak_ratio:.2f}x, p={fit.p_value:.4f})\n"
    )
    if not np.isfinite(period) or period <= 2:
        print("No usable period fit; nothing to design event geometry around.")
        return 1

    metrics = build_causal_metrics(ohlcv["close"], ohlcv.get("volume"), period)
    results: list[dict] = []

    print("=== wavemetrics triggers ===")
    for name, ev in detect_triggers(metrics, period=period).items():
        results.append(_report(f"trigger:{name}", idx, np.flatnonzero(ev.to_numpy())))

    print("\n=== amplitude events (waveevent) ===")
    for name, ev in detect_amplitude_events(metrics, period=period).items():
        results.append(_report(f"amp_event:{name}", idx, np.flatnonzero(ev.to_numpy())))

    print("\n=== structure breaks (structurebreak) ===")
    boundaries = build_boundaries(ohlcv, SYMBOL, TIMEFRAME)
    atr = _atr(ohlcv).reindex(boundaries.index)
    ohlcv_b = ohlcv.reindex(boundaries.index)
    for boundary_name, (up_col, lo_col) in BOUNDARY_PAIRS.items():
        if up_col not in boundaries.columns or lo_col not in boundaries.columns:
            print(f"  {boundary_name}: boundary columns missing, skipped")
            continue
        confirmations = detect_breaks(ohlcv_b, boundaries[up_col], boundaries[lo_col], atr=atr)
        for conf_name, ev in confirmations.items():
            results.append(
                _report(f"break:{boundary_name}:{conf_name}", boundaries.index, np.flatnonzero(ev.to_numpy()))
            )

    n_ok = sum(1 for r in results if r["clears_floor"])
    print(
        f"\n{n_ok}/{len(results)} candidate event definitions clear the "
        f"{MIN_EVENTS_PER_FOLD}-per-fold / {MIN_POOLED_EVENTS}-pooled floor."
    )
    if n_ok < len(results):
        print(
            "The honest reading for anything under the floor is that it cannot be evaluated "
            "at the required evidence level on this geometry, not that the floor should move."
        )

    out_dir = ARTIFACTS / "reports" / "wave001"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "event_design.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(
            {
                "designed_utc": pd.Timestamp.utcnow().isoformat(),
                "basis": "event counts only; no performance statistic was computed",
                "symbol": SYMBOL,
                "timeframe": TIMEFRAME,
                "period_bars": period,
                "min_events_per_fold": MIN_EVENTS_PER_FOLD,
                "min_pooled_events": MIN_POOLED_EVENTS,
                "results": results,
            },
            fh,
            indent=2,
            default=str,
        )
    print(f"\nwrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
