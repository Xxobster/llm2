# Autonomy public-indicator hunt gen 1430

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T142541Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma401_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 2.0398 | 0.6973 | 4.4226 | 0.0248 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma401_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.8504 | 0.6806 | 4.0647 | 0.0209 | 0.3770 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma401_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.2116 | 0.6932 | 4.3948 | 0.0172 | 0.3920 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma401_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.1239 | 0.6897 | 4.0801 | 0.0160 | 0.3678 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma401_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.3010 | 0.6054 | 1.5261 | 0.0103 | 0.2270 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma401_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.2750 | 0.5990 | 1.4002 | 0.0093 | 0.2344 | ok | RAN |
| SOLUSDT | 8 | `wma401_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4090 | 0.6114 | 2.0598 | 0.0063 | 0.2591 | ok | RAN |
| SOLUSDT | 4 | `wma401_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3481 | 0.5928 | 1.7849 | 0.0056 | 0.2732 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma401_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma401_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma401_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma401_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma401_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma401_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma401_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma401_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma401_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma401_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma401_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma401_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma401_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma401_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma401_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma401_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
