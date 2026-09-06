# Autonomy public-indicator hunt gen 577

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T230023Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema1000_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.7970 | 0.6596 | 3.7870 | 0.0190 | 0.3447 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema1000_below_at_h` | one_head_filter_pi_star | 242 | 19.7692 | 1.7395 | 0.6570 | 3.6796 | 0.0182 | 0.3430 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema1000_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 1.8263 | 0.6475 | 4.0793 | 0.0126 | 0.2989 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1000_above_at_h` | one_head_filter_pi_star | 116 | 9.5342 | 1.7463 | 0.6466 | 2.4485 | 0.0105 | 0.3276 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1000_below_at_h` | one_head_filter_pi_star | 272 | 22.1277 | 1.6050 | 0.6287 | 3.3179 | 0.0101 | 0.3051 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema1000_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.6538 | 0.6348 | 2.2392 | 0.0097 | 0.3130 | ok | RAN |
| ETHUSDT | 4 | `ema1000_above_at_h` | one_head_filter_pi_star | 130 | 10.6858 | 1.2360 | 0.6000 | 1.0388 | 0.0093 | 0.2308 | ok | RAN |
| ETHUSDT | 8 | `ema1000_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 1.2313 | 0.5909 | 1.0001 | 0.0086 | 0.2424 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1000_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1000_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1000_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1000_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1000_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
