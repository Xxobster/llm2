# Autonomy public-indicator hunt gen 2420

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T160857Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `ema1097_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0788 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1097_below_at_h` | one_head_filter_pi_star | 10 | 1.2643 | 1.8915 | 0.6000 | 1.0949 | 0.0757 | 0.1000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema1097_above_at_h` | one_head_filter_pi_star | 114 | 9.2956 | 1.1850 | 0.5877 | 0.7636 | 0.0032 | 0.1404 | ok | RAN |
| SOLUSDT | 4 | `ema1097_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.0779 | 0.5508 | 0.3411 | 0.0014 | 0.1271 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1097_below_at_h` | one_head_filter_pi_star | 263 | 21.5057 | 0.9467 | 0.5361 | -0.3783 | -0.0011 | 0.1293 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1097_below_at_h` | one_head_filter_pi_star | 266 | 21.6396 | 0.9032 | 0.5226 | -0.7126 | -0.0021 | 0.1278 | ok | RAN |
| ETHUSDT | 4 | `ema1097_above_at_h` | one_head_filter_pi_star | 130 | 10.7278 | 0.9380 | 0.5462 | -0.2945 | -0.0026 | 0.1154 | ok | RAN |
| ETHUSDT | 8 | `ema1097_below_at_h` | one_head_filter_pi_star | 231 | 18.8706 | 0.9108 | 0.5411 | -0.6557 | -0.0029 | 0.1515 | ok | RAN |
| ETHUSDT | 4 | `ema1097_below_at_h` | one_head_filter_pi_star | 215 | 17.5635 | 0.8975 | 0.5395 | -0.7086 | -0.0033 | 0.1581 | ok | RAN |
| ETHUSDT | 8 | `ema1097_above_at_h` | one_head_filter_pi_star | 114 | 9.3707 | 0.8015 | 0.5263 | -0.9521 | -0.0091 | 0.1140 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1097_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1097_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4803 | 0.2941 | -1.1084 | -0.0580 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1097_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1097_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1097_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1097_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1097_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1097_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1097_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1097_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1097_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1097_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1097_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1097_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
