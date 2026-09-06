# Autonomy public-indicator hunt gen 1582

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260901T160442Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma424_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1471 | 0.5914 | 0.8853 | 0.0045 | 0.1989 | ok | RAN |
| ETHUSDT | 8 | `wma424_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1424 | 0.5873 | 0.8548 | 0.0044 | 0.1958 | ok | RAN |
| SOLUSDT | 8 | `wma424_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0812 | 0.5723 | 0.4488 | 0.0017 | 0.1561 | ok | RAN |
| SOLUSDT | 4 | `wma424_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 1.0495 | 0.5665 | 0.2779 | 0.0010 | 0.1561 | ok | RAN |
| SOLUSDT | 8 | `wma424_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0423 | 0.5500 | 0.2383 | 0.0007 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `wma424_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 0.9521 | 0.5285 | -0.2904 | -0.0009 | 0.1088 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma424_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 0.8412 | 0.5297 | -0.9928 | -0.0064 | 0.0973 | ok | RAN |
| ETHUSDT | 8 | `wma424_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8037 | 0.5344 | -1.2741 | -0.0081 | 0.0899 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma424_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma424_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4116 | 0.2778 | -1.4041 | -0.0735 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma424_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma424_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
