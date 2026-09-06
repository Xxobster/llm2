# Autonomy public-indicator hunt gen 2446

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T191258Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma559_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1523 | 0.5924 | 0.9019 | 0.0046 | 0.1848 | ok | RAN |
| ETHUSDT | 4 | `wma559_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.1349 | 0.5889 | 0.7888 | 0.0041 | 0.1889 | ok | RAN |
| SOLUSDT | 8 | `wma559_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.1093 | 0.5508 | 0.6147 | 0.0020 | 0.0963 | ok | RAN |
| SOLUSDT | 4 | `wma559_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.0343 | 0.5489 | 0.1983 | 0.0007 | 0.0978 | ok | RAN |
| SOLUSDT | 4 | `wma559_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0262 | 0.5667 | 0.1540 | 0.0005 | 0.1500 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma559_below_at_h` | one_head_filter_pi_star | 187 | 15.2912 | 0.9619 | 0.5508 | -0.2266 | -0.0008 | 0.1551 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma559_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 0.8770 | 0.5393 | -0.7351 | -0.0048 | 0.0955 | ok | RAN |
| ETHUSDT | 4 | `wma559_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 0.8578 | 0.5450 | -0.8762 | -0.0059 | 0.1058 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma559_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma559_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma559_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma559_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma559_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma559_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma559_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma559_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma559_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma559_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma559_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma559_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma559_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma559_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma559_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma559_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
