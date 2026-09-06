# Autonomy public-indicator hunt gen 2448

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T192628Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5720_above_at_h` | one_head_filter_pi_star | 12 | 1.3824 | 5.5650 | 0.8333 | 2.1078 | 0.0415 | 0.0833 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5720_above_at_h` | one_head_filter_pi_star | 55 | 4.9210 | 1.8955 | 0.6545 | 1.9005 | 0.0134 | 0.0909 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5720_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9918 | 0.5605 | -0.0658 | -0.0003 | 0.1327 | ok | RAN |
| ETHUSDT | 8 | `sma5720_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9893 | 0.5601 | -0.0870 | -0.0003 | 0.1349 | ok | RAN |
| SOLUSDT | 8 | `sma5720_below_at_h` | one_head_filter_pi_star | 316 | 25.8396 | 0.9599 | 0.5316 | -0.3109 | -0.0008 | 0.1297 | ok | RAN |
| SOLUSDT | 4 | `sma5720_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9408 | 0.5358 | -0.4871 | -0.0012 | 0.1261 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5720_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.7542 | 0.4737 | -1.4033 | -0.0145 | 0.1579 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5720_above_at_h` | one_head_filter_pi_star | 40 | 11.8025 | 0.7067 | 0.4750 | -1.7731 | -0.0174 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `sma5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5720_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5720_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5720_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5720_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
