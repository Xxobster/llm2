# Autonomy public-indicator hunt gen 1286

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T185149Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma710_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0486 | 0.6968 | 4.5025 | 0.0235 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma710_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9893 | 0.6856 | 4.3495 | 0.0233 | 0.3814 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma710_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.8323 | 0.6650 | 3.6059 | 0.0125 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma710_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8001 | 0.6633 | 3.5083 | 0.0122 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `wma710_above_at_h` | one_head_filter_pi_star | 188 | 15.3296 | 1.6119 | 0.6170 | 2.7517 | 0.0094 | 0.2713 | ok | RAN |
| SOLUSDT | 4 | `wma710_above_at_h` | one_head_filter_pi_star | 175 | 14.2696 | 1.5478 | 0.6171 | 2.4915 | 0.0088 | 0.2971 | ok | RAN |
| ETHUSDT | 8 | `wma710_above_at_h` | one_head_filter_pi_star | 178 | 14.6314 | 1.2200 | 0.5955 | 1.1322 | 0.0080 | 0.2079 | ok | RAN |
| ETHUSDT | 4 | `wma710_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.1669 | 0.6032 | 0.8797 | 0.0061 | 0.2116 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma710_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma710_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma710_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma710_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma710_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma710_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
