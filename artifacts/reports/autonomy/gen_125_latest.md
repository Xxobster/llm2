# Autonomy public-indicator hunt gen 125

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T174045Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret16_cross_up_0` | one_head_filter_pi_star | 18 | 1.5648 | 2.8515 | 0.6667 | 1.8257 | 0.0296 | 0.2778 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret16_cross_down_0` | one_head_filter_pi_star | 22 | 1.8098 | 3.8463 | 0.7273 | 2.2971 | 0.0245 | 0.1364 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret16_neg_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 1.7999 | 0.6776 | 3.8312 | 0.0204 | 0.3879 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret16_cross_up_0` | one_head_filter_pi_star | 31 | 2.5509 | 1.4289 | 0.5806 | 0.8123 | 0.0199 | 0.2581 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret16_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7258 | 0.6712 | 3.5624 | 0.0192 | 0.3744 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret16_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1474 | 0.6914 | 3.8989 | 0.0173 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret16_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1412 | 0.6914 | 3.8924 | 0.0171 | 0.4198 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret16_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2381 | 0.5938 | 1.0835 | 0.0074 | 0.2000 | ok | RAN |
| ETHUSDT | 4 | `ret16_pos_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2092 | 0.5924 | 0.9778 | 0.0066 | 0.2102 | ok | RAN |
| SOLUSDT | 4 | `ret16_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.3911 | 0.6019 | 2.0853 | 0.0058 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `ret16_pos_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3593 | 0.5869 | 1.9488 | 0.0054 | 0.2535 | ok | RAN |
| ETHUSDT | 4 | `ret16_cross_down_0` | one_head_filter_pi_star | 17 | 1.4087 | 1.1497 | 0.5882 | 0.2321 | 0.0050 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret16_cross_down_0` | one_head_filter_pi_star | 47 | 3.8818 | 1.0672 | 0.5319 | 0.1933 | 0.0030 | 0.1915 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret16_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret16_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret16_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret16_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret16_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret16_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret16_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret16_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret16_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret16_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret16_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
