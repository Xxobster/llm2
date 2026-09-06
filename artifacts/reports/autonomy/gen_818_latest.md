# Autonomy public-indicator hunt gen 818

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T172219Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret672_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8697 | 0.6735 | 3.7317 | 0.0195 | 0.3673 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret672_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.7246 | 0.6648 | 3.3590 | 0.0170 | 0.3681 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret672_neg_at_h` | one_head_filter_pi_star | 197 | 16.2155 | 1.9512 | 0.6599 | 3.6905 | 0.0155 | 0.3249 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret672_neg_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.8565 | 0.6545 | 3.7303 | 0.0138 | 0.3364 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret672_pos_at_h` | one_head_filter_pi_star | 113 | 9.2666 | 1.8416 | 0.6814 | 2.7192 | 0.0113 | 0.2655 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret672_pos_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 1.2235 | 0.5984 | 0.9752 | 0.0089 | 0.2520 | ok | RAN |
| SOLUSDT | 4 | `ret672_pos_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.4986 | 0.6050 | 1.9491 | 0.0074 | 0.2521 | ok | RAN |
| ETHUSDT | 4 | `ret672_pos_at_h` | one_head_filter_pi_star | 131 | 10.8112 | 1.0790 | 0.5725 | 0.3617 | 0.0034 | 0.2443 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret672_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5653 | 0.2778 | -0.8933 | -0.0380 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret672_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0573 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret672_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret672_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret672_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret672_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
