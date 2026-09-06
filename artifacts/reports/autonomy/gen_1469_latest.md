# Autonomy public-indicator hunt gen 1469

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T235505Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret253_neg_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 2.0093 | 0.6935 | 4.3219 | 0.0251 | 0.3817 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret253_neg_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.0137 | 0.6957 | 4.4104 | 0.0242 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret253_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 1.9106 | 0.6609 | 3.6778 | 0.0139 | 0.3448 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ret253_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 1.8602 | 0.6550 | 3.4858 | 0.0132 | 0.3509 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret253_pos_at_h` | one_head_filter_pi_star | 171 | 14.0228 | 1.5605 | 0.6199 | 2.4854 | 0.0085 | 0.2749 | ok | RAN |
| SOLUSDT | 4 | `ret253_pos_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.4958 | 0.6154 | 2.2642 | 0.0077 | 0.2802 | ok | RAN |
| ETHUSDT | 4 | `ret253_pos_at_h` | one_head_filter_pi_star | 166 | 13.6450 | 1.1752 | 0.5904 | 0.8421 | 0.0063 | 0.2410 | ok | RAN |
| ETHUSDT | 8 | `ret253_pos_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.1333 | 0.5934 | 0.6859 | 0.0049 | 0.2308 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret253_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0416 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret253_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret253_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret253_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret253_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret253_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret253_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret253_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret253_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret253_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret253_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret253_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret253_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret253_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret253_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret253_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
