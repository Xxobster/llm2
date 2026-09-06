# Autonomy public-indicator hunt gen 725

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T085855Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret129_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8602 | 0.6772 | 3.9338 | 0.0220 | 0.3704 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret129_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 1.8653 | 0.6750 | 3.6022 | 0.0215 | 0.3875 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret129_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.1774 | 0.6885 | 4.3605 | 0.0165 | 0.3661 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret129_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.1292 | 0.6796 | 4.0920 | 0.0152 | 0.3646 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret129_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.3630 | 0.6271 | 1.7426 | 0.0119 | 0.2260 | ok | RAN |
| ETHUSDT | 8 | `ret129_pos_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.3379 | 0.6175 | 1.7356 | 0.0114 | 0.2459 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret129_pos_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.4078 | 0.6096 | 2.0272 | 0.0066 | 0.2620 | ok | RAN |
| SOLUSDT | 4 | `ret129_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3381 | 0.6010 | 1.7245 | 0.0055 | 0.2591 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret129_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret129_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret129_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret129_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret129_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret129_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret129_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret129_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret129_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret129_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret129_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret129_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret129_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret129_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret129_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret129_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
