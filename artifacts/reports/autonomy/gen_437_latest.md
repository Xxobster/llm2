# Autonomy public-indicator hunt gen 437

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T110816Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret57_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.7908 | 0.6845 | 3.9338 | 0.0205 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret57_neg_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.6861 | 0.6702 | 3.4485 | 0.0188 | 0.3717 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret57_neg_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1921 | 0.6894 | 4.1247 | 0.0173 | 0.3913 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret57_neg_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.0410 | 0.6848 | 3.8262 | 0.0164 | 0.3818 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret57_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.3112 | 0.6073 | 1.5161 | 0.0096 | 0.2356 | ok | RAN |
| ETHUSDT | 8 | `ret57_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2592 | 0.5934 | 1.2929 | 0.0082 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `ret57_pos_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3538 | 0.5941 | 1.8637 | 0.0052 | 0.2525 | ok | RAN |
| SOLUSDT | 4 | `ret57_pos_at_h` | one_head_filter_pi_star | 204 | 16.6342 | 1.2854 | 0.5784 | 1.5578 | 0.0044 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret57_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret57_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret57_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret57_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret57_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret57_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret57_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret57_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret57_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret57_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret57_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret57_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret57_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret57_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret57_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret57_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
