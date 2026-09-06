# Autonomy public-indicator hunt gen 1804

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T144643Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1016_above_at_h` | one_head_filter_pi_star | 123 | 10.0295 | 1.2580 | 0.6179 | 1.0434 | 0.0044 | 0.1463 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1016_above_at_h` | one_head_filter_pi_star | 117 | 9.5402 | 1.0892 | 0.5726 | 0.3937 | 0.0017 | 0.1282 | ok | RAN |
| SOLUSDT | 4 | `ema1016_below_at_h` | one_head_filter_pi_star | 244 | 19.9521 | 1.0100 | 0.5492 | 0.0657 | 0.0002 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema1016_below_at_h` | one_head_filter_pi_star | 252 | 20.6063 | 0.9746 | 0.5397 | -0.1747 | -0.0005 | 0.1310 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1016_below_at_h` | one_head_filter_pi_star | 235 | 19.1973 | 0.9129 | 0.5404 | -0.6299 | -0.0028 | 0.1532 | ok | RAN |
| ETHUSDT | 8 | `ema1016_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 0.9110 | 0.5417 | -0.6122 | -0.0028 | 0.1528 | ok | RAN |
| ETHUSDT | 8 | `ema1016_above_at_h` | one_head_filter_pi_star | 120 | 9.9026 | 0.9253 | 0.5500 | -0.3494 | -0.0032 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `ema1016_above_at_h` | one_head_filter_pi_star | 124 | 10.2335 | 0.8407 | 0.5403 | -0.7860 | -0.0069 | 0.1371 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1016_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0536 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1016_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0547 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1016_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1016_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1016_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1016_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1016_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1016_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1016_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1016_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1016_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1016_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1016_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1016_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1016_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1016_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
