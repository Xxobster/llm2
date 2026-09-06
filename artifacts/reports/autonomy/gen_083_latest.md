# Autonomy public-indicator hunt gen 083

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T145849Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 4 | `pdi_cross_down_20` | one_head_filter_pi_star | 14 | 1.1529 | 64.0422 | 0.9286 | 2.9063 | 0.0512 | 0.3571 | EBR>35% | RAN |
| SOLUSDT | 8 | `pdi_cross_down_20` | one_head_filter_pi_star | 32 | 2.6351 | 6.8283 | 0.8438 | 3.3690 | 0.0420 | 0.2812 | TPM<MIN | RAN |
| ETHUSDT | 4 | `pdi_cross_down_20` | one_head_filter_pi_star | 21 | 1.7354 | 2.4315 | 0.6190 | 1.6774 | 0.0356 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 8 | `pdi_cross_down_20` | one_head_filter_pi_star | 32 | 2.6444 | 1.7976 | 0.5938 | 1.3998 | 0.0257 | 0.2812 | TPM<MIN | RAN |
| ETHUSDT | 4 | `pdi_low_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.8430 | 0.6761 | 3.9535 | 0.0216 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `pdi_low_at_h` | one_head_filter_pi_star | 209 | 17.0734 | 1.8048 | 0.6794 | 3.7328 | 0.0211 | 0.3780 | EBR>35% | RAN |
| SOLUSDT | 8 | `pdi_low_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.0540 | 0.6726 | 3.8199 | 0.0164 | 0.3929 | EBR>35% | RAN |
| SOLUSDT | 4 | `pdi_low_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.0163 | 0.6707 | 3.7076 | 0.0160 | 0.3952 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `pdi_high_at_h` | one_head_filter_pi_star | 133 | 10.9753 | 1.3443 | 0.6316 | 1.3826 | 0.0103 | 0.2105 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `pdi_cross_up_25` | one_head_filter_pi_star | 22 | 2.0133 | 1.5200 | 0.6364 | 0.8246 | 0.0087 | 0.2727 | TPM<MIN | RAN |
| ETHUSDT | 8 | `pdi_high_at_h` | one_head_filter_pi_star | 115 | 9.4900 | 1.2125 | 0.6087 | 0.8468 | 0.0069 | 0.2087 | ok | RAN |
| SOLUSDT | 8 | `pdi_high_at_h` | one_head_filter_pi_star | 113 | 9.4371 | 1.4205 | 0.6195 | 1.7197 | 0.0064 | 0.3097 | ok | RAN |
| SOLUSDT | 4 | `pdi_high_at_h` | one_head_filter_pi_star | 171 | 13.9434 | 1.4225 | 0.5965 | 2.0801 | 0.0061 | 0.2690 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `pdi_high_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `pdi_high_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `pdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `pdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `pdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `pdi_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `pdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `pdi_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `pdi_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `pdi_cross_up_25` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `pdi_cross_down_20` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
