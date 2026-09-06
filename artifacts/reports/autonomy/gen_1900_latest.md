# Autonomy public-indicator hunt gen 1900

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T232459Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1029_above_at_h` | one_head_filter_pi_star | 112 | 9.1325 | 1.2217 | 0.6071 | 0.8695 | 0.0038 | 0.1429 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1029_above_at_h` | one_head_filter_pi_star | 122 | 9.9479 | 1.1121 | 0.5656 | 0.4890 | 0.0021 | 0.1148 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1029_below_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 0.9700 | 0.5412 | -0.2081 | -0.0006 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `ema1029_above_at_h` | one_head_filter_pi_star | 129 | 10.6462 | 0.9798 | 0.5581 | -0.0935 | -0.0009 | 0.1240 | ok | RAN |
| SOLUSDT | 4 | `ema1029_below_at_h` | one_head_filter_pi_star | 269 | 21.8837 | 0.9324 | 0.5316 | -0.4875 | -0.0015 | 0.1301 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1029_below_at_h` | one_head_filter_pi_star | 229 | 18.7072 | 0.9242 | 0.5371 | -0.5450 | -0.0024 | 0.1528 | ok | RAN |
| ETHUSDT | 4 | `ema1029_below_at_h` | one_head_filter_pi_star | 243 | 19.8509 | 0.9101 | 0.5350 | -0.6624 | -0.0030 | 0.1481 | ok | RAN |
| ETHUSDT | 8 | `ema1029_above_at_h` | one_head_filter_pi_star | 125 | 10.3160 | 0.9267 | 0.5440 | -0.3569 | -0.0031 | 0.1200 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1029_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1029_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1029_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1029_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1029_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1029_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1029_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1029_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1029_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1029_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1029_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1029_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1029_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1029_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1029_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1029_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
