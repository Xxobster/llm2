# Autonomy public-indicator hunt gen 134

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260822T181651Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SOLUSDT | 8 | `wma50_cross_up` | one_head_filter_pi_star | 15 | 1.2824 | 16.8394 | 0.8000 | 3.0893 | 0.0686 | 0.3333 | TPM<MIN | RAN |
| ETHUSDT | 8 | `wma50_cross_down` | one_head_filter_pi_star | 18 | 1.5708 | 2.0075 | 0.6111 | 1.1922 | 0.0281 | 0.2222 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma50_below_at_h` | one_head_filter_pi_star | 221 | 18.0537 | 1.8489 | 0.6833 | 4.0789 | 0.0218 | 0.3710 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma50_below_at_h` | one_head_filter_pi_star | 220 | 17.9720 | 1.8433 | 0.6818 | 3.9782 | 0.0213 | 0.3773 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma50_below_at_h` | one_head_filter_pi_star | 163 | 13.3287 | 2.2172 | 0.6933 | 4.1611 | 0.0184 | 0.4233 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma50_below_at_h` | one_head_filter_pi_star | 161 | 13.1651 | 2.1405 | 0.6832 | 3.9468 | 0.0174 | 0.4161 | EBR>35% | RAN |
| ETHUSDT | 8 | `wma50_cross_up` | one_head_filter_pi_star | 14 | 1.1979 | 1.5276 | 0.6429 | 0.6901 | 0.0155 | 0.2857 | TPM<MIN | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 8 | `wma50_cross_down` | one_head_filter_pi_star | 14 | 1.3585 | 2.2132 | 0.7143 | 1.2304 | 0.0151 | 0.0714 | TPM<MIN | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma50_above_at_h` | one_head_filter_pi_star | 159 | 13.1209 | 1.1801 | 0.5912 | 0.8463 | 0.0056 | 0.2013 | ok | RAN |
| ETHUSDT | 8 | `wma50_above_at_h` | one_head_filter_pi_star | 163 | 13.4510 | 1.1718 | 0.5890 | 0.8115 | 0.0056 | 0.2025 | ok | RAN |
| SOLUSDT | 4 | `wma50_above_at_h` | one_head_filter_pi_star | 217 | 17.6943 | 1.3562 | 0.5991 | 1.9327 | 0.0052 | 0.2442 | ok | RAN |
| SOLUSDT | 8 | `wma50_above_at_h` | one_head_filter_pi_star | 216 | 17.6127 | 1.3533 | 0.5972 | 1.9172 | 0.0052 | 0.2454 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma50_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma50_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma50_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma50_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma50_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma50_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma50_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma50_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma50_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma50_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma50_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma50_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
