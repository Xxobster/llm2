# Autonomy public-indicator hunt gen 2344

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T062058Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5460_above_at_h` | one_head_filter_pi_star | 45 | 4.2251 | 2.1392 | 0.6222 | 2.0203 | 0.0178 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `sma5460_above_at_h` | one_head_filter_pi_star | 56 | 4.7685 | 2.1140 | 0.6607 | 2.0759 | 0.0141 | 0.1071 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5460_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9743 | 0.5569 | -0.2058 | -0.0008 | 0.1287 | ok | RAN |
| ETHUSDT | 8 | `sma5460_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 0.9736 | 0.5565 | -0.2140 | -0.0009 | 0.1369 | ok | RAN |
| SOLUSDT | 8 | `sma5460_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 0.9554 | 0.5317 | -0.3550 | -0.0009 | 0.1239 | ok | RAN |
| SOLUSDT | 4 | `sma5460_below_at_h` | one_head_filter_pi_star | 289 | 23.5107 | 0.9364 | 0.5225 | -0.4784 | -0.0013 | 0.1384 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma5460_above_at_h` | one_head_filter_pi_star | 27 | 8.1477 | 0.9130 | 0.4815 | -0.3773 | -0.0043 | 0.1481 | ok | RAN |
| ETHUSDT | 8 | `sma5460_above_at_h` | one_head_filter_pi_star | 39 | 11.3833 | 0.8697 | 0.5128 | -0.6642 | -0.0070 | 0.1795 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5460_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5460_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5460_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5460_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5460_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
