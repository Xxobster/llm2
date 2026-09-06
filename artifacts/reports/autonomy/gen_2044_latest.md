# Autonomy public-indicator hunt gen 2044

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T141818Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1048_above_at_h` | one_head_filter_pi_star | 120 | 9.8630 | 1.1458 | 0.5833 | 0.6294 | 0.0027 | 0.1417 | ok | RAN |
| SOLUSDT | 8 | `ema1048_above_at_h` | one_head_filter_pi_star | 116 | 9.4587 | 1.0518 | 0.5776 | 0.2348 | 0.0010 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1048_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9983 | 0.5521 | -0.0117 | -0.0000 | 0.1313 | ok | RAN |
| SOLUSDT | 4 | `ema1048_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 0.9566 | 0.5430 | -0.3044 | -0.0009 | 0.1289 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1048_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9463 | 0.5424 | -0.3775 | -0.0017 | 0.1483 | ok | RAN |
| ETHUSDT | 8 | `ema1048_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9149 | 0.5339 | -0.6120 | -0.0028 | 0.1483 | ok | RAN |
| ETHUSDT | 4 | `ema1048_above_at_h` | one_head_filter_pi_star | 130 | 10.7287 | 0.9274 | 0.5538 | -0.3547 | -0.0031 | 0.1154 | ok | RAN |
| ETHUSDT | 8 | `ema1048_above_at_h` | one_head_filter_pi_star | 120 | 9.8638 | 0.8042 | 0.5167 | -0.9530 | -0.0088 | 0.1167 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1048_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1048_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1048_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1048_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1048_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1048_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1048_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1048_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1048_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1048_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1048_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1048_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1048_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1048_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1048_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1048_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
