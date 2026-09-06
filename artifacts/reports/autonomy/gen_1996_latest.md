# Autonomy public-indicator hunt gen 1996

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T084448Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1042_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.1777 | 0.5868 | 0.7623 | 0.0031 | 0.1322 | ok | RAN |
| SOLUSDT | 4 | `ema1042_above_at_h` | one_head_filter_pi_star | 103 | 8.5606 | 1.1663 | 0.6117 | 0.6698 | 0.0030 | 0.1553 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1042_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.9895 | 0.5645 | -0.0479 | -0.0004 | 0.1210 | ok | RAN |
| SOLUSDT | 8 | `ema1042_below_at_h` | one_head_filter_pi_star | 233 | 19.0526 | 0.9613 | 0.5536 | -0.2561 | -0.0008 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1042_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 0.9659 | 0.5482 | -0.2326 | -0.0011 | 0.1491 | ok | RAN |
| ETHUSDT | 4 | `ema1042_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9637 | 0.5500 | -0.2423 | -0.0011 | 0.1591 | ok | RAN |
| SOLUSDT | 4 | `ema1042_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 0.9418 | 0.5382 | -0.3999 | -0.0013 | 0.1325 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1042_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 0.7843 | 0.5046 | -1.0144 | -0.0097 | 0.1193 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1042_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1042_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0595 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1042_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1042_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1042_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1042_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1042_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1042_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1042_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1042_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1042_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1042_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1042_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1042_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1042_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1042_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
