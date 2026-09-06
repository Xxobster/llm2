# Autonomy public-indicator hunt gen 1366

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T023028Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma760_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.2744 | 0.7158 | 4.9931 | 0.0277 | 0.3880 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma760_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9960 | 0.6825 | 4.3411 | 0.0232 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma760_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.8269 | 0.6699 | 3.5911 | 0.0124 | 0.3254 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma760_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7772 | 0.6599 | 3.3545 | 0.0119 | 0.3249 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma760_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5638 | 0.6175 | 2.5995 | 0.0088 | 0.2842 | ok | RAN |
| SOLUSDT | 4 | `wma760_above_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.5348 | 0.6140 | 2.4093 | 0.0085 | 0.3041 | ok | RAN |
| ETHUSDT | 8 | `wma760_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.2403 | 0.6023 | 1.1850 | 0.0084 | 0.2105 | ok | RAN |
| ETHUSDT | 4 | `wma760_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.2035 | 0.6057 | 1.0380 | 0.0075 | 0.2286 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma760_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma760_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
