# Autonomy public-indicator hunt gen 517

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T190247Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret77_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8487 | 0.6736 | 3.9435 | 0.0211 | 0.3886 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret77_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8173 | 0.6649 | 3.9113 | 0.0201 | 0.3717 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret77_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2615 | 0.6743 | 4.3855 | 0.0174 | 0.3714 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret77_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1020 | 0.6758 | 4.0673 | 0.0157 | 0.3681 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret77_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2969 | 0.6150 | 1.4499 | 0.0099 | 0.2246 | ok | RAN |
| ETHUSDT | 4 | `ret77_pos_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2754 | 0.6166 | 1.4166 | 0.0090 | 0.2228 | ok | RAN |
| SOLUSDT | 8 | `ret77_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.4079 | 0.6129 | 2.0504 | 0.0063 | 0.2527 | ok | RAN |
| SOLUSDT | 4 | `ret77_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4090 | 0.6032 | 2.0527 | 0.0062 | 0.2593 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret77_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret77_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret77_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret77_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret77_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret77_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret77_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret77_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret77_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret77_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret77_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret77_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret77_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret77_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret77_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret77_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
