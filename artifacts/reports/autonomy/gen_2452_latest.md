# Autonomy public-indicator hunt gen 2452

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T195323Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1102_above_at_h` | one_head_filter_pi_star | 106 | 8.6925 | 1.2453 | 0.6038 | 0.9535 | 0.0040 | 0.1321 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1102_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.1986 | 0.5804 | 0.8005 | 0.0033 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1102_below_at_h` | one_head_filter_pi_star | 232 | 18.9523 | 0.9932 | 0.5517 | -0.0471 | -0.0002 | 0.1466 | ok | RAN |
| SOLUSDT | 4 | `ema1102_below_at_h` | one_head_filter_pi_star | 262 | 21.4240 | 0.9769 | 0.5420 | -0.1617 | -0.0005 | 0.1298 | ok | RAN |
| SOLUSDT | 8 | `ema1102_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 0.9301 | 0.5253 | -0.5001 | -0.0015 | 0.1323 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1102_below_at_h` | one_head_filter_pi_star | 248 | 20.2593 | 0.9380 | 0.5403 | -0.4591 | -0.0020 | 0.1492 | ok | RAN |
| ETHUSDT | 4 | `ema1102_above_at_h` | one_head_filter_pi_star | 105 | 8.6655 | 0.8852 | 0.5429 | -0.5137 | -0.0046 | 0.1143 | ok | RAN |
| ETHUSDT | 8 | `ema1102_above_at_h` | one_head_filter_pi_star | 104 | 8.5830 | 0.8466 | 0.5288 | -0.6778 | -0.0068 | 0.1154 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1102_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1102_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1102_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1102_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1102_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1102_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
