# Autonomy public-indicator hunt gen 1876

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T211601Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema1026_above_at_h` | one_head_filter_pi_star | 109 | 8.9594 | 1.2313 | 0.6147 | 0.8922 | 0.0040 | 0.1376 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1026_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.1564 | 0.5854 | 0.6918 | 0.0027 | 0.1301 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `ema1026_below_at_h` | one_head_filter_pi_star | 214 | 17.4818 | 0.9797 | 0.5514 | -0.1304 | -0.0006 | 0.1589 | ok | RAN |
| SOLUSDT | 4 | `ema1026_below_at_h` | one_head_filter_pi_star | 249 | 20.3609 | 0.9609 | 0.5382 | -0.2665 | -0.0008 | 0.1205 | ok | RAN |
| SOLUSDT | 8 | `ema1026_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9357 | 0.5349 | -0.4567 | -0.0014 | 0.1279 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1026_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9235 | 0.5359 | -0.5523 | -0.0024 | 0.1435 | ok | RAN |
| ETHUSDT | 4 | `ema1026_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.9398 | 0.5565 | -0.2869 | -0.0026 | 0.1210 | ok | RAN |
| ETHUSDT | 8 | `ema1026_above_at_h` | one_head_filter_pi_star | 122 | 10.0282 | 0.9327 | 0.5492 | -0.3091 | -0.0028 | 0.1311 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1026_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0294 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1026_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1026_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1026_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1026_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1026_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1026_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1026_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1026_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1026_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1026_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1026_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1026_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1026_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1026_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1026_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
