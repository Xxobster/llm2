# Autonomy public-indicator hunt gen 528

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T194801Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma920_below_at_h` | one_head_filter_pi_star | 167 | 13.6424 | 2.4412 | 0.7246 | 4.9383 | 0.0278 | 0.3892 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma920_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.3612 | 0.7059 | 4.9784 | 0.0270 | 0.3797 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma920_above_at_h` | one_head_filter_pi_star | 115 | 9.4306 | 1.9263 | 0.6696 | 2.8376 | 0.0125 | 0.3043 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma920_below_at_h` | one_head_filter_pi_star | 234 | 19.1344 | 1.7495 | 0.6453 | 3.6396 | 0.0122 | 0.3077 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma920_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.6857 | 0.6493 | 3.2024 | 0.0113 | 0.3318 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma920_above_at_h` | one_head_filter_pi_star | 135 | 11.0080 | 1.7541 | 0.6370 | 2.6797 | 0.0107 | 0.2963 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma920_above_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.1261 | 0.5723 | 0.6508 | 0.0049 | 0.2023 | ok | RAN |
| ETHUSDT | 4 | `sma920_above_at_h` | one_head_filter_pi_star | 138 | 11.3434 | 1.0793 | 0.5580 | 0.3583 | 0.0030 | 0.2029 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma920_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4904 | 0.2778 | -1.0918 | -0.0549 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma920_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4581 | 0.2222 | -1.1942 | -0.0556 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma920_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma920_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma920_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
