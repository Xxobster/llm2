# Autonomy public-indicator hunt gen 2440

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T183132Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5700_above_at_h` | one_head_filter_pi_star | 41 | 3.8496 | 3.8793 | 0.7317 | 3.0664 | 0.0243 | 0.1220 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma5700_above_at_h` | one_head_filter_pi_star | 51 | 4.3428 | 2.0782 | 0.6275 | 2.0186 | 0.0147 | 0.0980 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5700_below_at_h` | one_head_filter_pi_star | 335 | 27.2529 | 1.0081 | 0.5612 | 0.0646 | 0.0003 | 0.1313 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5700_below_at_h` | one_head_filter_pi_star | 318 | 25.8699 | 0.9689 | 0.5346 | -0.2397 | -0.0006 | 0.1258 | ok | RAN |
| ETHUSDT | 4 | `sma5700_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9760 | 0.5565 | -0.1937 | -0.0008 | 0.1310 | ok | RAN |
| SOLUSDT | 8 | `sma5700_below_at_h` | one_head_filter_pi_star | 344 | 27.9851 | 0.9467 | 0.5349 | -0.4368 | -0.0011 | 0.1250 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5700_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.9191 | 0.5294 | -0.3853 | -0.0039 | 0.1471 | ok | RAN |
| ETHUSDT | 4 | `sma5700_above_at_h` | one_head_filter_pi_star | 36 | 10.8636 | 0.7276 | 0.4722 | -1.6316 | -0.0153 | 0.1389 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5700_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5700_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
