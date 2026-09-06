# Autonomy public-indicator hunt gen 680

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T054545Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `sma1300_below_at_h` | one_head_filter_pi_star | 225 | 18.3804 | 1.8403 | 0.6711 | 3.8922 | 0.0203 | 0.3556 | EBR>35% | RAN |
| ETHUSDT | 4 | `sma1300_below_at_h` | one_head_filter_pi_star | 234 | 19.1157 | 1.8404 | 0.6752 | 4.0797 | 0.0200 | 0.3504 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `sma1300_below_at_h` | one_head_filter_pi_star | 284 | 23.2229 | 1.8635 | 0.6444 | 4.3903 | 0.0129 | 0.3099 | GATE_CAND | RAN |
| SOLUSDT | 4 | `sma1300_below_at_h` | one_head_filter_pi_star | 296 | 24.2042 | 1.6886 | 0.6318 | 3.7904 | 0.0109 | 0.3108 | GATE_CAND | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma1300_above_at_h` | one_head_filter_pi_star | 75 | 6.1166 | 1.6477 | 0.6533 | 1.8547 | 0.0098 | 0.3067 | ok | RAN |
| SOLUSDT | 4 | `sma1300_above_at_h` | one_head_filter_pi_star | 66 | 5.4247 | 1.4896 | 0.6515 | 1.4618 | 0.0077 | 0.2424 | ok | RAN |
| ETHUSDT | 8 | `sma1300_above_at_h` | one_head_filter_pi_star | 99 | 8.1703 | 1.1756 | 0.5859 | 0.6931 | 0.0069 | 0.2020 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1300_above_at_h` | one_head_filter_pi_star | 126 | 10.3986 | 0.9930 | 0.5476 | -0.0337 | -0.0003 | 0.1984 | ok | RAN |
| BTCUSDT | 4 | `sma1300_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.4666 | 0.2778 | -1.1692 | -0.0613 | 0.0000 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma1300_above_at_h` | one_head_filter_pi_star | 15 | 1.2765 | 0.3384 | 0.2667 | -1.4922 | -0.0722 | 0.0000 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1300_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma1300_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma1300_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
