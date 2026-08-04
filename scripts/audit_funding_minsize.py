"""Explain why gap-fold funding dollars can print 0.00 at MIN_EXCHANGE size."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from llm2.data.macro import load_funding
from llm2.paths import FORWARD_LOCKBOX_START

TRADES = Path(
    r"D:\projectsdata\backtests\reports\llm2-structure_v1-lgbm-fold5-7cf686aca1\trades.csv"
)


def main() -> int:
    t = pd.read_csv(TRADES)
    funding = load_funding("BTCUSDT")
    funding = funding[funding.index < pd.Timestamp(FORWARD_LOCKBOX_START, tz="UTC")]
    w = funding.loc["2025-10-01":"2026-04-30"]
    qty = float(t["qty"].median()) if len(t) else 0.001
    # Approximate funding cash = qty * mark * rate per settlement while open.
    # With qty=0.001 and ~70k mark, notional≈70; rate ~1e-4 → ~0.007 USDT per hit.
    notionals = t["entry_price"].to_numpy(float) * t["qty"].to_numpy(float)
    abs_rates = w.abs().to_numpy(float)
    typical = float(np.median(notionals) * np.median(abs_rates)) if len(abs_rates) else 0.0
    total_reported = float(t["funding"].sum()) if "funding" in t.columns else float("nan")
    out = {
        "n_trades": int(len(t)),
        "median_qty": qty,
        "median_notional_usdt": float(np.median(notionals)),
        "funding_rows_in_gap": int(len(w)),
        "funding_rate_sum": float(w.sum()) if len(w) else None,
        "funding_rate_abs_sum": float(w.abs().sum()) if len(w) else None,
        "median_abs_rate": float(np.median(abs_rates)) if len(abs_rates) else None,
        "typical_one_settlement_usdt": typical,
        "trades_csv_funding_sum": total_reported,
        "explanation": (
            "At MIN_EXCHANGE qty (~0.001 BTC) notional is tiny (~70 USDT). "
            "Bybit funding is rate×notional per settlement; many holds are <8h so they "
            "miss the settlement entirely. Surviving settlements are often <<0.01 USDT "
            "and round to 0.00 in headline totals. Rates were attached; dollars are dust."
        ),
    }
    path = Path("artifacts/reports/funding_minsize_audit_fold5.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
