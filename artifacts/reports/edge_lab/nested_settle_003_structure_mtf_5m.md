# Edge lab nested outer out-of-sample settle 003 (WaveTheory structure)

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T082234Z`.
Arms: 3 stitched. Clearing all gates: **0**.
Batch: 5-minute only (`settle_5m.sqlite`).

| Symbol | TF | Event | Session | k_sl | r | n | PF | HAC | ebr | folds+ | inner PF | gate |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BTCUSDT | 5m | `wt_htf_bias_pullback_short` | weekday_ny | 1.0 | 1.0 | 552 | 0.92 | -0.47 | 0.18 | 1/5 | 1.35 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 5m | `wt_htf_bias_pullback_long` | weekday_ny | 2.0 | 2.0 | 536 | 0.73 | -1.60 | 0.05 | 0/5 | 1.25 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
| ETHUSDT | 5m | `wt_hh_hl_continuation_long` | ny_am_kz_no_weekend | 1.5 | 1.0 | 283 | 0.71 | -1.46 | 0.17 | 1/5 | 1.44 | fail: pf<1.2,sharpe<1.0,hac_sharpe<0.75,positive_folds<80% |
