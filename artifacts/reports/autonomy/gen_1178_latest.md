# Autonomy public-indicator hunt gen 1178

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T080945Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret1032_pos_at_h` | one_head_filter_pi_star | 13 | 1.1619 | 2.3843 | 0.6923 | 1.3617 | 0.0293 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret1032_neg_at_h` | one_head_filter_pi_star | 274 | 22.2904 | 1.7037 | 0.6533 | 3.9236 | 0.0174 | 0.3248 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret1032_neg_at_h` | one_head_filter_pi_star | 275 | 22.3718 | 1.6952 | 0.6473 | 3.7578 | 0.0170 | 0.3273 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1032_pos_at_h` | one_head_filter_pi_star | 45 | 3.7407 | 2.2120 | 0.7111 | 2.2410 | 0.0141 | 0.2889 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ret1032_pos_at_h` | one_head_filter_pi_star | 58 | 4.8205 | 2.1531 | 0.7241 | 2.5858 | 0.0130 | 0.2759 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1032_neg_at_h` | one_head_filter_pi_star | 279 | 22.6972 | 1.7549 | 0.6344 | 3.8987 | 0.0116 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1032_neg_at_h` | one_head_filter_pi_star | 290 | 23.5921 | 1.6859 | 0.6276 | 3.7463 | 0.0108 | 0.3207 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret1032_pos_at_h` | one_head_filter_pi_star | 29 | 2.5919 | 1.2160 | 0.5517 | 0.4606 | 0.0092 | 0.3103 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1032_pos_at_h` | one_head_filter_pi_star | 16 | 1.3616 | 0.4479 | 0.3125 | -1.1181 | -0.0446 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1032_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.3442 | 0.2941 | -1.4812 | -0.0689 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1032_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1032_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1032_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1032_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1032_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1032_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1032_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1032_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1032_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret1032_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1032_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1032_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1032_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1032_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
