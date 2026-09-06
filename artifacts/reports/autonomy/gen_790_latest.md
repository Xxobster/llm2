# Autonomy public-indicator hunt gen 790

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T144554Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma400_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.9541 | 0.6940 | 4.2665 | 0.0228 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma400_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9079 | 0.6911 | 4.1354 | 0.0221 | 0.3822 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma400_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2278 | 0.6988 | 4.1668 | 0.0168 | 0.3675 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma400_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.1559 | 0.6906 | 4.2791 | 0.0166 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma400_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2746 | 0.6043 | 1.4213 | 0.0094 | 0.2193 | ok | RAN |
| ETHUSDT | 4 | `wma400_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2668 | 0.6022 | 1.3585 | 0.0092 | 0.2312 | ok | RAN |
| SOLUSDT | 4 | `wma400_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4208 | 0.6000 | 2.1207 | 0.0065 | 0.2650 | ok | RAN |
| SOLUSDT | 8 | `wma400_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3477 | 0.5950 | 1.8199 | 0.0055 | 0.2600 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma400_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0204 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma400_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
