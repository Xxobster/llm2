# Autonomy public-indicator hunt gen 1307

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260829T210227Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma645_below_at_h` | one_head_filter_pi_star | 180 | 14.7044 | 1.9691 | 0.6778 | 3.9906 | 0.0228 | 0.4000 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma645_below_at_h` | one_head_filter_pi_star | 190 | 15.5213 | 1.9815 | 0.6789 | 4.1724 | 0.0227 | 0.3789 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma645_below_at_h` | one_head_filter_pi_star | 189 | 15.4547 | 1.7747 | 0.6667 | 3.3455 | 0.0123 | 0.3333 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma645_below_at_h` | one_head_filter_pi_star | 197 | 16.1089 | 1.7823 | 0.6650 | 3.3755 | 0.0121 | 0.3299 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma645_above_at_h` | one_head_filter_pi_star | 139 | 11.3987 | 1.5765 | 0.6187 | 2.2883 | 0.0091 | 0.3381 | ok | RAN |
| ETHUSDT | 8 | `sma645_above_at_h` | one_head_filter_pi_star | 153 | 12.5764 | 1.2250 | 0.6144 | 1.0855 | 0.0083 | 0.2092 | ok | RAN |
| SOLUSDT | 4 | `sma645_above_at_h` | one_head_filter_pi_star | 150 | 12.3007 | 1.4752 | 0.6067 | 1.9991 | 0.0077 | 0.3067 | ok | RAN |
| ETHUSDT | 4 | `sma645_above_at_h` | one_head_filter_pi_star | 164 | 13.4806 | 1.1575 | 0.5854 | 0.8108 | 0.0059 | 0.2134 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma645_above_at_h` | one_head_filter_pi_star | 20 | 1.7020 | 0.5795 | 0.3000 | -0.8976 | -0.0424 | 0.0500 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma645_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma645_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma645_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma645_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma645_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
