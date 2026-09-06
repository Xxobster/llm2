# Autonomy public-indicator hunt gen 1017

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T123442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema2100_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.6067 | 0.6433 | 3.7171 | 0.0162 | 0.3070 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2100_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.6028 | 0.6394 | 3.6076 | 0.0160 | 0.3061 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2100_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8378 | 0.6540 | 4.1255 | 0.0131 | 0.3308 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2100_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.7858 | 0.6441 | 4.1309 | 0.0124 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema2100_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.6428 | 0.6404 | 2.1793 | 0.0087 | 0.2368 | ok | RAN |
| SOLUSDT | 4 | `ema2100_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.5816 | 0.6404 | 2.0344 | 0.0082 | 0.2544 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2100_above_at_h` | one_head_filter_pi_star | 37 | 4.3479 | 0.9791 | 0.4595 | -0.0634 | -0.0010 | 0.2703 | ok | RAN |
| ETHUSDT | 8 | `ema2100_above_at_h` | one_head_filter_pi_star | 20 | 2.3502 | 0.7046 | 0.4000 | -0.7986 | -0.0181 | 0.4000 | EBR>35% | RAN |
| BTCUSDT | 8 | `ema2100_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.5944 | 0.3125 | -0.8370 | -0.0482 | 0.0625 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2100_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3194 | 0.2143 | -1.5369 | -0.0827 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
