# Autonomy public-indicator hunt gen 157

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T194626Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret18_cross_up_0` | one_head_filter_pi_star | 32 | 2.6332 | 1.9310 | 0.6250 | 1.4869 | 0.0303 | 0.2812 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret18_cross_up_0` | one_head_filter_pi_star | 27 | 2.3472 | 2.4959 | 0.7037 | 1.8495 | 0.0225 | 0.1852 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret18_neg_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.8738 | 0.6872 | 3.9517 | 0.0218 | 0.3791 | EBR>35% | RAN |
| ETHUSDT | 8 | `ret18_neg_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7750 | 0.6742 | 3.7215 | 0.0199 | 0.3710 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret18_neg_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2369 | 0.6982 | 4.2649 | 0.0186 | 0.4083 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret18_neg_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0870 | 0.6826 | 3.8679 | 0.0170 | 0.4192 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ret18_cross_down_0` | one_head_filter_pi_star | 23 | 2.1282 | 2.2276 | 0.7391 | 1.6189 | 0.0143 | 0.0870 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ret18_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2149 | 0.5963 | 0.9888 | 0.0068 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `ret18_pos_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.1967 | 0.5828 | 0.9605 | 0.0064 | 0.1963 | ok | RAN |
| SOLUSDT | 8 | `ret18_pos_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3880 | 0.5971 | 2.0370 | 0.0057 | 0.2476 | ok | RAN |
| SOLUSDT | 4 | `ret18_pos_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3360 | 0.5896 | 1.8294 | 0.0050 | 0.2453 | ok | RAN |
| ETHUSDT | 8 | `ret18_cross_down_0` | one_head_filter_pi_star | 35 | 2.9003 | 1.0375 | 0.5714 | 0.0913 | 0.0015 | 0.1714 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret18_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret18_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret18_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret18_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret18_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ret18_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret18_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret18_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret18_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret18_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret18_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret18_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
