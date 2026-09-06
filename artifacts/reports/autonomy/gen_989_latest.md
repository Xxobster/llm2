# Autonomy public-indicator hunt gen 989

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T181015Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret195_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.2610 | 0.7091 | 4.8105 | 0.0270 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret195_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 2.0444 | 0.6954 | 4.3052 | 0.0231 | 0.3736 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret195_neg_at_h` | one_head_filter_pi_star | 152 | 12.4292 | 2.0634 | 0.6776 | 3.8943 | 0.0162 | 0.3816 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret195_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.0261 | 0.6740 | 3.9123 | 0.0149 | 0.3646 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret195_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.5335 | 0.6296 | 2.4749 | 0.0081 | 0.2751 | ok | RAN |
| SOLUSDT | 4 | `ret195_pos_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.4984 | 0.6162 | 2.3734 | 0.0075 | 0.2677 | ok | RAN |
| ETHUSDT | 8 | `ret195_pos_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.1759 | 0.5968 | 0.8954 | 0.0063 | 0.2312 | ok | RAN |
| ETHUSDT | 4 | `ret195_pos_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1174 | 0.5787 | 0.6231 | 0.0044 | 0.2234 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret195_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret195_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret195_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret195_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret195_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret195_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret195_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret195_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret195_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret195_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret195_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret195_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret195_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret195_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret195_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret195_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
