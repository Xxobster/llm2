# Autonomy public-indicator hunt gen 2276

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T214811Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1078_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1078_above_at_h` | one_head_filter_pi_star | 105 | 8.5617 | 1.1900 | 0.5905 | 0.7559 | 0.0032 | 0.1524 | ok | RAN |
| SOLUSDT | 8 | `ema1078_above_at_h` | one_head_filter_pi_star | 124 | 10.1110 | 1.1525 | 0.5887 | 0.6540 | 0.0026 | 0.1129 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1078_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 0.9845 | 0.5586 | -0.1065 | -0.0005 | 0.1532 | ok | RAN |
| ETHUSDT | 4 | `ema1078_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9700 | 0.5487 | -0.2011 | -0.0009 | 0.1504 | ok | RAN |
| SOLUSDT | 8 | `ema1078_below_at_h` | one_head_filter_pi_star | 270 | 21.9650 | 0.9549 | 0.5333 | -0.3204 | -0.0009 | 0.1296 | ok | RAN |
| SOLUSDT | 4 | `ema1078_below_at_h` | one_head_filter_pi_star | 268 | 21.9146 | 0.9450 | 0.5373 | -0.3958 | -0.0012 | 0.1306 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1078_above_at_h` | one_head_filter_pi_star | 140 | 11.5540 | 0.9489 | 0.5571 | -0.2540 | -0.0022 | 0.1214 | ok | RAN |
| ETHUSDT | 8 | `ema1078_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.9354 | 0.5431 | -0.3000 | -0.0026 | 0.1293 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1078_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0313 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1078_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1078_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1078_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1078_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1078_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1078_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1078_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1078_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1078_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1078_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1078_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1078_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1078_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1078_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
