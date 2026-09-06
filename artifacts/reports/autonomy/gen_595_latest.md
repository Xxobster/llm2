# Autonomy public-indicator hunt gen 595

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T001319Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma334_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 2.1084 | 0.7059 | 4.7476 | 0.0256 | 0.3957 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma334_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9397 | 0.6828 | 4.2299 | 0.0229 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma334_below_at_h` | one_head_filter_pi_star | 175 | 14.3099 | 2.1267 | 0.6800 | 4.1302 | 0.0162 | 0.3771 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma334_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1241 | 0.6784 | 4.0721 | 0.0161 | 0.3743 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma334_above_at_h` | one_head_filter_pi_star | 193 | 15.8644 | 1.2428 | 0.5959 | 1.2718 | 0.0086 | 0.2228 | ok | RAN |
| ETHUSDT | 8 | `sma334_above_at_h` | one_head_filter_pi_star | 191 | 15.7000 | 1.2230 | 0.5969 | 1.1828 | 0.0077 | 0.2199 | ok | RAN |
| SOLUSDT | 8 | `sma334_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.4784 | 0.6033 | 2.2472 | 0.0075 | 0.2663 | ok | RAN |
| SOLUSDT | 4 | `sma334_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4384 | 0.6114 | 2.1534 | 0.0068 | 0.2642 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma334_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma334_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma334_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma334_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma334_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma334_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma334_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma334_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma334_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma334_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma334_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma334_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma334_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma334_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma334_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma334_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
