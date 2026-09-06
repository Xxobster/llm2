# Autonomy public-indicator hunt gen 1234

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T133121Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1088_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.8770 | 0.6736 | 3.5473 | 0.0211 | 0.3834 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1088_neg_at_h` | one_head_filter_pi_star | 299 | 24.3242 | 1.6542 | 0.6555 | 3.7727 | 0.0164 | 0.3211 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1088_pos_at_h` | one_head_filter_pi_star | 23 | 2.1303 | 1.8936 | 0.7391 | 1.4953 | 0.0115 | 0.3478 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret1088_neg_at_h` | one_head_filter_pi_star | 291 | 23.6734 | 1.7287 | 0.6289 | 3.7904 | 0.0114 | 0.3162 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1088_neg_at_h` | one_head_filter_pi_star | 283 | 23.1412 | 1.6751 | 0.6290 | 3.4644 | 0.0109 | 0.3322 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1088_pos_at_h` | one_head_filter_pi_star | 33 | 2.8323 | 1.6867 | 0.6970 | 1.4381 | 0.0109 | 0.3030 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1088_pos_at_h` | one_head_filter_pi_star | 16 | 1.4806 | 0.7795 | 0.4375 | -0.4260 | -0.0140 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1088_pos_at_h` | one_head_filter_pi_star | 30 | 2.7593 | 0.6944 | 0.4333 | -0.8719 | -0.0204 | 0.2667 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1088_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.3008 | 0.2222 | -1.6957 | -0.0710 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1088_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3092 | 0.2353 | -1.6326 | -0.0748 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1088_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1088_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1088_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1088_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1088_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1088_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1088_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1088_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1088_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1088_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1088_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1088_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1088_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1088_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
