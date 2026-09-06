# Autonomy public-indicator hunt gen 2400

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T135009Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma5600_above_at_h` | one_head_filter_pi_star | 53 | 4.9763 | 2.7977 | 0.6981 | 2.8893 | 0.0205 | 0.1509 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma5600_above_at_h` | one_head_filter_pi_star | 52 | 4.4279 | 2.3522 | 0.6731 | 2.3172 | 0.0157 | 0.1154 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma5600_below_at_h` | one_head_filter_pi_star | 304 | 24.8583 | 0.9764 | 0.5362 | -0.1758 | -0.0005 | 0.1316 | ok | RAN |
| SOLUSDT | 8 | `sma5600_below_at_h` | one_head_filter_pi_star | 298 | 24.3677 | 0.9756 | 0.5302 | -0.1839 | -0.0005 | 0.1376 | ok | RAN |
| ETHUSDT | 8 | `sma5600_below_at_h` | one_head_filter_pi_star | 334 | 27.1716 | 0.9711 | 0.5569 | -0.2375 | -0.0009 | 0.1347 | ok | RAN |
| ETHUSDT | 4 | `sma5600_below_at_h` | one_head_filter_pi_star | 333 | 27.0902 | 0.9668 | 0.5556 | -0.2720 | -0.0011 | 0.1321 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5600_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.9352 | 0.5333 | -0.2924 | -0.0030 | 0.1667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5600_above_at_h` | one_head_filter_pi_star | 34 | 10.2600 | 0.6685 | 0.4412 | -2.0121 | -0.0194 | 0.1765 | ok | RAN |
| ETHUSDT | 4 | `sma5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5600_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5600_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5600_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5600_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5600_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
