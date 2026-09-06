# Autonomy public-indicator hunt gen 224

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T001049Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma140_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 1.8955 | 0.6866 | 4.2443 | 0.0215 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma140_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.7907 | 0.6737 | 3.8085 | 0.0199 | 0.3789 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma140_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.3012 | 0.7022 | 4.5191 | 0.0177 | 0.3764 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma140_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2347 | 0.6932 | 4.3336 | 0.0173 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma140_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2402 | 0.6033 | 1.2080 | 0.0082 | 0.2174 | ok | RAN |
| ETHUSDT | 4 | `sma140_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.2302 | 0.6022 | 1.1629 | 0.0079 | 0.2204 | ok | RAN |
| SOLUSDT | 8 | `sma140_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3732 | 0.6051 | 1.9075 | 0.0059 | 0.2615 | ok | RAN |
| SOLUSDT | 4 | `sma140_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3248 | 0.5918 | 1.6898 | 0.0052 | 0.2653 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma140_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma140_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
