# Autonomy public-indicator hunt gen 582

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T232103Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma270_below_at_h` | one_head_filter_pi_star | 184 | 15.0311 | 2.1393 | 0.7120 | 4.8332 | 0.0255 | 0.3804 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma270_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9141 | 0.6923 | 4.1810 | 0.0224 | 0.3795 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma270_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.2248 | 0.6928 | 4.2192 | 0.0176 | 0.3795 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma270_below_at_h` | one_head_filter_pi_star | 170 | 13.9010 | 2.2274 | 0.6941 | 4.3158 | 0.0173 | 0.3765 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma270_above_at_h` | one_head_filter_pi_star | 203 | 16.6863 | 1.1533 | 0.5862 | 0.8247 | 0.0055 | 0.2315 | ok | RAN |
| ETHUSDT | 4 | `wma270_above_at_h` | one_head_filter_pi_star | 201 | 16.5219 | 1.1491 | 0.5920 | 0.8120 | 0.0053 | 0.2289 | ok | RAN |
| SOLUSDT | 4 | `wma270_above_at_h` | one_head_filter_pi_star | 201 | 16.3896 | 1.3382 | 0.5920 | 1.7563 | 0.0053 | 0.2537 | ok | RAN |
| SOLUSDT | 8 | `wma270_above_at_h` | one_head_filter_pi_star | 203 | 16.5527 | 1.2967 | 0.5862 | 1.5806 | 0.0047 | 0.2660 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma270_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma270_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma270_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma270_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma270_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma270_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma270_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma270_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma270_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma270_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma270_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma270_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma270_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma270_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma270_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma270_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
