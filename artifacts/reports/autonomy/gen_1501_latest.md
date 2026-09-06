# Autonomy public-indicator hunt gen 1501

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T025324Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret258_neg_at_h` | one_head_filter_pi_star | 159 | 12.9888 | 2.3683 | 0.7296 | 4.8039 | 0.0292 | 0.4025 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret258_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 2.3909 | 0.7125 | 4.6358 | 0.0288 | 0.3937 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret258_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 1.8823 | 0.6648 | 3.6863 | 0.0135 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret258_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.8824 | 0.6559 | 3.6937 | 0.0133 | 0.3387 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret258_pos_at_h` | one_head_filter_pi_star | 169 | 13.8588 | 1.5623 | 0.6272 | 2.4737 | 0.0089 | 0.2840 | ok | RAN |
| ETHUSDT | 4 | `ret258_pos_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2218 | 0.5966 | 1.1271 | 0.0078 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `ret258_pos_at_h` | one_head_filter_pi_star | 189 | 15.4989 | 1.4987 | 0.6138 | 2.3551 | 0.0077 | 0.2804 | ok | RAN |
| ETHUSDT | 8 | `ret258_pos_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.1846 | 0.6000 | 0.9192 | 0.0063 | 0.2242 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret258_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret258_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret258_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret258_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret258_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret258_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret258_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret258_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret258_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret258_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret258_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret258_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret258_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret258_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret258_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret258_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
