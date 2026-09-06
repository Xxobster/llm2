# Autonomy public-indicator hunt gen 2027

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T122052Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma744_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.2044 | 0.5909 | 1.1402 | 0.0058 | 0.1932 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma744_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1185 | 0.5730 | 0.7119 | 0.0035 | 0.1784 | ok | RAN |
| SOLUSDT | 8 | `sma744_above_at_h` | one_head_filter_pi_star | 124 | 10.1692 | 1.0836 | 0.5565 | 0.3813 | 0.0016 | 0.1371 | ok | RAN |
| SOLUSDT | 4 | `sma744_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.0506 | 0.5500 | 0.2524 | 0.0010 | 0.1071 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma744_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 0.9263 | 0.5455 | -0.4602 | -0.0015 | 0.1340 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma744_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.8915 | 0.5510 | -0.6859 | -0.0023 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `sma744_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.8356 | 0.5633 | -0.8962 | -0.0068 | 0.1013 | ok | RAN |
| ETHUSDT | 8 | `sma744_above_at_h` | one_head_filter_pi_star | 165 | 13.5628 | 0.8221 | 0.5394 | -1.0381 | -0.0075 | 0.0970 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma744_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma744_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma744_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma744_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma744_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma744_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma744_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma744_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma744_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma744_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma744_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma744_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma744_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma744_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma744_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma744_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
