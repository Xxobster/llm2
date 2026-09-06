# Autonomy public-indicator hunt gen 420

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T065532Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema285_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0763 | 0.6974 | 4.6417 | 0.0244 | 0.3795 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema285_below_at_h` | one_head_filter_pi_star | 200 | 16.3382 | 1.7756 | 0.6700 | 3.7809 | 0.0197 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema285_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 2.2107 | 0.6862 | 4.4885 | 0.0170 | 0.3777 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema285_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 2.0132 | 0.6684 | 4.0940 | 0.0150 | 0.3520 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema285_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.3379 | 0.6270 | 1.6792 | 0.0109 | 0.2162 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema285_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.5909 | 0.6223 | 2.7101 | 0.0087 | 0.2660 | ok | RAN |
| ETHUSDT | 4 | `ema285_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2254 | 0.6011 | 1.1350 | 0.0078 | 0.2077 | ok | RAN |
| SOLUSDT | 8 | `ema285_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.2934 | 0.5882 | 1.5252 | 0.0048 | 0.2620 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema285_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema285_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema285_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema285_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema285_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema285_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
