# Autonomy public-indicator hunt gen 2316

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T023630Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1084_above_at_h` | one_head_filter_pi_star | 115 | 9.3771 | 1.2852 | 0.6000 | 1.1301 | 0.0048 | 0.1391 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1084_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.1452 | 0.5856 | 0.6083 | 0.0026 | 0.1532 | ok | RAN |
| ETHUSDT | 8 | `ema1084_below_at_h` | one_head_filter_pi_star | 252 | 20.5861 | 1.0223 | 0.5516 | 0.1615 | 0.0007 | 0.1548 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1084_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 1.0007 | 0.5489 | 0.0050 | 0.0000 | 0.1532 | ok | RAN |
| SOLUSDT | 4 | `ema1084_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 0.9665 | 0.5412 | -0.2320 | -0.0007 | 0.1255 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `ema1084_below_at_h` | one_head_filter_pi_star | 260 | 21.2604 | 0.9197 | 0.5308 | -0.5751 | -0.0017 | 0.1269 | ok | RAN |
| ETHUSDT | 4 | `ema1084_above_at_h` | one_head_filter_pi_star | 131 | 10.7680 | 0.8962 | 0.5496 | -0.4966 | -0.0046 | 0.1221 | ok | RAN |
| ETHUSDT | 8 | `ema1084_above_at_h` | one_head_filter_pi_star | 101 | 8.3354 | 0.8336 | 0.5248 | -0.7588 | -0.0076 | 0.1188 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1084_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0307 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1084_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1084_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1084_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1084_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1084_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1084_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1084_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1084_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1084_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1084_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1084_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1084_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1084_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1084_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1084_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
