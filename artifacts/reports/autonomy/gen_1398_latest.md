# Autonomy public-indicator hunt gen 1398

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T053300Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma780_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1914 | 0.6995 | 4.7485 | 0.0255 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma780_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.8237 | 0.6620 | 4.0026 | 0.0198 | 0.3474 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma780_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8825 | 0.6700 | 3.7481 | 0.0131 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma780_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.7470 | 0.6524 | 3.3760 | 0.0115 | 0.3286 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma780_above_at_h` | one_head_filter_pi_star | 174 | 14.2689 | 1.5986 | 0.6092 | 2.6179 | 0.0095 | 0.2931 | ok | RAN |
| SOLUSDT | 8 | `wma780_above_at_h` | one_head_filter_pi_star | 160 | 13.0465 | 1.4768 | 0.6000 | 2.0564 | 0.0075 | 0.3000 | ok | RAN |
| ETHUSDT | 8 | `wma780_above_at_h` | one_head_filter_pi_star | 157 | 12.9559 | 1.2028 | 0.5924 | 0.9844 | 0.0072 | 0.1975 | ok | RAN |
| ETHUSDT | 4 | `wma780_above_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.1262 | 0.5988 | 0.6489 | 0.0047 | 0.2099 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma780_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma780_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
