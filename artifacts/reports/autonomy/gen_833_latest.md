# Autonomy public-indicator hunt gen 833

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T184713Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1640_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1640_below_at_h` | one_head_filter_pi_star | 306 | 24.9974 | 1.6548 | 0.6503 | 3.6602 | 0.0166 | 0.3170 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1640_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.5835 | 0.6407 | 3.5693 | 0.0156 | 0.3084 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1640_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 1.8051 | 0.6479 | 4.0833 | 0.0127 | 0.3221 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1640_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.8002 | 0.6496 | 4.1549 | 0.0124 | 0.3248 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1640_above_at_h` | one_head_filter_pi_star | 81 | 6.6048 | 1.5651 | 0.6543 | 1.6507 | 0.0080 | 0.2716 | ok | RAN |
| SOLUSDT | 8 | `ema1640_above_at_h` | one_head_filter_pi_star | 86 | 7.0136 | 1.5345 | 0.6512 | 1.6204 | 0.0077 | 0.2558 | ok | RAN |
| ETHUSDT | 8 | `ema1640_above_at_h` | one_head_filter_pi_star | 58 | 4.9354 | 1.1909 | 0.5690 | 0.5566 | 0.0072 | 0.2241 | ok | RAN |
| ETHUSDT | 4 | `ema1640_above_at_h` | one_head_filter_pi_star | 43 | 3.7814 | 1.0860 | 0.5581 | 0.2258 | 0.0033 | 0.2558 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1640_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1640_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4384 | 0.2500 | -1.2254 | -0.0654 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
