# Autonomy public-indicator hunt gen 029

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T112044Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ac_cross_up_0` | one_head_filter_pi_star | 237 | 19.3607 | 1.8298 | 0.6878 | 4.0696 | 0.0221 | 0.3586 | EBR>35% | RAN |
| ETHUSDT | 4 | `ac_cross_down_0` | one_head_filter_pi_star | 47 | 3.8668 | 1.5438 | 0.6170 | 1.3221 | 0.0213 | 0.3617 | EBR>35% | RAN |
| ETHUSDT | 8 | `ac_pos_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.7699 | 0.6683 | 3.7137 | 0.0205 | 0.3568 | EBR>35% | RAN |
| ETHUSDT | 4 | `ac_neg_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.7649 | 0.6728 | 3.5812 | 0.0201 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `ac_cross_up_0` | one_head_filter_pi_star | 38 | 3.5157 | 1.5893 | 0.7105 | 1.3119 | 0.0200 | 0.2368 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ac_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1542 | 0.6905 | 3.9451 | 0.0181 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 8 | `ac_pos_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.1065 | 0.6946 | 3.9710 | 0.0171 | 0.4072 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ac_cross_down_0` | one_head_filter_pi_star | 36 | 3.0778 | 1.6373 | 0.6111 | 1.2854 | 0.0139 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 8 | `ac_cross_up_0` | one_head_filter_pi_star | 185 | 15.1276 | 1.9090 | 0.6865 | 3.7093 | 0.0136 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 8 | `ac_cross_down_0` | one_head_filter_pi_star | 206 | 16.8774 | 1.3347 | 0.6068 | 1.6770 | 0.0112 | 0.2427 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ac_neg_at_h` | one_head_filter_pi_star | 167 | 13.7811 | 1.2462 | 0.5928 | 1.1504 | 0.0078 | 0.2275 | ok | RAN |
| ETHUSDT | 4 | `ac_pos_at_h` | one_head_filter_pi_star | 169 | 13.9461 | 1.2275 | 0.5858 | 1.0830 | 0.0073 | 0.2130 | ok | RAN |
| SOLUSDT | 4 | `ac_cross_up_0` | one_head_filter_pi_star | 44 | 3.7045 | 1.4361 | 0.6818 | 0.9992 | 0.0058 | 0.1364 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ac_cross_down_0` | one_head_filter_pi_star | 222 | 18.1020 | 1.3528 | 0.5811 | 2.0168 | 0.0057 | 0.2793 | ok | RAN |
| SOLUSDT | 8 | `ac_neg_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.3593 | 0.6114 | 1.7832 | 0.0056 | 0.2686 | ok | RAN |
| SOLUSDT | 4 | `ac_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3376 | 0.5935 | 1.8591 | 0.0051 | 0.2430 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ac_neg_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ac_cross_down_0` | one_head_filter_pi_star | 20 | 1.7020 | 0.7748 | 0.3500 | -0.4429 | -0.0230 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ac_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ac_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ac_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ac_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ac_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ac_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
