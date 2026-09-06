# Autonomy public-indicator hunt gen 605

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T005124Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret99_neg_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.8018 | 0.6684 | 3.8120 | 0.0201 | 0.3632 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret99_neg_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.7586 | 0.6634 | 3.8108 | 0.0194 | 0.3561 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret99_neg_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1610 | 0.6722 | 4.2032 | 0.0166 | 0.3611 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret99_neg_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.0951 | 0.6667 | 3.9011 | 0.0157 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret99_pos_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.3454 | 0.6298 | 1.6752 | 0.0117 | 0.2320 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret99_pos_at_h` | one_head_filter_pi_star | 183 | 15.1014 | 1.2934 | 0.6175 | 1.4289 | 0.0098 | 0.2350 | ok | RAN |
| SOLUSDT | 4 | `ret99_pos_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.3785 | 0.6000 | 1.9073 | 0.0061 | 0.2595 | ok | RAN |
| SOLUSDT | 8 | `ret99_pos_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3146 | 0.5895 | 1.6213 | 0.0052 | 0.2632 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret99_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret99_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret99_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret99_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret99_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret99_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret99_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret99_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret99_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret99_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret99_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret99_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret99_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret99_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret99_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret99_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
