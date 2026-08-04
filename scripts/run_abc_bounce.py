"""One-shot forward-lockbox evaluation of abc_bounce_001 (preregistered)."""

from __future__ import annotations

from llm2.experiments.abc_bounce import run_abc_bounce
from llm2.research_policy import PolicyError


def main() -> int:
    try:
        out = run_abc_bounce()
    except PolicyError as exc:
        print(f"HOLD: {exc}")
        return 5
    print(f"verdict={out['verdict']} success={out['success']} "
          f"family_closed={out['family_closed']} underpowered={out['underpowered']}")
    bounce = out["arms"]["bounce"]
    ctrl = out["arms"]["random_vol_matched"]
    print(f"bounce PF={bounce['pooled_pf']:.4f} n={bounce['n_trades']} "
          f"pnl={bounce['pooled_pnl']:.2f}")
    print(f"control PF={ctrl['pooled_pf']:.4f} n={ctrl['n_trades']} "
          f"pnl={ctrl['pooled_pnl']:.2f}")
    print(f"prereg_sha256={out['prereg_sha256']}")
    print(f"wrote {out['report_md']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
