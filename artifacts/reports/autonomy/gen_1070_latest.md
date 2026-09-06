# Autonomy public-indicator hunt gen 1070

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T191748Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma575_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9573 | 0.6898 | 4.2964 | 0.0231 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma575_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9494 | 0.6919 | 4.2581 | 0.0223 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma575_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.9808 | 0.6717 | 4.0153 | 0.0145 | 0.3485 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma575_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 1.8644 | 0.6617 | 3.7257 | 0.0132 | 0.3582 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma575_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2654 | 0.5979 | 1.3738 | 0.0090 | 0.2328 | ok | RAN |
| SOLUSDT | 4 | `wma575_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5410 | 0.6216 | 2.5383 | 0.0085 | 0.2649 | ok | RAN |
| SOLUSDT | 8 | `wma575_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4639 | 0.6094 | 2.2991 | 0.0071 | 0.2604 | ok | RAN |
| ETHUSDT | 4 | `wma575_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 1.1643 | 0.5866 | 0.8761 | 0.0061 | 0.2067 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma575_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma575_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma575_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma575_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma575_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma575_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
