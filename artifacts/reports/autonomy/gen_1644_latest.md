# Autonomy public-indicator hunt gen 1644

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T223601Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema993_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema993_above_at_h` | one_head_filter_pi_star | 121 | 9.8664 | 1.1274 | 0.5785 | 0.5557 | 0.0023 | 0.1405 | ok | RAN |
| ETHUSDT | 4 | `ema993_above_at_h` | one_head_filter_pi_star | 114 | 9.4082 | 1.0355 | 0.5614 | 0.1518 | 0.0014 | 0.1140 | ok | RAN |
| SOLUSDT | 8 | `ema993_above_at_h` | one_head_filter_pi_star | 119 | 9.7033 | 1.0148 | 0.5462 | 0.0693 | 0.0003 | 0.1176 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema993_below_at_h` | one_head_filter_pi_star | 242 | 19.7885 | 0.9954 | 0.5537 | -0.0303 | -0.0001 | 0.1322 | ok | RAN |
| ETHUSDT | 4 | `ema993_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9854 | 0.5633 | -0.1010 | -0.0005 | 0.1528 | ok | RAN |
| ETHUSDT | 8 | `ema993_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9658 | 0.5458 | -0.2487 | -0.0011 | 0.1458 | ok | RAN |
| SOLUSDT | 4 | `ema993_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 0.9483 | 0.5385 | -0.3617 | -0.0011 | 0.1308 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema993_above_at_h` | one_head_filter_pi_star | 128 | 10.5627 | 0.9557 | 0.5625 | -0.2111 | -0.0019 | 0.1094 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema993_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema993_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema993_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema993_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema993_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema993_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema993_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema993_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema993_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema993_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema993_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema993_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema993_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema993_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema993_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
