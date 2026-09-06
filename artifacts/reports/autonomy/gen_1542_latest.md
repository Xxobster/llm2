# Autonomy public-indicator hunt gen 1542

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T064432Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma418_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.1160 | 0.7081 | 4.6359 | 0.0253 | 0.3838 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma418_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9548 | 0.6973 | 4.3162 | 0.0225 | 0.3892 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma418_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2424 | 0.6966 | 4.4447 | 0.0174 | 0.3933 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma418_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1706 | 0.6932 | 4.2184 | 0.0168 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma418_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2976 | 0.6087 | 1.4803 | 0.0100 | 0.2174 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma418_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2361 | 0.5969 | 1.2390 | 0.0081 | 0.2147 | ok | RAN |
| SOLUSDT | 8 | `wma418_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4070 | 0.6042 | 2.0298 | 0.0063 | 0.2604 | ok | RAN |
| SOLUSDT | 4 | `wma418_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.2984 | 0.5888 | 1.5536 | 0.0048 | 0.2640 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma418_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma418_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma418_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma418_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma418_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma418_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
