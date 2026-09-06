# Autonomy public-indicator hunt gen 172

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T204640Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema40_cross_up` | one_head_filter_pi_star | 18 | 1.5389 | 17.6605 | 0.8333 | 3.3881 | 0.0639 | 0.3333 | TPM<MIN | RAN |
| SOLUSDT | 8 | `ema40_cross_down` | one_head_filter_pi_star | 23 | 1.9630 | 4.7688 | 0.8261 | 2.6253 | 0.0373 | 0.1739 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema40_cross_down` | one_head_filter_pi_star | 15 | 1.8244 | 2.2344 | 0.6000 | 1.7690 | 0.0343 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema40_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8105 | 0.6820 | 3.9263 | 0.0210 | 0.3733 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema40_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.7462 | 0.6728 | 3.6713 | 0.0197 | 0.3733 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema40_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1210 | 0.6790 | 3.9097 | 0.0172 | 0.4136 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema40_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.1245 | 0.6810 | 3.9158 | 0.0172 | 0.4172 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema40_above_at_h` | one_head_filter_pi_star | 161 | 13.2859 | 1.2737 | 0.6025 | 1.2528 | 0.0083 | 0.2112 | ok | RAN |
| ETHUSDT | 4 | `ema40_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2351 | 0.6038 | 1.0680 | 0.0073 | 0.2138 | ok | RAN |
| ETHUSDT | 8 | `ema40_cross_up` | one_head_filter_pi_star | 22 | 1.8824 | 1.1821 | 0.5455 | 0.3273 | 0.0066 | 0.2727 | TPM<MIN | RAN |
| SOLUSDT | 4 | `ema40_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3800 | 0.6037 | 2.0439 | 0.0056 | 0.2442 | ok | RAN |
| SOLUSDT | 8 | `ema40_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3477 | 0.5943 | 1.8899 | 0.0051 | 0.2453 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema40_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema40_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `ema40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema40_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema40_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema40_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema40_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
