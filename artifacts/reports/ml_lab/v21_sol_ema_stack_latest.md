# V2.1 remainder — Solana 1-hour EMA stack

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T042404Z`.
Frozen name only. No Exponential Moving Average / efficiency-ratio / stop search.
Deflated Sharpe Ratio trial count = **449** (hunt-004 event-study rows).
Probability of Backtest Overfitting: unavailable (single frozen arm).

**Overall V2.1 blocking:** **FAIL**.

| Gate | Status | Value |
|---|---|---|
| outer_folds | PASS | 6 |
| trades_per_fold | PASS | 79 |
| pooled_trades | PASS | 683 |
| pooled_pf | PASS | 1.3566 |
| daily_mtm_sharpe | PASS | 1.3358 |
| hac_sharpe | PASS | 1.1603 |
| dsr | PASS | 1.0000 |
| bootstrap_positive_frac | PASS | 1.0000 |
| positive_fold_frac | PASS | 1.0000 |
| stress_pnl | FAIL | -24.0120 |
| stress_pf | FAIL | 0.8528 |
| baseline_mdd | PASS | 0.0004 |
| stress_mdd | PASS | 0.0024 |
| margin_utilization | PASS | 0.0004 |
| liquidation | PASS |  |
| pbo | UNKNOWN | PBO_UNAVAILABLE_INSUFFICIENT_MATRIX |

### Headline (baseline working-limit, all-taker fee book)

- Trades: 683  (**13.256 per month**)
- Profit factor: 1.357
- Win rate: 0.507
- Entry-bar exit rate: 0.091
- Fill rate: 0.332
- Fees: 6.323  Funding: -0.786

### Deflated Sharpe Ratio sensitivity (same daily returns)

| n_trials | DSR |
|---:|---:|
| 1 | 1.0000 |
| 2 | 1.0000 |
| 9 | 1.0000 |
| 30 | 1.0000 |
| 449 | 1.0000 |

### Moderate stress (all-taker fills + 2× slippage)

- Trades: 1145  (22.183 / month)
- Net PnL: -24.012
- Profit factor: 0.853
- Liquidations: 0
