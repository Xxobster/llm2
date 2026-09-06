# Autonomy public-indicator hunt gen 1273

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T173924Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2740_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2740_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.6570 | 0.6465 | 3.8046 | 0.0170 | 0.3112 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2740_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 1.6047 | 0.6426 | 3.5512 | 0.0159 | 0.3093 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2740_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 2.0047 | 0.6630 | 4.7368 | 0.0142 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2740_below_at_h` | one_head_filter_pi_star | 268 | 21.8023 | 1.8526 | 0.6493 | 4.2058 | 0.0128 | 0.3396 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2740_above_at_h` | one_head_filter_pi_star | 107 | 8.7745 | 1.8127 | 0.6542 | 2.5235 | 0.0115 | 0.2523 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2740_above_at_h` | one_head_filter_pi_star | 104 | 8.6437 | 1.4671 | 0.6154 | 1.6127 | 0.0074 | 0.2596 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2740_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0290 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2740_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
