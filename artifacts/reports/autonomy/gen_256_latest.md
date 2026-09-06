# Autonomy public-indicator hunt gen 256

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T022217Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma240_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9569 | 0.6919 | 4.3268 | 0.0233 | 0.3784 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma240_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9347 | 0.6947 | 4.2520 | 0.0225 | 0.3842 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma240_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.3246 | 0.7006 | 4.5701 | 0.0179 | 0.3842 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma240_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1440 | 0.6845 | 3.9847 | 0.0166 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma240_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.2680 | 0.6064 | 1.4023 | 0.0092 | 0.2287 | ok | RAN |
| ETHUSDT | 4 | `sma240_above_at_h` | one_head_filter_pi_star | 204 | 16.7685 | 1.2364 | 0.6029 | 1.2519 | 0.0080 | 0.2255 | ok | RAN |
| SOLUSDT | 4 | `sma240_above_at_h` | one_head_filter_pi_star | 198 | 16.1450 | 1.4466 | 0.6061 | 2.2185 | 0.0068 | 0.2626 | ok | RAN |
| SOLUSDT | 8 | `sma240_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.3451 | 0.5947 | 1.7598 | 0.0055 | 0.2632 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma240_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma240_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma240_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma240_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma240_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
