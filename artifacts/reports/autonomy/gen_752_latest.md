# Autonomy public-indicator hunt gen 752

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T105656Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1480_below_at_h` | one_head_filter_pi_star | 278 | 22.7101 | 1.7718 | 0.6583 | 4.0911 | 0.0188 | 0.3273 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1480_below_at_h` | one_head_filter_pi_star | 262 | 21.4030 | 1.7434 | 0.6489 | 3.9165 | 0.0181 | 0.3282 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `sma1480_above_at_h` | one_head_filter_pi_star | 85 | 7.2329 | 1.3803 | 0.6235 | 1.2657 | 0.0142 | 0.2471 | ok | RAN |
| SOLUSDT | 8 | `sma1480_below_at_h` | one_head_filter_pi_star | 300 | 24.4056 | 1.7069 | 0.6333 | 3.8377 | 0.0108 | 0.3167 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1480_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.6980 | 0.6258 | 3.8040 | 0.0107 | 0.3212 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma1480_above_at_h` | one_head_filter_pi_star | 88 | 7.2625 | 1.2492 | 0.5909 | 0.9000 | 0.0100 | 0.2159 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1480_above_at_h` | one_head_filter_pi_star | 68 | 5.6526 | 1.6447 | 0.6765 | 1.6989 | 0.0093 | 0.3088 | ok | RAN |
| SOLUSDT | 8 | `sma1480_above_at_h` | one_head_filter_pi_star | 62 | 5.1539 | 1.4765 | 0.6613 | 1.3304 | 0.0073 | 0.3065 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1480_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0555 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1480_above_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4612 | 0.2500 | -1.1796 | -0.0582 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1480_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1480_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1480_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
