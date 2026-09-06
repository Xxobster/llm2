# Autonomy public-indicator hunt gen 1083

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T205921Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma609_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.0799 | 0.6907 | 4.5265 | 0.0244 | 0.3969 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma609_below_at_h` | one_head_filter_pi_star | 198 | 16.1748 | 1.9462 | 0.6768 | 4.1754 | 0.0222 | 0.3687 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma609_below_at_h` | one_head_filter_pi_star | 220 | 17.9896 | 1.8727 | 0.6636 | 3.8988 | 0.0129 | 0.3091 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma609_below_at_h` | one_head_filter_pi_star | 194 | 15.8635 | 1.7477 | 0.6649 | 3.3610 | 0.0118 | 0.3351 | GATE_CAND | RAN |
| ETHUSDT | 4 | `sma609_above_at_h` | one_head_filter_pi_star | 146 | 12.0481 | 1.3104 | 0.6096 | 1.4036 | 0.0110 | 0.2123 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma609_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.6279 | 0.6242 | 2.4708 | 0.0096 | 0.3154 | ok | RAN |
| SOLUSDT | 8 | `sma609_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.5509 | 0.6200 | 2.3152 | 0.0086 | 0.3133 | ok | RAN |
| ETHUSDT | 8 | `sma609_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1762 | 0.5988 | 0.9251 | 0.0063 | 0.2093 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma609_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma609_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma609_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma609_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma609_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma609_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma609_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma609_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma609_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma609_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma609_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma609_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma609_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma609_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma609_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma609_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
