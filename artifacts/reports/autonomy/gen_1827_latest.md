# Autonomy public-indicator hunt gen 1827

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260902T165043Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma717_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.2266 | 0.5784 | 1.2621 | 0.0067 | 0.1784 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma717_below_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 1.1390 | 0.5697 | 0.7912 | 0.0040 | 0.1879 | ok | RAN |
| SOLUSDT | 4 | `sma717_above_at_h` | one_head_filter_pi_star | 118 | 9.6766 | 1.1571 | 0.5678 | 0.6669 | 0.0028 | 0.1271 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma717_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 0.9681 | 0.5159 | -0.1547 | -0.0006 | 0.1349 | ok | RAN |
| SOLUSDT | 4 | `sma717_below_at_h` | one_head_filter_pi_star | 201 | 16.3517 | 0.9419 | 0.5572 | -0.3616 | -0.0012 | 0.1343 | ok | RAN |
| SOLUSDT | 8 | `sma717_below_at_h` | one_head_filter_pi_star | 205 | 16.6772 | 0.9376 | 0.5561 | -0.3910 | -0.0013 | 0.1317 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma717_above_at_h` | one_head_filter_pi_star | 155 | 12.7408 | 0.9135 | 0.5677 | -0.4676 | -0.0035 | 0.1097 | ok | RAN |
| ETHUSDT | 4 | `sma717_above_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 0.8665 | 0.5517 | -0.7671 | -0.0056 | 0.1092 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma717_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma717_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4111 | 0.2632 | -1.4070 | -0.0682 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma717_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma717_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma717_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma717_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma717_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma717_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma717_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma717_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma717_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma717_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma717_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma717_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma717_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma717_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
