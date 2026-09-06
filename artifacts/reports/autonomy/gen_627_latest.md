# Autonomy public-indicator hunt gen 627

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T021457Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma364_below_at_h` | one_head_filter_pi_star | 178 | 14.5410 | 2.2079 | 0.7022 | 4.8052 | 0.0266 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma364_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9523 | 0.6963 | 4.2927 | 0.0225 | 0.3822 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma364_below_at_h` | one_head_filter_pi_star | 179 | 14.6370 | 2.1047 | 0.6872 | 4.1078 | 0.0156 | 0.3631 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma364_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 1.9171 | 0.6667 | 3.7580 | 0.0141 | 0.3672 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma364_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2599 | 0.6010 | 1.3499 | 0.0089 | 0.2228 | ok | RAN |
| ETHUSDT | 4 | `sma364_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2529 | 0.5918 | 1.3387 | 0.0087 | 0.2296 | ok | RAN |
| SOLUSDT | 4 | `sma364_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.5269 | 0.6073 | 2.4967 | 0.0083 | 0.2670 | ok | RAN |
| SOLUSDT | 8 | `sma364_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5160 | 0.6150 | 2.4233 | 0.0080 | 0.2674 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma364_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma364_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma364_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma364_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma364_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma364_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma364_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma364_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma364_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma364_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma364_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma364_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma364_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma364_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma364_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma364_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
