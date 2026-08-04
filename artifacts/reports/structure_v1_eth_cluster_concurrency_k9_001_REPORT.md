# ETH concurrency ladder K=1..9 (max 18 total)

**Maximum readiness:** `RESEARCH_ONLY`  
**Base arm:** `mean_strength|hold12|tp1%|sl2%`  
**K** = max books **per side**; both sides full → **2×K** (18 at K=9).

## Open ladder (always allow add-ons under cap)

| K | Max total | Profit Factor (PF) | Trades | Net PnL | Δ PF vs K=1 | Marginal Δ PF |
|---|-----------|--------------------|--------|---------|-------------|---------------|
| 1 | 2 | 3.21 | 2916 | 358 | — | — |
| 2 | 4 | 3.32 | 5862 | 724 | +0.11 | +0.11 |
| 3 | 6 | 3.53 | 7950 | 1014 | +0.32 | +0.21 |
| 4 | 8 | 3.77 | 9584 | 1264 | +0.56 | +0.24 |
| 5 | 10 | 3.89 | 10818 | 1450 | +0.68 | +0.12 |
| 6 | 12 | 3.99 | 11700 | 1587 | +0.78 | +0.10 |
| 7 | 14 | 4.07 | 12344 | 1690 | +0.87 | +0.08 |
| 8 | 16 | 4.12 | 12783 | 1762 | +0.92 | +0.05 |
| **9** | **18** | **4.16** | **13069** | **1809** | **+0.95** | **+0.04** |

## K=9 with cluster gate

| Arm | PF | Trades | Net PnL |
|-----|-----|--------|---------|
| k9_open | 4.16 | 13069 | **1809** |
| k9_cluster3 (≤3h) | **4.24** | 9226 | 1287 |
| k9_cluster6 (≤6h) | 4.16 | 11319 | 1570 |

## Takeaways

1. Scaling to **9 per side / 18 total** still helps vs K=1; PF and PnL rise monotonically on the open ladder.
2. **Diminishing returns** after ~K=4–5: each extra book adds less PF/PnL (K8→K9 only +0.04 PF / +47 USDT).
3. At K=9, a **3-hour cluster gate** lifts PF further (4.24) but cuts dollars vs always-open.
4. Cap skips at K=9 are nearly gone (fold skip_cap ~25–65) — most strength-filtered signals can be taken.

Still **RESEARCH_ONLY**. Min-exchange stacked books ≠ scale / margin readiness. Not a live pack change.

JSON: `structure_v1_eth_cluster_concurrency_k9_001_latest.json`
