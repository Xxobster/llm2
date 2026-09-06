# Autonomy public-indicator hunt gen 476

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T162103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema355_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 2.0092 | 0.6947 | 4.3951 | 0.0229 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema355_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9638 | 0.6875 | 4.2328 | 0.0226 | 0.3698 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema355_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.8902 | 0.6584 | 3.8217 | 0.0139 | 0.3614 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema355_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8100 | 0.6550 | 3.5555 | 0.0124 | 0.3450 | GATE_CAND | RAN |
| ETHUSDT | 8 | `ema355_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.3006 | 0.6264 | 1.5045 | 0.0103 | 0.2253 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema355_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.2287 | 0.6023 | 1.1605 | 0.0081 | 0.2159 | ok | RAN |
| SOLUSDT | 8 | `ema355_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.5040 | 0.6201 | 2.3688 | 0.0079 | 0.2737 | ok | RAN |
| SOLUSDT | 4 | `ema355_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.4899 | 0.6108 | 2.3414 | 0.0078 | 0.2703 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema355_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema355_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema355_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema355_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema355_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema355_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
