# Autonomy public-indicator hunt gen 2435

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260905T175625Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma797_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.2244 | 0.5820 | 1.2432 | 0.0064 | 0.1799 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma797_above_at_h` | one_head_filter_pi_star | 126 | 10.3326 | 1.2398 | 0.5873 | 1.0290 | 0.0041 | 0.1270 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma797_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 1.1445 | 0.5801 | 0.8212 | 0.0040 | 0.1768 | ok | RAN |
| SOLUSDT | 4 | `sma797_above_at_h` | one_head_filter_pi_star | 150 | 12.2311 | 1.1209 | 0.5467 | 0.5881 | 0.0022 | 0.1267 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| SOLUSDT | 4 | `sma797_below_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 0.9818 | 0.5587 | -0.1140 | -0.0004 | 0.1362 | ok | RAN |
| SOLUSDT | 8 | `sma797_below_at_h` | one_head_filter_pi_star | 223 | 18.2349 | 0.9638 | 0.5516 | -0.2366 | -0.0008 | 0.1390 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 8 | `sma797_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 0.8538 | 0.5509 | -0.8187 | -0.0062 | 0.1018 | ok | RAN |
| ETHUSDT | 4 | `sma797_above_at_h` | one_head_filter_pi_star | 150 | 12.3298 | 0.8388 | 0.5467 | -0.8766 | -0.0068 | 0.1067 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma797_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4641 | 0.2632 | -1.1807 | -0.0530 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma797_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0567 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma797_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma797_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma797_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma797_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma797_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma797_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma797_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma797_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma797_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma797_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma797_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma797_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma797_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma797_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
