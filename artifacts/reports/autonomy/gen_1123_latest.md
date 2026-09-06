# Autonomy public-indicator hunt gen 1123

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T014557Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma615_below_at_h` | one_head_filter_pi_star | 202 | 16.5016 | 2.0095 | 0.6832 | 4.4246 | 0.0235 | 0.3663 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma615_below_at_h` | one_head_filter_pi_star | 197 | 16.0931 | 2.0486 | 0.6904 | 4.4242 | 0.0234 | 0.3756 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma615_below_at_h` | one_head_filter_pi_star | 196 | 16.0271 | 1.8585 | 0.6786 | 3.7229 | 0.0131 | 0.3367 | GATE_CAND | RAN |
| SOLUSDT | 8 | `sma615_below_at_h` | one_head_filter_pi_star | 205 | 16.7630 | 1.7843 | 0.6634 | 3.5459 | 0.0120 | 0.3268 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 4 | `sma615_above_at_h` | one_head_filter_pi_star | 143 | 11.7267 | 1.6354 | 0.6294 | 2.3817 | 0.0097 | 0.3217 | ok | RAN |
| SOLUSDT | 8 | `sma615_above_at_h` | one_head_filter_pi_star | 140 | 11.4807 | 1.6129 | 0.6286 | 2.3808 | 0.0096 | 0.3214 | ok | RAN |
| ETHUSDT | 4 | `sma615_above_at_h` | one_head_filter_pi_star | 182 | 14.9602 | 1.2238 | 0.6099 | 1.1648 | 0.0082 | 0.2143 | ok | RAN |
| ETHUSDT | 8 | `sma615_above_at_h` | one_head_filter_pi_star | 158 | 12.9874 | 1.1423 | 0.5949 | 0.7314 | 0.0053 | 0.2152 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma615_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma615_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma615_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma615_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma615_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma615_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
