# Autonomy public-indicator hunt gen 1333

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T232431Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret234_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1878 | 0.7005 | 4.7559 | 0.0265 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret234_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.0825 | 0.6994 | 4.4132 | 0.0250 | 0.3699 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret234_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.9874 | 0.6667 | 3.9406 | 0.0148 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret234_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 1.7341 | 0.6364 | 3.1430 | 0.0116 | 0.3369 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret234_pos_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.2886 | 0.6149 | 1.3717 | 0.0103 | 0.2484 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret234_pos_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.5236 | 0.6168 | 2.2126 | 0.0078 | 0.2575 | ok | RAN |
| ETHUSDT | 8 | `ret234_pos_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.2070 | 0.6069 | 1.0320 | 0.0076 | 0.2312 | ok | RAN |
| SOLUSDT | 8 | `ret234_pos_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.4389 | 0.6047 | 2.0225 | 0.0069 | 0.2674 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret234_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret234_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret234_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret234_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret234_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret234_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret234_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret234_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret234_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret234_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret234_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret234_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret234_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret234_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret234_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret234_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
