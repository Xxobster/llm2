# Autonomy public-indicator hunt gen 757

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T111927Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ret137_neg_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9016 | 0.6891 | 4.1955 | 0.0223 | 0.3782 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret137_neg_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.7084 | 0.6548 | 3.4853 | 0.0183 | 0.3655 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret137_neg_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1430 | 0.6757 | 4.2882 | 0.0164 | 0.3730 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret137_neg_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1492 | 0.6813 | 4.2081 | 0.0162 | 0.3626 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `ret137_pos_at_h` | one_head_filter_pi_star | 178 | 14.6888 | 1.3807 | 0.6124 | 1.8426 | 0.0121 | 0.2303 | ok | RAN |
| ETHUSDT | 8 | `ret137_pos_at_h` | one_head_filter_pi_star | 182 | 15.0189 | 1.3371 | 0.6209 | 1.6418 | 0.0113 | 0.2253 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ret137_pos_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3865 | 0.5990 | 1.9435 | 0.0062 | 0.2604 | ok | RAN |
| SOLUSDT | 8 | `ret137_pos_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.3174 | 0.5978 | 1.5633 | 0.0052 | 0.2663 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret137_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret137_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret137_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret137_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 8 | `ret137_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ret137_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret137_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret137_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret137_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ret137_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret137_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret137_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret137_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret137_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret137_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret137_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
