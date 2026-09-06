# Autonomy public-indicator hunt gen 1254

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T154406Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma690_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1075 | 0.7021 | 4.5750 | 0.0253 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma690_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0351 | 0.6911 | 4.4304 | 0.0236 | 0.3770 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma690_below_at_h` | one_head_filter_pi_star | 198 | 16.1906 | 1.8347 | 0.6667 | 3.6154 | 0.0128 | 0.3485 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma690_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8353 | 0.6633 | 3.5476 | 0.0128 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma690_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.5537 | 0.6190 | 2.6299 | 0.0090 | 0.2804 | ok | RAN |
| SOLUSDT | 4 | `wma690_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5704 | 0.6136 | 2.5687 | 0.0089 | 0.2955 | ok | RAN |
| ETHUSDT | 8 | `wma690_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.2189 | 0.6033 | 1.1489 | 0.0078 | 0.2120 | ok | RAN |
| ETHUSDT | 4 | `wma690_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2046 | 0.6011 | 1.0750 | 0.0072 | 0.2191 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma690_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma690_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma690_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma690_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma690_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma690_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
