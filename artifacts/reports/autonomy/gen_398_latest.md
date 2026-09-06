# Autonomy public-indicator hunt gen 398

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T014834Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma155_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9742 | 0.6904 | 4.4575 | 0.0232 | 0.3655 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma155_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.8639 | 0.6802 | 4.1313 | 0.0213 | 0.3706 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma155_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.2779 | 0.6970 | 4.3328 | 0.0188 | 0.4061 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma155_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.3188 | 0.6949 | 4.5980 | 0.0186 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma155_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2623 | 0.6054 | 1.2828 | 0.0086 | 0.2270 | ok | RAN |
| ETHUSDT | 8 | `wma155_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2154 | 0.6044 | 1.0605 | 0.0072 | 0.2308 | ok | RAN |
| SOLUSDT | 4 | `wma155_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2903 | 0.5922 | 1.5474 | 0.0045 | 0.2621 | ok | RAN |
| SOLUSDT | 8 | `wma155_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.2514 | 0.5750 | 1.3624 | 0.0039 | 0.2550 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma155_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma155_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `wma155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma155_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma155_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma155_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma155_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
