"""Freeze hunt 003 (WaveTheory structure) survivors for the nested settle.

Mechanical, before any outer out-of-sample bar is scored. Same selection rule as
hunt 002: HAC Sharpe rank, trade floor 80, entry-bar ceiling 0.25, one arm per
(symbol, timeframe, event).
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parents[1]
HUNT_DB = _ROOT / "artifacts" / "sqlite" / "edge_lab_hunt_003_structure_mtf" / "hunt.sqlite"
OUT_YAML = _ROOT / "configs" / "preregister" / "edge_lab_nested_settle_003_structure_mtf.yaml"

MIN_TRADES = 80
MIN_PF = 1.20
MIN_HAC_SHARPE = 0.75
MIN_TPM = 2.0
MAX_ENTRY_BAR_RATE = 0.25
MIN_FILL = 0.25
N_SURVIVORS = 24
MAX_PER_SYMBOL = 10
MAX_PER_TIMEFRAME = 12


def _num(d: dict, k: str) -> float:
    try:
        v = float(d.get(k))
    except (TypeError, ValueError):
        return float("nan")
    return v


def load_scored(db: Path) -> list[dict]:
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    out = []
    for (payload,) in con.execute("SELECT payload FROM arms WHERE payload IS NOT NULL"):
        try:
            d = json.loads(payload)
        except Exception:
            continue
        if str(d.get("status")) == "RAN":
            out.append(d)
    con.close()
    return out


def passes_screen(d: dict) -> bool:
    return (
        int(_num(d, "n_trades") or 0) >= MIN_TRADES
        and _num(d, "profit_factor") >= MIN_PF
        and _num(d, "sharpe_hac_annualised") >= MIN_HAC_SHARPE
        and _num(d, "trades_per_month") >= MIN_TPM
        and _num(d, "entry_bar_exit_rate") <= MAX_ENTRY_BAR_RATE
        and _num(d, "fill_pct") >= MIN_FILL
    )


def select(rows: list[dict]) -> list[dict]:
    ok = [d for d in rows if passes_screen(d)]
    best: dict[tuple, dict] = {}
    for d in ok:
        key = (d.get("symbol"), d.get("timeframe"), d.get("event"))
        cur = best.get(key)
        if cur is None or _num(d, "sharpe_hac_annualised") > _num(cur, "sharpe_hac_annualised"):
            best[key] = d
    ranked = sorted(best.values(), key=lambda d: -_num(d, "sharpe_hac_annualised"))
    chosen: list[dict] = []
    per_sym: Counter = Counter()
    per_tf: Counter = Counter()
    for d in ranked:
        if len(chosen) >= N_SURVIVORS:
            break
        s, tf = str(d.get("symbol")), str(d.get("timeframe"))
        if per_sym[s] >= MAX_PER_SYMBOL or per_tf[tf] >= MAX_PER_TIMEFRAME:
            continue
        chosen.append(d)
        per_sym[s] += 1
        per_tf[tf] += 1
    return chosen


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    rows = load_scored(HUNT_DB)
    ok = [d for d in rows if passes_screen(d)]
    chosen = select(rows)
    print(f"scored={len(rows)} clear_screen={len(ok)} selected={len(chosen)}")
    print(f"  by symbol:    {dict(Counter(str(d['symbol']) for d in chosen).most_common())}")
    print(f"  by timeframe: {dict(Counter(str(d['timeframe']) for d in chosen).most_common())}")
    print(f"  by event:     {dict(Counter(str(d['event']) for d in chosen).most_common())}")
    for i, d in enumerate(chosen, 1):
        print(
            f"  {i:2d}. HACSh={_num(d, 'sharpe_hac_annualised'):5.2f} "
            f"PF={_num(d, 'profit_factor'):5.2f} n={int(_num(d, 'n_trades')):4d} "
            f"tpm={_num(d, 'trades_per_month'):5.2f} ebr={_num(d, 'entry_bar_exit_rate'):.2f} "
            f"{d.get('arm_id')}"
        )

    survivors = [
        {
            "symbol": str(d["symbol"]),
            "timeframe": str(d["timeframe"]),
            "event": str(d["event"]),
            "session_filter": str(d["session_filter"]),
            "k_sl": float(d["k_sl"]),
            "tp_ratio": float(d["tp_ratio"]),
            "htf": str(d.get("htf") or ""),
            "swing_wing": int(d.get("swing_wing") or 5),
            "inner_profit_factor": round(_num(d, "profit_factor"), 4),
            "inner_hac_sharpe": round(_num(d, "sharpe_hac_annualised"), 4),
            "inner_n_trades": int(_num(d, "n_trades")),
            "inner_entry_bar_exit_rate": round(_num(d, "entry_bar_exit_rate"), 4),
        }
        for d in chosen
    ]
    if not args.write:
        print("\n(dry run: pass --write to freeze)")
        return 0

    cfg = {
        "generation_id": "edge_lab_nested_settle_003_structure_mtf",
        "hypothesis": (
            "WaveTheory-derived, causally implemented pullback and structure-break "
            "events that clear the hunt 003 inner screen retain a post-cost edge on "
            "outer out-of-sample folds. No numeric result is inherited from the "
            "original WaveTheory project."
        ),
        "readiness_max": "SHADOW_READY",
        "posture": "LIVE_STOP / RESEARCH_ONLY",
        "selection": {
            "source_hunt": "edge_lab_hunt_003_structure_mtf",
            "screen_window": "pre-2022-01-01 (inner only)",
            "objective": "HAC annualised Sharpe, descending",
            "min_trades": MIN_TRADES,
            "min_profit_factor": MIN_PF,
            "min_hac_sharpe": MIN_HAC_SHARPE,
            "min_trades_per_month": MIN_TPM,
            "max_entry_bar_exit_rate": MAX_ENTRY_BAR_RATE,
            "min_fill_pct": MIN_FILL,
            "dedupe": "one arm per (symbol, timeframe, event)",
            "n_survivors": len(survivors),
        },
        "higher_timeframe_map": {"5m": "1h", "15m": "4h", "1h": "4h", "4h": "1d"},
        "swing_wing": {"5m": 12, "15m": 8, "1h": 5, "4h": 5},
        "work_bars": {"5m": 6, "15m": 4, "1h": 3, "4h": 2},
        "max_hold_bars": {"5m": 36, "15m": 24, "1h": 16, "4h": 10},
        "sl_cap": 0.030,
        "gates_for_shadow_ready": {
            "min_eligible_folds": 5,
            "min_pooled_oos_trades": 50,
            "min_pooled_profit_factor": 1.20,
            "min_sharpe_annualised": 1.00,
            "min_sharpe_hac_annualised": 0.75,
            "min_fraction_positive_folds": 0.80,
            "max_entry_bar_exit_rate": 0.25,
        },
        "survivors": survivors,
    }
    OUT_YAML.write_text(
        "# Frozen mechanically from hunt 003 inner screen before any outer OOS bar.\n"
        + yaml.safe_dump(cfg, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"\nWROTE {OUT_YAML} survivors={len(survivors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
