# Autonomy public-indicator hunt gen 1732

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T081033Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1007_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1007_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0910 | 0.5546 | 0.4008 | 0.0016 | 0.1261 | ok | RAN |
| SOLUSDT | 8 | `ema1007_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.0741 | 0.5739 | 0.3256 | 0.0013 | 0.1304 | ok | RAN |
| ETHUSDT | 4 | `ema1007_below_at_h` | one_head_filter_pi_star | 228 | 18.6255 | 1.0065 | 0.5526 | 0.0441 | 0.0002 | 0.1491 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1007_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 1.0008 | 0.5469 | 0.0058 | 0.0000 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ema1007_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9932 | 0.5474 | -0.0465 | -0.0002 | 0.1552 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `ema1007_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 0.9132 | 0.5346 | -0.6298 | -0.0019 | 0.1231 | ok | RAN |
| ETHUSDT | 4 | `ema1007_above_at_h` | one_head_filter_pi_star | 136 | 11.2229 | 0.9527 | 0.5662 | -0.2343 | -0.0020 | 0.1176 | ok | RAN |
| ETHUSDT | 8 | `ema1007_above_at_h` | one_head_filter_pi_star | 123 | 10.1510 | 0.9230 | 0.5528 | -0.3679 | -0.0032 | 0.1138 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1007_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0301 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1007_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1007_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1007_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1007_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1007_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1007_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1007_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1007_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1007_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1007_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1007_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1007_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1007_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1007_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
