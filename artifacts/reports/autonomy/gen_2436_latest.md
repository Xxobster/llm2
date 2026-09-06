# Autonomy public-indicator hunt gen 2436

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T180315Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1099_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.1728 | 0.5856 | 0.7188 | 0.0032 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `ema1099_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.0802 | 0.5833 | 0.3369 | 0.0014 | 0.1389 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1099_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9773 | 0.5489 | -0.1573 | -0.0007 | 0.1489 | ok | RAN |
| SOLUSDT | 8 | `ema1099_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9619 | 0.5397 | -0.2574 | -0.0008 | 0.1349 | ok | RAN |
| ETHUSDT | 8 | `ema1099_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 0.9612 | 0.5447 | -0.2863 | -0.0012 | 0.1545 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1099_below_at_h` | one_head_filter_pi_star | 270 | 22.0781 | 0.9158 | 0.5296 | -0.6164 | -0.0018 | 0.1296 | ok | RAN |
| ETHUSDT | 8 | `ema1099_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 0.8928 | 0.5315 | -0.4778 | -0.0046 | 0.0991 | ok | RAN |
| ETHUSDT | 4 | `ema1099_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.8916 | 0.5431 | -0.4886 | -0.0048 | 0.1034 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1099_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1099_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1099_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1099_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1099_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1099_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1099_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1099_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1099_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1099_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1099_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1099_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1099_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1099_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1099_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1099_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
