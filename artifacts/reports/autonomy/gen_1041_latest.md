# Autonomy public-indicator hunt gen 1041

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T153413Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2160_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0799 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2160_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6322 | 0.6450 | 3.7231 | 0.0165 | 0.3047 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2160_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5854 | 0.6388 | 3.5057 | 0.0157 | 0.3045 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2160_below_at_h` | one_head_filter_pi_star | 276 | 22.4531 | 1.8276 | 0.6486 | 4.1544 | 0.0128 | 0.3297 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2160_below_at_h` | one_head_filter_pi_star | 277 | 22.6505 | 1.7980 | 0.6498 | 4.0755 | 0.0127 | 0.3285 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2160_above_at_h` | one_head_filter_pi_star | 111 | 9.1233 | 1.6288 | 0.6486 | 2.1576 | 0.0087 | 0.2613 | ok | RAN |
| SOLUSDT | 4 | `ema2160_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.6243 | 0.6429 | 2.0285 | 0.0083 | 0.2589 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2160_above_at_h` | one_head_filter_pi_star | 32 | 3.6477 | 0.9717 | 0.5000 | -0.0775 | -0.0012 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2160_above_at_h` | one_head_filter_pi_star | 20 | 2.3502 | 0.6680 | 0.4000 | -0.8829 | -0.0200 | 0.3500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2160_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4709 | 0.2857 | -1.0847 | -0.0600 | 0.0714 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2160_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4702 | 0.2667 | -1.0879 | -0.0615 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2160_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2160_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2160_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
