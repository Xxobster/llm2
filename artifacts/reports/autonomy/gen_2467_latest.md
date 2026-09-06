# Autonomy public-indicator hunt gen 2467

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T213527Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma802_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1725 | 0.5926 | 0.9909 | 0.0048 | 0.1746 | ok | RAN |
| ETHUSDT | 8 | `sma802_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 1.1482 | 0.5792 | 0.8740 | 0.0044 | 0.1749 | ok | RAN |
| SOLUSDT | 8 | `sma802_above_at_h` | one_head_filter_pi_star | 123 | 10.0866 | 1.2045 | 0.5772 | 0.8773 | 0.0035 | 0.1220 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma802_above_at_h` | one_head_filter_pi_star | 135 | 11.0080 | 1.1161 | 0.5630 | 0.5471 | 0.0021 | 0.1259 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma802_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9665 | 0.5561 | -0.2067 | -0.0007 | 0.1366 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma802_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 0.9100 | 0.5419 | -0.5666 | -0.0020 | 0.1379 | ok | RAN |
| ETHUSDT | 8 | `sma802_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 0.8363 | 0.5410 | -0.9699 | -0.0070 | 0.0984 | ok | RAN |
| ETHUSDT | 4 | `sma802_above_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 0.8000 | 0.5301 | -1.1667 | -0.0087 | 0.1145 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma802_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0546 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma802_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0578 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma802_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma802_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma802_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma802_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma802_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma802_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma802_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma802_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma802_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma802_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma802_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma802_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma802_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma802_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
