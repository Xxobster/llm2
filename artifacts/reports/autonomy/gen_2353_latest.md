# Autonomy public-indicator hunt gen 2353

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T072912Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5440_above_at_h` | one_head_filter_pi_star | 28 | 2.5961 | 3.0788 | 0.6786 | 2.0451 | 0.0201 | 0.0714 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5440_above_at_h` | one_head_filter_pi_star | 44 | 4.0796 | 1.3898 | 0.5682 | 0.8599 | 0.0059 | 0.1136 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5440_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9514 | 0.5283 | -0.3805 | -0.0010 | 0.1289 | ok | RAN |
| SOLUSDT | 8 | `ema5440_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 0.9499 | 0.5260 | -0.3897 | -0.0011 | 0.1331 | ok | RAN |
| ETHUSDT | 8 | `ema5440_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9655 | 0.5569 | -0.2839 | -0.0011 | 0.1341 | ok | RAN |
| ETHUSDT | 4 | `ema5440_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9610 | 0.5556 | -0.3181 | -0.0013 | 0.1374 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5440_above_at_h` | one_head_filter_pi_star | 45 | 13.1346 | 0.8811 | 0.5111 | -0.7148 | -0.0065 | 0.2000 | ok | RAN |
| ETHUSDT | 4 | `ema5440_above_at_h` | one_head_filter_pi_star | 39 | 6.6428 | 0.8293 | 0.5128 | -0.6636 | -0.0083 | 0.1282 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5440_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6251 | 0.3000 | -0.8291 | -0.0442 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5440_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5440_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5440_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5440_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
