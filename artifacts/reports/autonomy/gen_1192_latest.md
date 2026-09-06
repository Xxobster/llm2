# Autonomy public-indicator hunt gen 1192

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T093203Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 4 | `sma2580_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1286 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2580_below_at_h` | one_head_filter_pi_star | 338 | 27.4970 | 1.5819 | 0.6420 | 3.5397 | 0.0155 | 0.3077 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2580_below_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.5124 | 0.6310 | 3.2244 | 0.0140 | 0.3095 | ok | RAN |
| SOLUSDT | 4 | `sma2580_below_at_h` | one_head_filter_pi_star | 294 | 23.9175 | 1.8688 | 0.6599 | 4.3735 | 0.0132 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2580_above_at_h` | one_head_filter_pi_star | 50 | 4.5988 | 1.3110 | 0.5600 | 0.8390 | 0.0125 | 0.2800 | ok | RAN |
| SOLUSDT | 8 | `sma2580_below_at_h` | one_head_filter_pi_star | 304 | 24.7310 | 1.7119 | 0.6414 | 3.8717 | 0.0112 | 0.3289 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2580_above_at_h` | one_head_filter_pi_star | 64 | 5.3201 | 1.7551 | 0.6406 | 1.8057 | 0.0106 | 0.2188 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma2580_above_at_h` | one_head_filter_pi_star | 66 | 5.4256 | 1.6566 | 0.6515 | 1.5904 | 0.0084 | 0.1970 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma2580_above_at_h` | one_head_filter_pi_star | 38 | 3.6656 | 1.0145 | 0.5263 | 0.0406 | 0.0006 | 0.2368 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2580_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2580_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2580_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2580_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2580_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
