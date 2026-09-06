# Autonomy public-indicator hunt gen 1053

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T165908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret188_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0041 | 0.6889 | 4.2713 | 0.0234 | 0.3667 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret188_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.9580 | 0.6946 | 4.0918 | 0.0232 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret188_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 2.0950 | 0.6688 | 3.8343 | 0.0158 | 0.3885 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret188_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.0052 | 0.6739 | 3.9072 | 0.0150 | 0.3533 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret188_pos_at_h` | one_head_filter_pi_star | 207 | 17.0819 | 1.3081 | 0.6135 | 1.6440 | 0.0102 | 0.2271 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret188_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4897 | 0.6150 | 2.3110 | 0.0076 | 0.2674 | ok | RAN |
| SOLUSDT | 4 | `ret188_pos_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3987 | 0.5980 | 1.9996 | 0.0063 | 0.2663 | ok | RAN |
| ETHUSDT | 8 | `ret188_pos_at_h` | one_head_filter_pi_star | 203 | 16.6863 | 1.1498 | 0.5862 | 0.7980 | 0.0051 | 0.2266 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret188_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret188_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret188_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret188_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret188_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret188_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret188_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret188_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret188_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret188_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret188_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret188_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret188_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret188_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret188_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret188_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
