# Autonomy public-indicator hunt gen 329

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T114509Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema380_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8645 | 0.6683 | 4.0219 | 0.0214 | 0.3610 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema380_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.8747 | 0.6821 | 4.1058 | 0.0213 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema380_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.8845 | 0.6587 | 3.8355 | 0.0136 | 0.3510 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema380_below_at_h` | one_head_filter_pi_star | 208 | 17.0083 | 1.8895 | 0.6635 | 3.8036 | 0.0135 | 0.3365 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema380_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.2911 | 0.6163 | 1.3778 | 0.0099 | 0.2209 | ok | RAN |
| SOLUSDT | 4 | `ema380_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.5854 | 0.6175 | 2.7105 | 0.0091 | 0.2732 | ok | RAN |
| ETHUSDT | 4 | `ema380_above_at_h` | one_head_filter_pi_star | 169 | 13.9461 | 1.2460 | 0.6095 | 1.2247 | 0.0087 | 0.2071 | ok | RAN |
| SOLUSDT | 8 | `ema380_above_at_h` | one_head_filter_pi_star | 178 | 14.5142 | 1.5083 | 0.6180 | 2.3406 | 0.0080 | 0.2697 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema380_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema380_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema380_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema380_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema380_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
