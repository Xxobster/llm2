# Autonomy public-indicator hunt gen 1246

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T145955Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma685_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0196 | 0.6853 | 4.4353 | 0.0232 | 0.3706 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma685_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9964 | 0.6984 | 4.3133 | 0.0229 | 0.3810 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma685_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7996 | 0.6585 | 3.5100 | 0.0121 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma685_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7907 | 0.6497 | 3.4776 | 0.0118 | 0.3299 | GATE_CAND | RAN |
| ETHUSDT | 8 | `wma685_above_at_h` | one_head_filter_pi_star | 162 | 13.3162 | 1.2929 | 0.6049 | 1.3939 | 0.0101 | 0.2160 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma685_above_at_h` | one_head_filter_pi_star | 180 | 14.6773 | 1.5096 | 0.6111 | 2.3835 | 0.0083 | 0.2667 | ok | RAN |
| SOLUSDT | 4 | `wma685_above_at_h` | one_head_filter_pi_star | 165 | 13.4542 | 1.5177 | 0.6061 | 2.2587 | 0.0081 | 0.2848 | ok | RAN |
| ETHUSDT | 4 | `wma685_above_at_h` | one_head_filter_pi_star | 188 | 15.5140 | 1.2060 | 0.5957 | 1.0970 | 0.0072 | 0.2074 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma685_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma685_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma685_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma685_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma685_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma685_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
