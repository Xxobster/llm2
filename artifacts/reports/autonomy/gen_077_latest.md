# Autonomy public-indicator hunt gen 077

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T143616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `stochd_ob_at_h` | one_head_filter_pi_star | 21 | 1.8692 | 5.4810 | 0.9048 | 3.0730 | 0.0862 | 0.4762 | EBR>35% | RAN |
| ETHUSDT | 4 | `stochd_os_at_h` | one_head_filter_pi_star | 21 | 1.8542 | 3.3068 | 0.8095 | 2.5788 | 0.0712 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 4 | `stochd_cross_up_20` | one_head_filter_pi_star | 41 | 3.4510 | 3.6992 | 0.8049 | 3.3140 | 0.0274 | 0.2927 | TPM<MIN | RAN |
| ETHUSDT | 4 | `stochd_cross_up_20` | one_head_filter_pi_star | 102 | 8.4372 | 1.9900 | 0.7255 | 3.1600 | 0.0244 | 0.4020 | EBR>35% | RAN |
| SOLUSDT | 4 | `stochd_os_at_h` | one_head_filter_pi_star | 19 | 1.9267 | 2.7201 | 0.7895 | 1.9975 | 0.0237 | 0.4737 | EBR>35% | RAN |
| ETHUSDT | 8 | `stochd_cross_up_20` | one_head_filter_pi_star | 161 | 13.1670 | 1.8145 | 0.7019 | 3.3343 | 0.0210 | 0.3727 | EBR>35% | RAN |
| SOLUSDT | 8 | `stochd_cross_up_20` | one_head_filter_pi_star | 134 | 10.9573 | 2.1982 | 0.7015 | 3.6186 | 0.0178 | 0.4179 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `stochd_ob_at_h` | one_head_filter_pi_star | 63 | 5.4761 | 1.6032 | 0.6349 | 1.7320 | 0.0133 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `stochd_cross_down_80` | one_head_filter_pi_star | 166 | 13.5357 | 1.2336 | 0.5663 | 1.2422 | 0.0036 | 0.2349 | ok | RAN |
| SOLUSDT | 4 | `stochd_cross_down_80` | one_head_filter_pi_star | 81 | 6.6048 | 1.0872 | 0.5556 | 0.3385 | 0.0015 | 0.1481 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `stochd_cross_down_80` | one_head_filter_pi_star | 114 | 9.4074 | 1.0357 | 0.5614 | 0.1634 | 0.0012 | 0.1579 | ok | RAN |
| ETHUSDT | 4 | `stochd_cross_down_80` | one_head_filter_pi_star | 57 | 4.7961 | 0.7741 | 0.4561 | -0.7990 | -0.0068 | 0.0702 | ok | RAN |
| BTCUSDT | 8 | `stochd_cross_down_80` | one_head_filter_pi_star | 15 | 1.2765 | 0.6208 | 0.2667 | -0.7097 | -0.0345 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `stochd_os_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `stochd_ob_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `stochd_os_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `stochd_ob_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stochd_os_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stochd_ob_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stochd_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `stochd_cross_down_80` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stochd_os_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stochd_ob_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `stochd_cross_up_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
