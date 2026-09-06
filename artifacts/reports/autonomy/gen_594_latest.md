# Autonomy public-indicator hunt gen 594

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T000915Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret448_neg_at_h` | one_head_filter_pi_star | 160 | 13.0705 | 2.2905 | 0.7125 | 4.5801 | 0.0282 | 0.3812 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret448_neg_at_h` | one_head_filter_pi_star | 138 | 11.2733 | 2.2577 | 0.7101 | 4.2743 | 0.0259 | 0.3986 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret448_neg_at_h` | one_head_filter_pi_star | 208 | 16.9212 | 1.7548 | 0.6587 | 3.4789 | 0.0116 | 0.3269 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ret448_neg_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.7171 | 0.6580 | 3.2015 | 0.0115 | 0.3420 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret448_pos_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.6591 | 0.6205 | 2.7639 | 0.0101 | 0.2831 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret448_pos_at_h` | one_head_filter_pi_star | 121 | 9.9226 | 1.5880 | 0.6281 | 2.1231 | 0.0093 | 0.2727 | ok | RAN |
| ETHUSDT | 8 | `ret448_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2619 | 0.6111 | 1.3402 | 0.0091 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `ret448_pos_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1294 | 0.5706 | 0.6862 | 0.0049 | 0.2331 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret448_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5883 | 0.3500 | -0.8891 | -0.0400 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret448_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5547 | 0.3000 | -0.9879 | -0.0437 | 0.0500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret448_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret448_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret448_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret448_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
