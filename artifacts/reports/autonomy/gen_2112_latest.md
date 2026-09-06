# Autonomy public-indicator hunt gen 2112

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T234651Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4880_above_at_h` | one_head_filter_pi_star | 46 | 3.8635 | 1.7792 | 0.5435 | 1.3772 | 0.0094 | 0.0652 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma4880_above_at_h` | one_head_filter_pi_star | 43 | 3.6615 | 1.4764 | 0.5581 | 0.9617 | 0.0076 | 0.0930 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma4880_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 1.0017 | 0.5599 | 0.0137 | 0.0001 | 0.1377 | ok | RAN |
| SOLUSDT | 4 | `sma4880_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 0.9994 | 0.5407 | -0.0048 | -0.0000 | 0.1368 | ok | RAN |
| ETHUSDT | 4 | `sma4880_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9815 | 0.5565 | -0.1494 | -0.0006 | 0.1339 | ok | RAN |
| SOLUSDT | 8 | `sma4880_below_at_h` | one_head_filter_pi_star | 307 | 25.1037 | 0.9589 | 0.5342 | -0.3130 | -0.0008 | 0.1368 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4880_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.8772 | 0.5135 | -0.6328 | -0.0065 | 0.1622 | ok | RAN |
| ETHUSDT | 8 | `sma4880_above_at_h` | one_head_filter_pi_star | 39 | 11.5074 | 0.7382 | 0.4872 | -1.4082 | -0.0155 | 0.1538 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4880_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4880_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4880_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4880_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
