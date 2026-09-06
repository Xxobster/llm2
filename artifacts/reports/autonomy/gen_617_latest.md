# Autonomy public-indicator hunt gen 617

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T013616Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1100_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 3.3760 | 0.7000 | 1.9329 | 0.1364 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema1100_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 1.7123 | 0.6513 | 3.5072 | 0.0176 | 0.3403 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1100_below_at_h` | one_head_filter_pi_star | 255 | 20.8312 | 1.7084 | 0.6471 | 3.6290 | 0.0175 | 0.3294 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1100_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.8263 | 0.6459 | 4.0539 | 0.0126 | 0.3152 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1100_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 1.6160 | 0.6283 | 3.3293 | 0.0100 | 0.3086 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1100_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.6508 | 0.6441 | 2.2874 | 0.0096 | 0.2881 | ok | RAN |
| SOLUSDT | 4 | `ema1100_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.6338 | 0.6404 | 2.1576 | 0.0094 | 0.2982 | ok | RAN |
| ETHUSDT | 4 | `ema1100_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 1.0656 | 0.5688 | 0.2797 | 0.0027 | 0.2018 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1100_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 1.0098 | 0.5446 | 0.0442 | 0.0004 | 0.2143 | ok | RAN |
| BTCUSDT | 8 | `ema1100_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1100_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1100_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1100_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1100_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
