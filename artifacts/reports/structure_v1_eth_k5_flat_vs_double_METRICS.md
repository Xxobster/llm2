# ETH K=5: flat 1× vs double-within-3h — full metrics

**Period:** fold-V2 stitched outer OOS ≈ 2021-12-29 → 2026-04-30 (lockbox excluded)  
**Base:** `mean_strength|hold12|tp1%|sl2%` · **K=5** (max 10 books both sides)  
**Double rule:** qty = 2× min-exchange if signal ≤3h after last same-side entry, else 1×  
**Finplot trade overlay:** last **600** trades (= 5× usual lockbox cap of 120)

| Metric | Flat 1× | Double ≤3h | Delta (d−f) |
|--------|---------|------------|-------------|
| Trades | 10819 | 10819 | 0 |
| Longs / Shorts | 5726 / 5093 | 5726 / 5093 | 0 |
| Profit Factor | **3.893** | **4.119** | **+0.226** |
| Net PnL (USDT) | **1451.15** | **2395.27** | **+944.12** |
| Win rate | 83.94% | 83.94% | 0 |
| WR Wilson 95% | [83.24%, 84.62%] | [83.24%, 84.62%] | — |
| Long WR / Short WR | 83.23% / 84.74% | 83.23% / 84.74% | 0 |
| Expectancy USDT/trade | 0.134 | 0.221 | +0.087 |
| Payoff ratio | 0.745 | 0.788 | +0.043 |
| Avg win / avg loss | 0.215 / −0.289 | 0.348 / −0.442 | size scales |
| Fees | 294.81 | 473.30 | +178.49 |
| Slippage | 134.53 | 215.98 | +81.45 |
| Funding | 0.00 | 0.00 | 0 |
| Max drawdown (USDT) | 4.51 | 8.36 | +3.85 |
| Max drawdown % (wallet) | 0.041% | 0.073% | +0.031pp |
| MDD duration (days) | 9.08 | 9.46 | +0.38 |
| Sharpe daily raw | 0.924 | 0.899 | −0.025 |
| Sharpe annualised | 17.66 | 17.18 | −0.48 |
| Sharpe HAC ann. | 12.12 | 12.19 | +0.07 |
| Sortino annualised | 22.20 | 20.17 | −2.02 |
| Exposure | 50.66% | 50.66% | 0 |
| Entry-bar exits | 2216 (20.5%) | 2216 (20.5%) | 0 |
| Liquidations | 0 | 0 | 0 |
| Signals emitted | 10886 | 10886 | 0 |
| of which size 2× | 0 | 6605 | — |

**Read:** same trades and win rate; double increases size on clustered entries → higher PnL/PF and higher fees/slip/MDD dollars. Wallet MDD% stays tiny under min-exchange + oversized research wallet (not scale evidence).

JSON: `structure_v1_eth_k5_flat_vs_double_metrics.json`
