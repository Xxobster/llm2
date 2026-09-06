# Autonomy public-indicator hunt gen 708

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T074455Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema645_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8344 | 0.6650 | 3.8317 | 0.0197 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema645_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.7149 | 0.6667 | 3.4714 | 0.0178 | 0.3615 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema645_below_at_h` | one_head_filter_pi_star | 219 | 17.9078 | 1.8409 | 0.6621 | 3.7791 | 0.0128 | 0.3242 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema645_below_at_h` | one_head_filter_pi_star | 209 | 17.0901 | 1.8453 | 0.6651 | 3.6930 | 0.0124 | 0.3301 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `ema645_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.6630 | 0.6214 | 2.4676 | 0.0097 | 0.3214 | ok | RAN |
| SOLUSDT | 4 | `ema645_above_at_h` | one_head_filter_pi_star | 137 | 11.2347 | 1.4991 | 0.6204 | 1.9868 | 0.0079 | 0.3285 | ok | RAN |
| ETHUSDT | 4 | `ema645_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.2212 | 0.6051 | 1.0513 | 0.0079 | 0.2038 | ok | RAN |
| ETHUSDT | 8 | `ema645_above_at_h` | one_head_filter_pi_star | 141 | 11.6355 | 1.1869 | 0.6099 | 0.8780 | 0.0068 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema645_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema645_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema645_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema645_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
