# Autonomy public-indicator hunt gen 645

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T032431Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret109_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.7563 | 0.6721 | 3.6257 | 0.0195 | 0.3716 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret109_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.6661 | 0.6526 | 3.3455 | 0.0178 | 0.3579 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret109_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.2660 | 0.6868 | 4.5496 | 0.0176 | 0.3681 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret109_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 2.2089 | 0.6825 | 4.4180 | 0.0166 | 0.3651 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret109_pos_at_h` | one_head_filter_pi_star | 197 | 16.2567 | 1.4047 | 0.6294 | 1.9909 | 0.0126 | 0.2437 | ok | RAN |
| ETHUSDT | 8 | `ret109_pos_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.3859 | 0.6264 | 1.8134 | 0.0121 | 0.2414 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret109_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.3985 | 0.6011 | 1.9580 | 0.0063 | 0.2640 | ok | RAN |
| SOLUSDT | 8 | `ret109_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.3293 | 0.5955 | 1.6657 | 0.0054 | 0.2528 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret109_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret109_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret109_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret109_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret109_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret109_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret109_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret109_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret109_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret109_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret109_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret109_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret109_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret109_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret109_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret109_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
