# Autonomy public-indicator hunt gen 661

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T042806Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret113_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8361 | 0.6754 | 3.8631 | 0.0210 | 0.3613 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret113_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.8217 | 0.6761 | 3.7688 | 0.0203 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret113_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2987 | 0.6966 | 4.4544 | 0.0171 | 0.3596 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret113_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.2752 | 0.6811 | 4.3698 | 0.0171 | 0.3676 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret113_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.5471 | 0.6526 | 2.4867 | 0.0163 | 0.2684 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret113_pos_at_h` | one_head_filter_pi_star | 190 | 15.6791 | 1.3939 | 0.6263 | 1.8862 | 0.0124 | 0.2421 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret113_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.4616 | 0.6102 | 2.1718 | 0.0072 | 0.2599 | ok | RAN |
| SOLUSDT | 4 | `ret113_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.3826 | 0.6045 | 1.8909 | 0.0062 | 0.2599 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret113_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret113_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret113_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret113_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret113_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret113_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret113_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret113_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret113_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret113_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret113_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret113_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret113_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret113_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret113_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret113_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
