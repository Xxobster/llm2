# Autonomy public-indicator hunt gen 2492

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T001911Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1107_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0860 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1107_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.1065 | 0.5833 | 0.4524 | 0.0019 | 0.1389 | ok | RAN |
| SOLUSDT | 8 | `ema1107_above_at_h` | one_head_filter_pi_star | 110 | 8.9694 | 1.0740 | 0.5727 | 0.3233 | 0.0013 | 0.1364 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1107_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 0.9965 | 0.5520 | -0.0234 | -0.0001 | 0.1320 | ok | RAN |
| ETHUSDT | 8 | `ema1107_below_at_h` | one_head_filter_pi_star | 230 | 18.7889 | 0.9624 | 0.5522 | -0.2604 | -0.0012 | 0.1565 | ok | RAN |
| SOLUSDT | 8 | `ema1107_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9466 | 0.5328 | -0.3711 | -0.0012 | 0.1351 | ok | RAN |
| ETHUSDT | 4 | `ema1107_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 0.9593 | 0.5455 | -0.2726 | -0.0012 | 0.1500 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1107_above_at_h` | one_head_filter_pi_star | 117 | 9.6558 | 0.8724 | 0.5385 | -0.6132 | -0.0059 | 0.1111 | ok | RAN |
| ETHUSDT | 8 | `ema1107_above_at_h` | one_head_filter_pi_star | 103 | 8.5004 | 0.8327 | 0.5243 | -0.7546 | -0.0075 | 0.1165 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1107_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1107_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1107_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1107_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1107_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1107_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1107_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1107_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1107_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1107_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1107_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1107_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1107_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1107_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1107_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
