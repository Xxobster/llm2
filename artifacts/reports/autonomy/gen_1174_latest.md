# Autonomy public-indicator hunt gen 1174

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T074702Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma640_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1981 | 0.7127 | 4.8193 | 0.0261 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma640_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1774 | 0.7059 | 4.7570 | 0.0254 | 0.3690 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma640_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8355 | 0.6600 | 3.6092 | 0.0127 | 0.3400 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma640_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8545 | 0.6650 | 3.5784 | 0.0127 | 0.3450 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma640_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.2457 | 0.5967 | 1.2672 | 0.0086 | 0.2210 | ok | RAN |
| SOLUSDT | 8 | `wma640_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5310 | 0.6141 | 2.4997 | 0.0084 | 0.2609 | ok | RAN |
| SOLUSDT | 4 | `wma640_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.4939 | 0.6102 | 2.2697 | 0.0078 | 0.2768 | ok | RAN |
| ETHUSDT | 4 | `wma640_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2129 | 0.5946 | 1.1066 | 0.0075 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma640_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma640_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
