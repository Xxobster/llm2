# Autonomy public-indicator hunt gen 2449

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T193314Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema5680_above_at_h` | one_head_filter_pi_star | 47 | 4.0379 | 1.7294 | 0.5957 | 1.4554 | 0.0105 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `ema5680_above_at_h` | one_head_filter_pi_star | 37 | 3.4740 | 1.5943 | 0.5676 | 1.1113 | 0.0089 | 0.1081 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema5680_below_at_h` | one_head_filter_pi_star | 319 | 26.0849 | 0.9993 | 0.5423 | -0.0049 | -0.0000 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `ema5680_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9767 | 0.5581 | -0.1889 | -0.0008 | 0.1395 | ok | RAN |
| SOLUSDT | 8 | `ema5680_below_at_h` | one_head_filter_pi_star | 329 | 26.9026 | 0.9621 | 0.5350 | -0.2996 | -0.0008 | 0.1307 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema5680_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 0.9280 | 0.5500 | -0.6028 | -0.0024 | 0.1353 | ok | RAN |
| ETHUSDT | 8 | `ema5680_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.9274 | 0.5294 | -0.3564 | -0.0036 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `ema5680_above_at_h` | one_head_filter_pi_star | 38 | 10.2897 | 0.8098 | 0.5000 | -0.9432 | -0.0094 | 0.1316 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema5680_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5261 | 0.2778 | -1.0707 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema5680_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5440 | 0.3000 | -1.0991 | -0.0584 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema5680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
