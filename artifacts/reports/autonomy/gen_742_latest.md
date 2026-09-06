# Autonomy public-indicator hunt gen 742

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T101338Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma370_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9193 | 0.6882 | 4.2177 | 0.0224 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma370_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9034 | 0.6878 | 4.1780 | 0.0220 | 0.3862 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma370_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2019 | 0.6914 | 4.3326 | 0.0168 | 0.3886 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma370_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1780 | 0.6923 | 4.0762 | 0.0163 | 0.3787 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma370_above_at_h` | one_head_filter_pi_star | 196 | 16.1109 | 1.2861 | 0.6071 | 1.4814 | 0.0099 | 0.2296 | ok | RAN |
| ETHUSDT | 4 | `wma370_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.2626 | 0.6127 | 1.3121 | 0.0090 | 0.2197 | ok | RAN |
| SOLUSDT | 8 | `wma370_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4428 | 0.6062 | 2.1972 | 0.0068 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `wma370_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4207 | 0.6073 | 2.0618 | 0.0065 | 0.2618 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma370_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma370_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma370_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma370_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
