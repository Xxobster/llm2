# Autonomy public-indicator hunt gen 998

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T095213Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma530_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9734 | 0.6904 | 4.4823 | 0.0229 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma530_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9541 | 0.6952 | 4.2521 | 0.0227 | 0.3850 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma530_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.1362 | 0.6875 | 4.4111 | 0.0159 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma530_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.9692 | 0.6700 | 4.0584 | 0.0141 | 0.3498 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma530_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.1995 | 0.5882 | 1.0770 | 0.0072 | 0.2246 | ok | RAN |
| ETHUSDT | 4 | `wma530_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2038 | 0.5907 | 1.0948 | 0.0071 | 0.2176 | ok | RAN |
| SOLUSDT | 4 | `wma530_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4401 | 0.6064 | 2.1555 | 0.0071 | 0.2606 | ok | RAN |
| SOLUSDT | 8 | `wma530_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4300 | 0.6071 | 2.1628 | 0.0069 | 0.2551 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma530_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma530_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma530_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma530_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma530_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma530_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma530_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma530_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma530_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma530_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma530_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma530_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma530_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma530_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma530_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma530_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
