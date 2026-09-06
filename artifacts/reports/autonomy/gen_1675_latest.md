# Autonomy public-indicator hunt gen 1675

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T012451Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma697_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.1910 | 0.5904 | 1.0547 | 0.0055 | 0.1867 | ok | RAN |
| ETHUSDT | 8 | `sma697_below_at_h` | one_head_filter_pi_star | 172 | 14.0508 | 1.1399 | 0.5698 | 0.7758 | 0.0042 | 0.1919 | ok | RAN |
| SOLUSDT | 4 | `sma697_above_at_h` | one_head_filter_pi_star | 156 | 12.7928 | 1.1024 | 0.5513 | 0.5201 | 0.0019 | 0.1090 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma697_above_at_h` | one_head_filter_pi_star | 147 | 12.0547 | 0.9800 | 0.5238 | -0.1048 | -0.0004 | 0.1088 | ok | RAN |
| SOLUSDT | 4 | `sma697_below_at_h` | one_head_filter_pi_star | 200 | 16.2704 | 0.9438 | 0.5500 | -0.3493 | -0.0012 | 0.1300 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma697_above_at_h` | one_head_filter_pi_star | 145 | 11.9656 | 0.9585 | 0.5724 | -0.2099 | -0.0017 | 0.1034 | ok | RAN |
| ETHUSDT | 8 | `sma697_above_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 0.9549 | 0.5804 | -0.2337 | -0.0018 | 0.1189 | ok | RAN |
| SOLUSDT | 8 | `sma697_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 0.8954 | 0.5544 | -0.6644 | -0.0023 | 0.1347 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma697_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma697_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma697_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma697_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma697_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma697_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma697_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma697_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma697_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma697_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma697_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma697_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma697_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma697_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma697_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma697_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
