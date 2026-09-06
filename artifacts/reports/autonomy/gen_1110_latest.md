# Autonomy public-indicator hunt gen 1110

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T001536Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma600_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0213 | 0.6952 | 4.4515 | 0.0235 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma600_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8147 | 0.6784 | 3.8871 | 0.0201 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma600_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.9454 | 0.6667 | 3.9595 | 0.0138 | 0.3532 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma600_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8534 | 0.6649 | 3.5989 | 0.0127 | 0.3613 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma600_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2937 | 0.6043 | 1.4931 | 0.0101 | 0.2246 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma600_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2795 | 0.6053 | 1.4651 | 0.0095 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `wma600_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5374 | 0.6201 | 2.4303 | 0.0084 | 0.2737 | ok | RAN |
| SOLUSDT | 8 | `wma600_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4980 | 0.6032 | 2.4152 | 0.0081 | 0.2698 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma600_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma600_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
