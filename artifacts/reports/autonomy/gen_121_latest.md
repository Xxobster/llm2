# Autonomy public-indicator hunt gen 121

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T172530Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema9_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1219 | 0.7128 | 4.5471 | 0.0266 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema9_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7923 | 0.6787 | 3.8100 | 0.0203 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema9_below_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 2.2133 | 0.6821 | 3.9769 | 0.0187 | 0.4437 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema9_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema9_cross_up` | one_head_filter_pi_star | 196 | 16.0114 | 1.4213 | 0.6276 | 2.1470 | 0.0124 | 0.3163 | ok | RAN |
| SOLUSDT | 8 | `ema9_cross_up` | one_head_filter_pi_star | 59 | 4.8341 | 1.8047 | 0.6780 | 1.6674 | 0.0122 | 0.4068 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema9_above_at_h` | one_head_filter_pi_star | 122 | 10.0676 | 1.3044 | 0.6148 | 1.1886 | 0.0106 | 0.2459 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema9_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.2299 | 0.5951 | 1.0538 | 0.0074 | 0.2025 | ok | RAN |
| SOLUSDT | 8 | `ema9_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3900 | 0.5968 | 2.0188 | 0.0063 | 0.2634 | ok | RAN |
| SOLUSDT | 4 | `ema9_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3705 | 0.5953 | 2.0004 | 0.0055 | 0.2465 | ok | RAN |
| ETHUSDT | 8 | `ema9_cross_down` | one_head_filter_pi_star | 104 | 8.6200 | 1.1767 | 0.5962 | 0.6746 | 0.0053 | 0.1731 | ok | RAN |
| SOLUSDT | 8 | `ema9_cross_down` | one_head_filter_pi_star | 150 | 12.2317 | 1.3075 | 0.5933 | 1.4115 | 0.0045 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema9_cross_down` | one_head_filter_pi_star | 11 | 1.1069 | 0.6135 | 0.4545 | -0.6140 | -0.0113 | 0.0909 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema9_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.6425 | 0.3571 | -0.6474 | -0.0361 | 0.0714 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema9_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema9_cross_down` | one_head_filter_pi_star | 16 | 1.3616 | 0.4075 | 0.2500 | -1.2442 | -0.0563 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema9_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema9_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema9_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema9_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema9_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema9_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema9_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema9_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
