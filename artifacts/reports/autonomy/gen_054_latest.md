# Autonomy public-indicator hunt gen 054

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T130556Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `trrel_low_at_h` | one_head_filter_pi_star | 54 | 4.7647 | 4.1950 | 0.7963 | 4.1126 | 0.0564 | 0.4444 | EBR>35% | RAN |
| ETHUSDT | 4 | `trrel_cross_up_1` | one_head_filter_pi_star | 16 | 1.3908 | 2.9591 | 0.6250 | 1.8040 | 0.0355 | 0.3750 | EBR>35% | RAN |
| SOLUSDT | 8 | `trrel_low_at_h` | one_head_filter_pi_star | 28 | 2.5480 | 3.1934 | 0.7500 | 2.7265 | 0.0273 | 0.6071 | EBR>35% | RAN |
| ETHUSDT | 8 | `trrel_cross_up_1` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 8 | `trrel_cross_down_1` | one_head_filter_pi_star | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 4 | `trrel_cross_down_1` | one_head_filter_pi_star | 363 | 29.5308 | 1.5121 | 0.6391 | 3.4489 | 0.0145 | 0.2975 | ok | RAN |
| SOLUSDT | 8 | `trrel_cross_down_1` | one_head_filter_pi_star | 382 | 31.0765 | 1.6890 | 0.6387 | 4.3279 | 0.0102 | 0.3194 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `trrel_cross_up_1` | one_head_filter_pi_star | 359 | 29.2054 | 1.6119 | 0.6295 | 3.7753 | 0.0091 | 0.2953 | ok | RAN |
| SOLUSDT | 4 | `trrel_cross_down_1` | one_head_filter_pi_star | 338 | 27.4970 | 1.5285 | 0.6243 | 3.3039 | 0.0082 | 0.2988 | ok | RAN |
| BTCUSDT | 8 | `trrel_cross_up_1` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0068 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 8 | `trrel_cross_down_1` | one_head_filter_pi_star | 27 | 2.2976 | 1.0729 | 0.4444 | 0.1508 | 0.0065 | 0.1481 | TPM<MIN | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| SOLUSDT | 4 | `trrel_cross_up_1` | one_head_filter_pi_star | 26 | 2.1423 | 0.8293 | 0.5000 | -0.4024 | -0.0025 | 0.0385 | TPM<MIN | RAN |
| BTCUSDT | 4 | `trrel_high_at_h` | one_head_filter_pi_star | 14 | 1.1914 | 0.4733 | 0.3571 | -1.1052 | -0.0373 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `trrel_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| ETHUSDT | 4 | `trrel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `trrel_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `trrel_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `trrel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `trrel_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `trrel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `trrel_cross_up_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `trrel_cross_down_1` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `trrel_high_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `trrel_low_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
