# Autonomy public-indicator hunt gen 621

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T015152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret103_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8326 | 0.6684 | 3.9834 | 0.0209 | 0.3523 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret103_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.7796 | 0.6579 | 3.7610 | 0.0198 | 0.3526 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret103_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2619 | 0.6854 | 4.3595 | 0.0172 | 0.3708 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret103_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.2979 | 0.6833 | 4.4512 | 0.0172 | 0.3611 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret103_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.4626 | 0.6444 | 2.1214 | 0.0142 | 0.2444 | ok | RAN |
| ETHUSDT | 8 | `ret103_pos_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.4126 | 0.6339 | 1.9696 | 0.0131 | 0.2514 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret103_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4094 | 0.6044 | 2.0109 | 0.0065 | 0.2582 | ok | RAN |
| SOLUSDT | 8 | `ret103_pos_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.3733 | 0.5990 | 1.9141 | 0.0058 | 0.2640 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret103_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret103_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret103_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret103_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret103_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret103_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret103_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret103_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret103_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret103_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret103_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret103_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret103_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret103_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret103_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret103_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
