# Autonomy public-indicator hunt gen 477

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T162450Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret67_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7787 | 0.6802 | 3.8464 | 0.0206 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret67_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7831 | 0.6751 | 3.7967 | 0.0204 | 0.3655 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret67_neg_at_h` | one_head_filter_pi_star | 184 | 15.0458 | 2.2892 | 0.6957 | 4.5338 | 0.0180 | 0.3859 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret67_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2626 | 0.6954 | 4.3611 | 0.0177 | 0.3908 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret67_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.3304 | 0.6096 | 1.6163 | 0.0103 | 0.2299 | ok | RAN |
| ETHUSDT | 4 | `ret67_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.3247 | 0.6243 | 1.6356 | 0.0102 | 0.2328 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret67_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4198 | 0.6150 | 2.1631 | 0.0062 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ret67_pos_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.2990 | 0.5969 | 1.6012 | 0.0047 | 0.2551 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret67_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret67_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret67_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret67_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret67_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret67_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret67_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret67_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret67_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret67_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret67_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret67_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret67_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret67_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret67_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret67_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
