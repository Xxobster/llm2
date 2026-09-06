# Autonomy public-indicator hunt gen 1162

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T062805Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1016_neg_at_h` | one_head_filter_pi_star | 293 | 23.8361 | 1.8179 | 0.6587 | 4.4860 | 0.0195 | 0.3345 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1016_neg_at_h` | one_head_filter_pi_star | 287 | 23.4453 | 1.7437 | 0.6551 | 4.2029 | 0.0184 | 0.3345 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1016_neg_at_h` | one_head_filter_pi_star | 279 | 22.8141 | 1.8747 | 0.6595 | 4.3181 | 0.0132 | 0.3405 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1016_neg_at_h` | one_head_filter_pi_star | 255 | 20.8516 | 1.8291 | 0.6510 | 3.8300 | 0.0128 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1016_pos_at_h` | one_head_filter_pi_star | 80 | 6.5232 | 1.8369 | 0.6750 | 2.3725 | 0.0120 | 0.2375 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1016_pos_at_h` | one_head_filter_pi_star | 80 | 6.5757 | 1.5076 | 0.6375 | 1.5474 | 0.0077 | 0.2625 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1016_pos_at_h` | one_head_filter_pi_star | 49 | 4.3091 | 0.9978 | 0.5510 | -0.0067 | -0.0001 | 0.2449 | ok | RAN |
| ETHUSDT | 4 | `ret1016_pos_at_h` | one_head_filter_pi_star | 64 | 5.4788 | 0.9696 | 0.5781 | -0.1114 | -0.0016 | 0.2344 | ok | RAN |
| BTCUSDT | 4 | `ret1016_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.4083 | 0.2667 | -1.2405 | -0.0515 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1016_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.1399 | 0.2143 | -2.1808 | -0.0764 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1016_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1016_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1016_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1016_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1016_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1016_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1016_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1016_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1016_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1016_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1016_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1016_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1016_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1016_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
