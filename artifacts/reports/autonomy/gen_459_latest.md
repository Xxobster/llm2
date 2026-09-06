# Autonomy public-indicator hunt gen 459

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T151557Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma226_below_at_h` | one_head_filter_pi_star | 181 | 14.7860 | 2.1728 | 0.7127 | 4.8605 | 0.0261 | 0.3923 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma226_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 1.9926 | 0.6983 | 4.3350 | 0.0233 | 0.3966 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma226_below_at_h` | one_head_filter_pi_star | 174 | 14.2281 | 2.3185 | 0.7011 | 4.5340 | 0.0177 | 0.3908 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma226_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.1239 | 0.6786 | 3.9914 | 0.0160 | 0.3690 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma226_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.3148 | 0.6073 | 1.6107 | 0.0104 | 0.2304 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma226_above_at_h` | one_head_filter_pi_star | 196 | 16.1742 | 1.2421 | 0.5969 | 1.2799 | 0.0084 | 0.2245 | ok | RAN |
| SOLUSDT | 8 | `sma226_above_at_h` | one_head_filter_pi_star | 196 | 15.9819 | 1.3455 | 0.5969 | 1.7872 | 0.0055 | 0.2653 | ok | RAN |
| SOLUSDT | 4 | `sma226_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3247 | 0.5885 | 1.6695 | 0.0052 | 0.2656 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma226_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma226_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma226_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma226_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma226_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma226_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma226_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma226_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma226_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma226_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma226_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma226_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma226_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma226_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma226_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma226_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
