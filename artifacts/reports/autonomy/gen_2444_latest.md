# Autonomy public-indicator hunt gen 2444

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T185937Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1101_above_at_h` | one_head_filter_pi_star | 103 | 8.3987 | 1.2358 | 0.6117 | 0.9283 | 0.0039 | 0.1456 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1101_above_at_h` | one_head_filter_pi_star | 108 | 8.8064 | 1.1891 | 0.6019 | 0.7497 | 0.0033 | 0.1389 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema1101_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9780 | 0.5420 | -0.1525 | -0.0005 | 0.1260 | ok | RAN |
| SOLUSDT | 8 | `ema1101_below_at_h` | one_head_filter_pi_star | 236 | 19.2979 | 0.9424 | 0.5339 | -0.3836 | -0.0012 | 0.1229 | ok | RAN |
| ETHUSDT | 4 | `ema1101_below_at_h` | one_head_filter_pi_star | 223 | 18.2171 | 0.9575 | 0.5426 | -0.2866 | -0.0013 | 0.1525 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1101_below_at_h` | one_head_filter_pi_star | 248 | 20.2593 | 0.8954 | 0.5363 | -0.8012 | -0.0035 | 0.1452 | ok | RAN |
| ETHUSDT | 4 | `ema1101_above_at_h` | one_head_filter_pi_star | 112 | 9.2432 | 0.8361 | 0.5357 | -0.7441 | -0.0074 | 0.0982 | ok | RAN |
| ETHUSDT | 8 | `ema1101_above_at_h` | one_head_filter_pi_star | 104 | 8.5830 | 0.8304 | 0.5288 | -0.7762 | -0.0077 | 0.1154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1101_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1101_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1101_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1101_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1101_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1101_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1101_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1101_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1101_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1101_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1101_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1101_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1101_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1101_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1101_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1101_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
