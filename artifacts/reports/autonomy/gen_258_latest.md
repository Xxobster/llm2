# Autonomy public-indicator hunt gen 258

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T023145Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret112_neg_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.7463 | 0.6633 | 3.6924 | 0.0193 | 0.3568 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret112_neg_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.2330 | 0.6898 | 4.5115 | 0.0171 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret112_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.6525 | 0.6510 | 3.1931 | 0.0170 | 0.3438 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret112_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1930 | 0.6786 | 4.1066 | 0.0167 | 0.3631 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret112_pos_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.4786 | 0.6354 | 2.1809 | 0.0146 | 0.2431 | ok | RAN |
| ETHUSDT | 4 | `ret112_pos_at_h` | one_head_filter_pi_star | 194 | 16.0092 | 1.4127 | 0.6340 | 2.0368 | 0.0135 | 0.2526 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret112_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4179 | 0.6042 | 2.0782 | 0.0065 | 0.2604 | ok | RAN |
| SOLUSDT | 4 | `ret112_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.3697 | 0.5932 | 1.8178 | 0.0060 | 0.2712 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret112_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret112_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret112_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret112_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret112_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret112_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
