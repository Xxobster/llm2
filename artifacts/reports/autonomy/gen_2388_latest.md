# Autonomy public-indicator hunt gen 2388

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T122201Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1093_below_at_h` | one_head_filter_pi_star | 10 | 1.7037 | 2.0605 | 0.7000 | 1.4030 | 0.0833 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1093_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1093_above_at_h` | one_head_filter_pi_star | 108 | 8.8565 | 1.3131 | 0.6204 | 1.1784 | 0.0051 | 0.1389 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1093_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.2276 | 0.5882 | 0.9157 | 0.0038 | 0.1261 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1093_below_at_h` | one_head_filter_pi_star | 239 | 19.5432 | 0.9968 | 0.5523 | -0.0207 | -0.0001 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `ema1093_below_at_h` | one_head_filter_pi_star | 267 | 21.8328 | 0.9522 | 0.5393 | -0.3422 | -0.0010 | 0.1348 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1093_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9468 | 0.5447 | -0.3754 | -0.0017 | 0.1532 | ok | RAN |
| ETHUSDT | 4 | `ema1093_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 0.9287 | 0.5536 | -0.3329 | -0.0030 | 0.0982 | ok | RAN |
| ETHUSDT | 8 | `ema1093_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9043 | 0.5391 | -0.7113 | -0.0031 | 0.1440 | ok | RAN |
| ETHUSDT | 8 | `ema1093_above_at_h` | one_head_filter_pi_star | 116 | 9.5733 | 0.8904 | 0.5345 | -0.5176 | -0.0049 | 0.1121 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1093_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1093_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1093_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1093_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1093_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1093_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1093_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1093_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1093_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1093_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1093_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1093_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1093_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1093_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
