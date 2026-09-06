# Autonomy public-indicator hunt gen 2342

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T060523Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma543_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1885 | 0.6032 | 1.0996 | 0.0056 | 0.1905 | ok | RAN |
| ETHUSDT | 8 | `wma543_below_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 1.1337 | 0.5879 | 0.8014 | 0.0041 | 0.1868 | ok | RAN |
| SOLUSDT | 4 | `wma543_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.0728 | 0.5699 | 0.4258 | 0.0015 | 0.1559 | ok | RAN |
| SOLUSDT | 8 | `wma543_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.0457 | 0.5407 | 0.2523 | 0.0008 | 0.0988 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `wma543_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 0.9905 | 0.5556 | -0.0581 | -0.0002 | 0.1534 | ok | RAN |
| SOLUSDT | 4 | `wma543_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 0.9885 | 0.5361 | -0.0681 | -0.0002 | 0.1082 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `wma543_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8655 | 0.5410 | -0.8225 | -0.0053 | 0.0929 | ok | RAN |
| ETHUSDT | 4 | `wma543_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 0.8054 | 0.5269 | -1.2440 | -0.0081 | 0.0968 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma543_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0695 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma543_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0709 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma543_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma543_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma543_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma543_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma543_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma543_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma543_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma543_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma543_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma543_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma543_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma543_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma543_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma543_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
