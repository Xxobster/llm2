# Autonomy public-indicator hunt gen 1442

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T194513Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `ret1296_pos_at_h` | one_head_filter_pi_star | 23 | 2.0297 | 3.2787 | 0.7826 | 2.2209 | 0.0192 | 0.4348 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret1296_neg_at_h` | one_head_filter_pi_star | 343 | 27.9037 | 1.6308 | 0.6501 | 3.9469 | 0.0167 | 0.3003 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ret1296_neg_at_h` | one_head_filter_pi_star | 330 | 26.8461 | 1.5849 | 0.6424 | 3.6385 | 0.0154 | 0.3091 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret1296_pos_at_h` | one_head_filter_pi_star | 12 | 1.3207 | 1.8559 | 0.6667 | 1.0618 | 0.0122 | 0.4167 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret1296_neg_at_h` | one_head_filter_pi_star | 340 | 27.6597 | 1.6739 | 0.6324 | 4.0207 | 0.0102 | 0.3176 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret1296_neg_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.6368 | 0.6304 | 3.8843 | 0.0098 | 0.3181 | ok | RAN |
| ETHUSDT | 4 | `ret1296_pos_at_h` | one_head_filter_pi_star | 41 | 4.0253 | 1.2148 | 0.5366 | 0.5780 | 0.0091 | 0.2439 | ok | RAN |
| ETHUSDT | 8 | `ret1296_pos_at_h` | one_head_filter_pi_star | 40 | 3.6791 | 1.1540 | 0.5500 | 0.4111 | 0.0059 | 0.2250 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1296_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.6452 | 0.3333 | -0.6698 | -0.0267 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1296_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5849 | 0.3000 | -0.8836 | -0.0390 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1296_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1296_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1296_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1296_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
