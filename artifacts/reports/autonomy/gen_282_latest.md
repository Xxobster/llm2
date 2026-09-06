# Autonomy public-indicator hunt gen 282

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T041136Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret136_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8351 | 0.6718 | 3.9313 | 0.0214 | 0.3641 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret136_neg_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.7887 | 0.6776 | 3.6568 | 0.0202 | 0.3880 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret136_neg_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2543 | 0.6914 | 4.3447 | 0.0172 | 0.3657 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret136_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.0890 | 0.6761 | 3.9599 | 0.0157 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret136_pos_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.3610 | 0.6216 | 1.7502 | 0.0120 | 0.2432 | ok | RAN |
| ETHUSDT | 4 | `ret136_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.3621 | 0.6222 | 1.7587 | 0.0113 | 0.2167 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret136_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.3939 | 0.6054 | 1.9149 | 0.0064 | 0.2649 | ok | RAN |
| SOLUSDT | 4 | `ret136_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.3224 | 0.5909 | 1.5767 | 0.0053 | 0.2614 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret136_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret136_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret136_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret136_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret136_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret136_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
