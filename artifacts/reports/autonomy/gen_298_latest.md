# Autonomy public-indicator hunt gen 298

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T052043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret152_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0270 | 0.7011 | 4.5357 | 0.0241 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret152_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8411 | 0.6768 | 4.0247 | 0.0215 | 0.3586 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret152_neg_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.1699 | 0.6809 | 4.3231 | 0.0161 | 0.3564 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret152_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1668 | 0.6811 | 4.3111 | 0.0161 | 0.3568 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret152_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.3242 | 0.6102 | 1.5570 | 0.0106 | 0.2260 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret152_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4398 | 0.6114 | 2.1279 | 0.0068 | 0.2487 | ok | RAN |
| ETHUSDT | 4 | `ret152_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.1536 | 0.5895 | 0.8062 | 0.0055 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `ret152_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.2866 | 0.5798 | 1.4576 | 0.0047 | 0.2713 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret152_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret152_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret152_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret152_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret152_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret152_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
