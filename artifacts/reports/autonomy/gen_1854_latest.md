# Autonomy public-indicator hunt gen 1854

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T191544Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma467_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1340 | 0.5833 | 0.7917 | 0.0041 | 0.2000 | ok | RAN |
| ETHUSDT | 4 | `wma467_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.0945 | 0.5761 | 0.5788 | 0.0030 | 0.2011 | ok | RAN |
| SOLUSDT | 4 | `wma467_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0973 | 0.5780 | 0.5353 | 0.0020 | 0.1561 | ok | RAN |
| SOLUSDT | 8 | `wma467_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0644 | 0.5484 | 0.3629 | 0.0011 | 0.1022 | ok | RAN |
| SOLUSDT | 8 | `wma467_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 1.0368 | 0.5625 | 0.2101 | 0.0008 | 0.1648 | ok | RAN |
| SOLUSDT | 4 | `wma467_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0168 | 0.5376 | 0.0973 | 0.0003 | 0.1022 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma467_above_at_h` | one_head_filter_pi_star | 179 | 14.7713 | 0.8451 | 0.5419 | -0.9568 | -0.0064 | 0.0950 | ok | RAN |
| ETHUSDT | 8 | `wma467_above_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 0.7888 | 0.5326 | -1.3724 | -0.0090 | 0.0978 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma467_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma467_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma467_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma467_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma467_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma467_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma467_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma467_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma467_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma467_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma467_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma467_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma467_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma467_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma467_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma467_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
