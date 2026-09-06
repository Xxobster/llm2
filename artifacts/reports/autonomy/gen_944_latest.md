# Autonomy public-indicator hunt gen 944

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T061824Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `sma1960_above_at_h` | one_head_filter_pi_star | 47 | 3.9070 | 2.1689 | 0.7234 | 2.4438 | 0.0153 | 0.3404 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma1960_below_at_h` | one_head_filter_pi_star | 331 | 26.9275 | 1.5640 | 0.6405 | 3.4224 | 0.0152 | 0.3112 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma1960_below_at_h` | one_head_filter_pi_star | 341 | 27.7410 | 1.5423 | 0.6364 | 3.3945 | 0.0149 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1960_below_at_h` | one_head_filter_pi_star | 292 | 23.7548 | 1.9059 | 0.6507 | 4.4730 | 0.0132 | 0.3219 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1960_below_at_h` | one_head_filter_pi_star | 302 | 24.5683 | 1.8249 | 0.6424 | 4.2192 | 0.0122 | 0.3212 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1960_above_at_h` | one_head_filter_pi_star | 71 | 5.9020 | 1.6511 | 0.6761 | 1.7975 | 0.0101 | 0.3099 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma1960_above_at_h` | one_head_filter_pi_star | 36 | 3.3112 | 1.1554 | 0.5556 | 0.3863 | 0.0068 | 0.3056 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1960_above_at_h` | one_head_filter_pi_star | 47 | 4.2516 | 1.0705 | 0.5532 | 0.1965 | 0.0031 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1960_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0538 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1960_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1960_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1960_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1960_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
