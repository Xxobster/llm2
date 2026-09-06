# Autonomy public-indicator hunt gen 499

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T175103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma256_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9986 | 0.7027 | 4.3318 | 0.0239 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma256_below_at_h` | one_head_filter_pi_star | 185 | 15.1128 | 1.9324 | 0.6919 | 4.1790 | 0.0225 | 0.3784 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma256_below_at_h` | one_head_filter_pi_star | 167 | 13.6557 | 2.2261 | 0.6946 | 4.1830 | 0.0172 | 0.3772 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma256_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1235 | 0.6867 | 4.0336 | 0.0163 | 0.3735 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `sma256_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.3148 | 0.6117 | 1.5950 | 0.0103 | 0.2287 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma256_above_at_h` | one_head_filter_pi_star | 193 | 15.9266 | 1.2247 | 0.5959 | 1.1443 | 0.0077 | 0.2280 | ok | RAN |
| SOLUSDT | 4 | `sma256_above_at_h` | one_head_filter_pi_star | 199 | 16.2265 | 1.3427 | 0.5930 | 1.7508 | 0.0055 | 0.2613 | ok | RAN |
| SOLUSDT | 8 | `sma256_above_at_h` | one_head_filter_pi_star | 189 | 15.4111 | 1.2944 | 0.5926 | 1.5299 | 0.0048 | 0.2593 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma256_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma256_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma256_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma256_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma256_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma256_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma256_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma256_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma256_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma256_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma256_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma256_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma256_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma256_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma256_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma256_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
