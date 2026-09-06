# Autonomy public-indicator hunt gen 2524

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T033901Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `ema1111_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema1111_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.2195 | 0.6019 | 0.8765 | 0.0036 | 0.1359 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1111_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.1862 | 0.5963 | 0.7543 | 0.0032 | 0.1284 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1111_below_at_h` | one_head_filter_pi_star | 271 | 22.1599 | 0.9679 | 0.5351 | -0.2271 | -0.0007 | 0.1328 | ok | RAN |
| SOLUSDT | 4 | `ema1111_below_at_h` | one_head_filter_pi_star | 275 | 22.4870 | 0.9273 | 0.5273 | -0.5305 | -0.0016 | 0.1309 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1111_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 0.9370 | 0.5385 | -0.4447 | -0.0020 | 0.1538 | ok | RAN |
| ETHUSDT | 4 | `ema1111_above_at_h` | one_head_filter_pi_star | 119 | 9.8209 | 0.9497 | 0.5546 | -0.2300 | -0.0022 | 0.1176 | ok | RAN |
| ETHUSDT | 8 | `ema1111_below_at_h` | one_head_filter_pi_star | 238 | 19.4424 | 0.9235 | 0.5378 | -0.5655 | -0.0025 | 0.1471 | ok | RAN |
| ETHUSDT | 8 | `ema1111_above_at_h` | one_head_filter_pi_star | 114 | 9.3707 | 0.8387 | 0.5351 | -0.7569 | -0.0072 | 0.1140 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1111_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1111_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1111_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1111_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1111_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1111_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1111_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1111_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1111_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1111_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1111_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1111_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1111_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1111_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1111_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
