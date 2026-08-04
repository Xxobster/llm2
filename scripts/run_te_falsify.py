"""Run the three transfer-entropy falsification controls against the external panel.

Usage:
    python scripts/run_te_falsify.py --symbol BTCUSDT --timeframe 1h
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from llm2.data.loader import load_ohlcv
from llm2.data.macro import build_external_panel
from llm2.diagnostics.te_falsify import falsify_panel
from llm2.paths import ARTIFACTS, FORWARD_LOCKBOX_START
from llm2.registry.ledger import append_ledger
from llm2.validation.folds import index_to_ms


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", default="BTCUSDT")
    ap.add_argument("--timeframe", default="1h")
    ap.add_argument("--window", type=int, default=6)
    ap.add_argument("--horizon", type=int, default=6)
    ap.add_argument("--surrogates", type=int, default=100)
    ap.add_argument("--max-symbols", type=int, default=0, help="0 = all")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    import pandas as pd

    from llm2.data.macro import EXTERNAL_REGISTRY, build_external_panel

    ohlcv = load_ohlcv(args.symbol, args.timeframe)
    lock_ms = int(pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC").value // 1_000_000)
    ohlcv = ohlcv.loc[index_to_ms(ohlcv.index) < lock_ms].copy()

    # Same external set the original transfer-entropy scan used — no new series.
    symbols = sorted({s.symbol for s in EXTERNAL_REGISTRY})
    panel = build_external_panel(ohlcv.index, symbols, args.timeframe)
    reports = falsify_panel(
        ohlcv,
        panel,
        window=args.window,
        horizon=args.horizon,
        n_surrogates=args.surrogates,
        max_symbols=args.max_symbols or None,
        seed=args.seed,
    )

    survives_all = [r for r in reports if r.survives_all_three]
    survives_any = [r for r in reports if r.survives_any]
    closed = [r for r in reports if not r.survives_any]

    print(f"\n{args.symbol} {args.timeframe}: {len(reports)} pairs tested")
    print(f"  survives all three controls: {len(survives_all)}")
    print(f"  survives any control:        {len(survives_any)}")
    print(f"  closed (none survive):       {len(closed)}")

    print("\n=== per pair ===")
    for r in sorted(reports, key=lambda x: -abs(x.baseline.statistic or 0)):
        print(r.summary())
        print()

    out = {
        "symbol": args.symbol,
        "timeframe": args.timeframe,
        "window": args.window,
        "horizon": args.horizon,
        "n_pairs": len(reports),
        "n_survives_all": len(survives_all),
        "n_survives_any": len(survives_any),
        "n_closed": len(closed),
        "pairs": [
            {
                "source": r.source,
                "baseline": r.baseline.statistic,
                "baseline_q": r.baseline.q_value,
                "baseline_sig": r.baseline.significant,
                "block_shuffle": r.block_shuffle.statistic,
                "block_shuffle_sig": r.block_shuffle.significant,
                "survives_block_shuffle": r.survives_block_shuffle,
                "vol_standardised": r.vol_standardised.statistic,
                "vol_standardised_sig": r.vol_standardised.significant,
                "survives_vol_standardisation": r.survives_vol_standardisation,
                "sign_only": r.sign_only.statistic,
                "sign_only_sig": r.sign_only.significant,
                "survives_sign_only": r.survives_sign_only,
                "survives_all_three": r.survives_all_three,
            }
            for r in reports
        ],
        "verdict": (
            "NONLINEAR_CROSSASSET_OPEN"
            if survives_all
            else (
                "NONLINEAR_CROSSASSET_PARTIAL"
                if survives_any
                else "NONLINEAR_CROSSASSET_CLOSED"
            )
        ),
    }

    path = ARTIFACTS / "reports" / "diagnostics" / f"te_falsify_{args.symbol}_{args.timeframe}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"wrote {path}")

    append_ledger(
        f"TE_FALSIFY {args.symbol} {args.timeframe}: {out['verdict']} "
        f"pairs={len(reports)} all3={len(survives_all)} any={len(survives_any)} "
        f"closed={len(closed)}",
        tier=0,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
