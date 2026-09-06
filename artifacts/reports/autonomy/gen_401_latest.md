# Autonomy public-indicator hunt gen 401

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T022932Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `ema560_below_at_h` | one_head_filter_pi_star | 201 | 16.4199 | 2.1365 | 0.6915 | 4.7359 | 0.0254 | 0.3881 | EBR>35% | RAN |
| ETHUSDT | 8 | `ema560_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0131 | 0.6733 | 4.3789 | 0.0232 | 0.3762 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `ema560_below_at_h` | one_head_filter_pi_star | 211 | 17.2537 | 1.9351 | 0.6682 | 3.9927 | 0.0137 | 0.3318 | GATE_CAND | RAN |
| SOLUSDT | 8 | `ema560_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.9177 | 0.6634 | 3.8769 | 0.0135 | 0.3317 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `ema560_above_at_h` | one_head_filter_pi_star | 170 | 13.9408 | 1.5850 | 0.6118 | 2.5194 | 0.0091 | 0.2882 | ok | RAN |
| SOLUSDT | 8 | `ema560_above_at_h` | one_head_filter_pi_star | 143 | 11.6603 | 1.5178 | 0.6014 | 2.1296 | 0.0083 | 0.3077 | ok | RAN |
| ETHUSDT | 8 | `ema560_above_at_h` | one_head_filter_pi_star | 157 | 12.9052 | 1.1906 | 0.6115 | 0.9225 | 0.0069 | 0.2038 | ok | RAN |
| ETHUSDT | 4 | `ema560_above_at_h` | one_head_filter_pi_star | 172 | 14.1382 | 1.1093 | 0.5814 | 0.5760 | 0.0041 | 0.2035 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `ema560_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `ema560_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `ema560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `ema560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `ema560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `ema560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `ema560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `ema560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `ema560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema560_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `ema560_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `ema560_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
