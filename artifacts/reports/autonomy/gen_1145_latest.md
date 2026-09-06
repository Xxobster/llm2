# Autonomy public-indicator hunt gen 1145

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T041515Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2420_below_at_h` | one_head_filter_pi_star | 351 | 28.5545 | 1.5822 | 0.6410 | 3.5809 | 0.0156 | 0.2991 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema2420_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.5666 | 0.6385 | 3.4747 | 0.0152 | 0.3032 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2420_below_at_h` | one_head_filter_pi_star | 277 | 22.5345 | 1.8840 | 0.6498 | 4.3369 | 0.0130 | 0.3177 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2420_below_at_h` | one_head_filter_pi_star | 279 | 22.6972 | 1.8363 | 0.6487 | 4.1685 | 0.0127 | 0.3226 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema2420_above_at_h` | one_head_filter_pi_star | 36 | 3.4727 | 1.1963 | 0.5556 | 0.4777 | 0.0093 | 0.2778 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema2420_above_at_h` | one_head_filter_pi_star | 92 | 7.6464 | 1.5734 | 0.6413 | 1.8375 | 0.0090 | 0.2717 | ok | RAN |
| SOLUSDT | 4 | `ema2420_above_at_h` | one_head_filter_pi_star | 109 | 8.9589 | 1.4879 | 0.6330 | 1.7340 | 0.0074 | 0.2936 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2420_above_at_h` | one_head_filter_pi_star | 31 | 2.9904 | 1.0101 | 0.5161 | 0.0248 | 0.0005 | 0.2903 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2420_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6980 | 0.3158 | -0.6210 | -0.0297 | 0.1053 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2420_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
