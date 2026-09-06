# Autonomy public-indicator hunt gen 712

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T080222Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1380_below_at_h` | one_head_filter_pi_star | 249 | 20.3410 | 1.7190 | 0.6506 | 3.6837 | 0.0180 | 0.3293 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1380_below_at_h` | one_head_filter_pi_star | 263 | 21.4847 | 1.6954 | 0.6540 | 3.7350 | 0.0179 | 0.3346 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1380_above_at_h` | one_head_filter_pi_star | 66 | 5.4864 | 1.9664 | 0.6970 | 2.3510 | 0.0128 | 0.3030 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1380_below_at_h` | one_head_filter_pi_star | 295 | 24.1224 | 1.7967 | 0.6407 | 4.1820 | 0.0119 | 0.3153 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1380_below_at_h` | one_head_filter_pi_star | 309 | 25.2672 | 1.7818 | 0.6375 | 4.2050 | 0.0116 | 0.3236 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1380_above_at_h` | one_head_filter_pi_star | 67 | 5.5078 | 1.4569 | 0.6418 | 1.3042 | 0.0068 | 0.2836 | ok | RAN |
| ETHUSDT | 8 | `sma1380_above_at_h` | one_head_filter_pi_star | 99 | 8.1703 | 1.1631 | 0.5657 | 0.6453 | 0.0067 | 0.2121 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1380_above_at_h` | one_head_filter_pi_star | 97 | 8.0053 | 0.9800 | 0.5567 | -0.0874 | -0.0009 | 0.2165 | ok | RAN |
| BTCUSDT | 4 | `sma1380_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4938 | 0.3125 | -1.0772 | -0.0541 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1380_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3256 | 0.2667 | -1.5225 | -0.0801 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
