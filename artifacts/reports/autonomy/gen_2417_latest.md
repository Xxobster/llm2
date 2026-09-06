# Autonomy public-indicator hunt gen 2417

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T154839Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5600_above_at_h` | one_head_filter_pi_star | 30 | 2.7815 | 2.0269 | 0.6000 | 1.4300 | 0.0129 | 0.0667 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5600_above_at_h` | one_head_filter_pi_star | 33 | 3.0597 | 1.7455 | 0.5758 | 1.1913 | 0.0096 | 0.0909 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5600_below_at_h` | one_head_filter_pi_star | 301 | 24.6130 | 1.0105 | 0.5449 | 0.0770 | 0.0002 | 0.1329 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5600_below_at_h` | one_head_filter_pi_star | 326 | 26.6573 | 0.9655 | 0.5337 | -0.2705 | -0.0007 | 0.1319 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema5600_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9364 | 0.5526 | -0.5324 | -0.0021 | 0.1345 | ok | RAN |
| ETHUSDT | 8 | `ema5600_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9214 | 0.5490 | -0.6571 | -0.0026 | 0.1365 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5600_above_at_h` | one_head_filter_pi_star | 42 | 11.3728 | 0.6503 | 0.4524 | -2.1247 | -0.0187 | 0.1429 | ok | RAN |
| ETHUSDT | 8 | `ema5600_above_at_h` | one_head_filter_pi_star | 45 | 13.1346 | 0.6853 | 0.4667 | -2.0466 | -0.0188 | 0.1778 | ok | RAN |
| BTCUSDT | 8 | `ema5600_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0602 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5600_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0642 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
