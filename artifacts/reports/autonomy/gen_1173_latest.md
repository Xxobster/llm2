# Autonomy public-indicator hunt gen 1173

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T074048Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret211_neg_at_h` | one_head_filter_pi_star | 166 | 13.5607 | 2.2578 | 0.7108 | 4.8034 | 0.0276 | 0.4036 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret211_neg_at_h` | one_head_filter_pi_star | 176 | 14.3776 | 2.1355 | 0.7045 | 4.5648 | 0.0256 | 0.3920 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret211_neg_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.0905 | 0.6821 | 4.0868 | 0.0161 | 0.3815 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret211_neg_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.9882 | 0.6735 | 4.0287 | 0.0147 | 0.3673 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret211_pos_at_h` | one_head_filter_pi_star | 166 | 13.5357 | 1.5533 | 0.6145 | 2.3918 | 0.0082 | 0.2831 | ok | RAN |
| SOLUSDT | 4 | `ret211_pos_at_h` | one_head_filter_pi_star | 174 | 14.1880 | 1.4161 | 0.6092 | 1.9755 | 0.0065 | 0.2874 | ok | RAN |
| ETHUSDT | 4 | `ret211_pos_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.0941 | 0.5758 | 0.4940 | 0.0035 | 0.2222 | ok | RAN |
| ETHUSDT | 8 | `ret211_pos_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.0620 | 0.5771 | 0.3362 | 0.0023 | 0.2189 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret211_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0433 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret211_pos_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret211_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret211_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret211_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret211_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret211_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret211_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret211_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret211_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret211_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret211_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret211_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret211_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret211_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret211_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
