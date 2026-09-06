# Autonomy public-indicator hunt gen 2030

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260903T124155Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma494_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1924 | 0.5979 | 1.1244 | 0.0057 | 0.1852 | ok | RAN |
| ETHUSDT | 4 | `wma494_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.1114 | 0.5895 | 0.6935 | 0.0035 | 0.1947 | ok | RAN |
| SOLUSDT | 8 | `wma494_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.0704 | 0.5519 | 0.3966 | 0.0013 | 0.0984 | ok | RAN |
| SOLUSDT | 4 | `wma494_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.0318 | 0.5640 | 0.1752 | 0.0007 | 0.1628 | ok | RAN |
| SOLUSDT | 8 | `wma494_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.0134 | 0.5611 | 0.0790 | 0.0003 | 0.1611 | ok | RAN |
| SOLUSDT | 4 | `wma494_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.0054 | 0.5389 | 0.0320 | 0.0001 | 0.1036 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma494_above_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 0.8199 | 0.5341 | -1.0891 | -0.0074 | 0.0852 | ok | RAN |
| ETHUSDT | 4 | `wma494_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 0.8159 | 0.5272 | -1.1678 | -0.0075 | 0.0924 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma494_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5128 | 0.2778 | -1.0553 | -0.0479 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma494_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma494_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma494_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma494_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma494_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma494_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma494_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma494_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma494_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma494_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma494_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma494_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma494_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma494_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma494_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
