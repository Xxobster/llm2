# Autonomy public-indicator hunt gen 1253

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T153800Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret222_neg_at_h` | one_head_filter_pi_star | 171 | 13.9691 | 2.1602 | 0.6959 | 4.5704 | 0.0260 | 0.3860 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret222_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 1.9243 | 0.6936 | 3.9600 | 0.0229 | 0.3873 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret222_neg_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.0171 | 0.6723 | 3.8426 | 0.0153 | 0.3729 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret222_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.9983 | 0.6720 | 3.9773 | 0.0144 | 0.3656 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret222_pos_at_h` | one_head_filter_pi_star | 164 | 13.3726 | 1.5415 | 0.6159 | 2.3472 | 0.0079 | 0.2805 | ok | RAN |
| ETHUSDT | 4 | `ret222_pos_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2234 | 0.5989 | 1.1503 | 0.0079 | 0.2139 | ok | RAN |
| SOLUSDT | 8 | `ret222_pos_at_h` | one_head_filter_pi_star | 164 | 13.3726 | 1.4491 | 0.6159 | 2.0418 | 0.0072 | 0.2805 | ok | RAN |
| ETHUSDT | 8 | `ret222_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.0941 | 0.5761 | 0.4826 | 0.0035 | 0.2283 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret222_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret222_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret222_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret222_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret222_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret222_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret222_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret222_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret222_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret222_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret222_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret222_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret222_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret222_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret222_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret222_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
