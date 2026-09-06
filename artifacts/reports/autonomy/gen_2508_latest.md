# Autonomy public-indicator hunt gen 2508

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260906T015912Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ema1109_above_at_h` | one_head_filter_pi_star | 106 | 8.6433 | 1.2912 | 0.6321 | 1.1051 | 0.0048 | 0.1321 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema1109_above_at_h` | one_head_filter_pi_star | 111 | 9.0510 | 1.2109 | 0.6036 | 0.8461 | 0.0036 | 0.1351 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema1109_below_at_h` | one_head_filter_pi_star | 247 | 20.1974 | 1.0186 | 0.5466 | 0.1228 | 0.0004 | 0.1296 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 376 | 30.5314 | 1.0041 | 0.5479 | 0.0341 | 0.0001 | 0.1330 | ok | RAN |
| ETHUSDT | 4 | `ema1109_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 0.9723 | 0.5443 | -0.1954 | -0.0009 | 0.1477 | ok | RAN |
| SOLUSDT | 8 | `ema1109_below_at_h` | one_head_filter_pi_star | 258 | 21.0969 | 0.9507 | 0.5349 | -0.3450 | -0.0011 | 0.1318 | ok | RAN |
| ETHUSDT | 8 | `ema1109_below_at_h` | one_head_filter_pi_star | 246 | 20.0959 | 0.9522 | 0.5447 | -0.3529 | -0.0015 | 0.1463 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 373 | 30.3443 | 0.9511 | 0.5576 | -0.4157 | -0.0017 | 0.1421 | ok | RAN |
| ETHUSDT | 4 | `ema1109_above_at_h` | one_head_filter_pi_star | 114 | 9.4082 | 0.9129 | 0.5439 | -0.3896 | -0.0038 | 0.1228 | ok | RAN |
| ETHUSDT | 8 | `ema1109_above_at_h` | one_head_filter_pi_star | 109 | 8.9956 | 0.8876 | 0.5413 | -0.5134 | -0.0048 | 0.1101 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 0.8377 | 0.3929 | -0.3856 | -0.0166 | 0.0357 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema1109_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema1109_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0526 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema1109_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema1109_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1109_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema1109_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1109_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema1109_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1109_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema1109_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1109_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema1109_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema1109_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1109_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema1109_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema1109_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
