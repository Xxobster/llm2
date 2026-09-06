# Autonomy public-indicator hunt gen 046

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T123247Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `lrs_cross_down_0` | one_head_filter_pi_star | 22 | 1.8331 | 2.1776 | 0.6364 | 1.5004 | 0.0221 | 0.4545 | EBR>35% | RAN |
| ETHUSDT | 4 | `lrs_neg_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8505 | 0.6806 | 4.0099 | 0.0215 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 8 | `lrs_cross_up_0` | one_head_filter_pi_star | 27 | 2.5113 | 1.7869 | 0.5926 | 1.1860 | 0.0211 | 0.2593 | TPM<MIN | RAN |
| SOLUSDT | 8 | `lrs_cross_down_0` | one_head_filter_pi_star | 26 | 2.1664 | 2.3493 | 0.6538 | 1.6758 | 0.0207 | 0.4231 | EBR>35% | RAN |
| ETHUSDT | 8 | `lrs_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `lrs_cross_up_0` | one_head_filter_pi_star | 19 | 1.7672 | 1.9738 | 0.5789 | 1.2483 | 0.0201 | 0.3158 | TPM<MIN | RAN |
| SOLUSDT | 8 | `lrs_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2020 | 0.6951 | 4.0975 | 0.0182 | 0.4268 | EBR>35% | RAN |
| SOLUSDT | 4 | `lrs_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1888 | 0.6982 | 4.1357 | 0.0178 | 0.4201 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `lrs_cross_up_0` | one_head_filter_pi_star | 32 | 3.0574 | 1.8941 | 0.6250 | 1.5795 | 0.0137 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 8 | `lrs_cross_up_0` | one_head_filter_pi_star | 38 | 3.6306 | 1.6957 | 0.6053 | 1.4396 | 0.0114 | 0.1842 | TPM<MIN | RAN |
| ETHUSDT | 8 | `lrs_cross_down_0` | one_head_filter_pi_star | 53 | 4.3798 | 1.2694 | 0.6226 | 0.7099 | 0.0102 | 0.2830 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `lrs_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2406 | 0.5938 | 1.1316 | 0.0073 | 0.2000 | ok | RAN |
| ETHUSDT | 8 | `lrs_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2157 | 0.5926 | 0.9952 | 0.0069 | 0.2037 | ok | RAN |
| SOLUSDT | 4 | `lrs_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3934 | 0.5953 | 2.1046 | 0.0058 | 0.2512 | ok | RAN |
| SOLUSDT | 8 | `lrs_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3945 | 0.5981 | 2.1188 | 0.0058 | 0.2477 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `lrs_cross_down_0` | one_head_filter_pi_star | 47 | 3.8840 | 1.0105 | 0.5745 | 0.0286 | 0.0005 | 0.3191 | TPM<MIN | RAN |
| BTCUSDT | 4 | `lrs_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `lrs_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `lrs_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `lrs_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `lrs_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `lrs_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `lrs_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `lrs_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
