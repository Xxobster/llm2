# Autonomy public-indicator hunt gen 1221

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T122014Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret218_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.2835 | 0.7091 | 4.7046 | 0.0282 | 0.4061 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret218_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.1980 | 0.7110 | 4.7669 | 0.0274 | 0.4104 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret218_neg_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 2.0045 | 0.6667 | 4.0252 | 0.0150 | 0.3698 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret218_neg_at_h` | one_head_filter_pi_star | 188 | 15.3884 | 1.9246 | 0.6649 | 3.7700 | 0.0139 | 0.3723 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret218_pos_at_h` | one_head_filter_pi_star | 176 | 14.4329 | 1.6265 | 0.6307 | 2.7322 | 0.0092 | 0.2898 | ok | RAN |
| SOLUSDT | 4 | `ret218_pos_at_h` | one_head_filter_pi_star | 173 | 14.1869 | 1.4564 | 0.6127 | 2.1012 | 0.0071 | 0.2775 | ok | RAN |
| ETHUSDT | 8 | `ret218_pos_at_h` | one_head_filter_pi_star | 195 | 16.0287 | 1.1655 | 0.5846 | 0.8805 | 0.0059 | 0.2410 | ok | RAN |
| ETHUSDT | 4 | `ret218_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1405 | 0.5946 | 0.7370 | 0.0050 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret218_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret218_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret218_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret218_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret218_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret218_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret218_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret218_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret218_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret218_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret218_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret218_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret218_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret218_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret218_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret218_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
