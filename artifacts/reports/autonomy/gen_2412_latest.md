# Autonomy public-indicator hunt gen 2412

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T151429Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1096_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1096_above_at_h` | one_head_filter_pi_star | 101 | 8.2356 | 1.3687 | 0.6337 | 1.3472 | 0.0059 | 0.1485 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1096_above_at_h` | one_head_filter_pi_star | 113 | 9.2141 | 1.0733 | 0.5752 | 0.3227 | 0.0013 | 0.1504 | ok | RAN |
| SOLUSDT | 8 | `ema1096_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 1.0208 | 0.5447 | 0.1360 | 0.0004 | 0.1301 | ok | RAN |
| ETHUSDT | 4 | `ema1096_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 1.0054 | 0.5565 | 0.0373 | 0.0002 | 0.1522 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1096_below_at_h` | one_head_filter_pi_star | 264 | 21.5875 | 0.9436 | 0.5379 | -0.4029 | -0.0012 | 0.1364 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1096_above_at_h` | one_head_filter_pi_star | 120 | 9.9034 | 0.9482 | 0.5500 | -0.2376 | -0.0022 | 0.1417 | ok | RAN |
| ETHUSDT | 8 | `ema1096_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9121 | 0.5401 | -0.6419 | -0.0028 | 0.1477 | ok | RAN |
| ETHUSDT | 4 | `ema1096_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.9149 | 0.5431 | -0.3832 | -0.0037 | 0.1121 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1096_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1096_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1096_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1096_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1096_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1096_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1096_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1096_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1096_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1096_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1096_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1096_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1096_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1096_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1096_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
