# Autonomy public-indicator hunt gen 1723

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T071549Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma704_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.3011 | 0.6084 | 1.5947 | 0.0080 | 0.1988 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma704_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1460 | 0.5739 | 0.8622 | 0.0045 | 0.1818 | ok | RAN |
| SOLUSDT | 8 | `sma704_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.1031 | 0.5591 | 0.4732 | 0.0020 | 0.1339 | ok | RAN |
| SOLUSDT | 4 | `sma704_above_at_h` | one_head_filter_pi_star | 127 | 10.4146 | 1.0349 | 0.5433 | 0.1638 | 0.0007 | 0.1181 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma704_below_at_h` | one_head_filter_pi_star | 196 | 15.9450 | 0.9646 | 0.5612 | -0.2176 | -0.0007 | 0.1378 | ok | RAN |
| ETHUSDT | 8 | `sma704_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 0.9725 | 0.5823 | -0.1489 | -0.0011 | 0.1076 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma704_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 0.9063 | 0.5521 | -0.5824 | -0.0021 | 0.1458 | ok | RAN |
| ETHUSDT | 4 | `sma704_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8395 | 0.5400 | -0.8842 | -0.0067 | 0.1067 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma704_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.4092 | 0.2500 | -1.4181 | -0.0663 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma704_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma704_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma704_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma704_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma704_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma704_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma704_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma704_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma704_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma704_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma704_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma704_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma704_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma704_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma704_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
