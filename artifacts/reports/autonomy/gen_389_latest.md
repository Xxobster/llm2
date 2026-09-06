# Autonomy public-indicator hunt gen 389

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T234930Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret45_neg_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.8004 | 0.6779 | 3.8286 | 0.0213 | 0.3558 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret45_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.6667 | 0.6650 | 3.4150 | 0.0182 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret45_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1015 | 0.6807 | 3.8280 | 0.0169 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret45_neg_at_h` | one_head_filter_pi_star | 151 | 12.3474 | 1.9391 | 0.6821 | 3.4978 | 0.0152 | 0.4106 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret45_cross_up_0` | one_head_filter_pi_star | 16 | 1.3642 | 1.8843 | 0.5000 | 0.9960 | 0.0131 | 0.2500 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret45_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2511 | 0.5988 | 1.2093 | 0.0080 | 0.2209 | ok | RAN |
| SOLUSDT | 8 | `ret45_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.5676 | 0.6250 | 2.8604 | 0.0079 | 0.2685 | ok | RAN |
| SOLUSDT | 4 | `ret45_pos_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.5342 | 0.6190 | 2.6663 | 0.0075 | 0.2714 | ok | RAN |
| ETHUSDT | 8 | `ret45_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.2276 | 0.6034 | 1.0912 | 0.0072 | 0.2299 | ok | RAN |
| ETHUSDT | 8 | `ret45_cross_down_0` | one_head_filter_pi_star | 21 | 1.7968 | 1.1735 | 0.4762 | 0.2978 | 0.0068 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret45_cross_down_0` | one_head_filter_pi_star | 31 | 2.5915 | 1.2813 | 0.4839 | 0.5873 | 0.0062 | 0.2581 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret45_cross_up_0` | one_head_filter_pi_star | 17 | 1.5009 | 0.9069 | 0.4706 | -0.1804 | -0.0037 | 0.1765 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret45_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret45_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret45_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret45_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret45_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret45_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret45_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret45_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret45_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret45_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret45_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret45_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
