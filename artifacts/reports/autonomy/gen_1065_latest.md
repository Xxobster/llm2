# Autonomy public-indicator hunt gen 1065

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T184413Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2220_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0799 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema2220_below_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.5632 | 0.6372 | 3.3792 | 0.0150 | 0.3049 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2220_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5527 | 0.6361 | 3.4471 | 0.0150 | 0.3018 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2220_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 1.9100 | 0.6575 | 4.3236 | 0.0141 | 0.3346 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2220_below_at_h` | one_head_filter_pi_star | 276 | 22.4531 | 1.8407 | 0.6486 | 4.1944 | 0.0128 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema2220_above_at_h` | one_head_filter_pi_star | 39 | 3.7621 | 1.2378 | 0.5641 | 0.5919 | 0.0099 | 0.2821 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema2220_above_at_h` | one_head_filter_pi_star | 107 | 8.7945 | 1.6624 | 0.6449 | 2.1575 | 0.0091 | 0.2617 | ok | RAN |
| SOLUSDT | 8 | `ema2220_above_at_h` | one_head_filter_pi_star | 111 | 9.1233 | 1.5085 | 0.6216 | 1.8244 | 0.0076 | 0.2703 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2220_above_at_h` | one_head_filter_pi_star | 17 | 5.2980 | 0.7555 | 0.3529 | -0.9183 | -0.0151 | 0.3529 | EBR>35% | RAN |
| BTCUSDT | 8 | `ema2220_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6375 | 0.3333 | -0.7032 | -0.0402 | 0.0667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2220_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4702 | 0.2667 | -1.0879 | -0.0551 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2220_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2220_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2220_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
