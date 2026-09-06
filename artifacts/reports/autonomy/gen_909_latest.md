# Autonomy public-indicator hunt gen 909

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T022451Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret175_neg_at_h` | one_head_filter_pi_star | 173 | 14.1325 | 2.0935 | 0.7052 | 4.5123 | 0.0247 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret175_neg_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.9371 | 0.6889 | 4.2354 | 0.0234 | 0.3889 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret175_neg_at_h` | one_head_filter_pi_star | 157 | 12.8380 | 2.1061 | 0.6688 | 3.8552 | 0.0161 | 0.3885 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret175_neg_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.0884 | 0.6687 | 3.9450 | 0.0159 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret175_pos_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2380 | 0.6010 | 1.2631 | 0.0081 | 0.2228 | ok | RAN |
| ETHUSDT | 8 | `ret175_pos_at_h` | one_head_filter_pi_star | 206 | 16.9329 | 1.2446 | 0.5971 | 1.2992 | 0.0078 | 0.2184 | ok | RAN |
| SOLUSDT | 8 | `ret175_pos_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.4566 | 0.6098 | 2.2619 | 0.0072 | 0.2634 | ok | RAN |
| SOLUSDT | 4 | `ret175_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.4387 | 0.6068 | 2.2069 | 0.0069 | 0.2621 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret175_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret175_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret175_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret175_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret175_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret175_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret175_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret175_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret175_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret175_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret175_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret175_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret175_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret175_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret175_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret175_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
