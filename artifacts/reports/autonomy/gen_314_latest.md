# Autonomy public-indicator hunt gen 314

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T062945Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret168_neg_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0476 | 0.6973 | 4.4572 | 0.0251 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret168_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9242 | 0.6882 | 4.2036 | 0.0237 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret168_neg_at_h` | one_head_filter_pi_star | 154 | 12.5927 | 2.1918 | 0.6753 | 4.0009 | 0.0163 | 0.3831 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret168_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.0154 | 0.6707 | 3.7430 | 0.0154 | 0.3780 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret168_pos_at_h` | one_head_filter_pi_star | 202 | 16.6041 | 1.2591 | 0.5990 | 1.3683 | 0.0085 | 0.2228 | ok | RAN |
| ETHUSDT | 4 | `ret168_pos_at_h` | one_head_filter_pi_star | 208 | 17.0973 | 1.2448 | 0.6058 | 1.3063 | 0.0080 | 0.2212 | ok | RAN |
| SOLUSDT | 4 | `ret168_pos_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.4141 | 0.6059 | 2.0751 | 0.0065 | 0.2660 | ok | RAN |
| SOLUSDT | 8 | `ret168_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3786 | 0.5968 | 1.8799 | 0.0062 | 0.2688 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret168_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret168_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret168_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret168_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret168_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret168_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
