# Autonomy public-indicator hunt gen 442

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T122223Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret296_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 2.6428 | 0.7405 | 5.2997 | 0.0325 | 0.4177 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret296_neg_at_h` | one_head_filter_pi_star | 156 | 12.7438 | 2.2993 | 0.7179 | 4.6544 | 0.0272 | 0.4231 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret296_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 1.8730 | 0.6707 | 3.4769 | 0.0141 | 0.3720 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret296_neg_at_h` | one_head_filter_pi_star | 152 | 12.4292 | 1.8477 | 0.6579 | 3.1694 | 0.0136 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret296_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.5601 | 0.6207 | 2.4547 | 0.0088 | 0.2816 | ok | RAN |
| SOLUSDT | 4 | `ret296_pos_at_h` | one_head_filter_pi_star | 169 | 13.8588 | 1.5424 | 0.6095 | 2.4037 | 0.0085 | 0.2899 | ok | RAN |
| ETHUSDT | 4 | `ret296_pos_at_h` | one_head_filter_pi_star | 137 | 11.3054 | 1.1496 | 0.5985 | 0.7222 | 0.0052 | 0.1971 | ok | RAN |
| ETHUSDT | 8 | `ret296_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.0566 | 0.5824 | 0.3078 | 0.0021 | 0.1941 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret296_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6092 | 0.3158 | -0.8112 | -0.0413 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret296_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5824 | 0.3158 | -0.9020 | -0.0444 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret296_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret296_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
