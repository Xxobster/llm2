# Autonomy public-indicator hunt gen 798

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T152920Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma405_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9470 | 0.6895 | 4.3006 | 0.0227 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma405_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9062 | 0.6878 | 4.1502 | 0.0223 | 0.3810 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma405_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2921 | 0.6941 | 4.3861 | 0.0178 | 0.4000 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma405_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.2082 | 0.6971 | 4.2888 | 0.0169 | 0.3829 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma405_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2753 | 0.6000 | 1.4075 | 0.0093 | 0.2211 | ok | RAN |
| ETHUSDT | 4 | `wma405_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2611 | 0.5969 | 1.3484 | 0.0087 | 0.2251 | ok | RAN |
| SOLUSDT | 4 | `wma405_above_at_h` | one_head_filter_pi_star | 212 | 17.2866 | 1.3701 | 0.5943 | 1.9440 | 0.0059 | 0.2642 | ok | RAN |
| SOLUSDT | 8 | `wma405_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.3436 | 0.6096 | 1.7289 | 0.0055 | 0.2620 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma405_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.7517 | 0.3333 | -0.4636 | -0.0208 | 0.0556 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma405_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma405_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma405_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma405_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma405_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
