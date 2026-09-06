# Autonomy public-indicator hunt gen 1795

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T135722Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma713_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 1.1679 | 0.5749 | 0.9420 | 0.0048 | 0.1976 | ok | RAN |
| ETHUSDT | 8 | `sma713_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1304 | 0.5706 | 0.7404 | 0.0040 | 0.1751 | ok | RAN |
| SOLUSDT | 8 | `sma713_above_at_h` | one_head_filter_pi_star | 129 | 10.5786 | 1.1903 | 0.5581 | 0.8316 | 0.0033 | 0.1240 | ok | RAN |
| SOLUSDT | 4 | `sma713_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.1165 | 0.5635 | 0.5230 | 0.0022 | 0.1190 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma713_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 0.9362 | 0.5495 | -0.3982 | -0.0014 | 0.1337 | ok | RAN |
| SOLUSDT | 4 | `sma713_below_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 0.9345 | 0.5567 | -0.4094 | -0.0014 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma713_above_at_h` | one_head_filter_pi_star | 133 | 10.9324 | 0.9384 | 0.5714 | -0.3019 | -0.0024 | 0.1203 | ok | RAN |
| ETHUSDT | 8 | `sma713_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.8521 | 0.5471 | -0.8443 | -0.0058 | 0.1000 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma713_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma713_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0566 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma713_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma713_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma713_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma713_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma713_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma713_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma713_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma713_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma713_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma713_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma713_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma713_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma713_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma713_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
