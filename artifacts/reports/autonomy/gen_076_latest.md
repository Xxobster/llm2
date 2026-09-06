# Autonomy public-indicator hunt gen 076

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T143226Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `adxsl_neg_at_h` | one_head_filter_pi_star | 28 | 2.3057 | 4.0429 | 0.7500 | 2.8403 | 0.0342 | 0.3571 | EBR>35% | RAN |
| ETHUSDT | 4 | `adxsl_cross_up_0` | one_head_filter_pi_star | 48 | 3.9835 | 2.4153 | 0.6667 | 2.4424 | 0.0327 | 0.1875 | TPM<MIN | RAN |
| ETHUSDT | 4 | `adxsl_neg_at_h` | one_head_filter_pi_star | 56 | 4.6225 | 1.7329 | 0.6071 | 1.7499 | 0.0236 | 0.2500 | GATE_CAND | RAN |
| ETHUSDT | 8 | `adxsl_cross_up_0` | one_head_filter_pi_star | 86 | 7.0988 | 1.8863 | 0.6395 | 2.3717 | 0.0234 | 0.1977 | GATE_CAND | RAN |
| ETHUSDT | 8 | `adxsl_neg_at_h` | one_head_filter_pi_star | 68 | 5.5955 | 1.9903 | 0.7059 | 2.4076 | 0.0228 | 0.2941 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `adxsl_pos_at_h` | one_head_filter_pi_star | 322 | 26.1953 | 1.4589 | 0.6398 | 2.8921 | 0.0133 | 0.3075 | ok | RAN |
| BTCUSDT | 8 | `adxsl_pos_at_h` | one_head_filter_pi_star | 11 | 1.1980 | 1.1039 | 0.5455 | 0.1645 | 0.0124 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 8 | `adxsl_pos_at_h` | one_head_filter_pi_star | 271 | 22.0464 | 1.3839 | 0.6162 | 2.2281 | 0.0119 | 0.2952 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `adxsl_pos_at_h` | one_head_filter_pi_star | 253 | 20.7362 | 1.5543 | 0.6166 | 2.9292 | 0.0095 | 0.3202 | ok | RAN |
| ETHUSDT | 4 | `adxsl_cross_down_0` | one_head_filter_pi_star | 43 | 3.8407 | 1.3226 | 0.6279 | 0.7585 | 0.0093 | 0.2093 | TPM<MIN | RAN |
| SOLUSDT | 8 | `adxsl_neg_at_h` | one_head_filter_pi_star | 61 | 4.9748 | 1.6247 | 0.6557 | 1.5793 | 0.0086 | 0.2623 | ok | RAN |
| SOLUSDT | 4 | `adxsl_cross_up_0` | one_head_filter_pi_star | 45 | 3.8351 | 1.4576 | 0.5778 | 1.0837 | 0.0085 | 0.2444 | TPM<MIN | RAN |
| SOLUSDT | 4 | `adxsl_pos_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5486 | 0.6213 | 3.5030 | 0.0085 | 0.3166 | ok | RAN |
| BTCUSDT | 8 | `adxsl_neg_at_h` | one_head_filter_pi_star | 13 | 1.5001 | 1.1179 | 0.3846 | 0.1884 | 0.0082 | 0.0769 | TPM<MIN | RAN |
| ETHUSDT | 8 | `adxsl_cross_down_0` | one_head_filter_pi_star | 232 | 19.1088 | 1.2515 | 0.6121 | 1.4598 | 0.0079 | 0.2802 | ok | RAN |
| SOLUSDT | 8 | `adxsl_cross_up_0` | one_head_filter_pi_star | 63 | 5.3691 | 1.3767 | 0.5873 | 1.0716 | 0.0075 | 0.2222 | ok | RAN |
| SOLUSDT | 8 | `adxsl_cross_down_0` | one_head_filter_pi_star | 271 | 22.0464 | 1.5093 | 0.6125 | 2.9526 | 0.0071 | 0.2435 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `adxsl_cross_down_0` | one_head_filter_pi_star | 23 | 2.0284 | 1.0142 | 0.5652 | 0.0296 | 0.0003 | 0.1304 | TPM<MIN | RAN |
| BTCUSDT | 4 | `adxsl_pos_at_h` | one_head_filter_pi_star | 25 | 2.1274 | 0.9676 | 0.4400 | -0.0672 | -0.0032 | 0.1600 | TPM<MIN | RAN |
| BTCUSDT | 8 | `adxsl_cross_down_0` | one_head_filter_pi_star | 16 | 1.4683 | 0.5065 | 0.3125 | -1.0681 | -0.0365 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `adxsl_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `adxsl_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `adxsl_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `adxsl_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
