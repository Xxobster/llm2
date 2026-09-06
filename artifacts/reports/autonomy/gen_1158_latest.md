# Autonomy public-indicator hunt gen 1158

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T055828Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma630_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 2.1436 | 0.7090 | 4.7820 | 0.0251 | 0.3757 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma630_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0233 | 0.6990 | 4.4703 | 0.0236 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma630_below_at_h` | one_head_filter_pi_star | 190 | 15.5365 | 1.8905 | 0.6684 | 3.7149 | 0.0135 | 0.3632 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma630_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.8477 | 0.6601 | 3.6945 | 0.0129 | 0.3399 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma630_above_at_h` | one_head_filter_pi_star | 187 | 15.2481 | 1.5096 | 0.6096 | 2.3840 | 0.0080 | 0.2674 | ok | RAN |
| SOLUSDT | 4 | `wma630_above_at_h` | one_head_filter_pi_star | 179 | 14.5957 | 1.4976 | 0.6089 | 2.3371 | 0.0079 | 0.2737 | ok | RAN |
| ETHUSDT | 8 | `wma630_above_at_h` | one_head_filter_pi_star | 165 | 13.6160 | 1.2059 | 0.6000 | 1.0381 | 0.0073 | 0.2061 | ok | RAN |
| ETHUSDT | 4 | `wma630_above_at_h` | one_head_filter_pi_star | 184 | 15.1839 | 1.2003 | 0.5978 | 1.0665 | 0.0070 | 0.2174 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma630_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma630_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma630_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma630_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma630_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma630_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
