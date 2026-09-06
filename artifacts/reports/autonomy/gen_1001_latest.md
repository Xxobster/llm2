# Autonomy public-indicator hunt gen 1001

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T102708Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema2060_below_at_h` | one_head_filter_pi_star | 321 | 26.1140 | 1.6493 | 0.6480 | 3.6902 | 0.0167 | 0.3146 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema2060_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.6365 | 0.6450 | 3.7424 | 0.0166 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema2060_below_at_h` | one_head_filter_pi_star | 273 | 22.2091 | 1.8862 | 0.6520 | 4.3336 | 0.0134 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2060_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 1.8487 | 0.6502 | 4.1735 | 0.0134 | 0.3270 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema2060_above_at_h` | one_head_filter_pi_star | 98 | 7.9923 | 1.5356 | 0.6327 | 1.7091 | 0.0078 | 0.2653 | ok | RAN |
| SOLUSDT | 8 | `ema2060_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.4952 | 0.6228 | 1.7808 | 0.0074 | 0.2456 | ok | RAN |
| ETHUSDT | 8 | `ema2060_above_at_h` | one_head_filter_pi_star | 49 | 4.3091 | 1.1149 | 0.5510 | 0.3197 | 0.0051 | 0.2449 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2060_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6375 | 0.3333 | -0.7032 | -0.0393 | 0.0667 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2060_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6375 | 0.3333 | -0.7032 | -0.0411 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2060_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
