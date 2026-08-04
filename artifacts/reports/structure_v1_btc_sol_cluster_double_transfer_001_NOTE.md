# Track 2 transfer winners (RESEARCH_ONLY) — full hedge settle deferred

**generation:** `structure_v1_btc_sol_cluster_double_transfer_001`  
**evidence_class:** frozen geometry transfer fold-V2  
**lockbox:** not used (hard end 2026-05-01)  
**max readiness:** `RESEARCH_ONLY` — not a V2.1 full-gate settle pack freeze

## Result (stitched outer PF)

| Symbol | Target | control (hold6) | k1_clarity | k5_double3h | beats control |
|---|---|---:|---:|---:|---|
| BTCUSDT | fwd_return | 2.03 | 2.86 | **3.89** | k1 + k5 |
| SOLUSDT | direction | 1.94 | 2.66 | **3.36** | k1 + k5 |

`k5_double3h` wins on both symbols with bootstrap pos-exp ≥ 0.90 and no liquidations.

## Policy

- No re-ranking of K on BTC/SOL.
- Hedge concurrency settle (stress, MTM Sharpe, DSR, pack freeze) is **separate work**
  if promoting beyond single-book clarity.
- Track 1 already full-settled single-book `mean_strength|hold12|tp1%` for BTC/ETH/SOL
  under V2.1; that is the primary promotion path for Xxobster7 single-book swaps.

## Next

Separate OUTER_SETTLE prereg for hedge `k5_double3h` only after single-book pack
swap auth decision; do not open lockbox for selection.
