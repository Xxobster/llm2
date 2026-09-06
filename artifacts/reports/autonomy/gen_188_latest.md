# Autonomy public-indicator hunt gen 188

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T214713Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `ema32_cross_down` | one_head_filter_pi_star | 27 | 2.2906 | 2.7730 | 0.7778 | 2.0583 | 0.0223 | 0.1111 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema32_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.7789 | 0.6742 | 3.8316 | 0.0205 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema32_below_at_h` | one_head_filter_pi_star | 219 | 17.8903 | 1.7480 | 0.6712 | 3.7425 | 0.0197 | 0.3653 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema32_below_at_h` | one_head_filter_pi_star | 162 | 13.2469 | 2.1523 | 0.6852 | 3.9861 | 0.0175 | 0.4198 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema32_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1137 | 0.6832 | 3.8819 | 0.0171 | 0.4224 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema32_cross_down` | one_head_filter_pi_star | 12 | 1.4595 | 1.8476 | 0.5000 | 1.0271 | 0.0169 | 0.2500 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema32_cross_up` | one_head_filter_pi_star | 22 | 1.8824 | 1.2593 | 0.5455 | 0.4674 | 0.0096 | 0.2273 | TPM<MIN | RAN |
| ETHUSDT | 8 | `ema32_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.2111 | 0.5975 | 0.9672 | 0.0066 | 0.2075 | ok | RAN |
| ETHUSDT | 4 | `ema32_above_at_h` | one_head_filter_pi_star | 160 | 13.2034 | 1.2067 | 0.5938 | 0.9491 | 0.0065 | 0.2062 | ok | RAN |
| SOLUSDT | 4 | `ema32_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3744 | 0.6019 | 2.0172 | 0.0055 | 0.2454 | ok | RAN |
| SOLUSDT | 8 | `ema32_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3427 | 0.5981 | 1.8587 | 0.0050 | 0.2477 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema32_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema32_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `ema32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `ema32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema32_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema32_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema32_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema32_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
