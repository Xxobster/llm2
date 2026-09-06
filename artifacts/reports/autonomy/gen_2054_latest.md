# Autonomy public-indicator hunt gen 2054

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T154549Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma498_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1830 | 0.6045 | 1.0299 | 0.0053 | 0.1921 | ok | RAN |
| ETHUSDT | 4 | `wma498_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 1.1208 | 0.5899 | 0.7064 | 0.0037 | 0.2022 | ok | RAN |
| SOLUSDT | 4 | `wma498_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 1.0324 | 0.5600 | 0.1874 | 0.0007 | 0.1600 | ok | RAN |
| SOLUSDT | 4 | `wma498_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.0351 | 0.5469 | 0.2029 | 0.0006 | 0.0990 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma498_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0034 | 0.5421 | 0.0198 | 0.0001 | 0.1000 | ok | RAN |
| SOLUSDT | 8 | `wma498_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 0.9730 | 0.5440 | -0.1637 | -0.0006 | 0.1648 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma498_above_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 0.8716 | 0.5449 | -0.7765 | -0.0051 | 0.0899 | ok | RAN |
| ETHUSDT | 4 | `wma498_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 0.8299 | 0.5323 | -1.0716 | -0.0071 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma498_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma498_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma498_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma498_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma498_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma498_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma498_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma498_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma498_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma498_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma498_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma498_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma498_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma498_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma498_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma498_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
