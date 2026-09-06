# Autonomy public-indicator hunt gen 2432

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T173459Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5680_above_at_h` | one_head_filter_pi_star | 49 | 4.6007 | 2.1734 | 0.6735 | 2.1389 | 0.0166 | 0.1020 | ok | RAN |
| SOLUSDT | 8 | `sma5680_above_at_h` | one_head_filter_pi_star | 49 | 4.6007 | 1.8773 | 0.6327 | 1.6916 | 0.0126 | 0.1224 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5680_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9838 | 0.5592 | -0.1294 | -0.0005 | 0.1361 | ok | RAN |
| SOLUSDT | 4 | `sma5680_below_at_h` | one_head_filter_pi_star | 308 | 25.0564 | 0.9616 | 0.5325 | -0.2946 | -0.0008 | 0.1299 | ok | RAN |
| SOLUSDT | 8 | `sma5680_below_at_h` | one_head_filter_pi_star | 317 | 25.9214 | 0.9367 | 0.5268 | -0.4995 | -0.0013 | 0.1325 | ok | RAN |
| ETHUSDT | 8 | `sma5680_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9494 | 0.5546 | -0.4140 | -0.0017 | 0.1357 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5680_above_at_h` | one_head_filter_pi_star | 29 | 8.7512 | 0.8106 | 0.4828 | -0.8970 | -0.0096 | 0.1379 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5680_above_at_h` | one_head_filter_pi_star | 39 | 11.5074 | 0.6064 | 0.4359 | -2.6402 | -0.0263 | 0.1795 | ok | RAN |
| ETHUSDT | 4 | `sma5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5680_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5680_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
