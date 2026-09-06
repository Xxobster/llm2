# Autonomy public-indicator hunt gen 774

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T130830Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `wma390_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9356 | 0.6882 | 4.2730 | 0.0223 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma390_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 1.8997 | 0.6862 | 4.0904 | 0.0218 | 0.3777 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma390_below_at_h` | one_head_filter_pi_star | 169 | 13.8193 | 2.1478 | 0.6864 | 4.0845 | 0.0165 | 0.3846 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma390_below_at_h` | one_head_filter_pi_star | 165 | 13.4922 | 2.1335 | 0.6909 | 3.9661 | 0.0162 | 0.3697 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma390_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.2711 | 0.6000 | 1.3867 | 0.0092 | 0.2216 | ok | RAN |
| SOLUSDT | 8 | `wma390_above_at_h` | one_head_filter_pi_star | 200 | 16.3081 | 1.4295 | 0.6000 | 2.1701 | 0.0066 | 0.2500 | ok | RAN |
| ETHUSDT | 8 | `wma390_above_at_h` | one_head_filter_pi_star | 175 | 14.3848 | 1.1868 | 0.5943 | 0.9555 | 0.0065 | 0.2171 | ok | RAN |
| SOLUSDT | 4 | `wma390_above_at_h` | one_head_filter_pi_star | 191 | 15.5742 | 1.4076 | 0.6021 | 2.0262 | 0.0063 | 0.2670 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma390_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma390_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma390_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma390_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma390_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma390_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma390_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma390_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma390_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma390_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma390_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma390_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma390_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma390_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma390_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma390_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
