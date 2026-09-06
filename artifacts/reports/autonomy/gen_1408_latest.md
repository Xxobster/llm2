# Autonomy public-indicator hunt gen 1408

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260830T063741Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| BTCUSDT | 8 | `sma3120_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1230 | 0.2000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma3120_below_at_h` | one_head_filter_pi_star | 10 | 1.4001 | 3.0531 | 0.7000 | 1.7887 | 0.1088 | 0.2000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma3120_below_at_h` | one_head_filter_pi_star | 380 | 30.9137 | 1.6276 | 0.6500 | 4.0011 | 0.0171 | 0.3026 | GATE_CAND | RAN |
| ETHUSDT | 8 | `sma3120_below_at_h` | one_head_filter_pi_star | 379 | 30.8324 | 1.5845 | 0.6464 | 3.7676 | 0.0162 | 0.2982 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma3120_below_at_h` | one_head_filter_pi_star | 285 | 23.1853 | 1.8982 | 0.6561 | 4.5741 | 0.0135 | 0.3368 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma3120_below_at_h` | one_head_filter_pi_star | 297 | 24.1615 | 1.9013 | 0.6599 | 4.6667 | 0.0135 | 0.3266 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma3120_above_at_h` | one_head_filter_pi_star | 65 | 5.3312 | 1.6309 | 0.6000 | 1.5078 | 0.0081 | 0.1846 | ok | RAN |
| SOLUSDT | 4 | `sma3120_above_at_h` | one_head_filter_pi_star | 62 | 5.0968 | 1.5131 | 0.6129 | 1.2724 | 0.0068 | 0.1452 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma3120_above_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma3120_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma3120_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
