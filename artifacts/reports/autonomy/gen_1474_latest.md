# Autonomy public-indicator hunt gen 1474

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T002239Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ret1328_pos_at_h` | one_head_filter_pi_star | 25 | 2.2062 | 3.2122 | 0.8000 | 2.2544 | 0.0243 | 0.4400 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1328_pos_at_h` | one_head_filter_pi_star | 24 | 2.0203 | 3.1339 | 0.7917 | 2.2164 | 0.0191 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1328_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.6745 | 0.6529 | 4.0098 | 0.0175 | 0.3088 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1328_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.6256 | 0.6490 | 3.7749 | 0.0165 | 0.3068 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1328_neg_at_h` | one_head_filter_pi_star | 332 | 27.0089 | 1.7471 | 0.6446 | 4.1748 | 0.0111 | 0.3253 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret1328_neg_at_h` | one_head_filter_pi_star | 339 | 27.5783 | 1.7107 | 0.6342 | 4.1055 | 0.0105 | 0.3186 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret1328_pos_at_h` | one_head_filter_pi_star | 28 | 2.7669 | 1.0473 | 0.5357 | 0.1102 | 0.0019 | 0.2143 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1328_pos_at_h` | one_head_filter_pi_star | 23 | 2.2728 | 0.8468 | 0.4783 | -0.3560 | -0.0063 | 0.1739 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1328_pos_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6169 | 0.2667 | -0.7191 | -0.0322 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1328_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1328_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1328_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret1328_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1328_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
