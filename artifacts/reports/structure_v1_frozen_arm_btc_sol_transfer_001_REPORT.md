# Frozen-arm transfer: BTCUSDT + SOLUSDT

**Maximum readiness:** `RESEARCH_ONLY`  
**Evidence class:** frozen-arm symbol transfer, fold V2 stitched outer out-of-sample (OOS)  
**Selection:** frozen from ETH gen-1 — **no re-rank** on BTC/SOL  
**Arm:** `mean_strength|hold12|tp1%` vs control `none|hold6|tp1%` (Stop Loss 2%)

## Stitched outer Profit Factor (PF)

| Symbol | Target | Frozen PF | Control PF | Δ PF | Beats |
|--------|--------|-----------|------------|------|-------|
| ETHUSDT | direction | 3.32 | 1.99 | +1.34 | yes (gen-1 ref) |
| BTCUSDT | direction | 2.94 | 1.90 | +1.04 | yes |
| BTCUSDT | fwd_return | **2.86** | 2.03 | +0.83 | yes (live target) |
| SOLUSDT | direction | **2.66** | 1.94 | +0.72 | yes (live target) |
| SOLUSDT | fwd_return | 1.90 | 1.51 | +0.38 | yes |

Live-matching packs: BTC = `fwd_return`, SOL = `direction` — both transfer successfully under this execution-grid protocol.

## Notes

- Lockbox not used. No new Take Profit / Stop Loss search.
- Not a full V2.1 gate settle; not live-pack authorization.
- Min-exchange equity / Maximum Drawdown (MDD) is not scale evidence.
- Official settle proxies remain: ETH direction ≈1.77, SOL direction ≈1.86, BTC settle from structure_v1_lgbm path.

JSON: `structure_v1_frozen_arm_btc_sol_transfer_001_latest.json`
