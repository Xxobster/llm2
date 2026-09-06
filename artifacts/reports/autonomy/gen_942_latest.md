# Autonomy public-indicator hunt gen 942

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T060610Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma495_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0894 | 0.7074 | 4.5858 | 0.0244 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma495_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9995 | 0.6961 | 4.3695 | 0.0237 | 0.3978 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma495_below_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.1736 | 0.6902 | 4.3937 | 0.0166 | 0.3696 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma495_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.0716 | 0.6811 | 4.1447 | 0.0154 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma495_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2633 | 0.6108 | 1.3370 | 0.0088 | 0.2108 | ok | RAN |
| ETHUSDT | 4 | `wma495_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2131 | 0.5979 | 1.1337 | 0.0075 | 0.2268 | ok | RAN |
| SOLUSDT | 8 | `wma495_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4249 | 0.5989 | 2.0752 | 0.0068 | 0.2620 | ok | RAN |
| SOLUSDT | 4 | `wma495_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.3775 | 0.5960 | 1.9420 | 0.0060 | 0.2626 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma495_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma495_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma495_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma495_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma495_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma495_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
