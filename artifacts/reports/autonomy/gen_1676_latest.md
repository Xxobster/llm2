# Autonomy public-indicator hunt gen 1676

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T013102Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema998_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema998_above_at_h` | one_head_filter_pi_star | 125 | 10.2740 | 1.1715 | 0.5840 | 0.7556 | 0.0030 | 0.1280 | ok | RAN |
| SOLUSDT | 8 | `ema998_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.1658 | 0.6071 | 0.6840 | 0.0030 | 0.1339 | ok | RAN |
| ETHUSDT | 4 | `ema998_above_at_h` | one_head_filter_pi_star | 140 | 11.5530 | 1.0171 | 0.5786 | 0.0816 | 0.0007 | 0.1214 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema998_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 0.9940 | 0.5473 | -0.0396 | -0.0001 | 0.1235 | ok | RAN |
| ETHUSDT | 4 | `ema998_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.9850 | 0.5508 | -0.1032 | -0.0005 | 0.1525 | ok | RAN |
| ETHUSDT | 8 | `ema998_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9521 | 0.5458 | -0.3528 | -0.0016 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema998_below_at_h` | one_head_filter_pi_star | 246 | 20.1156 | 0.9213 | 0.5366 | -0.5469 | -0.0017 | 0.1260 | ok | RAN |
| ETHUSDT | 8 | `ema998_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.9422 | 0.5690 | -0.2528 | -0.0024 | 0.1121 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema998_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema998_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema998_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema998_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema998_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema998_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema998_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema998_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema998_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema998_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema998_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema998_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema998_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema998_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema998_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
