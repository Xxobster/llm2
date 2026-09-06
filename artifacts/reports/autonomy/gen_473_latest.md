# Autonomy public-indicator hunt gen 473

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T160908Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema740_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.8937 | 0.6683 | 3.7366 | 0.0206 | 0.3819 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema740_below_at_h` | one_head_filter_pi_star | 217 | 17.7269 | 1.8520 | 0.6820 | 3.9045 | 0.0205 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `ema740_below_at_h` | one_head_filter_pi_star | 231 | 18.8891 | 1.7887 | 0.6580 | 3.6996 | 0.0121 | 0.3203 | GATE_CAND | RAN |
| SOLUSDT | 4 | `ema740_below_at_h` | one_head_filter_pi_star | 227 | 18.5620 | 1.7947 | 0.6476 | 3.6597 | 0.0120 | 0.3084 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema740_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.6680 | 0.6475 | 2.5327 | 0.0100 | 0.3165 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema740_above_at_h` | one_head_filter_pi_star | 124 | 10.3060 | 1.6445 | 0.6290 | 2.3593 | 0.0099 | 0.3306 | ok | RAN |
| ETHUSDT | 8 | `ema740_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.2094 | 0.6115 | 0.9949 | 0.0077 | 0.2102 | ok | RAN |
| ETHUSDT | 4 | `ema740_above_at_h` | one_head_filter_pi_star | 161 | 13.2340 | 1.1722 | 0.5963 | 0.8492 | 0.0064 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema740_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.6188 | 0.3684 | -0.7870 | -0.0400 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema740_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema740_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema740_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema740_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
