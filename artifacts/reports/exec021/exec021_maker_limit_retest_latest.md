# EXEC-021 maker-limit retest

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Engine tradesim 1.1.0.
Resting limit, first 1-minute touch is the fill, maker 0.02% on resting legs.
Take-profit/stop armed only after that fill. Not a Shadow-Ready stamp. Not a deploy.

Min-size Post-Only vote (not already live): **1** research names. Already-live names that still pass the same bar: **1**.

## Live (this project, currently authorized units)

| Id | Unit | n | /mo | PF | WR | ebr | fill | Sharpe | min-live? |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `live_dsr_eth_bounce_upper_1h` | llm2-dsr-eth-bu-1h | 502 | 9.659 | 1.034 | 0.462 | 0.171 | 0.323 | 0.156 | no |
| `live_dsr_sol_bounce_upper_1h` | llm2-dsr-sol-bu-1h | 488 | 9.396 | 0.997 | 0.436 | 0.250 | 0.327 | -0.012 | no |
| `live_pivot_eth_15m_1pct` | llm2-pivot-eth-p75-ctrl-atr-w4 | 373 | 30.344 | 1.007 | 0.558 | 0.142 | 0.384 | 0.060 | no |
| `live_pivot_sol_15m_1pct` | llm2-pivot-sol-geo-p75-w4 | 376 | 30.531 | 1.065 | 0.548 | 0.133 | 0.454 | 0.520 | no |
| `live_pivot_eth_15m_050` | llm2-pivot-eth-p50-tp05-sl05 | 407 | 33.110 | 1.252 | 0.609 | 0.553 | 0.384 | 2.075 | no_entry_bar_noise |
| `live_pivot_sol_15m_050` | llm2-pivot-sol-p50-tp05-sl05 | 401 | 32.561 | 1.275 | 0.601 | 0.509 | 0.454 | 2.376 | no_entry_bar_noise |
| `live_autonomy_376_sol_sma540` | llm2-autonomy-376-sol-sma540 | 188 | 15.373 | 1.114 | 0.574 | 0.149 | 0.464 | 0.657 | no |
| `live_autonomy_705_eth_ema1320` | llm2-autonomy-705-eth-ema1320 | 264 | 21.566 | 1.108 | 0.568 | 0.152 | 0.375 | 0.730 | no |
| `live_autonomy_013_sol_atrrel` | llm2-autonomy-013-sol-atrrel | 70 | 5.832 | 1.436 | 0.586 | 0.071 | 0.444 | 1.329 | yes_min_size_limit_only |

## Research / not currently live

| Id | n | /mo | PF | WR | ebr | fill | Sharpe | min-live? |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `dsr_btc_confluence_bounce_long_1h` | 304 | 5.876 | 1.053 | 0.553 | 0.128 | 0.363 | 0.180 | no |
| `dsr_btc_channel_walk_long_1h` | 676 | 12.990 | 0.993 | 0.516 | 0.139 | 0.317 | -0.038 | no |
| `dsr_btc_bounce_lower_1h` | 522 | 10.031 | 0.922 | 0.521 | 0.130 | 0.332 | -0.360 | no |
| `dsr_btc_bounce_upper_1h` | 440 | 8.466 | 0.856 | 0.498 | 0.139 | 0.295 | -0.658 | no |
| `dsr_eth_bounce_lower_1h` | 506 | 9.760 | 0.772 | 0.413 | 0.170 | 0.350 | -1.226 | no |
| `dsr_btc_confluence_bounce_short_1h` | 256 | 4.926 | 0.954 | 0.539 | 0.141 | 0.286 | -0.149 | no |
| `dsr_eth_channel_walk_short_1h` | 940 | 18.061 | 0.997 | 0.456 | 0.155 | 0.323 | -0.020 | no |
| `dsr_eth_channel_walk_long_1h` | 673 | 12.982 | 0.837 | 0.422 | 0.183 | 0.324 | -0.972 | no |
| `dsr_sol_confluence_bounce_short_15m` | 778 | 22.939 | 0.893 | 0.501 | 0.069 | 0.379 | -0.762 | no |
| `pivot_btc_15m_1pct` | 28 | 2.372 | 0.876 | 0.429 | 0.036 | 0.429 | -0.288 | no |
| `sol_1h_power_ema_stack_long` | 669 | 12.985 | 1.231 | 0.484 | 0.063 | 0.332 | 1.172 | yes_min_size_limit_only |
| `btc_4h_power_ema_stack_long` | 187 | 3.676 | 0.965 | 0.444 | 0.118 | 0.252 | -0.095 | no |
| `inner004_SOLUSDT_4h_power_ema_stack_long` | 130 | 9.667 | 1.102 | 0.415 | 0.400 | 0.456 | 0.442 | no_inner_only |
| `inner004_ETHUSDT_4h_power_ema_stack_long` | 168 | 7.114 | 1.487 | 0.554 | 0.190 | 0.293 | 1.503 | no_inner_only |
| `inner004_SOLUSDT_4h_mix_turtle_hurst` | 117 | 7.664 | 0.988 | 0.436 | 0.513 | 0.518 | -0.055 | no_inner_only |
| `inner004_ETHUSDT_15m_power_vol_expand` | 38 | 1.581 | 5.076 | 0.632 | 0.132 | 0.340 | 1.666 | no_inner_only |
| `inner004_ETHUSDT_1h_power_ema_stack_long` | 445 | 17.905 | 1.146 | 0.499 | 0.065 | 0.349 | 0.694 | no_inner_only |
| `inner004_SOLUSDT_1h_mix_turtle_hurst` | 337 | 21.663 | 0.919 | 0.401 | 0.196 | 0.433 | -0.576 | no_inner_only |
| `inner004_BTCUSDT_4h_surf_linreg_channel` | 17 | 1.103 | 1.328 | 0.529 | 0.235 | 0.333 | 0.458 | no_inner_only |
| `inner005_SOLUSDT_1h_wick_reject_follow` | 53 | 3.482 | 0.838 | 0.377 | 0.170 | 0.376 | -0.509 | no_inner_only |
| `inner005_SOLUSDT_4h_cvd_slope` | 684 | 43.953 | 1.095 | 0.425 | 0.386 | 0.444 | 0.933 | no_inner_only |
| `inner005_ETHUSDT_4h_cvd_slope` | 595 | 23.653 | 1.092 | 0.467 | 0.212 | 0.284 | 0.607 | no_inner_only |
| `inner005_SOLUSDT_15m_wick_reject_follow` | 141 | 9.122 | 0.968 | 0.362 | 0.085 | 0.390 | -0.146 | no_inner_only |
| `inner006_SOLUSDT_4h_outside_bar_follow` | 122 | 7.840 | 1.204 | 0.410 | 0.352 | 0.451 | 0.697 | no_inner_only |
| `inner006_SOLUSDT_4h_close_streak_fade` | 53 | 3.406 | 1.341 | 0.434 | 0.528 | 0.477 | 0.818 | no_inner_only |
| `inner006_SOLUSDT_1h_close_streak_fade` | 146 | 9.382 | 0.758 | 0.356 | 0.192 | 0.429 | -1.305 | no_inner_only |
| `inner006_BTCUSDT_4h_macd_hist_cross` | 63 | 2.301 | 1.106 | 0.444 | 0.111 | 0.194 | 0.209 | no_inner_only |
| `inner006_SOLUSDT_1h_utc_vwap_reclaim` | 295 | 18.957 | 1.083 | 0.441 | 0.088 | 0.330 | 0.528 | no_inner_only |
| `inner006_ETHUSDT_4h_close_streak_follow` | 50 | 2.087 | 1.882 | 0.540 | 0.240 | 0.299 | 1.020 | no_inner_only |
