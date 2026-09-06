# Autonomy public-indicator hunt gen 1302

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T203218Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma720_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1331 | 0.7037 | 4.7373 | 0.0249 | 0.3651 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma720_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.9378 | 0.6850 | 4.2651 | 0.0224 | 0.3700 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma720_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8845 | 0.6716 | 3.7870 | 0.0135 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma720_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8250 | 0.6719 | 3.4945 | 0.0127 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma720_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2816 | 0.6062 | 1.3453 | 0.0097 | 0.2250 | ok | RAN |
| ETHUSDT | 4 | `wma720_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2589 | 0.6136 | 1.2991 | 0.0089 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `wma720_above_at_h` | one_head_filter_pi_star | 168 | 13.6988 | 1.5465 | 0.6131 | 2.3720 | 0.0083 | 0.2798 | ok | RAN |
| SOLUSDT | 4 | `wma720_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5085 | 0.6045 | 2.3081 | 0.0083 | 0.2938 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma720_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma720_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
