# Autonomy public-indicator hunt gen 1285

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T184616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret227_neg_at_h` | one_head_filter_pi_star | 158 | 12.9072 | 2.4229 | 0.7215 | 4.9979 | 0.0294 | 0.4114 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret227_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.2234 | 0.7024 | 4.6119 | 0.0275 | 0.3929 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret227_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.8745 | 0.6559 | 3.6420 | 0.0129 | 0.3656 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret227_neg_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 1.7982 | 0.6536 | 3.2946 | 0.0120 | 0.3575 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret227_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2522 | 0.6041 | 1.2752 | 0.0086 | 0.2335 | ok | RAN |
| SOLUSDT | 4 | `ret227_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.4382 | 0.6084 | 1.9458 | 0.0069 | 0.2831 | ok | RAN |
| SOLUSDT | 8 | `ret227_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.3637 | 0.5977 | 1.7314 | 0.0059 | 0.2701 | ok | RAN |
| ETHUSDT | 8 | `ret227_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.1349 | 0.5751 | 0.7186 | 0.0051 | 0.2332 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret227_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret227_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret227_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret227_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret227_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret227_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret227_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret227_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret227_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret227_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret227_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret227_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret227_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret227_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret227_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret227_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
