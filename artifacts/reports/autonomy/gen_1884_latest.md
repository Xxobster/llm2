# Autonomy public-indicator hunt gen 1884

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T215829Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1027_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1027_above_at_h` | one_head_filter_pi_star | 99 | 8.1370 | 1.5882 | 0.6667 | 1.9639 | 0.0086 | 0.1414 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1027_above_at_h` | one_head_filter_pi_star | 113 | 9.2877 | 1.1487 | 0.5752 | 0.6487 | 0.0026 | 0.1416 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1027_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 0.9946 | 0.5488 | -0.0354 | -0.0002 | 0.1581 | ok | RAN |
| SOLUSDT | 4 | `ema1027_below_at_h` | one_head_filter_pi_star | 253 | 20.6880 | 0.9379 | 0.5415 | -0.4366 | -0.0013 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1027_below_at_h` | one_head_filter_pi_star | 266 | 21.7510 | 0.9234 | 0.5301 | -0.5577 | -0.0017 | 0.1278 | ok | RAN |
| ETHUSDT | 4 | `ema1027_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.9492 | 0.5645 | -0.2386 | -0.0022 | 0.1371 | ok | RAN |
| ETHUSDT | 8 | `ema1027_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.8806 | 0.5297 | -0.8901 | -0.0040 | 0.1525 | ok | RAN |
| ETHUSDT | 8 | `ema1027_above_at_h` | one_head_filter_pi_star | 119 | 9.8209 | 0.8472 | 0.5210 | -0.7294 | -0.0068 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1027_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1027_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1027_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1027_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1027_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1027_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1027_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1027_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1027_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1027_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1027_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1027_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1027_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1027_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1027_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
