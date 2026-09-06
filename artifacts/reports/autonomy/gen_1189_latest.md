# Autonomy public-indicator hunt gen 1189

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T091530Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret213_neg_at_h` | one_head_filter_pi_star | 165 | 13.4790 | 2.1761 | 0.7030 | 4.5589 | 0.0271 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret213_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.1323 | 0.7048 | 4.4580 | 0.0246 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret213_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9994 | 0.6737 | 3.9608 | 0.0149 | 0.3789 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret213_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 1.8631 | 0.6595 | 3.5717 | 0.0132 | 0.3676 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret213_pos_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.6227 | 0.6348 | 2.7321 | 0.0091 | 0.2697 | ok | RAN |
| ETHUSDT | 4 | `ret213_pos_at_h` | one_head_filter_pi_star | 211 | 17.3439 | 1.2383 | 0.5877 | 1.1936 | 0.0085 | 0.2227 | ok | RAN |
| ETHUSDT | 8 | `ret213_pos_at_h` | one_head_filter_pi_star | 209 | 17.1795 | 1.2395 | 0.5933 | 1.3028 | 0.0085 | 0.2440 | ok | RAN |
| SOLUSDT | 4 | `ret213_pos_at_h` | one_head_filter_pi_star | 169 | 13.7803 | 1.3794 | 0.6036 | 1.7883 | 0.0061 | 0.2959 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret213_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret213_pos_at_h` | one_head_filter_pi_star | 17 | 1.4467 | 0.5773 | 0.2941 | -0.8964 | -0.0465 | 0.0588 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret213_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret213_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret213_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret213_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret213_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret213_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret213_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret213_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret213_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret213_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret213_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret213_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret213_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret213_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
