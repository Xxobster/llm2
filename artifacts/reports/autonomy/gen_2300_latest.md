# Autonomy public-indicator hunt gen 2300

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T004119Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1082_above_at_h` | one_head_filter_pi_star | 118 | 9.6218 | 1.2133 | 0.5932 | 0.8898 | 0.0036 | 0.1271 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1082_above_at_h` | one_head_filter_pi_star | 119 | 9.7808 | 1.0955 | 0.5714 | 0.4203 | 0.0017 | 0.1429 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1082_below_at_h` | one_head_filter_pi_star | 244 | 19.9326 | 1.0019 | 0.5533 | 0.0138 | 0.0001 | 0.1557 | ok | RAN |
| SOLUSDT | 8 | `ema1082_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9538 | 0.5397 | -0.3209 | -0.0010 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `ema1082_below_at_h` | one_head_filter_pi_star | 265 | 21.6693 | 0.9245 | 0.5321 | -0.5420 | -0.0016 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1082_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9270 | 0.5391 | -0.5512 | -0.0024 | 0.1481 | ok | RAN |
| ETHUSDT | 4 | `ema1082_above_at_h` | one_head_filter_pi_star | 120 | 9.8638 | 0.9379 | 0.5500 | -0.2850 | -0.0026 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `ema1082_above_at_h` | one_head_filter_pi_star | 113 | 9.2885 | 0.9027 | 0.5398 | -0.4287 | -0.0043 | 0.1150 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1082_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1082_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1082_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1082_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1082_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1082_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1082_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1082_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1082_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1082_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1082_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1082_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1082_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1082_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1082_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1082_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
