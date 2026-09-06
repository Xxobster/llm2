# Autonomy public-indicator hunt gen 619

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T014425Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma358_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9763 | 0.6979 | 4.4011 | 0.0228 | 0.3750 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma358_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9526 | 0.6931 | 4.2843 | 0.0224 | 0.3757 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma358_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 2.1191 | 0.6778 | 4.3188 | 0.0161 | 0.3778 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma358_below_at_h` | one_head_filter_pi_star | 185 | 15.1276 | 2.1473 | 0.6919 | 4.2963 | 0.0160 | 0.3730 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma358_above_at_h` | one_head_filter_pi_star | 185 | 15.0850 | 1.5572 | 0.6162 | 2.5947 | 0.0085 | 0.2703 | ok | RAN |
| SOLUSDT | 4 | `sma358_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.5057 | 0.6042 | 2.4059 | 0.0079 | 0.2656 | ok | RAN |
| ETHUSDT | 4 | `sma358_above_at_h` | one_head_filter_pi_star | 198 | 16.2753 | 1.2142 | 0.5909 | 1.1642 | 0.0076 | 0.2172 | ok | RAN |
| ETHUSDT | 8 | `sma358_above_at_h` | one_head_filter_pi_star | 192 | 15.7822 | 1.1729 | 0.5781 | 0.9364 | 0.0061 | 0.2135 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma358_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma358_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma358_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma358_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma358_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma358_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma358_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma358_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma358_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma358_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma358_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma358_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma358_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma358_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma358_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma358_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
