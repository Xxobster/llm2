# Autonomy public-indicator hunt gen 348

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T145029Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema195_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0282 | 0.6959 | 4.5907 | 0.0235 | 0.3763 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema195_below_at_h` | one_head_filter_pi_star | 193 | 15.7663 | 1.9882 | 0.6995 | 4.3727 | 0.0232 | 0.3731 | EBR>35% | RAN |
| SOLUSDT | 8 | `ema195_below_at_h` | one_head_filter_pi_star | 176 | 14.3917 | 2.3656 | 0.7045 | 4.6458 | 0.0188 | 0.3807 | EBR>35% | RAN |
| SOLUSDT | 4 | `ema195_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1887 | 0.6964 | 4.1433 | 0.0167 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `ema195_above_at_h` | one_head_filter_pi_star | 180 | 14.8539 | 1.2162 | 0.6000 | 1.0880 | 0.0075 | 0.2111 | ok | RAN |
| ETHUSDT | 4 | `ema195_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.1510 | 0.5895 | 0.7897 | 0.0054 | 0.2263 | ok | RAN |
| SOLUSDT | 4 | `ema195_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3455 | 0.5879 | 1.7908 | 0.0053 | 0.2613 | ok | RAN |
| SOLUSDT | 8 | `ema195_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3047 | 0.5938 | 1.5862 | 0.0049 | 0.2604 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema195_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema195_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema195_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema195_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema195_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema195_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
