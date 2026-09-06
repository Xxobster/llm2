# Autonomy public-indicator hunt gen 993

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T195043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2040_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0799 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2040_below_at_h` | one_head_filter_pi_star | 321 | 26.1140 | 1.6570 | 0.6449 | 3.6976 | 0.0168 | 0.3146 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2040_below_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.6255 | 0.6481 | 3.6085 | 0.0163 | 0.3086 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema2040_below_at_h` | one_head_filter_pi_star | 277 | 22.6505 | 1.8942 | 0.6534 | 4.4368 | 0.0135 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2040_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.8271 | 0.6496 | 4.1827 | 0.0130 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2040_above_at_h` | one_head_filter_pi_star | 98 | 7.9910 | 1.7256 | 0.6735 | 2.1612 | 0.0097 | 0.2551 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2040_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.5956 | 0.6306 | 2.0701 | 0.0084 | 0.2523 | ok | RAN |
| ETHUSDT | 4 | `ema2040_above_at_h` | one_head_filter_pi_star | 48 | 4.2211 | 1.2104 | 0.5625 | 0.5517 | 0.0081 | 0.2708 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2040_above_at_h` | one_head_filter_pi_star | 29 | 2.7975 | 0.8486 | 0.4828 | -0.3977 | -0.0079 | 0.3103 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2040_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0415 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2040_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0473 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2040_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2040_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2040_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
