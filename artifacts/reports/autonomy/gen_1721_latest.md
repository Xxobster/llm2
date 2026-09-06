# Autonomy public-indicator hunt gen 1721

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T070432Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3860_above_at_h` | one_head_filter_pi_star | 87 | 7.1356 | 1.6826 | 0.6552 | 1.8603 | 0.0087 | 0.1034 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3860_above_at_h` | one_head_filter_pi_star | 89 | 7.2997 | 1.4743 | 0.6292 | 1.4122 | 0.0068 | 0.1124 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema3860_below_at_h` | one_head_filter_pi_star | 285 | 23.3047 | 1.0362 | 0.5439 | 0.2591 | 0.0007 | 0.1333 | ok | RAN |
| SOLUSDT | 4 | `ema3860_below_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.0135 | 0.5412 | 0.0963 | 0.0003 | 0.1326 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema3860_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9752 | 0.5572 | -0.1959 | -0.0008 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `ema3860_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9728 | 0.5575 | -0.2180 | -0.0009 | 0.1327 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema3860_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8252 | 0.5000 | -0.8162 | -0.0079 | 0.1562 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema3860_above_at_h` | one_head_filter_pi_star | 20 | 6.0353 | 0.5423 | 0.4000 | -2.0988 | -0.0259 | 0.2000 | ok | RAN |
| ETHUSDT | 4 | `ema3860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
