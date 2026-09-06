# Autonomy public-indicator hunt gen 328

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260823T113029Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 4 | `sma420_below_at_h` | one_head_filter_pi_star | 188 | 15.3579 | 2.0764 | 0.7021 | 4.6421 | 0.0248 | 0.3883 | EBR>35% | RAN |
| ETHUSDT | 8 | `sma420_below_at_h` | one_head_filter_pi_star | 183 | 14.9494 | 2.0618 | 0.6995 | 4.5318 | 0.0245 | 0.3989 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `sma420_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 1.9991 | 0.6776 | 3.9424 | 0.0143 | 0.3716 | EBR>35% | RAN |
| SOLUSDT | 8 | `sma420_below_at_h` | one_head_filter_pi_star | 188 | 15.3729 | 1.8109 | 0.6543 | 3.5333 | 0.0124 | 0.3670 | EBR>35% | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| SOLUSDT | 8 | `sma420_above_at_h` | one_head_filter_pi_star | 184 | 15.0034 | 1.5863 | 0.6141 | 2.6444 | 0.0091 | 0.2609 | ok | RAN |
| ETHUSDT | 4 | `sma420_above_at_h` | one_head_filter_pi_star | 186 | 15.2890 | 1.2658 | 0.5968 | 1.3473 | 0.0091 | 0.2258 | ok | RAN |
| ETHUSDT | 8 | `sma420_above_at_h` | one_head_filter_pi_star | 181 | 14.8780 | 1.2222 | 0.5912 | 1.1120 | 0.0080 | 0.2155 | ok | RAN |
| SOLUSDT | 4 | `sma420_above_at_h` | one_head_filter_pi_star | 195 | 15.9004 | 1.4074 | 0.5949 | 1.9821 | 0.0066 | 0.2667 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `sma420_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0426 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `sma420_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `sma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `sma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `sma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `sma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `sma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `sma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `sma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma420_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `sma420_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `sma420_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
