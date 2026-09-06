# Autonomy public-indicator hunt gen 2489

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T235958Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5780_above_at_h` | one_head_filter_pi_star | 25 | 2.4080 | 3.2678 | 0.7200 | 2.1019 | 0.0205 | 0.0400 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema5780_above_at_h` | one_head_filter_pi_star | 38 | 3.5233 | 1.5276 | 0.5789 | 1.0099 | 0.0077 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema5780_below_at_h` | one_head_filter_pi_star | 325 | 26.5755 | 0.9800 | 0.5385 | -0.1562 | -0.0004 | 0.1292 | ok | RAN |
| ETHUSDT | 4 | `ema5780_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9750 | 0.5581 | -0.2061 | -0.0008 | 0.1366 | ok | RAN |
| SOLUSDT | 4 | `ema5780_below_at_h` | one_head_filter_pi_star | 317 | 25.9214 | 0.9605 | 0.5300 | -0.3061 | -0.0008 | 0.1325 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5780_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9487 | 0.5549 | -0.4284 | -0.0017 | 0.1329 | ok | RAN |
| ETHUSDT | 8 | `ema5780_above_at_h` | one_head_filter_pi_star | 39 | 11.7689 | 0.8366 | 0.5128 | -0.8359 | -0.0083 | 0.1538 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5780_above_at_h` | one_head_filter_pi_star | 44 | 12.8427 | 0.6801 | 0.4773 | -2.0814 | -0.0187 | 0.1818 | ok | RAN |
| BTCUSDT | 8 | `ema5780_above_at_h` | one_head_filter_pi_star | 21 | 1.7871 | 0.6195 | 0.3333 | -0.9018 | -0.0454 | 0.0476 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5780_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5780_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5780_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5780_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
