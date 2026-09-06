# Autonomy public-indicator hunt gen 902

**Max readiness:** `LIVE_STOP / RESEARCH_ONLY`. Stamp `20260826T013909Z`. Arms: 27.
Gates: ebr≤0.35, tpm∈[4.0,40.0], n≥50, PF≥max(1.20, control).

| Symbol | H | Event | Mode | n | /mo | PF | WR | Sharpe | exp_i | ebr | flag | status |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| ETHUSDT | 8 | `wma470_below_at_h` | one_head_filter_pi_star | 194 | 15.8480 | 2.1147 | 0.7062 | 4.7930 | 0.0252 | 0.3918 | EBR>35% | RAN |
| ETHUSDT | 4 | `wma470_below_at_h` | one_head_filter_pi_star | 186 | 15.1945 | 1.9840 | 0.6935 | 4.4097 | 0.0234 | 0.3871 | EBR>35% | RAN |
| SOLUSDT | 4 | `wma470_below_at_h` | one_head_filter_pi_star | 181 | 14.8005 | 2.2004 | 0.6851 | 4.3537 | 0.0166 | 0.3812 | EBR>35% | RAN |
| SOLUSDT | 8 | `wma470_below_at_h` | one_head_filter_pi_star | 183 | 14.9641 | 2.1906 | 0.6940 | 4.3911 | 0.0165 | 0.3825 | EBR>35% | RAN |
| ETHUSDT | 4 | `control` | control | 384 | 31.2392 | 1.5469 | 0.6432 | 3.6395 | 0.0153 | 0.3021 | ok | RAN |
| SOLUSDT | 4 | `control` | control | 385 | 31.2622 | 1.6659 | 0.6364 | 4.2244 | 0.0100 | 0.3195 | ok | RAN |
| ETHUSDT | 8 | `wma470_above_at_h` | one_head_filter_pi_star | 187 | 15.4315 | 1.2017 | 0.5989 | 1.0563 | 0.0070 | 0.2139 | ok | RAN |
| SOLUSDT | 8 | `wma470_above_at_h` | one_head_filter_pi_star | 183 | 14.9219 | 1.4168 | 0.5956 | 2.0207 | 0.0064 | 0.2623 | ok | RAN |
| ETHUSDT | 4 | `wma470_above_at_h` | one_head_filter_pi_star | 191 | 15.7616 | 1.1748 | 0.5916 | 0.9611 | 0.0062 | 0.2094 | ok | RAN |
| SOLUSDT | 4 | `wma470_above_at_h` | one_head_filter_pi_star | 202 | 16.4712 | 1.3677 | 0.5990 | 1.8930 | 0.0059 | 0.2574 | ok | RAN |
| BTCUSDT | 4 | `control` | control | 28 | 2.3723 | 1.0150 | 0.4286 | 0.0327 | 0.0014 | 0.1429 | TPM<MIN | RAN |
| BTCUSDT | 4 | `wma470_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| BTCUSDT | 8 | `wma470_above_at_h` | one_head_filter_pi_star | 19 | 1.6169 | 0.5826 | 0.3158 | -0.8864 | -0.0434 | 0.0526 | TPM<MIN | RAN |
| ETHUSDT | 4 | `wma470_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 4 | `wma470_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma470_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| ETHUSDT | 8 | `wma470_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma470_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 4 | `wma470_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma470_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| SOLUSDT | 8 | `wma470_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma470_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 4 | `wma470_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 4 | `wma470_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma470_below_at_h` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW |
| BTCUSDT | 8 | `wma470_cross_up` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
| BTCUSDT | 8 | `wma470_cross_down` | one_head_filter_pi_star | 0 |  |  |  |  |  |  |  | TOO_FEW_GATED |
