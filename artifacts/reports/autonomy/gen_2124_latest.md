# Autonomy public-indicator hunt gen 2124

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T011225Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1058_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1058_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.1832 | 0.5929 | 0.7581 | 0.0033 | 0.1150 | ok | RAN |
| SOLUSDT | 8 | `ema1058_above_at_h` | one_head_filter_pi_star | 113 | 9.2877 | 1.1652 | 0.5929 | 0.6802 | 0.0028 | 0.1504 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1058_above_at_h` | one_head_filter_pi_star | 136 | 11.2229 | 0.9835 | 0.5588 | -0.0796 | -0.0007 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1058_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9470 | 0.5442 | -0.3610 | -0.0017 | 0.1549 | ok | RAN |
| ETHUSDT | 8 | `ema1058_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 0.9404 | 0.5385 | -0.4184 | -0.0019 | 0.1496 | ok | RAN |
| SOLUSDT | 8 | `ema1058_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9112 | 0.5283 | -0.6505 | -0.0020 | 0.1283 | ok | RAN |
| SOLUSDT | 4 | `ema1058_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 0.9070 | 0.5281 | -0.6810 | -0.0020 | 0.1311 | ok | RAN |
| ETHUSDT | 8 | `ema1058_above_at_h` | one_head_filter_pi_star | 118 | 9.7383 | 0.8534 | 0.5339 | -0.7260 | -0.0062 | 0.1102 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1058_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1058_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1058_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1058_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1058_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1058_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1058_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1058_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1058_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1058_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1058_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1058_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1058_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1058_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1058_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
