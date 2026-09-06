# Autonomy public-indicator hunt gen 1139

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T033428Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma617_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0597 | 0.6853 | 4.4342 | 0.0243 | 0.3807 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma617_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.0081 | 0.6834 | 4.3082 | 0.0237 | 0.3920 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma617_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8367 | 0.6786 | 3.6430 | 0.0127 | 0.3418 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma617_below_at_h` | one_head_filter_pi_star | 206 | 16.8448 | 1.8031 | 0.6650 | 3.5706 | 0.0122 | 0.3204 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma617_above_at_h` | one_head_filter_pi_star | 179 | 14.7136 | 1.2665 | 0.6201 | 1.3100 | 0.0095 | 0.2179 | ok | RAN |
| SOLUSDT | 8 | `sma617_above_at_h` | one_head_filter_pi_star | 131 | 10.7426 | 1.5710 | 0.6183 | 2.2378 | 0.0089 | 0.3282 | ok | RAN |
| SOLUSDT | 4 | `sma617_above_at_h` | one_head_filter_pi_star | 145 | 11.8907 | 1.5416 | 0.6138 | 2.1717 | 0.0086 | 0.3310 | ok | RAN |
| ETHUSDT | 8 | `sma617_above_at_h` | one_head_filter_pi_star | 167 | 13.7272 | 1.1486 | 0.5928 | 0.7757 | 0.0057 | 0.2275 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma617_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma617_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma617_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma617_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma617_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma617_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma617_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma617_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma617_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma617_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma617_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma617_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma617_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma617_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma617_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma617_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
