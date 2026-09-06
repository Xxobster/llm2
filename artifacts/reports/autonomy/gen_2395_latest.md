# Autonomy public-indicator hunt gen 2395

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T131454Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma792_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2805 | 0.6069 | 1.5104 | 0.0077 | 0.1734 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma792_below_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.2119 | 0.5780 | 1.1679 | 0.0059 | 0.1734 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma792_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.1076 | 0.5612 | 0.5148 | 0.0020 | 0.1223 | ok | RAN |
| SOLUSDT | 8 | `sma792_above_at_h` | one_head_filter_pi_star | 136 | 11.1527 | 1.0717 | 0.5368 | 0.3455 | 0.0013 | 0.1250 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| SOLUSDT | 4 | `sma792_below_at_h` | one_head_filter_pi_star | 212 | 17.3354 | 0.9045 | 0.5377 | -0.6202 | -0.0021 | 0.1321 | ok | RAN |
| SOLUSDT | 8 | `sma792_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 0.8977 | 0.5459 | -0.6391 | -0.0023 | 0.1429 | ok | RAN |
| ETHUSDT | 4 | `sma792_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 0.8749 | 0.5510 | -0.6383 | -0.0052 | 0.0952 | ok | RAN |
| ETHUSDT | 8 | `sma792_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 0.8530 | 0.5435 | -0.7648 | -0.0064 | 0.1159 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma792_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma792_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0540 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma792_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma792_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma792_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma792_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma792_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma792_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma792_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma792_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma792_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma792_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma792_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma792_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma792_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma792_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
