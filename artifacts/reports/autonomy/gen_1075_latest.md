# Autonomy public-indicator hunt gen 1075

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260828T195159Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma608_below_at_h` | one_head_filter_pi_star | 177 | 14.4593 | 2.1322 | 0.6893 | 4.5243 | 0.0252 | 0.4124 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma608_below_at_h` | one_head_filter_pi_star | 213 | 17.4002 | 1.9781 | 0.6761 | 4.3782 | 0.0224 | 0.3521 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma608_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.8131 | 0.6634 | 3.5700 | 0.0120 | 0.3171 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma608_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7579 | 0.6600 | 3.4013 | 0.0116 | 0.3250 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma608_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5867 | 0.6081 | 2.3841 | 0.0091 | 0.3176 | ok | RAN |
| SOLUSDT | 4 | `sma608_above_at_h` | one_head_filter_pi_star | 149 | 12.2187 | 1.5735 | 0.6174 | 2.2765 | 0.0089 | 0.3221 | ok | RAN |
| ETHUSDT | 8 | `sma608_above_at_h` | one_head_filter_pi_star | 147 | 12.0832 | 1.2063 | 0.6054 | 0.9679 | 0.0077 | 0.2245 | ok | RAN |
| ETHUSDT | 4 | `sma608_above_at_h` | one_head_filter_pi_star | 176 | 14.4670 | 1.1647 | 0.5966 | 0.8542 | 0.0060 | 0.2102 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma608_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma608_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma608_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma608_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma608_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma608_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma608_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma608_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma608_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma608_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma608_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma608_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma608_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma608_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma608_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma608_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
