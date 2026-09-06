# Autonomy public-indicator hunt gen 2476

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T223632Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1105_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.1809 | 0.6117 | 0.7217 | 0.0031 | 0.1262 | ok | RAN |
| SOLUSDT | 4 | `ema1105_above_at_h` | one_head_filter_pi_star | 108 | 8.8767 | 1.1621 | 0.5926 | 0.6821 | 0.0028 | 0.1296 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1105_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9906 | 0.5434 | -0.0649 | -0.0002 | 0.1321 | ok | RAN |
| SOLUSDT | 4 | `ema1105_below_at_h` | one_head_filter_pi_star | 269 | 21.9964 | 0.9390 | 0.5390 | -0.4404 | -0.0013 | 0.1338 | ok | RAN |
| ETHUSDT | 8 | `ema1105_below_at_h` | one_head_filter_pi_star | 252 | 20.5861 | 0.9571 | 0.5437 | -0.3259 | -0.0014 | 0.1508 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1105_below_at_h` | one_head_filter_pi_star | 240 | 19.6058 | 0.9289 | 0.5375 | -0.5141 | -0.0023 | 0.1500 | ok | RAN |
| ETHUSDT | 8 | `ema1105_above_at_h` | one_head_filter_pi_star | 105 | 8.6655 | 0.8894 | 0.5429 | -0.5010 | -0.0048 | 0.1143 | ok | RAN |
| ETHUSDT | 4 | `ema1105_above_at_h` | one_head_filter_pi_star | 123 | 10.1104 | 0.8482 | 0.5366 | -0.7280 | -0.0069 | 0.1138 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1105_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0288 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1105_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1105_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1105_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1105_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1105_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
