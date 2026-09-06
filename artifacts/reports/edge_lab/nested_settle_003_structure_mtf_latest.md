# Edge lab nested outer out-of-sample settle 003 (WaveTheory structure)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T082234Z`.
Arms: 24 stitched. Clearing all gates: **0**.
Combined 24 frozen hunt-003 survivors. 5-minute scored in a separate SQLite file.

| Symbol | TF | Event | Session | k_sl | r | n | PF | HAC | ebr | folds+ | inner PF | gate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ETHUSDT | 1h | `wt_htf_bias_pullback_long` | no_weekend | 1.5 | 1.0 | 203 | 1.37 | 0.91 | 0.20 | 5/6 | 1.66 | fail: sharpe<1.0 |
| ETHUSDT | 4h | `wt_pullback_short` | all | 2.0 | 2.0 | 179 | 1.20 | 0.50 | 0.10 | 4/6 | 1.35 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `wt_pullback_long` | all | 1.5 | 1.0 | 933 | 1.08 | 0.50 | 0.21 | 5/6 | 1.20 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75 |
| SOLUSDT | 1h | `wt_pullback_short` | no_weekend | 1.0 | 2.0 | 686 | 1.03 | 0.20 | 0.19 | 4/6 | 1.22 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 1h | `wt_pullback_confirmed_short` | all | 2.0 | 1.5 | 402 | 1.02 | 0.08 | 0.06 | 4/6 | 1.45 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `wt_pullback_short` | all | 1.5 | 1.0 | 2776 | 0.94 | -0.69 | 0.13 | 1/5 | 1.24 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `wt_bas_break_short` | no_weekend | 1.5 | 2.0 | 809 | 0.94 | -0.40 | 0.09 | 2/6 | 1.22 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `wt_lh_ll_continuation_short` | all | 1.5 | 1.0 | 872 | 0.94 | -0.43 | 0.14 | 2/5 | 1.80 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 1h | `wt_pullback_confirmed_short` | no_weekend | 1.5 | 1.0 | 320 | 0.92 | -0.31 | 0.17 | 3/6 | 1.28 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `wt_lh_ll_continuation_short` | no_weekend | 1.0 | 1.5 | 616 | 0.92 | -0.42 | 0.20 | 1/5 | 1.32 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `wt_hh_hl_continuation_long` | no_weekend | 1.5 | 1.0 | 723 | 0.92 | -0.52 | 0.11 | 2/5 | 1.26 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 5m | `wt_htf_bias_pullback_short` | weekday_ny | 1.0 | 1.0 | 552 | 0.92 | -0.47 | 0.18 | 1/5 | 1.35 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `wt_pullback_confirmed_short` | all | 1.5 | 1.0 | 1340 | 0.92 | -0.64 | 0.12 | 0/5 | 1.25 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 15m | `wt_pullback_short` | ny_am_kz_no_weekend | 2.0 | 1.0 | 398 | 0.91 | -0.42 | 0.17 | 2/5 | 1.30 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 15m | `wt_hh_hl_continuation_long` | weekday_ny | 1.5 | 2.0 | 273 | 0.89 | -0.45 | 0.12 | 1/5 | 1.40 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 15m | `wt_htf_bias_pullback_long` | all | 1.5 | 1.0 | 929 | 0.89 | -0.80 | 0.12 | 1/5 | 1.21 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| SOLUSDT | 1h | `wt_pullback_long` | weekday_ny | 1.5 | 1.5 | 361 | 0.89 | -0.45 | 0.09 | 2/6 | 1.32 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 1h | `wt_bas_break_short` | no_weekend | 2.0 | 1.5 | 717 | 0.88 | -0.80 | 0.06 | 2/6 | 1.35 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `wt_lh_ll_continuation_short` | no_weekend | 1.0 | 1.5 | 206 | 0.82 | -0.58 | 0.27 | 1/6 | 1.50 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,entry_bar>0.25,positive_folds<80% |
| BTCUSDT | 15m | `wt_lh_ll_continuation_short` | weekday_ny | 1.5 | 1.0 | 270 | 0.82 | -0.70 | 0.20 | 2/5 | 1.44 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 1h | `wt_top_break_long` | ny_am_kz_no_weekend | 2.0 | 1.0 | 247 | 0.73 | -1.05 | 0.13 | 2/6 | 1.29 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 5m | `wt_htf_bias_pullback_long` | weekday_ny | 2.0 | 2.0 | 536 | 0.73 | -1.60 | 0.05 | 0/5 | 1.25 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 5m | `wt_hh_hl_continuation_long` | ny_am_kz_no_weekend | 1.5 | 1.0 | 283 | 0.71 | -1.46 | 0.17 | 1/5 | 1.44 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| BTCUSDT | 15m | `wt_htf_bias_pullback_long` | weekday_ny | 1.5 | 1.0 | 291 | 0.69 | -1.45 | 0.23 | 1/5 | 1.37 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
