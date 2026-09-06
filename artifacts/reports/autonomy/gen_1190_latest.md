# Autonomy public-indicator hunt gen 1190

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T092058Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma650_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0745 | 0.7000 | 4.5580 | 0.0237 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma650_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9740 | 0.6839 | 4.2385 | 0.0224 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma650_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.9298 | 0.6735 | 3.8742 | 0.0139 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma650_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.8803 | 0.6736 | 3.6888 | 0.0131 | 0.3523 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma650_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.6194 | 0.6180 | 2.7131 | 0.0093 | 0.2809 | ok | RAN |
| SOLUSDT | 8 | `wma650_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5631 | 0.6108 | 2.6095 | 0.0088 | 0.2757 | ok | RAN |
| ETHUSDT | 8 | `wma650_above_at_h` | one_head_filter_pi_star | 168 | 13.8094 | 1.2084 | 0.6012 | 1.0478 | 0.0074 | 0.2143 | ok | RAN |
| ETHUSDT | 4 | `wma650_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.1551 | 0.5852 | 0.8093 | 0.0056 | 0.2102 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma650_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma650_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma650_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma650_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma650_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma650_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
