# Autonomy public-indicator hunt gen 1350

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T010024Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma750_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.1766 | 0.7049 | 4.7281 | 0.0259 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma750_below_at_h` | one_head_filter_pi_star | 207 | 16.9100 | 1.8720 | 0.6618 | 4.1557 | 0.0207 | 0.3671 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `wma750_below_at_h` | one_head_filter_pi_star | 204 | 16.6813 | 1.8924 | 0.6765 | 3.9114 | 0.0132 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 8 | `wma750_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8425 | 0.6700 | 3.6254 | 0.0127 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma750_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.2716 | 0.6013 | 1.2928 | 0.0095 | 0.2278 | ok | RAN |
| SOLUSDT | 4 | `wma750_above_at_h` | one_head_filter_pi_star | 172 | 14.0249 | 1.5816 | 0.6047 | 2.5632 | 0.0092 | 0.2965 | ok | RAN |
| ETHUSDT | 4 | `wma750_above_at_h` | one_head_filter_pi_star | 173 | 14.2762 | 1.2020 | 0.6012 | 1.0562 | 0.0070 | 0.2081 | ok | RAN |
| SOLUSDT | 8 | `wma750_above_at_h` | one_head_filter_pi_star | 167 | 13.6172 | 1.3322 | 0.5868 | 1.5972 | 0.0056 | 0.2874 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma750_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma750_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma750_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma750_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma750_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma750_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
