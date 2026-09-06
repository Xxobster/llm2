# Autonomy public-indicator hunt gen 052

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T125837Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `gator_cross_down_0` | one_head_filter_pi_star | 23 | 1.9664 | 5.5858 | 0.6957 | 2.6993 | 0.0533 | 0.3913 | EBR>35% | RAN |
| SOLUSDT | 8 | `gator_cross_down_0` | one_head_filter_pi_star | 24 | 2.0518 | 3.7418 | 0.6667 | 2.3114 | 0.0461 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `gator_cross_up_0` | one_head_filter_pi_star | 24 | 2.2323 | 1.8816 | 0.5833 | 1.3084 | 0.0257 | 0.1667 | TPM<MIN | RAN |
| ETHUSDT | 8 | `gator_neg_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0207 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `gator_neg_at_h` | one_head_filter_pi_star | 218 | 17.8086 | 1.7443 | 0.6697 | 3.6350 | 0.0196 | 0.3716 | EBR>35% | RAN |
| ETHUSDT | 4 | `gator_cross_down_0` | one_head_filter_pi_star | 43 | 3.5534 | 1.4644 | 0.6279 | 1.1148 | 0.0184 | 0.3023 | TPM<MIN | RAN |
| SOLUSDT | 8 | `gator_neg_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1781 | 0.6871 | 4.0304 | 0.0179 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 4 | `gator_neg_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1476 | 0.6894 | 3.9416 | 0.0174 | 0.4286 | EBR>35% | RAN |
| ETHUSDT | 8 | `gator_cross_down_0` | one_head_filter_pi_star | 43 | 3.5534 | 1.4644 | 0.6279 | 1.1148 | 0.0170 | 0.3023 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `gator_cross_up_0` | one_head_filter_pi_star | 25 | 2.3253 | 1.4365 | 0.5600 | 0.7769 | 0.0152 | 0.1600 | TPM<MIN | RAN |
| SOLUSDT | 4 | `gator_cross_up_0` | one_head_filter_pi_star | 34 | 2.9633 | 1.6755 | 0.6471 | 1.2618 | 0.0122 | 0.1176 | TPM<MIN | RAN |
| SOLUSDT | 8 | `gator_cross_up_0` | one_head_filter_pi_star | 34 | 2.9633 | 1.6755 | 0.6471 | 1.2618 | 0.0120 | 0.1176 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `gator_pos_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2003 | 0.5901 | 0.9238 | 0.0064 | 0.2050 | ok | RAN |
| ETHUSDT | 4 | `gator_pos_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.1835 | 0.5938 | 0.8616 | 0.0058 | 0.2000 | ok | RAN |
| SOLUSDT | 8 | `gator_pos_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3772 | 0.5981 | 2.0354 | 0.0056 | 0.2430 | ok | RAN |
| SOLUSDT | 4 | `gator_pos_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3597 | 0.6000 | 1.9464 | 0.0053 | 0.2372 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `gator_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `gator_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `gator_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `gator_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `gator_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `gator_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `gator_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `gator_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
