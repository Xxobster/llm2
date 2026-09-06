# Autonomy public-indicator hunt gen 395

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T010728Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma172_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.9712 | 0.6915 | 4.4070 | 0.0233 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma172_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.7604 | 0.6720 | 3.6899 | 0.0194 | 0.3651 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma172_below_at_h` | one_head_filter_pi_star | 173 | 14.1464 | 2.2531 | 0.6994 | 4.3743 | 0.0175 | 0.3815 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma172_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2216 | 0.6928 | 4.1627 | 0.0175 | 0.3855 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma172_above_at_h` | one_head_filter_pi_star | 186 | 15.3490 | 1.3458 | 0.6075 | 1.6476 | 0.0111 | 0.2151 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma172_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2830 | 0.6062 | 1.3827 | 0.0093 | 0.2176 | ok | RAN |
| SOLUSDT | 4 | `sma172_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.3685 | 0.5971 | 1.9152 | 0.0058 | 0.2573 | ok | RAN |
| SOLUSDT | 8 | `sma172_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.3036 | 0.5813 | 1.6180 | 0.0048 | 0.2611 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma172_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma172_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma172_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma172_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma172_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma172_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma172_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma172_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma172_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma172_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma172_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma172_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma172_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma172_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma172_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma172_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
