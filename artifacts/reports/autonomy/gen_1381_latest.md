# Autonomy public-indicator hunt gen 1381

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T035237Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret241_neg_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.1557 | 0.7022 | 4.6485 | 0.0262 | 0.3764 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret241_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9127 | 0.6882 | 4.0059 | 0.0226 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret241_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0011 | 0.6613 | 4.0345 | 0.0146 | 0.3495 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret241_neg_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.9503 | 0.6614 | 3.8155 | 0.0145 | 0.3439 | GATE_CAND | RAN |
| ETHUSDT | 4 | `ret241_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.3168 | 0.6136 | 1.4957 | 0.0110 | 0.2330 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret241_pos_at_h` | one_head_filter_pi_star | 163 | 13.2911 | 1.6162 | 0.6258 | 2.5419 | 0.0090 | 0.2699 | ok | RAN |
| SOLUSDT | 8 | `ret241_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5203 | 0.6136 | 2.3117 | 0.0078 | 0.2841 | ok | RAN |
| ETHUSDT | 8 | `ret241_pos_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1637 | 0.5904 | 0.8652 | 0.0059 | 0.2287 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret241_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.6954 | 0.3500 | -0.6289 | -0.0311 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret241_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret241_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret241_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret241_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret241_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret241_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret241_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret241_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret241_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret241_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret241_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret241_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret241_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret241_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret241_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
