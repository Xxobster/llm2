# Autonomy public-indicator hunt gen 1118

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T011210Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma605_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9940 | 0.6911 | 4.4629 | 0.0232 | 0.3874 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma605_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9781 | 0.6952 | 4.3117 | 0.0228 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma605_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.7832 | 0.6520 | 3.4730 | 0.0118 | 0.3529 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma605_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7425 | 0.6548 | 3.2703 | 0.0116 | 0.3401 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma605_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2542 | 0.6053 | 1.3305 | 0.0088 | 0.2211 | ok | RAN |
| SOLUSDT | 4 | `wma605_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5238 | 0.6150 | 2.4842 | 0.0083 | 0.2674 | ok | RAN |
| SOLUSDT | 8 | `wma605_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5095 | 0.6120 | 2.4056 | 0.0081 | 0.2732 | ok | RAN |
| ETHUSDT | 4 | `wma605_above_at_h` | one_head_filter_pi_star | 185 | 15.2665 | 1.1555 | 0.5892 | 0.8489 | 0.0057 | 0.2162 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma605_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma605_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma605_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma605_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma605_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma605_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
