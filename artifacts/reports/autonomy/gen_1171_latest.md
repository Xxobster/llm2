# Autonomy public-indicator hunt gen 1171

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T072512Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma623_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.1023 | 0.6915 | 4.5146 | 0.0244 | 0.3830 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma623_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0747 | 0.6939 | 4.5997 | 0.0243 | 0.3878 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma623_below_at_h` | one_head_filter_pi_star | 202 | 16.5177 | 1.7725 | 0.6634 | 3.4537 | 0.0121 | 0.3218 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma623_below_at_h` | one_head_filter_pi_star | 203 | 16.5995 | 1.7484 | 0.6601 | 3.2928 | 0.0116 | 0.3202 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma623_above_at_h` | one_head_filter_pi_star | 132 | 10.8247 | 1.5528 | 0.6212 | 2.0888 | 0.0086 | 0.3182 | ok | RAN |
| SOLUSDT | 4 | `sma623_above_at_h` | one_head_filter_pi_star | 144 | 11.8087 | 1.5128 | 0.6042 | 2.1111 | 0.0082 | 0.3125 | ok | RAN |
| ETHUSDT | 8 | `sma623_above_at_h` | one_head_filter_pi_star | 171 | 14.0560 | 1.1504 | 0.5965 | 0.7845 | 0.0056 | 0.2222 | ok | RAN |
| ETHUSDT | 4 | `sma623_above_at_h` | one_head_filter_pi_star | 163 | 13.3984 | 1.1428 | 0.5890 | 0.7252 | 0.0055 | 0.2147 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma623_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma623_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5765 | 0.2778 | -0.8994 | -0.0441 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma623_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma623_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma623_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma623_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma623_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma623_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma623_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma623_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma623_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma623_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma623_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma623_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma623_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma623_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
