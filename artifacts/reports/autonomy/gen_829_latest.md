# Autonomy public-indicator hunt gen 829

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T182433Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret155_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0037 | 0.7011 | 4.4952 | 0.0241 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret155_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.9326 | 0.6848 | 4.2443 | 0.0232 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret155_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2420 | 0.6882 | 4.2975 | 0.0169 | 0.3824 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret155_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.1199 | 0.6761 | 4.1096 | 0.0164 | 0.3693 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret155_pos_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2441 | 0.6071 | 1.2631 | 0.0083 | 0.2398 | ok | RAN |
| ETHUSDT | 8 | `ret155_pos_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.2370 | 0.6000 | 1.2204 | 0.0082 | 0.2324 | ok | RAN |
| SOLUSDT | 8 | `ret155_pos_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.3293 | 0.5847 | 1.6287 | 0.0054 | 0.2678 | ok | RAN |
| SOLUSDT | 4 | `ret155_pos_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.3237 | 0.5820 | 1.6075 | 0.0054 | 0.2593 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret155_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret155_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret155_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret155_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret155_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret155_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret155_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret155_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret155_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret155_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret155_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret155_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret155_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret155_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret155_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret155_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
