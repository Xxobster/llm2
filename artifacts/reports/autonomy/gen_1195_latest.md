# Autonomy public-indicator hunt gen 1195

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T094859Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma627_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0006 | 0.6842 | 4.3260 | 0.0243 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma627_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9812 | 0.6828 | 4.1385 | 0.0227 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma627_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 1.8723 | 0.6754 | 3.6752 | 0.0132 | 0.3403 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma627_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7131 | 0.6582 | 3.2376 | 0.0112 | 0.3163 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma627_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.6133 | 0.6138 | 2.4438 | 0.0096 | 0.3310 | ok | RAN |
| SOLUSDT | 8 | `sma627_above_at_h` | one_head_filter_pi_star | 164 | 13.4488 | 1.5698 | 0.6037 | 2.4327 | 0.0091 | 0.3049 | ok | RAN |
| ETHUSDT | 4 | `sma627_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1957 | 0.5990 | 1.0671 | 0.0072 | 0.2292 | ok | RAN |
| ETHUSDT | 8 | `sma627_above_at_h` | one_head_filter_pi_star | 154 | 12.6586 | 1.1690 | 0.6104 | 0.8397 | 0.0062 | 0.2208 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma627_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma627_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma627_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma627_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma627_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma627_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma627_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma627_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma627_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma627_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma627_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma627_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma627_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma627_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma627_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma627_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
