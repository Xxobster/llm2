# Autonomy public-indicator hunt gen 452

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T144913Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema325_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9627 | 0.6853 | 4.2456 | 0.0227 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema325_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 1.9278 | 0.6904 | 4.2454 | 0.0221 | 0.3858 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema325_below_at_h` | one_head_filter_pi_star | 191 | 15.6182 | 2.0397 | 0.6806 | 4.1132 | 0.0152 | 0.3717 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema325_below_at_h` | one_head_filter_pi_star | 192 | 15.7000 | 1.9606 | 0.6667 | 3.9116 | 0.0144 | 0.3542 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema325_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2408 | 0.6096 | 1.2636 | 0.0084 | 0.2193 | ok | RAN |
| SOLUSDT | 8 | `ema325_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5680 | 0.6216 | 2.6255 | 0.0084 | 0.2649 | ok | RAN |
| SOLUSDT | 4 | `ema325_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5219 | 0.6099 | 2.4040 | 0.0079 | 0.2802 | ok | RAN |
| ETHUSDT | 4 | `ema325_above_at_h` | one_head_filter_pi_star | 177 | 14.6063 | 1.1755 | 0.5932 | 0.9270 | 0.0063 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema325_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema325_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema325_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema325_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema325_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema325_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
