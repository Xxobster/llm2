# Autonomy public-indicator hunt gen 801

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T154607Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1560_below_at_h` | one_head_filter_pi_star | 298 | 24.3439 | 1.6694 | 0.6510 | 3.7971 | 0.0169 | 0.3255 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1560_below_at_h` | one_head_filter_pi_star | 311 | 25.4059 | 1.5678 | 0.6431 | 3.4175 | 0.0151 | 0.3183 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1560_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.7353 | 0.6406 | 3.9078 | 0.0118 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1560_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 1.7193 | 0.6388 | 3.9293 | 0.0113 | 0.3177 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1560_above_at_h` | one_head_filter_pi_star | 101 | 8.2370 | 1.6373 | 0.6733 | 2.0343 | 0.0090 | 0.2475 | ok | RAN |
| ETHUSDT | 4 | `ema1560_above_at_h` | one_head_filter_pi_star | 43 | 3.7814 | 1.1736 | 0.5814 | 0.4524 | 0.0072 | 0.2326 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1560_above_at_h` | one_head_filter_pi_star | 101 | 8.2356 | 1.4337 | 0.6337 | 1.5125 | 0.0070 | 0.2673 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1560_above_at_h` | one_head_filter_pi_star | 41 | 3.6056 | 1.0108 | 0.5610 | 0.0296 | 0.0005 | 0.2927 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1560_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0423 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1560_above_at_h` | one_head_filter_pi_star | 12 | 1.0212 | 0.4436 | 0.2500 | -1.0639 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
