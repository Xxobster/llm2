"""Run the A–B / B–C distance-factor similarity study (RESEARCH_ONLY)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.diagnostics.abc_factor import (
    build_abc_triples,
    factor_summary,
    load_legs,
    run_abc_factor_study,
)
from llm2.diagnostics.stats import effects_to_frame
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START

SYMBOL = "BTCUSDT"
TIMEFRAMES = ("1h", "4h")
TRAIN_END = FORWARD_LOCKBOX_START


def main() -> int:
    out_dir = ARTIFACTS / "reports" / "abc_factor"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    all_rows = []

    for tf in TIMEFRAMES:
        print(f"\n=== {SYMBOL} {tf} ===")
        ohlcv_full = load_ohlcv(SYMBOL, tf)
        ohlcv = ohlcv_full[ohlcv_full.index < pd.Timestamp(TRAIN_END, tz="UTC")]
        legs = load_legs(SYMBOL, tf)
        # Restrict legs to those confirmed before lockbox
        legs = legs[legs["end_ts_ms"] < int(pd.Timestamp(TRAIN_END, tz="UTC").timestamp() * 1000)]
        triples = build_abc_triples(legs)
        summary = factor_summary(triples)
        print(f"triples={int(summary['n_triples'])} median_factor={summary['median']:.3f} "
              f"near_1.0={summary['frac_near_1.0']:.1%} near_0.618={summary['frac_near_0.618']:.1%}")

        effects = run_abc_factor_study(ohlcv, SYMBOL, tf)
        n_sig = sum(e.significant for e in effects)
        print(f"effects={len(effects)} significant_q05={n_sig}")
        frame = effects_to_frame(effects)
        if len(frame):
            top = frame.sort_values("q_value").head(15)
            print(top[["name", "statistic", "n", "p_value", "q_value", "significant"]].to_string(index=False))
        all_rows.append(
            {
                "symbol": SYMBOL,
                "timeframe": tf,
                "summary": summary,
                "n_effects": len(effects),
                "n_significant": n_sig,
                "effects": json.loads(frame.to_json(orient="records")) if len(frame) else [],
            }
        )

    payload = {
        "study_id": "abc_factor_001",
        "readiness": "RESEARCH_ONLY",
        "train_end": TRAIN_END,
        "definition": (
            "Confirmed warehouse swings: consecutive legs share B; "
            "factor = |C-B| / |B-A|; knowable at confirmation of C"
        ),
        "runs": all_rows,
        "stamped_utc": stamp,
    }
    json_path = out_dir / f"abc_factor_{SYMBOL}_{stamp}.json"
    md_path = out_dir / f"abc_factor_{SYMBOL}_{stamp}.md"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, default=str)

    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(f"# ABC distance-factor study — {SYMBOL} ({stamp})\n\n")
        fh.write(f"**Readiness: RESEARCH_ONLY.** Train window ends `{TRAIN_END}`.\n\n")
        fh.write(
            "Definition: three consecutive confirmed swings A→B→C; "
            "`factor = |BC| / |AB|`; known only when C is confirmed.\n\n"
        )
        for run in all_rows:
            fh.write(f"## {run['symbol']} {run['timeframe']}\n\n")
            s = run["summary"]
            fh.write(
                f"- triples: {int(s['n_triples'])}, median factor {s['median']:.3f}, "
                f"fraction near 1.0: {s['frac_near_1.0']:.1%}, "
                f"near 0.618: {s['frac_near_0.618']:.1%}, "
                f"near 1.618: {s['frac_near_1.618']:.1%}\n"
            )
            fh.write(f"- effects: {run['n_effects']}, FDR survivors q≤0.05: {run['n_significant']}\n\n")
            if run["effects"]:
                fh.write("| name | statistic | n | p | q | significant |\n|---|---|---|---|---|---|\n")
                rows = sorted(run["effects"], key=lambda r: r.get("q_value", 1) or 1)[:20]
                for e in rows:
                    fh.write(
                        f"| {e['name']} | {e['statistic']:.5f} | {e['n']} | "
                        f"{e.get('p_value', float('nan')):.4f} | "
                        f"{e.get('q_value', float('nan')):.4f} | {e.get('significant')} |\n"
                    )
                fh.write("\n")

    print(f"\nwrote {json_path}\nwrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
