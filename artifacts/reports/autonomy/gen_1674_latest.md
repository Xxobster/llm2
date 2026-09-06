# Autonomy public-indicator hunt gen 1674

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T011833Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ret1528_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 0.9919 | 0.5441 | -0.0621 | -0.0002 | 0.1337 | ok | RAN |
| SOLUSDT | 4 | `ret1528_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 0.9791 | 0.5420 | -0.1662 | -0.0004 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `ret1528_pos_at_h` | one_head_filter_pi_star | 17 | 1.9977 | 0.9869 | 0.5882 | -0.0287 | -0.0006 | 0.1765 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ret1528_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9375 | 0.5487 | -0.5149 | -0.0021 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `ret1528_neg_at_h` | one_head_filter_pi_star | 350 | 28.4732 | 0.9323 | 0.5514 | -0.5596 | -0.0023 | 0.1400 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1528_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5076 | 0.2353 | -1.0300 | -0.0491 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1528_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4124 | 0.2353 | -1.3306 | -0.0692 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1528_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret1528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1528_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1528_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ret1528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1528_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1528_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1528_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1528_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
