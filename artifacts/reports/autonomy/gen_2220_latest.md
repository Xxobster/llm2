# Autonomy public-indicator hunt gen 2220

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T150720Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1071_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1071_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.1721 | 0.5804 | 0.7135 | 0.0029 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `ema1071_above_at_h` | one_head_filter_pi_star | 101 | 8.3944 | 1.1609 | 0.5842 | 0.6651 | 0.0028 | 0.1485 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1071_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9790 | 0.5590 | -0.1448 | -0.0007 | 0.1528 | ok | RAN |
| SOLUSDT | 8 | `ema1071_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9623 | 0.5409 | -0.2639 | -0.0008 | 0.1284 | ok | RAN |
| SOLUSDT | 4 | `ema1071_below_at_h` | one_head_filter_pi_star | 259 | 21.1787 | 0.9352 | 0.5367 | -0.4600 | -0.0014 | 0.1274 | ok | RAN |
| ETHUSDT | 4 | `ema1071_below_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 0.9493 | 0.5487 | -0.3460 | -0.0016 | 0.1504 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1071_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9378 | 0.5528 | -0.2947 | -0.0027 | 0.1220 | ok | RAN |
| ETHUSDT | 8 | `ema1071_above_at_h` | one_head_filter_pi_star | 117 | 9.6172 | 0.8500 | 0.5299 | -0.7264 | -0.0066 | 0.1368 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1071_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1071_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1071_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1071_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1071_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1071_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1071_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1071_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1071_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1071_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1071_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1071_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1071_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1071_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1071_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
