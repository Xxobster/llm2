# Autonomy public-indicator hunt gen 873

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T224131Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1740_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1740_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1740_below_at_h` | one_head_filter_pi_star | 321 | 26.1140 | 1.6133 | 0.6417 | 3.5471 | 0.0159 | 0.3146 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ema1740_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5461 | 0.6369 | 3.3707 | 0.0150 | 0.3065 | ok | RAN |
| SOLUSDT | 8 | `ema1740_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.8345 | 0.6533 | 4.1837 | 0.0130 | 0.3248 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1740_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.7988 | 0.6477 | 4.1631 | 0.0126 | 0.3238 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1740_above_at_h` | one_head_filter_pi_star | 98 | 7.9923 | 1.6139 | 0.6429 | 1.9113 | 0.0085 | 0.2449 | ok | RAN |
| SOLUSDT | 4 | `ema1740_above_at_h` | one_head_filter_pi_star | 95 | 7.7476 | 1.4863 | 0.6105 | 1.5783 | 0.0070 | 0.2632 | ok | RAN |
| ETHUSDT | 4 | `ema1740_above_at_h` | one_head_filter_pi_star | 49 | 4.3091 | 1.1691 | 0.5918 | 0.4790 | 0.0066 | 0.2653 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1740_above_at_h` | one_head_filter_pi_star | 28 | 2.6210 | 0.8367 | 0.5000 | -0.4150 | -0.0084 | 0.1786 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1740_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0575 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1740_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4741 | 0.2500 | -1.1218 | -0.0640 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
