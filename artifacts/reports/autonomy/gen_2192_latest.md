# Autonomy public-indicator hunt gen 2192

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T112810Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5080_above_at_h` | one_head_filter_pi_star | 44 | 3.8804 | 1.9954 | 0.5909 | 1.7117 | 0.0127 | 0.0909 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5080_above_at_h` | one_head_filter_pi_star | 60 | 5.0394 | 1.5250 | 0.5833 | 1.2158 | 0.0074 | 0.1167 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5080_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 0.9935 | 0.5582 | -0.0528 | -0.0002 | 0.1373 | ok | RAN |
| ETHUSDT | 4 | `sma5080_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9816 | 0.5569 | -0.1472 | -0.0006 | 0.1317 | ok | RAN |
| SOLUSDT | 4 | `sma5080_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 0.9564 | 0.5294 | -0.3313 | -0.0009 | 0.1340 | ok | RAN |
| SOLUSDT | 8 | `sma5080_below_at_h` | one_head_filter_pi_star | 306 | 24.8937 | 0.9425 | 0.5327 | -0.4415 | -0.0012 | 0.1275 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5080_above_at_h` | one_head_filter_pi_star | 35 | 10.5618 | 0.8281 | 0.5143 | -0.9973 | -0.0084 | 0.1143 | ok | RAN |
| ETHUSDT | 8 | `sma5080_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.7654 | 0.5000 | -1.4192 | -0.0124 | 0.1111 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5080_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5080_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5080_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5080_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5080_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
