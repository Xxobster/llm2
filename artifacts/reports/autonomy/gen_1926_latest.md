# Autonomy public-indicator hunt gen 1926

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T014851Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma478_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1474 | 0.5932 | 0.8635 | 0.0045 | 0.2034 | ok | RAN |
| ETHUSDT | 8 | `wma478_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.1016 | 0.5862 | 0.5948 | 0.0032 | 0.1954 | ok | RAN |
| SOLUSDT | 8 | `wma478_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0392 | 0.5690 | 0.2244 | 0.0008 | 0.1667 | ok | RAN |
| SOLUSDT | 8 | `wma478_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.0393 | 0.5526 | 0.2262 | 0.0007 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `wma478_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0045 | 0.5430 | 0.0262 | 0.0001 | 0.1022 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma478_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 0.9814 | 0.5515 | -0.1060 | -0.0004 | 0.1576 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma478_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 0.8324 | 0.5440 | -1.0508 | -0.0068 | 0.0934 | ok | RAN |
| ETHUSDT | 4 | `wma478_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.7928 | 0.5269 | -1.3520 | -0.0086 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma478_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0470 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma478_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma478_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma478_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma478_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma478_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
