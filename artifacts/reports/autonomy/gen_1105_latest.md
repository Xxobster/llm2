# Autonomy public-indicator hunt gen 1105

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T234146Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2320_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2320_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6405 | 0.6462 | 3.7892 | 0.0167 | 0.3012 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2320_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 1.5816 | 0.6400 | 3.6765 | 0.0157 | 0.3000 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2320_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.9130 | 0.6554 | 4.3680 | 0.0139 | 0.3296 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2320_below_at_h` | one_head_filter_pi_star | 276 | 22.4531 | 1.8322 | 0.6413 | 4.1602 | 0.0125 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2320_above_at_h` | one_head_filter_pi_star | 93 | 7.6438 | 1.7830 | 0.6452 | 2.3313 | 0.0111 | 0.2688 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2320_above_at_h` | one_head_filter_pi_star | 110 | 9.0411 | 1.6822 | 0.6455 | 2.2248 | 0.0095 | 0.2727 | GATE_CAND | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2320_above_at_h` | one_head_filter_pi_star | 22 | 2.5852 | 0.6497 | 0.3636 | -0.9431 | -0.0224 | 0.2727 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2320_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0308 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2320_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6366 | 0.3125 | -0.7061 | -0.0370 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2320_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2320_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2320_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2320_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
