# Autonomy public-indicator hunt gen 273

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T033426Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema240_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9976 | 0.7005 | 4.4709 | 0.0231 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema240_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9541 | 0.6973 | 4.1803 | 0.0227 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema240_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.2818 | 0.7027 | 4.6308 | 0.0178 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema240_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.0345 | 0.6816 | 3.9559 | 0.0153 | 0.3631 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema240_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.4272 | 0.6032 | 2.0658 | 0.0066 | 0.2646 | ok | RAN |
| ETHUSDT | 8 | `ema240_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.1829 | 0.6011 | 0.9761 | 0.0064 | 0.2181 | ok | RAN |
| SOLUSDT | 8 | `ema240_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.3839 | 0.6099 | 1.9140 | 0.0061 | 0.2637 | ok | RAN |
| ETHUSDT | 4 | `ema240_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.1407 | 0.5928 | 0.7541 | 0.0051 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema240_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema240_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
