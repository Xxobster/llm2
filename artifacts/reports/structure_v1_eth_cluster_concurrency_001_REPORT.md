# ETH cluster concurrency (2nd / 3rd book)

**Maximum readiness:** `RESEARCH_ONLY`  
**Base arm (frozen):** `mean_strength|hold12|tp1%|sl2%`  
**Question:** when several signals arrive close together, does opening a 2nd/3rd concurrent min-size book help?

## Stitched outer Profit Factor (PF) — fold V2

| Arm | K | Cluster window | PF | Trades | Net PnL | Δ PF vs K=1 |
|-----|---|----------------|-----|--------|---------|-------------|
| k1_baseline | 1 | — | 3.21 | 2916 | 358 | — |
| k2_open | 2 | always | 3.32 | 5862 | 724 | +0.11 |
| k3_open | 3 | always | 3.53 | 7950 | **1014** | +0.32 |
| **k3_cluster3** | 3 | **3 hours** | **3.61** | 6572 | 847 | **+0.41** |
| k3_cluster6 | 3 | 6 hours | 3.58 | 7011 | 901 | +0.38 |

Best Profit Factor: **k3_cluster3** (add 2nd/3rd book only if the new signal is within 3 hours of the previous same-side entry).  
Best dollars (min-exchange): **k3_open** (always stack up to 3).

## How it works

1. Keep the frozen strength filter + Take Profit 1% + hold 12.
2. If a book is already open on that side and another signal fires:
   - **open:** take it until K books are open;
   - **cluster3 / cluster6:** take it only if it is within 3h / 6h of the last entry on that side.
3. Simulator: `research_sim_hedge` for K>1 (independent Take Profit / Stop Loss per book).

## Caveats

- Signal-gate lifecycle uses **max-hold only** (conservative vs early Take Profit / Stop Loss exits).
- K=1 here is not identical to gen-1 emit-all single-book (gen-1 stitched PF≈3.32); compare arms **inside this table**.
- Min-exchange concurrent PnL is **not** scale / margin evidence.
- Not a live pack change; Xxobster8 already runs a different multitrade pack (K=7 + fib book3+).

JSON: `structure_v1_eth_cluster_concurrency_001_latest.json`
