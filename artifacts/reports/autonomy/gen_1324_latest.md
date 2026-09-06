# Autonomy public-indicator hunt gen 1324

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T223501Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema947_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.8660 | 0.6624 | 4.1322 | 0.0201 | 0.3460 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ema947_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8261 | 0.6682 | 3.8735 | 0.0195 | 0.3682 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema947_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.8019 | 0.6478 | 3.8398 | 0.0122 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema947_below_at_h` | one_head_filter_pi_star | 257 | 21.0151 | 1.7481 | 0.6459 | 3.7590 | 0.0119 | 0.3035 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema947_above_at_h` | one_head_filter_pi_star | 129 | 10.6027 | 1.6221 | 0.6357 | 2.2648 | 0.0093 | 0.3256 | ok | RAN |
| SOLUSDT | 8 | `ema947_above_at_h` | one_head_filter_pi_star | 125 | 10.1925 | 1.6225 | 0.6320 | 2.2702 | 0.0092 | 0.3040 | ok | RAN |
| ETHUSDT | 4 | `ema947_above_at_h` | one_head_filter_pi_star | 126 | 10.3570 | 1.2354 | 0.6032 | 1.0061 | 0.0088 | 0.2302 | ok | RAN |
| ETHUSDT | 8 | `ema947_above_at_h` | one_head_filter_pi_star | 118 | 9.7383 | 1.2188 | 0.5932 | 0.9430 | 0.0084 | 0.2373 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema947_above_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.6498 | 0.3529 | -0.6566 | -0.0300 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema947_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema947_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema947_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema947_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema947_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema947_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema947_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema947_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema947_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema947_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema947_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema947_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema947_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema947_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema947_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
