# Autonomy public-indicator hunt gen 358

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T161835Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma130_cross_up` | one_head_filter_pi_star | 11 | 0.9345 | 3.5173 | 0.7273 | 1.6311 | 0.0327 | 0.1818 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma130_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9510 | 0.6884 | 4.4072 | 0.0231 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma130_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.8951 | 0.6900 | 4.2401 | 0.0224 | 0.3650 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma130_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2867 | 0.6964 | 4.3624 | 0.0188 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma130_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2851 | 0.6946 | 4.3535 | 0.0187 | 0.4072 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `wma130_above_at_h` | one_head_filter_pi_star | 174 | 14.3587 | 1.3578 | 0.6149 | 1.6384 | 0.0108 | 0.2184 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma130_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2440 | 0.6000 | 1.1870 | 0.0078 | 0.2324 | ok | RAN |
| SOLUSDT | 4 | `wma130_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3051 | 0.5905 | 1.6306 | 0.0047 | 0.2524 | ok | RAN |
| SOLUSDT | 8 | `wma130_above_at_h` | one_head_filter_pi_star | 213 | 17.3681 | 1.3081 | 0.5915 | 1.6531 | 0.0046 | 0.2535 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma130_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma130_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `wma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma130_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma130_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma130_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma130_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
