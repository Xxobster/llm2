# Autonomy public-indicator hunt gen 644

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T032040Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema565_below_at_h` | one_head_filter_pi_star | 203 | 16.5832 | 1.8694 | 0.6700 | 3.8990 | 0.0213 | 0.3842 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema565_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8366 | 0.6732 | 3.8719 | 0.0205 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema565_below_at_h` | one_head_filter_pi_star | 214 | 17.4990 | 1.8460 | 0.6589 | 3.7449 | 0.0127 | 0.3224 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema565_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8504 | 0.6569 | 3.7329 | 0.0127 | 0.3382 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema565_above_at_h` | one_head_filter_pi_star | 165 | 13.5308 | 1.6439 | 0.6242 | 2.6835 | 0.0099 | 0.3030 | ok | RAN |
| SOLUSDT | 8 | `ema565_above_at_h` | one_head_filter_pi_star | 157 | 12.8018 | 1.5383 | 0.6115 | 2.2502 | 0.0085 | 0.2803 | ok | RAN |
| ETHUSDT | 8 | `ema565_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2195 | 0.6111 | 1.0610 | 0.0077 | 0.2099 | ok | RAN |
| ETHUSDT | 4 | `ema565_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1168 | 0.5951 | 0.5843 | 0.0045 | 0.1963 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema565_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema565_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema565_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema565_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema565_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema565_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
