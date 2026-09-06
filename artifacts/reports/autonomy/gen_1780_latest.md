# Autonomy public-indicator hunt gen 1780

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T123437Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1013_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.1560 | 0.5820 | 0.6720 | 0.0027 | 0.1393 | ok | RAN |
| SOLUSDT | 8 | `ema1013_above_at_h` | one_head_filter_pi_star | 120 | 9.7848 | 1.1341 | 0.5750 | 0.5812 | 0.0024 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1013_below_at_h` | one_head_filter_pi_star | 250 | 20.4427 | 1.0002 | 0.5480 | 0.0014 | 0.0000 | 0.1200 | ok | RAN |
| ETHUSDT | 8 | `ema1013_above_at_h` | one_head_filter_pi_star | 135 | 11.1413 | 0.9838 | 0.5630 | -0.0765 | -0.0007 | 0.1111 | ok | RAN |
| SOLUSDT | 8 | `ema1013_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9466 | 0.5364 | -0.3796 | -0.0012 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1013_above_at_h` | one_head_filter_pi_star | 132 | 10.8937 | 0.9516 | 0.5682 | -0.2378 | -0.0020 | 0.1288 | ok | RAN |
| ETHUSDT | 4 | `ema1013_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9256 | 0.5411 | -0.5368 | -0.0024 | 0.1558 | ok | RAN |
| ETHUSDT | 8 | `ema1013_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9030 | 0.5333 | -0.7202 | -0.0032 | 0.1458 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1013_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1013_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1013_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1013_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1013_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1013_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1013_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1013_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1013_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1013_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1013_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1013_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1013_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1013_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1013_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1013_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
