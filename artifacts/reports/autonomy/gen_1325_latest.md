# Autonomy public-indicator hunt gen 1325

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T224026Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret233_neg_at_h` | one_head_filter_pi_star | 164 | 13.3973 | 2.3421 | 0.7195 | 4.8560 | 0.0282 | 0.3902 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret233_neg_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9905 | 0.6952 | 4.2954 | 0.0239 | 0.3904 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret233_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8376 | 0.6458 | 3.6048 | 0.0131 | 0.3542 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret233_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.7667 | 0.6373 | 3.4497 | 0.0122 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret233_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5369 | 0.6215 | 2.3589 | 0.0082 | 0.2768 | ok | RAN |
| SOLUSDT | 4 | `ret233_pos_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.4806 | 0.6215 | 2.2244 | 0.0075 | 0.2938 | ok | RAN |
| ETHUSDT | 8 | `ret233_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.2011 | 0.6051 | 1.0690 | 0.0071 | 0.2359 | ok | RAN |
| ETHUSDT | 4 | `ret233_pos_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1577 | 0.5979 | 0.8175 | 0.0057 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret233_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret233_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret233_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret233_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret233_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret233_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret233_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret233_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret233_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret233_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret233_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret233_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret233_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret233_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret233_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret233_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
