# Autonomy public-indicator hunt gen 525

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T193551Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret79_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8046 | 0.6684 | 3.7776 | 0.0205 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret79_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8086 | 0.6684 | 3.9009 | 0.0204 | 0.3731 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret79_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1634 | 0.6778 | 4.2701 | 0.0168 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret79_neg_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.0544 | 0.6667 | 3.9645 | 0.0150 | 0.3661 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret79_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.3054 | 0.6114 | 1.5192 | 0.0098 | 0.2176 | ok | RAN |
| ETHUSDT | 8 | `ret79_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2215 | 0.6054 | 1.0925 | 0.0074 | 0.2270 | ok | RAN |
| SOLUSDT | 8 | `ret79_pos_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3925 | 0.6062 | 2.0204 | 0.0061 | 0.2539 | ok | RAN |
| SOLUSDT | 4 | `ret79_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3674 | 0.6000 | 1.8609 | 0.0059 | 0.2632 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret79_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret79_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0459 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret79_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret79_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret79_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret79_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret79_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret79_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret79_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret79_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret79_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret79_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret79_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret79_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret79_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret79_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
