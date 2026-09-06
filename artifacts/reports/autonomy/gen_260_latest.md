# Autonomy public-indicator hunt gen 260

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T023956Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `ema95_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 2.0900 | 0.7068 | 4.7482 | 0.0253 | 0.3717 | EBR>35% | RAN |
| ETHUSDT | 4 | `ema95_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.8827 | 0.6818 | 4.1919 | 0.0215 | 0.3737 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema95_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1921 | 0.6867 | 4.1464 | 0.0178 | 0.3916 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema95_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.2409 | 0.6959 | 4.2984 | 0.0178 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `ema95_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2583 | 0.6096 | 1.2565 | 0.0085 | 0.2193 | ok | RAN |
| ETHUSDT | 8 | `ema95_above_at_h` | one_head_filter_pi_star | 181 | 14.9364 | 1.2031 | 0.6022 | 0.9882 | 0.0066 | 0.2155 | ok | RAN |
| SOLUSDT | 8 | `ema95_above_at_h` | one_head_filter_pi_star | 214 | 17.4496 | 1.3545 | 0.5981 | 1.8688 | 0.0053 | 0.2570 | ok | RAN |
| SOLUSDT | 4 | `ema95_above_at_h` | one_head_filter_pi_star | 205 | 16.7158 | 1.2661 | 0.5805 | 1.4487 | 0.0041 | 0.2585 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema95_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema95_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema95_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema95_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema95_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema95_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
