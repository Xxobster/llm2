# Autonomy public-indicator hunt gen 696

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T065247Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1340_below_at_h` | one_head_filter_pi_star | 233 | 19.0340 | 1.8964 | 0.6695 | 4.1475 | 0.0210 | 0.3605 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1340_below_at_h` | one_head_filter_pi_star | 237 | 19.3607 | 1.8880 | 0.6709 | 4.1322 | 0.0207 | 0.3460 | GATE_CAND | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma1340_below_at_h` | one_head_filter_pi_star | 273 | 22.3234 | 1.8314 | 0.6520 | 4.2036 | 0.0127 | 0.3114 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1340_below_at_h` | one_head_filter_pi_star | 286 | 23.3865 | 1.7144 | 0.6329 | 3.8449 | 0.0113 | 0.3112 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma1340_above_at_h` | one_head_filter_pi_star | 78 | 6.4120 | 1.7351 | 0.6667 | 2.1059 | 0.0106 | 0.2949 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma1340_above_at_h` | one_head_filter_pi_star | 68 | 5.6526 | 1.4325 | 0.6471 | 1.3551 | 0.0073 | 0.3088 | ok | RAN |
| ETHUSDT | 4 | `sma1340_above_at_h` | one_head_filter_pi_star | 122 | 10.0685 | 1.0556 | 0.5656 | 0.2627 | 0.0023 | 0.2131 | ok | RAN |
| ETHUSDT | 8 | `sma1340_above_at_h` | one_head_filter_pi_star | 111 | 9.1607 | 1.0357 | 0.5495 | 0.1534 | 0.0014 | 0.2162 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1340_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.6169 | 0.2667 | -0.7191 | -0.0335 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma1340_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4993 | 0.3333 | -1.0668 | -0.0516 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1340_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1340_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1340_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
