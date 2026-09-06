# Autonomy public-indicator hunt gen 2416

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T154156Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5640_above_at_h` | one_head_filter_pi_star | 39 | 3.6618 | 3.5232 | 0.7179 | 2.8027 | 0.0247 | 0.1026 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5640_above_at_h` | one_head_filter_pi_star | 43 | 4.0373 | 2.1072 | 0.6512 | 1.9187 | 0.0163 | 0.1395 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5640_below_at_h` | one_head_filter_pi_star | 318 | 26.0031 | 0.9793 | 0.5377 | -0.1591 | -0.0004 | 0.1258 | ok | RAN |
| SOLUSDT | 8 | `sma5640_below_at_h` | one_head_filter_pi_star | 365 | 29.6935 | 0.9689 | 0.5452 | -0.2582 | -0.0006 | 0.1315 | ok | RAN |
| ETHUSDT | 8 | `sma5640_below_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 0.9778 | 0.5572 | -0.1805 | -0.0007 | 0.1295 | ok | RAN |
| ETHUSDT | 4 | `sma5640_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9646 | 0.5556 | -0.2931 | -0.0011 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5640_above_at_h` | one_head_filter_pi_star | 31 | 9.1469 | 0.7939 | 0.4516 | -1.0403 | -0.0118 | 0.1613 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5640_above_at_h` | one_head_filter_pi_star | 37 | 11.1653 | 0.6862 | 0.4595 | -1.9564 | -0.0182 | 0.1622 | ok | RAN |
| ETHUSDT | 4 | `sma5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5640_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5640_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5640_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5640_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5640_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
