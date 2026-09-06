# Autonomy public-indicator hunt gen 899

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T012110Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma588_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 1.9961 | 0.6821 | 4.3496 | 0.0231 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma588_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.9353 | 0.6834 | 4.1698 | 0.0222 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma588_below_at_h` | one_head_filter_pi_star | 195 | 15.9453 | 1.8757 | 0.6821 | 3.7387 | 0.0131 | 0.3436 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma588_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.7836 | 0.6633 | 3.4724 | 0.0122 | 0.3367 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma588_above_at_h` | one_head_filter_pi_star | 171 | 14.1112 | 1.2407 | 0.6082 | 1.2254 | 0.0088 | 0.2222 | ok | RAN |
| SOLUSDT | 4 | `sma588_above_at_h` | one_head_filter_pi_star | 148 | 12.1367 | 1.5588 | 0.6216 | 2.2205 | 0.0088 | 0.3108 | ok | RAN |
| ETHUSDT | 4 | `sma588_above_at_h` | one_head_filter_pi_star | 187 | 15.3712 | 1.2057 | 0.5989 | 1.0827 | 0.0074 | 0.2032 | ok | RAN |
| SOLUSDT | 8 | `sma588_above_at_h` | one_head_filter_pi_star | 154 | 12.6288 | 1.4455 | 0.6039 | 1.9732 | 0.0074 | 0.3052 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma588_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma588_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma588_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma588_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma588_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma588_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma588_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma588_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma588_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma588_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma588_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma588_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma588_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma588_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma588_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma588_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
