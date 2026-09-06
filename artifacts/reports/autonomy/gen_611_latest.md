# Autonomy public-indicator hunt gen 611

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T011405Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma352_below_at_h` | one_head_filter_pi_star | 195 | 15.9297 | 2.0783 | 0.7026 | 4.6163 | 0.0243 | 0.3744 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma352_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9221 | 0.6898 | 4.2069 | 0.0222 | 0.3743 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma352_below_at_h` | one_head_filter_pi_star | 182 | 14.8823 | 2.1932 | 0.6868 | 4.4502 | 0.0163 | 0.3681 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma352_below_at_h` | one_head_filter_pi_star | 172 | 14.0646 | 1.9794 | 0.6686 | 3.7468 | 0.0146 | 0.3547 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma352_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2348 | 0.5979 | 1.2132 | 0.0083 | 0.2371 | ok | RAN |
| SOLUSDT | 8 | `sma352_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.5149 | 0.6031 | 2.4413 | 0.0077 | 0.2526 | ok | RAN |
| SOLUSDT | 4 | `sma352_above_at_h` | one_head_filter_pi_star | 197 | 16.0635 | 1.4992 | 0.6091 | 2.4128 | 0.0076 | 0.2640 | ok | RAN |
| ETHUSDT | 8 | `sma352_above_at_h` | one_head_filter_pi_star | 194 | 15.9466 | 1.2205 | 0.5928 | 1.1631 | 0.0074 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma352_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma352_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma352_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma352_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma352_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma352_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma352_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma352_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma352_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma352_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma352_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma352_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma352_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma352_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma352_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma352_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
