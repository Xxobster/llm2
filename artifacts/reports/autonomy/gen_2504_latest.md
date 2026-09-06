# Autonomy public-indicator hunt gen 2504

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T013429Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5860_above_at_h` | one_head_filter_pi_star | 51 | 4.7885 | 2.2907 | 0.6863 | 2.2429 | 0.0170 | 0.0980 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5860_above_at_h` | one_head_filter_pi_star | 61 | 5.3928 | 1.8170 | 0.6393 | 1.8052 | 0.0114 | 0.0820 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5860_below_at_h` | one_head_filter_pi_star | 324 | 26.4938 | 0.9699 | 0.5340 | -0.2366 | -0.0006 | 0.1296 | ok | RAN |
| ETHUSDT | 4 | `sma5860_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9669 | 0.5562 | -0.2687 | -0.0011 | 0.1361 | ok | RAN |
| ETHUSDT | 8 | `sma5860_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9604 | 0.5546 | -0.3274 | -0.0013 | 0.1357 | ok | RAN |
| SOLUSDT | 4 | `sma5860_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 0.9267 | 0.5260 | -0.5726 | -0.0016 | 0.1299 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5860_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8595 | 0.5000 | -0.6786 | -0.0064 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `sma5860_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8546 | 0.5000 | -0.7032 | -0.0068 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5860_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5860_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5860_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5860_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
