# Autonomy public-indicator hunt gen 1533

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T055441Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret262_neg_at_h` | one_head_filter_pi_star | 182 | 14.8677 | 2.0297 | 0.6978 | 4.3857 | 0.0247 | 0.3846 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret262_neg_at_h` | one_head_filter_pi_star | 175 | 14.2959 | 2.0057 | 0.6914 | 4.1587 | 0.0238 | 0.3829 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret262_neg_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.0878 | 0.6818 | 4.1459 | 0.0164 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ret262_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 1.9627 | 0.6647 | 3.7487 | 0.0143 | 0.3533 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret262_pos_at_h` | one_head_filter_pi_star | 178 | 14.5969 | 1.5854 | 0.6180 | 2.5771 | 0.0088 | 0.2921 | ok | RAN |
| ETHUSDT | 8 | `ret262_pos_at_h` | one_head_filter_pi_star | 170 | 13.9738 | 1.2407 | 0.6176 | 1.1770 | 0.0082 | 0.2118 | ok | RAN |
| ETHUSDT | 4 | `ret262_pos_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1819 | 0.6047 | 0.9045 | 0.0063 | 0.2151 | ok | RAN |
| SOLUSDT | 4 | `ret262_pos_at_h` | one_head_filter_pi_star | 184 | 15.0889 | 1.3663 | 0.5978 | 1.7955 | 0.0062 | 0.2772 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret262_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0411 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret262_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret262_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret262_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret262_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret262_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret262_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret262_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret262_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret262_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret262_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret262_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret262_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret262_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret262_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret262_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
