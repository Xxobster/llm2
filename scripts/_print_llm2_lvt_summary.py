import json
from pathlib import Path

s = json.loads(
    Path("artifacts/reports/llm2_accounts_live_vs_bt/summary_latest.json").read_text(
        encoding="utf-8"
    )
)
for r in s:
    if r.get("error"):
        print(r)
        continue
    ec = r["entry_comparison"]
    lm, bm = r["live_metrics"], r["backtest_metrics"]
    pf = bm["profit_factor_raw"]
    pf_s = "inf" if pf == float("inf") else (f"{pf:.3f}" if pf == pf else "nan")
    wr = bm["win_rate"]
    wr_s = f"{wr * 100:.1f}" if wr == wr else "nan"
    print(f"{r['account']:12s} {r['label']:20s} {r['symbol']} {r['timeframe']}")
    print(
        f"  LIVE forced n={lm['n_trades']} PF={lm['profit_factor_raw']:.3f} "
        f"WR={lm['win_rate'] * 100:.1f}% net={lm['net_pnl']:.3f}"
    )
    print(f"  FREE BT     n={bm['n_trades']} PF={pf_s} WR={wr_s}% net={bm['net_pnl']:.3f}")
    print(
        f"  entry_bars both={ec['intersection']}/{ec['n_live_entries']} "
        f"live_only={ec['live_only_n']} bt_only={ec['bt_only_n']}"
    )
    if ec.get("live_only_utc"):
        print(f"  live_only bars: {ec['live_only_utc'][:8]}")
    print(f"  live_run {lm['run_id']}")
    print(f"  bt_run   {bm['run_id']}")
    print()
