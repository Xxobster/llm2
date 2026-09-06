# Edge lab nested outer out-of-sample settle 002 (Average True Range brackets)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T024027Z`.
**Evidence class:** stitched outer out-of-sample union, 2022-01-01 to the forward lockbox at 2026-05-01. Selection was frozen from the pre-2022 inner screen, ranked by HAC Sharpe with a trade floor of 80, before these bars were scored.

Arms: 24 stitched. Clearing all gates: **0**.

> Total return, max drawdown and recovery factor are **not quotable** here: positions are minimum-exchange size against the research wallet, so drawdown lands near 0.02%. Profit factor, win rate, payoff, Sharpe, HAC Sharpe, Sortino, entry-bar rate and fill rate are scale-free.

| Symbol | TF | Event | Session | k_sl | r | n | /mo | PF | WR | Payoff | Sharpe | HAC | Sortino | ebr | fill% | folds+ | inner PF | gate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SOLUSDT | 1h | `fvg_bear_ob_bear_short` | all | 1.0 | 1.5 | 290 | 5.58 | 1.34 | 0.50 | 1.32 | 0.98 | 1.06 | 0.51 | 0.17 | 0.35 | 6/6 | 1.93 | fail: sharpe<1.0 |
| BTCUSDT | 1h | `sweep_prev_day_high` | all | 1.0 | 1.5 | 381 | 7.37 | 1.18 | 0.48 | 1.28 | 0.62 | 0.67 | 0.33 | 0.28 | 0.31 | 4/6 | 1.43 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,entry_bar>0.25,positive_folds<80% |
| BTCUSDT | 1h | `sweep_pdh_fvg_bear_short` | all | 1.0 | 1.5 | 242 | 4.70 | 1.16 | 0.50 | 1.18 | 0.47 | 0.48 | 0.20 | 0.23 | 0.32 | 3/6 | 1.67 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `fvg_bull_ce_tag` | no_weekend | 1.5 | 1.0 | 728 | 16.96 | 1.14 | 0.56 | 0.89 | 0.75 | 0.75 | 0.54 | 0.14 | 0.38 | 5/5 | 1.48 | fail: pf<1.2,sharpe<1.0 |
| ETHUSDT | 1h | `sweep_london_high` | no_weekend | 1.0 | 1.5 | 451 | 8.68 | 1.14 | 0.48 | 1.25 | 0.59 | 0.60 | 0.35 | 0.37 | 0.40 | 4/6 | 1.74 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,entry_bar>0.25,positive_folds<80% |
| ETHUSDT | 1h | `ob_bear_tap` | weekday_ny | 1.5 | 1.0 | 416 | 8.05 | 1.13 | 0.56 | 0.90 | 0.49 | 0.53 | 0.25 | 0.27 | 0.39 | 5/6 | 1.70 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,entry_bar>0.25 |
| SOLUSDT | 15m | `fvg_bull_ce_discount` | all | 1.5 | 1.0 | 598 | 13.97 | 1.09 | 0.56 | 0.87 | 0.49 | 0.48 | 0.31 | 0.16 | 0.39 | 3/5 | 1.42 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `ob_bull_tap` | all | 1.5 | 1.0 | 1103 | 21.20 | 1.09 | 0.55 | 0.87 | 0.55 | 0.52 | 0.43 | 0.28 | 0.34 | 4/6 | 1.25 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,entry_bar>0.25,positive_folds<80% |
| SOLUSDT | 1h | `ob_bear_tap` | no_weekend | 2.0 | 1.5 | 685 | 13.19 | 1.02 | 0.48 | 1.12 | 0.13 | 0.14 | 0.09 | 0.06 | 0.36 | 3/6 | 1.31 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 1h | `sweep_asia_high` | all | 1.5 | 1.5 | 516 | 9.92 | 1.00 | 0.48 | 1.09 | -0.01 | -0.01 | -0.00 | 0.10 | 0.35 | 2/6 | 1.55 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `fvg_bear_ce_tag` | weekday_ny | 1.5 | 1.5 | 245 | 5.71 | 0.98 | 0.41 | 1.40 | -0.06 | -0.06 | -0.03 | 0.08 | 0.38 | 1/5 | 1.69 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `sweep_prev_day_low` | no_weekend | 1.0 | 2.0 | 320 | 6.17 | 0.98 | 0.41 | 1.41 | -0.07 | -0.06 | -0.03 | 0.28 | 0.36 | 2/6 | 1.81 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,entry_bar>0.25,positive_folds<80% |
| SOLUSDT | 1h | `sweep_london_high` | no_weekend | 2.0 | 1.5 | 363 | 6.99 | 0.97 | 0.48 | 1.03 | -0.10 | -0.10 | -0.05 | 0.10 | 0.39 | 3/6 | 1.63 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `fvg_bull_with_structure` | all | 1.5 | 1.0 | 357 | 8.32 | 0.97 | 0.54 | 0.82 | -0.11 | -0.12 | -0.06 | 0.12 | 0.35 | 3/5 | 1.78 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bull_ce_tag` | all | 1.0 | 1.5 | 918 | 21.39 | 0.97 | 0.44 | 1.22 | -0.24 | -0.24 | -0.19 | 0.18 | 0.36 | 1/5 | 1.32 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 15m | `fvg_bear_ce_premium` | no_weekend | 1.5 | 1.0 | 420 | 9.78 | 0.95 | 0.53 | 0.85 | -0.26 | -0.28 | -0.13 | 0.12 | 0.33 | 2/5 | 1.51 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 15m | `fvg_bear_ob_bear_short` | no_weekend | 1.5 | 1.0 | 763 | 17.77 | 0.94 | 0.53 | 0.85 | -0.35 | -0.37 | -0.22 | 0.16 | 0.38 | 2/5 | 1.49 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `sweep_pdl_fvg_bull_long` | no_weekend | 2.0 | 1.0 | 199 | 3.86 | 0.94 | 0.55 | 0.77 | -0.17 | -0.16 | -0.05 | 0.14 | 0.36 | 3/6 | 2.20 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bear_ob_bear_short` | all | 1.5 | 1.0 | 977 | 22.76 | 0.92 | 0.54 | 0.78 | -0.57 | -0.58 | -0.40 | 0.16 | 0.36 | 2/5 | 1.56 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `fvg_bear_ce_premium` | no_weekend | 2.0 | 1.5 | 440 | 10.25 | 0.87 | 0.40 | 1.28 | -0.56 | -0.60 | -0.34 | 0.04 | 0.37 | 2/5 | 1.40 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `fvg_bull_ob_bull_long` | all | 1.0 | 1.5 | 941 | 21.90 | 0.84 | 0.42 | 1.16 | -1.18 | -1.15 | -0.92 | 0.18 | 0.39 | 2/5 | 1.27 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 1h | `fvg_bear_ob_bear_short` | all | 1.5 | 1.0 | 285 | 5.51 | 0.80 | 0.51 | 0.78 | -0.73 | -0.79 | -0.28 | 0.20 | 0.34 | 2/6 | 1.76 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `ignition_with_trend_long` | all | 1.5 | 2.0 | 397 | 9.28 | 0.79 | 0.36 | 1.43 | -1.06 | -1.01 | -0.62 | 0.22 | 1.00 | 0/5 | 1.55 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `ignition_long` | all | 2.0 | 1.0 | 668 | 15.61 | 0.77 | 0.47 | 0.85 | -1.44 | -1.50 | -0.90 | 0.19 | 1.00 | 0/5 | 1.40 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
