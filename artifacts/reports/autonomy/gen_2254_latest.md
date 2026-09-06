# Autonomy public-indicator hunt gen 2254

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T190822Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma529_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.1389 | 0.5946 | 0.8356 | 0.0043 | 0.1838 | ok | RAN |
| ETHUSDT | 4 | `wma529_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.0763 | 0.5761 | 0.4656 | 0.0024 | 0.1957 | ok | RAN |
| SOLUSDT | 8 | `wma529_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.1055 | 0.5556 | 0.5759 | 0.0019 | 0.1111 | ok | RAN |
| SOLUSDT | 4 | `wma529_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.0142 | 0.5385 | 0.0847 | 0.0003 | 0.1026 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma529_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 0.9935 | 0.5611 | -0.0386 | -0.0001 | 0.1500 | ok | RAN |
| SOLUSDT | 8 | `wma529_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 0.9581 | 0.5455 | -0.2500 | -0.0009 | 0.1551 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma529_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 0.8617 | 0.5389 | -0.8429 | -0.0056 | 0.0889 | ok | RAN |
| ETHUSDT | 4 | `wma529_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8188 | 0.5323 | -1.1430 | -0.0077 | 0.1022 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma529_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma529_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma529_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma529_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma529_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma529_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma529_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma529_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma529_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma529_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma529_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma529_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma529_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma529_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma529_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma529_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
