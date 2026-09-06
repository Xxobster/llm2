# Autonomy public-indicator hunt gen 1136

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T031344Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2440_above_at_h` | one_head_filter_pi_star | 50 | 4.5988 | 1.4124 | 0.6000 | 1.0909 | 0.0162 | 0.2600 | ok | RAN |
| ETHUSDT | 8 | `sma2440_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.5943 | 0.6414 | 3.6881 | 0.0161 | 0.3061 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2440_below_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.6082 | 0.6402 | 3.5415 | 0.0161 | 0.3110 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2440_above_at_h` | one_head_filter_pi_star | 45 | 4.0706 | 1.4141 | 0.6222 | 1.0149 | 0.0158 | 0.2000 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma2440_below_at_h` | one_head_filter_pi_star | 286 | 23.2667 | 1.8859 | 0.6573 | 4.3765 | 0.0132 | 0.3252 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2440_below_at_h` | one_head_filter_pi_star | 294 | 24.0406 | 1.7956 | 0.6463 | 4.1321 | 0.0120 | 0.3163 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma2440_above_at_h` | one_head_filter_pi_star | 65 | 5.3434 | 1.4830 | 0.6308 | 1.3163 | 0.0065 | 0.2308 | ok | RAN |
| SOLUSDT | 8 | `sma2440_above_at_h` | one_head_filter_pi_star | 60 | 4.8932 | 1.3881 | 0.6000 | 0.9658 | 0.0049 | 0.1833 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
