# Autonomy public-indicator hunt gen 1046

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T160729Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma560_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.9820 | 0.6906 | 4.3221 | 0.0235 | 0.3867 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma560_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8119 | 0.6717 | 3.9161 | 0.0201 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma560_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 2.0078 | 0.6845 | 3.9981 | 0.0145 | 0.3583 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma560_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8850 | 0.6633 | 3.7179 | 0.0133 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma560_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2581 | 0.6043 | 1.3390 | 0.0091 | 0.2193 | ok | RAN |
| ETHUSDT | 8 | `wma560_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2158 | 0.5936 | 1.1523 | 0.0075 | 0.2139 | ok | RAN |
| SOLUSDT | 8 | `wma560_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.4710 | 0.6011 | 2.2668 | 0.0074 | 0.2606 | ok | RAN |
| SOLUSDT | 4 | `wma560_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.4151 | 0.5947 | 2.0819 | 0.0068 | 0.2684 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma560_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma560_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
