# Autonomy public-indicator hunt gen 1225

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T124153Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema2620_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2620_below_at_h` | one_head_filter_pi_star | 358 | 29.1240 | 1.6552 | 0.6508 | 3.9879 | 0.0172 | 0.2961 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema2620_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.5896 | 0.6388 | 3.5344 | 0.0157 | 0.3015 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2620_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 1.8928 | 0.6556 | 4.3619 | 0.0131 | 0.3296 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2620_below_at_h` | one_head_filter_pi_star | 286 | 23.2667 | 1.7933 | 0.6469 | 4.0716 | 0.0122 | 0.3322 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2620_above_at_h` | one_head_filter_pi_star | 88 | 7.3139 | 1.8897 | 0.6818 | 2.4960 | 0.0118 | 0.2727 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2620_above_at_h` | one_head_filter_pi_star | 92 | 7.5616 | 1.6995 | 0.6522 | 2.0683 | 0.0100 | 0.2826 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema2620_above_at_h` | one_head_filter_pi_star | 18 | 5.4318 | 0.7769 | 0.4444 | -0.9468 | -0.0112 | 0.2222 | ok | RAN |
| BTCUSDT | 4 | `ema2620_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7186 | 0.3333 | -0.5631 | -0.0301 | 0.1111 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2620_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3190 | 0.2000 | -1.5401 | -0.0848 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2620_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
