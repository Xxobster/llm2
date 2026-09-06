# Autonomy public-indicator hunt gen 1539

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260831T062735Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma679_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 2.1032 | 0.6834 | 4.7493 | 0.0248 | 0.3719 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma679_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 2.0157 | 0.6888 | 4.3965 | 0.0237 | 0.3724 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma679_below_at_h` | one_head_filter_pi_star | 200 | 16.3542 | 1.7793 | 0.6650 | 3.3522 | 0.0124 | 0.3350 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma679_below_at_h` | one_head_filter_pi_star | 203 | 16.5144 | 1.6031 | 0.6404 | 2.8277 | 0.0099 | 0.3103 | ok | RAN |
| SOLUSDT | 8 | `sma679_above_at_h` | one_head_filter_pi_star | 158 | 12.9568 | 1.5651 | 0.6203 | 2.3706 | 0.0091 | 0.3101 | ok | RAN |
| SOLUSDT | 4 | `sma679_above_at_h` | one_head_filter_pi_star | 162 | 13.2848 | 1.5365 | 0.6111 | 2.2972 | 0.0086 | 0.3025 | ok | RAN |
| ETHUSDT | 8 | `sma679_above_at_h` | one_head_filter_pi_star | 152 | 12.4942 | 1.1894 | 0.6053 | 0.8992 | 0.0068 | 0.2171 | ok | RAN |
| ETHUSDT | 4 | `sma679_above_at_h` | one_head_filter_pi_star | 144 | 11.8366 | 1.1478 | 0.6042 | 0.6974 | 0.0054 | 0.2083 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma679_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0418 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma679_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma679_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma679_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma679_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma679_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma679_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma679_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma679_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma679_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma679_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma679_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma679_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma679_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma679_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma679_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
