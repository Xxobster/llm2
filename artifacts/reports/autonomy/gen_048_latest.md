# Autonomy public-indicator hunt gen 048

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T124113Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `midroc_cross_down_0` | one_head_filter_pi_star | 19 | 1.5631 | 2.3461 | 0.6842 | 1.4794 | 0.0241 | 0.2632 | TPM<MIN | RAN |
| ETHUSDT | 8 | `midroc_cross_up_0` | one_head_filter_pi_star | 21 | 1.7337 | 2.0433 | 0.6190 | 1.3280 | 0.0229 | 0.2381 | TPM<MIN | RAN |
| ETHUSDT | 8 | `midroc_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.7865 | 0.6757 | 3.8245 | 0.0203 | 0.3694 | EBR>35% | RAN |
| ETHUSDT | 4 | `midroc_neg_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7681 | 0.6758 | 3.6956 | 0.0198 | 0.3744 | EBR>35% | RAN |
| SOLUSDT | 8 | `midroc_neg_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2426 | 0.6951 | 4.1776 | 0.0184 | 0.4207 | EBR>35% | RAN |
| SOLUSDT | 4 | `midroc_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1566 | 0.6933 | 3.9615 | 0.0175 | 0.4172 | EBR>35% | RAN |
| SOLUSDT | 8 | `midroc_cross_down_0` | one_head_filter_pi_star | 20 | 1.6453 | 2.1837 | 0.7000 | 1.3331 | 0.0172 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `midroc_cross_down_0` | one_head_filter_pi_star | 37 | 3.0559 | 1.2917 | 0.6216 | 0.6579 | 0.0126 | 0.2162 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `midroc_cross_down_0` | one_head_filter_pi_star | 34 | 2.8081 | 1.1717 | 0.5882 | 0.3978 | 0.0084 | 0.2353 | TPM<MIN | RAN |
| ETHUSDT | 8 | `midroc_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2652 | 0.6025 | 1.1880 | 0.0083 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `midroc_pos_at_h` | one_head_filter_pi_star | 162 | 13.3685 | 1.2211 | 0.5926 | 1.0376 | 0.0069 | 0.1975 | ok | RAN |
| SOLUSDT | 8 | `midroc_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3958 | 0.5972 | 2.1313 | 0.0059 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `midroc_cross_up_0` | one_head_filter_pi_star | 15 | 1.3017 | 1.1866 | 0.5333 | 0.2821 | 0.0057 | 0.2000 | TPM<MIN | RAN |
| SOLUSDT | 8 | `midroc_cross_up_0` | one_head_filter_pi_star | 27 | 2.3472 | 1.2550 | 0.5926 | 0.5517 | 0.0057 | 0.1852 | TPM<MIN | RAN |
| SOLUSDT | 4 | `midroc_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3664 | 0.5888 | 1.9863 | 0.0055 | 0.2477 | ok | RAN |
| SOLUSDT | 4 | `midroc_cross_up_0` | one_head_filter_pi_star | 23 | 1.9995 | 1.1115 | 0.5652 | 0.2278 | 0.0025 | 0.1739 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `midroc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `midroc_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `midroc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `midroc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `midroc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `midroc_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `midroc_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `midroc_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
