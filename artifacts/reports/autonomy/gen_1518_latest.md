# Autonomy public-indicator hunt gen 1518

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T042700Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma414_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9997 | 0.6968 | 4.4243 | 0.0238 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma414_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9784 | 0.7027 | 4.2952 | 0.0232 | 0.3838 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma414_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.3171 | 0.6994 | 4.4669 | 0.0177 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma414_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1842 | 0.6949 | 4.2479 | 0.0166 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma414_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2497 | 0.5989 | 1.2936 | 0.0085 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `wma414_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2264 | 0.6010 | 1.2138 | 0.0078 | 0.2176 | ok | RAN |
| SOLUSDT | 4 | `wma414_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4019 | 0.6000 | 1.9581 | 0.0063 | 0.2649 | ok | RAN |
| SOLUSDT | 8 | `wma414_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3875 | 0.6051 | 1.9491 | 0.0060 | 0.2564 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma414_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma414_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma414_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma414_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma414_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma414_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma414_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma414_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma414_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma414_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma414_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma414_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma414_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma414_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma414_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma414_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
