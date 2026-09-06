# Autonomy public-indicator hunt gen 969

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T200720Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1980_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1980_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.7022 | 0.6481 | 3.9151 | 0.0180 | 0.3117 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1980_above_at_h` | one_head_filter_pi_star | 45 | 3.9573 | 1.4230 | 0.6000 | 0.9390 | 0.0157 | 0.2667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema1980_below_at_h` | one_head_filter_pi_star | 312 | 25.3818 | 1.5585 | 0.6410 | 3.2863 | 0.0149 | 0.3173 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1980_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 1.8809 | 0.6567 | 4.3654 | 0.0137 | 0.3284 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1980_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8261 | 0.6464 | 4.0653 | 0.0130 | 0.3270 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1980_above_at_h` | one_head_filter_pi_star | 60 | 5.2764 | 1.3066 | 0.5833 | 0.8896 | 0.0121 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1980_above_at_h` | one_head_filter_pi_star | 101 | 8.2356 | 1.6569 | 0.6535 | 2.0918 | 0.0092 | 0.2574 | ok | RAN |
| SOLUSDT | 4 | `ema1980_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.5779 | 0.6311 | 1.8828 | 0.0080 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1980_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0454 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1980_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
