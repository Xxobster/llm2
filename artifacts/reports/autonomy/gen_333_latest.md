# Autonomy public-indicator hunt gen 333

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T120300Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret34_cross_up_0` | one_head_filter_pi_star | 35 | 2.9052 | 2.1085 | 0.6286 | 1.8409 | 0.0369 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret34_neg_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.7855 | 0.6683 | 3.8147 | 0.0209 | 0.3654 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret34_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.6724 | 0.6633 | 3.3497 | 0.0182 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret34_cross_down_0` | one_head_filter_pi_star | 17 | 1.3999 | 2.1226 | 0.5882 | 1.1318 | 0.0161 | 0.2353 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret34_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.0060 | 0.6746 | 3.7471 | 0.0160 | 0.3964 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret34_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.9174 | 0.6667 | 3.5790 | 0.0149 | 0.3801 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret34_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2631 | 0.6136 | 1.2562 | 0.0082 | 0.2443 | ok | RAN |
| SOLUSDT | 4 | `ret34_pos_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.5489 | 0.6175 | 2.6848 | 0.0076 | 0.2627 | ok | RAN |
| SOLUSDT | 8 | `ret34_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.5213 | 0.6111 | 2.5647 | 0.0072 | 0.2593 | ok | RAN |
| ETHUSDT | 8 | `ret34_pos_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.1913 | 0.5965 | 0.9414 | 0.0061 | 0.2164 | ok | RAN |
| SOLUSDT | 8 | `ret34_cross_up_0` | one_head_filter_pi_star | 23 | 2.0004 | 1.3116 | 0.5652 | 0.5327 | 0.0056 | 0.1739 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret34_cross_down_0` | one_head_filter_pi_star | 29 | 2.4813 | 0.9192 | 0.4483 | -0.1973 | -0.0039 | 0.1724 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret34_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret34_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret34_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret34_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret34_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret34_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret34_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret34_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret34_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret34_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret34_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret34_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
