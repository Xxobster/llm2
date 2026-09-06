# Autonomy public-indicator hunt gen 992

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T192453Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `sma2080_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2080_below_at_h` | one_head_filter_pi_star | 326 | 26.5207 | 1.6234 | 0.6472 | 3.7000 | 0.0166 | 0.3190 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2080_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6170 | 0.6420 | 3.7138 | 0.0164 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma2080_above_at_h` | one_head_filter_pi_star | 40 | 3.3251 | 1.8092 | 0.6750 | 1.7119 | 0.0136 | 0.3000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma2080_below_at_h` | one_head_filter_pi_star | 299 | 24.3242 | 1.8085 | 0.6421 | 4.2549 | 0.0122 | 0.3144 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2080_above_at_h` | one_head_filter_pi_star | 59 | 4.9045 | 1.8233 | 0.6780 | 1.9702 | 0.0115 | 0.2881 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2080_above_at_h` | one_head_filter_pi_star | 46 | 4.1611 | 1.3087 | 0.5652 | 0.7756 | 0.0114 | 0.2609 | ok | RAN |
| SOLUSDT | 4 | `sma2080_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7510 | 0.6340 | 3.9751 | 0.0113 | 0.3203 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2080_above_at_h` | one_head_filter_pi_star | 57 | 4.7961 | 1.2709 | 0.5965 | 0.7712 | 0.0110 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2080_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3356 | 0.2308 | -1.4359 | -0.0867 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2080_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
