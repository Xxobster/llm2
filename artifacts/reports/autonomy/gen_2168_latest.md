# Autonomy public-indicator hunt gen 2168

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T074300Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5020_above_at_h` | one_head_filter_pi_star | 56 | 4.7034 | 2.2275 | 0.6071 | 2.1456 | 0.0145 | 0.1071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5020_above_at_h` | one_head_filter_pi_star | 58 | 4.8714 | 1.3046 | 0.5690 | 0.7636 | 0.0050 | 0.1379 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma5020_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0245 | 0.5625 | 0.1953 | 0.0008 | 0.1369 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma5020_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9941 | 0.5569 | -0.0470 | -0.0002 | 0.1347 | ok | RAN |
| SOLUSDT | 8 | `sma5020_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 0.9707 | 0.5402 | -0.2238 | -0.0006 | 0.1350 | ok | RAN |
| SOLUSDT | 4 | `sma5020_below_at_h` | one_head_filter_pi_star | 290 | 23.5921 | 0.9671 | 0.5310 | -0.2434 | -0.0007 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5020_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.7379 | 0.4706 | -1.5873 | -0.0140 | 0.1176 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma5020_above_at_h` | one_head_filter_pi_star | 40 | 11.8025 | 0.6988 | 0.4750 | -2.0888 | -0.0180 | 0.1750 | ok | RAN |
| ETHUSDT | 4 | `sma5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5020_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5020_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5020_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5020_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5020_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
