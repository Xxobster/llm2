# Autonomy public-indicator hunt gen 1945

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T033919Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema4420_above_at_h` | one_head_filter_pi_star | 73 | 6.0010 | 1.8260 | 0.6575 | 1.9853 | 0.0123 | 0.1096 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema4420_above_at_h` | one_head_filter_pi_star | 54 | 5.0068 | 1.7238 | 0.6296 | 1.6209 | 0.0108 | 0.1481 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema4420_below_at_h` | one_head_filter_pi_star | 305 | 24.9401 | 1.0230 | 0.5443 | 0.1684 | 0.0005 | 0.1311 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `ema4420_below_at_h` | one_head_filter_pi_star | 308 | 25.1854 | 0.9875 | 0.5325 | -0.0953 | -0.0003 | 0.1299 | ok | RAN |
| ETHUSDT | 4 | `ema4420_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9777 | 0.5585 | -0.1792 | -0.0007 | 0.1374 | ok | RAN |
| ETHUSDT | 8 | `ema4420_below_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 0.9686 | 0.5578 | -0.2616 | -0.0010 | 0.1358 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `ema4420_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.9519 | 0.5294 | -0.2305 | -0.0022 | 0.1176 | ok | RAN |
| ETHUSDT | 4 | `ema4420_above_at_h` | one_head_filter_pi_star | 31 | 9.3547 | 0.7964 | 0.4839 | -0.9577 | -0.0115 | 0.1613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema4420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema4420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema4420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema4420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema4420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4420_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema4420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4420_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema4420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
