# Autonomy public-indicator hunt gen 1700

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T045349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1002_above_at_h` | one_head_filter_pi_star | 111 | 9.2255 | 1.0816 | 0.5766 | 0.3542 | 0.0015 | 0.1351 | ok | RAN |
| SOLUSDT | 8 | `ema1002_below_at_h` | one_head_filter_pi_star | 256 | 20.9333 | 1.0285 | 0.5547 | 0.1916 | 0.0006 | 0.1289 | ok | RAN |
| SOLUSDT | 4 | `ema1002_above_at_h` | one_head_filter_pi_star | 116 | 9.6411 | 1.0089 | 0.5603 | 0.0421 | 0.0002 | 0.1379 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1002_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 0.9832 | 0.5502 | -0.1121 | -0.0004 | 0.1285 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1002_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9020 | 0.5371 | -0.7079 | -0.0033 | 0.1572 | ok | RAN |
| ETHUSDT | 8 | `ema1002_below_at_h` | one_head_filter_pi_star | 236 | 19.2790 | 0.8995 | 0.5339 | -0.7378 | -0.0033 | 0.1568 | ok | RAN |
| ETHUSDT | 4 | `ema1002_above_at_h` | one_head_filter_pi_star | 129 | 10.6462 | 0.8918 | 0.5504 | -0.5270 | -0.0048 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema1002_above_at_h` | one_head_filter_pi_star | 110 | 9.0781 | 0.8688 | 0.5364 | -0.6183 | -0.0058 | 0.1364 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1002_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1002_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1002_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1002_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1002_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1002_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1002_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1002_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1002_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1002_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1002_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1002_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1002_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1002_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1002_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1002_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
