# Autonomy public-indicator hunt gen 386

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T230808Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret240_neg_at_h` | one_head_filter_pi_star | 168 | 13.7241 | 2.0899 | 0.7024 | 4.4248 | 0.0253 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret240_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.0718 | 0.7022 | 4.4009 | 0.0246 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret240_neg_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.9559 | 0.6599 | 4.0531 | 0.0141 | 0.3452 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret240_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.8695 | 0.6517 | 3.5626 | 0.0133 | 0.3483 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret240_pos_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.2920 | 0.6074 | 1.3846 | 0.0098 | 0.2331 | ok | RAN |
| SOLUSDT | 8 | `ret240_pos_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.6257 | 0.6294 | 2.6800 | 0.0093 | 0.2882 | ok | RAN |
| SOLUSDT | 4 | `ret240_pos_at_h` | one_head_filter_pi_star | 164 | 13.3726 | 1.4942 | 0.6159 | 2.1399 | 0.0076 | 0.2744 | ok | RAN |
| ETHUSDT | 8 | `ret240_pos_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.1577 | 0.5812 | 0.8489 | 0.0056 | 0.2356 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret240_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret240_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret240_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret240_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret240_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret240_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
