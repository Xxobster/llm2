# Autonomy public-indicator hunt gen 1281

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T182355Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2760_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0833 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema2760_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5479 | 0.6364 | 3.4213 | 0.0149 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2760_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5335 | 0.6364 | 3.3583 | 0.0148 | 0.2991 | ok | RAN |
| SOLUSDT | 8 | `ema2760_below_at_h` | one_head_filter_pi_star | 263 | 21.3956 | 1.9440 | 0.6578 | 4.5008 | 0.0138 | 0.3422 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2760_below_at_h` | one_head_filter_pi_star | 282 | 22.9413 | 1.7871 | 0.6383 | 3.9973 | 0.0121 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2760_above_at_h` | one_head_filter_pi_star | 91 | 7.5633 | 1.7672 | 0.6703 | 2.2472 | 0.0106 | 0.2527 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2760_above_at_h` | one_head_filter_pi_star | 113 | 9.3918 | 1.6442 | 0.6549 | 2.2186 | 0.0102 | 0.2566 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2760_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0290 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2760_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0290 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2760_above_at_h` | one_head_filter_pi_star | 12 | 3.7398 | 0.2809 | 0.1667 | -3.3710 | -0.0586 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2760_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
