"""Re-run the four settled ETH/SOL structure_v1 winners and dump full numeric metrics."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_leak = Path(r"C:\projects\botsgeneral\packages\leakage\src")
if _leak.is_dir() and str(_leak) not in sys.path:
    sys.path.insert(0, str(_leak))

from llm2.hunt.runner import DEFAULT_HORIZON, HuntConfig, run_nested_hunt
from llm2.paths import ARTIFACTS
from llm2.research_policy import stamp_min_size_equity_caveat
from llm2.validation.folds import FOLD_GEOMETRY_VERSION, OUTER_FOLD_RANGES

# Settled winners (lgbm_regressor) from structure_v1_eth_sol_settle_20260803T161346Z.
COMBOS = (
    ("ETHUSDT", "1h", "fwd_return"),
    ("ETHUSDT", "1h", "direction"),
    ("SOLUSDT", "1h", "fwd_return"),
    ("SOLUSDT", "1h", "direction"),
)


def _pick(gates: dict, *keys: str):
    for k in keys:
        if k in gates and gates[k] is not None:
            return gates[k]
    return None


def main() -> int:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = ARTIFACTS / "reports" / f"structure_v1_eth_sol_metrics_{stamp}.json"
    rows = []
    for i, (sym, tf, tgt) in enumerate(COMBOS):
        gid = f"metrics_struct2_{i:02d}_{sym}_{tf}_{tgt}_{stamp[:8]}"
        cfg = HuntConfig(
            generation_id=gid,
            symbol=sym,
            timeframe=tf,
            target=tgt,
            feature_space="structure_v1",
            horizon=DEFAULT_HORIZON[tgt],
            max_trials=1,
            seed=20260803 + i,
            run_backtest=True,
            run_surrogate_challenge=True,
            models=["lgbm_regressor"],
            tp_pct=0.01,
            sl_pct=0.02,
        )
        summary = run_nested_hunt(cfg)
        best = summary.get("best") or {}
        gates = best.get("gates") or {}
        row = {
            "symbol": sym,
            "timeframe": tf,
            "target": tgt,
            "model": best.get("model"),
            "generation_id": gid,
            "tier": best.get("tier") or summary.get("best_tier"),
            "overall": gates.get("overall"),
            "pooled_pf": best.get("pooled_pf"),
            "pooled_trades": best.get("pooled_trades"),
            "pooled_pnl": best.get("pooled_pnl"),
            "win_rate": best.get("win_rate"),
            "expectancy": best.get("expectancy"),
            "payoff": best.get("payoff"),
            "daily_mtm_sharpe": _pick(gates, "daily_mtm_sharpe_value"),
            "hac_sharpe": _pick(gates, "hac_sharpe_value"),
            "dsr": _pick(gates, "dsr_value"),
            "bootstrap_positive_frac": _pick(gates, "bootstrap_positive_frac_value"),
            "positive_fold_frac": _pick(gates, "positive_fold_frac_value"),
            "stress_pnl": _pick(gates, "stress_pnl_value"),
            "stress_pf": _pick(gates, "stress_pf_value"),
            "baseline_mdd": _pick(gates, "baseline_mdd_value"),
            "stress_mdd": _pick(gates, "stress_mdd_value"),
            "margin_utilization": _pick(gates, "margin_utilization_value"),
            "liquidation": gates.get("liquidation"),
            "pbo": gates.get("pbo"),
            "pbo_note": gates.get("pbo_note"),
            "fold_trades": gates.get("fold_trades"),
            "fold_pnls": gates.get("fold_pnls"),
            "fold_pfs": gates.get("fold_pfs"),
            "gates": gates,
            "n_folds": summary.get("n_folds"),
            "cost_hurdle": summary.get("cost_hurdle"),
            "break_even_p": summary.get("break_even_p"),
        }
        rows.append(row)
        print(
            f"{sym} {tgt}: PF={row['pooled_pf']:.4f} n={row['pooled_trades']} "
            f"Sharpe={row['daily_mtm_sharpe']} WR={row['win_rate']} overall={row['overall']}",
            flush=True,
        )

    payload = stamp_min_size_equity_caveat(
        {
            "stamped_utc": stamp,
            "fold_geometry": FOLD_GEOMETRY_VERSION,
            "outer_fold_ranges": OUTER_FOLD_RANGES,
            "readiness": "RESEARCH_ONLY",
            "note": (
                "Full numeric dump for settled ETH/SOL structure_v1 LightGBM regressor "
                "winners. Not a live authorization."
            ),
            "models": rows,
        }
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
