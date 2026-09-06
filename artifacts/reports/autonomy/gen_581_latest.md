# Autonomy public-indicator hunt gen 581

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T231650Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret93_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8550 | 0.6683 | 3.9906 | 0.0214 | 0.3769 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret93_neg_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.7751 | 0.6601 | 3.8348 | 0.0196 | 0.3596 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret93_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.2209 | 0.6719 | 4.4871 | 0.0168 | 0.3646 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret93_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0928 | 0.6720 | 4.1330 | 0.0157 | 0.3656 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret93_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.3112 | 0.6278 | 1.5043 | 0.0101 | 0.2167 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret93_pos_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2756 | 0.6222 | 1.3281 | 0.0094 | 0.2333 | ok | RAN |
| SOLUSDT | 4 | `ret93_pos_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.3497 | 0.5904 | 1.8021 | 0.0057 | 0.2553 | ok | RAN |
| SOLUSDT | 8 | `ret93_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.3385 | 0.5899 | 1.7090 | 0.0055 | 0.2528 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret93_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret93_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret93_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret93_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret93_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret93_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret93_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret93_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret93_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret93_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret93_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret93_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret93_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret93_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret93_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret93_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
