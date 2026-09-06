# Autonomy public-indicator hunt gen 1379

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T034152Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma656_below_at_h` | one_head_filter_pi_star | 192 | 15.6846 | 1.9637 | 0.6771 | 4.1888 | 0.0229 | 0.3802 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma656_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9233 | 0.6718 | 4.1681 | 0.0224 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma656_below_at_h` | one_head_filter_pi_star | 196 | 15.9450 | 1.7849 | 0.6633 | 3.3907 | 0.0120 | 0.3316 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma656_below_at_h` | one_head_filter_pi_star | 209 | 17.0026 | 1.7591 | 0.6603 | 3.4416 | 0.0113 | 0.3206 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma656_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.6650 | 0.6329 | 2.6987 | 0.0101 | 0.3038 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma656_above_at_h` | one_head_filter_pi_star | 113 | 9.2666 | 1.6660 | 0.6195 | 2.3766 | 0.0097 | 0.3274 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma656_above_at_h` | one_head_filter_pi_star | 145 | 11.9656 | 1.2221 | 0.6138 | 1.0523 | 0.0078 | 0.2138 | ok | RAN |
| ETHUSDT | 8 | `sma656_above_at_h` | one_head_filter_pi_star | 145 | 11.9188 | 1.2148 | 0.6000 | 1.0152 | 0.0077 | 0.2207 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma656_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma656_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma656_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma656_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma656_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma656_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma656_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma656_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma656_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma656_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma656_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma656_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma656_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma656_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma656_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma656_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
