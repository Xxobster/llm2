# Autonomy public-indicator hunt gen 1534

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T060015Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma417_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9532 | 0.6927 | 4.3260 | 0.0228 | 0.3906 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma417_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9157 | 0.6947 | 4.1761 | 0.0218 | 0.3895 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma417_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2455 | 0.6971 | 4.4634 | 0.0172 | 0.3829 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma417_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1962 | 0.6944 | 4.3154 | 0.0166 | 0.3778 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma417_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2345 | 0.5979 | 1.2183 | 0.0082 | 0.2275 | ok | RAN |
| ETHUSDT | 8 | `wma417_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.1928 | 0.5990 | 1.0258 | 0.0067 | 0.2183 | ok | RAN |
| SOLUSDT | 8 | `wma417_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.3822 | 0.6054 | 1.8995 | 0.0060 | 0.2649 | ok | RAN |
| SOLUSDT | 4 | `wma417_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.3718 | 0.6000 | 1.8720 | 0.0058 | 0.2615 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma417_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma417_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma417_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma417_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma417_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma417_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma417_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma417_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma417_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma417_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma417_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma417_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma417_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma417_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma417_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma417_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
