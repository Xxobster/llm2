# Autonomy public-indicator hunt gen 2336

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T051728Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5440_above_at_h` | one_head_filter_pi_star | 49 | 4.1725 | 2.0135 | 0.6327 | 1.8829 | 0.0150 | 0.1020 | ok | RAN |
| SOLUSDT | 4 | `sma5440_above_at_h` | one_head_filter_pi_star | 58 | 4.9388 | 2.0402 | 0.6552 | 2.0830 | 0.0149 | 0.1034 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5440_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9983 | 0.5625 | -0.0138 | -0.0001 | 0.1310 | ok | RAN |
| ETHUSDT | 8 | `sma5440_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9968 | 0.5605 | -0.0257 | -0.0001 | 0.1357 | ok | RAN |
| SOLUSDT | 8 | `sma5440_below_at_h` | one_head_filter_pi_star | 313 | 25.4632 | 0.9736 | 0.5304 | -0.2027 | -0.0005 | 0.1278 | ok | RAN |
| SOLUSDT | 4 | `sma5440_below_at_h` | one_head_filter_pi_star | 310 | 25.3490 | 0.9676 | 0.5355 | -0.2474 | -0.0007 | 0.1290 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5440_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.7951 | 0.5000 | -1.0415 | -0.0102 | 0.1176 | ok | RAN |
| ETHUSDT | 8 | `sma5440_above_at_h` | one_head_filter_pi_star | 42 | 12.2589 | 0.7866 | 0.5000 | -1.3772 | -0.0124 | 0.1429 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5440_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
