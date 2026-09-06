# Autonomy public-indicator hunt gen 905

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T015814Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1820_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.9118 | 0.6667 | 1.7154 | 0.1098 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1820_below_at_h` | one_head_filter_pi_star | 325 | 26.5495 | 1.6449 | 0.6492 | 3.7422 | 0.0169 | 0.3138 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1820_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5865 | 0.6391 | 3.6020 | 0.0159 | 0.3107 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1820_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.8893 | 0.6630 | 4.3667 | 0.0135 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1820_below_at_h` | one_head_filter_pi_star | 276 | 22.5688 | 1.7920 | 0.6413 | 4.1013 | 0.0125 | 0.3261 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1820_above_at_h` | one_head_filter_pi_star | 103 | 8.3991 | 1.6404 | 0.6214 | 2.0186 | 0.0083 | 0.2524 | ok | RAN |
| SOLUSDT | 4 | `ema1820_above_at_h` | one_head_filter_pi_star | 100 | 8.1554 | 1.5081 | 0.6200 | 1.6447 | 0.0075 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1820_above_at_h` | one_head_filter_pi_star | 44 | 3.8694 | 1.0199 | 0.5455 | 0.0554 | 0.0008 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1820_above_at_h` | one_head_filter_pi_star | 27 | 2.6045 | 0.6725 | 0.4074 | -0.9226 | -0.0194 | 0.2222 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1820_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1820_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4988 | 0.2857 | -1.0212 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1820_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1820_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1820_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
