# Autonomy public-indicator hunt gen 2172

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T082454Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1065_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1065_above_at_h` | one_head_filter_pi_star | 119 | 9.7808 | 1.1556 | 0.5966 | 0.6625 | 0.0028 | 0.1261 | ok | RAN |
| SOLUSDT | 8 | `ema1065_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.1241 | 0.5882 | 0.5345 | 0.0023 | 0.1345 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1065_below_at_h` | one_head_filter_pi_star | 248 | 20.2792 | 0.9877 | 0.5484 | -0.0834 | -0.0003 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema1065_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9882 | 0.5471 | -0.0798 | -0.0004 | 0.1570 | ok | RAN |
| SOLUSDT | 4 | `ema1065_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 0.9691 | 0.5440 | -0.2103 | -0.0007 | 0.1280 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1065_below_at_h` | one_head_filter_pi_star | 241 | 19.6875 | 0.9173 | 0.5353 | -0.6128 | -0.0027 | 0.1411 | ok | RAN |
| ETHUSDT | 4 | `ema1065_above_at_h` | one_head_filter_pi_star | 120 | 10.2111 | 0.9143 | 0.5500 | -0.4076 | -0.0037 | 0.1167 | ok | RAN |
| ETHUSDT | 8 | `ema1065_above_at_h` | one_head_filter_pi_star | 102 | 8.4179 | 0.8510 | 0.5294 | -0.6806 | -0.0066 | 0.1471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1065_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1065_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1065_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1065_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1065_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1065_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1065_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1065_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1065_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1065_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1065_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1065_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1065_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1065_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1065_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
