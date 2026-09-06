# Autonomy public-indicator hunt gen 1886

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T220904Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma472_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 1.1585 | 0.5924 | 0.9174 | 0.0048 | 0.1902 | ok | RAN |
| ETHUSDT | 4 | `wma472_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.1311 | 0.5806 | 0.7898 | 0.0041 | 0.1935 | ok | RAN |
| SOLUSDT | 4 | `wma472_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.0879 | 0.5805 | 0.4852 | 0.0018 | 0.1552 | ok | RAN |
| SOLUSDT | 8 | `wma472_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 1.0347 | 0.5706 | 0.1945 | 0.0007 | 0.1588 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma472_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 0.9996 | 0.5323 | -0.0023 | -0.0000 | 0.0968 | ok | RAN |
| SOLUSDT | 4 | `wma472_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 0.9888 | 0.5368 | -0.0653 | -0.0002 | 0.1053 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma472_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8150 | 0.5323 | -1.1553 | -0.0076 | 0.0914 | ok | RAN |
| ETHUSDT | 4 | `wma472_above_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 0.8001 | 0.5301 | -1.2806 | -0.0084 | 0.0929 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma472_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma472_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma472_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma472_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma472_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma472_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
