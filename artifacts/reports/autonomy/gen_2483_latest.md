# Autonomy public-indicator hunt gen 2483

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T232058Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma804_below_at_h` | one_head_filter_pi_star | 162 | 13.2339 | 1.2224 | 0.5864 | 1.1562 | 0.0063 | 0.1790 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma804_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.1609 | 0.5876 | 0.9248 | 0.0046 | 0.1921 | ok | RAN |
| SOLUSDT | 8 | `sma804_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.1376 | 0.5547 | 0.6353 | 0.0024 | 0.1168 | ok | RAN |
| SOLUSDT | 4 | `sma804_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.0338 | 0.5481 | 0.1652 | 0.0006 | 0.1185 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma804_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9424 | 0.5502 | -0.3662 | -0.0012 | 0.1435 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma804_below_at_h` | one_head_filter_pi_star | 215 | 17.5807 | 0.9011 | 0.5488 | -0.6374 | -0.0022 | 0.1349 | ok | RAN |
| ETHUSDT | 4 | `sma804_above_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 0.9006 | 0.5529 | -0.5434 | -0.0041 | 0.0941 | ok | RAN |
| ETHUSDT | 8 | `sma804_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 0.8431 | 0.5429 | -0.9139 | -0.0067 | 0.1086 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma804_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma804_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma804_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma804_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma804_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma804_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma804_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma804_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma804_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma804_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma804_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma804_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma804_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma804_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma804_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma804_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
