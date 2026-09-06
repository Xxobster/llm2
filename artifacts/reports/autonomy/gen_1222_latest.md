# Autonomy public-indicator hunt gen 1222

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T122551Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma670_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.2118 | 0.7112 | 4.9051 | 0.0261 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma670_below_at_h` | one_head_filter_pi_star | 179 | 14.6227 | 2.0116 | 0.6927 | 4.3201 | 0.0235 | 0.3911 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma670_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.9135 | 0.6789 | 3.7278 | 0.0134 | 0.3526 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma670_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7780 | 0.6531 | 3.4390 | 0.0122 | 0.3469 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma670_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.6480 | 0.6229 | 2.8004 | 0.0098 | 0.2914 | ok | RAN |
| SOLUSDT | 8 | `wma670_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5125 | 0.6000 | 2.3176 | 0.0081 | 0.2914 | ok | RAN |
| ETHUSDT | 8 | `wma670_above_at_h` | one_head_filter_pi_star | 180 | 14.7958 | 1.2205 | 0.6056 | 1.1321 | 0.0078 | 0.2167 | ok | RAN |
| ETHUSDT | 4 | `wma670_above_at_h` | one_head_filter_pi_star | 188 | 15.4534 | 1.2166 | 0.5957 | 1.1438 | 0.0075 | 0.2128 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma670_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma670_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma670_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma670_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma670_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma670_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
