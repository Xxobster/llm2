# Autonomy public-indicator hunt gen 301

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T053354Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ret27_cross_down_0` | one_head_filter_pi_star | 34 | 2.9555 | 4.0748 | 0.6471 | 3.1034 | 0.0353 | 0.2353 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret27_cross_up_0` | one_head_filter_pi_star | 23 | 1.9247 | 1.9619 | 0.5652 | 1.4042 | 0.0305 | 0.0870 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ret27_cross_down_0` | one_head_filter_pi_star | 32 | 2.6312 | 3.0809 | 0.6875 | 2.3806 | 0.0239 | 0.1562 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret27_neg_at_h` | one_head_filter_pi_star | 211 | 17.2368 | 1.8748 | 0.6777 | 4.0723 | 0.0217 | 0.3934 | EBR>35% | RAN |
| ETHUSDT | 4 | `ret27_neg_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8122 | 0.6746 | 3.9273 | 0.0210 | 0.3732 | EBR>35% | RAN |
| SOLUSDT | 8 | `ret27_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.1659 | 0.6941 | 4.0816 | 0.0179 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 4 | `ret27_neg_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.0114 | 0.6765 | 3.7398 | 0.0156 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ret27_pos_at_h` | one_head_filter_pi_star | 211 | 17.2050 | 1.4385 | 0.6066 | 2.2313 | 0.0064 | 0.2559 | ok | RAN |
| SOLUSDT | 4 | `ret27_pos_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3834 | 0.5972 | 2.0252 | 0.0058 | 0.2500 | ok | RAN |
| ETHUSDT | 4 | `ret27_pos_at_h` | one_head_filter_pi_star | 170 | 14.0286 | 1.1819 | 0.5941 | 0.8862 | 0.0058 | 0.2118 | ok | RAN |
| SOLUSDT | 8 | `ret27_cross_up_0` | one_head_filter_pi_star | 19 | 1.7232 | 1.3034 | 0.5263 | 0.4834 | 0.0052 | 0.1579 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ret27_pos_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.1470 | 0.6026 | 0.7108 | 0.0047 | 0.1795 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ret27_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ret27_pos_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ret27_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ret27_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret27_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ret27_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret27_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ret27_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ret27_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret27_neg_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ret27_cross_up_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ret27_cross_down_0` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
