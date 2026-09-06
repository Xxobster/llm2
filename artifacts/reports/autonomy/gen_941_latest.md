# Autonomy public-indicator hunt gen 941

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T060001Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret183_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.3363 | 0.7169 | 5.0338 | 0.0283 | 0.3976 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret183_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.0886 | 0.6928 | 4.4602 | 0.0260 | 0.3916 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret183_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1101 | 0.6805 | 4.0267 | 0.0158 | 0.3669 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret183_neg_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 1.9779 | 0.6667 | 3.8834 | 0.0150 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret183_pos_at_h` | one_head_filter_pi_star | 219 | 18.0722 | 1.2854 | 0.6027 | 1.4990 | 0.0096 | 0.2374 | ok | RAN |
| SOLUSDT | 8 | `ret183_pos_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4853 | 0.6126 | 2.3206 | 0.0074 | 0.2618 | ok | RAN |
| SOLUSDT | 4 | `ret183_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.4227 | 0.6087 | 2.0077 | 0.0067 | 0.2717 | ok | RAN |
| ETHUSDT | 8 | `ret183_pos_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.1638 | 0.5904 | 0.8488 | 0.0057 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret183_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret183_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret183_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret183_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret183_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret183_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret183_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret183_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret183_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret183_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret183_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret183_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret183_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret183_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret183_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret183_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
