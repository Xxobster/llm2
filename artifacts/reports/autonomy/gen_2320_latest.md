# Autonomy public-indicator hunt gen 2320

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T030511Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5400_above_at_h` | one_head_filter_pi_star | 62 | 5.2794 | 2.2427 | 0.6774 | 2.3010 | 0.0150 | 0.0968 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma5400_above_at_h` | one_head_filter_pi_star | 58 | 4.9388 | 2.1369 | 0.6552 | 2.1350 | 0.0145 | 0.1034 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma5400_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 1.1682 | 0.5556 | 0.6197 | 0.0063 | 0.1481 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma5400_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 0.9873 | 0.5407 | -0.0944 | -0.0003 | 0.1303 | ok | RAN |
| ETHUSDT | 4 | `sma5400_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9897 | 0.5579 | -0.0843 | -0.0003 | 0.1335 | ok | RAN |
| ETHUSDT | 8 | `sma5400_below_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 0.9854 | 0.5598 | -0.1197 | -0.0005 | 0.1341 | ok | RAN |
| SOLUSDT | 4 | `sma5400_below_at_h` | one_head_filter_pi_star | 314 | 25.5445 | 0.9489 | 0.5318 | -0.3934 | -0.0010 | 0.1338 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5400_above_at_h` | one_head_filter_pi_star | 32 | 9.6565 | 0.8172 | 0.5000 | -0.9713 | -0.0091 | 0.1250 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5400_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5400_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5400_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5400_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
