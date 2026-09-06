# Autonomy public-indicator hunt gen 2216

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T143607Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5140_above_at_h` | one_head_filter_pi_star | 51 | 4.3428 | 1.9080 | 0.6471 | 1.7401 | 0.0132 | 0.0980 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5140_above_at_h` | one_head_filter_pi_star | 50 | 4.2576 | 1.9873 | 0.6200 | 1.7883 | 0.0131 | 0.1400 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5140_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0216 | 0.5625 | 0.1710 | 0.0007 | 0.1339 | ok | RAN |
| ETHUSDT | 4 | `sma5140_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.0123 | 0.5612 | 0.0983 | 0.0004 | 0.1313 | ok | RAN |
| SOLUSDT | 4 | `sma5140_below_at_h` | one_head_filter_pi_star | 288 | 23.4294 | 1.0144 | 0.5382 | 0.1025 | 0.0003 | 0.1424 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5140_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 0.9898 | 0.5414 | -0.0771 | -0.0002 | 0.1306 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5140_above_at_h` | one_head_filter_pi_star | 36 | 10.6222 | 0.7763 | 0.5000 | -1.2004 | -0.0115 | 0.1944 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5140_above_at_h` | one_head_filter_pi_star | 37 | 10.9173 | 0.6177 | 0.4595 | -2.1288 | -0.0233 | 0.1351 | ok | RAN |
| ETHUSDT | 4 | `sma5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5140_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5140_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5140_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5140_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5140_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
