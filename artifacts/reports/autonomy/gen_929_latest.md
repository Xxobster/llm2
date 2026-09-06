# Autonomy public-indicator hunt gen 929

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T043906Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1880_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1112 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1880_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 1.5822 | 0.6404 | 3.6043 | 0.0158 | 0.3070 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1880_below_at_h` | one_head_filter_pi_star | 311 | 25.4059 | 1.5870 | 0.6399 | 3.4329 | 0.0157 | 0.3119 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema1880_below_at_h` | one_head_filter_pi_star | 284 | 23.2229 | 1.9166 | 0.6585 | 4.5855 | 0.0142 | 0.3275 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1880_below_at_h` | one_head_filter_pi_star | 274 | 22.4052 | 1.8461 | 0.6569 | 4.3096 | 0.0134 | 0.3321 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1880_above_at_h` | one_head_filter_pi_star | 60 | 5.2086 | 1.3134 | 0.6167 | 0.8778 | 0.0120 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema1880_above_at_h` | one_head_filter_pi_star | 57 | 5.0126 | 1.2087 | 0.5789 | 0.5917 | 0.0080 | 0.2281 | ok | RAN |
| SOLUSDT | 4 | `ema1880_above_at_h` | one_head_filter_pi_star | 105 | 8.5622 | 1.5380 | 0.6286 | 1.7954 | 0.0074 | 0.2286 | ok | RAN |
| SOLUSDT | 8 | `ema1880_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.4347 | 0.6134 | 1.6259 | 0.0063 | 0.2437 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1880_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5935 | 0.2941 | -0.8400 | -0.0444 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1880_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3190 | 0.2000 | -1.5401 | -0.0811 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
