"""Freeze the hunt 002 (Average True Range bracket) survivors for the nested settle.

Selection is mechanical and happens **before** any outer out-of-sample bar is
scored. Hunt 001 taught the lesson this encodes: ranking 154 inner passes by
inner profit factor produced 0 of 12 survivors out of sample, because inner
profit factor is exactly the quantity selection noise inflates.

So this script does three things differently:

1. **Ranks by dependence-aware Sharpe**, not profit factor. The HAC (Newey-West)
   annualised Sharpe already discounts serially correlated returns.
2. **Raises the trade floor to 80.** Hunt 001's survivors clustered at 50-60
   trades, where a handful of lucky trades moves profit factor by 0.5.
3. **Caps concentration** so the settle tests distinct mechanisms rather than
   twelve session variants of one event on one symbol.

Every arm must already clear the frozen screen, including the 25% entry-bar exit
ceiling, which is the gate that makes an Average True Range bracket meaningful.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path

import yaml

_ROOT = Path(__file__).resolve().parents[1]
HUNT_DB = _ROOT / "artifacts" / "sqlite" / "edge_lab_hunt_002_atr" / "hunt.sqlite"
OUT_YAML = _ROOT / "configs" / "preregister" / "edge_lab_nested_settle_002_atr.yaml"

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
    # Best bracket per distinct mechanism, so bracket variants cannot crowd out events.
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
    ap.add_argument("--write", action="store_true", help="write the preregister YAML")
    args = ap.parse_args()

    rows = load_scored(HUNT_DB)
    ok = [d for d in rows if passes_screen(d)]
    chosen = select(rows)
    print(f"scored={len(rows)} clear_screen={len(ok)} distinct_mechanisms_selected={len(chosen)}")
    print(f"  by symbol:    {dict(Counter(str(d['symbol']) for d in chosen).most_common())}")
    print(f"  by timeframe: {dict(Counter(str(d['timeframe']) for d in chosen).most_common())}")
    print()
    for i, d in enumerate(chosen, 1):
        print(
            f"  {i:2d}. HACSh={_num(d, 'sharpe_hac_annualised'):5.2f} "
            f"PF={_num(d, 'profit_factor'):5.2f} n={int(_num(d, 'n_trades')):4d} "
            f"tpm={_num(d, 'trades_per_month'):5.2f} ebr={_num(d, 'entry_bar_exit_rate'):.2f} "
            f"fill={_num(d, 'fill_pct'):.2f}  {d.get('arm_id')}"
        )

    survivors = [
        {
            "symbol": str(d["symbol"]),
            "timeframe": str(d["timeframe"]),
            "event": str(d["event"]),
            "session_filter": str(d["session_filter"]),
            "k_sl": float(d["k_sl"]),
            "tp_ratio": float(d["tp_ratio"]),
            "inner_profit_factor": round(_num(d, "profit_factor"), 4),
            "inner_hac_sharpe": round(_num(d, "sharpe_hac_annualised"), 4),
            "inner_n_trades": int(_num(d, "n_trades")),
            "inner_entry_bar_exit_rate": round(_num(d, "entry_bar_exit_rate"), 4),
            "inner_fill_pct": round(_num(d, "fill_pct"), 4),
        }
        for d in chosen
    ]

    if not args.write:
        print("\n(dry run: pass --write to freeze the preregister YAML)")
        return 0

    cfg = {
        "generation_id": "edge_lab_nested_settle_002_atr",
        "hypothesis": (
            "Events that clear the hunt 002 inner screen with an Average True Range "
            "scaled bracket — and therefore an entry-bar exit rate at or below 25% — "
            "retain a post-cost edge on outer out-of-sample folds. Hunt 001 rejected "
            "the same events under fixed percentage brackets, where the edge was "
            "confounded with same-bar noise resolution."
        ),
        "readiness_max": "SHADOW_READY",
        "posture": "LIVE_STOP / RESEARCH_ONLY",
        "selection": {
            "source_hunt": "edge_lab_hunt_002_atr",
            "screen_window": "pre-2022-01-01 (inner only)",
            "objective": "HAC annualised Sharpe, descending",
            "min_trades": MIN_TRADES,
            "min_profit_factor": MIN_PF,
            "min_hac_sharpe": MIN_HAC_SHARPE,
            "min_trades_per_month": MIN_TPM,
            "max_entry_bar_exit_rate": MAX_ENTRY_BAR_RATE,
            "min_fill_pct": MIN_FILL,
            "dedupe": "one arm per (symbol, timeframe, event)",
            "max_per_symbol": MAX_PER_SYMBOL,
            "max_per_timeframe": MAX_PER_TIMEFRAME,
            "n_survivors": len(survivors),
            "note": (
                "Ranked by HAC Sharpe rather than profit factor, and the trade floor "
                "raised from 50 to 80, because hunt 001 ranked by inner profit factor "
                "at 50-60 trades and returned 0 of 12 out of sample."
            ),
        },
        "work_bars": {"15m": 4, "1h": 3, "4h": 2},
        "max_hold_bars": {"15m": 16, "1h": 8, "4h": 6},
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
        "quotable_metrics": (
            "Profit factor, win rate, payoff, Sharpe, HAC Sharpe, Sortino, entry-bar "
            "exit rate and fill rate are scale-free and quotable. Total return, max "
            "drawdown and recovery factor are NOT quotable: positions are "
            "minimum-exchange size against the research wallet, so drawdown lands near "
            "0.02% and carries no risk information."
        ),
        "survivors": survivors,
    }
    OUT_YAML.parent.mkdir(parents=True, exist_ok=True)
    OUT_YAML.write_text(
        "# Frozen mechanically from the hunt 002 inner screen before any outer\n"
        "# out-of-sample bar was scored. Do not edit survivors after the settle runs.\n"
        + yaml.safe_dump(cfg, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"\nWROTE {OUT_YAML} survivors={len(survivors)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
