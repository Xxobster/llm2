# Autonomy public-indicator hunt gen 1113

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T003829Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema2340_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2340_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.4502 | 0.6667 | 1.3795 | 0.0869 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2340_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.5744 | 0.6405 | 3.4470 | 0.0154 | 0.3051 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema2340_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.5572 | 0.6390 | 3.5567 | 0.0151 | 0.3009 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2340_below_at_h` | one_head_filter_pi_star | 272 | 22.2417 | 1.8316 | 0.6581 | 4.1008 | 0.0130 | 0.3346 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2340_below_at_h` | one_head_filter_pi_star | 281 | 22.8599 | 1.8362 | 0.6477 | 4.2100 | 0.0127 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema2340_above_at_h` | one_head_filter_pi_star | 95 | 7.8082 | 1.7620 | 0.6632 | 2.2763 | 0.0106 | 0.2737 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema2340_above_at_h` | one_head_filter_pi_star | 100 | 8.3113 | 1.7025 | 0.6500 | 2.2618 | 0.0105 | 0.2700 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema2340_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.5092 | 0.2857 | -0.9832 | -0.0544 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema2340_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4384 | 0.2500 | -1.2254 | -0.0668 | 0.0625 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema2340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2340_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ema2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema2340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
