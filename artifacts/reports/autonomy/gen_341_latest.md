# Autonomy public-indicator hunt gen 341

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T132841Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret35_cross_down_0` | one_head_filter_pi_star | 32 | 2.7769 | 1.7365 | 0.5625 | 1.2456 | 0.0214 | 0.2188 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret35_neg_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8062 | 0.6733 | 3.8630 | 0.0208 | 0.3564 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret35_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.7146 | 0.6699 | 3.5775 | 0.0194 | 0.3541 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret35_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0027 | 0.6747 | 3.6960 | 0.0163 | 0.4036 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret35_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9463 | 0.6707 | 3.5360 | 0.0155 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret35_pos_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2914 | 0.6082 | 1.3903 | 0.0088 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `ret35_pos_at_h` | one_head_filter_pi_star | 169 | 13.8916 | 1.2858 | 0.6154 | 1.3693 | 0.0087 | 0.2367 | ok | RAN |
| ETHUSDT | 8 | `ret35_cross_up_0` | one_head_filter_pi_star | 29 | 2.4071 | 1.1915 | 0.5517 | 0.4298 | 0.0087 | 0.2069 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret35_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.5505 | 0.6204 | 2.6899 | 0.0076 | 0.2639 | ok | RAN |
| SOLUSDT | 8 | `ret35_pos_at_h` | one_head_filter_pi_star | 207 | 16.8789 | 1.4578 | 0.6087 | 2.2599 | 0.0064 | 0.2657 | ok | RAN |
| SOLUSDT | 8 | `ret35_cross_up_0` | one_head_filter_pi_star | 17 | 1.4400 | 1.4062 | 0.5882 | 0.5284 | 0.0057 | 0.1176 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret35_cross_down_0` | one_head_filter_pi_star | 14 | 1.1638 | 1.4932 | 0.5000 | 0.5725 | 0.0055 | 0.2143 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret35_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret35_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret35_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret35_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret35_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret35_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret35_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret35_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret35_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret35_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret35_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret35_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
