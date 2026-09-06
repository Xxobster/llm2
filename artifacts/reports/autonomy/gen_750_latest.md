# Autonomy public-indicator hunt gen 750

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T104818Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma375_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9711 | 0.6952 | 4.3903 | 0.0229 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma375_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.8930 | 0.6865 | 4.0699 | 0.0220 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma375_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.3791 | 0.7069 | 4.6015 | 0.0186 | 0.3908 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma375_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1489 | 0.6914 | 4.1606 | 0.0161 | 0.3714 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma375_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2783 | 0.6073 | 1.4269 | 0.0094 | 0.2304 | ok | RAN |
| ETHUSDT | 8 | `wma375_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2622 | 0.6020 | 1.3738 | 0.0089 | 0.2194 | ok | RAN |
| SOLUSDT | 4 | `wma375_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3400 | 0.5920 | 1.7612 | 0.0054 | 0.2637 | ok | RAN |
| SOLUSDT | 8 | `wma375_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.3080 | 0.5907 | 1.6152 | 0.0050 | 0.2642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma375_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma375_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma375_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma375_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma375_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma375_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
