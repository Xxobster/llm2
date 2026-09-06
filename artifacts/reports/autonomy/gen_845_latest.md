# Autonomy public-indicator hunt gen 845

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T195556Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret159_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9971 | 0.6952 | 4.4471 | 0.0242 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret159_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9603 | 0.6963 | 4.2851 | 0.0237 | 0.3822 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret159_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1522 | 0.6824 | 4.1197 | 0.0162 | 0.3765 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret159_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1120 | 0.6784 | 4.0124 | 0.0159 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret159_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.2452 | 0.6000 | 1.2697 | 0.0082 | 0.2105 | ok | RAN |
| SOLUSDT | 8 | `ret159_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3605 | 0.5879 | 1.7575 | 0.0058 | 0.2527 | ok | RAN |
| SOLUSDT | 4 | `ret159_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3186 | 0.5882 | 1.5844 | 0.0051 | 0.2567 | ok | RAN |
| ETHUSDT | 8 | `ret159_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.1235 | 0.5889 | 0.6633 | 0.0045 | 0.2111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret159_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret159_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret159_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret159_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret159_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret159_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret159_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret159_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret159_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret159_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret159_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret159_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret159_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret159_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret159_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret159_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
