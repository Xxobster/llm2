# Autonomy public-indicator hunt gen 2345

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T062937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema5420_above_at_h` | one_head_filter_pi_star | 25 | 2.3473 | 3.2571 | 0.7200 | 2.1002 | 0.0215 | 0.0800 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema5420_above_at_h` | one_head_filter_pi_star | 46 | 3.9983 | 1.9979 | 0.6522 | 1.7878 | 0.0132 | 0.1304 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5420_below_at_h` | one_head_filter_pi_star | 328 | 26.8208 | 0.9626 | 0.5366 | -0.2967 | -0.0008 | 0.1250 | ok | RAN |
| SOLUSDT | 8 | `ema5420_below_at_h` | one_head_filter_pi_star | 317 | 25.9214 | 0.9388 | 0.5300 | -0.4860 | -0.0013 | 0.1293 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5420_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9419 | 0.5526 | -0.4897 | -0.0019 | 0.1374 | ok | RAN |
| ETHUSDT | 8 | `ema5420_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9281 | 0.5497 | -0.6098 | -0.0024 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `ema5420_above_at_h` | one_head_filter_pi_star | 43 | 7.3242 | 0.9045 | 0.5116 | -0.3803 | -0.0043 | 0.1628 | ok | RAN |
| ETHUSDT | 8 | `ema5420_above_at_h` | one_head_filter_pi_star | 45 | 12.1987 | 0.8774 | 0.5111 | -0.6866 | -0.0061 | 0.1778 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5420_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6104 | 0.3000 | -0.8674 | -0.0426 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5420_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5593 | 0.2941 | -0.9437 | -0.0562 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
