# Autonomy public-indicator hunt gen 2329

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T040841Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5380_above_at_h` | one_head_filter_pi_star | 48 | 4.4505 | 1.8071 | 0.6458 | 1.6773 | 0.0115 | 0.1458 | ok | RAN |
| SOLUSDT | 8 | `ema5380_above_at_h` | one_head_filter_pi_star | 69 | 5.9280 | 1.8068 | 0.6667 | 1.9401 | 0.0107 | 0.1014 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5380_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9934 | 0.5409 | -0.0502 | -0.0001 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `ema5380_below_at_h` | one_head_filter_pi_star | 323 | 26.4120 | 0.9765 | 0.5387 | -0.1817 | -0.0005 | 0.1300 | ok | RAN |
| ETHUSDT | 4 | `ema5380_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9601 | 0.5549 | -0.3364 | -0.0013 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5380_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 0.9473 | 0.5516 | -0.4449 | -0.0018 | 0.1357 | ok | RAN |
| ETHUSDT | 8 | `ema5380_above_at_h` | one_head_filter_pi_star | 51 | 5.9853 | 0.9422 | 0.5490 | -0.2340 | -0.0028 | 0.1569 | ok | RAN |
| ETHUSDT | 4 | `ema5380_above_at_h` | one_head_filter_pi_star | 37 | 6.3022 | 0.9067 | 0.5405 | -0.3402 | -0.0045 | 0.1351 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5380_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5380_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0550 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
