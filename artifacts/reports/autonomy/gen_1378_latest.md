# Autonomy public-indicator hunt gen 1378

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T033627Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1232_neg_at_h` | one_head_filter_pi_star | 317 | 25.7886 | 1.7206 | 0.6562 | 4.0759 | 0.0179 | 0.3186 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1232_neg_at_h` | one_head_filter_pi_star | 329 | 26.7648 | 1.6812 | 0.6505 | 4.1442 | 0.0178 | 0.3131 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1232_neg_at_h` | one_head_filter_pi_star | 324 | 26.3580 | 1.7471 | 0.6358 | 4.0980 | 0.0118 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1232_neg_at_h` | one_head_filter_pi_star | 352 | 28.6359 | 1.6887 | 0.6307 | 4.1099 | 0.0108 | 0.3153 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret1232_pos_at_h` | one_head_filter_pi_star | 11 | 1.2419 | 1.3028 | 0.6364 | 0.4325 | 0.0052 | 0.4545 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1232_pos_at_h` | one_head_filter_pi_star | 59 | 5.5227 | 1.0685 | 0.5593 | 0.2288 | 0.0031 | 0.2373 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1232_pos_at_h` | one_head_filter_pi_star | 39 | 3.7621 | 0.8623 | 0.5128 | -0.4311 | -0.0068 | 0.2308 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1232_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0667 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1232_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3142 | 0.2222 | -1.6016 | -0.0717 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1232_pos_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1232_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1232_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1232_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1232_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
