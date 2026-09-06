# Autonomy public-indicator hunt gen 2364

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T085349Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1090_above_at_h` | one_head_filter_pi_star | 109 | 8.8879 | 1.2636 | 0.6239 | 1.0313 | 0.0043 | 0.1468 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1090_above_at_h` | one_head_filter_pi_star | 113 | 9.2877 | 1.1882 | 0.6018 | 0.7809 | 0.0033 | 0.1327 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1090_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9890 | 0.5574 | -0.0763 | -0.0003 | 0.1532 | ok | RAN |
| SOLUSDT | 4 | `ema1090_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9727 | 0.5465 | -0.1877 | -0.0006 | 0.1357 | ok | RAN |
| SOLUSDT | 8 | `ema1090_below_at_h` | one_head_filter_pi_star | 261 | 21.3422 | 0.9675 | 0.5364 | -0.2285 | -0.0007 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema1090_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9366 | 0.5485 | -0.4513 | -0.0020 | 0.1519 | ok | RAN |
| ETHUSDT | 4 | `ema1090_above_at_h` | one_head_filter_pi_star | 127 | 10.4392 | 0.9323 | 0.5512 | -0.3215 | -0.0031 | 0.1260 | ok | RAN |
| ETHUSDT | 8 | `ema1090_above_at_h` | one_head_filter_pi_star | 121 | 9.9859 | 0.8897 | 0.5372 | -0.5243 | -0.0048 | 0.1240 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1090_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1090_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1090_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1090_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1090_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1090_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1090_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1090_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1090_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1090_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1090_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1090_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1090_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1090_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1090_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1090_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
