"""Run the frozen pulse-continuation preregistration through tradesim."""

from __future__ import annotations

import argparse
import json

from llm2.experiments.pulse_continuation import PREREG_PATH, run_pulse_continuation
from llm2.paths import ARTIFACTS


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prereg", default=str(PREREG_PATH))
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    from pathlib import Path

    res = run_pulse_continuation(prereg_path=Path(args.prereg), seed=args.seed)

    print(f"\n=== {res['verdict']} ===")
    print(f"prereg   {res['prereg_sha256'][:16]}   folds {res['fold_design_hash']}")
    st = res["engine_stamp"]
    print(f"engine   {st['engine_name']} {st['engine_version']} "
          f"fixtures {st['fixture_pack_hash'][:12]} "
          f"conformance {st['satisfied_count']}/{st['required_count']}")
    print(f"\n{'arm':22s} {'PF':>8s} {'net PnL':>12s} {'trades':>7s} "
          f"{'fees':>10s} {'funding':>10s} {'entryTP':>8s} {'liq':>4s}")
    for name, arm in res["arms"].items():
        print(f"{name:22s} {arm['pooled_pf']:8.3f} {arm['pooled_pnl']:12.2f} "
              f"{arm['n_trades']:7d} {arm['fees_paid']:10.2f} {arm['funding_paid']:10.2f} "
              f"{arm['entry_bar_stops']:8d} {arm['liquidations']:4d}")

    print("\nper-fold (pulse arm):")
    for r in res["arms"]["pulse"]["fold_rows"]:
        print(f"  fold {r['fold']}: signals={r.get('signals', 0):3d} trades={r['n']:3d} "
              f"pnl={r['pnl']:10.2f} gp={r['gross_profit']:9.2f} gl={r['gross_loss']:9.2f}")

    print("\ncriteria:")
    for k, v in res["criteria"].items():
        print(f"  {k}: {v}")

    out = ARTIFACTS / "reports" / "pulse_continuation_result.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=2, default=str), encoding="utf-8")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
