# Autonomy public-indicator hunt gen 1482

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T010716Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1336_neg_at_h` | one_head_filter_pi_star | 328 | 26.6834 | 1.6458 | 0.6494 | 3.7379 | 0.0168 | 0.3110 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1336_neg_at_h` | one_head_filter_pi_star | 323 | 26.2767 | 1.6044 | 0.6440 | 3.5844 | 0.0162 | 0.3189 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1336_pos_at_h` | one_head_filter_pi_star | 21 | 2.0623 | 2.1684 | 0.7143 | 1.7279 | 0.0162 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1336_neg_at_h` | one_head_filter_pi_star | 346 | 28.1478 | 1.7360 | 0.6416 | 4.2850 | 0.0110 | 0.3121 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1336_neg_at_h` | one_head_filter_pi_star | 356 | 28.9613 | 1.6736 | 0.6348 | 4.1423 | 0.0103 | 0.3174 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1336_pos_at_h` | one_head_filter_pi_star | 30 | 2.9454 | 1.1488 | 0.5333 | 0.3306 | 0.0052 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1336_pos_at_h` | one_head_filter_pi_star | 19 | 1.8654 | 0.7780 | 0.5263 | -0.4632 | -0.0104 | 0.2632 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1336_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.6417 | 0.3125 | -0.6719 | -0.0295 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1336_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.4931 | 0.2941 | -1.0802 | -0.0522 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1336_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret1336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1336_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1336_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1336_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1336_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
