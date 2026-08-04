# ETH size-double on ≤3h cluster (K=3..9)

**Maximum readiness:** `RESEARCH_ONLY`  
**Protocol:** fold V2 walk-forward, ETHUSDT 1h direction only, lockbox excluded (no future peek)  
**Base arm:** `mean_strength|hold12|tp1%|sl2%`  
**Rule:** if signal ≤ **3 hours** after last same-side entry → qty = **2×** min-exchange; else **1×**. Concurrent books K=3..9.

## Stitched outer results

| K | Max total | Flat 1× PF | Double-3h PF | Δ PF | Flat PnL | Double PnL | Δ PnL |
|---|-----------|------------|--------------|------|----------|------------|-------|
| 3 | 6 | 3.53 | 3.69 | +0.16 | 1014 | 1537 | +523 |
| 4 | 8 | 3.77 | 3.97 | +0.20 | 1264 | 2021 | +757 |
| 5 | 10 | 3.89 | 4.11 | +0.23 | 1450 | 2394 | +944 |
| 6 | 12 | 3.99 | 4.23 | +0.24 | 1587 | 2672 | +1085 |
| 7 | 14 | 4.07 | 4.32 | +0.25 | 1690 | 2884 | +1194 |
| 8 | 16 | 4.12 | 4.38 | +0.26 | 1762 | 3034 | +1273 |
| **9** | **18** | **4.16** | **4.43** | **+0.27** | **1809** | **3133** | **+1324** |

Double-within-3h beats flat 1× on **Profit Factor and PnL at every K (7/7)**.

## Notes

- Same trade count as flat 1× at each K (size changes, not entry count).
- Roughly half of emissions are 2× (clustered).
- Min-exchange / 2× stacking is **not** scale or liquidation evidence.
- Not a live pack change.

JSON: `structure_v1_eth_cluster_size_double_k3_9_001_latest.json`
