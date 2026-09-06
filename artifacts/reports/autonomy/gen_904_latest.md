# Autonomy public-indicator hunt gen 904

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T015057Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1860_below_at_h` | one_head_filter_pi_star | 316 | 25.7072 | 1.5917 | 0.6424 | 3.4606 | 0.0156 | 0.3133 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1860_below_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 1.5604 | 0.6372 | 3.3597 | 0.0150 | 0.3123 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1860_above_at_h` | one_head_filter_pi_star | 47 | 3.9070 | 1.8677 | 0.6596 | 1.8483 | 0.0119 | 0.3191 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma1860_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 1.7679 | 0.6401 | 4.1212 | 0.0116 | 0.3185 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1860_below_at_h` | one_head_filter_pi_star | 315 | 25.6259 | 1.7497 | 0.6349 | 4.0502 | 0.0113 | 0.3175 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1860_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.7106 | 0.6562 | 1.8840 | 0.0103 | 0.2500 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1860_above_at_h` | one_head_filter_pi_star | 42 | 3.7993 | 1.1715 | 0.5714 | 0.4688 | 0.0073 | 0.3095 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1860_above_at_h` | one_head_filter_pi_star | 54 | 4.8848 | 1.1474 | 0.5556 | 0.4665 | 0.0060 | 0.2407 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1860_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3356 | 0.2308 | -1.4359 | -0.0787 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
