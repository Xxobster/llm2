# Autonomy public-indicator hunt gen 961

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T081618Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1960_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1067 | 0.3000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1960_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 2.9360 | 0.7000 | 1.7370 | 0.1026 | 0.3000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1960_below_at_h` | one_head_filter_pi_star | 317 | 25.8960 | 1.6345 | 0.6467 | 3.6684 | 0.0165 | 0.3123 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ema1960_below_at_h` | one_head_filter_pi_star | 308 | 25.1608 | 1.4861 | 0.6299 | 2.9024 | 0.0133 | 0.3084 | ok | RAN |
| SOLUSDT | 8 | `ema1960_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.8307 | 0.6484 | 4.2286 | 0.0132 | 0.3223 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1960_below_at_h` | one_head_filter_pi_star | 281 | 22.9776 | 1.7941 | 0.6477 | 4.1265 | 0.0126 | 0.3203 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1960_above_at_h` | one_head_filter_pi_star | 101 | 8.2356 | 1.6808 | 0.6535 | 2.1597 | 0.0097 | 0.2574 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema1960_above_at_h` | one_head_filter_pi_star | 72 | 6.3317 | 1.2135 | 0.5972 | 0.7155 | 0.0092 | 0.2500 | ok | RAN |
| SOLUSDT | 4 | `ema1960_above_at_h` | one_head_filter_pi_star | 89 | 7.3163 | 1.6419 | 0.6629 | 1.8301 | 0.0088 | 0.2584 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema1960_above_at_h` | one_head_filter_pi_star | 22 | 2.1222 | 0.5720 | 0.3636 | -1.1457 | -0.0272 | 0.3182 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1960_above_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.3421 | 0.2143 | -1.4008 | -0.0747 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1960_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3426 | 0.2308 | -1.3975 | -0.0819 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
