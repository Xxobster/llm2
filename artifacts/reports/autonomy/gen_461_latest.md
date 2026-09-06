# Autonomy public-indicator hunt gen 461

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T152335Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret63_neg_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.7841 | 0.6753 | 3.8616 | 0.0204 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret63_neg_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.7654 | 0.6771 | 3.8539 | 0.0202 | 0.3802 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret63_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.3735 | 0.7118 | 4.5700 | 0.0191 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret63_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.3365 | 0.7012 | 4.3934 | 0.0184 | 0.4024 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret63_pos_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.3487 | 0.6108 | 1.6809 | 0.0105 | 0.2324 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret63_pos_at_h` | one_head_filter_pi_star | 184 | 15.1246 | 1.3107 | 0.6087 | 1.5360 | 0.0097 | 0.2337 | ok | RAN |
| SOLUSDT | 4 | `ret63_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3851 | 0.6019 | 2.0316 | 0.0058 | 0.2476 | ok | RAN |
| SOLUSDT | 8 | `ret63_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.2344 | 0.5885 | 1.2751 | 0.0036 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret63_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret63_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret63_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret63_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret63_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret63_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret63_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret63_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret63_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret63_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret63_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret63_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret63_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret63_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret63_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret63_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
