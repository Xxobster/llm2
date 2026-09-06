# Autonomy public-indicator hunt gen 2328

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T040120Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5420_above_at_h` | one_head_filter_pi_star | 51 | 4.3428 | 1.9901 | 0.6275 | 1.8682 | 0.0148 | 0.1176 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5420_above_at_h` | one_head_filter_pi_star | 57 | 5.3518 | 2.1108 | 0.6491 | 2.1895 | 0.0141 | 0.1228 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5420_below_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.0024 | 0.5605 | 0.0193 | 0.0001 | 0.1327 | ok | RAN |
| SOLUSDT | 8 | `sma5420_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 0.9838 | 0.5407 | -0.1212 | -0.0003 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `sma5420_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9815 | 0.5601 | -0.1524 | -0.0006 | 0.1320 | ok | RAN |
| SOLUSDT | 4 | `sma5420_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 0.9646 | 0.5318 | -0.2723 | -0.0007 | 0.1338 | ok | RAN |
| ETHUSDT | 4 | `sma5420_above_at_h` | one_head_filter_pi_star | 29 | 8.7512 | 0.9648 | 0.5172 | -0.1434 | -0.0017 | 0.1379 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5420_above_at_h` | one_head_filter_pi_star | 24 | 7.2424 | 0.8999 | 0.5000 | -0.4125 | -0.0048 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5420_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5420_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
