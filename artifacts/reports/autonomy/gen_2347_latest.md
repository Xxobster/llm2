# Autonomy public-indicator hunt gen 2347

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T064458Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma786_below_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.2777 | 0.6034 | 1.4783 | 0.0076 | 0.2011 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma786_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.2001 | 0.5882 | 1.1192 | 0.0058 | 0.1658 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma786_above_at_h` | one_head_filter_pi_star | 115 | 9.5585 | 1.2342 | 0.5913 | 1.0007 | 0.0040 | 0.1130 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma786_above_at_h` | one_head_filter_pi_star | 135 | 11.0707 | 1.1374 | 0.5407 | 0.6359 | 0.0025 | 0.1185 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma786_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9381 | 0.5583 | -0.3900 | -0.0013 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 8 | `sma786_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 0.9223 | 0.5366 | -0.4912 | -0.0017 | 0.1366 | ok | RAN |
| ETHUSDT | 8 | `sma786_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 0.9047 | 0.5556 | -0.5142 | -0.0038 | 0.1111 | ok | RAN |
| ETHUSDT | 4 | `sma786_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8451 | 0.5510 | -0.8011 | -0.0066 | 0.1020 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma786_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma786_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4605 | 0.2353 | -1.1826 | -0.0583 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma786_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma786_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma786_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma786_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma786_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma786_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma786_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma786_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma786_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma786_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma786_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma786_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma786_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma786_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
