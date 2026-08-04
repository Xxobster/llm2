"""Re-apply prereg gate ranking to the latest ablation report (no re-sim)."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

PATH = Path("artifacts/reports/structure_v1_eth_switch_tp_ablation_001_latest.json")
PEAK_CAP = 12
N_TRADES_MIN = 200


def clean(r: pd.Series) -> dict:
    keys = [
        "label",
        "kind",
        "clarity",
        "switch_book",
        "addon_tp",
        "hold",
        "k",
        "n_trades",
        "net_pnl",
        "profit_factor",
        "win_rate",
        "max_drawdown",
        "peak_concurrent_all",
        "balance",
    ]
    out = {}
    for k in keys:
        if k not in r.index:
            out[k] = None
            continue
        v = r[k]
        if isinstance(v, (float, np.floating)):
            out[k] = float(v)
        elif isinstance(v, (int, np.integer)):
            out[k] = int(v)
        else:
            out[k] = v
    return out


def main() -> int:
    d = json.loads(PATH.read_text(encoding="utf-8"))
    rows = []
    for t in d["trials"]:
        pnl = float(t.get("net_pnl") or float("nan"))
        pf = float(t.get("profit_factor") or float("nan"))
        mdd = abs(float(t.get("max_drawdown") or 0.0))
        peak = float(t.get("peak_concurrent_all") or 0.0)
        n = float(t.get("n_trades") or 0.0)
        if not np.isfinite(pnl) or not np.isfinite(pf):
            continue
        if n < N_TRADES_MIN or peak > PEAK_CAP:
            continue
        rows.append({**t, "pnl_over_mdd": pnl / max(mdd, 1e-9)})
    df = pd.DataFrame(rows)
    df["r_pf"] = df["profit_factor"].rank(pct=True)
    df["r_pnl"] = df["net_pnl"].rank(pct=True)
    df["r_calmar"] = df["pnl_over_mdd"].rank(pct=True)
    df["balance"] = 0.4 * df["r_pf"] + 0.3 * df["r_pnl"] + 0.3 * df["r_calmar"]

    live = df[
        (df.clarity == "mean_strength")
        & (df.switch_book == 3)
        & np.isclose(df.addon_tp.astype(float), 0.02618)
        & (df.hold == 12)
        & (df.k == 7)
    ].iloc[0]
    ms = df[df.clarity == "mean_strength"].copy()
    dom = ms[
        (ms.balance > float(live.balance))
        & (ms.profit_factor >= float(live.profit_factor))
        & (ms.peak_concurrent_all <= PEAK_CAP)
    ].sort_values(["balance", "profit_factor"], ascending=False)

    if len(dom):
        best = dom.iloc[0]
        verdict = "CANDIDATE_LIVE_v1_2_LOCKBOX_ONLY"
        reason = (
            f"{best.label} beats live on balance+PF with peak<={PEAK_CAP} "
            f"(contaminated lockbox - micro revision only, not promotion)"
        )
        gate_pass = clean(best)
    else:
        best = ms.sort_values("balance", ascending=False).iloc[0]
        verdict = "KEEP_LIVE_eth_multitrade_v1_1"
        reason = "no mean_strength arm beats live on both balance and PF under peak cap"
        gate_pass = None

    ranking = {
        "n_eligible": int(len(df)),
        "peak_cap": PEAK_CAP,
        "n_trades_min": N_TRADES_MIN,
        "live_reference": clean(live),
        "best_overall_eligible": clean(
            df.sort_values("balance", ascending=False).iloc[0]
        ),
        "best_mean_strength_eligible": clean(
            ms.sort_values("balance", ascending=False).iloc[0]
        ),
        "best_gate_pass_mean_strength": gate_pass,
        "n_gate_pass_mean_strength": int(len(dom)),
        "top10": [
            clean(r)
            for _, r in df.sort_values("balance", ascending=False).head(10).iterrows()
        ],
        "verdict": verdict,
        "reason": reason,
        "gate_note": (
            "Prereg require_all: balance>live AND pf>=live AND peak<=12 AND mean_strength"
        ),
    }
    d["ranking"] = ranking
    PATH.write_text(json.dumps(d, indent=2, default=str) + "\n", encoding="utf-8")
    Path("artifacts/reports/structure_v1_eth_switch_tp_ablation_001_ranking.json").write_text(
        json.dumps(ranking, indent=2) + "\n", encoding="utf-8"
    )
    print("VERDICT", verdict)
    print("REASON", reason)
    print("n_gate_pass", len(dom))
    if gate_pass:
        print("gate_pass", gate_pass["label"], "pf", gate_pass["profit_factor"], "pnl", gate_pass["net_pnl"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
