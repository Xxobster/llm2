# Autonomy public-indicator hunt gen 984

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260827T113558Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma2060_below_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.6118 | 0.6455 | 3.6792 | 0.0161 | 0.3121 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2060_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.5632 | 0.6385 | 3.5374 | 0.0155 | 0.3032 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2060_above_at_h` | one_head_filter_pi_star | 51 | 4.6134 | 1.3504 | 0.5686 | 0.9135 | 0.0138 | 0.2549 | ok | RAN |
| SOLUSDT | 4 | `sma2060_above_at_h` | one_head_filter_pi_star | 76 | 6.3177 | 1.8549 | 0.6842 | 2.2977 | 0.0122 | 0.2763 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2060_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 1.8219 | 0.6450 | 4.2695 | 0.0122 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2060_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 1.7770 | 0.6405 | 4.1375 | 0.0115 | 0.3137 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma2060_above_at_h` | one_head_filter_pi_star | 75 | 6.2335 | 1.4895 | 0.6267 | 1.5277 | 0.0080 | 0.2667 | ok | RAN |
| ETHUSDT | 4 | `sma2060_above_at_h` | one_head_filter_pi_star | 43 | 3.8897 | 1.0963 | 0.5814 | 0.2657 | 0.0038 | 0.1860 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma2060_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4390 | 0.2667 | -1.2223 | -0.0625 | 0.0667 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2060_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2060_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2060_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2060_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
