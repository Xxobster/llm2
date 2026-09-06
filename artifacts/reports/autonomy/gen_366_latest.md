# Autonomy public-indicator hunt gen 366

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T181115Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma135_below_at_h` | one_head_filter_pi_star | 205 | 16.7466 | 1.8415 | 0.6829 | 4.1097 | 0.0211 | 0.3610 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma135_below_at_h` | one_head_filter_pi_star | 199 | 16.2565 | 1.7906 | 0.6734 | 3.8803 | 0.0201 | 0.3668 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma135_below_at_h` | one_head_filter_pi_star | 168 | 13.7375 | 2.2793 | 0.6964 | 4.3570 | 0.0188 | 0.4048 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma135_below_at_h` | one_head_filter_pi_star | 164 | 13.4104 | 2.2245 | 0.6890 | 4.2042 | 0.0180 | 0.3963 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| ETHUSDT | 8 | `wma135_above_at_h` | one_head_filter_pi_star | 173 | 14.2204 | 1.3719 | 0.6185 | 1.6556 | 0.0111 | 0.2254 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma135_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2478 | 0.6022 | 1.2160 | 0.0081 | 0.2210 | ok | RAN |
| SOLUSDT | 8 | `wma135_above_at_h` | one_head_filter_pi_star | 210 | 17.1235 | 1.3116 | 0.5905 | 1.6567 | 0.0047 | 0.2571 | ok | RAN |
| SOLUSDT | 4 | `wma135_above_at_h` | one_head_filter_pi_star | 206 | 16.7973 | 1.2661 | 0.5825 | 1.4487 | 0.0041 | 0.2524 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma135_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma135_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 4 | `wma135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| SOLUSDT | 8 | `wma135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma135_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma135_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma135_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma135_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
