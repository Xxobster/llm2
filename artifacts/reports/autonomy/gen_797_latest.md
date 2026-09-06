# Autonomy public-indicator hunt gen 797

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T152409Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret147_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9754 | 0.6878 | 4.4131 | 0.0232 | 0.3862 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret147_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8209 | 0.6667 | 3.8934 | 0.0206 | 0.3636 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret147_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0983 | 0.6720 | 4.0975 | 0.0155 | 0.3548 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret147_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.0145 | 0.6722 | 3.8608 | 0.0147 | 0.3667 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret147_pos_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.1869 | 0.6022 | 0.9633 | 0.0066 | 0.2155 | ok | RAN |
| ETHUSDT | 4 | `ret147_pos_at_h` | one_head_filter_pi_star | 192 | 15.8441 | 1.1908 | 0.6042 | 1.0205 | 0.0066 | 0.2240 | ok | RAN |
| SOLUSDT | 8 | `ret147_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3488 | 0.5978 | 1.7075 | 0.0056 | 0.2554 | ok | RAN |
| SOLUSDT | 4 | `ret147_pos_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3456 | 0.5979 | 1.7488 | 0.0055 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret147_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret147_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret147_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret147_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret147_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret147_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret147_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret147_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret147_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret147_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret147_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret147_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret147_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret147_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret147_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret147_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
