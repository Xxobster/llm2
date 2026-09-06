# Autonomy public-indicator hunt gen 838

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260825T191559Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma430_below_at_h` | one_head_filter_pi_star | 191 | 15.6030 | 1.9924 | 0.6963 | 4.4203 | 0.0236 | 0.3874 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma430_below_at_h` | one_head_filter_pi_star | 196 | 16.0114 | 1.9551 | 0.6990 | 4.3755 | 0.0230 | 0.3878 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma430_below_at_h` | one_head_filter_pi_star | 178 | 14.5552 | 2.2377 | 0.6854 | 4.4622 | 0.0172 | 0.3876 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma430_below_at_h` | one_head_filter_pi_star | 177 | 14.4734 | 2.1751 | 0.6949 | 4.2675 | 0.0164 | 0.3785 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 4 | `wma430_above_at_h` | one_head_filter_pi_star | 190 | 15.6178 | 1.2784 | 0.6053 | 1.4238 | 0.0094 | 0.2211 | ok | RAN |
| ETHUSDT | 8 | `wma430_above_at_h` | one_head_filter_pi_star | 189 | 15.5356 | 1.2733 | 0.6032 | 1.3977 | 0.0093 | 0.2275 | ok | RAN |
| SOLUSDT | 8 | `wma430_above_at_h` | one_head_filter_pi_star | 192 | 15.6558 | 1.3472 | 0.5938 | 1.7817 | 0.0057 | 0.2604 | ok | RAN |
| SOLUSDT | 4 | `wma430_above_at_h` | one_head_filter_pi_star | 194 | 15.8188 | 1.3052 | 0.5876 | 1.5888 | 0.0050 | 0.2629 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma430_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma430_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma430_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma430_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma430_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma430_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
