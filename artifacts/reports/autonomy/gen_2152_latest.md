# Autonomy public-indicator hunt gen 2152

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260904T052051Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma4980_above_at_h` | one_head_filter_pi_star | 47 | 4.3466 | 2.0091 | 0.5957 | 1.8162 | 0.0124 | 0.1064 | ok | RAN |
| SOLUSDT | 4 | `sma4980_above_at_h` | one_head_filter_pi_star | 53 | 4.4515 | 1.6764 | 0.5849 | 1.3592 | 0.0090 | 0.0755 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 8 | `sma4980_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.0000 | 0.5595 | 0.0005 | 0.0000 | 0.1339 | ok | RAN |
| ETHUSDT | 4 | `sma4980_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 0.9941 | 0.5579 | -0.0477 | -0.0002 | 0.1306 | ok | RAN |
| SOLUSDT | 8 | `sma4980_below_at_h` | one_head_filter_pi_star | 289 | 23.5107 | 0.9898 | 0.5398 | -0.0728 | -0.0002 | 0.1384 | ok | RAN |
| SOLUSDT | 4 | `sma4980_below_at_h` | one_head_filter_pi_star | 290 | 23.5921 | 0.9611 | 0.5345 | -0.2866 | -0.0008 | 0.1345 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `sma4980_above_at_h` | one_head_filter_pi_star | 38 | 11.2124 | 0.8595 | 0.5263 | -0.8283 | -0.0076 | 0.1579 | ok | RAN |
| ETHUSDT | 8 | `sma4980_above_at_h` | one_head_filter_pi_star | 34 | 10.0321 | 0.8284 | 0.5000 | -0.8305 | -0.0093 | 0.1765 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4980_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4980_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4980_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4980_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma4980_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
