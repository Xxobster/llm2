# Autonomy public-indicator hunt gen 2148

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T044331Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1062_above_at_h` | one_head_filter_pi_star | 106 | 8.7123 | 1.3118 | 0.6321 | 1.1696 | 0.0053 | 0.1415 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1062_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.2592 | 0.5946 | 1.0555 | 0.0044 | 0.1351 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1062_below_at_h` | one_head_filter_pi_star | 243 | 19.8703 | 1.0138 | 0.5514 | 0.0909 | 0.0003 | 0.1317 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1062_below_at_h` | one_head_filter_pi_star | 254 | 20.7698 | 0.9663 | 0.5433 | -0.2342 | -0.0007 | 0.1260 | ok | RAN |
| ETHUSDT | 8 | `ema1062_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9734 | 0.5485 | -0.1834 | -0.0008 | 0.1519 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1062_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.8848 | 0.5368 | -0.8518 | -0.0038 | 0.1558 | ok | RAN |
| ETHUSDT | 4 | `ema1062_above_at_h` | one_head_filter_pi_star | 119 | 9.8209 | 0.9014 | 0.5462 | -0.4566 | -0.0045 | 0.1176 | ok | RAN |
| ETHUSDT | 8 | `ema1062_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 0.8835 | 0.5405 | -0.5341 | -0.0052 | 0.1351 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1062_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1062_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0559 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1062_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1062_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1062_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1062_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1062_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1062_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1062_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1062_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1062_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1062_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1062_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1062_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1062_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1062_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
