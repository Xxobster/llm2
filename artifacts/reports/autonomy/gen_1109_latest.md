# Autonomy public-indicator hunt gen 1109

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T000846Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret202_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.1945 | 0.7076 | 4.7680 | 0.0269 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret202_neg_at_h` | one_head_filter_pi_star | 169 | 13.8058 | 2.2216 | 0.7101 | 4.7557 | 0.0265 | 0.3964 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret202_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1199 | 0.6975 | 3.9547 | 0.0162 | 0.3765 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret202_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.0138 | 0.6810 | 3.7272 | 0.0151 | 0.3804 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret202_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4606 | 0.6054 | 2.1719 | 0.0070 | 0.2865 | ok | RAN |
| SOLUSDT | 8 | `ret202_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4062 | 0.6050 | 2.0754 | 0.0065 | 0.2650 | ok | RAN |
| ETHUSDT | 8 | `ret202_pos_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1648 | 0.5926 | 0.8904 | 0.0061 | 0.2328 | ok | RAN |
| ETHUSDT | 4 | `ret202_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1476 | 0.5825 | 0.8020 | 0.0054 | 0.2371 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret202_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0449 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret202_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret202_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret202_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret202_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret202_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret202_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret202_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret202_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret202_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret202_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret202_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret202_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret202_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret202_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret202_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
