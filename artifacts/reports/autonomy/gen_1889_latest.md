# Autonomy public-indicator hunt gen 1889

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T222523Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema4280_above_at_h` | one_head_filter_pi_star | 63 | 5.1790 | 1.7600 | 0.6508 | 1.6739 | 0.0098 | 0.1111 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4280_above_at_h` | one_head_filter_pi_star | 83 | 6.8231 | 1.4484 | 0.6145 | 1.3284 | 0.0070 | 0.0964 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `ema4280_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9951 | 0.5409 | -0.0374 | -0.0001 | 0.1352 | ok | RAN |
| SOLUSDT | 4 | `ema4280_below_at_h` | one_head_filter_pi_star | 290 | 23.7136 | 0.9931 | 0.5310 | -0.0503 | -0.0001 | 0.1379 | ok | RAN |
| ETHUSDT | 8 | `ema4280_below_at_h` | one_head_filter_pi_star | 354 | 28.7986 | 0.9769 | 0.5593 | -0.1935 | -0.0008 | 0.1328 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema4280_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9472 | 0.5533 | -0.4289 | -0.0017 | 0.1331 | ok | RAN |
| ETHUSDT | 4 | `ema4280_above_at_h` | one_head_filter_pi_star | 29 | 8.7512 | 0.7647 | 0.4828 | -1.0808 | -0.0112 | 0.1379 | ok | RAN |
| ETHUSDT | 8 | `ema4280_above_at_h` | one_head_filter_pi_star | 29 | 8.7512 | 0.7687 | 0.4828 | -1.0599 | -0.0113 | 0.1724 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4280_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4280_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
