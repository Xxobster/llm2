# Autonomy public-indicator hunt gen 789

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T144008Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret145_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8882 | 0.6911 | 4.1296 | 0.0217 | 0.3665 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret145_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.8445 | 0.6772 | 3.8833 | 0.0215 | 0.3862 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret145_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.1537 | 0.6791 | 4.2914 | 0.0163 | 0.3529 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret145_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.0553 | 0.6722 | 3.9732 | 0.0152 | 0.3611 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret145_pos_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.2741 | 0.6044 | 1.3896 | 0.0089 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `ret145_pos_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.2299 | 0.6011 | 1.1669 | 0.0080 | 0.2186 | ok | RAN |
| SOLUSDT | 8 | `ret145_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4570 | 0.6150 | 2.2110 | 0.0072 | 0.2750 | ok | RAN |
| SOLUSDT | 4 | `ret145_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3821 | 0.5989 | 1.8424 | 0.0060 | 0.2637 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret145_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret145_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret145_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret145_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret145_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret145_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret145_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret145_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret145_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret145_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret145_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret145_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret145_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret145_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret145_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret145_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
