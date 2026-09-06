# Autonomy public-indicator hunt gen 635

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T024550Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma370_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0541 | 0.7049 | 4.5030 | 0.0242 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma370_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9174 | 0.6919 | 4.1264 | 0.0221 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma370_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.0746 | 0.6813 | 3.9942 | 0.0149 | 0.3626 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma370_below_at_h` | one_head_filter_pi_star | 186 | 15.2094 | 2.0313 | 0.6774 | 3.9835 | 0.0145 | 0.3548 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma370_above_at_h` | one_head_filter_pi_star | 200 | 16.4397 | 1.2598 | 0.6000 | 1.3614 | 0.0091 | 0.2300 | ok | RAN |
| SOLUSDT | 4 | `sma370_above_at_h` | one_head_filter_pi_star | 186 | 15.1665 | 1.5799 | 0.6183 | 2.6364 | 0.0088 | 0.2688 | ok | RAN |
| SOLUSDT | 8 | `sma370_above_at_h` | one_head_filter_pi_star | 190 | 15.4927 | 1.5129 | 0.6053 | 2.4159 | 0.0079 | 0.2737 | ok | RAN |
| ETHUSDT | 8 | `sma370_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2208 | 0.5939 | 1.1730 | 0.0079 | 0.2234 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma370_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma370_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma370_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma370_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma370_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma370_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
