# Autonomy public-indicator hunt gen 1009

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T113026Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2080_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0799 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2080_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.5902 | 0.6414 | 3.6296 | 0.0160 | 0.3032 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2080_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5967 | 0.6407 | 3.5531 | 0.0157 | 0.3054 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2080_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 1.9316 | 0.6587 | 4.3541 | 0.0145 | 0.3373 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2080_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 1.8508 | 0.6481 | 4.2149 | 0.0135 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2080_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.6443 | 0.6381 | 2.0981 | 0.0089 | 0.2476 | ok | RAN |
| SOLUSDT | 4 | `ema2080_above_at_h` | one_head_filter_pi_star | 102 | 8.3840 | 1.6697 | 0.6667 | 2.0576 | 0.0088 | 0.2745 | GATE_CAND | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2080_above_at_h` | one_head_filter_pi_star | 30 | 2.8939 | 0.8266 | 0.4667 | -0.4470 | -0.0090 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2080_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4384 | 0.2500 | -1.2254 | -0.0640 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2080_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.5084 | 0.2667 | -0.9862 | -0.0646 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2080_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
