# Autonomy public-indicator hunt gen 1313

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T213526Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2840_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.5945 | 0.6404 | 3.5475 | 0.0158 | 0.3041 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2840_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5881 | 0.6422 | 3.5858 | 0.0157 | 0.3050 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2840_below_at_h` | one_head_filter_pi_star | 277 | 22.5345 | 1.8834 | 0.6498 | 4.3634 | 0.0133 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2840_below_at_h` | one_head_filter_pi_star | 280 | 22.8958 | 1.8218 | 0.6464 | 4.1801 | 0.0124 | 0.3286 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2840_above_at_h` | one_head_filter_pi_star | 105 | 8.6301 | 1.5496 | 0.6381 | 1.8582 | 0.0084 | 0.2667 | ok | RAN |
| SOLUSDT | 4 | `ema2840_above_at_h` | one_head_filter_pi_star | 97 | 7.9726 | 1.3728 | 0.6186 | 1.2781 | 0.0059 | 0.2474 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2840_above_at_h` | one_head_filter_pi_star | 12 | 3.6212 | 0.6065 | 0.3333 | -1.5130 | -0.0244 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2840_above_at_h` | one_head_filter_pi_star | 13 | 4.0514 | 0.4170 | 0.2308 | -2.5778 | -0.0390 | 0.3077 | ok | RAN |
| ETHUSDT | 4 | `ema2840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2840_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2840_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2840_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2840_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2840_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
