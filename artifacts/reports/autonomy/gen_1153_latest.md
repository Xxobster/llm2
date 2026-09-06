# Autonomy public-indicator hunt gen 1153

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T052008Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2440_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2440_below_at_h` | one_head_filter_pi_star | 347 | 28.2291 | 1.5849 | 0.6427 | 3.6007 | 0.0156 | 0.3026 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2440_below_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.5870 | 0.6406 | 3.5447 | 0.0156 | 0.3014 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2440_below_at_h` | one_head_filter_pi_star | 273 | 22.2091 | 1.8612 | 0.6520 | 4.2671 | 0.0129 | 0.3260 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2440_below_at_h` | one_head_filter_pi_star | 272 | 22.1277 | 1.8302 | 0.6507 | 4.0793 | 0.0122 | 0.3272 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2440_above_at_h` | one_head_filter_pi_star | 110 | 9.0411 | 1.7828 | 0.6636 | 2.4642 | 0.0107 | 0.2545 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2440_above_at_h` | one_head_filter_pi_star | 108 | 8.8565 | 1.6572 | 0.6389 | 2.1841 | 0.0098 | 0.2685 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2440_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0290 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2440_above_at_h` | one_head_filter_pi_star | 16 | 4.8283 | 0.4317 | 0.2500 | -2.7486 | -0.0405 | 0.2500 | ok | RAN |
| BTCUSDT | 8 | `ema2440_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4581 | 0.3125 | -1.1797 | -0.0591 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
