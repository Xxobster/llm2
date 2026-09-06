# Autonomy public-indicator hunt gen 840

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T192621Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `sma1700_below_at_h` | one_head_filter_pi_star | 9 | 1.2601 | 2.9118 | 0.6667 | 1.7154 | 0.1146 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 4 | `sma1700_above_at_h` | one_head_filter_pi_star | 49 | 4.0470 | 2.3678 | 0.7551 | 2.5901 | 0.0167 | 0.3061 | ok | RAN |
| ETHUSDT | 4 | `sma1700_below_at_h` | one_head_filter_pi_star | 298 | 24.3439 | 1.6334 | 0.6477 | 3.6405 | 0.0160 | 0.3188 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1700_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6027 | 0.6453 | 3.5346 | 0.0155 | 0.3243 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1700_above_at_h` | one_head_filter_pi_star | 61 | 5.0708 | 2.0786 | 0.7049 | 2.4625 | 0.0142 | 0.2951 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1700_below_at_h` | one_head_filter_pi_star | 311 | 25.3005 | 1.8193 | 0.6399 | 4.2930 | 0.0119 | 0.3215 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1700_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.7552 | 0.6408 | 4.0266 | 0.0111 | 0.3139 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1700_above_at_h` | one_head_filter_pi_star | 66 | 5.6161 | 1.1545 | 0.5758 | 0.5064 | 0.0065 | 0.2424 | ok | RAN |
| ETHUSDT | 4 | `sma1700_above_at_h` | one_head_filter_pi_star | 72 | 5.9420 | 1.0562 | 0.5694 | 0.2048 | 0.0027 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1700_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4748 | 0.2667 | -1.1188 | -0.0585 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1700_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3356 | 0.2308 | -1.4359 | -0.0752 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1700_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1700_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1700_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
