# Autonomy public-indicator hunt gen 2355

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T074443Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma787_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 1.2715 | 0.5989 | 1.4478 | 0.0074 | 0.1977 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma787_above_at_h` | one_head_filter_pi_star | 134 | 10.9887 | 1.2740 | 0.5821 | 1.2175 | 0.0047 | 0.1269 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma787_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.1417 | 0.5820 | 0.8251 | 0.0042 | 0.1746 | ok | RAN |
| SOLUSDT | 4 | `sma787_above_at_h` | one_head_filter_pi_star | 141 | 11.5627 | 1.1366 | 0.5603 | 0.6449 | 0.0025 | 0.1206 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 8 | `sma787_below_at_h` | one_head_filter_pi_star | 201 | 16.4359 | 0.9434 | 0.5522 | -0.3520 | -0.0012 | 0.1343 | ok | RAN |
| SOLUSDT | 4 | `sma787_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 0.9260 | 0.5485 | -0.4706 | -0.0016 | 0.1311 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma787_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 0.9057 | 0.5682 | -0.5283 | -0.0037 | 0.1023 | ok | RAN |
| ETHUSDT | 4 | `sma787_above_at_h` | one_head_filter_pi_star | 132 | 10.8502 | 0.8358 | 0.5455 | -0.8298 | -0.0073 | 0.0985 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma787_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma787_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma787_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma787_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma787_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma787_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma787_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma787_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma787_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma787_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma787_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma787_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma787_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma787_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma787_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma787_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
