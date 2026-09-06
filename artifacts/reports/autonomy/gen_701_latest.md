# Autonomy public-indicator hunt gen 701

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T071427Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret123_neg_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9167 | 0.6821 | 4.2048 | 0.0221 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret123_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.8681 | 0.6771 | 3.9496 | 0.0215 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret123_neg_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 2.2748 | 0.6859 | 4.6094 | 0.0169 | 0.3665 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret123_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2048 | 0.6798 | 4.2580 | 0.0163 | 0.3596 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret123_pos_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.5070 | 0.6374 | 2.1798 | 0.0154 | 0.2281 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret123_pos_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.3885 | 0.6271 | 1.7970 | 0.0125 | 0.2260 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret123_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.3953 | 0.6034 | 1.9157 | 0.0064 | 0.2586 | ok | RAN |
| SOLUSDT | 4 | `ret123_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.3857 | 0.6054 | 1.9248 | 0.0064 | 0.2703 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret123_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret123_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret123_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret123_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret123_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret123_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret123_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret123_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret123_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret123_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret123_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret123_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret123_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret123_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret123_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret123_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
