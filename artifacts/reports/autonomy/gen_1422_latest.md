# Autonomy public-indicator hunt gen 1422

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T102416Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma795_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 1.9907 | 0.6856 | 4.3131 | 0.0222 | 0.3608 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma795_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 1.8929 | 0.6733 | 4.0244 | 0.0206 | 0.3663 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma795_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.8817 | 0.6772 | 3.7299 | 0.0132 | 0.3386 | GATE_CAND | RAN |
| SOLUSDT | 4 | `wma795_below_at_h` | one_head_filter_pi_star | 210 | 17.1719 | 1.8218 | 0.6571 | 3.6564 | 0.0124 | 0.3190 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `wma795_above_at_h` | one_head_filter_pi_star | 161 | 13.2028 | 1.5104 | 0.6025 | 2.2292 | 0.0083 | 0.2981 | ok | RAN |
| SOLUSDT | 8 | `wma795_above_at_h` | one_head_filter_pi_star | 166 | 13.6128 | 1.5065 | 0.6084 | 2.2459 | 0.0082 | 0.2892 | ok | RAN |
| ETHUSDT | 4 | `wma795_above_at_h` | one_head_filter_pi_star | 160 | 13.1518 | 1.2178 | 0.5938 | 1.0553 | 0.0078 | 0.2250 | ok | RAN |
| ETHUSDT | 8 | `wma795_above_at_h` | one_head_filter_pi_star | 151 | 12.4607 | 1.1649 | 0.5960 | 0.8141 | 0.0060 | 0.2119 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma795_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma795_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma795_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma795_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma795_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma795_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
