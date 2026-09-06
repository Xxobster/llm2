# Autonomy public-indicator hunt gen 832

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T184123Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma1680_below_at_h` | one_head_filter_pi_star | 278 | 22.7101 | 1.7138 | 0.6475 | 3.8651 | 0.0175 | 0.3165 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1680_below_at_h` | one_head_filter_pi_star | 296 | 24.1805 | 1.6011 | 0.6453 | 3.5631 | 0.0155 | 0.3277 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1680_above_at_h` | one_head_filter_pi_star | 61 | 5.3021 | 2.2194 | 0.7213 | 2.5232 | 0.0149 | 0.3279 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1680_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.7483 | 0.6325 | 3.9667 | 0.0112 | 0.3113 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1680_below_at_h` | one_head_filter_pi_star | 309 | 25.1378 | 1.6999 | 0.6343 | 3.8479 | 0.0106 | 0.3107 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1680_above_at_h` | one_head_filter_pi_star | 59 | 4.9045 | 1.6009 | 0.6780 | 1.6339 | 0.0096 | 0.3220 | ok | RAN |
| ETHUSDT | 4 | `sma1680_above_at_h` | one_head_filter_pi_star | 54 | 4.7488 | 1.1707 | 0.5741 | 0.5250 | 0.0074 | 0.2593 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma1680_above_at_h` | one_head_filter_pi_star | 63 | 5.3608 | 0.9084 | 0.5397 | -0.3321 | -0.0042 | 0.2063 | ok | RAN |
| BTCUSDT | 8 | `sma1680_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3190 | 0.2000 | -1.5401 | -0.0744 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1680_above_at_h` | one_head_filter_pi_star | 13 | 1.1063 | 0.3426 | 0.2308 | -1.3975 | -0.0762 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1680_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1680_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1680_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
