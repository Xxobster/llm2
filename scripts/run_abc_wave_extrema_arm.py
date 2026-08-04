"""Causal-wave extrema ABC factor arm — separate from warehouse legs (train only)."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pandas as pd

from llm2.data.loader import load_ohlcv
from llm2.diagnostics.abc_factor import (
    build_abc_triples_from_extrema,
    causal_wave_extrema,
    factor_summary,
    run_abc_factor_study_wave_extrema,
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
        print(f"\n=== WAVE EXTREMA ARM {SYMBOL} {tf} ===")
        ohlcv_full = load_ohlcv(SYMBOL, tf)
        ohlcv = ohlcv_full[ohlcv_full.index < pd.Timestamp(TRAIN_END, tz="UTC")]
        extrema = causal_wave_extrema(ohlcv["close"].astype(float))
        triples = build_abc_triples_from_extrema(extrema)
        summary = factor_summary(triples) if len(triples) else {"n_triples": 0}
        print(
            f"triples={int(summary.get('n_triples', 0))} "
            f"median_factor={summary.get('median', float('nan'))}"
        )
        effects = run_abc_factor_study_wave_extrema(ohlcv)
        n_sig = sum(e.significant for e in effects)
        print(f"effects={len(effects)} significant_q05={n_sig}")
        frame = effects_to_frame(effects)
        if len(frame):
            top = frame.sort_values("q_value").head(15)
            print(top[["name", "statistic", "n", "p_value", "q_value", "significant"]].to_string(
                index=False
            ))
        all_rows.append(
            {
                "symbol": SYMBOL,
                "timeframe": tf,
                "geometry": "causal_wave_extrema",
                "summary": summary,
                "n_effects": len(effects),
                "n_significant": n_sig,
                "effects": json.loads(frame.to_json(orient="records")) if len(frame) else [],
            }
        )

    payload = {
        "study_id": "abc_wave_extrema_001",
        "readiness": "RESEARCH_ONLY",
        "train_end": TRAIN_END,
        "definition": (
            "Causal-wave peaks/troughs confirmed one bar after the turn; "
            "factor = |BC|/|AB|; SEPARATE arm from warehouse legs — not tradeable geometry"
        ),
        "runs": all_rows,
        "stamped_utc": stamp,
    }
    json_path = out_dir / f"abc_wave_extrema_{SYMBOL}_{stamp}.json"
    md_path = out_dir / f"abc_wave_extrema_{SYMBOL}_{stamp}.md"
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(f"# ABC wave-extrema factor arm — {SYMBOL} ({stamp})\n\n")
        fh.write(f"**Readiness: RESEARCH_ONLY.** Train window ends `{TRAIN_END}`.\n\n")
        fh.write(
            "Separate arm from warehouse `indicators.legs`. Labels are `abc_wave|*`. "
            "Not a substitute for audited confirmation times on swing legs.\n\n"
        )
        for run in all_rows:
            fh.write(f"## {run['symbol']} {run['timeframe']}\n\n")
            s = run["summary"]
            fh.write(
                f"- triples: {int(s.get('n_triples', 0))}, "
                f"median factor {s.get('median', float('nan'))}\n"
            )
            fh.write(
                f"- effects: {run['n_effects']}, FDR survivors q≤0.05: {run['n_significant']}\n\n"
            )
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
