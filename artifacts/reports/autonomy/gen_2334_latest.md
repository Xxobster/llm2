# Autonomy public-indicator hunt gen 2334

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T045329Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma542_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.1746 | 0.5957 | 1.0153 | 0.0052 | 0.1862 | ok | RAN |
| ETHUSDT | 8 | `wma542_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.1316 | 0.5922 | 0.7821 | 0.0041 | 0.1899 | ok | RAN |
| SOLUSDT | 4 | `wma542_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0790 | 0.5722 | 0.4548 | 0.0016 | 0.1611 | ok | RAN |
| SOLUSDT | 8 | `wma542_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.0725 | 0.5484 | 0.4024 | 0.0013 | 0.0968 | ok | RAN |
| SOLUSDT | 8 | `wma542_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.0290 | 0.5622 | 0.1711 | 0.0006 | 0.1568 | ok | RAN |
| SOLUSDT | 4 | `wma542_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.0069 | 0.5401 | 0.0408 | 0.0001 | 0.1016 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma542_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 0.8379 | 0.5401 | -1.0280 | -0.0064 | 0.0909 | ok | RAN |
| ETHUSDT | 4 | `wma542_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 0.8211 | 0.5272 | -1.1440 | -0.0076 | 0.0924 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma542_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma542_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma542_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma542_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma542_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma542_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma542_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma542_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma542_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma542_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma542_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma542_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma542_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma542_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma542_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma542_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
