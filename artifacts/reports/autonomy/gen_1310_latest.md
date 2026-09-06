# Autonomy public-indicator hunt gen 1310

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T211858Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma725_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.2228 | 0.7128 | 4.9550 | 0.0262 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma725_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9591 | 0.6825 | 4.2165 | 0.0225 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma725_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.9084 | 0.6749 | 3.8580 | 0.0134 | 0.3399 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma725_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8301 | 0.6601 | 3.5951 | 0.0125 | 0.3300 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma725_above_at_h` | one_head_filter_pi_star | 177 | 14.4326 | 1.5985 | 0.6158 | 2.5897 | 0.0090 | 0.2881 | ok | RAN |
| ETHUSDT | 8 | `wma725_above_at_h` | one_head_filter_pi_star | 183 | 15.0424 | 1.2460 | 0.6120 | 1.2561 | 0.0085 | 0.2186 | ok | RAN |
| SOLUSDT | 8 | `wma725_above_at_h` | one_head_filter_pi_star | 181 | 14.7588 | 1.5308 | 0.6077 | 2.4247 | 0.0083 | 0.2818 | ok | RAN |
| ETHUSDT | 4 | `wma725_above_at_h` | one_head_filter_pi_star | 177 | 14.5492 | 1.1456 | 0.5932 | 0.7891 | 0.0054 | 0.2203 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma725_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma725_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma725_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma725_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma725_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma725_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
