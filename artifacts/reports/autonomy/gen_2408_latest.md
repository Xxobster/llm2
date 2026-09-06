# Autonomy public-indicator hunt gen 2408

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T144655Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5620_above_at_h` | one_head_filter_pi_star | 38 | 3.5679 | 2.9583 | 0.7105 | 2.4865 | 0.0216 | 0.1316 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5620_above_at_h` | one_head_filter_pi_star | 49 | 4.6007 | 2.1170 | 0.6531 | 2.0732 | 0.0142 | 0.1020 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5620_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.9895 | 0.5312 | -0.0475 | -0.0005 | 0.1562 | ok | RAN |
| ETHUSDT | 8 | `sma5620_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.9789 | 0.5312 | -0.0960 | -0.0009 | 0.1250 | ok | RAN |
| ETHUSDT | 8 | `sma5620_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 0.9696 | 0.5562 | -0.2541 | -0.0010 | 0.1361 | ok | RAN |
| SOLUSDT | 4 | `sma5620_below_at_h` | one_head_filter_pi_star | 319 | 25.9513 | 0.9518 | 0.5329 | -0.3744 | -0.0010 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `sma5620_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9627 | 0.5549 | -0.3056 | -0.0012 | 0.1335 | ok | RAN |
| SOLUSDT | 8 | `sma5620_below_at_h` | one_head_filter_pi_star | 306 | 25.0219 | 0.9257 | 0.5261 | -0.5774 | -0.0016 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5620_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5620_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5620_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5620_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5620_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
