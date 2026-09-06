# Autonomy public-indicator hunt gen 155

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T193810Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `sma45_cross_up` | one_head_filter_pi_star | 12 | 1.2249 | 8.8442 | 0.6667 | 2.6016 | 0.0444 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma45_cross_up` | one_head_filter_pi_star | 21 | 2.1255 | 1.7734 | 0.6190 | 1.2526 | 0.0224 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma45_below_at_h` | one_head_filter_pi_star | 216 | 17.6452 | 1.8532 | 0.6852 | 3.9888 | 0.0217 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma45_below_at_h` | one_head_filter_pi_star | 224 | 18.2988 | 1.7995 | 0.6830 | 3.9261 | 0.0211 | 0.3661 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma45_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1899 | 0.6871 | 4.1032 | 0.0180 | 0.4110 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma45_below_at_h` | one_head_filter_pi_star | 158 | 12.9198 | 2.1272 | 0.6899 | 3.8905 | 0.0172 | 0.4241 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma45_cross_down` | one_head_filter_pi_star | 28 | 2.3898 | 1.6365 | 0.6429 | 1.0307 | 0.0135 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma45_above_at_h` | one_head_filter_pi_star | 156 | 12.8733 | 1.2462 | 0.6026 | 1.1157 | 0.0075 | 0.2115 | ok | RAN |
| ETHUSDT | 4 | `sma45_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2179 | 0.5938 | 1.0074 | 0.0067 | 0.2125 | ok | RAN |
| SOLUSDT | 8 | `sma45_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3414 | 0.5981 | 1.8310 | 0.0050 | 0.2523 | ok | RAN |
| SOLUSDT | 4 | `sma45_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3013 | 0.5943 | 1.6587 | 0.0045 | 0.2500 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 8 | `sma45_cross_down` | one_head_filter_pi_star | 26 | 2.1545 | 1.0246 | 0.5385 | 0.0544 | 0.0011 | 0.2308 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma45_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma45_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `sma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma45_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma45_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma45_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma45_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
