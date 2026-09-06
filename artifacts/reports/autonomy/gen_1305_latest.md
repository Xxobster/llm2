# Autonomy public-indicator hunt gen 1305

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T205151Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2820_below_at_h` | one_head_filter_pi_star | 359 | 29.2054 | 1.5925 | 0.6435 | 3.8036 | 0.0162 | 0.3036 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2820_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.6035 | 0.6431 | 3.5857 | 0.0160 | 0.3097 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2820_below_at_h` | one_head_filter_pi_star | 282 | 22.9413 | 1.8104 | 0.6454 | 4.1451 | 0.0126 | 0.3227 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2820_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.8073 | 0.6441 | 4.0979 | 0.0124 | 0.3310 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2820_above_at_h` | one_head_filter_pi_star | 97 | 7.9726 | 1.7289 | 0.6701 | 2.2666 | 0.0098 | 0.2577 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2820_above_at_h` | one_head_filter_pi_star | 99 | 8.1370 | 1.5573 | 0.6263 | 1.8638 | 0.0084 | 0.2828 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2820_above_at_h` | one_head_filter_pi_star | 33 | 3.8778 | 0.8789 | 0.4848 | -0.3649 | -0.0058 | 0.2121 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2820_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0284 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2820_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
