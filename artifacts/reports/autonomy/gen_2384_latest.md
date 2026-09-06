# Autonomy public-indicator hunt gen 2384

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T114932Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5560_above_at_h` | one_head_filter_pi_star | 52 | 4.8824 | 3.0599 | 0.7115 | 3.0520 | 0.0192 | 0.1346 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5560_above_at_h` | one_head_filter_pi_star | 52 | 4.8824 | 2.1445 | 0.6346 | 2.1826 | 0.0148 | 0.1346 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5560_above_at_h` | one_head_filter_pi_star | 36 | 10.5076 | 1.0605 | 0.5556 | 0.2900 | 0.0027 | 0.1944 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5560_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9918 | 0.5605 | -0.0655 | -0.0003 | 0.1327 | ok | RAN |
| SOLUSDT | 8 | `sma5560_below_at_h` | one_head_filter_pi_star | 312 | 25.5125 | 0.9776 | 0.5353 | -0.1726 | -0.0005 | 0.1314 | ok | RAN |
| ETHUSDT | 8 | `sma5560_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9796 | 0.5572 | -0.1687 | -0.0007 | 0.1320 | ok | RAN |
| SOLUSDT | 4 | `sma5560_below_at_h` | one_head_filter_pi_star | 303 | 24.6496 | 0.9417 | 0.5281 | -0.4507 | -0.0012 | 0.1353 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5560_above_at_h` | one_head_filter_pi_star | 36 | 10.8636 | 0.8706 | 0.5000 | -0.6452 | -0.0066 | 0.1389 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5560_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5560_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
