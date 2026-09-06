# Autonomy public-indicator hunt gen 2459

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T204107Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma801_below_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 1.3013 | 0.6024 | 1.5303 | 0.0078 | 0.1807 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma801_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.2476 | 0.5969 | 1.3754 | 0.0070 | 0.1728 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma801_above_at_h` | one_head_filter_pi_star | 155 | 12.7108 | 1.1613 | 0.5613 | 0.7954 | 0.0029 | 0.1097 | ok | RAN |
| SOLUSDT | 4 | `sma801_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.0855 | 0.5556 | 0.3889 | 0.0015 | 0.1270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma801_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 0.9352 | 0.5502 | -0.4099 | -0.0014 | 0.1435 | ok | RAN |
| SOLUSDT | 8 | `sma801_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 0.9305 | 0.5429 | -0.4429 | -0.0015 | 0.1381 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma801_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 0.8309 | 0.5389 | -1.0015 | -0.0069 | 0.1056 | ok | RAN |
| ETHUSDT | 4 | `sma801_above_at_h` | one_head_filter_pi_star | 146 | 12.0010 | 0.8336 | 0.5548 | -0.8772 | -0.0074 | 0.1027 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma801_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0528 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma801_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma801_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma801_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma801_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma801_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma801_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma801_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma801_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma801_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma801_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma801_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma801_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma801_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma801_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma801_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
