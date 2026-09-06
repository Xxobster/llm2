# Autonomy public-indicator hunt gen 1769

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T113120Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema3980_above_at_h` | one_head_filter_pi_star | 67 | 5.5078 | 1.6302 | 0.6567 | 1.4894 | 0.0086 | 0.0896 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema3980_above_at_h` | one_head_filter_pi_star | 81 | 6.6435 | 1.6474 | 0.6420 | 1.7013 | 0.0082 | 0.0988 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema3980_above_at_h` | one_head_filter_pi_star | 35 | 4.1128 | 1.1374 | 0.5714 | 0.3652 | 0.0057 | 0.1714 | ok | RAN |
| SOLUSDT | 4 | `ema3980_below_at_h` | one_head_filter_pi_star | 299 | 24.4495 | 1.0284 | 0.5418 | 0.2071 | 0.0006 | 0.1338 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema3980_below_at_h` | one_head_filter_pi_star | 302 | 24.6948 | 1.0038 | 0.5397 | 0.0289 | 0.0001 | 0.1325 | ok | RAN |
| ETHUSDT | 8 | `ema3980_below_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 0.9744 | 0.5587 | -0.2113 | -0.0008 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `ema3980_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9557 | 0.5552 | -0.3702 | -0.0015 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema3980_above_at_h` | one_head_filter_pi_star | 25 | 7.5441 | 0.7632 | 0.4800 | -1.0192 | -0.0109 | 0.1200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema3980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema3980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema3980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema3980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema3980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3980_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema3980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema3980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3980_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema3980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema3980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
