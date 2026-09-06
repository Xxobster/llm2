# Autonomy public-indicator hunt gen 637

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T025325Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret107_neg_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.7922 | 0.6717 | 3.8492 | 0.0203 | 0.3586 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret107_neg_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.7906 | 0.6720 | 3.7124 | 0.0201 | 0.3651 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret107_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.3419 | 0.6868 | 4.6012 | 0.0179 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret107_neg_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 2.1523 | 0.6789 | 4.3630 | 0.0162 | 0.3632 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ret107_pos_at_h` | one_head_filter_pi_star | 176 | 14.5238 | 1.4815 | 0.6477 | 2.1850 | 0.0146 | 0.2443 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ret107_pos_at_h` | one_head_filter_pi_star | 205 | 16.9169 | 1.2726 | 0.6146 | 1.4187 | 0.0092 | 0.2293 | ok | RAN |
| SOLUSDT | 4 | `ret107_pos_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.3860 | 0.6023 | 1.9017 | 0.0063 | 0.2557 | ok | RAN |
| SOLUSDT | 8 | `ret107_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3832 | 0.5947 | 1.9430 | 0.0061 | 0.2526 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret107_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret107_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0458 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret107_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret107_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret107_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret107_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret107_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret107_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret107_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret107_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret107_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret107_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret107_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret107_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret107_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret107_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
