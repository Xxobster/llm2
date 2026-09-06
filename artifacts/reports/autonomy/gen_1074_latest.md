# Autonomy public-indicator hunt gen 1074

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T194519Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret928_neg_at_h` | one_head_filter_pi_star | 159 | 13.0751 | 2.1723 | 0.7170 | 4.0999 | 0.0251 | 0.4151 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret928_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9834 | 0.6895 | 4.0331 | 0.0236 | 0.4053 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret928_neg_at_h` | one_head_filter_pi_star | 268 | 21.9459 | 1.8614 | 0.6493 | 4.2620 | 0.0128 | 0.3172 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret928_neg_at_h` | one_head_filter_pi_star | 279 | 22.6972 | 1.8358 | 0.6452 | 4.2236 | 0.0126 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret928_pos_at_h` | one_head_filter_pi_star | 45 | 3.7407 | 1.8524 | 0.6667 | 1.7420 | 0.0116 | 0.3111 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret928_pos_at_h` | one_head_filter_pi_star | 63 | 5.3932 | 1.2276 | 0.6190 | 0.7593 | 0.0102 | 0.2540 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret928_pos_at_h` | one_head_filter_pi_star | 29 | 2.5503 | 1.1718 | 0.5517 | 0.3526 | 0.0087 | 0.3103 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret928_pos_at_h` | one_head_filter_pi_star | 31 | 2.8249 | 1.2096 | 0.6129 | 0.5042 | 0.0037 | 0.1613 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret928_pos_at_h` | one_head_filter_pi_star | 12 | 2.2038 | 0.7079 | 0.4167 | -0.6785 | -0.0235 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret928_pos_at_h` | one_head_filter_pi_star | 15 | 2.7547 | 0.3050 | 0.2000 | -2.4047 | -0.0846 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret928_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret928_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret928_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret928_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret928_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret928_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret928_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret928_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret928_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret928_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret928_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret928_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret928_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret928_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
