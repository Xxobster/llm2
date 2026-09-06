# Autonomy public-indicator hunt gen 699

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T070602Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma424_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9899 | 0.6963 | 4.4469 | 0.0232 | 0.3822 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma424_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9075 | 0.6882 | 4.1265 | 0.0221 | 0.3871 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma424_below_at_h` | one_head_filter_pi_star | 180 | 14.7188 | 1.9798 | 0.6833 | 3.9272 | 0.0143 | 0.3722 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma424_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 1.8692 | 0.6685 | 3.6257 | 0.0130 | 0.3652 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `sma424_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2590 | 0.5968 | 1.2882 | 0.0093 | 0.2312 | ok | RAN |
| SOLUSDT | 8 | `sma424_above_at_h` | one_head_filter_pi_star | 193 | 15.7373 | 1.4775 | 0.6114 | 2.3261 | 0.0075 | 0.2642 | ok | RAN |
| SOLUSDT | 4 | `sma424_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.4610 | 0.5990 | 2.2009 | 0.0074 | 0.2760 | ok | RAN |
| ETHUSDT | 4 | `sma424_above_at_h` | one_head_filter_pi_star | 185 | 15.2068 | 1.1984 | 0.5838 | 1.0530 | 0.0071 | 0.2216 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma424_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma424_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0443 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma424_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma424_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma424_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma424_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
