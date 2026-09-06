# Autonomy public-indicator hunt gen 2433

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T174200Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5640_above_at_h` | one_head_filter_pi_star | 39 | 3.6160 | 1.7046 | 0.6154 | 1.2869 | 0.0099 | 0.1538 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5640_above_at_h` | one_head_filter_pi_star | 51 | 4.3816 | 1.2113 | 0.5686 | 0.5153 | 0.0033 | 0.0784 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5640_below_at_h` | one_head_filter_pi_star | 321 | 26.2484 | 0.9744 | 0.5389 | -0.1988 | -0.0005 | 0.1340 | ok | RAN |
| SOLUSDT | 8 | `ema5640_below_at_h` | one_head_filter_pi_star | 317 | 25.9214 | 0.9437 | 0.5268 | -0.4433 | -0.0012 | 0.1293 | ok | RAN |
| ETHUSDT | 8 | `ema5640_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9588 | 0.5539 | -0.3406 | -0.0014 | 0.1370 | ok | RAN |
| ETHUSDT | 4 | `ema5640_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9579 | 0.5543 | -0.3510 | -0.0014 | 0.1378 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5640_above_at_h` | one_head_filter_pi_star | 38 | 11.4671 | 0.8613 | 0.5263 | -0.7170 | -0.0076 | 0.1842 | ok | RAN |
| ETHUSDT | 8 | `ema5640_above_at_h` | one_head_filter_pi_star | 41 | 11.9670 | 0.7587 | 0.4878 | -1.4114 | -0.0128 | 0.1463 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5640_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5640_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4537 | 0.2500 | -1.3535 | -0.0715 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
