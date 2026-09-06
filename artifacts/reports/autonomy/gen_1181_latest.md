# Autonomy public-indicator hunt gen 1181

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T082614Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret212_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 2.1375 | 0.7000 | 4.2661 | 0.0253 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret212_neg_at_h` | one_head_filter_pi_star | 170 | 13.8874 | 1.9456 | 0.6824 | 3.9754 | 0.0233 | 0.3882 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret212_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.9431 | 0.6743 | 3.7067 | 0.0145 | 0.3771 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret212_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.9261 | 0.6615 | 3.7821 | 0.0140 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret212_pos_at_h` | one_head_filter_pi_star | 167 | 13.6948 | 1.6136 | 0.6347 | 2.6656 | 0.0093 | 0.2874 | ok | RAN |
| SOLUSDT | 4 | `ret212_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.4052 | 0.6067 | 1.9485 | 0.0066 | 0.2865 | ok | RAN |
| ETHUSDT | 8 | `ret212_pos_at_h` | one_head_filter_pi_star | 209 | 17.1795 | 1.1077 | 0.5789 | 0.5903 | 0.0040 | 0.2344 | ok | RAN |
| ETHUSDT | 4 | `ret212_pos_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1065 | 0.5781 | 0.5759 | 0.0039 | 0.2240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret212_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6964 | 0.3684 | -0.6260 | -0.0304 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret212_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret212_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret212_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret212_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret212_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret212_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret212_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret212_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret212_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret212_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret212_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret212_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret212_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret212_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret212_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
