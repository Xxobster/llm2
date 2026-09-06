# Autonomy public-indicator hunt gen 016

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T083159Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `obv_osc_cross_up_0` | one_head_filter_pi_star | 16 | 1.4617 | 3.0737 | 0.6875 | 1.9144 | 0.0516 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `obv_osc_cross_down_0` | one_head_filter_pi_star | 29 | 2.5700 | 2.0093 | 0.6207 | 1.5121 | 0.0233 | 0.1034 | TPM<MIN | RAN |
| ETHUSDT | 8 | `obv_osc_neg_at_h` | one_head_filter_pi_star | 226 | 18.4621 | 1.7640 | 0.6726 | 3.7225 | 0.0204 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 4 | `obv_osc_neg_at_h` | one_head_filter_pi_star | 227 | 18.5438 | 1.7453 | 0.6740 | 3.6125 | 0.0198 | 0.3656 | EBR>35% | RAN |
| SOLUSDT | 4 | `obv_osc_neg_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.3074 | 0.7135 | 4.5127 | 0.0189 | 0.3989 | EBR>35% | RAN |
| SOLUSDT | 8 | `obv_osc_neg_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.2613 | 0.7011 | 4.3598 | 0.0186 | 0.4023 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `obv_osc_cross_down_0` | one_head_filter_pi_star | 16 | 1.4166 | 1.8864 | 0.6250 | 1.0389 | 0.0151 | 0.1250 | TPM<MIN | RAN |
| ETHUSDT | 8 | `obv_osc_cross_up_0` | one_head_filter_pi_star | 29 | 2.5591 | 1.3458 | 0.5862 | 0.7089 | 0.0136 | 0.3103 | TPM<MIN | RAN |
| SOLUSDT | 8 | `obv_osc_cross_down_0` | one_head_filter_pi_star | 28 | 2.4791 | 1.7117 | 0.6071 | 1.2186 | 0.0135 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 8 | `obv_osc_cross_up_0` | one_head_filter_pi_star | 16 | 1.4083 | 1.6119 | 0.6250 | 0.8454 | 0.0120 | 0.1250 | TPM<MIN | RAN |
| SOLUSDT | 4 | `obv_osc_cross_up_0` | one_head_filter_pi_star | 14 | 1.4196 | 1.6474 | 0.5714 | 0.8652 | 0.0116 | 0.0714 | TPM<MIN | RAN |
| ETHUSDT | 4 | `obv_osc_cross_down_0` | one_head_filter_pi_star | 14 | 1.3045 | 1.4500 | 0.5714 | 0.5430 | 0.0106 | 0.0000 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `obv_osc_pos_at_h` | one_head_filter_pi_star | 153 | 12.6258 | 1.2217 | 0.5882 | 0.9901 | 0.0069 | 0.2026 | ok | RAN |
| ETHUSDT | 4 | `obv_osc_pos_at_h` | one_head_filter_pi_star | 155 | 12.7908 | 1.2087 | 0.5935 | 0.9418 | 0.0066 | 0.2129 | ok | RAN |
| SOLUSDT | 4 | `obv_osc_pos_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.3331 | 0.5800 | 1.7861 | 0.0050 | 0.2600 | ok | RAN |
| SOLUSDT | 8 | `obv_osc_pos_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3190 | 0.5829 | 1.7434 | 0.0049 | 0.2563 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `obv_osc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `obv_osc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `obv_osc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `obv_osc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `obv_osc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `obv_osc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `obv_osc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `obv_osc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
