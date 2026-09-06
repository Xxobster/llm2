# Autonomy public-indicator hunt gen 1485

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T012345Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret255_neg_at_h` | one_head_filter_pi_star | 154 | 12.5804 | 2.3932 | 0.7208 | 4.7523 | 0.0300 | 0.4026 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret255_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 2.0463 | 0.7000 | 4.3265 | 0.0251 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret255_neg_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 1.8727 | 0.6488 | 3.4369 | 0.0134 | 0.3512 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret255_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.8790 | 0.6615 | 3.7698 | 0.0131 | 0.3385 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret255_pos_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.5378 | 0.6176 | 2.3803 | 0.0084 | 0.2882 | ok | RAN |
| ETHUSDT | 4 | `ret255_pos_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.2293 | 0.6000 | 1.1351 | 0.0080 | 0.2171 | ok | RAN |
| SOLUSDT | 4 | `ret255_pos_at_h` | one_head_filter_pi_star | 178 | 14.5969 | 1.4298 | 0.6011 | 1.9862 | 0.0069 | 0.2809 | ok | RAN |
| ETHUSDT | 8 | `ret255_pos_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.1581 | 0.5879 | 0.8098 | 0.0055 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret255_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6154 | 0.3500 | -0.7982 | -0.0398 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret255_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0460 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret255_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret255_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret255_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret255_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret255_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret255_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret255_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret255_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret255_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret255_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret255_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret255_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret255_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret255_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
