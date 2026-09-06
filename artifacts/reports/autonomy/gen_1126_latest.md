# Autonomy public-indicator hunt gen 1126

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T020611Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma610_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9842 | 0.6862 | 4.3033 | 0.0228 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma610_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9711 | 0.6927 | 4.3560 | 0.0222 | 0.3802 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma610_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.9309 | 0.6701 | 3.8654 | 0.0137 | 0.3660 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma610_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8614 | 0.6633 | 3.6690 | 0.0132 | 0.3469 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma610_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2552 | 0.6023 | 1.2927 | 0.0089 | 0.2159 | ok | RAN |
| SOLUSDT | 4 | `wma610_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5317 | 0.6108 | 2.4589 | 0.0083 | 0.2703 | ok | RAN |
| SOLUSDT | 8 | `wma610_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4799 | 0.6054 | 2.3140 | 0.0077 | 0.2649 | ok | RAN |
| ETHUSDT | 4 | `wma610_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.1816 | 0.5833 | 0.9628 | 0.0067 | 0.1944 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma610_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma610_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma610_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma610_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma610_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma610_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
