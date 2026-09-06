# Autonomy public-indicator hunt gen 475

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260824T161700Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma238_below_at_h` | one_head_filter_pi_star | 187 | 15.2762 | 1.9536 | 0.6898 | 4.3592 | 0.0233 | 0.3850 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma238_below_at_h` | one_head_filter_pi_star | 189 | 15.4396 | 1.9507 | 0.6878 | 4.2862 | 0.0227 | 0.3862 | EBR>35% | RAN |
| SOLUSDT | 4 | `sma238_below_at_h` | one_head_filter_pi_star | 166 | 13.5740 | 2.1395 | 0.6867 | 3.9988 | 0.0165 | 0.3795 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma238_below_at_h` | one_head_filter_pi_star | 171 | 13.9828 | 2.1427 | 0.6842 | 4.0569 | 0.0161 | 0.3684 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `sma238_above_at_h` | one_head_filter_pi_star | 197 | 16.1931 | 1.2687 | 0.6091 | 1.4334 | 0.0090 | 0.2234 | ok | RAN |
| ETHUSDT | 8 | `sma238_above_at_h` | one_head_filter_pi_star | 195 | 16.0917 | 1.2120 | 0.5949 | 1.1564 | 0.0073 | 0.2205 | ok | RAN |
| SOLUSDT | 4 | `sma238_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.4376 | 0.6031 | 2.1319 | 0.0066 | 0.2680 | ok | RAN |
| SOLUSDT | 8 | `sma238_above_at_h` | one_head_filter_pi_star | 208 | 16.9604 | 1.4048 | 0.6010 | 2.0711 | 0.0063 | 0.2644 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma238_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma238_above_at_h` | one_head_filter_pi_star | 18 | 1.5318 | 0.5834 | 0.3333 | -0.8834 | -0.0450 | 0.0556 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma238_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma238_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma238_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma238_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma238_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma238_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma238_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma238_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma238_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma238_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma238_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma238_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma238_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma238_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
