# Autonomy public-indicator hunt gen 1434

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T161911Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret1288_neg_at_h` | one_head_filter_pi_star | 348 | 28.3105 | 1.7248 | 0.6609 | 4.2097 | 0.0188 | 0.3017 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1288_pos_at_h` | one_head_filter_pi_star | 17 | 1.4607 | 2.7903 | 0.7647 | 1.6882 | 0.0171 | 0.4118 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret1288_neg_at_h` | one_head_filter_pi_star | 349 | 28.3918 | 1.6305 | 0.6504 | 3.9273 | 0.0168 | 0.2980 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret1288_neg_at_h` | one_head_filter_pi_star | 336 | 27.3343 | 1.7282 | 0.6369 | 4.2395 | 0.0111 | 0.3185 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret1288_neg_at_h` | one_head_filter_pi_star | 345 | 28.0664 | 1.6863 | 0.6377 | 4.1292 | 0.0107 | 0.3217 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret1288_pos_at_h` | one_head_filter_pi_star | 46 | 4.5162 | 1.1970 | 0.5435 | 0.6041 | 0.0084 | 0.2391 | ok | RAN |
| SOLUSDT | 4 | `ret1288_pos_at_h` | one_head_filter_pi_star | 13 | 1.4497 | 1.4140 | 0.6154 | 0.5934 | 0.0072 | 0.3077 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret1288_pos_at_h` | one_head_filter_pi_star | 15 | 3.0710 | 0.6952 | 0.4000 | -0.9458 | -0.0122 | 0.1333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret1288_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.4966 | 0.3158 | -1.0784 | -0.0493 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret1288_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4777 | 0.2778 | -1.1199 | -0.0531 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret1288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret1288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret1288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret1288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret1288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1288_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret1288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1288_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1288_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret1288_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
