# Autonomy public-indicator hunt gen 1125

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T015934Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret204_neg_at_h` | one_head_filter_pi_star | 152 | 12.4170 | 2.3247 | 0.7105 | 4.7142 | 0.0277 | 0.4079 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret204_neg_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.0222 | 0.6949 | 4.2359 | 0.0241 | 0.4011 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret204_neg_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1910 | 0.6899 | 3.9924 | 0.0169 | 0.3924 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret204_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.0024 | 0.6723 | 3.7771 | 0.0148 | 0.3616 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret204_pos_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5566 | 0.6229 | 2.4932 | 0.0084 | 0.2743 | ok | RAN |
| ETHUSDT | 8 | `ret204_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2197 | 0.5864 | 1.1302 | 0.0077 | 0.2356 | ok | RAN |
| SOLUSDT | 4 | `ret204_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4692 | 0.6129 | 2.2188 | 0.0072 | 0.2742 | ok | RAN |
| ETHUSDT | 4 | `ret204_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.1524 | 0.5761 | 0.7992 | 0.0052 | 0.2228 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret204_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret204_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret204_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret204_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret204_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret204_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret204_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret204_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret204_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret204_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret204_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret204_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret204_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret204_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret204_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret204_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
