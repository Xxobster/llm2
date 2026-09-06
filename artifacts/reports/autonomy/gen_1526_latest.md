# Autonomy public-indicator hunt gen 1526

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T051547Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma416_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.1128 | 0.7088 | 4.6320 | 0.0255 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma416_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9830 | 0.6979 | 4.4241 | 0.0233 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma416_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1130 | 0.6868 | 4.1867 | 0.0161 | 0.3901 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma416_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1427 | 0.6914 | 4.1469 | 0.0160 | 0.3714 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma416_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2215 | 0.5873 | 1.1371 | 0.0078 | 0.2275 | ok | RAN |
| ETHUSDT | 8 | `wma416_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2241 | 0.6082 | 1.1610 | 0.0078 | 0.2165 | ok | RAN |
| SOLUSDT | 8 | `wma416_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.4178 | 0.6071 | 2.0970 | 0.0065 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `wma416_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3994 | 0.6000 | 1.9984 | 0.0063 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma416_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma416_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0451 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma416_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma416_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma416_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma416_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma416_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma416_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma416_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma416_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma416_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma416_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma416_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma416_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma416_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma416_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
