# Edge lab nested outer out-of-sample settle 001

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T230634Z`.
**Evidence class:** stitched outer out-of-sample union, 2022-01-01 to the forward lockbox at 2026-05-01. Selection was frozen from the pre-2022 inner screen before these bars were scored.

Arms: 12 stitched. Clearing all gates: **0**.

> Total return, max drawdown and recovery factor are **not quotable** here: positions are minimum-exchange size against the research wallet, so exposure runs a few percent and drawdown lands near 0.02%. Profit factor, win rate, payoff, Sharpe, HAC Sharpe, Sortino and entry-bar rate are scale-free.

| Symbol | TF | Event | Session | TP | SL | n | /mo | PF | WR | Payoff | Sharpe | HAC | Sortino | ebr | fill% | folds+ | gate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SOLUSDT | 15m | `sweep_pdh_fvg_bear_short` | all | 0.02 | 0.01 | 361 | 8.43 | 1.14 | 0.45 | 1.40 | 0.54 | 0.55 | 0.32 | 0.09 | 0.40 | 3/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `fvg_bear_ce_premium` | no_weekend | 0.015 | 0.01 | 447 | 10.41 | 1.12 | 0.47 | 1.26 | 0.52 | 0.53 | 0.33 | 0.12 | 0.37 | 3/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `sweep_prev_day_high` | all | 0.02 | 0.01 | 682 | 15.93 | 1.04 | 0.45 | 1.27 | 0.23 | 0.25 | 0.16 | 0.09 | 0.41 | 2/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 15m | `sweep_prev_day_high` | weekday_ny | 0.01 | 0.0075 | 235 | 5.52 | 1.01 | 0.48 | 1.09 | 0.04 | 0.04 | 0.02 | 0.08 | 0.48 | 2/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `sweep_asia_high` | all | 0.02 | 0.01 | 590 | 11.39 | 1.01 | 0.43 | 1.32 | 0.04 | 0.04 | 0.03 | 0.20 | 0.38 | 3/6 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bear_ob_bear_short` | no_weekend | 0.01 | 0.01 | 660 | 15.38 | 0.97 | 0.51 | 0.93 | -0.16 | -0.15 | -0.10 | 0.10 | 0.38 | 2/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bull_ce_tag` | weekday_ny | 0.015 | 0.01 | 244 | 5.69 | 0.95 | 0.50 | 0.94 | -0.17 | -0.17 | -0.07 | 0.07 | 0.42 | 2/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 1h | `sweep_pdl_fvg_bull_long` | all | 0.02 | 0.01 | 242 | 4.66 | 0.90 | 0.47 | 1.02 | -0.30 | -0.30 | -0.13 | 0.13 | 0.33 | 3/6 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bear_with_structure` | no_weekend | 0.01 | 0.0075 | 239 | 5.57 | 0.85 | 0.45 | 1.03 | -0.57 | -0.57 | -0.26 | 0.05 | 0.33 | 2/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bull_ob_bull_long` | weekday_ny | 0.01 | 0.01 | 288 | 6.73 | 0.82 | 0.50 | 0.83 | -0.73 | -0.68 | -0.31 | 0.16 | 0.48 | 1/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `ignition_with_trend_long` | all | 0.02 | 0.01 | 379 | 8.86 | 0.81 | 0.37 | 1.38 | -0.90 | -0.88 | -0.53 | 0.09 | 1.00 | 1/5 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 1h | `fvg_bear_ob_bear_short` | all | 0.015 | 0.01 | 271 | 5.24 | 0.72 | 0.44 | 0.91 | -1.01 | -1.00 | -0.41 | 0.13 | 0.34 | 2/6 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
