# Autonomy public-indicator hunt gen 834

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T185345Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret688_neg_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.1529 | 0.6946 | 4.1515 | 0.0232 | 0.3832 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret688_neg_at_h` | one_head_filter_pi_star | 174 | 14.2142 | 1.8559 | 0.6724 | 3.6337 | 0.0195 | 0.3678 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret688_neg_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 1.9938 | 0.6776 | 3.9958 | 0.0154 | 0.3364 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret688_neg_at_h` | one_head_filter_pi_star | 213 | 17.4172 | 1.8488 | 0.6573 | 3.7256 | 0.0137 | 0.3239 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret688_pos_at_h` | one_head_filter_pi_star | 143 | 11.7544 | 1.2719 | 0.6014 | 1.1859 | 0.0106 | 0.2448 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret688_pos_at_h` | one_head_filter_pi_star | 125 | 10.2512 | 1.6879 | 0.6320 | 2.4570 | 0.0098 | 0.2800 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret688_pos_at_h` | one_head_filter_pi_star | 124 | 10.1686 | 1.6505 | 0.6371 | 2.3705 | 0.0093 | 0.2661 | ok | RAN |
| ETHUSDT | 4 | `ret688_pos_at_h` | one_head_filter_pi_star | 174 | 14.3026 | 1.1853 | 0.5862 | 0.9599 | 0.0074 | 0.2471 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret688_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.5092 | 0.2857 | -0.9832 | -0.0532 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret688_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4567 | 0.2778 | -1.2119 | -0.0589 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret688_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret688_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret688_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret688_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
