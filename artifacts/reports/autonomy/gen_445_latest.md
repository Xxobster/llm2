# Autonomy public-indicator hunt gen 445

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T131033Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret59_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.7910 | 0.6788 | 3.9101 | 0.0207 | 0.3679 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret59_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.7975 | 0.6828 | 3.7954 | 0.0205 | 0.3817 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret59_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2859 | 0.6982 | 4.3677 | 0.0181 | 0.4024 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret59_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.1042 | 0.6854 | 4.1110 | 0.0166 | 0.3820 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret59_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.3618 | 0.6170 | 1.7451 | 0.0108 | 0.2340 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret59_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.3070 | 0.5990 | 1.5080 | 0.0096 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `ret59_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3969 | 0.5971 | 2.0662 | 0.0059 | 0.2573 | ok | RAN |
| SOLUSDT | 4 | `ret59_pos_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.3294 | 0.5865 | 1.7659 | 0.0050 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret59_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret59_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret59_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret59_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret59_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret59_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret59_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret59_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret59_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret59_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret59_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret59_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret59_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret59_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret59_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret59_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
