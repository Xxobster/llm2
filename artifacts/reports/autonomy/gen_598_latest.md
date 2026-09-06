# Autonomy public-indicator hunt gen 598

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T002440Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma280_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.2264 | 0.7174 | 4.9264 | 0.0266 | 0.3859 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma280_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.0723 | 0.7059 | 4.7074 | 0.0243 | 0.3850 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma280_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.2122 | 0.6923 | 4.1669 | 0.0173 | 0.3728 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma280_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.0767 | 0.6805 | 3.8977 | 0.0158 | 0.3728 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma280_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1685 | 0.5938 | 0.8809 | 0.0061 | 0.2240 | ok | RAN |
| SOLUSDT | 4 | `wma280_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3260 | 0.5857 | 1.7416 | 0.0051 | 0.2571 | ok | RAN |
| SOLUSDT | 8 | `wma280_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3126 | 0.5876 | 1.6287 | 0.0049 | 0.2629 | ok | RAN |
| ETHUSDT | 8 | `wma280_above_at_h` | one_head_filter_pi_star | 197 | 16.2567 | 1.1034 | 0.5736 | 0.5599 | 0.0038 | 0.2284 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma280_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma280_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma280_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma280_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma280_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
