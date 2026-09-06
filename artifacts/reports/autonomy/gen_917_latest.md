# Autonomy public-indicator hunt gen 917

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T031909Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret177_neg_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.1357 | 0.7039 | 4.5976 | 0.0262 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret177_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0256 | 0.7022 | 4.4905 | 0.0247 | 0.3989 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret177_neg_at_h` | one_head_filter_pi_star | 156 | 12.7563 | 2.0397 | 0.6667 | 3.7101 | 0.0157 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret177_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.8795 | 0.6550 | 3.4469 | 0.0136 | 0.3626 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret177_pos_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.5200 | 0.6119 | 2.4894 | 0.0079 | 0.2687 | ok | RAN |
| ETHUSDT | 4 | `ret177_pos_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.2246 | 0.6000 | 1.1610 | 0.0074 | 0.2256 | ok | RAN |
| SOLUSDT | 4 | `ret177_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4586 | 0.6010 | 2.1876 | 0.0069 | 0.2591 | ok | RAN |
| ETHUSDT | 8 | `ret177_pos_at_h` | one_head_filter_pi_star | 198 | 16.3392 | 1.1962 | 0.5909 | 1.0499 | 0.0067 | 0.2273 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret177_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret177_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0456 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret177_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret177_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret177_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret177_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret177_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret177_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret177_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret177_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret177_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret177_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret177_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret177_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret177_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret177_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
