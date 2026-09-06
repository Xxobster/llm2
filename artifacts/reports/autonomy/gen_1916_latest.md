# Autonomy public-indicator hunt gen 1916

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T005244Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1031_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0822 | 0.1000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1031_above_at_h` | one_head_filter_pi_star | 132 | 10.8937 | 1.0654 | 0.5833 | 0.3012 | 0.0026 | 0.1136 | ok | RAN |
| SOLUSDT | 4 | `ema1031_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.0963 | 0.5785 | 0.4273 | 0.0017 | 0.1405 | ok | RAN |
| SOLUSDT | 8 | `ema1031_above_at_h` | one_head_filter_pi_star | 116 | 9.6411 | 1.0472 | 0.5776 | 0.2148 | 0.0010 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1031_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9775 | 0.5396 | -0.1585 | -0.0005 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `ema1031_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9591 | 0.5417 | -0.2895 | -0.0009 | 0.1326 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1031_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 0.9327 | 0.5336 | -0.4886 | -0.0022 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `ema1031_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9243 | 0.5351 | -0.5281 | -0.0024 | 0.1491 | ok | RAN |
| ETHUSDT | 8 | `ema1031_above_at_h` | one_head_filter_pi_star | 110 | 9.0781 | 0.8606 | 0.5364 | -0.6531 | -0.0064 | 0.1091 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1031_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1031_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1031_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1031_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1031_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1031_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1031_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1031_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1031_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1031_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1031_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1031_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1031_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1031_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1031_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
