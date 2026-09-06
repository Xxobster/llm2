# Autonomy public-indicator hunt gen 1056

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T172416Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma2240_above_at_h` | one_head_filter_pi_star | 55 | 4.9752 | 1.7731 | 0.6545 | 1.8248 | 0.0253 | 0.2727 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma2240_above_at_h` | one_head_filter_pi_star | 48 | 4.1668 | 1.7718 | 0.6667 | 1.6488 | 0.0244 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma2240_below_at_h` | one_head_filter_pi_star | 337 | 27.4156 | 1.5697 | 0.6409 | 3.5042 | 0.0152 | 0.3056 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma2240_below_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.5544 | 0.6382 | 3.4874 | 0.0150 | 0.3059 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2240_above_at_h` | one_head_filter_pi_star | 72 | 5.9851 | 1.9752 | 0.6944 | 2.3996 | 0.0136 | 0.3056 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2240_above_at_h` | one_head_filter_pi_star | 62 | 5.1539 | 1.7979 | 0.6452 | 1.9136 | 0.0121 | 0.3065 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma2240_below_at_h` | one_head_filter_pi_star | 297 | 24.1615 | 1.8382 | 0.6465 | 4.2743 | 0.0120 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma2240_below_at_h` | one_head_filter_pi_star | 307 | 24.9751 | 1.7528 | 0.6450 | 3.9715 | 0.0112 | 0.3225 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2240_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2240_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma2240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma2240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
