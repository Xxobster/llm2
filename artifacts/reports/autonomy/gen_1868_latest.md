# Autonomy public-indicator hunt gen 1868

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T203102Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1025_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.2000 | 0.6034 | 0.8238 | 0.0035 | 0.1466 | ok | RAN |
| SOLUSDT | 8 | `ema1025_above_at_h` | one_head_filter_pi_star | 112 | 9.2055 | 1.1182 | 0.5714 | 0.5154 | 0.0022 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `ema1025_below_at_h` | one_head_filter_pi_star | 245 | 20.0339 | 1.0124 | 0.5551 | 0.0822 | 0.0003 | 0.1224 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1025_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 0.9853 | 0.5478 | -0.1014 | -0.0004 | 0.1478 | ok | RAN |
| ETHUSDT | 8 | `ema1025_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9849 | 0.5489 | -0.1052 | -0.0005 | 0.1447 | ok | RAN |
| SOLUSDT | 8 | `ema1025_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 0.9413 | 0.5356 | -0.4208 | -0.0013 | 0.1348 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1025_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.9482 | 0.5537 | -0.2318 | -0.0022 | 0.1322 | ok | RAN |
| ETHUSDT | 4 | `ema1025_above_at_h` | one_head_filter_pi_star | 127 | 10.4811 | 0.9419 | 0.5591 | -0.2824 | -0.0026 | 0.1102 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1025_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1025_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1025_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1025_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1025_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1025_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1025_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1025_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1025_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1025_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1025_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1025_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1025_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1025_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1025_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1025_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
