# Autonomy public-indicator hunt gen 2464

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T211502Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma5760_above_at_h` | one_head_filter_pi_star | 41 | 3.8496 | 2.3832 | 0.6585 | 2.1321 | 0.0168 | 0.1220 | TPM<MIN | RAN |
| SOLUSDT | 8 | `sma5760_above_at_h` | one_head_filter_pi_star | 47 | 4.4129 | 2.1697 | 0.6809 | 2.1215 | 0.0161 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `sma5760_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9883 | 0.5579 | -0.0933 | -0.0004 | 0.1365 | ok | RAN |
| SOLUSDT | 8 | `sma5760_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 0.9411 | 0.5337 | -0.4818 | -0.0012 | 0.1261 | ok | RAN |
| SOLUSDT | 4 | `sma5760_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 0.9411 | 0.5275 | -0.4587 | -0.0012 | 0.1359 | ok | RAN |
| ETHUSDT | 8 | `sma5760_below_at_h` | one_head_filter_pi_star | 342 | 27.8224 | 0.9582 | 0.5556 | -0.3447 | -0.0014 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma5760_above_at_h` | one_head_filter_pi_star | 30 | 9.0530 | 0.7565 | 0.4667 | -1.2007 | -0.0124 | 0.1333 | ok | RAN |
| ETHUSDT | 4 | `sma5760_above_at_h` | one_head_filter_pi_star | 39 | 11.5074 | 0.7539 | 0.4872 | -1.4092 | -0.0138 | 0.1795 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5760_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5760_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5760_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5760_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma5760_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
