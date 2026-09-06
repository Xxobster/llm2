# Autonomy public-indicator hunt gen 045

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T122843Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ii_neg_at_h` | one_head_filter_pi_star | 208 | 16.9917 | 1.9102 | 0.6971 | 4.0897 | 0.0223 | 0.3894 | EBR>35% | RAN |
| ETHUSDT | 8 | `ii_neg_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.8362 | 0.6888 | 3.7008 | 0.0219 | 0.3878 | EBR>35% | RAN |
| SOLUSDT | 8 | `ii_cross_up_0` | one_head_filter_pi_star | 44 | 3.6323 | 2.1109 | 0.7045 | 2.1339 | 0.0202 | 0.3182 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ii_neg_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.3342 | 0.7025 | 4.3058 | 0.0193 | 0.4051 | EBR>35% | RAN |
| SOLUSDT | 4 | `ii_neg_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.3000 | 0.7037 | 4.2615 | 0.0189 | 0.4136 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `ii_cross_up_0` | one_head_filter_pi_star | 53 | 4.4913 | 1.3108 | 0.5849 | 0.8681 | 0.0101 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ii_pos_at_h` | one_head_filter_pi_star | 171 | 14.0099 | 1.2164 | 0.5906 | 1.0112 | 0.0074 | 0.2047 | ok | RAN |
| ETHUSDT | 8 | `ii_pos_at_h` | one_head_filter_pi_star | 174 | 14.2557 | 1.2110 | 0.5862 | 1.0296 | 0.0071 | 0.1954 | ok | RAN |
| SOLUSDT | 4 | `ii_pos_at_h` | one_head_filter_pi_star | 220 | 17.9389 | 1.3590 | 0.5909 | 1.9924 | 0.0054 | 0.2455 | ok | RAN |
| SOLUSDT | 8 | `ii_cross_down_0` | one_head_filter_pi_star | 39 | 3.3113 | 1.3473 | 0.6154 | 0.8203 | 0.0052 | 0.2308 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ii_pos_at_h` | one_head_filter_pi_star | 218 | 17.7758 | 1.3104 | 0.5826 | 1.7352 | 0.0049 | 0.2385 | ok | RAN |
| SOLUSDT | 4 | `ii_cross_up_0` | one_head_filter_pi_star | 24 | 2.0864 | 1.0928 | 0.6250 | 0.1967 | 0.0026 | 0.2083 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ii_cross_down_0` | one_head_filter_pi_star | 15 | 1.3109 | 1.1287 | 0.6000 | 0.1887 | 0.0019 | 0.1333 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ii_cross_up_0` | one_head_filter_pi_star | 19 | 1.7795 | 0.9096 | 0.4737 | -0.1974 | -0.0036 | 0.2632 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ii_cross_down_0` | one_head_filter_pi_star | 34 | 2.8286 | 0.5656 | 0.4412 | -1.3362 | -0.0132 | 0.0882 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ii_pos_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.7040 | 0.3500 | -0.6085 | -0.0297 | 0.1000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ii_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6980 | 0.3158 | -0.6210 | -0.0308 | 0.1053 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ii_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ii_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ii_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ii_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ii_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ii_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ii_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
