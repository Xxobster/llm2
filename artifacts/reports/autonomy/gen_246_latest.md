# Autonomy public-indicator hunt gen 246

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T014140Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma45_cross_down` | one_head_filter_pi_star | 20 | 1.7453 | 2.1068 | 0.6000 | 1.3807 | 0.0285 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma45_below_at_h` | one_head_filter_pi_star | 222 | 18.1354 | 1.8033 | 0.6802 | 3.8752 | 0.0209 | 0.3739 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma45_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8007 | 0.6787 | 3.8626 | 0.0207 | 0.3756 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma45_cross_down` | one_head_filter_pi_star | 17 | 1.5730 | 2.6997 | 0.7647 | 1.6040 | 0.0198 | 0.0588 | TPM<MIN | RAN |
| SOLUSDT | 4 | `wma45_below_at_h` | one_head_filter_pi_star | 160 | 13.0833 | 2.1473 | 0.6875 | 3.9575 | 0.0175 | 0.4188 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma45_below_at_h` | one_head_filter_pi_star | 159 | 13.0016 | 2.1279 | 0.6855 | 3.8964 | 0.0172 | 0.4151 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma45_cross_up` | one_head_filter_pi_star | 16 | 1.3209 | 1.4241 | 0.6250 | 0.6005 | 0.0140 | 0.1875 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma45_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0064 | 0.2062 | ok | RAN |
| ETHUSDT | 8 | `wma45_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1961 | 0.5912 | 0.9014 | 0.0062 | 0.2075 | ok | RAN |
| SOLUSDT | 8 | `wma45_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.4202 | 0.6037 | 2.2116 | 0.0061 | 0.2535 | ok | RAN |
| SOLUSDT | 4 | `wma45_above_at_h` | one_head_filter_pi_star | 215 | 17.5312 | 1.3610 | 0.5953 | 1.9510 | 0.0053 | 0.2419 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma45_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma45_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `wma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma45_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma45_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
