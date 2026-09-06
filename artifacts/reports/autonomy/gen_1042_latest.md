# Autonomy public-indicator hunt gen 1042

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T154054Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret896_neg_at_h` | one_head_filter_pi_star | 258 | 21.0762 | 1.7313 | 0.6550 | 3.9376 | 0.0179 | 0.3333 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret896_neg_at_h` | one_head_filter_pi_star | 264 | 21.5664 | 1.7024 | 0.6515 | 3.8243 | 0.0174 | 0.3258 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret896_neg_at_h` | one_head_filter_pi_star | 201 | 16.5447 | 2.0289 | 0.6617 | 3.9505 | 0.0156 | 0.3433 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret896_neg_at_h` | one_head_filter_pi_star | 260 | 21.1515 | 1.8375 | 0.6462 | 3.9259 | 0.0128 | 0.3269 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret896_pos_at_h` | one_head_filter_pi_star | 84 | 6.9324 | 1.2230 | 0.6190 | 0.8116 | 0.0100 | 0.2262 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret896_pos_at_h` | one_head_filter_pi_star | 87 | 7.1396 | 1.6624 | 0.6437 | 2.0213 | 0.0089 | 0.2299 | ok | RAN |
| SOLUSDT | 8 | `ret896_pos_at_h` | one_head_filter_pi_star | 73 | 6.0281 | 1.3970 | 0.6438 | 1.2557 | 0.0064 | 0.2603 | ok | RAN |
| ETHUSDT | 8 | `ret896_pos_at_h` | one_head_filter_pi_star | 77 | 6.5521 | 1.1320 | 0.6104 | 0.4960 | 0.0063 | 0.2338 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret896_pos_at_h` | one_head_filter_pi_star | 10 | 0.8510 | 0.5687 | 0.3000 | -0.6719 | -0.0447 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret896_pos_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4406 | 0.2857 | -1.1310 | -0.0574 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret896_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret896_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret896_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret896_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret896_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret896_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret896_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret896_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret896_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret896_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret896_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret896_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret896_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret896_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
