# Autonomy public-indicator hunt gen 809

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T163300Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema1580_above_at_h` | one_head_filter_pi_star | 59 | 5.1885 | 1.6516 | 0.6441 | 1.6190 | 0.0222 | 0.2542 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1580_below_at_h` | one_head_filter_pi_star | 312 | 25.4875 | 1.6391 | 0.6474 | 3.7338 | 0.0163 | 0.3205 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1580_below_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.5629 | 0.6383 | 3.3850 | 0.0150 | 0.3070 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1580_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.7646 | 0.6484 | 3.9706 | 0.0120 | 0.3297 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1580_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 1.7293 | 0.6400 | 3.8871 | 0.0119 | 0.3309 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema1580_above_at_h` | one_head_filter_pi_star | 93 | 7.6451 | 1.5889 | 0.6667 | 1.8489 | 0.0088 | 0.2581 | ok | RAN |
| ETHUSDT | 4 | `ema1580_above_at_h` | one_head_filter_pi_star | 44 | 3.8694 | 1.2076 | 0.5909 | 0.5291 | 0.0083 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1580_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.5448 | 0.6417 | 1.9376 | 0.0078 | 0.2417 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1580_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6125 | 0.3333 | -0.8000 | -0.0415 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1580_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0554 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
