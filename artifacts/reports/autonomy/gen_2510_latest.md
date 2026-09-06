# Autonomy public-indicator hunt gen 2510

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T021211Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma569_below_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 1.1613 | 0.5909 | 0.9275 | 0.0049 | 0.1989 | ok | RAN |
| ETHUSDT | 8 | `wma569_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1415 | 0.5924 | 0.8405 | 0.0044 | 0.1848 | ok | RAN |
| SOLUSDT | 4 | `wma569_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0711 | 0.5500 | 0.3924 | 0.0013 | 0.1000 | ok | RAN |
| SOLUSDT | 4 | `wma569_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.0139 | 0.5538 | 0.0834 | 0.0003 | 0.1559 | ok | RAN |
| SOLUSDT | 8 | `wma569_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.0131 | 0.5333 | 0.0754 | 0.0002 | 0.1056 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma569_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 0.9998 | 0.5580 | -0.0014 | -0.0000 | 0.1547 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma569_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 0.8821 | 0.5580 | -0.7238 | -0.0046 | 0.0994 | ok | RAN |
| ETHUSDT | 4 | `wma569_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 0.8519 | 0.5355 | -0.9203 | -0.0062 | 0.0984 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma569_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma569_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma569_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma569_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma569_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma569_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma569_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma569_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma569_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma569_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma569_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma569_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma569_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma569_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma569_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma569_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
