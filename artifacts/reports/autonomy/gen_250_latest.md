# Autonomy public-indicator hunt gen 250

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T015758Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret104_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8219 | 0.6649 | 3.8663 | 0.0207 | 0.3560 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret104_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.7791 | 0.6684 | 3.7105 | 0.0201 | 0.3684 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret104_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.2414 | 0.6828 | 4.3854 | 0.0168 | 0.3602 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret104_neg_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.1887 | 0.6740 | 4.2835 | 0.0162 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret104_pos_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.4488 | 0.6333 | 2.0637 | 0.0140 | 0.2333 | ok | RAN |
| ETHUSDT | 8 | `ret104_pos_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.3229 | 0.6283 | 1.5707 | 0.0103 | 0.2304 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret104_pos_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.3593 | 0.5968 | 1.8335 | 0.0058 | 0.2634 | ok | RAN |
| SOLUSDT | 8 | `ret104_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.3403 | 0.5916 | 1.7558 | 0.0054 | 0.2513 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret104_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret104_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret104_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret104_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret104_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret104_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
