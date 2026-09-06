# Autonomy public-indicator hunt gen 1134

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T030009Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma615_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.1670 | 0.7083 | 4.8635 | 0.0258 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma615_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 2.1073 | 0.6979 | 4.6488 | 0.0250 | 0.3854 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma615_below_at_h` | one_head_filter_pi_star | 193 | 15.7818 | 1.9646 | 0.6580 | 3.8532 | 0.0140 | 0.3523 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma615_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.9385 | 0.6702 | 3.8276 | 0.0138 | 0.3670 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma615_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.2897 | 0.6150 | 1.4910 | 0.0101 | 0.2299 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma615_above_at_h` | one_head_filter_pi_star | 182 | 14.8404 | 1.5484 | 0.6154 | 2.5448 | 0.0086 | 0.2747 | ok | RAN |
| SOLUSDT | 4 | `wma615_above_at_h` | one_head_filter_pi_star | 176 | 14.3511 | 1.5587 | 0.6136 | 2.5025 | 0.0085 | 0.2841 | ok | RAN |
| ETHUSDT | 4 | `wma615_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.2009 | 0.5968 | 1.0761 | 0.0072 | 0.2204 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma615_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma615_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma615_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma615_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
