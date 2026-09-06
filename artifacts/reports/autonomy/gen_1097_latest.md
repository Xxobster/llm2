# Autonomy public-indicator hunt gen 1097

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T224137Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2300_below_at_h` | one_head_filter_pi_star | 327 | 26.6021 | 1.6177 | 0.6422 | 3.6187 | 0.0161 | 0.3089 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2300_below_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 1.5759 | 0.6400 | 3.6653 | 0.0158 | 0.3029 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2300_below_at_h` | one_head_filter_pi_star | 281 | 22.8599 | 1.8504 | 0.6477 | 4.2545 | 0.0130 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2300_below_at_h` | one_head_filter_pi_star | 279 | 22.6972 | 1.7882 | 0.6416 | 3.9681 | 0.0117 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2300_above_at_h` | one_head_filter_pi_star | 105 | 8.6301 | 1.6481 | 0.6381 | 2.1369 | 0.0095 | 0.2667 | ok | RAN |
| SOLUSDT | 4 | `ema2300_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.5175 | 0.6111 | 1.7615 | 0.0076 | 0.2593 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2300_above_at_h` | one_head_filter_pi_star | 27 | 3.1728 | 1.0014 | 0.4815 | 0.0037 | 0.0001 | 0.4074 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema2300_above_at_h` | one_head_filter_pi_star | 22 | 2.5852 | 0.9081 | 0.4091 | -0.2419 | -0.0044 | 0.3182 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2300_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4384 | 0.2500 | -1.2254 | -0.0627 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2300_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4390 | 0.2667 | -1.2223 | -0.0698 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
