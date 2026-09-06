# Autonomy public-indicator hunt gen 1852

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T190510Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1023_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1023_above_at_h` | one_head_filter_pi_star | 119 | 9.7808 | 1.1639 | 0.5882 | 0.6936 | 0.0031 | 0.1429 | ok | RAN |
| SOLUSDT | 8 | `ema1023_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.1520 | 0.5877 | 0.6390 | 0.0029 | 0.1404 | ok | RAN |
| ETHUSDT | 4 | `ema1023_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.0321 | 0.5575 | 0.2119 | 0.0010 | 0.1549 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1023_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9710 | 0.5379 | -0.2032 | -0.0006 | 0.1326 | ok | RAN |
| SOLUSDT | 4 | `ema1023_below_at_h` | one_head_filter_pi_star | 235 | 19.2162 | 0.9263 | 0.5362 | -0.4925 | -0.0016 | 0.1234 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1023_below_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 0.9179 | 0.5374 | -0.5781 | -0.0026 | 0.1498 | ok | RAN |
| ETHUSDT | 4 | `ema1023_above_at_h` | one_head_filter_pi_star | 129 | 10.6036 | 0.8886 | 0.5581 | -0.5619 | -0.0050 | 0.1240 | ok | RAN |
| ETHUSDT | 8 | `ema1023_above_at_h` | one_head_filter_pi_star | 108 | 8.8775 | 0.8405 | 0.5463 | -0.7472 | -0.0069 | 0.1296 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1023_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1023_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1023_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1023_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1023_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1023_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1023_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1023_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1023_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1023_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1023_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1023_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1023_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1023_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1023_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
