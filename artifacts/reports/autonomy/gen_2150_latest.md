# Autonomy public-indicator hunt gen 2150

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T050357Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma513_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1796 | 0.5979 | 1.0539 | 0.0053 | 0.1905 | ok | RAN |
| ETHUSDT | 8 | `wma513_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.0938 | 0.5812 | 0.5855 | 0.0030 | 0.1780 | ok | RAN |
| SOLUSDT | 8 | `wma513_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.1347 | 0.5618 | 0.7086 | 0.0024 | 0.1011 | ok | RAN |
| SOLUSDT | 4 | `wma513_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0949 | 0.5805 | 0.5273 | 0.0019 | 0.1552 | ok | RAN |
| SOLUSDT | 4 | `wma513_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.0358 | 0.5351 | 0.2066 | 0.0007 | 0.1027 | ok | RAN |
| SOLUSDT | 8 | `wma513_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.0094 | 0.5538 | 0.0565 | 0.0002 | 0.1613 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `wma513_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8011 | 0.5215 | -1.2721 | -0.0084 | 0.0968 | ok | RAN |
| ETHUSDT | 8 | `wma513_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.7994 | 0.5301 | -1.3076 | -0.0084 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma513_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma513_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma513_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma513_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma513_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma513_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma513_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma513_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma513_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma513_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma513_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma513_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma513_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma513_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma513_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma513_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
